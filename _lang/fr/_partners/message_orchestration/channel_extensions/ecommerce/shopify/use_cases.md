---
nav_title: Données Shopify dans Braze
article_title: "Utilisation des données Shopify dans Braze"
description: "Cet article explique comment utiliser les données Shopify dans Braze pour la personnalisation et la segmentation."
page_type: partner
search_tag: Partenaire

---

# Utilisation des données Shopify dans Braze

## Personnalisation

Grâce à la prise en charge des objets imbriqués pour les événements personnalisés, les clients de Braze Shopify peuvent utiliser les variables de modèle Liquid des propriétés de l’événement imbriqué. Les tableaux suivants répertorient les variables du modèle Liquid pour chaque événement.

{% tabs %}
{% tab Shopify Abandon Checkout Event %}
**Event**: `shopify_abandoned_checkout`<br>
**Type**: [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Modèle Liquid |
| --- | --- |
| ID de paiement | `{{event_properties.${checkout_id}}}` |
| URL du chariot abandonné | `{{event_properties.${abandoned_checkout_url}}}` |
| Code de remise | `{{event_properties.${discount_code}}}` |
| Prix total | `{{event_properties.${total_price}}}` |
| Montant de la remise | `{{event_properties.${applied_discount}[0].amount}}` |
| Titre de la remise | `{{event_properties.${applied_discount}[0].title}}` |
| Description de la remise | `{{event_properties.${applied_discount}[0].description}}` |
| ID d’article | `{{event_properties.${line_items}[0].product_id}}` |
| Quantité d’articles | `{{event_properties.${line_items}[0].quantity}}` |
| Unité de gestion des stocks de l’article | `{{event_properties.${line_items}[0].sku}}` |
| Titre de l’article | `{{event_properties.${line_items}[0].title}}` |
| Fournisseur de l’article | `{{event_properties.${line_items}[0].vendor}}` |
| Propriétés de l’article | `{{event_properties.${line_items}[0].properties}}` |
| Prix de l’article | `{{event_properties.${line_items}[0].price}}` |
{% endraw %}

{% endtab %}
{% tab Shopify Created Order Event %}

**Event**: `shopify_created_order`<br>
**Type**: [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Modèle Liquid |
| --- | --- |
| ID de commande | `{{event_properties.${order_id}}}` |
| État confirmé | `{{event_properties.${confirmed}}}` |
| URL du statut de la commande | `{{event_properties.${order_status_url}}}` |
| Numéro de commande | `{{event_properties.${order_number}}}` |
| Horodatage annulé | `{{event_properties.${cancelled_at}}}` |
| Total des remises | `{{event_properties.${total_discounts}}}` |
| Prix total | `{{event_properties.${total_price}}}` |
| Balises | `{{event_properties.${tags}}}` |
| Codes de remise | `{{event_properties.${discount_codes}}}` |
| ID d’article | `{{event_properties.${line_items}[0].product_id}}` |
| Quantité d’articles | `{{event_properties.${line_items}[0].quantity}}` |
| Unité de gestion des stocks de l’article | `{{event_properties.${line_items}[0].sku}}` |
| Titre de l’article | `{{event_properties.${line_items}[0].title}}` |
| Fournisseur de l’article | `{{event_properties.${line_items}[0].vendor}}` |
| Propriétés de l’élément | `{{event_properties.${line_items}[0].properties}}` |
| Prix de l’article | `{{event_properties.${line_items}[0].price}}` |
| Titre de l’expédition | `{{event_properties.${shipping}[0].title}}` |
| Prix de l’expédition | `{{event_properties.${shipping}[0].price}}` |

{% endraw %}

{% endtab %}
{% tab Purchase Event %}

**Event**: Achat<br>

**Type**: [Événement d’achat Braze]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/)

{% raw %}
| Variable | Modèle Liquid |
| --- | --- |
| Unité de gestion des stocks de l’article | `{{event_properties.${line_items}[0].sku}}` |
| Titre de l’article  | `{{event_properties.${line_items}[0].title}}` |
| Fournisseur de l’article | `{{event_properties.${line_items}[0].vendor}}` |
| Propriétés de l’élément | `{{event_properties.${line_items}[0].properties}}` |
{% endraw %}

{% endtab %}
{% endtabs %}

## Segmentation

Vous pouvez filtrer les événements de Shopify avec tous les [filtres personnalisés existants]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) dans Segmentation. 

![Page de détails du segment pour un segment Shopify_Test avec le filtre pour l’événement personnalisé « abandon_paiement_shopify » mis en évidence.][12]{: style="max-width:80%;"}

En outre, vous pouvez également utiliser le filtre d’étendue des achats de Braze pour créer des segments d’utilisateurs basés sur :
- Premier/dernier achat
- Premier/dernier achat pour une application spécifique
- Produits déjà achetés au cours des 30 derniers jours
- Nombre d’achats qu’ils ont effectués

![Filtre de segmentation pour les utilisateurs ayant effectué leur premier achat après le 17 octobre 2020.][13]

![Recherche d’un ID du produit spécifique comme filtre de segmentation.][14]

{% alert note %}
Si vous cherchez à segmenter par des propriétés d’événement personnalisées, assurez-vous de travailler avec votre gestionnaire du succès des clients ou le [support]({{site.baseurl}}/braze_support/) Braze pour activer le filtrage de toutes les propriétés d’événement pertinentes que vous souhaitez utiliser dans la segmentation et Liquid.
{% endalert %} 

## Déclenchement de campagne et de Canvas 

Avec les événements personnalisés Shopify dans Braze, vous pouvez déclencher des Canvas ou des campagnes comme vous le feriez normalement avec n’importe quel autre [événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-storage). Par exemple, vous pouvez créer un Canvas basé sur des actions qui se déclenchent suite à un événement `shopify_checkouts_abandon` Shopify au sein des critères d’entrée du Canvas. 

![Canvas basé sur l’action qui saisit les utilisateurs qui effectuent l’événement personnalisé « abandon_paiement_shopify ».][5]

Avec la prise en charge des objets imbriqués pour les propriétés d’événement personnalisées, les clients peuvent désormais déclencher des campagnes et des Canvas à l’aide d’une propriété de l’événement imbriqué. Voici un exemple de déclenchement d’une campagne utilisant un produit spécifique de l’événement personnalisé `shopify_created_order`.

![Campagne basée sur l’action qui envoie aux utilisateurs qui effectuent l’événement personnalisé « commande_shopify_créée » où la propriété imbriquée « product_id » est égale à un nombre spécifique.][26]

[5]: {% image_buster /assets/img/Shopify/shopify_integration11.png %}  
[12]: {% image_buster /assets/img/Shopify/shopify_segmentation2.png %} 
[13]: {% image_buster /assets/img/Shopify/shopify_segmentation3.png %} 
[14]: {% image_buster /assets/img/Shopify/shopify_segmentation4.png %}   
[26]: {% image_buster /assets/img/Shopify/shopify_integration17.png %}
