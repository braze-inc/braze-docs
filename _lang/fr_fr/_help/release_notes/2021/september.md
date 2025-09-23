---
nav_title: septembre
page_order: 3
noindex: true
page_type: update
description: "Cet article contient les notes de version de septembre 2021."
---

# Septembre 2021

## iOS 15

### Protection de la confidentialité dans Apple Mail 

La protection de la confidentialité dans Mail (MPP) d’Apple est une mise à jour de confidentialité qui sera disponible mi-septembre pour les utilisateurs de l’application Apple Mail sur iOS 15, iPadOS 15, macOS Monterey et watchOS 8. Pour les utilisateurs qui optent pour la confidentialité dans Mail, les e-mails seront désormais préchargés à l'aide de serveurs proxy, ce qui mettra les images en cache et empêchera d'exploiter les pixels de suivi pour des indicateurs tels que le [suivi du nombre d'ouvertures]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#open-tracking-pixel). Pour en savoir plus sur la protection de la confidentialité dans Mail et les problèmes concernant les indicateurs de livrabilité des e-mails et les problèmes liés aux campagnes préexistantes et aux Canvases qui se déclenchent sur la base de ces indicateurs, consultez notre [documentation]({{site.baseurl}}/user_guide/message_building_by_channel/email/apple_mail/mpp/).

### Fonctionnalités Push

iOS 15 a introduit de nouvelles fonctionnalités de notification pour aider les utilisateurs à rester focalisés et à éviter de fréquentes interruptions tout au long de la journée. Nous sommes ravis d'offrir une prise en charge de ces nouvelles fonctionnalités, notamment les [niveaux d'interruption et les scores de pertinence.]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/)

## Cartes de visite

Les cartes de contact sont un format de fichier normalisé pour l’envoi d’informations professionnelles/de contact facilement importables dans les carnets d’adresses/contacts. Vous pouvez maintenant télécharger et créer des cartes de contact pour vos messages SMS et MMS. Pour en savoir plus sur la manière de créer des cartes de contact dans notre générateur de cartes de contact intégré, consultez notre [documentation]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/contact_card/).

## Personnalisation des cartes de contenu par défaut

Vous pouvez créer votre propre interface de cartes de contenu en étendant le `ABKContentCardsTableViewController` pour personnaliser tous les éléments de l’interface utilisateur et le comportement des cartes de contenu. Pour en savoir plus sur la manière de personnaliser le flux des cartes de contenu, consultez notre [documentation]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style/). 

## Limites de débit de l’API

[Les limites de débit]({{site.baseurl}}/api/basics/#api-limits/) s'appliqueront à tous les clients embarqués après le 16 septembre 2021. 

## Mises à jour des Guides du développeur pour Android et FireOS

Les Guides du développeur pour Android et FireOS ont été fusionnés dans un seul endroit. Des articles dédiés à FireOS seront disponibles dans cette [nouvelle section Android.]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android)

## Mises à jour des Rapports d’entonnoir et de rétention

Les [rapports d'entonnoir]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) et les [rapports de rétention]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/) sont désormais disponibles pour les campagnes SMS.
