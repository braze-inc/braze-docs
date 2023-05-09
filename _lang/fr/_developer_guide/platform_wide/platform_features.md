---
nav_title: Caractéristiques de la plateforme
article_title: Caractéristiques de la plateforme
page_order: 0
description: "Cet article de référence couvre des fonctionnalités spécifiques de la plateforme, notamment les tailles de SDK, l’interface utilisateur de tableau de bord, les données API, la messagerie multicanal, etc."
platform:
  - iOS
  - Android
  - Web
  
---

# Caractéristiques de la plateforme

> Braze offre une solution complète d’engagement utilisateur pour vos applications mobiles et Web. La plateforme Braze comporte trois composants principaux : le SDK, le tableau de bord et l’API de données.

## SDK

Les SDK Braze peuvent être intégrés à vos applications mobiles et Web pour offrir des outils de marketing, de support client et d’analyse performants.

## Interface utilisateur du tableau de bord

Le tableau de bord contrôle toutes les données et interactions au cœur de la plateforme Braze. Les marketeurs peuvent utiliser le site pour gérer les notifications, configurer les campagnes de messagerie ciblées et afficher les analyses. Les développeurs peuvent utiliser le tableau de bord pour gérer les paramètres d’intégration des applications, comme les clés API et les informations d’identification de notification push.

## API de données

L’API de données Braze fournit un service Web où vous pouvez enregistrer des actions prises par vos utilisateurs directement via HTTP, plutôt que par le biais des SDK mobiles et Web. Cela vous permet d’ajouter des événements personnalisés à des fins de segmentation directement à partir d’une application Web.

## Ciblage et analyse granulaires

### Analyse des applications
Le tableau de bord de Braze affiche les graphiques mis à jour en temps réel sur la base d’un certain nombre de mesures d’analyse ainsi que d’événements personnalisés que vous avez utilisés dans votre application.

### Segmentation utilisateur

La segmentation vous permet de créer des groupes d’utilisateurs reposant sur des critères précis de comportement dans l’application, des données démographiques, etc. Braze vous permet également de définir toute action utilisateur in-app comme un « événement personnalisé » si l’action souhaitée n’est pas capturée par défaut. Il en va de même pour les caractéristiques de l’utilisateur via des « attributs personnalisés ». Une fois qu’un segment utilisateur est créé sur le tableau de bord, vos utilisateurs entreront et sortiront du segment selon qu’ils remplissent (ou ne remplissent pas) les critères définis. Par exemple, l’image suivante montre un segment qui inclut tous les utilisateurs qui ont dépensé de l’argent dans l’application et qui ont utilisé l’application il y a plus de deux semaines.

![Un exemple de segment où les filtres « Dernier achat effectué il y a plus de 7 jours » et « Dernière utilisation de ces applications il y a plus de 4 semaines » sont définis.][2]

## Messagerie multicanal

Une fois que vous avez défini un segment, les outils de messagerie de Braze permettent une communication multicanal avec vos utilisateurs. Par exemple, envoyez une notification push et un e-mail à l’exemple de segment défini dans la section précédente. Il est préférable d'utiliser les canaux de communication de manière conjointe et régulière afin de réengager les utilisateurs perdus, fidéliser les utilisateurs actifs et dynamiser les ambassadeurs de votre marque. De plus, vous pouvez utiliser nos options de planification avancée pour automatiser les campagnes destinées à des groupes spécifiques de ces utilisateurs à l’avenir.

{% alert tip %}
Vous pouvez utiliser Braze pour créer des campagnes de communication accessibles sur chaque canal. Vérifiez avec vos ingénieurs que vous répondez aux normes d’accessibilité lors de la mise en place.
{% endalert %}

### Cartes de contenu {#platform-features-content-cards}

Avec les cartes de contenu, vous pouvez envoyer un flux dynamique et hautement ciblé de contenu riche à vos clients, dans les applications qu’ils aiment, sans interrompre leur expérience. De plus, les cartes de contenu prennent en charge des fonctionnalités plus personnalisées, notamment l’épinglage des cartes, la fermeture de carte de contenu, la diffusion par API, un contenu connecté, des délais d’expiration de carte personnalisés, des métriques des performances et une coordination aisée avec les notifications push.

![Image mobile générique illustrant la bannière, l’image légendée et le look de la Classic Content Card côte à côte.]({% image_buster /assets/img/cc_feed_new.png %}){: style="max-width:60%"}

### Notifications push {#platform-features-push}

Braze prend en charge le service de notification Push Apple (APNS) pour iOS et Firebase Cloud Messaging (FCM) pour Android. Les notifications push peuvent être déclenchées par la publication de campagnes de communication et d’articles d’actualités.

![Éditeur de messages push affichant un exemple de message push et de titre à envoyer aux canaux de communication Android, iOS et Web.][8]

### Envoi de messages in-app {#platform-features-in-app-messaging}

Braze fournit des notifications intégrées dans les applications via notre interface utilisateur native intégrée. Les messages peuvent être présentés à tout moment de votre choix (p. ex., lorsque les utilisateurs commencent une nouvelle session ou effectuent une action spécifique), ce qui garantit que votre message arrive au moment le plus opportun pour engager l’utilisateur. En savoir plus sur [créer un message dans l’application][13].

![Éditeur de messages in-app affichant un exemple de message in-app avec un en-tête, un corps et un texte de bouton.][9]

### E-mail {#platform-features-email}

Envoyez à vos utilisateurs des messages HTML riches en ajoutant vos modèles HTML existants, en utilisant notre éditeur de texte enrichi ou notre éditeur de glisser-déposer. Braze vous permet d’inclure facilement des e-mails dans le cadre de votre stratégie d’engagement mobile.

![Éditeur de courrier électronique affichant le corps HTML d’un e-mail. Ici, vous pouvez également voir les onglets pour mettre à jour les informations d’envoi, afficher un aperçu en direct de l’e-mail ou ajouter du contenu à partir de la bibliothèque de contenu.][10]

### SMS et MMS {#platform-features-sms-mms}

Utilisez les SMS avec Braze pour envoyer des notifications transactionnelles, partager des promotions, envoyer des rappels, et bien plus encore. Plus de 23 milliards de messages de texte sont envoyés chaque jour dans le monde entier, les SMS étant la façon la plus directe d’atteindre les utilisateurs et les clients.

![Éditeur de messages SMS et MMS affichant un exemple de message.]({% image_buster /assets/img_archive/sms_preview.png %})

### Webhooks {#platform-features-webhooks}

Les Webhooks de Braze vous permettent de déclencher des actions hors application, d’autres systèmes et applications avec des informations en temps réel. La flexibilité de cette fonctionnalité vous permet d’envoyer des informations à n’importe quel endpoint.

![Éditeur de Webhook affichant un exemple de charge utile de Webhook.][22]

[2]: {% image_buster /assets/img_archive/dashboard_segment_example.png %} "Segmentation Example"
[4]: http://en.wikipedia.org/wiki/Dayparting
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#deep-links
[8]: {% image_buster /assets/img_archive/UOiOSPush.png %} "Example Push dashboard"
[9]: {% image_buster /assets/img_archive/In-App_Modal.png %} "Slideup Example"
[10]: {% image_buster /assets/img_archive/EmailTemplateEditor.png %} "Email Template Editor"
[22]: {% image_buster /assets/img_archive/Webhook_Body_Edit.png %}
[13]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#creating-an-in-app-message
