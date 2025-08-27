---
nav_title: "À propos des notifications push"
article_title: À propos des notifications push
page_order: 0
page_type: reference
description: "Le présent article de référence donne un bref aperçu des notifications push, fournit des ressources pour débuter dans les messages de notification push et présente certaines réglementations."
channel:
  - Push

---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-push){: style="float:right;width:120px;border:0;" class="noimgborder"}À propos de notifications push

> Les notifications push sont idéales pour les appels à l’action urgents, ainsi que pour le ré-engagement des utilisateurs qui n’ont pas utilisé l’application depuis un certain temps. Les campagnes de notifications push réussies amènent l’utilisateur directement au contenu et démontrent la valeur de votre application.

Gardez à l’esprit que les utilisateurs doivent s’abonner pour recevoir vos messages, ce qui signifie qu’il peut être intéressant d’utiliser des messages in-app pour expliquer à vos clients pourquoi vous voulez leur envoyer des notifications push et en quoi leur activation leur sera bénéfique. Ce processus est appelé [amorçage de notification push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

![Exemple de message push sur les produits Apple.]({% image_buster /assets/img/red-dress.gif %}){: height="400px"}  ![Exemple de message push de Stopwatch sur l'écran d'accueil d'un iPhone : « Bonjour ! Il s'agit d'un "Push" iOS.]({% image_buster /assets/img/ios_push.png %}){: height="400px"}

Pour voir d'autres exemples de notifications push, consultez nos [études de cas.](https://www.braze.com/customers)

## Cas d’usage potentiels

Les notifications push constituent un outil formidable pour attirer de nouveaux utilisateurs et conduire des campagnes de ré-engagement. Voici quelques exemples de cas d’utilisation courants de messages de notification push.

| Cas d’utilisation | Explication |
| -------- | ----------- |
| Onboarding initial | Tant que les utilisateurs n'ont pas franchi les premières étapes de l'utilisation de votre application (comme l'enregistrement d'un compte), leur valeur est fortement limitée. Utilisez des notifications push pour inciter les utilisateurs à effectuer ces étapes afin qu’ils puissent commencer à utiliser votre application dans sa totalité. |
| Premiers achats | Une fois que les utilisateurs sont à l’aise dans l’utilisation de votre application, vous pouvez utiliser des notifications push pour les convertir en acheteurs in-app. |
| Nouvelles fonctionnalités | Les notifications push peuvent être efficaces pour informer les utilisateurs désengagés de nouvelles fonctionnalités susceptibles de les attirer à nouveau vers votre application. |
| Offres limitées dans le temps | Si vous avez une offre qui va disparaître, une notification push peut parfois être un excellent moyen d’en parler à vos utilisateurs avant son expiration. Ces messages transmettent généralement une notion claire de l’urgence et sont optimaux pour rappeler votre application aux utilisateurs récemment inactifs.<br><br> Par exemple, supposons que votre application soit un jeu et que vous offrez à vos utilisateurs un bonus de monnaie du jeu s’ils maintiennent une habitude de jouer au jeu quotidiennement. Signaler à un utilisateur que cette série de connexions risque d’être brisée peut constituer une notification push raisonnable s’il a dépassé un certain nombre de jours. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour plus d'informations sur le réengagement des utilisateurs qui n'ont plus d'ancienneté, consultez notre page " [Quick Wins "]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users) sur le sujet.

## Conditions préalables à l’utilisation de notification push

Avant de pouvoir créer et envoyer des messages de notification push à l’aide de Braze, vous devez travailler avec vos développeurs pour les intégrer à votre site Internet ou à votre application. Pour des instructions détaillées, consultez nos guides d’intégration pour chaque plateforme :

- [iOS]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android)
- [Web]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)

## Réglementations relatives aux messages de notification push

Les messages de notification push étant un type de messages intrusif qui est envoyé directement vers le téléphone ou le navigateur de votre client, il existe des directives pour envoyer des messages de notification push via des applications et des sites.

### Réglementations des notifications push mobiles pour les applications

{% alert important %}
Vos messages de notification push doivent être conformes aux directives de l’App Store d’Apple et des politiques de Google Play Store, en particulier concernant l’utilisation de messages de notification push en tant que publicités, spam, promotions, etc.
{% endalert %}

|Politiques de l’App Store d’Apple|
|---|
|[3.2.2](https://developer.apple.com/app-store/review/guidelines/#unacceptable) Inacceptable : (i) Créer une interface pour afficher des applications, des extensions ou des plug-ins de tiers similaires à l'App Store ou en tant que collection d'intérêt général.| 
|[4.5.4](https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services) Les notifications push ne doivent pas être nécessaires au fonctionnement de l'app et ne doivent pas être utilisées pour envoyer des informations personnelles ou confidentielles sensibles. Les notifications push ne doivent pas être utilisées à des fins de promotion ou de marketing direct, sauf si les clients ont explicitement choisi de les recevoir via un langage de consentement affiché dans l'interface utilisateur de votre application, et si vous fournissez une méthode dans votre application pour qu'un utilisateur puisse refuser de recevoir de tels messages.|
|[4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) Vous ne pouvez pas monétiser les capacités intégrées fournies par le matériel ou le système d'exploitation, telles que les notifications Push, l'appareil photo ou le gyroscope ; ou les services et technologies Apple, tels que l'accès à Apple Music, le stockage iCloud ou les API de temps d'écran.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

|Politique de Google Play Store|
|---|
|[Utilisation non autorisée ou imitation de la fonctionnalité du système](https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories) Nous n'autorisons pas les applications ou les publicités qui imitent ou interfèrent avec la fonctionnalité du système, comme les notifications ou les avertissements. Les notifications au niveau du système ne peuvent être utilisées que pour les fonctionnalités intégrales d'une application, comme l'application d'une compagnie aérienne qui informe les utilisateurs des offres spéciales, ou un jeu qui informe les utilisateurs des promotions en cours de jeu.|
{: .reset-td-br-1 role="presentation" }

