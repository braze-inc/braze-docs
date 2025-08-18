---
nav_title: août
page_order: 5
noindex: true
page_type: update
description: "Cet article contient les notes de version d’août 2017."
---

# Août 2017

## Mise à jour des boutons d’action push

Nous avons ajouté la prise en charge des [boutons d'action push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_action_buttons/#how-to-use-action-buttons) à nos endpoints de messages de l'API REST.

## Mise à jour du templating Liquid

Vous pouvez désormais [personnaliser un message]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) en fonction de :
- L’appareil auquel il a été envoyé,
- ID d’appareil,
- Opérateur,
- IDFA,
- Modèle,
- OS et
- Plateforme

## Canvas déclenché par API

Vous pouvez désormais déclencher un [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) via des endpoints API (envoyer, planifier, mettre à jour, supprimer) qui correspondent à ceux existants pour les campagnes, ce qui vous permet d'automatiser et d'optimiser davantage votre marketing.

## Boutons d’action push WEB

Nous avons ajouté une prise en charge des boutons d’action push sur le SDK Web pour Chrome, ce qui vous permet d’augmenter votre engagement en offrant aux utilisateurs des choix contextuels qui leur simplifie la vie. Consultez les [meilleures pratiques en matière de notifications push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/).

## Nouveaux endpoints de l’API

Nous avons exposé de nouveaux endpoints API, /email/hard_bounces, qui vous permet d'obtenir les échecs d'envoi par adresse e-mail ou dans une plage de dates donnée, et /messages/scheduled_broadcasts, qui vous permet d'obtenir la prochaine heure de début des campagnes planifiées et des toiles à entrée programmée. Ces nouveaux endpoints vous permettent de personnaliser et d’optimiser davantage vos campagnes. En savoir plus sur nos [endpoints API]({{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api).

## Géorepérages

Nous avons ajouté une nouvelle fonctionnalité de geofencing, qui vous permet de déclencher des messages en temps réel lorsque les clients entrent et sortent de zones géographiques définies, ce qui permet des communications personnalisées et pertinentes avec vos clients. En savoir plus sur l'[emplacement/localisation marketing]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/locations_and_geofences/).

## Mise à jour de l’éditeur d’e-mail

Pour vous faciliter la vie, nous avons ajouté un autoremplissage dynamique à notre nouvel éditeur d’e-mails, pour renseigner automatiquement les attributs et les événements personnalisés réels de vos clients quand vous utilisez Liquid. En savoir plus sur les [meilleures pratiques en matière d'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices).

## Mettre à jour des filtres de date

Nous avons ajouté un filtre de date « never (jamais) » pour que vous puissiez cibler les clients qui n’ont jamais reçu ou interagi avec l’un de vos messages, ce qui vous permet d’avoir des listes de clients propres et de garantir la livraison des e-mails. En savoir plus sur les [filtres]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#segmentation-filters).

## Mise à jour de Canvas

Nous avons ajouté des pourcentages en haut de chaque Canvas Variant, pour que vous puissiez voir en un coup d’œil quelles variantes fonctionnent mieux. En savoir plus sur [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).

## Canvas avec sélection intelligente

Canvas a maintenant une sélection intelligente, ce qui vous permet de tester vos Canvas avec plus d’efficacité. En savoir plus sur notre [suite d'intelligence.]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)

## Mise à jour des noms d’affichage des e-mails

Nous avons ajouté des caractères UTF-8 spéciaux dans les noms d’affichage des e-mails, afin que vous puissiez créer des e-mails encore plus personnalisés pour vos clients. En savoir plus sur les [meilleures pratiques en matière d'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices).

## Rapports d'engagement agrégés sur CSV 

Maintenant, vous pouvez recevoir des données consolidées pour chaque campagne et chaque Canvas dans deux fichiers distincts, quel que soit le nombre de campagnes ou de Canvas sélectionnés, pour avoir toutes les données dont vous avez besoin quand vous en avez besoin. En savoir plus sur les [rapports d'engagement]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/).

> Comme indiqué dans nos [notes de mise à jour de septembre 2017]({{site.baseurl}}/help/release_notes/2017/september/), vous pouvez désormais agréger les données d'une période spécifique ainsi que planifier des exportations à exécuter de manière récurrente.


