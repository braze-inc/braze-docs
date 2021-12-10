---
nav_title: Shopify Données dans Braze
article_title: "Utiliser les données Shopify dans Braze"
description: "Cet article décrit comment utiliser les données Shopify dans Braze pour la personnalisation et la segmentation."
page_type: partenaire
search_tag: Partenaire
---

# Utiliser les données Shopify dans Braze

## Personnalisation

En utilisant la prise en charge d'objet imbriqué pour les événements personnalisés, les clients de Braze Shopify peuvent utiliser des variables de modèles Liquid des propriétés d'événement imbriquées. Vous trouverez ci-dessous les variables de modèles Liquid pour chaque événement.

{% tabs %}
{% tab Shopify Abandon Checkout Event %}
__Événement__: `shopify_abandoned_checkout`<br> __Type__: [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable                   | Templating Liquide                                        |
| -------------------------- | --------------------------------------------------------- |
| ID du paiement             | `{{event_properties.${checkout_id}}}`                     |
| URL de la carte abandonnée | `{{event_properties.${abandoned_checkout_url}}}`          |
| Code de réduction          | `{{event_properties.${discount_code}}}`                   |
| Prix total                 | `{{event_properties.${total_price}}}`                     |
| Montant de la remise       | `{{event_properties.${applied_discount}[0].amount}}`      |
| Titre de la remise         | `{{event_properties.${applied_discount}[0].title}}`       |
| Description de la remise   | `{{event_properties.${applied_discount}[0].description}}` |
| Item ID                    | `{{event_properties.${line_items}[0].product_id}}`        |
| Quantité d'articles        | `{{event_properties.${line_items}[0].quantity}}`          |
| UGS de l'article           | `{{event_properties.${line_items}[0].sku}}`               |
| Titre de l'élément         | `{{event_properties.${line_items}[0].title}}`             |
| Fournisseur d'objet        | `{{event_properties.${line_items}[0].vendor}}`            |
| Propétitions d'objets      | `{{event_properties.${line_items}[0].properties}}`        |
| Prix de l’article          | `{{event_properties.${line_items}[0].price}}`             |
{% endraw %}

{% endtab %}
{% tab Shopify Created Order Event %}

__Event__: `shopify_created_order`<br> __Type__: [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable                     | Templating Liquide                                 |
| ---------------------------- | -------------------------------------------------- |
| ID de la commande            | `{{event_properties.${order_id}}}`                 |
| Statut confirmé              | `{{event_properties.${confirmed}}}`                |
| URL du statut de la commande | `{{event_properties.${order_status_url}}}`         |
| Numéro de commande           | `{{event_properties.${order_number}}}`             |
| Horodatage annulé            | `{{event_properties.${cancelled_at}}}`             |
| Réductions totales           | `{{event_properties.${total_discounts}}}`          |
| Prix total                   | `{{event_properties.${total_price}}}`              |
| Tags                         | `{{event_properties.${tags}}}`                     |
| Codes de réduction           | `{{event_properties.${discount_codes}}}`           |
| Item ID                      | `{{event_properties.${line_items}[0].product_id}}` |
| Quantité d'articles          | `{{event_properties.${line_items}[0].quantity}}`   |
| UGS de l'article             | `{{event_properties.${line_items}[0].sku}}`        |
| Titre de l'élément           | `{{event_properties.${line_items}[0].title}}`      |
| Fournisseur d'objet          | `{{event_properties.${line_items}[0].vendor}}`     |
| Propriétés de l'élément      | `{{event_properties.${line_items}[0].properties}}` |
| Prix de l’article            | `{{event_properties.${line_items}[0].price}}`      |
| Titre de la livraison        | `{{event_properties.${shipping}[0].title}}`        |
| Frais de port                | `{{event_properties.${shipping}[0].price}}`        |

{% endraw %}

{% endtab %}
{% tab Purchase Event %}

__Evénement__: Achat<br> __Type__: [Evénement d'Achat de Braze]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/)

{% raw %}
| Variable                | Templating Liquide                                 |
| ----------------------- | -------------------------------------------------- |
| UGS de l'article        | `{{event_properties.${line_items}[0].sku}}`        |
| Titre de l'élément      | `{{event_properties.${line_items}[0].title}}`      |
| Fournisseur d'objet     | `{{event_properties.${line_items}[0].vendor}}`     |
| Propriétés de l'élément | `{{event_properties.${line_items}[0].properties}}` |
{% endraw %}

{% endtab %}
{% endtabs %}

## Segmentation

Vous pouvez filtrer les événements de Shopify avec tous les [filtres personnalisés existants]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) dans Segmentation.

!\[Shopify\]\[12\]{: style="max-width:80%;"}

En outre, vous pouvez également utiliser le filtre d'achat de Braze pour créer des segments d'utilisateurs basés sur:
- Premier/dernier achat
- Premier/dernier achat pour une application spécifique
- Produits qu'ils ont déjà achetés au cours des 30 derniers jours
- Le nombre d'achats qu'ils ont effectués

!\[Shopify\]\[13\]

!\[Shopify\]\[14\]

{% alert note %}
Si vous cherchez à segmenter par des propriétés d'événement personnalisées, veuillez vous assurer que vous travaillez avec votre Customer Success Manager ou le support [Braze]({{site.baseurl}}/braze_support/) pour activer le filtrage de toutes les propriétés d'événements pertinentes que vous souhaitez utiliser dans la segmentation et dans Liquid.
{% endalert %}

## Déclenchement de la campagne et de la toile

Avec Shopify événements personnalisés au Brésil, vous pouvez déclencher des Canvases ou des campagnes comme vous le feriez normalement avec n'importe quel [événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-storage). For example, you may create an Action-Based Canvas that triggers off of the Shopify `shopify_checkouts_abandon` event within the Canvas entry criteria.

!\[Shopify\]\[5\]

Avec la prise en charge d'objets imbriqués pour les propriétés d'événements personnalisés, les clients peuvent maintenant déclencher des campagnes et des toiles en utilisant une propriété d'événements imbriqués. Afficher ci-dessous est un exemple de déclenchement d'une campagne en utilisant un produit spécifique de l'événement personnalisé `shopify_created_order`.

!\[Shopify\]\[26\]
[5]: {% image_buster /assets/img/Shopify/shopify_integration11.png %} [12]: {% image_buster /assets/img/Shopify/shopify_segmentation2.png %} [13]: {% image_buster /assets/img/Shopify_segmentation3. ng %} [14]: {% image_buster /assets/img/Shopify/shopify_segmentation4.png %} [26]: {% image_buster /assets/img/Shopify/shopify_integration17.png %}
