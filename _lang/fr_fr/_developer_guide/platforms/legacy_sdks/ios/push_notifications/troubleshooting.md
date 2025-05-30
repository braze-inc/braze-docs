---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes de notification push pour iOS
platform: iOS
page_order: 30
description: "Cet article de référence couvre les sujets concernant la résolution des problèmes potentiels pour votre implémentation de notifications push iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Résolution des problèmes{#push-troubleshooting}

## Comprendre le flux de travail du Braze/APN

Le service Apple Push Notification (APN) est l’infrastructure d’Apple pour l’envoi de notifications push aux applications iOS et OS X. Voici la structure simplifiée de la manière dont les notifications push sont activées pour les appareils de vos utilisateurs et la façon dont Braze peut leur envoyer des notifications push :

1. Vous configurez le certificat push et le profil de provisionnement
2. Les appareils s’enregistrent pour les APN et fournissent à Braze des jetons de notification push
3. Vous lancez une campagne de notifications push Braze
4. Braze supprime les jetons non valides

#### Étape 1 : Configurer le certificat push et le profil de provisionnement

Lors du développement de votre application, vous devez créer un certificat SSL pour activer les notifications push. Ce certificat sera inclus dans le profil de provisionnement avec lequel votre application est créée et devra également être téléchargé sur le tableau de bord de Braze. Le certificat permet à Braze de communiquer aux APN que nous sommes autorisés à envoyer des notifications push en votre nom.

Il existe deux types de [profils de provisionnement](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html) et de certificats : le développement et la distribution. Nous vous recommandons d’utiliser uniquement des profils de distribution et des certificats pour éviter toute confusion. Si vous choisissez d’utiliser différents profils et certificats pour le développement et la distribution, assurez-vous que le certificat téléchargé sur le tableau de bord correspond au profil de provisionnement que vous utilisez actuellement.

{% alert warning %}
Ne modifiez pas l’environnement de certificat push (développement par rapport à la production). La modification du certificat de notification push pour un environnement incorrect peut entraîner la suppression accidentelle de son jeton de notification push, ce qui le rend inaccessible par la notification push.
{% endalert %}

#### Étape 2 : Les appareils s’enregistrent pour les APN et fournissent à Braze des jetons de notification push

Lorsque les utilisateurs ouvrent votre application, ils sont invités à accepter les notifications push. S’ils acceptent cette invite, les APN généreront un jeton de notification push pour cet appareil particulier. Le SDK iOS enverra immédiatement et de manière asynchrone le jeton push pour les apps utilisant la [politique de rinçage automatique]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/fine_network_traffic_control/#automatic-request-processing) par défaut. Une fois que nous aurons associé un jeton push à un utilisateur, il apparaîtra comme "Enregistré Push" dans le tableau de bord de son profil utilisateur sous l'onglet **Engagement** et sera éligible pour recevoir des notifications push des campagnes Braze.

{% alert note %}
À partir de Xcode 14, vous pouvez tester les notifications push à distance sur un simulateur iOS.
{% endalert %}

#### Étape 3 : Lancer une campagne de notifications push Braze

Lorsqu’une campagne de notifications push est lancée, Braze effectuera des demandes aux APN pour délivrer votre message. Braze utilisera le certificat push SSL téléchargé dans le tableau de bord pour authentifier et vérifier que nous sommes autorisés à envoyer des notifications push aux jetons de notification push fournis. Si un appareil est en ligne, la notification devrait être reçue peu de temps après l’envoi de la campagne. Notez que Braze fixe à 30 jours la [date d'expiration](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607) par défaut des APN pour les notifications.

#### Étape 4 : Supprimer les jetons non valides

Si l ['APN](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) nous informe que l'un des jetons push auxquels nous avons tenté d'envoyer un message n'est pas valide, nous supprimons ces jetons des profils utilisateurs auxquels ils étaient associés.

## Utiliser les journaux d’erreur de notification push

Braze fournit un journal des erreurs de notification push dans le **journal d'activité des messages.** Ce journal d’erreurs fournit de nombreux avertissements qui peuvent être très utiles pour identifier les raisons pour lesquelles vos campagnes ne fonctionnent pas comme prévu. Cliquer sur un message d’erreur vous redirigera vers la documentation pertinente pour vous aider à résoudre un incident particulier.

![Les journaux d'erreurs en mode push affichent l'heure à laquelle l'erreur s'est produite, le nom de l'application, le canal, le type d'erreur et le message d'erreur.]({% image_buster /assets/img_archive/message_activity_log.png %})

Les erreurs courantes que vous pouvez voir ici comprennent des notifications spécifiques à l'utilisateur, telles que ["Received Unregistered Sending to Push Token".](#received-unregistered-sending)

En outre, Braze fournit également un journal des modifications en mode push sur le profil utilisateur, sous l'onglet **Engagement.**  Ce journal des modifications donne un aperçu du comportement d’enregistrement des notifications push, comme l’invalidation des jetons, les erreurs d’enregistrement push, les jetons déplacés vers de nouveaux utilisateurs, etc.

![]({% image_buster /assets/img_archive/push_changelog.gif %}){: style="max-width:50%;" }

## Problèmes d’enregistrement de notifications push

Pour ajouter une vérification à la logique d'enregistrement de push de votre application, mettez en place des [tests unitaires de push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/unit_tests/).

#### Pas d’invite d’enregistrement push

Si l’application ne vous invite pas à vous inscrire aux notifications push, il y a probablement un problème avec votre intégration d’inscription push. Assurez-vous d'avoir suivi notre [documentation]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration/) et d'avoir correctement intégré notre enregistrement push. Vous pouvez également définir des points d’arrêt dans votre code pour vous assurer que le code d’inscription de notification push est en cours d’exécution.

#### Aucun utilisateur « push registered » (notification push enregistrée) affiché dans le tableau de bord

- Vérifiez que votre application vous invite à autoriser les notifications push. En général, cette invite apparaîtra lors de votre première ouverture de l’application, mais elle peut être programmée pour apparaître ailleurs. Si elle n’apparaît pas là où elle le devrait, le problème est probablement la configuration de base des capacités de notification push de votre application.
  - Vérifiez que les étapes de l'[intégration push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration/) ont été effectuées avec succès.
  - Vérifiez que le profil de provisionnement de votre application a été créé avec des autorisations pour les notifications push. Assurez-vous de retirer tous les profils de provisionnement disponibles depuis votre compte développeur Apple. Pour confirmer cela, procédez comme suit :
    1. Dans Xcode, sélectionnez **Préférences > Comptes** (ou utilisez le raccourci clavier <kbd>Command</kbd>+<kbd>,</kbd>).
    2. Sélectionnez l’ID Apple que vous utilisez pour votre compte développeur et cliquez sur **Afficher les détails**.
    3. Sur la page suivante, cliquez sur **<i class="fas fa-redo-alt"></i> Actualiser** et confirmez que vous tirez tous les profils de provisionnement disponibles.
- Vérifiez que vous avez [bien activé la fonction "push"]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-2-enable-push-capabilities) dans votre application.
- Vérifiez que votre profil de provisionnement de notification push correspond à l’environnement dans lequel vous effectuez des tests. Les certificats universels peuvent être configurés dans le tableau de bord de Braze pour envoyer vers l’environnement de développement ou de production APN. L’utilisation d’un certificat de développement pour une application de production ou d’un certificat de production pour une application de développement ne fonctionnera pas.
- Vérifiez que vous utilisez `registerPushToken` en définissant un point de rupture dans votre code.
- Vérifiez que vous êtes sur un appareil (la notification push ne fonctionnera pas sur un simulateur) et avez une bonne connectivité réseau.

## Appareils ne recevant pas de notifications push

#### Utilisateurs plus « push registered » (inscrits aux notifications push) après l’envoi d’une notification push

Ceci indique probablement que l'utilisateur avait un jeton de notification push non valide. Cela peut se produire pour plusieurs raisons :

##### Pas de correspondance du tableau de bord et du certificat d’application

Si le certificat de notification push que vous avez téléchargé dans le tableau de bord n’est pas le même dans le profil de provisionnement avec lequel votre application a été créée , les APN rejetteront le jeton. Vérifiez que vous avez téléchargé le bon certificat et terminé une autre session dans l’application avant de tenter une autre notification de test.

##### Désinstallations

Si un utilisateur a désinstallé votre application, son jeton de notification push sera invalide et supprimé lors du prochain envoi.

##### Régénération de votre profil de provisionnement

En dernier recours, recommencez à zéro et en créant un tout nouveau profil de provisionnement cela peut éliminer les erreurs de configuration résultant de l’utilisation simultanée de plusieurs environnements, profils et applications. Il existe de nombreuses « pièces mobiles » dans la configuration des notifications push pour les applications iOS, il est donc parfois préférable de réessayer dès le début. Cela permettra également d’isoler le problème si vous devez continuer la résolution des problèmes.

#### Utilisateur encore « push registered » (inscrits aux notifications push) après l’envoi d’une notification push

##### Application au premier plan

Sur les versions iOS qui ne sont pas intégrées à la commande via l’infrastructure `UserNotifications`, si l’application est en premier plan lorsque le message de notification push est reçu, il ne s’affiche pas. Vous devez faire l’expérience de l’application sur vos appareils de test avant d’envoyer des messages de test.

##### Notification de test planifiée de manière incorrecte

Vérifiez la planification que vous avez définie pour votre message de test. S'il est réglé sur la réception/distribution par fuseau horaire local ou sur le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/), il se peut que vous n'ayez pas encore reçu le message (ou que l'application ait été au premier plan au moment de sa réception).

#### L’utilisateur n’est pas « inscrit aux notifications push » pour l’application testée

Vérifiez le profil utilisateur de l’utilisateur auquel vous essayez d’envoyer un message de test. Sous l'onglet **Engagement**, il devrait y avoir une liste d'"apps poussables". Vérifiez que l’application à laquelle vous essayez d’envoyer des messages de test figure dans cette liste. Les utilisateurs apparaîtront comme "Push Registered" s'ils ont un jeton push pour n'importe quelle application dans votre espace de travail, ce qui pourrait donc être un faux positif.

Ce qui suit indiquerait un problème avec l’inscription aux notifications push ou que le jeton de l’utilisateur a été renvoyé à Braze comme invalide par les APN après avoir été envoyé :

![Profil utilisateur affichant les paramètres de contact d’un utilisateur. Ici, vous pouvez voir pour quelles applications push est enregistré.]({% image_buster /assets/img_archive/registration_problem.png %}){: style="max-width:50%"}

## Les messages push ne sont pas envoyés

Pour résoudre les problèmes liés aux notifications push qui ne sont pas envoyées, reportez-vous à la section [Résolution des problèmes push.]({{site.baseurl}}/user_guide/message_building_by_channel/push/troubleshooting/)

## Erreurs du journal d’activité de message

#### Réception d’un envoi non enregistré au jeton de notification push {#received-unregistered-sending}

- Assurez-vous que le jeton de commande est envoyé à Braze à partir de la méthode `[[Appboy sharedInstance] registerPushToken:]` est valide. Vous pouvez consulter le **journal des activités liées aux messages** pour voir le jeton de notification push. Il devrait ressembler à quelque chose comme `6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6`, une longue chaîne de caractères contenant un mélange de lettres et de chiffres. Si votre jeton de poussée semble différent, vérifiez votre [code]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-4-register-push-tokens-with-braze) d'envoi des jetons de poussée à Braze.
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

## Problèmes après l’envoi de la notification push

Pour ajouter une vérification à la gestion de push de votre application, mettez en place des [tests unitaires de push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/unit_tests/).

#### Les clics de notification push ne sont pas enregistrés {#push-clicks-not-logged}

- Si cela ne se produit que sur iOS 10, assurez-vous d'avoir suivi les étapes d'intégration push pour [iOS 10.]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-5-enable-push-handling)
- Braze ne gère pas les notifications push reçues silencieusement au premier plan (par ex., comportement des notifications push d’avant-plan par défaut avant le framework `UserNotifications`). Cela signifie que les liens ne seront pas ouverts et que les clics sur les notifications push ne seront pas enregistrés. Si votre application n’a pas encore intégré l’infrastructure `UserNotifications`, Braze ne traitera pas les notifications push lorsque l’état de l’application est `UIApplicationStateActive`. Vous devez vous assurer que votre application ne retarde pas les appels à nos [méthodes de gestion des pushs]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-5-enable-push-handling); dans le cas contraire, le SDK iOS peut considérer les notifications push comme des événements push silencieux de premier plan et ne pas les traiter.

#### Les liens Web des clics sur les notifications push ne s’ouvrent pas

iOS 9+ nécessite que les liens soient conformes à ATS pour être ouverts dans les vues Web. Assurez-vous que vos liens Web utilisent HTTPS. Pour plus d'informations, reportez-vous à notre article sur [la conformité des STA.]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#app-transport-security-ats) 

#### Les liens profonds à partir des clics sur les notifications push ne s’ouvrent pas

La plupart du code qui gère les liens profonds gère également les ouvertures push. Tout d’abord, assurez-vous que les ouvertures de notification push sont enregistrées. Si ce n'est pas le cas, [corrigez ce problème](#push-clicks-not-logged) (car la correction corrige souvent la gestion des liens).

Si les ouvertures sont enregistrées, vérifiez s’il s’agit d’un problème avec le lien profond en général ou avec la gestion des clics sur les notifications push du lien profond. Pour ce faire, testez si un lien profond d’un message in-app fonctionne.

#### Peu ou pas d'ouvertures directes

Si au moins un utilisateur ouvre votre notification push iOS, mais que peu ou pas d'_ouvertures directes_ sont enregistrées dans Braze, il se peut qu'il y ait un problème avec votre [intégration SDK]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview/). Gardez à l'esprit que les _ouvertures directes_ ne sont pas enregistrées pour les envois de test ou les notifications push silencieuses.

- Assurez-vous que les messages ne sont pas envoyés en tant que [notifications push silencieuses]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/#sending-silent-push-notifications). Le message doit comporter du texte dans le titre ou le corps du message pour ne pas être considéré comme silencieux.
- Vérifiez à nouveau les étapes suivantes du [guide d'intégration push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration/):
   - [Inscrivez-vous pour pousser]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-register-for-push-notifications-with-apns): À chaque lancement d'application, de préférence sur `application:didFinishLaunchingWithOptions:`, le code de l'étape 3 doit être exécuté. La propriété delegate de `UNUserNotificationCenter.current()` doit être assignée à un objet qui implémente `UNUserNotificationCenterDelegate` et contient la méthode `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:`.
   - [Activer la gestion de la poussée]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/push_notifications/integration/#step-5-enable-push-handling): Vérifiez que la méthode `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` a été mise en œuvre.

