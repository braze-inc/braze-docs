## Comprendre le flux de travail du Braze/APN

Le service Apple Push Notification (APN) est l'infrastructure permettant d'envoyer des notifications push aux applications fonctionnant sur les plateformes d'Apple. Voici la structure simplifiée de la manière dont les notifications push sont activées pour les appareils de vos utilisateurs et la façon dont Braze peut leur envoyer des notifications push :

1. Vous configurez le certificat push et le profil de provisionnement
2. Les appareils s’enregistrent pour les APN et fournissent à Braze des jetons de notification push
3. Vous lancez une campagne de notifications push Braze
4. Braze supprime les jetons non valides

### Étape 1 : Configurer le certificat push et le profil de provisionnement

Lors du développement de votre application, vous devez créer un certificat SSL pour activer les notifications push. Ce certificat sera inclus dans le profil de provisionnement avec lequel votre application est créée et devra également être téléchargé sur le tableau de bord de Braze. Le certificat permet à Braze de communiquer aux APN que nous sommes autorisés à envoyer des notifications push en votre nom.

Il existe deux types de [profils de provisionnement](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html) et de certificats : le développement et la distribution. Nous vous recommandons d’utiliser uniquement des profils de distribution et des certificats pour éviter toute confusion. Si vous choisissez d’utiliser différents profils et certificats pour le développement et la distribution, assurez-vous que le certificat téléchargé sur le tableau de bord correspond au profil de provisionnement que vous utilisez actuellement.

{% alert warning %}
Ne modifiez pas l’environnement de certificat push (développement par rapport à la production). La modification du certificat de notification push pour un environnement incorrect peut entraîner la suppression accidentelle de son jeton de notification push, ce qui le rend inaccessible par la notification push.
{% endalert %}

### Étape 2 : Les appareils s’enregistrent pour les APN et fournissent à Braze des jetons de notification push

Lorsque les utilisateurs ouvrent votre application, ils sont invités à accepter les notifications push. S’ils acceptent cette invite, les APN généreront un jeton de notification push pour cet appareil particulier. Le SDK Swift enverra immédiatement et de manière asynchrone le jeton push pour les apps utilisant la [politique de rinçage automatique]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/fine_network_traffic_control/#automatic-request-processing) par défaut. Une fois que nous aurons associé un jeton push à un utilisateur, il apparaîtra comme "Enregistré Push" dans le tableau de bord de son profil utilisateur sous l'onglet **Engagement** et sera éligible pour recevoir des notifications push des campagnes Braze.

{% alert note %}
À partir de macOS 13, sur certains appareils, vous pouvez tester les notifications push sur un simulateur iOS 16 fonctionnant sous Xcode 14. Pour plus de détails, reportez-vous aux [notes de version de Xcode 14](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes).
{% endalert %}

#### Considérations relatives à la génération de jetons push

- Si les utilisateurs installent votre app sur un autre appareil, un autre jeton sera créé et capturé de la même manière. 
- Si les utilisateurs réinstallent votre app, un nouveau jeton sera généré et transmis à Braze. Cependant, le jeton d'origine peut toujours être considéré comme valide par les APN et Braze.
- Si les utilisateurs désinstallent votre application, Braze n'en est pas immédiatement informé et le jeton apparaîtra toujours comme valide jusqu'à ce qu'il soit retiré par les APN. 
- À un moment donné, les APN retireront les anciens jetons. Braze n'en a ni le contrôle ni la visibilité. 

### Étape 3 : Lancer une campagne de notifications push Braze

Lorsqu’une campagne de notifications push est lancée, Braze effectuera des demandes aux APN pour délivrer votre message. Plus précisément, les demandes sont transmises aux APN pour chaque jeton de poussée en cours de validité, sauf si l'option **Envoyer à l'appareil le plus récent de l'utilisateur** est sélectionnée. Une fois que Braze a reçu une réponse positive des APN, nous enregistrons une réception/distribution réussie dans le profil de l'utilisateur, bien que l'utilisateur puisse ne pas avoir reçu le message pour diverses raisons :
- Leur appareil est hors tension.
- Leur appareil n'est pas connecté à l'internet (Wi-Fi ou cellulaire).
- Ils ont récemment désinstallé l'application.

Braze utilisera le certificat push SSL téléchargé dans le tableau de bord pour authentifier et vérifier que nous sommes autorisés à envoyer des notifications push aux jetons de notification push fournis. Si un appareil est en ligne, la notification devrait être reçue peu de temps après l’envoi de la campagne. Notez que Braze fixe à 30 jours la [date d'expiration](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607) par défaut des APN pour les notifications.

### Étape 4 : Supprimer les jetons non valides

Si l ['APN](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) nous informe que l'un des jetons push auxquels nous avons tenté d'envoyer un message n'est pas valide, nous supprimons ces jetons des profils utilisateurs auxquels ils étaient associés.

{% alert note %}
Il est normal que les APN renvoient initialement un statut de réussite même si un jeton n'est plus enregistré, car les APN ne signalent pas immédiatement les événements d'invalidation des jetons. Les APN retardent intentionnellement le renvoi de l'état `410` pour les jetons non valides selon une planification aléatoire, conçue pour protéger la vie privée des utilisateurs et empêcher le suivi des désinstallations d'applications. Vous pouvez continuer à envoyer des notifications à un jeton non enregistré jusqu'à ce que l'APN renvoie le statut `410`.
{% endalert %}

## Utilisation des journaux d'erreurs de push

Le [journal d'activité des messages]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) vous donne la possibilité de voir tous les messages (en particulier les messages d'erreur) associés à vos campagnes et à vos envois, y compris les erreurs de notification push. Ce journal d’erreurs fournit de nombreux avertissements qui peuvent être très utiles pour identifier les raisons pour lesquelles vos campagnes ne fonctionnent pas comme prévu. Cliquer sur un message d’erreur vous redirigera vers la documentation pertinente pour vous aider à résoudre un incident particulier.

![Les journaux d'erreurs en mode push affichent l'heure à laquelle l'erreur s'est produite, le nom de l'application, le canal, le type d'erreur et le message d'erreur.]({% image_buster /assets/img_archive/message_activity_log.png %})

Les erreurs courantes que vous pouvez voir ici comprennent des notifications spécifiques à l'utilisateur, telles que ["Received Unregistered Sending to Push Token".](#swift_received-unregistered-sending)

En outre, Braze fournit également un journal des modifications en mode push sur le profil utilisateur, sous l'onglet **Engagement.**  Ce journal des modifications donne un aperçu du comportement d’enregistrement des notifications push, comme l’invalidation des jetons, les erreurs d’enregistrement push, les jetons déplacés vers de nouveaux utilisateurs, etc.

![]({% image_buster /assets/img_archive/push_changelog.gif %}){: style="max-width:50%;" }

### Erreurs du journal des activités liées aux messages

#### Réception d’un envoi non enregistré au jeton de notification push {#received-unregistered-sending}

- Assurez-vous que le jeton de commande est envoyé à Braze à partir de la méthode `AppDelegate.braze?.notifications.register(deviceToken:)` est valide. Vous pouvez consulter le **journal des activités liées aux messages** pour voir le jeton de notification push. Il devrait ressembler à quelque chose comme `6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6`, une longue chaîne de caractères contenant un mélange de lettres et de chiffres. Si votre jeton de poussée semble différent, vérifiez votre [code]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-4-register-push-tokens-with-braze) d'envoi des jetons de poussée à Braze.
- Vérifiez que votre profil de provisionnement de notification push correspond à l’environnement dans lequel vous effectuez des tests. Les certificats universels peuvent être configurés dans le tableau de bord de Braze pour envoyer vers l’environnement de développement ou de production APN. L’utilisation d’un certificat de développement pour une application de production ou d’un certificat de production pour une application de développement ne fonctionnera pas.
 - Vérifiez que le jeton de notification push que vous avez téléchargé sur Braze correspond au profil de provisionnement que vous avez utilisé pour créer l’application à partir de laquelle vous avez envoyé le jeton de notification push.

#### Jeton d'appareil non destiné à la rubrique

Cette erreur indique que le certificat push et l’ID de lot (bundle ID) de votre application ne correspondent pas. Vérifiez que le certificat de notification push que vous avez téléchargé sur Braze correspond au profil de provisionnement que vous avez utilisé pour créer l’application à partir de laquelle vous avez envoyé le jeton de notification push.

#### BadDeviceToken envoyant au jeton de notification push

Le `BadDeviceToken` est un code d’erreur APN et ne provient pas de Braze. Cette réponse peut être renvoyée pour plusieurs raisons, notamment :

- L’application a reçu un jeton de notification push qui n’était pas valide pour les informations d’identification téléchargées sur le tableau de bord.
- La fonction "Push" a été désactivée pour cet espace de travail.
- L’utilisateur s’est désinscrit des notifications push.
- L’application a été désinstallée.
- Apple a actualisé le jeton de notification push, ce qui a invalidé l’ancien jeton.
- L’application a été conçue pour un environnement de production, mais les informations d’identification des notifications push téléchargées sur Braze sont définies pour un environnement de développement (ou l’inverse).

## Problèmes d’enregistrement de notifications push

### Pas d’invite d’enregistrement push

Si l’application ne vous invite pas à vous inscrire aux notifications push, il y a probablement un problème avec votre intégration d’inscription push. Assurez-vous d'avoir suivi notre [documentation]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) et d'avoir correctement intégré notre enregistrement push. Vous pouvez également définir des points d’arrêt dans votre code pour vous assurer que le code d’inscription de notification push est en cours d’exécution.

### Aucun utilisateur "enregistré en push" n'apparaît dans le tableau de bord (avant l'envoi des messages)

Assurez-vous que votre application est correctement configurée pour autoriser les notifications push. Les points de défaillance fréquents à vérifier comprennent :

- Vérifiez que votre application vous invite à autoriser les notifications push. En général, cette invite apparaîtra lors de votre première ouverture de l’application, mais elle peut être programmée pour apparaître ailleurs. Si elle n’apparaît pas là où elle le devrait, le problème est probablement la configuration de base des capacités de notification push de votre application.
  - Vérifiez que les étapes de l'[intégration push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) ont été effectuées avec succès.
  - Vérifiez que le profil de provisionnement de votre application a été créé avec des autorisations pour les notifications push. Assurez-vous de retirer tous les profils de provisionnement disponibles depuis votre compte développeur Apple. Pour confirmer cela, procédez comme suit :
    1. Dans Xcode, sélectionnez **Préférences > Comptes** (ou utilisez le raccourci clavier <kbd>Command</kbd>+<kbd>,</kbd>).
    2. Sélectionnez l’ID Apple que vous utilisez pour votre compte développeur et cliquez sur **Afficher les détails**.
    3. Sur la page suivante, cliquez sur **<i class="fas fa-redo-alt"></i> Actualiser** et confirmez que vous tirez tous les profils de provisionnement disponibles.
- Vérifiez que vous avez [bien activé la fonction "push"]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-2-enable-push-capabilities) dans votre application.
- Vérifiez que votre profil de provisionnement de notification push correspond à l’environnement dans lequel vous effectuez des tests. Les certificats universels peuvent être configurés dans le tableau de bord de Braze pour envoyer vers l’environnement de développement ou de production APN. L’utilisation d’un certificat de développement pour une application de production ou d’un certificat de production pour une application de développement ne fonctionnera pas.
- Vérifiez que vous utilisez `registerPushToken` en définissant un point de rupture dans votre code.
- Assurez-vous que vous testez à l'aide d'un appareil (push ne fonctionnera pas sur un simulateur) et que vous disposez d'une bonne connectivité réseau.

## Notifications push envoyées mais non affichées sur les appareils des utilisateurs.

### Les utilisateurs « Push Registered » (Enregistré pour les notifications push) ne sont plus activés après l’envoi de messages

Ceci indique probablement que l'utilisateur avait un jeton de notification push non valide. Cela peut se produire pour plusieurs raisons :

#### Pas de correspondance du tableau de bord et du certificat d’application

Si le certificat de notification push que vous avez téléchargé dans le tableau de bord n’est pas le même dans le profil de provisionnement avec lequel votre application a été créée , les APN rejetteront le jeton. Vérifiez que vous avez téléchargé le bon certificat et terminé une autre session dans l’application avant de tenter une autre notification de test.

#### L’application a été désinstallée

Si un utilisateur a désinstallé votre application, son jeton de notification push sera invalide et supprimé lors du prochain envoi.

#### Régénération de votre profil de provisionnement

En dernier recours, recommencez à zéro et en créant un tout nouveau profil de provisionnement cela peut éliminer les erreurs de configuration résultant de l’utilisation simultanée de plusieurs environnements, profils et applications. La mise en place des notifications push comporte de nombreuses "pièces mobiles", c'est pourquoi il est parfois préférable de recommencer depuis le début. Cela permettra également d’isoler le problème si vous devez continuer la résolution des problèmes.

### Messages non livrés aux utilisateurs « notification push enregistrée »

#### Application au premier plan

Sur les versions iOS qui ne sont pas intégrées à la commande via l’infrastructure `UserNotifications`, si l’application est en premier plan lorsque le message de notification push est reçu, il ne s’affiche pas. Vous devez faire l’expérience de l’application sur vos appareils de test avant d’envoyer des messages de test.

#### Notification de test planifiée de manière incorrecte

Vérifiez la planification que vous avez définie pour votre message de test. S'il est réglé sur la réception/distribution par fuseau horaire local ou sur le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/), il se peut que vous n'ayez pas encore reçu le message (ou que l'application ait été au premier plan au moment de sa réception).

### L’utilisateur n’est pas « inscrit aux notifications push » pour l’application testée

Vérifiez le profil utilisateur de l’utilisateur auquel vous essayez d’envoyer un message de test. Sous l'onglet **Engagement**, il devrait y avoir une liste d'"apps poussables". Vérifiez que l’application à laquelle vous essayez d’envoyer des messages de test figure dans cette liste. Les utilisateurs apparaîtront comme "Push Registered" s'ils ont un jeton push pour n'importe quelle application dans votre espace de travail, ce qui pourrait donc être un faux positif.

Ce qui suit indiquerait un problème avec l’inscription aux notifications push ou que le jeton de l’utilisateur a été renvoyé à Braze comme invalide par les APN après avoir été envoyé :

![Profil utilisateur affichant les paramètres de contact d’un utilisateur. Sous Push, "No Apps" s'affiche.]({% image_buster /assets/img_archive/registration_problem.png %}){: style="max-width:50%"}

## Les clics de notification push ne sont pas enregistrés {#push-clicks-not-logged}

- Assurez-vous d'avoir suivi les [étapes de l'intégration push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-5-enable-push-handling).
- Braze ne gère pas les notifications push reçues silencieusement au premier plan (par ex., comportement push avant-plan par défaut avant le framework `UserNotifications`). Cela signifie que les liens ne seront pas ouverts et que les clics ne seront pas enregistrés. Si votre application n’a pas encore intégré l’infrastructure `UserNotifications`, Braze ne traitera pas les notifications push lorsque l’état de l’application est `UIApplicationStateActive`. Veillez à ce que votre application ne retarde pas les appels aux [méthodes de gestion de push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-5-enable-push-handling); sinon, le SDK Swift risque de considérer les notifications push comme des événements push silencieux de premier plan et de ne pas les traiter.

## Les liens profonds ne fonctionnent pas

### Les liens Web des clics sur les notifications push ne s’ouvrent pas

Les liens dans les notifications push doivent être conformes à la norme ATS pour être ouverts dans des vues web. Assurez-vous que vos liens Web utilisent HTTPS. Pour plus d'informations, veuillez vous référer à la [conformité ATS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/#app-transport-security-ats).

### Les liens profonds à partir des clics sur les notifications push ne s’ouvrent pas

La plupart du code qui gère les liens profonds gère également les ouvertures push. Tout d’abord, assurez-vous que les ouvertures de notification push sont enregistrées. Si ce n'est pas le cas, corrigez ce problème (car la correction corrige souvent la gestion des liens).

Si les ouvertures sont enregistrées, vérifiez s’il s’agit d’un problème avec le lien profond en général ou avec la gestion des clics sur les notifications push du lien profond. Pour ce faire, testez si un lien profond d’un message in-app fonctionne.

