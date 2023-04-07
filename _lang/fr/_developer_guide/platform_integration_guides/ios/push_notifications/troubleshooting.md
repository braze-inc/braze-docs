---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes de notification push pour iOS
platform: iOS
page_order: 30
description: "Cet article couvre les sujets concernant la résolution des problèmes potentiels pour votre implémentation de notifications push iOS."
channel:
  - Notification push

---

# Résolution des problèmes{#push-troubleshooting}

## Comprendre le flux de travail du Braze/APN

Le service Apple Push Notification (APN) est l’infrastructure d’Apple pour l’envoi de notifications push aux applications iOS et OS X. Voici la structure simplifiée de la manière dont les notifications push sont activées pour les appareils de vos utilisateurs et la façon dont Braze peut leur envoyer des notifications push :

1. Vous configurez le certificat push et le profil de provisionnement
2. Les appareils s’enregistrent pour les APN et fournissent à Braze des jetons de notification push
3. Vous lancez une campagne de notifications push Braze
4. Braze supprime les jetons non valides

#### Étape 1 : Configurer le certificat push et le profil de provisionnement

Lors du développement de votre application, vous devez créer un certificat SSL pour activer les notifications push. Ce certificat sera inclus dans le profil de provisionnement avec lequel votre application est construite et devra également être téléchargé sur le tableau de bord de Braze. Le certificat permet à Braze de communiquer aux APN que nous sommes autorisés à envoyer des notifications push en votre nom.

Il existe deux types de [profils de provisionnement][2] et de certificats : développement et distribution. Nous vous recommandons d’utiliser uniquement des profils de distribution et des certificats pour éviter toute confusion. Si vous choisissez d’utiliser différents profils et certificats pour le développement et la distribution, assurez-vous que le certificat téléchargé sur le tableau de bord correspond au profil de provisionnement que vous utilisez actuellement.

{% alert warning %}
Ne modifiez pas l’environnement de certificat push (développement par rapport à la production). La modification du certificat de notification push pour un environnement incorrect peut entraîner la suppression accidentelle de son jeton de notification push, ce qui le rend inaccessible par la notification push. 
{% endalert %}

#### Étape 2 : Les appareils s’enregistrent pour les APN et fournissent à Braze des jetons de notification push

Lorsque les utilisateurs ouvrent votre application, ils sont invités à accepter les notifications push. S’ils acceptent cette invite, les APN généreront un jeton de notification push pour cet appareil particulier. Le SDK iOS enverra immédiatement et de manière asynchrone le jeton de notification push pour les applications utilisant la [politique de rinçage automatique][40] par défaut. Une fois que nous avons un jeton de notification push associé à un utilisateur, il apparaîtra comme « Push Registered » (Envoi enregistré) dans le tableau de bord du profil utilisateur sous l’onglet **Engagement** et sera éligible pour recevoir des notifications push des campagnes Braze.

{% alert note %}
Cela ne fonctionne pas avec le simulateur iOS. Par conséquent, vous ne pouvez pas tester les notifications push avec le simulateur iOS.
{% endalert %}

#### Étape 3 : Lancer une campagne de notifications push Braze

Lorsqu’une campagne de notifications push est lancée, Braze effectuera des demandes aux APN pour délivrer votre message. Braze utilisera le certificat push SSL téléchargé dans le tableau de bord pour authentifier et vérifier que nous sommes autorisés à envoyer des notifications push aux jetons de notification push fournis. Si un appareil est en ligne, la notification devrait être reçue peu de temps après l’envoi de la campagne. Notez que Braze définit à 30 jours la [date d’expiration](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607) des APN par défaut pour les notifications.

#### Étape 4 : Supprimer les jetons non valides

Si les [APN][20] nous informent que l’un des jetons push auxquels nous tentons d’envoyer un message est invalide, nous supprimons ces jetons des profils utilisateur auxquels ils étaient associés.

## Utiliser les journaux d’erreur de notification push

Braze fournit un journal des erreurs de notification push dans le **journal d’activité de message**. Ce journal d’erreurs fournit de nombreux avertissements qui peuvent être très utiles pour identifier les raisons pour lesquelles vos campagnes ne fonctionnent pas comme prévu. Cliquer sur un message d’erreur vous redirigera vers la documentation pertinente pour vous aider à résoudre un incident particulier.

![Les journaux d’erreur Push affichent l’heure à laquelle l’erreur s’est produite, le nom de l’application, le canal, le type d’erreur et le message d’erreur.][26]

Les erreurs courantes que vous pouvez voir ici incluent des notifications spécifiques à l’utilisateur, comme la [« réception d’un envoi non enregistré vers un jeton de notification push »][35].

En outre, Braze fournit également un journal de modifications de notifications push au profil utilisateur dans l’onglet **Engagement**. Ce journal de modifications donne un aperçu du comportement d’enregistrement des notifications push, comme l’invalidation des jetons, les erreurs d’enregistrement push, les jetons déplacés vers de nouveaux utilisateurs, etc.

![][1]{: style="max-width:50%;" }

## Problèmes d’enregistrement de notifications push

Pour ajouter une vérification de la logique d’enregistrement push de votre application, mettez en œuvre le protocole de [test d’unité de notification push][41] de Braze.

#### Pas d’invite d’enregistrement push

Si l’application ne vous invite pas à vous inscrire aux notifications push, il y a probablement un problème avec votre intégration d’inscription push. Assurez-vous de suivre notre [documentation][21] et de correctement intégrer notre inscription push. Vous pouvez également définir des points d’arrêt dans votre code pour vous assurer que le code d’inscription de notification push est en cours d’exécution.

#### Aucun utilisateur « push registered » (notification push enregistrée) affiché dans le tableau de bord

- Vérifiez que votre application vous invite à autoriser les notifications push. En général, cette invite apparaîtra lors de votre première ouverture de l’application, mais elle peut être programmée pour apparaître ailleurs. Si elle n’apparaît pas là où elle le devrait, le problème est probablement la configuration de base des capacités de notification push de votre application.
  - Vérifiez les étapes pour l’[intégration push][21] ont été correctement remplis.
  - Vérifiez que le profil de provisionnement de votre application a été créé avec des autorisations pour les notifications push. Assurez-vous de retirer tous les profils de provisionnement disponibles depuis votre compte développeur Apple. Pour confirmer cela, procédez comme suit :
    1. Dans Xcode, naviguez jusqu’à **Préférences > Comptes** (Ou utilisez le raccourci clavier <kbd>Command</kbd>+<kbd>,</kbd>).
    2. Sélectionnez l’ID Apple que vous utilisez pour votre compte développeur et cliquez sur **View Details (Afficher les détails)**.
    3. Sur la page suivante, cliquez sur **<i class="fas fa-redo-alt"></i> Refresh (Actualiser)** et confirmez que vous retirez tous les profils de provisionnement disponibles.
- Vérifiez que vous avez [correctement activé la capacité de notification push][29] dans votre application.
- Vérifiez que votre profil de provisionnement de notification push correspond à l’environnement dans lequel vous effectuez des tests. Les certificats universels peuvent être configurés dans le tableau de bord de Braze pour envoyer vers l’environnement de développement ou de production APN. L’utilisation d’un certificat de développement pour une application de production ou d’un certificat de production pour une application de développement ne fonctionnera pas.
- Vérifiez que vous utilisez `registerPushToken` en définissant un point de rupture dans votre code.
- Vérifiez que vous êtes sur un appareil (la notification push ne fonctionnera pas sur un simulateur) et avez une bonne connectivité réseau.

## Appareils ne recevant pas de notifications push

#### Utilisateurs plus « push registered » (inscrits aux notifications push) après l’envoi d’une notification push

Cela indique probablement que l’utilisateur avait un jeton de notification push non valide. Cela peut se produire pour plusieurs raisons :

##### Pas de correspondance du tableau de bord et du certificat d’application

Si le certificat de notification push que vous avez téléchargé dans le tableau de bord n’est pas le même dans le profil de provisionnement avec lequel votre application a été construite, les APN rejetteront le jeton. Vérifiez que vous avez téléchargé le bon certificat et terminé une autre session dans l’application avant de tenter une autre notification de test.

##### Désinstallations

Si un utilisateur a désinstallé votre application, son jeton de notification push sera invalide et supprimé lors du prochain envoi.

##### Régénération de votre profil de provisionnement

En dernier recours, recommencez à zéro et en créant un tout nouveau profil de provisionnement cela peut éliminer les erreurs de configuration résultant de l’utilisation simultanée de plusieurs environnements, profils et applications. Il existe de nombreuses « pièces mobiles » dans la configuration des notifications push pour les applications iOS, il est donc parfois préférable de réessayer dès le début. Cela permettra également d’isoler le problème si vous devez continuer la résolution des problèmes.

#### Utilisateur encore « push registered » (inscrits aux notifications push) après l’envoi d’une notification push

##### Application au premier plan

Sur les versions iOS qui ne sont pas intégrées à la commande via l’infrastructure `UserNotifications`, si l’application est en premier plan lorsque le message de notification push est reçu, il ne s’affiche pas. Vous devez faire l’expérience de l’application sur vos appareils de test avant d’envoyer des messages de test.

##### Notification de test planifiée de manière incorrecte

Vérifiez la planification que vous avez définie pour votre message de test. Si elle est définie sur le fuseau horaire local ou sur [Timing Intelligent]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/), vous n’avez peut-être pas encore reçu le message (ou l’application était au premier plan lorsqu’elle a été reçue).

#### L’utilisateur n’est pas « inscrit aux notifications push » pour l’application testée

Vérifiez le profil utilisateur de l’utilisateur auquel vous essayez d’envoyer un message de test. Sous l’onglet **Engagement**, il doit y avoir une liste d’« applications pushable ». Vérifiez que l’application à laquelle vous essayez d’envoyer des messages de test figure dans cette liste. Les utilisateurs apparaîtront comme « Push Registered » s’ils ont un jeton de notification push pour n’importe quelle application de votre groupe d’applications, il peut donc s’agir d’un faux positif.

Ce qui suit indiquerait un problème avec l’inscription aux notifications push ou que le jeton de l’utilisateur a été renvoyé à Braze comme invalide par les APN après avoir été envoyé :

![Profil utilisateur affichant les paramètres de contact d’un utilisateur. Vous pouvez voir ici quelles applications push sont enregistrées.][25]{: style="max-width:50%"}

## Erreurs du journal d’activité de message

#### Réception d’un envoi non enregistré au jeton de notification push {#received-unregistered-sending}

- Assurez-vous que le jeton de commande est envoyé à Braze à partir de la méthode `[[Appboy sharedInstance] registerPushToken:]` est valide. Vous pouvez consulter le **journal d’activité de message** pour voir le jeton de notification push. Il devrait ressembler à quelque chose comme `6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6`, une longue chaîne de caractères contenant un mélange de lettres et de chiffres. Si votre jeton de notification push semble différent, vérifiez votre [code][37] pour envoyer des jetons de Braze.
- Vérifiez que votre profil de provisionnement de notification push correspond à l’environnement dans lequel vous effectuez des tests. Les certificats universels peuvent être configurés dans le tableau de bord de Braze pour envoyer vers l’environnement de développement ou de production APN. L’utilisation d’un certificat de développement pour une application de production ou d’un certificat de production pour une application de développement ne fonctionnera pas.
 - Vérifiez que le jeton de notification push que vous avez téléchargé sur Braze correspond au profil de provisionnement que vous avez utilisé pour créer l’application à partir de laquelle vous avez envoyé le jeton de notification push.

#### Jeton de périphérique non destiné à la rubrique

Cette erreur indique que le certificat push et l’ID de lot (bundle ID) de votre application ne correspondent pas. Vérifiez que le certificat de notification push que vous avez téléchargé sur Braze correspond au profil de provisionnement que vous avez utilisé pour créer l’application à partir de laquelle vous avez envoyé le jeton de notification push.

#### BadDeviceToken envoyant au jeton de notification push

Le `BadDeviceToken` est un code d’erreur APN et ne provient pas de Braze. Cette réponse peut être renvoyée pour plusieurs raisons, notamment :

- L’application a reçu un jeton de notification push qui n’était pas valide pour les informations d’identification téléchargées sur le tableau de bord.
- Les notifications push ont été désactivées pour ce groupe d’apps.
- L’utilisateur s’est désinscrit des notifications push.
- L’application a été désinstallée.
- Apple a actualisé le jeton de notification push, ce qui a invalidé l’ancien jeton.
- L’application a été conçue pour un environnement de production, mais les informations d’identification des notifications push téléchargées sur Braze sont définies pour un environnement de développement (ou l’inverse).

## Problèmes après l’envoi de la notification push

Pour ajouter une vérification pour la gestion des notifications push de votre application, implémentez les [tests de l’unité de notification push][41] de Braze.

#### Les clics de notification push ne sont pas enregistrés {#push-clicks-not-logged}

- Si cela ne se produit que sur iOS 10, assurez-vous d’avoir suivi les étapes d’intégration des notifications push pour [iOS 10][30].
- Braze ne gère pas les notifications push reçues silencieusement au premier plan (par ex., comportement push avant-plan par défaut avant l’infrastructure `UserNotifications`). Cela signifie que les liens ne seront pas ouverts et que les clics sur les notifications push ne seront pas enregistrés. Si votre application n’a pas encore intégré l’infrastructure `UserNotifications`, Braze ne traitera pas les notifications push lorsque l’état de l’application est `UIApplicationStateActive`. Vous devez vous assurer que votre application ne retarde pas les appels aux [méthodes de traitement des notifications push][30] de Braze ; sinon, le SDK iOS peut traiter les notifications push comme des événements push silencieux au premier plan et ne pas les transmettre.

#### Les liens Web des clics sur les notifications push ne s’ouvrent pas

iOS 9+ nécessite que les liens soient conformes à ATS pour être ouverts dans les vues Web. Assurez-vous que vos liens Web utilisent HTTPS. Consultez notre article sur la [Conformité ATS][38] pour plus d’informations.

#### Les liens profonds à partir des clics sur les notifications push ne s’ouvrent pas

La plupart du code qui gère les liens profonds gère également les ouvertures push. Tout d’abord, assurez-vous que les ouvertures de notification push sont enregistrées. Sinon [résolvez ce problème][34] (car cette réparation répare souvent la gestion des liens).

Si les ouvertures sont enregistrées, vérifiez s’il s’agit d’un problème avec le lien profond en général ou avec la gestion des clics sur les notifications push du lien profond. Pour ce faire, testez si un lien profond d’un message in-app fonctionne.

[1]: {% image_buster /assets/img_archive/push_changelog.gif %}
[20]: https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1
[21]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/
[25]: {% image_buster /assets/img_archive/registration_problem.png %}
[26]: {% image_buster /assets/img_archive/message_activity_log.png %}
[14]: https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607
[2]: https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html
[29]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-2-enable-push-capabilities
[30]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-5-enable-push-handling
[34]: #push-clicks-not-logged
[35]: #received-unregistered-sending
[37]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-4-register-push-tokens-with-braze
[38]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#app-transport-security-ats
[40]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/fine_network_traffic_control/#automatic-request-processing
[41]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/unit_tests/

