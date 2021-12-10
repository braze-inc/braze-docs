---
nav_title: Août
page_order: 5
noindex: vrai
page_type: Mettre à jour
description: "Cet article contient des notes de mise à jour pour août 2017."
---

# Août 2017

## Mettre à jour pour les boutons d'action push

Nous avons ajouté la prise en charge des [boutons d'action][70] à nos terminaux de messagerie de l'API REST.

## Mise à jour du modèle Liquid

Vous pouvez maintenant [personnaliser un message][69] basé sur :
- L'appareil auquel il a été envoyé,
- ID de l'appareil,
- Transporteur,
- IDFA,
- Modèle,
- OS, et
- Plateforme

## Canvas déclenchée par l'API

Vous pouvez maintenant déclencher un [Canvas][68] via les points de terminaison de l'API (send, schedule, update, supprimer) qui correspondent aux campagnes existantes, vous permettant d'automatiser et d'optimiser davantage votre marketing.

## Boutons d'action push Web

Nous avons ajouté le support des boutons d'action push sur le SDK web pour Chrome, vous permettant d’augmenter votre engagement en offrant à vos utilisateurs des choix contextuels qui simplifient leur vie chargée. En savoir plus sur les meilleures pratiques pour les notifications push [ici][66].

## Nouveaux terminaux API

Nous avons exposé de nouveaux points de terminaison API, /email/hard_bounces, qui vous permettent de tirer des bounces durs par adresse e-mail ou dans une plage de dates donnée, et /messages/scheduled_broadcasts, qui vous permet de tirer la prochaine fois que des campagnes planifiées et des Canvases d'entrée programmée commenceront. Ces nouveaux terminaux vous permettent de personnaliser et d'optimiser davantage vos campagnes. En savoir plus sur nos terminaux API [ici][65].

## Géorepérages

Nous avons ajouté une nouvelle fonctionnalité, les géofences, qui vous permet de déclencher des messages en temps réel lorsque les clients entrent et quittent des zones géographiques définies permettant une communication personnalisée et pertinente avec vos clients. en savoir plus sur le marketing de localisation dans [notre documentation][64].

## Mettre à jour vers l'éditeur d'e-mail

Nous avons ajouté une auto-complétion dynamique à notre nouvel éditeur de courriel, pour que vous puissiez maintenant compléter automatiquement les attributs et les événements personnalisés réels de vos clients lors de l'utilisation de Liquid, facilitant votre vie. En savoir plus sur les meilleures pratiques de messagerie dans [Académie][63].

## Mettre à jour les filtres de date

Nous avons ajouté un filtre de date "jamais" afin que vous puissiez cibler les clients qui n'ont jamais reçu ou interagi avec l'un de vos messages. vous permettant de disposer de listes de clients propres et d'assurer la délivrabilité des e-mails. En savoir plus sur les filtres [ici][62].

## Mettre à jour vers Canvas

Nous avons ajouté des pourcentages au sommet de chaque variante de Canvas de sorte que maintenant, vous pouvez voir quelles variantes fonctionnent mieux d’un coup d’œil. En savoir plus sur Canvas [ici][61].

## Toile avec sélection intelligente

Canvas possède maintenant une sélection intelligente qui vous permet de tester vos toiles de façon plus efficace. En savoir plus sur notre Suite Intelligence [ici][60].

## Mettre à jour vers les noms d'affichage des emails

Nous avons ajouté le support des caractères UTF-8 spéciaux dans les noms d'affichage des e-mails, afin que vous puissiez créer encore plus d'e-mails personnalisés pour vos clients. En savoir plus sur les meilleures pratiques de messagerie [ici][67].

## Agrégation CSV des rapports d'engagement

Maintenant, vous pouvez recevoir des données consolidées pour chaque campagne et chaque Canvas dans deux fichiers distincts, quel que soit le nombre de campagnes ou de Canvases sélectionnés, vous permettant de disposer de toutes les données dont vous avez besoin, lorsque vous en avez besoin. En savoir plus sur les rapports d'engagement [ici][59].

> Mise à jour : comme indiqué dans nos [notes de publication de Septembre 2017]({{site.baseurl}}/help/release_notes/2017/august/#september-2017), vous pouvez maintenant agréger des données à partir d'une période de temps spécifique, ainsi que planifier les exportations à exécuter sur une base récurrente.



[59]: {{site.baseurl}}/user_guide/data_and_analytics/engagement_reports/#creating-a-new-report
[61]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/
[62]: {{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#segmentation-filters
[63]: {{site.baseurl}}/help/troubleshooting_guide/troubleshooting_guide/#email
[64]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/locations_and_geofences/
[65]: {{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api
[66]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
[67]: {{site.baseurl}}/help/troubleshooting_guide/troubleshooting_guide/#email
[68]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/
[69]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[70]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_action_buttons/#how-to-use-action-buttons
