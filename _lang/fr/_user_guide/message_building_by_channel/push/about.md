---
nav_title: "À propos des notifications push"
article_title: À propos des notifications push
page_order: 0
page_type: reference
description: "Le présent article de référence donne un bref aperçu des notifications push, fournit des ressources pour débuter dans les messages de notification push et présente certaines réglementations."
channel:
  - Notification push

---

# [![Cours d’apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-push){: style="float:right;width:120px;border:0;" class="noimgborder"}À propos des notifications push

> Les notifications push sont idéales pour les appels à l’action urgents, ainsi que pour le ré-engagement des utilisateurs qui n’ont pas utilisé l’application depuis un certain temps. Les campagnes de notifications push réussies amènent l’utilisateur directement au contenu et démontrent la valeur de votre application. 

Gardez à l’esprit que les utilisateurs doivent s’abonner pour recevoir vos messages, ce qui signifie qu’il peut être intéressant d’utiliser des messages in-app pour expliquer à vos clients pourquoi vous voulez leur envoyer des notifications push et en quoi leur activation leur sera bénéfique. Ce processus est appelé [préparer à la notification push]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/create_push_primer/).

![Exemple de message de notification push pour des produits Apple.][1]{: height="400px"}  ![Exemple de message de notification push de Stopwatch sur un écran d’accueil iPhone qui affiche : « Bonjour ! Ceci est une notification push iOS ».][2]{: height="400px"}

Pour voir plus d’exemples de notifications push, consultez notre [Études de cas][8].

## Cas d’usage potentiels

Les notifications push constituent un outil formidable pour attirer de nouveaux utilisateurs et conduire des campagnes de ré-engagement. Voici quelques exemples de cas d’utilisation courants de messages de notification push. 

| Cas d’utilisation | Explication |
| -------- | ----------- |
| Onboarding initial | La valeur des utilisateurs est très limitée tant qu’ils n’ont pas fait les premiers pas pour utiliser votre application (comme l’enregistrement d’un compte). Utilisez des notifications push pour inciter les utilisateurs à effectuer ces étapes afin qu’ils puissent commencer à utiliser votre application dans sa totalité. |
| Premiers achats | Une fois que les utilisateurs sont à l’aise dans l’utilisation de votre application, vous pouvez utiliser des notifications push pour les convertir en acheteurs in-app. |
| Nouvelles fonctionnalités | Les notifications push peuvent être efficaces pour informer les utilisateurs désengagés de nouvelles fonctionnalités susceptibles de les attirer à nouveau vers votre application. |
| Offres limitées dans le temps | Si vous avez une offre qui va disparaître, une notification push peut parfois être un excellent moyen d’en parler à vos utilisateurs avant son expiration. Ces messages transmettent généralement une notion claire de l’urgence et sont optimaux pour rappeler votre application aux utilisateurs récemment inactifs.<br><br> Par exemple, supposons que votre application soit un jeu et que vous offrez à vos utilisateurs un bonus de monnaie du jeu s’ils maintiennent une habitude de jouer au jeu quotidiennement. Signaler à un utilisateur que cette série de connexions risque d’être brisée peut constituer une notification push raisonnable s’il a dépassé un certain nombre de jours. |
{: .reset-td-br-1 .reset-td-br-2}

Pour plus d’informations sur le ré-engagement d’utilisateurs inactifs, consultez notre page [Victoires rapides][23] sur le sujet.

## Conditions préalables à l’utilisation de notification push

Avant de pouvoir créer et envoyer des messages de notification push à l’aide de Braze, vous devez travailler avec vos développeurs pour les intégrer à votre site Internet ou à votre application. Pour des instructions détaillées, consultez nos guides d’intégration pour chaque plateforme :

- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/)
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/)

## Réglementations relatives aux messages de notification push

Les messages de notification push étant un type de messages intrusif qui est envoyé directement vers le téléphone ou le navigateur de votre client, il existe des directives pour envoyer des messages de notification push via des applications et des sites.

### Réglementations des notifications push mobiles pour les applications

{% alert important %}
Vos messages de notification push doivent être conformes aux directives de l’App Store d’Apple et des politiques de Google Play Store, en particulier concernant l’utilisation de messages de notification push en tant que publicités, spam, promotions, etc.
{% endalert %}

|Politiques de l’App Store d’Apple|
|---|
|[4.5.4][7] Les notifications push ne doivent pas être requises pour que l’application fonctionne et ne doivent pas être utilisée à des fins publicitaires, promotionnelles ou de marketing direct ou pour envoyer des informations personnelles ou confidentielles sensibles.|
|[3.2.2][9] (i) Créer une interface pour l’affichage d’applications, d’extensions ou de plug-ins tiers similaires à l’App Store ou en tant que collecte d’intérêt général. (ii) Monétiser des capacités intégrées fournies par le matériel ou le système d’exploitation, telles que les notifications push, la caméra ou le gyroscope, ou les services Apple, tels que l’accès à Apple Music ou le stockage iCloud.|
{: .reset-td-br-1 .reset-td-br-2}

|Politique de Google Play Store|
|---|
|[Utilisation non autorisée ou imitation des fonctionnalités du système][10] Nous n'autorisons pas les applications ou les annonces qui imitent ou perturbent les fonctionnalités système, comme les notifications ou les avertissements. Les notifications système ne peuvent être utilisées que pour les fonctionnalités principales de l'application. Par exemple, l'application d'une compagnie aérienne qui avertit les utilisateurs d'offres spéciales, ou un jeu qui les informe de promotions intégrées.|
{: .reset-td-br-1}

## Spécifications de l’image et du texte

Pour de meilleurs résultats, reportez-vous aux directives de taille et de longueur de message suivantes lors de l’élaboration de vos messages de notification push. Il peut y avoir une variation en fonction de la présence d’une image, de l’état de la notification (iOS) et du réglage d’affichage de l’appareil de l’utilisateur, ainsi que de sa taille. En cas de doute, gardez votre texte bref et agréable.

### Notification push mobiles natives

{% tabs local %}
{% tab Images %}

**Type d’image** | **Taille d’image recommandée** | **Taille d’image max.** | **Types de fichiers**
--- | --- | --- | ---
(iOS) 2:1 *recommandé* | 500 Ko | 5 Mo | PNG, JPG, GIF
(Android) Icône de notification push | 500 Ko | 5 Mo | PNG, JPG
(Android) Notification étendue | 500 Ko | 5 Mo | PNG, JPG
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% endtab %}
{% tab Text %}

| Type de message | Longueur recommandée du message (texte uniquement) | Longueur recommandée du message (riche)
--- | ---
(iOS) Écran de verrouillage | 160 caractères | 130 caractères
(iOS) Centre de notification | 160 caractères | 130 caractères
(iOS) Alerte de bannière | 80 caractères | 65 caractères
(Android) Écran de verrouillage | 49 caractères | S.O.
(Android) Barre de notification | 597 caractères | S.O.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

Vous vous demandez combien de caractères vous pouvez utiliser dans une notification push iOS sans qu’elle soit tronquée ? Consultez nos [directives sur le nombre de caractères pour iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count).

{% endtab %}
{% tab Payload Size %}

**Plateforme** | **Taille**
--- | ---
Pré-iOS 8 | 0,256 Ko
post iOS 8 | 2 Ko
Android (FCM) | 4 Ko
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}

### Notifications push Web

{% tabs local %}
{% tab Images %}

| **Navigateur** | **Taille d’icône recommandée**
| --- | ---
Chrome | 192 x 192 ≥
Firefox | 192 x 192 ≥
Safari | Icônes non configurables sur une base par campagne
Opéra | 192x192 ≥
{: .reset-td-br-1 .reset-td-br-2}

| **Navigateur** | **Plateforme** | **Taille de grande image**
| --- | --- | ---
Chrome | macOS | S.O.
Chrome | Android | 2:1 rapport d’aspect
Chrome | Windows | 360 ≥ x 240
Firefox | macOS| S.O.
Safari | macOS | S.O.
Opéra | macOS | S.O.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Text %}

| **Navigateur** | **Plateforme** | **Longueur maximale du titre**  | **Longueur maximale du corps du message**
| --- | --- | --- | ---
Chrome | macOS | 35 | 50
Safari | macOS | 38 | 84
Firefox | macOS | 38 | 42
Opéra | macOS | 38 | 42
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% endtab %}
{% endtabs %}

[1]: {% image_buster /assets/img/red-dress.gif %}
[2]: {% image_buster /assets/img/ios_push.png %}
[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content
[8]: https://www.braze.com/customers
[7]: https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services
[9]: https://developer.apple.com/app-store/review/guidelines/#unacceptable
[10]: https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories
[23]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users
