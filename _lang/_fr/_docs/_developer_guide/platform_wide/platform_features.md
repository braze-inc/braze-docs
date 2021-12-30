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

### Cartes de contenu {#platform-features-content-cards}

Avec les Cartes de Contenu, vous pouvez envoyer un très ciblé, flux dynamique de contenu riche pour vos clients directement dans les applications qu'ils aiment, sans interrompre leur expérience. De plus, les cartes de contenu prennent en charge des fonctionnalités plus personnalisées, y compris le épinglage de cartes, le rejet de carte, la livraison basée sur API, Contenu connecté, temps d'expiration de la carte personnalisée, analyse de la carte et coordination facile avec les notifications push.

![Flux de cartes de contenu]({% image_buster /assets/img/cc_feed_new.png %}){: style="largeur-max-60%"}

### Notifications push {#platform-features-push}

Braze prend en charge le service Apple Push Notification Service (APN) pour iOS et Firebase Cloud Messaging (FCM) pour Android. Les notifications push peuvent être déclenchées par la publication de campagnes de messagerie et d'actualités.

!\[Exemple de tableau de bord Push\]\[8\]

### Messagerie intégrée {#platform-features-in-app-messaging}

Braze fournit des notifications discrètes dans l'application via notre interface utilisateur native sur mesure. Les messages peuvent être présentés à tout moment de votre choix (par ex. lorsque les utilisateurs démarrent une nouvelle session ou effectuent une action spécifique) en s'assurant que votre message arrive au moment le plus efficace pour engager l'utilisateur. En savoir plus sur [la création d'un message dans l'application][13].

!\[IAM Example\]\[9\]

### Courriel {#platform-features-email}

Envoyez à vos utilisateurs des messages HTML enrichis en ajoutant vos modèles HTML existants, en utilisant notre éditeur de texte riche, ou notre éditeur de glisser-déposer. Braze facilite l'inclusion du courrier électronique dans votre stratégie d'engagement mobile.

!\[Tableau de bord des e-mails\]\[10\]

### SMS et MMS {#platform-features-sms-mms}

Utilisez des SMS avec Braze pour envoyer des notifications transactionnelles, partager des promotions, envoyer des rappels et plus encore. Avec plus de 23 milliards de SMS envoyés chaque jour dans le monde entier, le SMS est le moyen le plus direct d'atteindre les utilisateurs et les clients.

![Exemple d'aperçu SMS]({% image_buster /assets/img_archive/sms_preview.png %})

### Webhooks {#platform-features-webhooks}

Les webhooks de Braze vous permettent de déclencher des actions non-applicatives qui fournissent à d'autres systèmes et applications des informations en temps réel. La flexibilité de cette fonction vous permet d'envoyer des informations à n'importe quel terminal.

!\[Webhooks\]\[22\]
[2]: {% image_buster /assets/img_archive/dashboard_segment_example.png %} "Exemple de segmentation" [6]: {% image_buster /assets/img_archive/news_feed_dashboard_example. ng %} "News Feed Dashboard" [8]: {% image_buster /assets/img_archive/UOiOSPush. ng %} "Exemple Push Dashboard" [9]: {% image_buster /assets/img_archive/In-App_Modal.png %} "Slideup Example" [10]: {% image_buster /assets/img_archive/EmailTemplateEditor. ng %} "Éditeur de modèle d'e-mail" [22]: {% image_buster /assets/img_archive/Webhook_Body_Edit.png %}

[13]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#creating-an-in-app-message
