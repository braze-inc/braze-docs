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

Passer du fil d'actualités aux cartes de contenu prend du temps, mais c'est une adoption facile! Vous ne pouvez pas migrer automatiquement le contenu du flux d'actualités vers les cartes de contenu. Vous devez intégrer des cartes de contenu à partir de zéro. Cependant, avec la nouvelle flexibilité des Cartes de Contenu, nous ne pensons pas que vous la raterez ou l'esprit.

Contactez votre gestionnaire de compte Braze pour plus de détails.

## Fonctionnalités et fonctionnalités

Les Cartes de Contenu offrent de nombreuses fonctionnalités qui ne sont pas prises en charge par le fil d'actualité de Braze, comme des options de livraison supplémentaires telles que la livraison par action et API, et des analyses améliorées comme le suivi des conversions.

Au fur et à mesure que vous planifiez votre migration du flux d'actualités vers les cartes de contenu, il sera important de noter les principales différences entre les Cartes de Contenu et le Flux de Nouvelles :

- **Segmentation :** La segmentation des Cartes de Contenu est évaluée lors de l'envoi des messages, La segmentation des fils d'actualité est évaluée au moment où les fiches de nouvelles sont affichées.
- **Personnalisation :** La personnalisation des Cartes de Contenu est tempérée lors de l'envoi des messages, La personnalisation des fiches d'actualités est modélisée au moment où les fiches d'actualités sont affichées.

Le tableau suivant décrit plus loin la différence entre les fonctionnalités prises en charge entre les fils d'actualités et les cartes de contenu :

| Fonctionnalités                                            | Flux d'actualité           | Cartes de contenu          |
| ---------------------------------------------------------- | -------------------------- | -------------------------- |
| Transactionnel et messagerie 1:1                           | <i class="fas fa-times" title="Non pris en charge"></i>  | <i class="fas fa-check" title="Supporté"></i>  |
| Campagnes multivariées et multi-canaux                     | <i class="fas fa-times" title="Non pris en charge"></i>  | <i class="fas fa-check" title="Supporté"></i>  |
| Livraison planifiée, basée sur l'action et basée sur l'API | <i class="fas fa-times" title="Non pris en charge"></i>  | <i class="fas fa-check" title="Supporté"></i>  |
| Messages créés par l'API                                   | <i class="fas fa-times" title="Non pris en charge"></i>  | <i class="fas fa-check" title="Supporté"></i>  |
| Tests A/B                                                  | <i class="fas fa-times" title="Non pris en charge"></i>  | <i class="fas fa-check" title="Supporté"></i>  |
| [Cartes de révocation et d'épinglage][4]                   | <i class="fas fa-times" title="Non pris en charge"></i> | <i class="fas fa-check" title="Supporté"></i> |
| [Analyses riches][3]                                       | <i class="fas fa-times" title="Non pris en charge"></i> | <i class="fas fa-check" title="Supporté"></i> |
| [Disponible en Toile][2]                                   | <i class="fas fa-times" title="Non pris en charge"></i> | <i class="fas fa-check" title="Supporté"></i> |
| [Contenu connecté][5]                                      | <i class="fas fa-times" title="Non pris en charge"></i> | <i class="fas fa-check" title="Supporté"></i> |
| Personnalisation et Segmentation                           | Templé à Impression        | Templated at Send          |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Implémentation

- Les Cartes de Contenu et le Flux de Nouvelles sont des produits distincts, donc une intégration simple pour votre application ou votre site web est nécessaire pour utiliser les cartes de contenu.
- Si vous le souhaitez, les cartes de flux d'actualités existantes devront être migrées manuellement vers les campagnes de cartes de contenu lorsque vous changez.
- Les cartes de contenu ne sont pas destinées à être utilisées en même temps que le fil de nouvelles, car il remplace le fil d'actualité.
- Les cartes de contenu ne supportent pas actuellement les catégories. Les catégories peuvent être obtenues via [des paires de personnalisation et de valeur clé][1].


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/multiple_feeds/
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/content-cards_in_canvas/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#step-2-compose-a-content-card
[5]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/
