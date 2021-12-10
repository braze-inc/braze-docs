---
nav_title: Dépannage
article_title: Dépannage des notifications push pour iOS
platform: iOS
page_order: 30
description: "Cet article couvre les sujets potentiels de dépannage pour votre implémentation de push iOS."
channel:
  - Pousser
---

# Dépannage {#push-troubleshooting}

## Comprendre le workflow Braze/APN

Le service Apple Push Notification (APN) est l’infrastructure d’Apple pour l’envoi de notifications push aux applications iOS et OS X. Voici la structure simplifiée de la façon dont les notifications push sont activées pour les appareils de vos utilisateurs et comment Braze est capable de leur envoyer des notifications push :

1. Vous configurez le certificat push et le profil de provisioning
2. Les appareils s'enregistrent pour les APN et fournissent à Braze des jetons push
3. Vous lancez une campagne de poussée Braze
4. Braze supprime les jetons invalides

### Étape 1 : Configuration du profil du certificat push et du provisioning

Dans le développement de votre application, vous devrez créer un certificat SSL pour activer les notifications push. Ce certificat sera inclus dans le profil de provisioning avec lequel votre application est construite et devra également être téléchargée sur le tableau de bord Braze. Le certificat permet à Braze de dire aux APN que nous sommes autorisés à envoyer des notifications push en votre nom.

Il existe deux types de profils de provisioning et de certificats - développement et distribution. Nous vous recommandons d'utiliser simplement des profils de distribution/certificats pour éviter toute confusion. Si vous choisissez d'utiliser différents profils et certificats pour le développement et la distribution, assurez-vous que le certificat téléchargé sur le tableau de bord correspond au profil de provisioning que vous utilisez actuellement. Vous pouvez en savoir plus sur les profils de provisioning dans l' [Aide du développeur][2] d'Apple.

{% alert warning %}
Ne modifiez pas l'environnement de certificat push (développement contre production), car le fait de changer le certificat push vers le mauvais environnement peut conduire à ce que les utilisateurs finaux aient accidentellement été supprimés, ce qui les rend injoignables par push.
{% endalert %}

### Étape 2 : Les appareils s'enregistrent pour les APN et fournissent à Braze des jetons push

Lorsque les utilisateurs ouvrent votre application, ils seront invités à accepter les notifications push. S'ils acceptent cette invitation, alors les APN génèreront un jeton push pour ce périphérique particulier. Le SDK iOS enverra immédiatement et de manière asynchrone le jeton push pour les applications en utilisant la [politique de fermeture automatique][40] par défaut.  Après que nous ayons un jeton push associé à un utilisateur, ils s'afficheront comme "Push Registered" dans le tableau de bord de leur profil utilisateur sous l'onglet "Engagement" et seront éligibles pour recevoir des notifications push de campagnes Braze.

> Cela ne fonctionne pas avec le simulateur iOS. Vous ne pouvez donc pas tester les notifications push avec le simulateur iOS.

### Étape 3 : Lancement d'une campagne Braze push

Quand une campagne de push est lancée, Braze fera des demandes aux APN pour envoyer votre message. Braze utilisera le certificat SSL push téléchargé dans le tableau de bord pour s'authentifier et vérifier que nous sommes autorisés à envoyer des notifications push aux jetons de push fournis. Si un appareil est en ligne, la notification doit être reçue peu après l'envoi de la campagne.

{% alert note %}
Braze définit la date d'expiration des APNs [par défaut](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607) pour les notifications à 30 jours.
{% endalert %}

### Étape 4 : Suppression des jetons invalides

Si les APN nous informent que l'un des jetons de push que nous tentions d'envoyer est invalide, nous retirons ces jetons des profils d'utilisateurs auxquels ils ont été associés.

Apple a plus de détails sur les APN dans sa [bibliothèque de développeurs][20].

## Utilisation des logs d'erreur push

Braze fournit un journal des erreurs de notification Push dans le [Journal d'activité des messages][27]. Ce journal d'erreurs fournit une variété d'avertissements qui peuvent être très utiles pour identifier pourquoi vos campagnes ne fonctionnent pas comme prévu.  Cliquer sur un message d’erreur vous redirigera vers la documentation pertinente pour vous aider à résoudre un incident particulier.

!\[Journal d'erreur\]\[26\]

Les erreurs courantes que vous pourriez voir ici incluent des notifications spécifiques à l'utilisateur, telles que ["Received Unregistered Sending Sending to Push Token"][35].

En outre, Braze fournit également un Changelog Push sur le profil de l'utilisateur sous l'onglet Engagement. Ce changelog fournit un aperçu du comportement d’enregistrement push comme l’invalidation des jetons, les erreurs d’enregistrement push, les jetons étant déplacés vers les nouveaux utilisateurs, etc.

!\[Push Changelog\]\[1\]{: style="max-width:50%;" }

## Problèmes d'enregistrement de Push

### Pas d'invitation d'inscription push

Si l'application ne vous invite pas à vous inscrire pour recevoir des notifications push, il y a probablement un problème avec votre intégration à l'enregistrement push. Assurez-vous que vous avez suivi notre [documentation][21] et que vous avez correctement intégré notre inscription push. Vous pouvez également définir des points d'arrêt dans votre code pour vous assurer que le code d'enregistrement est en cours d'exécution.

### Aucun utilisateur "push registred" ne s'affiche dans le tableau de bord

  - Assurez-vous que votre application vous invite à autoriser les notifications push. Typiquement, cette invite apparaîtra lors de votre première ouverture de l'application, mais elle peut être programmée pour apparaître ailleurs. Si elle n'apparaît pas là où elle devrait être, alors le problème est probablement lié à la configuration de base des fonctionnalités de push de votre application.
    - Vérifiez que les étapes de [Intégration Push][21] ont été complétées avec succès.
    - Assurez-vous que le profil de provisioning de votre application a été construit avec des autorisations pour push. Assurez-vous que vous retirez tous les profils de provisioning disponibles de votre compte Apple Developer. Pour confirmer ceci, effectuez les étapes suivantes :
      1. Dans Xcode, accédez à **Préférences** > **Comptes clients** (Ou utilisez le raccourci clavier <kbd>Commande</kbd>+<kbd>,</kbd>).
      2. Sélectionnez l'identifiant Apple que vous utilisez pour votre compte développeur et cliquez sur **Voir les détails**.
      3. Sur la page suivante, cliquez sur **<i class="fas fa-redo-alt"></i> Rafraîchir** et confirmez que vous tirez tous les profils de provisioning disponibles.
  - Assurez-vous que vous avez [la capacité push][29] correctement activée dans votre application.
  - Assurez-vous que votre profil de provisioning push correspond à l'environnement dans lequel vous testez. Les certificats universels peuvent être configurés dans le tableau de bord de Braze pour être envoyés à l'environnement de développement ou de production des APN. Utiliser un certificat de développement pour une application de production ou un certificat de production pour une application de développement ne fonctionnera pas.
  - Assurez-vous que vous appelez notre méthode `registerPushToken` en définissant un point d'arrêt dans votre code.
  - Assurez-vous que vous êtes sur un périphérique (push ne fonctionnera pas sur un simulateur) et que vous avez une bonne connectivité réseau.

## Appareils ne recevant pas de notifications push

### Les utilisateurs ne "push registred" plus après avoir envoyé une notification push

Cela indiquerait probablement que l'utilisateur a un jeton push invalide. Cela peut se produire pour plusieurs raisons :

#### Incompatibilité du certificat du tableau de bord/application

Si le certificat push que vous avez téléchargé dans le tableau de bord n'est pas le même dans le profil de provisioning avec lequel votre application a été construite, Les APN rejetteront le jeton. Vérifiez que vous avez téléchargé le bon certificat et terminez une autre session dans l'application avant d'essayer une autre notification de test.

#### Désinstallation

Si un utilisateur a désinstallé votre application, alors son jeton push sera invalide et supprimé lors du prochain envoi.

#### Régénérer votre profil de provisioning

En dernier recours, commencer par rafraîchir et créer un nouveau profil de provisioning peut effacer les erreurs de configuration qui viennent de travailler avec plusieurs environnements, profils et applications en même temps. Il y a beaucoup de « pièces mobiles » dans la configuration des notifications push pour les applications iOS, il est donc parfois préférable de réessayer dès le début. Cela vous aidera également à isoler le problème si vous avez besoin de continuer le dépannage.

### Les utilisateurs "push registred" après avoir envoyé une notification push

#### L'application est au premier plan

Sur les versions iOS qui n'intègrent pas push via le framework UserNotifications, si l'application est au premier plan lorsque le message push est reçu, elle ne sera pas affichée. Vous devriez mettre en arrière-plan l'application sur vos appareils de test avant d'envoyer des messages de test.

#### Notification de test programmée incorrectement

Vérifiez le calendrier que vous avez défini pour votre message de test. Si réglé sur la livraison locale du fuseau horaire ou [Temps intelligent]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/), vous n'avez peut-être pas encore reçu le message (ou vous avez eu l'application au premier plan quand elle a été reçue).

### L'utilisateur n'est pas "push registered" pour l'application en cours de test

Vérifiez le profil utilisateur de l'utilisateur auquel vous essayez d'envoyer un message de test. Sous l'onglet "Engagement", il devrait y avoir une liste d'"Applications Pushable". Vérifiez que l'application à laquelle vous essayez d'envoyer des messages de test se trouve dans cette liste. Les utilisateurs s'afficheront comme "Push Registered" s'ils ont un jeton Push pour n'importe quelle application dans votre groupe d'applications, donc cela pourrait être quelque chose de faux positif.

Ce qui suit indiquerait un problème avec l'enregistrement push, ou que le jeton de l'utilisateur a été retourné à Braze comme invalide par les APN après avoir été poussé :

!\[Problème Push\]\[25\]{: style="max-width:50%"}

## Erreurs du journal d'activité du message

### Envoi non enregistré au jeton push reçu {#received-unregistered-sending}

- Assurez-vous que le jeton push envoyé à Braze à partir de la méthode `[[Appboy sharedInstance] registerPushToken:]` est valide. Vous pouvez regarder dans le [Journal d'activité des messages][27] pour voir le jeton push. Il devrait ressembler à `6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6`, une chaîne de caractères de cette longueur avec un mélange de lettres et de chiffres. Si votre jeton push semble différent, vérifiez votre code [][37] pour envoyer les jetons push Braze.
- Assurez-vous que votre profil de provisioning push correspond à l'environnement dans lequel vous testez. Les certificats universels peuvent être configurés dans le tableau de bord de Braze pour être envoyés à l'environnement de développement ou de production des APN. Utiliser un certificat de développement pour une application de production ou un certificat de production pour une application de développement ne fonctionnera pas.
 - Vérifiez que le jeton push que vous avez téléchargé sur Braze correspond au profil de provisioning que vous avez utilisé pour construire l'application depuis laquelle vous avez envoyé le jeton push.

### Jeton de l'appareil non pour le sujet

 Cette erreur indique que le certificat push et l'identifiant du paquet de votre application ne correspondent pas. Vérifiez que le certificat push que vous avez téléchargé sur Braze correspond au profil de provisioning utilisé pour construire l'application depuis laquelle le jeton de push a été envoyé.

### Envoi de BadDeviceToken au jeton push

Le `BadDeviceToken` est un code d'erreur APN et ne provient pas de Braze. Plusieurs raisons pourraient justifier le retour de cette réponse, parmi lesquelles:

- L'application a reçu un jeton push non valide pour les identifiants téléchargés sur le tableau de bord
- Push a été désactivé pour ce groupe d'applications
- L'utilisateur a choisi de ne plus recevoir de push
- L'application a été désinstallée
- Apple a rafraîchi le jeton push, qui a invalidé l'ancien jeton
- L'application a été construite pour un environnement de production, mais les identifiants de push envoyés sur Braze sont définis pour un environnement de développement (ou inversement)

## Problèmes après envoi de push

### Les clics push ne sont pas enregistrés {#push-clicks-not-logged}

 - Si cela ne se produit que sur iOS 10, assurez-vous que vous avez suivi les étapes d'intégration push pour [iOS 10][30].
 - Braze ne gère pas les notifications push reçues en mode silencieux au premier plan (par exemple, le comportement de premier plan par défaut avant le cadre UserNotice). Cela signifie que les liens ne seront pas ouverts et que les clics push ne seront pas enregistrés. Si votre application n'a pas encore intégré le framework UserNotifications, Braze ne gérera pas les notifications push lorsque l'état de l'application est UIApplicationStateActive. Vous devriez vous assurer que votre application ne retarde pas les appels vers les méthodes de gestion des push de [Braze][30], sinon, le SDK iOS peut traiter les notifications push comme des événements de premier plan silencieux et ne pas les distribuer.

### Les liens Web des clics push ne s'ouvrent pas

iOS 9+ nécessite que les liens soient conformes à la norme ATS pour être ouvert dans les vues Web. Assurez-vous que vos liens web utilisent HTTPS. Pour plus d'informations, reportez-vous à notre [documentation sur la conformité ATS][38].

### Les liens profonds des clics push ne s'ouvrent pas

La plupart du code qui gère les liens profonds gère également les ouvertures push.  Tout d'abord, assurez-vous que les ouvertures push sont enregistrées ; si ce n'est pas le cas, [corrigez d'abord ce problème][34] (comme la correction corrige souvent la gestion des liens).

Si les ouvertures sont enregistrées, vérifiez si c'est un problème avec le lien profond en général ou avec la gestion du clic poussé.  Pour ce faire, testez pour voir si un lien profond à partir d'un message In-App cliquez fonctionne.
[1]: {% image_buster /assets/img_archive/push_changelog.gif %} [25]: {% image_buster /assets/img_archive/registration_problem.png %} [26]: {% image_buster /assets/img_archive/message_activity_log.png %}

[20]: https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1
[21]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/
[21]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/
[27]: https://dashboard-01.braze.com/app_settings/developer_console/activitylog/
[2]: https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html
[29]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-2-enable-push-capabilities
[30]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-5-enable-push-handling
[30]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-5-enable-push-handling
[34]: #push-clicks-not-logged
[35]: #received-unregistered-sending
[37]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-4-register-push-tokens-with-braze
[37]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-4-register-push-tokens-with-braze
[38]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#app-transport-security-ats
[40]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/fine_network_traffic_control/#automatic-request-processing
