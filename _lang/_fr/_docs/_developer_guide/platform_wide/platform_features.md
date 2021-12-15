---
nav_title: Fonctionnalités de la plateforme
article_title: Fonctionnalités de la plateforme
page_order: 0
description: "Cet article de référence couvre des fonctionnalités spécifiques de la plate-forme, y compris les tailles du SDK, l'interface utilisateur du tableau de bord, la messagerie multi-canaux et bien plus encore."
platform:
  - iOS
  - Android
  - Web
---

# Fonctionnalités de la plateforme

Braze fournit une solution complète d'engagement utilisateur pour vos applications mobiles et web. La plateforme Braze a trois composants principaux : le SDK, le tableau de bord et l'API de données.

## SDK

Les SDKs de Braze peuvent être intégrés dans vos applications mobiles et web pour fournir des outils puissants de marketing, de support client et d'analyse.

| Plateforme | Taille approximative du SDK                              |
| ---------- | -------------------------------------------------------- |
| Android    | 800 Ko                                                   |
| iOS        | (IPA - Addition to App File) 1MB - 2MB; (Framework) 30MB |
| Web        | 35 Ko                                                    |
{: .reset-td-br-1 .reset-td-br-2}

## Tableau de bord/UI

Le tableau de bord contrôle toutes les données et interactions au cœur de la plateforme Braze. Les marketeurs peuvent utiliser le site pour gérer les notifications, configurer les campagnes de messagerie ciblées et afficher les analyses. Les développeurs peuvent utiliser le tableau de bord pour gérer les paramètres d'intégration des applications, telles que les clés API et les identifiants de notification push.

## API de données

L'API de données de Braze fournit un service web où vous pouvez enregistrer les actions prises par vos utilisateurs directement via HTTP, plutôt que par le biais des SDK mobiles et web. Cela vous permet d'ajouter des événements personnalisés à des fins de segmentation directement à partir d'une application web.

## Ciblage et analyse granulaires

### Analyses de l'application
Le tableau de bord Braze affiche des graphiques qui sont mis à jour en temps réel en se basant sur un certain nombre de métriques d'analyse ainsi que sur des événements personnalisés que vous utilisez dans votre application.

### Segmentation de l'utilisateur

La segmentation vous permet de créer des groupes d'utilisateurs basés sur des filtres puissants de leur comportement dans l'application, des données démographiques, des données sociales, etc. Braze vous permet également de définir toute action de l'utilisateur dans l'application comme un "événement personnalisé" si l'action désirée n'est pas capturée par défaut. Il en va de même pour les caractéristiques de l'utilisateur via "attributs personnalisés". Une fois qu'un segment utilisateur est créé sur le tableau de bord, vos utilisateurs se déplaceront dans et hors du segment quand ils rencontrent (ou ne répondent pas) les critères définis. Par exemple, l'image ci-dessous montre un segment qui inclut tous les utilisateurs qui ont dépensé de l'argent dans l'application et qui ont utilisé l'application il y a plus de deux semaines.

!\[Exemple de segmentation\]\[2\]

## Messagerie multi-canal

Une fois que vous avez défini un segment, les outils de messagerie de Braze permettent la communication multicanale avec vos utilisateurs. Par exemple, envoyez une notification push et un courriel au segment d'exemple défini dans la section précédente. Les canaux de messagerie sont mieux utilisés en concert et avec régularité pour réengager les utilisateurs perdus, retenir les utilisateurs actifs et dynamiser les ambassadeurs de votre marque. De plus, vous pouvez utiliser nos options de planification avancées pour automatiser les campagnes vers des groupes spécifiques de ces utilisateurs qui vont plus loin.

### Flux d'actualité {#platform-features-news-feed}

Quand votre application s'ouvre, le Braze SDK tire automatiquement vers le bas le fil d'actualité de l'utilisateur -- un ensemble d'articles d'actualités qui sont contrôlés sur le tableau de bord Braze. En faisant un appel à la bibliothèque Braze, vous pouvez afficher le flux d'actualités lorsqu'un bouton ou une action est déclenchée dans votre application, en fournissant un centre de notification intégré qui peut être mis à jour par des membres non techniques de l'équipe sans avoir à modifier votre code ou votre base de données.

- Braze va suivre combien de clics et d'impressions chaque carte dans le flux de nouvelles reçoit
- Vous pouvez planifier une période spécifique quand les cartes s'affichent, ce qui permet de profonds [dayparting][4]
- Les cartes dans le flux d'actualités peuvent être ciblées sur les segments des utilisateurs comme tout autre message
- Les messages dans l'application apparaîtront automatiquement lorsqu'un utilisateur a de nouveaux éléments dans son fil d'actualité
- Les éléments du flux d'actualités peuvent [« Lien profond»][5] vers le contenu dans l'application, ce qui permet au marketeur de fournir une navigation de contenu personnalisée pour chaque utilisateur. Tous les processus, de l'intégration à la surface de contenu riche dans l'application, peuvent être ciblés et personnalisés sur le plan comportemental en utilisant le fil d'actualité et ["Deep Links"][5]

!\[Tableau de bord des fils d'actualités\]\[6\]

### Notifications push {#platform-features-push}

Braze prend en charge le service Apple Push Notification Service (APN) pour iOS et Firebase Cloud Messaging (FCM) pour Android. Les notifications push peuvent être déclenchées par la publication de campagnes de messagerie et d'actualités.

!\[Exemple de tableau de bord Push\]\[8\]

### Messagerie intégrée {#platform-features-in-app-messaging}

Braze fournit des notifications discrètes dans l'application via notre interface utilisateur native sur mesure. Les messages peuvent être présentés à tout moment de votre choix (par ex. lorsque les utilisateurs démarrent une nouvelle session ou effectuent une action spécifique) en s'assurant que votre message arrive au moment le plus efficace pour engager l'utilisateur. En savoir plus sur [la création d'un message dans l'application ici][13].

!\[IAM Example\]\[9\]

### Courriel {#platform-features-email}

Envoyez à vos utilisateurs des messages HTML enrichis en ajoutant vos modèles HTML existants ou en utilisant notre éditeur de texte riche. Braze facilite l'inclusion du courrier électronique dans votre stratégie d'engagement mobile.

!\[Tableau de bord des e-mails\]\[10\]

### Webhooks {#platform-features-webhooks}

Les webhooks de Braze vous permettent de déclencher des actions non-applicatives qui fournissent à d'autres systèmes et applications des informations en temps réel. La flexibilité de cette fonction vous permet d'envoyer des informations à n'importe quel terminal.

!\[Webhooks\]\[22\]
[2]: {% image_buster /assets/img_archive/dashboard_segment_example.png %} "Exemple de segmentation" [6]: {% image_buster /assets/img_archive/news_feed_dashboard_example. ng %} "News Feed Dashboard" [8]: {% image_buster /assets/img_archive/UOiOSPush. ng %} "Exemple Push Dashboard" [9]: {% image_buster /assets/img_archive/In-App_Modal.png %} "Slideup Example" [10]: {% image_buster /assets/img_archive/EmailTemplateEditor. ng %} "Éditeur de modèle d'e-mail" [22]: {% image_buster /assets/img_archive/Webhook_Body_Edit.png %}

[4]: http://en.wikipedia.org/wiki/Dayparting
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#deep-links
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#deep-links
[13]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#creating-an-in-app-message
