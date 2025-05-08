---
nav_title: FAQ
article_title: FAQ sur les activités en direct
page_order: 20
description: "Cette page fournit des réponses aux questions fréquemment posées sur les activités en direct pour le SDK Swift."
tool: Live Activities
platform:
  - iOS
---

# Foire aux questions

> Cet article apporte des réponses à certaines questions fréquemment posées sur les activités en ligne/instantanées.

## Fonctionnalité et support

### Quelles plateformes prennent en charge les activités en direct ?

Les activités en direct sont actuellement une fonctionnalité spécifique à iOS. L’article Activités en direct couvre les [conditions préalables]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/live_activities/#prerequisites) à la gestion des activités en direct via le SDK Swift de Braze.

### Les applications React Native prennent-elles en charge les activités en direct ?

Oui, le SDK React Native 3.0.0+ prend en charge les activités en direct via le SDK Swift Braze. Autrement dit, vous devez écrire du code iOS React Native directement au-dessus du SDK Swift de Braze. 

Il n'existe pas d'API de commodité JavaScript spécifique à React Native pour les activités en direct, car les fonctionnalités des activités en direct fournies par Apple utilisent des langages intraduisibles en JavaScript (par exemple, la concurrence Swift, les génériques, SwiftUI).

### Braze prend-il en charge les activités en direct en tant que campagne ou étape de Canvas ?

Non, cela n’est pas pris en charge actuellement.

## Notifications push et activités en direct

### Que se passe-t-il si une notification push est envoyée alors qu’une activité en direct est active ? 

![Écran de téléphone avec un match sportif Bulls contre Bears en ligne/en production/instantané vers le milieu de l'écran et un texte de notification push lorem ipsum au bas de l'écran.]({% image_buster /assets/img/push-vs-live-activities.png %}){: style="max-width:30%;float:right;margin-left:15px;"}

Les activités en direct et les notifications push occupent différents écrans et n'entrent pas en conflit sur l'écran d'un utilisateur.

### Si les activités en direct exploitent la fonctionnalité de message de notification push, les notifications push doivent-elles être activées pour recevoir les activités en direct ?

Bien que les activités en direct reposent sur des notifications push pour les mises à jour, elles sont contrôlées par différents paramètres utilisateur. Un utilisateur peut choisir d'être abonné aux activités en direct mais pas aux notifications push, et inversement.

Les jetons de mise à jour de l'activité en ligne/instantanée expirent au bout de huit heures.

### Les activités en direct nécessitent-elles des amorces de notification push ?

Les [amorces de notification push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) constituent une bonne pratique pour inviter vos utilisateurs à s’abonner aux notifications push de votre application. Cependant, il n’y a pas de demande de la part du système pour s’abonner aux activités en direct. Par défaut, les utilisateurs sont abonnés aux activités en direct pour une app individuelle lorsque l'utilisateur installe cette app sur iOS 16.1 ou une version ultérieure. Cette autorisation peut être désactivée ou réactivée dans les paramètres de l'appareil, application par application.

## Sujets techniques et résolution des problèmes

### Comment puis-je savoir si les activités en ligne/instantanées ont des erreurs ?

Toute erreur d'activité en direct sera consignée dans le tableau de bord de Braze dans le [journal des activités liées aux messages]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/), où vous pouvez filtrer par « erreurs d'activités en direct ».

### Après avoir envoyé une notification push/instantanée, pourquoi n'ai-je pas reçu mon activité en direct ?

Tout d'abord, vérifiez que votre charge utile comprend tous les champs obligatoires décrits dans le point de terminaison [`messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start) endpoint. Les champs `activity_attributes` et `content_state` doivent correspondre aux propriétés définies dans le code de votre projet. Si vous êtes certain que la charge utile est correcte, il est possible que votre débit soit limité par les APN. Cette limite est imposée par Apple et non par Braze.

Pour vérifier que votre notification push-to-start est bien arrivée à l'appareil mais qu'elle n'a pas été affichée en raison des limites de débit, vous pouvez déboguer votre projet à l'aide de l'application Console sur votre Mac. Joignez le processus d'enregistrement de l'appareil souhaité, puis filtrez les journaux par `process:liveactivitiesd` dans la barre de recherche.

### Je reçois une réponse « Accès refusé » lorsque j’essaie d’utiliser l’endpoint `live_activity/update`. Pourquoi ?

Les clés API que vous utilisez doivent disposer des autorisations appropriées pour accéder aux différents endpoints de l’API Braze. Si vous utilisez une clé API que vous avez précédemment créée, il est possible que vous ayez omis de mettre à jour ses autorisations. Pour revoir ces points, lisez notre [aperçu de la sécurité des clés API]({{site.baseurl}}/api/basics/#rest-api-key-security).

### Est-ce que l’endpoint `messages/send` partage les limites de débit avec l’endpoint `messages/live_activity/update` ? 

Par défaut, la limite de débit pour l'endpoint `messages/live_activity/update` est de 250 000 requêtes par heure, par espace de travail et sur plusieurs endpoints. Pour plus d'informations, consultez les [limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

### Pourquoi mes jetons "push-to-start" ne sont-ils pas générés ?

Apple a limité ses API `pushToStartToken` et `pushToStartTokenUpdates`, qui ont été introduites dans iOS 17.2. Dans la pratique, les jetons push-to-start sont uniquement générés lors du premier lancement de l'appli dans `application(_:didFinishLaunchingWithOptions:)` après la première installation. Si cette étape doit être répétée, les jetons ne peuvent être générés à nouveau qu'en créant manuellement une nouvelle instance de cette activité en direct, ou après avoir redémarré et réinstallé l'application.

### Combien d'activités en ligne/instantanées puis-je lancer pour mon application ?

Les limites sont définies par Apple et peuvent varier en fonction d'un certain nombre de facteurs. Ils peuvent également être modifiés à l'avenir. Dans la pratique, le nombre d'instances d'activités simultanées pouvant être lancées par application à un moment donné est limité à cinq. Toute tentative ultérieure de lancement d'une nouvelle instance au-delà de cette limite sera ignorée par le système.

### Quels sont les autres éléments auxquels je dois faire attention lors de la résolution des problèmes ?

- Assurez-vous que vous utilisez une clé `.p8` pour l'authentification au lieu d'un fichier `.p12` ou `.pem`.
- Vérifiez que votre profil de provisionnement push correspond à l'environnement que vous testez. Les certificats universels peuvent être configurés dans le tableau de bord de Braze pour être envoyés à l'environnement de développement ou de production du service de notification push d'Apple (APNs). L’utilisation d’un certificat de développement pour une application de production ou d’un certificat de production pour une application de développement ne fonctionnera pas.


