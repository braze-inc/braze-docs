---
nav_title: Migration du fil d'actualité
article_title: Migration du fil d'actualité
page_order: 10
description: "Les cartes de contenu offrent beaucoup plus de fonctionnalités qui ne sont pas prises en charge par le fil d'actualité de Braze. Le présent article décrit les différences entre ces deux options et donne des conseils pour la migration et l’adoption."
channel:
  - cartes de contenu
  - fil d’actualité
  
---

# Migration du fil d'actualité vers les cartes de contenu

{% alert note %}
Le Fil d’actualité est obsolète. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu : il est plus flexible, plus personnalisable et plus fiable.
{% endalert %}

Passer du fil d'actualité aux cartes de contenu prend du temps, mais l’essayer, c’est l’adopter ! Vous ne pouvez pas migrer automatiquement le contenu du fil d’actualité vers des cartes de contenu. Vous devez intégrer des cartes de contenu à partir de zéro. Mais vu la flexibilité des cartes de contenu, nous sommes sûrs que vous le regretterez pas !

Contactez votre gestionnaire de compte Braze pour plus d’informations.

## Caractéristiques et fonctionnalités

Les cartes de contenu offrent de nombreuses fonctionnalités qui ne sont pas prises en charge par le fil d'actualité de Braze :  options de livraison supplémentaires en fonction des actions de l’utilisateur, livraison via l’API, analyses améliorées avec le suivi des conversions etc.

Si vous prévoyez de migrer du fil d'actualité vers les cartes de contenu, il est important de noter les principales différences entre les deux :

- **Segmentation :** La segmentation des cartes de contenu peut être évaluée au moment où les messages sont envoyés ou au moment où elles sont affichées pour la première fois. La segmentation des fils d’actualité est évaluée au moment où les cartes de fil d’actualité sont affichées.
- **Personnalisation :** La personnalisation des cartes de contenu peut être modélisée au moment où les messages sont envoyés ou au moment où elles sont affichées pour la première fois. La personnalisation des cartes de fil d’actualité est modélisée au moment où elles sont affichées.

Le tableau suivant décrit davantage les différences entre les fonctionnalités des fils d’actualités et celles des cartes de contenu :

| Fonctionnalité | Fil d’actualité | Cartes de contenu |
|---|---|---|
| Campagnes multivariées et multicanales | <i class="fas fa-times" title="Non pris en charge"></i> | <i class="fas fa-check" title="Pris en charge"></i> |
| Livraison planifiée, par événement et basée sur l’API | <i class="fas fa-times" title="Non pris en charge"></i> | <i class="fas fa-check" title="Pris en charge"></i> |
| Messages créés par API | <i class="fas fa-times" title="Non pris en charge"></i> | <i class="fas fa-check" title="Pris en charge"></i> |
| Tests A/B | <i class="fas fa-times" title="Non pris en charge"></i> | <i class="fas fa-check" title="Pris en charge"></i> |
| [Fermeture et épinglage des cartes][4] | <i class="fas fa-times" title="Non pris en charge"></i> | <i class="fas fa-check" title="Pris en charge"></i> |
| [Analytiques enrichies][3] (par ex., suivi des conversions) | <i class="fas fa-times" title="Non pris en charge"></i> | <i class="fas fa-check" title="Pris en charge"></i> |
| [Disponible dans Canvas][2] | <i class="fas fa-times" title="Non pris en charge"></i> | <i class="fas fa-check" title="Pris en charge"></i> |
| [Contenu connecté][5] | <i class="fas fa-times" title="Non pris en charge"></i> | <i class="fas fa-check" title="Pris en charge"></i> |
| Personnalisation et segmentation | Modélisé à l’impression | Modélisation à l’envoi ou à la première impression |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3} 

## Mise en œuvre

- Les cartes de contenu et le fil d'actualité sont des produits distincts. Une intégration simple pour votre application ou site Internet est nécessaire pour pouvoir utiliser les cartes de contenu.
- Le cas échéant, les cartes de fil d'actualité existantes devront être migrés manuellement vers les campagnes de carte de contenu lorsque vous ferez la transition.
- Les cartes de contenu ne sont pas destinées à être utilisées en même temps que le fil d'actualité, car elles le remplacent.
- Les cartes de contenu ne prennent pas en charge les catégories actuellement. Utilisez la [personnalisation et les paires clé-valeur][1] pour faire des catégories le cas échéant.


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/multiple_feeds/
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/content-cards_in_canvas/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#step-2-compose-a-content-card
[5]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/
