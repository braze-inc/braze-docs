---
nav_title: Octobre
page_order: 3
noindex: true
page_type: update
description: "Cet article contient les notes de version d’octobre 2021."
---

# Octobre 2021

## iOS 15

### Protection de la confidentialité dans Apple Mail 

La protection de la confidentialité dans Mail (MPP) d’Apple est une mise à jour de confidentialité qui sera disponible mi-septembre pour les utilisateurs de l’application Apple Mail sur iOS 15, iPadOS 15, macOS Monterey et watchOS 8. Pour les utilisateurs qui s’abonnent (opt-in) aux e-mails MPP, les e-mails seront désormais préchargés sur des serveurs proxy, avec mise en cache des images, ce qui limite les possibilités de suivi des pixels pour des métriques telles que le [suivi des ouvertures]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/email_settings/#email-open-tracking-pixel/). Pour en savoir plus sur le MPP et les questions concernant les métriques de délivrabilité des e-mails et les problèmes avec des campagnes ou Canvas préexistants qui se déclenchent en fonction de ces indicateurs, consultez notre [documentation]({{site.baseurl}}/user_guide/message_building_by_channel/email/mpp/).

### Fonctionnalités Push

iOS 15 a introduit de nouvelles fonctionnalités de notification pour aider les utilisateurs à rester focalisés et à éviter de fréquentes interruptions tout au long de la journée. Nous sommes ravis de vous proposer ces nouvelles fonctionnalités, notamment les [Niveaux d’interruption et Scores de pertinence]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/).

## Cartes de visite

Les cartes de contact sont un format de fichier normalisé pour l’envoi d’informations professionnelles/de contact facilement importables dans les carnets d’adresses/contacts. Vous pouvez maintenant télécharger et créer des cartes de contact pour vos messages SMS et MMS. Pour en savoir plus sur la façon de créer des cartes de contact avec notre Générateur de cartes de contact intégré, consultez notre [documentation]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/contact_card/).

## Personnalisation des cartes de contenu Out-of-the-box

Vous pouvez créer votre propre interface de cartes de contenu en étendant le `ABKContentCardsTableViewController` pour personnaliser tous les éléments de l’interface utilisateur et le comportement des cartes de contenu. Pour en savoir plus sur la personnalisation du flux des cartes de contenu, consultez notre [documentation]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/customization/customizing_feed/). 

## Limites de débit de l’API

Les [limites de débit]({{site.baseurl}}/api/basics/#api-limits/) s’appliqueront à tous les clients onboardés après le 16 septembre 2021. 

## Mises à jour des Guides du développeur pour Android et FireOS

Les Guides du développeur pour Android et FireOS ont été fusionnés dans un seul endroit. Des articles FireOS dédiés seront disponibles dans cette [nouvelle section Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/fireos/integration/).

## Mises à jour des Rapports d’entonnoir et de rétention

Les [rapports d’entonnoir]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_funnel_reports/) et [rapports de rétention]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/retention_reports/) sont maintenant disponibles pour les campagnes SMS.
