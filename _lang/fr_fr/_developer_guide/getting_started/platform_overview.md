---
nav_title: Aperçu de la plate-forme
article_title: Aperçu de la plate-forme
page_order: 1
description: "Cet article traite des composants et capacités de base de la plateforme Braze. Les liens de cet article renvoient à des rubriques essentielles de Braze."
platform:
  - iOS
  - Android
  - Web
  - React Native
  - Flutter
  - Cordova
  - Roku
  - Swift
  - Unity
---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/developer){: style="float:right;width:120px;border:0;" class="noimgborder"}Démarrage : Aperçu de la plate-forme

> Cet article traite des composants et capacités de base de la plateforme Braze. Les liens de cet article renvoient à des rubriques essentielles de Braze. 

{% alert tip %}
Consultez notre [parcours d'apprentissage gratuit pour les développeurs](https://learning.braze.com/path/developer) ainsi que ces articles.
{% endalert %}

## Qu’est-ce que Braze ?

Braze est une plateforme d'engagement client. Cela signifie simplement que Braze vous aide à écouter vos utilisateurs, à comprendre leurs actions et leurs comportements, puis à agir en conséquence. La plateforme Braze se compose de trois éléments principaux : le SDK, le tableau de bord et l'API REST.

Si vous êtes un spécialiste du marketing à la recherche d'un aperçu plus global de Braze, consultez plutôt la [section Démarrer pour les marketeurs]({{site.baseurl}}/user_guide/getting_started/overview/).

![La Braze comporte différentes couches. De manière générale, la plateforme se compose du SDK, de l'API, du tableau de bord et des intégrations partenaires. Chacun de ces éléments contribue à une couche d'ingestion de données, une couche de classification, une couche d'orchestration, une couche de personnalisation et une couche d'action. La couche d'action dispose de plusieurs canaux, notamment les messages in-app, Connected Catalog, webhook, SMS et e-mail.]({% image_buster /assets/img/getting-started/getting-started-vertically-integrated-stack.png %}){: style="max-width:55%;float:right;margin-left:15px;"}

### SDK

Les [SDK de Braze](#integrating-braze) peuvent être intégrés dans vos applications mobiles et web pour fournir de puissants outils de marketing, de gestion des utilisateurs et d'analyse.

En bref, dans le cas d’une intégration complète, le SDK :

* Collecte et synchronise les données de l'utilisateur dans un profil utilisateur consolidé.
* Recueille automatiquement les données de session, les informations sur l’appareil et les jetons push
* Capture les données d’engagement marketing et les données personnalisées spécifiques à votre entreprise
* Est conçu pour la sécurité et fait l'objet de tests de pénétration par des tiers
* est optimisé pour les appareils à faible niveau de batterie ou à réseau lent
* Prise en charge des signatures JWT côté serveur pour une sécurité accrue
* dispose d'un accès en écriture seule à vos systèmes (ne peut pas récupérer les données de l'utilisateur)
* Alimente les canaux de communication de notifications push, de messages in-app et de carte de contenu

### Interface utilisateur du tableau de bord

Le tableau de bord est l'interface utilisateur qui contrôle l'ensemble des données et des interactions au cœur de la plateforme Braze. Les marketeurs utiliseront le tableau de bord pour faire leur travail et créer du contenu. Les développeurs peuvent utiliser le tableau de bord pour gérer les paramètres d’intégration des applications, comme les clés API et les informations d’identification de notifications push.

Si vous débutez, l'administrateur de votre équipe devrait vous ajouter (ainsi que tous les autres membres de l'équipe qui ont besoin d'accéder à Braze) en tant qu' [utilisateurs sur votre tableau de bord.]({{site.baseurl}}/user_guide/administrative/access_braze)

### API REST

L'API de Braze vous permet de déplacer des données à l'intérieur et à l'extérieur de Braze à grande échelle. Utilisez l'API pour apporter des mises à jour depuis votre back-end, vos entrepôts de données et d'autres sources first-party et third-party. En outre, utilisez l'API pour ajouter des événements personnalisés, à des fins de segmentation, directement à partir d'une application Web. Vous pouvez déclencher et envoyer des messages via l'API, ce qui permet aux ressources techniques d'inclure des métadonnées JSON complexes dans le cadre de vos campagnes.

L’API fournit également un service Web où vous pouvez enregistrer des actions prises par vos utilisateurs directement via HTTP, plutôt que par le biais des SDK mobiles et Web. Combiné aux webhooks, cela signifie que vous pouvez suivre les actions et déclencher des actions pour les utilisateurs à l'intérieur et à l'extérieur de votre expérience sur l'application. Le [Guide de l’API]({{site.baseurl}}/api/home) répertorie les endpoints de l'API Braze disponibles et leur utilisation.

Pour en savoir plus sur les différentes parties de Braze, consultez le site : [Pour commencer : Aperçu de l'architecture]({{site.baseurl}}/developer_guide/getting_started/architecture_overview/).

## Analyse des données et action

Les données stockées dans Braze sont conservées et utilisables à des fins de segmentation, de personnalisation et de ciblage tant que vous êtes client de Braze. Cela vous permet d'agir sur les données du profil utilisateur (par exemple, l'activité de la session ou les achats) jusqu'à ce que vous décidiez de supprimer ces informations. Par exemple, un service de diffusion en continu pourrait suivre les contenus consultés par chaque abonné depuis son premier jour sur le service (même si cela remonte à plusieurs années) et utiliser ces données pour envoyer des messages pertinents.

![Un segment du tableau de bord de Braze intitulé "Acheteurs récents" juxtaposé à un écran de téléphone affichant un e-mail "Top Recommandations pour Linda".]({% image_buster /assets/img/getting-started/getting-started-segment.png %}){: style="max-width:80%"}

### Analyse des applications

Le tableau de bord de Braze affiche les graphiques mis à jour en temps réel sur la base d’un certain nombre de mesures d’analyse ainsi que d’événements personnalisés que vous avez utilisés dans votre application. La mesure et l'optimisation constantes de vos campagnes à l'aide de tests A/B, de rapports personnalisés et d'analyses/analytiques, ainsi que de renseignements automatisés vous aident à maintenir l'engagement des clients et à vous démarquer des concurrents dans votre espace.

### Segmentation utilisateur

La segmentation vous permet de créer des groupes d’utilisateurs reposant sur des critères précis de comportement dans l’application, des données démographiques, etc. Braze vous permet également de définir toute action utilisateur in-app comme un « événement personnalisé » si l’action souhaitée n’est pas capturée par défaut. Il en va de même pour les caractéristiques de l’utilisateur via des « attributs personnalisés ». Une fois qu'un segment d'utilisateurs est créé dans le tableau de bord, vos utilisateurs entrent et sortent du segment lorsqu'ils répondent (ou ne répondent pas) aux critères définis. Par exemple, vous pouvez créer un segment qui inclut tous les utilisateurs qui ont dépensé de l'argent in-app et dont la dernière utilisation remonte à plus de deux semaines.

Pour en savoir plus sur nos modèles de données, voir : [Pour commencer : Présentation des analyses]({{site.baseurl}}/developer_guide/getting_started/architecture_overview/).

## Communication multicanale

Après avoir défini un segment, les outils de communication de messages de Braze vous permettent d'engager le dialogue avec vos utilisateurs de manière dynamique et personnalisée. Braze a été conçu avec un modèle de données indépendant des canaux et centré sur l'utilisateur. L'envoi de messages se fait à l'intérieur de votre application ou de votre site (comme l'envoi de messages in-app ou par le biais d'éléments graphiques tels que les carrousels de cartes de contenu et les bannières) ou en dehors de votre expérience sur l'application (comme les notifications push ou les e-mails). Par exemple, vos marketeurs peuvent envoyer une notification push et un e-mail à l’exemple de segment défini dans la section précédente.

![Créez et déclenchez des messages personnalisés sur n'importe quel canal, que ce soit à l'extérieur ou à l'intérieur de votre appli ou site web.]({% image_buster /assets/img/getting-started/messaging-channels.png %}).{: style="border:none" }

| Canal                                                                                              | Description                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/)* | Envoyez des notifications in-app très ciblées et dynamiques sans interrompre le client. |
| [E-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/about/) | Envoyez des messages HTML riches en créant votre e-mail à l'aide de l'éditeur de texte riche, de notre éditeur par glisser-déposer ou en téléchargeant l'un de vos modèles HTML existants. |
| [in-app Messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) | Envoyez des notifications in-app discrètes à l'aide de l'interface utilisateur native créée sur mesure par Braze. |
| [Notification push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/) | Déclenchez automatiquement des notifications push à partir de campagnes de communication ou d'actualités à l'aide du service de notification push d'Apple (APN) pour iOS ou de Firebase Cloud Messaging (FCM) pour Android. |
| [SMS, MMS et RCS\*.]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs) | Utilisez les SMS, MMS ou RCS pour envoyer des notifications transactionnelles, partager des promotions, envoyer des rappels, et plus encore. |
| [Push Web]({{site.baseurl}}/user_guide/message_building_by_channel/push/web) | Envoyez des notifications au navigateur web, même si vos utilisateurs ne sont pas actuellement actifs sur votre site. |
| [Webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) | Utilisez les webhooks pour déclencher des actions hors application, en fournissant à d'autres systèmes et applications des données en temps réel. |
| [WhatsApp*]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/) | Entrez directement en contact avec vos utilisateurs et vos clients avec la plateforme de messagerie pair à pair très plébiscitée : WhatsApp. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<sup>\*\*Disponible en tant que fonctionnalité supplémentaire.</sup>

### Composants personnalisables

{% gallery %}
{{site.baseurl}}/assets/img/getting-started/crawl-example.png <br> Tous les composants de Braze sont conçus pour être accessibles, adaptables et personnalisables. Vous pouvez commencer avec Braze en utilisant les composants par défaut de `BrazeUI` et en les personnalisant en fonction des besoins de votre marque et de votre cas d'utilisation.
{{site.baseurl}}/assets/img/getting-started/walk-example.png <br> Pour aller au-delà des options par défaut, vous pouvez écrire un code personnalisé pour mettre à jour l'aspect et la convivialité d'un canal de communication afin qu'il corresponde mieux à votre marque. Il s'agit notamment de modifier le type de police, la taille de la police et les couleurs d'un composant. Les marketeurs conservent le contrôle de l’audience, de contenu, du comportement lors du clic et de l’expiration directement dans le tableau de bord de Braze.
{{site.baseurl}}/assets/img/getting-started/run-example.png <br> Vous pouvez également créer des composants entièrement personnalisés pour contrôler l'aspect de vos messages, leur comportement et leur interaction avec d'autres canaux d'envoi de messages (par exemple, déclenchement d'une carte de contenu sur la base d'une notification push). Braze fournit des méthodes SDK pour vous permettre d'enregistrer des indicateurs tels que les impressions, les clics et les rejets dans le tableau de bord de Braze. Chaque canal de communication dispose d'un article d'analyses pour faciliter cette démarche.
{% endgallery %}

<br>
<br>

## Intégration de Braze

La plateforme Braze a été conçue pour être rapidement et facilement opérationnelle. Notre délai moyen de rentabilisation est de six semaines pour notre clientèle composée de centaines de marques. Pour en savoir plus sur le processus d'intégration, voir : [Pour commencer : Aperçu de l'intégration]({{site.baseurl}}/developer_guide/getting_started/integration_overview/).

## Ressources à mettre en favoris

En tant que ressource technique, vous interviendrez dans une grande partie des rouages de Braze. En plus de notre documentation, voici des ressources utiles à conserver dans vos favoris. Au fur et à mesure que vous avancez, gardez notre glossaire des [termes à connaître]({{site.baseurl}}/user_guide/getting_started/terms_to_know/) à portée de main au cas où vous auriez des questions sur des termes propres à Braze.

| Ressources | Ce que vous allez apprendre|
|---|---|
| [Débogage du SDK]({{site.baseurl}}/developer_guide/sdk_integration/debugging) | Lors de la résolution des problèmes de votre intégration, l'outil de débogage du SDK vous sera d'une grande utilité. Assurez-vous de l'avoir sous la main ! |
| [Référentiel GitHub public Braze](https://github.com/braze-inc/) | Vous trouverez, dans notre référentiel GitHub, des informations détaillées sur l'intégration ainsi que des exemples de code. |
| [Référentiel GitHub du SDK Android](https://github.com/braze-inc/braze-android-sdk/) | Le dépôt GitHub du SDK Android. |
| [Référence SDK Android](https://appboy.github.io/appboy-android-sdk/kdoc/index.html) | Documentation des classes pour le SDK Android. |
| [Référentiel GitHub du SDK iOS (Swift)](https://github.com/braze-inc/braze-swift-sdk) | Référentiel GitHub du SDK Swift. |
| [Référence SDK iOS (Swift)](https://braze-inc.github.io/braze-swift-sdk/) | Documentation des classes pour le SDK iOS. |
| [Référentiel GitHub du SDK Web](https://github.com/braze-inc/braze-web-sdk) | Référentiel GitHub du SDK Web. |
| [Référence SDK Web](https://js.appboycdn.com/web-sdk/5.0/doc/modules/braze.html) | Documentation des classes pour le SDK iOS. |
| [Journaux de modifications SDK]({{site.baseurl}}/developer_guide/changelogs) | Braze propose des prédictions mensuelles, en plus des lancements de versions ciblant les problèmes critiques et les mises à jour majeures du système d'exploitation. |
| [Collection Postman de l'API Braze](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest) | Téléchargez notre collection Postman ici.  |
| [Moniteur d'état du système Braze](https://braze.statuspage.io/) | Notre page d'état est mise à jour chaque fois qu'il y a des incidents ou des pannes. Rendez-vous sur cette page pour vous abonner aux alertes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

