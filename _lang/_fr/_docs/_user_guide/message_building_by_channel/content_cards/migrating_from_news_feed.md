---
nav_title: Migration depuis le flux d'actualités
article_title: Migration depuis le flux d'actualités
page_order: 10
description: "Les Cartes de Contenu offrent beaucoup plus de fonctionnalités qui ne sont pas prises en charge par Braze News Feed. Cet article couvre les différences entre les deux et les orientations en matière de migration et d'adoption."
channel:
  - cartes de contenu
  - fil d'actualité
---

# Migration depuis le flux d'actualités vers les cartes de contenu

Passer du fil d'actualités aux cartes de contenu prend du temps, mais c'est une adoption facile! Vous ne pouvez pas migrer automatiquement le contenu du flux d'actualités vers des cartes de contenu - vous devez intégrer des cartes de contenu à partir de zéro. Cependant, avec la nouvelle flexibilité des Cartes de Contenu, nous ne pensons pas que vous la raterez ou l'esprit.

Contactez votre gestionnaire de compte Braze pour plus de détails.

## Fonctionnalités et fonctionnalités

Les Cartes de Contenu offrent de nombreuses fonctionnalités qui ne sont pas prises en charge par le flux d'actualités actuel de Braze, tels que des options de livraison supplémentaires telles que la livraison par action, la livraison par API et des analyses améliorées telles que le suivi des conversions.

Au fur et à mesure que vous planifiez votre migration du flux d'actualités vers les cartes de contenu, il sera important de noter les principales différences entre les Cartes de Contenu et le Flux de Nouvelles :

- La segmentation des Cartes de Contenu est évaluée au moment où les messages sont envoyés, la segmentation des News Feed est évaluée au moment où les Cartes de News sont affichées.
- La personnalisation des cartes de contenu est modélisée au moment de l'envoi des messages, La personnalisation des fiches d'actualités est modélisée au moment où les fiches d'actualités sont affichées.

| Fonctionnalités                                            | Flux d'actualité           | Cartes de contenu          |
| ---------------------------------------------------------- | -------------------------- | -------------------------- |
| Transactionnel et messagerie 1:1                           | <i class="fas fa-times"></i>  | <i class="fas fa-check"></i>  |
| Campagnes multivariées et multi-canaux                     | <i class="fas fa-times"></i>  | <i class="fas fa-check"></i>  |
| Livraison planifiée, basée sur l'action et basée sur l'API | <i class="fas fa-times"></i>  | <i class="fas fa-check"></i>  |
| Messages créés par l'API                                   | <i class="fas fa-times"></i>  | <i class="fas fa-check"></i>  |
| Tests A/B                                                  | <i class="fas fa-times"></i>  | <i class="fas fa-check"></i>  |
| [Cartes de révocation et d'épinglage][4]                   | <i class="fas fa-times"></i> | <i class="fas fa-check"></i> |
| [Analyses riches][3]                                       | <i class="fas fa-times"></i> | <i class="fas fa-check"></i> |
| [Disponible en Toile][2]                                   | <i class="fas fa-times"></i> | <i class="fas fa-check"></i> |
| [Contenu connecté][5]                                      | <i class="fas fa-times"></i> | <i class="fas fa-check"></i> |
| Personnalisation et Segmentation                           | Templé à Impression        | Templated at Send          |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Implémentation

- Les Cartes de Contenu et le Flux de Nouvelles sont des produits distincts, donc une intégration simple pour votre application ou votre site web est nécessaire pour utiliser les cartes de contenu.
- Si vous le souhaitez, les cartes de flux d'actualités existantes devront être migrées manuellement vers les campagnes de cartes de contenu lorsque vous changez.
- Les cartes de contenu ne sont pas destinées à être utilisées en même temps que le fil de nouvelles, car il remplace le fil d'actualité.
- Les cartes de contenu ne supportent pas actuellement les catégories - les catégories peuvent être obtenues via [la personnalisation et les paires clé-valeur][1].


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/multiple_feeds/
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/content-cards_in_canvas/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#step-2-compose-a-content-card
[5]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/
