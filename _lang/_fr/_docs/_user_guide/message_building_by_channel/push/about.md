---
nav_title: "À propos de Push"
article_title: À propos de Push
page_order: 0
page_type: Référence
description: "Cet article de référence donne un bref aperçu de push, fournit des ressources pour commencer avec des messages push, et note quelques règlements."
channel:
  - Pousser
---

# À propos des notifications push

> Cet article de référence donne un bref aperçu de push, fournit des ressources pour commencer avec des messages push, et note quelques règlements. Pour en savoir plus sur ce sujet, consultez notre [cours Push LAB](https://lab.braze.com/messaging-channels-push)!

Les notifications push sont merveilleuses pour les appels temporaires à l'action, ainsi que pour les utilisateurs qui ne sont pas entrés dans l'application depuis un certain temps. Des campagnes de push réussies poussent l'utilisateur directement vers le contenu et démontrent la valeur de votre application.

Gardez à l'esprit que les utilisateurs doivent opter pour pousser pour recevoir vos messages, ce qui signifie que c'est une bonne idée d'utiliser des messages dans l'application pour expliquer à vos clients pourquoi vous voulez leur envoyer des notifications push, et la manière dont la promotion de la poussée leur sera bénéfique. Ce processus s'appelle [amorçage push]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/create_push_primer/).

!\[Exemple de Message Push\]\[1\]{: height="400px"} !\[Exemple de Message Push\]\[2\]{: height="400px"}

_Pour voir plus d'exemples de notifications push, consultez notre [Études de cas][8]._

## Cas d'utilisation potentiels

Les notifications push sont un excellent outil pour attirer de nouveaux utilisateurs et faire des campagnes de réengagement. Voici quelques exemples de cas courants d'utilisation de messages push.

| Cas d'utilisation         | Explication                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Intégration initiale      | Jusqu'à ce que les utilisateurs prennent les mesures initiales pour utiliser votre application (comme l'enregistrement d'un compte), leur valeur est sévèrement limitée. Utilisez les notifications push pour inviter les utilisateurs à compléter ces étapes afin qu'ils puissent commencer à utiliser votre application dans son intégralité.                                                                                                                                                                                                                                                                                                               |
| Premiers achats           | Une fois que les utilisateurs sont à l'aise avec votre application, vous pouvez utiliser les notifications push pour les aider à les convertir en acheteurs intégrés à l'application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Nouvelles fonctionnalités | Les notifications push peuvent être efficaces pour avertir les utilisateurs désengagés des nouvelles fonctionnalités qui pourraient les attirer vers votre application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Offres sensibles au temps | Si vous avez une horloge à cocher sur une offre, pousser est parfois un excellent moyen de le faire savoir à vos utilisateurs avant qu'il n'expire. Ces messages ont généralement un sens aigu de l'urgence et sont optimaux pour rappeler aux utilisateurs récemment devenus obsolètes à propos de votre application.<br><br> Par exemple, supposons que votre application est un jeu et que vous offrez à vos utilisateurs un bonus en devise s'ils maintiennent une série de jeux tous les jours. Avertir un utilisateur que cette série risque d'être cassée pourrait être une poussée raisonnable s'il a dépassé un certain nombre de jours. |
{: .reset-td-br-1 .reset-td-br-2}

Pour plus d'informations sur les utilisateurs réengageants, consultez notre page [Victoires Rapides][23] sur le sujet.

## Pré-requis pour utiliser push

Avant de pouvoir créer et envoyer des messages push en utilisant Braze, vous devez travailler avec vos développeurs pour intégrer push dans votre site web ou application. Pour des étapes détaillées, reportez-vous à nos guides d'intégration pour chaque plateforme :

- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/)
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/)

## Réglages des messages push

Parce que les messages push sont un type intrusif de messagerie qui va directement au téléphone ou au navigateur de votre client, il y a des directives pour envoyer des messages push via des applications et des sites.

### Réglages de push pour les applications mobiles

{% alert important %}
Vos messages push doivent être conformes aux directives de l'Apple App Store et des politiques du Play Store de Google. en particulier en ce qui concerne l'utilisation des messages push comme publicités, spam, promotions, et plus encore.
{% endalert %}

| Politiques de l'App Store d'Apple                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [4.5.][7] Les notifications Push ne doivent pas être requises pour que l'application fonctionne, et ne doivent pas être utilisées pour la publicité, des promotions, ou des fins de marketing direct ou pour envoyer des informations personnelles ou confidentielles sensibles.                                                                                                                               |
| [3.2.2][9] (i) Créer une interface pour afficher des applications, extensions ou plugins tiers similaires à l'App Store ou en tant que collection d'intérêt général. (ii) Monétiser les capacités intégrées fournies par le matériel ou le système d'exploitation, telles que les notifications push, la caméra ou le gyroscope ; ou des services Apple, tels que l'accès à Apple Music ou le stockage iCloud. |
{: .reset-td-br-1 .reset-td-br-2}

| Règles du Google Play Store                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Utilisation ou Imitation non autorisée de la fonctionnalité système][10] Nous n'autorisons pas les applications ou les publicités qui imitent ou interfèrent avec la fonctionnalité du système, comme des notifications ou des avertissements. Les notifications au niveau du système ne peuvent être utilisées que pour les fonctionnalités intégrales d'une application, comme une application aérienne qui avertit les utilisateurs d'offres spéciales, ou un jeu qui informe les utilisateurs des promotions en jeu. |
{: .reset-td-br-1}

## Caractéristiques de l'image et du texte

Pour de meilleurs résultats, reportez-vous aux directives de taille d'image et de longueur de message suivantes lors de la création de vos messages push. Il peut y avoir une certaine variance selon la présence d'une image, l'état de la notification (iOS) et le réglage de l'affichage du périphérique de l'utilisateur, ainsi que la taille du périphérique. En cas de doute, gardez votre copie courte et sucrée.

### Notifications push mobiles natives

{% tabs local %}
{% tab Images %}

| **Type d'image**               | **Taille de l'image recommandée** | **Taille maximale de l'image** | **Types de fichiers** |
| ------------------------------ | --------------------------------- | ------------------------------ | --------------------- |
| (iOS) 2:1 *Recommandé*         | 500Ko                             | 5 Mo                           | PNG, JPG, GIF         |
| (Android) Icône Push           | 500Ko                             | 5 Mo                           | PNG, JPG              |
| (Android) Notification étendue | 500Ko                             | 5 Mo                           | PNG, JPG              |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% endtab %}
{% tab Text %}

|                                  | Type de message | Longueur du message recommandé (texte seulement) | Longueur du message recommandé (Rich) |
| -------------------------------- | --------------- | ------------------------------------------------ | ------------------------------------- |
| (iOS) Écran de verrouillage      | 160 caractères  | 130 caractères                                   |                                       |
| (iOS) Centre de Notification     | 160 caractères  | 130 caractères                                   |                                       |
| (iOS) Alerte de bannière         | 80 caractères   | 65 caractères                                    |                                       |
| (Android) Écran de verrouillage  | 49 caractères   | N/A                                              |                                       |
| (Android) Tiroir de notification | 597 caractères  | N/A                                              |                                       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

Vous vous demandez combien de caractères vous pouvez utiliser dans une notification push iOS sans qu'elle soit tronquée ? Consultez nos [lignes directrices pour le nombre de caractères iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count).

{% endtab %}
{% tab Payload Size %}

| **Plateforme** | **Taille** |
| -------------- | ---------- |
| pre iOS 8      | 0.256 Ko   |
| publier iOS 8  | 2 Ko       |
| Android (FCM)  | 4 Ko       |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}

### Notifications push Web

{% tabs local %}
{% tab Images %}

| **Navigateur** | **Taille de l'icône recommandée** |
| -------------- | --------------------------------- |
|                |                                   |
 Chrome | 192 x 192 † Firefox | 192 x 192 † Safari | Icônes non configurables par campagne Opera | 192x192 †.
{: .reset-td-br-1 .reset-td-br-2}

| **Navigateur** | **Plateforme** | **Grande taille d'image** |
| -------------- | -------------- | ------------------------- |
|                |                |                           |
 Chrome | macOS | N/A Chrome | Android | 2 : 1 aspect ratio Chrome | Windows | 360 ・x 240 Firefox | macOS| N/A Safari | macOS | N/A Opera | macOS | macOS | N/A
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Text %}

| **Navigateur** | **Plateforme** | **Longueur maximale du titre** | **Longueur maximale du corps du message** |
| -------------- | -------------- | ------------------------------ | ----------------------------------------- |
|                |                |                                |                                           |
 Chrome | macOS | 35 | 50 Safari | macOS | macOS | 38 | 84 Firefox | macOS | 38 | 42 Opera | macOS | 38 | 42
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% endtab %}
{% endtabs %}
[1]: {% image_buster /assets/img/red-dress.gif %} [2]: {% image_buster /assets/img/ios_push.png %}

[8]: https://www.braze.com/customers
[7]: https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services
[9]: https://developer.apple.com/app-store/review/guidelines/#unacceptable
[10]: https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories
[23]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users
