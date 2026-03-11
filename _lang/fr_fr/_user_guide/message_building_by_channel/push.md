---
nav_title: Notification push
article_title: Notification push
page_order: 4
layout: dev_guide
guide_top_header: "Notification push"
guide_top_text: "Les notifications push constituent un moyen éprouvé d'envoyer des appels à l'action urgents via mobile ou Internet, ainsi que de favoriser le réengagement des utilisateurs qui n'ont pas utilisé l'application depuis un certain temps. Ils dirigent l'utilisateur directement vers le contenu et démontrent la valeur de votre application. Les notifications push sont utiles pour diriger les utilisateurs vers un endroit spécifique, mais il est important de les utiliser avec discernement. <br><br> Lisez l'un des articles suivants ou consultez notre [cours d'apprentissage Braze sur les notifications Push](https://learning.braze.com/messaging-channels-push) pour savoir à qui vous pouvez envoyer une notification push, comment l'envoyer et quelles sont les fonctionnalités avancées offertes par Braze pour les notifications push. Pour des exemples de notifications push, veuillez consulter nos [témoignages clients](https://www.braze.com/customers)."
description: "Cette page d’accueil contient tous les messages push. Vous trouverez ici des articles sur les types de notification push, l’inscription aux notifications push, l’activation des notifications push, les amorces de notification push, le reporting des notifications push, etc."
channel:
  - push

guide_featured_title: "Articles populaires"
guide_featured_list:
- name: Types de notifications push
  link: /docs/user_guide/message_building_by_channel/push/types/
  image: /assets/img/braze_icons/list.svg
- name: Enregistrement d’une notification push
  link: /docs/user_guide/message_building_by_channel/push/push_registration/
  image: /assets/img/braze_icons/check-square-broken.svg
- name: Activation et abonnement aux notifications push
  link: /docs/user_guide/message_building_by_channel/push/users_and_subscriptions/
  image: /assets/img/braze_icons/users-01.svg
- name: Créer un message push
  link: /docs/user_guide/message_building_by_channel/push/creating_a_push_message/
  image: /assets/img/braze_icons/edit-05.svg

guide_menu_title: "More articles"
guide_menu_list:
- name: Options avancées
  link: /docs/user_guide/message_building_by_channel/push/advanced_push_options/
  image: /assets/img/braze_icons/settings-01.svg
- name: Amorces de notifications push
  link: /docs/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/
  image: /assets/img/braze_icons/phone-02.svg
- name: Reporting
  link: /docs/user_guide/message_building_by_channel/push/push_reporting/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: Options Android
  link: /docs/user_guide/message_building_by_channel/push/android/
  image: /assets/img/braze_icons/android.svg
- name: Options iOS
  link: /docs/user_guide/message_building_by_channel/push/ios/
  image: /assets/img/braze_icons/apple.svg
- name: Notification push Web
  link: /docs/user_guide/message_building_by_channel/push/web/
  image: /assets/img/braze_icons/monitor-01.svg
- name: Bonnes pratiques
  link: /docs/user_guide/message_building_by_channel/push/best_practices/
  image: /assets/img/braze_icons/check-square-broken.svg
- name: Locales dans les messages
  link: /docs/locales_in_messages/
  image: /assets/img/braze_icons/translate-01.svg
- name: Messages d’erreur « Push » courants
  link: /docs/user_guide/message_building_by_channel/push/push_error_codes/
  image: /assets/img/braze_icons/alert-triangle.svg
- name: Résolution des problèmes
  link: /docs/user_guide/message_building_by_channel/push/troubleshooting/
  image: /assets/img/braze_icons/annotation-question.svg
- name: Foire aux questions
  link: /docs/user_guide/message_building_by_channel/push/faq/
  image: /assets/img/braze_icons/annotation-question.svg
---

## [![C](https://learning.braze.com/path/push-fundamentals)ours[]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/push-fundamentals){: style="float:right;width:120px;border:0;" class="noimgborder"} [Braze Learning](https://learning.braze.com/path/push-fundamentals) Cas d'utilisation

![Exemple de message de notification push pour des produits Apple.]({% image_buster /assets/img/red-dress.gif %}){: height="400px"}  ![Exemple de message de notification push de Stopwatch sur un écran d’accueil iPhone qui affiche : « Bonjour ! Ceci est une notification push iOS ».]({% image_buster /assets/img/ios_push.png %}){: height="400px"}

Les notifications push constituent un outil formidable pour attirer de nouveaux utilisateurs et conduire des campagnes de ré-engagement. Voici quelques exemples de cas d’utilisation courants de messages de notification push.

| Cas d’utilisation | Explication |
| -------- | ----------- |
| Onboarding initial | Tant que les utilisateurs n'ont pas franchi les premières étapes de l'utilisation de votre application (comme l'enregistrement d'un compte), leur valeur est fortement limitée. Utilisez des notifications push pour inciter les utilisateurs à effectuer ces étapes afin qu’ils puissent commencer à utiliser votre application dans sa totalité. |
| Premiers achats | Une fois que les utilisateurs sont à l’aise dans l’utilisation de votre application, vous pouvez utiliser des notifications push pour les convertir en acheteurs in-app. |
| Nouvelles fonctionnalités | Les notifications push peuvent être efficaces pour informer les utilisateurs désengagés de nouvelles fonctionnalités susceptibles de les attirer à nouveau vers votre application. |
| Offres limitées dans le temps | Si vous avez une offre qui va disparaître, une notification push peut parfois être un excellent moyen d’en parler à vos utilisateurs avant son expiration. Ces messages transmettent généralement une notion claire de l’urgence et sont optimaux pour rappeler votre application aux utilisateurs récemment inactifs.<br><br> Par exemple, supposons que votre application soit un jeu et que vous offrez à vos utilisateurs un bonus de monnaie du jeu s’ils maintiennent une habitude de jouer au jeu quotidiennement. Il pourrait être judicieux d'alerter un utilisateur que sa série risque d'être interrompue s'il a dépassé un certain nombre de jours. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour plus d'informations sur le réengagement des utilisateurs qui n'ont plus d'ancienneté, consultez notre page " [Quick Wins "]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users) sur le sujet.

## Conditions préalables à l’utilisation de notification push

Avant de pouvoir créer et envoyer des messages de notification push à l’aide de Braze, vous devez travailler avec vos développeurs pour les intégrer à votre site Internet ou à votre application. Pour des instructions détaillées, consultez nos guides d’intégration pour chaque plateforme :

- [iOS]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android)
- [Web]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)

## Amorçage de notification push

Gardez à l’esprit que les utilisateurs doivent s’abonner pour recevoir vos messages, ce qui signifie qu’il peut être intéressant d’utiliser des messages in-app pour expliquer à vos clients pourquoi vous voulez leur envoyer des notifications push et en quoi leur activation leur sera bénéfique. Ce processus est appelé [amorçage de notification push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

## Réglementations relatives aux messages de notification push

Les messages push étant un type d'envoi de messages intrusif qui s'affiche directement sur le téléphone ou le navigateur de vos clients, il existe des directives relatives à leur envoi via des applications et des sites.

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
