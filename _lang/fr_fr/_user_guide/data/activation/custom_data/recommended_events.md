---
nav_title: Événements recommandés
article_title: Événements recommandés
alias: /recommended_events/
page_type: reference
description: "Cet article de référence décrit les événements recommandés, qui sont des recommandations fournies par Braze pour les événements de commerce électronique."
---

# Événements recommandés

> Les événements recommandés mappent les cas d'utilisation les plus courants du commerce électronique. En utilisant les événements personnalisés, vous pouvez débloquer des modèles de canvas pré-créés, des tableaux de bord de reporting qui mappent le cycle de vie du client, et plus encore.

Par exemple, vous pouvez avoir un événement personnalisé nommé “cart_updated” ou “update_to_cart” pour capturer le moment où un utilisateur a ajouté, supprimé ou mis à jour les produits dans son panier. Pour les événements recommandés, Braze fournira le modèle d'événement, qui comprend un nom défini et les propriétés pertinentes pour cet événement.

{% alert important %}
Les événements recommandés sont actuellement en accès anticipé. Contactez votre gestionnaire satisfaction client Braze si vous souhaitez participer à cet accès anticipé. <br><br>Si vous exploitez le nouveau [connecteur Shopify]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector), ces événements recommandés seront automatiquement disponibles grâce à l'intégration.
{% endalert %}

## Comment cela fonctionne-t-il ?

Braze applique une validation spéciale à tous les événements recommandés, et certains événements recommandés font l'objet d'un post-traitement particulier. Pour certains événements recommandés par l'industrie, Braze peut prendre en charge un traitement spécial, comme de nouveaux déclencheurs basés sur des actions pour les campagnes et les Canvases.

Les événements recommandés fonctionnent de la même manière que les [événements personnalisés]({{site.baseurl}}/user_guide/data/custom_data/custom_events). Vous pouvez exporter des événements recommandés à partir de Currents, les mettre en liste de blocage et les utiliser dans des rapports. Vous pouvez également envoyer des données dans Braze pour le suivi de ces événements à l'aide du [SDK de Braze]({{site.baseurl}}/developer_guide/getting_started/sdk_overview) ou de l'[endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track).

### Événements recommandés pour le commerce électronique

Les [événements recommandés pour le commerce électronique]({{site.baseurl}}/ecommerce_events/) sont basés sur des événements recommandés. Ces événements recommandés pour le commerce électronique suivent les actions entreprises par vos clients, telles que la consultation d'un produit, la mise à jour de leur panier ou le lancement du processus de paiement. 

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_refunded`
- `ecommerce.order_cancelled`

#### Modèles de canevas pour le commerce électronique

Consultez nos [cas d'utilisation]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/) dédiés à [l'e-commerce]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/) pour plus d'idées sur la façon d'utiliser les modèles préconstruits de Braze Canvas pour mettre en œuvre des stratégies essentielles.

## Questions fréquemment posées

### Les événements recommandés sont-ils les mêmes que les événements personnalisés ?

Non. Braze définira des schémas de données fondés sur l'opinion pour les événements recommandés. Il s'agira de propriétés d'événement obligatoires et facultatives qui feront l'objet d'un processus de validation dans Braze. Les [événements personnalisés]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) sont des actions spécifiques effectuées par, ou des mises à jour concernant, vos utilisateurs dans votre appli ou votre site web que vous souhaitez suivre. Vous pouvez personnaliser le nom de l'événement et ce qu'il suit.

### Puis-je personnaliser le nom des événements personnalisés ?

Non. Les événements recommandés ont des noms et des propriétés d'événement normalisés. Ces normalisations permettent d'assurer la cohérence de vos données.

### Puis-je encore utiliser les événements d'achat pour enregistrer les achats ?

Avec le lancement des événements recommandés pour le commerce électronique, Braze supprimera progressivement l'événement d'achat hérité à l'avenir. Si vous utilisez actuellement l'événement d'achat, vous recevrez un préavis concernant les plans de dépréciation. En attendant, vous pouvez continuer à utiliser les événements d'achat jusqu'à la date officielle d'obsolescence.