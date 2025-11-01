---
nav_title: Pousser
article_title: Pousser
page_order: 4
layout: dev_guide
guide_top_header: "Pousser"
guide_top_text: "Les notifications push sont un moyen éprouvé d'envoyer des appels à l'action sensibles au facteur temps via le mobile ou le web, ainsi que de réengager les utilisateurs qui ne sont pas venus dans l'application depuis un certain temps. Ils conduisent l'utilisateur directement au contenu et démontrent la valeur de votre application. Les notifications push sont utiles pour conduire les utilisateurs à un endroit précis, mais vous devez les utiliser à bon escient. <br><br> Lisez l'un des articles suivants ou consultez notre [cours d'apprentissage Push Braze] (https://learning.braze.com/messaging-channels-push) pour savoir à qui vous pouvez envoyer un message push, comment l'envoyer et quelles sont les possibilités d'avancement offertes par Braze. Pour des exemples de notifications push, consultez nos [témoignages de clients] (https://www.braze.com/customers)."
description: "Cette page d'atterrissage accueille des messages push. Vous y trouverez des articles sur les types de push, l'enregistrement de push, l'activation de push, les amorces de push, les rapports de push, et plus encore."
channel:
  - push

guide_featured_title: "Articles populaires"
guide_featured_list:
- name: Types de poussée
  link: /docs/user_guide/message_building_by_channel/push/types/
  image: /assets/img/braze_icons/list.svg
- name: "Pousser l'enregistrement"
  link: /docs/user_guide/message_building_by_channel/push/push_registration/
  image: /assets/img/braze_icons/check-square-broken.svg
- name: Activation de la poussée et abonnement
  link: /docs/user_guide/message_building_by_channel/push/users_and_subscriptions/
  image: /assets/img/braze_icons/users-01.svg
- name: "Création d'un message push"
  link: /docs/user_guide/message_building_by_channel/push/creating_a_push_message/
  image: /assets/img/braze_icons/edit-05.svg

guide_menu_title: "More articles"
guide_menu_list:
- name: Options avancées
  link: /docs/user_guide/message_building_by_channel/push/advanced_push_options/
  image: /assets/img/braze_icons/settings-01.svg
- name: Amorces à pousser
  link: /docs/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/
  image: /assets/img/braze_icons/phone-02.svg
- name: Rapports
  link: /docs/user_guide/message_building_by_channel/push/push_reporting/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: Options Android
  link: /docs/user_guide/message_building_by_channel/push/android/
  image: /assets/img/braze_icons/android.svg
- name: Options iOS
  link: /docs/user_guide/message_building_by_channel/push/ios/
  image: /assets/img/braze_icons/apple.svg
- name: Web Push
  link: /docs/user_guide/message_building_by_channel/push/web/
  image: /assets/img/braze_icons/monitor-01.svg
- name: Meilleures pratiques
  link: /docs/user_guide/message_building_by_channel/push/best_practices/
  image: /assets/img/braze_icons/check-square-broken.svg
- name: Locales dans les messages
  link: /docs/locales_in_messages/
  image: /assets/img/braze_icons/translate-01.svg
- name: "Messages d'erreur communs à Push"
  link: /docs/user_guide/message_building_by_channel/push/push_error_codes/
  image: /assets/img/braze_icons/alert-triangle.svg
- name: Résolution des problèmes
  link: /docs/user_guide/message_building_by_channel/push/troubleshooting/
  image: /assets/img/braze_icons/annotation-question.svg
- name: Questions fréquemment posées
  link: /docs/user_guide/message_building_by_channel/push/faq/
  image: /assets/img/braze_icons/annotation-question.svg
---

## ![cours d'apprentissage de Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/push-fundamentals){: style="float:right;width:120px;border:0;" class="noimgborder"} Cas d'utilisation

\![Exemple de message push sur l'ensemble des produits Apple.]({% image_buster /assets/img/red-dress.gif %}){: height="400px"} \![Exemple de message push de Stopwatch sur l'écran d'accueil d'un iPhone : "Bonjour ! Il s'agit d'un "push" d'iOS.]({% image_buster /assets/img/ios_push.png %}){: height="400px"}

Les notifications push sont un outil d'engagement formidable pour attirer de nouveaux utilisateurs et faire des campagnes de réengagement. Voici quelques exemples d'utilisations courantes des messages push.

| Cas d'utilisation | Explication |
| -------- | ----------- |
| Onboarding initial | Tant que les utilisateurs n'ont pas franchi les premières étapes de l'utilisation de votre application (comme l'enregistrement d'un compte), leur valeur est fortement limitée. Utilisez des notifications push pour inciter les utilisateurs à franchir ces étapes afin qu'ils puissent commencer à utiliser pleinement votre appli. |
| Premiers achats | Une fois que les utilisateurs sont à l'aise avec votre application, vous pouvez utiliser les notifications push pour les aider à se convertir en acheteurs in-app. |
| Nouvelles fonctionnalités | Les notifications push peuvent être efficaces pour informer les utilisateurs désengagés des nouvelles fonctionnalités susceptibles de les inciter à revenir sur votre appli. |
| Offres sensibles au temps | Si votre offre est assortie d'une date butoir, le push est parfois un excellent moyen d'en informer vos utilisateurs avant qu'elle n'expire. Ces messages comportent généralement un fort sentiment d'urgence et sont optimaux pour rappeler votre application aux utilisateurs qui l'ont récemment abandonnée.<br><br> Supposons par exemple que votre application soit un jeu et que vous offriez à vos utilisateurs un bonus en monnaie de jeu s'ils continuent à jouer quotidiennement au jeu. Alerter un utilisateur que sa série risque d'être interrompue pourrait être une incitation raisonnable s'il a dépassé un certain nombre de jours. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour plus d'informations sur le réengagement des anciens utilisateurs, consultez notre page " [Quick Wins"]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users) sur le sujet.

## Conditions préalables à l'utilisation de push

Avant de pouvoir créer et envoyer tout message in-app à l'aide de Braze, vous devez travailler avec vos développeurs pour intégrer push dans votre site web ou votre app. Pour connaître les étapes détaillées, consultez nos guides d'intégration pour chaque plateforme :

- [iOS]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android)
- [Web]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)

## Amorçage de push

Gardez à l'esprit que les utilisateurs doivent accepter le push pour recevoir vos messages, ce qui signifie qu'il est judicieux d'utiliser des messages in-app pour expliquer à vos clients pourquoi vous souhaitez leur envoyer des notifications push, et en quoi l'activation du push leur sera bénéfique. Ce processus est appelé [amorçage de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

## Envoi de messages réglementaires

Les messages in-app étant un type d'envoi intrusif qui s'adresse directement au téléphone ou au navigateur de votre client, il existe des directives concernant l'envoi de messages in-app par le biais d'applications et de sites.

### Réglementation de la poussée mobile pour les applications

{% alert important %}
Vos messages in-app doivent respecter les règles de l'App Store d'Apple et du Play Store de Google, notamment en ce qui concerne l'utilisation des messages in-app comme publicités, spams, promotions, etc.
{% endalert %}

|Politiques de l'App Store d'Apple|
|---|
|[3.2.2](https://developer.apple.com/app-store/review/guidelines/#unacceptable) Inacceptable : (i) Créer une interface pour afficher des applications, des extensions ou des plug-ins de tiers similaires à l'App Store ou en tant que collection d'intérêt général.| 
|[4.5.4](https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services) Les notifications push ne doivent pas être nécessaires au fonctionnement de l'app et ne doivent pas être utilisées pour envoyer des informations personnelles sensibles ou confidentielles. Les notifications push ne doivent pas être utilisées à des fins de promotion ou de marketing direct, sauf si les clients ont explicitement choisi de les recevoir via un langage de consentement affiché dans l'interface utilisateur de votre application, et si vous fournissez une méthode dans votre application permettant à un utilisateur de refuser de recevoir de tels messages.|
|[4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) Vous ne pouvez pas monétiser les capacités intégrées fournies par le matériel ou le système d'exploitation, telles que les notifications Push, l'appareil photo ou le gyroscope ; ou les services et technologies Apple, tels que l'accès à Apple Music, le stockage iCloud ou les API de temps d'écran.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

|Règles de la boutique Google Play|
|---|
|[Utilisation non autorisée ou imitation de la fonctionnalité du système](https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories) Nous n'autorisons pas les applications ou les publicités qui imitent ou interfèrent avec la fonctionnalité du système, comme les notifications ou les avertissements. Les notifications au niveau du système ne peuvent être utilisées que pour les fonctionnalités intégrales d'une application, comme l'application d'une compagnie aérienne qui informe les utilisateurs des offres spéciales, ou un jeu qui informe les utilisateurs des promotions en cours de jeu.|
{: .reset-td-br-1 role="presentation" }
