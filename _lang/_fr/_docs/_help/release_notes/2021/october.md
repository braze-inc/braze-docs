---
nav_title: Octobre
page_order: 3
noindex: vrai
page_type: Mettre à jour
description: "Cet article contient des notes de mise à jour pour octobre 2021."
---

# Octobre 2021

## iOS 15

### Protection de la vie privée d'Apple Mail

La protection de la vie privée (MPP) d’Apple est une mise à jour de la vie privée qui sera disponible pour les utilisateurs de l’application Apple Mail sur iOS 15, iPadOS 15, macOS Monterey, et watchOS 8, sorti à la mi-septembre. Pour les utilisateurs qui optent pour le MPP, les e-mails seront maintenant préchargés en utilisant des serveurs proxy, mettre en cache les images et empêcher la possibilité de tirer parti des pixels de suivi pour les métriques comme [le suivi d'ouverture]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/email_settings/#email-open-tracking-pixel/). Pour en savoir plus sur les MPP et les problèmes concernant les paramètres de délivrabilité des courriels et les problèmes liés aux campagnes préexistantes et aux toiles qui se déclenchent sur la base de ces métriques, visitez notre [documentation]({{site.baseurl}}/user_guide/message_building_by_channel/email/mpp/).

### Fonctionnalités push

iOS 15 a introduit de nouvelles fonctionnalités de notification pour aider les utilisateurs à rester concentrés et éviter des interruptions fréquentes tout au long de la journée. Nous sommes heureux de proposer un support pour ces nouvelles fonctionnalités, y compris les [niveaux d'interruption et les Scores de pertinence]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/).

## Cartes de contact

Les Cartes de contact sont un format de fichier normalisé pour envoyer des informations commerciales et de contact qui peuvent être facilement importées dans des carnets d'adresses ou des carnets de contacts. Vous pouvez maintenant télécharger et créer des cartes de contact pour vos messages SMS et MMS. Pour en savoir plus sur la façon de construire des cartes de contact dans notre générateur de carte de contact intégré, visitez notre [documentation]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/contact_card/).

## Personnalisation des cartes de contenu

Vous pouvez créer votre propre interface de cartes de contenu en étendant `ABKContentCardsTableViewController` pour personnaliser tous les éléments de l'interface utilisateur et le comportement des cartes de contenu. Pour en savoir plus sur la façon de personnaliser le flux des Cartes de Contenu, visitez notre [documentation]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/customization/#customizing-the-content-cards-feed/).

## Limites de débit de l'API

[Les limites de taux]({{site.baseurl}}/api/basics/#api-limits/) s'appliqueront à tous les clients embarqués après le 16 septembre 2021.

## Mises à jour vers les guides de développeurs Android et FireOS

Les guides de développeurs Android et FireOS ont fusionné en un seul endroit. Des articles dédiés à FireOS seront disponibles dans cette [nouvelle section Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/fireos/integration/).

## Mises à jour de l'entonnoir et des rapports de fidélisation

Les [Rapports d'entonnoir]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_funnel_reports/) et [Rapports de fidélisation]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/retention_reports/) sont maintenant disponibles pour les campagnes de SMS.
