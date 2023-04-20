---
nav_title: Données Shopify dans Braze
article_title: "Utilisation des données Shopify dans Braze"
description: "Cet article de référence explique comment utiliser les données Shopify dans Braze pour la personnalisation et la segmentation."
page_type: partner
search_tag: Partenaire
alias: "/shopify_data/"
page_order: 4
---

# Données Shopify dans Braze

## Personnalisation

Grâce à la prise en charge des objets imbriqués pour les événements personnalisés, les clients de Braze Shopify peuvent utiliser les variables de modèle Liquid des propriétés de l’événement imbriqué. Les tableaux suivants répertorient les variables du modèle Liquid pour chaque événement.

{% tabs %}
{% tab Product Viewed %}
**Événement** : `shopify_product_viewed`<br>
**Type** : [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Modèles Liquid |
| --- | --- |
| ID d’article | `{{event_properties.${id}}}` |
| Titre de l'élément  | `{{event_properties.${title}}}` |
| Prix de l’article | `{{event_properties.${price}}}` |
| Fournisseur de l’article | `{{event_properties.${vendor}}}` |
| Images de l’article | `{{event_properties.${images}}}` |

{% endraw %}
{% endtab %}

{% tab Product Clicked %}
**Événement** : `shopify_product_clicked`<br>
**Type** : [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Modèles Liquid |
| --- | --- |
| ID d’article | `{{event_properties.${id}}}` |
| Titre de l'élément  | `{{event_properties.${title}}}` |
| Prix de l’article | `{{event_properties.${price}}}` |
| Fournisseur de l’article | `{{event_properties.${vendor}}}` |
| Images de l’article | `{{event_properties.${images}}}` |
{% endraw %}
{% endtab %}

{% tab Abandon Cart %}
**Événement** : `shopify_abandoned_cart`<br>
**Type** : [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Modèles Liquid |
| --- | --- |
| ID d’article | `{{event_properties.${line_items}[0].product_id}}` |
| Quantité d’articles | `{{event_properties.${line_items}[0].quantity}}` |
| Unité de gestion des stocks de l’article | `{{event_properties.${line_items}[0].sku}}` |
| Titre de l'élément | `{{event_properties.${line_items}[0].title}}` |
| Fournisseur de l’article | `{{event_properties.${line_items}[0].vendor}}` |
| Propriétés de l’élément | `{{event_properties.${line_items}[0].properties}}` |
| Prix de l’article | `{{event_properties.${line_items}[0].price}}` |
{% endraw %}
{% endtab %}

{% tab Abandon Checkout %}
**Événement** : `shopify_abandoned_checkout`<br>
**Type** : [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Modèles Liquid |
| --- | --- |
| ID de paiement | `{{event_properties.${checkout_id}}}` |
| URL du panier abandonné | `{{event_properties.${abandoned_checkout_url}}}` |
| Code de remise | `{{event_properties.${discount_code}}}` |
| Prix total | `{{event_properties.${total_price}}}` |
| Montant de la remise | `{{event_properties.${applied_discount}[0].amount}}` |
| Titre de la remise | `{{event_properties.${applied_discount}[0].title}}` |
| Description de la remise | `{{event_properties.${applied_discount}[0].description}}` |
| ID d’article | `{{event_properties.${line_items}[0].product_id}}` |
| Quantité d’articles | `{{event_properties.${line_items}[0].quantity}}` |
| Unité de gestion des stocks de l’article | `{{event_properties.${line_items}[0].sku}}` |
| Titre de l'élément | `{{event_properties.${line_items}[0].title}}` |
| Fournisseur de l’article | `{{event_properties.${line_items}[0].vendor}}` |
| Propriétés de l’élément | `{{event_properties.${line_items}[0].properties}}` |
| Prix de l’article | `{{event_properties.${line_items}[0].price}}` |
{% endraw %}

{% endtab %}
{% tab Created Order %}

**Événement** : `shopify_created_order`<br>
**Type** : [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Modèles Liquid |
| --- | --- |
| ID de commande | `{{event_properties.${order_id}}}` |
| État confirmé | `{{event_properties.${confirmed}}}` |
| URL du statut de la commande | `{{event_properties.${order_status_url}}}` |
| Numéro de commande | `{{event_properties.${order_number}}}` |
| Horodatage d’annulation | `{{event_properties.${cancelled_at}}}` |
| Total des remises | `{{event_properties.${total_discounts}}}` |
| Prix total | `{{event_properties.${total_price}}}` |
| Balises | `{{event_properties.${tags}}}` |
| Codes de remise | `{{event_properties.${discount_codes}}}` |
| ID d’article | `{{event_properties.${line_items}[0].product_id}}` |
| Quantité d’articles | `{{event_properties.${line_items}[0].quantity}}` |
| Unité de gestion des stocks de l’article | `{{event_properties.${line_items}[0].sku}}` |
| Titre de l'élément | `{{event_properties.${line_items}[0].title}}` |
| Fournisseur de l’article | `{{event_properties.${line_items}[0].vendor}}` |
| Propriétés de l’élément | `{{event_properties.${line_items}[0].properties}}` |
| Prix de l’article | `{{event_properties.${line_items}[0].price}}` |
| Titre de l’expédition | `{{event_properties.${shipping}[0].title}}` |
| Prix de l’expédition | `{{event_properties.${shipping}[0].price}}` |
{% endraw %}

{% endtab %}
{% tab Purchase %}

**Événement** : Achat<br>
**Type** : [Événement d’achat Braze]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/)

{% raw %}
| Variable | Modèles Liquid |
| --- | --- |
| Unité de gestion des stocks de l’article | `{{event_properties.${line_items}[0].sku}}` |
| Titre de l'élément  | `{{event_properties.${line_items}[0].title}}` |
| Fournisseur de l’article | `{{event_properties.${line_items}[0].vendor}}` |
| Propriétés de l’élément | `{{event_properties.${line_items}[0].properties}}` |
{% endraw %}

{% endtab %}
{% tab Order Paid %}
**Événement** : `shopify_paid_order`<br>
**Type** : [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Modèles Liquid |
| --- | --- |
| ID de commande | `{{event_properties.${order_id}}}` |
| État confirmé | `{{event_properties.${confirmed}}}` |
| URL du statut de la commande | `{{event_properties.${order_status_url}}}` |
| Numéro de commande | `{{event_properties.${order_number}}}` |
| Horodatage d’annulation | `{{event_properties.${cancelled_at}}}` |
| Total des remises | `{{event_properties.${total_discounts}}}` |
| Prix total | `{{event_properties.${total_price}}}` |
| Balises | `{{event_properties.${tags}}}` |
| Codes de remise | `{{event_properties.${discount_codes}}}` |
| ID d’article | `{{event_properties.${line_items}[0].product_id}}` |
| Quantité d’articles | `{{event_properties.${line_items}[0].quantity}}` |
| Unité de gestion des stocks de l’article | `{{event_properties.${line_items}[0].sku}}` |
| Titre de l'élément | `{{event_properties.${line_items}[0].title}}` |
| Fournisseur de l’article | `{{event_properties.${line_items}[0].vendor}}` |
| Propriétés de l’élément | `{{event_properties.${line_items}[0].properties}}` |
| Prix de l’article | `{{event_properties.${line_items}[0].price}}` |
| Titre de l’expédition | `{{event_properties.${shipping}[0].title}}` |
| Prix de l’expédition | `{{event_properties.${shipping}[0].price}}` |
{% endraw %}
{% endtab %}

{% tab Partially Fulfilled Order %}
**Événement** : `shopify_partially_fulfilled_order`<br>
**Type** : [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Modèles Liquid |
| --- | --- |
| ID de commande | `{{event_properties.${order_id}}}` |
| Prix total | `{{event_properties.${total_price}}}` |
| Total des remises | `{{event_properties.${total_discounts}}}` |
| État confirmé | `{{event_properties.${confirmed}}}` |
| URL du statut de la commande | `{{event_properties.${order_status_url}}}` |
| Numéro de commande | `{{event_properties.${order_number}}}` |
| Horodatage d’annulation | `{{event_properties.${cancelled_at}}}` |
| Horodatage de fermeture | `{{event_properties.${closed_at}}}` |
| ID d’article | `{{event_properties.${line_items}[0].product_id}}` |
| Quantité d’articles | `{{event_properties.${line_items}[0].quantity}}` |
| Unité de gestion des stocks de l’article | `{{event_properties.${line_items}[0].sku}}` |
| Titre de l'élément | `{{event_properties.${line_items}[0].title}}` |
| Fournisseur de l’article | `{{event_properties.${line_items}[0].vendor}}` |
| Nom de l’article | `{{event_properties.${line_items}[0].name}}` |
| Propriétés de l’élément | `{{event_properties.${line_items}[0].properties}}` |
| Prix de l’article | `{{event_properties.${line_items}[0].price}}` |
| Titre de l’expédition | `{{event_properties.${shipping}[0].title}}` |
| Prix de l’expédition | `{{event_properties.${shipping}[0].price}}` |
| État de la commande | `{{event_properties.${fulfillment_status}}}` |
| Statut d’envoi de la commande | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| État de la commande | `{{event_properties.${fulfillments}[0].status}}` |
| Entreprise de suivi de la commande | `{{event_properties.${fulfillments}[0].tracking_company}}` |
| Numéro de suivi de la commande | `{{event_properties.${fulfillments}[0].tracking_number}}` |
| Numéros de suivi de la commande | `{{event_properties.${fulfillments}[0].tracking_numbers}}` |
| URL de suivi de la commande | `{{event_properties.${fulfillments}[0].tracking_url}}` |
| URLs de suivi de la commande | `{{event_properties.${fulfillments}[0].tracking_urls}}` |
| État de la commande | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| Nom de la commande | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| Prix de la commande | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| ID produit de la commande | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| Quantité de la commande | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| Expédition de la commande | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| Unité de gestion des stocks de la commande | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| Titre de la commande | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| Fournisseur de la commande | `{{event_properties.${fulfillments}[0].line_items[0].vendor` | 
{% endraw %}
{% endtab %}

{% tab Fulfilled Order %}
**Événement** : `shopify_fulfilled_order`<br>
**Type** : [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Modèles Liquid |
| --- | --- |
| ID de commande | `{{event_properties.${order_id}}}` |
| Prix total | `{{event_properties.${total_price}}}` |
| Total des remises | `{{event_properties.${total_discounts}}}` |
| État confirmé | `{{event_properties.${confirmed}}}` |
| URL du statut de la commande | `{{event_properties.${order_status_url}}}` |
| Numéro de commande | `{{event_properties.${order_number}}}` |
| Horodatage d’annulation | `{{event_properties.${cancelled_at}}}` |
| Horodatage de fermeture | `{{event_properties.${closed_at}}}` |
| ID d’article | `{{event_properties.${line_items}[0].product_id}}` |
| Quantité d’articles | `{{event_properties.${line_items}[0].quantity}}` |
| Unité de gestion des stocks de l’article | `{{event_properties.${line_items}[0].sku}}` |
| Titre de l'élément | `{{event_properties.${line_items}[0].title}}` |
| Fournisseur de l’article | `{{event_properties.${line_items}[0].vendor}}` |
| Nom de l’article | `{{event_properties.${line_items}[0].name}}` |
| Propriétés de l’élément | `{{event_properties.${line_items}[0].properties}}` |
| Prix de l’article | `{{event_properties.${line_items}[0].price}}` |
| Titre de l’expédition | `{{event_properties.${shipping}[0].title}}` |
| Prix de l’expédition | `{{event_properties.${shipping}[0].price}}` |
| État de la commande | `{{event_properties.${fulfillment_status}}}` |
| Statut d’envoi de la commande | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| Statut | `{{event_properties.${fulfillments}[0].status}}` |
| Entreprise de suivi de la commande | `{{event_properties.${fulfillments}[0].Fulfillment tracking_company}}` |
| Numéro de suivi de la commande | `{{event_properties.${fulfillments}[0].Fulfillment tracking_number}}` |
| Numéros de suivi de la commande | `{{event_properties.${fulfillments}[0].Fulfillment tracking_numbers}}` |
| URL de suivi de la commande | `{{event_properties.${fulfillments}[0].Fulfillment tracking_url}}` |
| URLs de suivi de la commande | `{{event_properties.${fulfillments}[0].Fulfillment tracking_urls}}` |
| État de la commande | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| Nom de la commande | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| Prix de la commande | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| ID produit de la commande | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| Quantité de la commande | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| Expédition de la commande | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| Unité de gestion des stocks de la commande | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| Titre de la commande | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| Fournisseur de la commande | `{{event_properties.${fulfillments}[0].line_items[0].vendor` | 
{% endraw %}
{% endtab %}

{% tab Cancelled Order %}
**Événement** : `shopify_cancelled_order`<br>
**Type** : [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Modèles Liquid |
| --- | --- |
| ID de commande | `{{event_properties.${order_id}}}` |
| Prix total | `{{event_properties.${total_price}}}` |
| Total des remises | `{{event_properties.${total_discounts}}}` |
| Confirmé | `{{event_properties.${confirmed}}}` |
| URL du statut de la commande | `{{event_properties.${order_status_url}}}` |
| Numéro de commande | `{{event_properties.${order_number}}}` |
| Horodatage d’annulation | `{{event_properties.${cancelled_at}}}` |
| Balises | `{{event_properties.${tags}}}` |
| Codes de remise | `{{event_properties.${discount_codes}}}` |
| État de la commande | `{{event_properties.${fulfillment_status}}}` |
| Commandes | `{{event_properties.${fulfillments}}}` |
| ID d’article | `{{event_properties.${line_items}[0].product_id}}` |
| Quantité d’articles | `{{event_properties.${line_items}[0].quantity}}` |
| Unité de gestion des stocks de l’article | `{{event_properties.${line_items}[0].sku}}` |
| Titre de l'élément | `{{event_properties.${line_items}[0].title}}` |
| Fournisseur de l’article | `{{event_properties.${line_items}[0].vendor}}` |
| Nom de l’article | `{{event_properties.${line_items}[0].name}}` |
| Propriétés de l’élément | `{{event_properties.${line_items}[0].properties}}` |
| État de la commande | `{{event_properties.${line_items}[0].fulfillment_status}}` |
| Titre de l’expédition | `{{event_properties.${shipping}[0].title}}` |
| Prix de l’expédition | `{{event_properties.${shipping}[0].price}}` |
{% endraw %}
{% endtab %}


{% tab Created Refund %}
**Événement** : `shopify_created_refund`<br>
**Type** : [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Modèles Liquid |
| --- | --- |
| ID de commande | `{{event_properties.${order_id}}}` |
| Remarque concernant la commande | `{event_properties.${note}}}` |
| ID d’article | `{{event_properties.${line_items}[0].product_id}}` |
| Quantité d’articles | `{{event_properties.${line_items}[0].quantity}}` |
| Unité de gestion des stocks de l’article | `{{event_properties.${line_items}[0].sku}}` |
| Titre de l'élément | `{{event_properties.${line_items}[0].title}}` |
| Fournisseur de l’article | `{{event_properties.${line_items}[0].vendor}}` |
| Nom de l’article | `{{event_properties.${line_items}[0].name}}` |
| Propriétés de l’élément | `{{event_properties.${line_items}[0].properties}}` |
| Prix de l’article | `{{event_properties.${line_items}[0].price}}` |
{% endraw %}
{% endtab %}
{% endtabs %}

## Segmentation

Vous pouvez filtrer les événements de Shopify avec tous les [filtres personnalisés existants]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) dans Segmentation. 

![Page de détails du segment pour un segment Shopify_Test avec le filtre pour l’événement personnalisé « shopify_checkouts_abandon » mis en évidence.][12]{: style="max-width:80%;"}

En outre, vous pouvez également utiliser le filtre d’étendue des achats de Braze pour créer des segments d’utilisateurs basés sur :
- Premier/dernier achat
- Premier/dernier achat pour une application spécifique
- Produits déjà achetés au cours des 30 derniers jours
- Nombre d’achats qu’ils ont effectués

![Filtre de segmentation pour les utilisateurs ayant effectué leur premier achat après le 17 octobre 2020.][13]

![Recherche d’un ID du produit spécifique comme filtre de segmentation.][14]

{% alert note %}
Si vous cherchez à segmenter par propriétés de l’événement personnalisées, assurez-vous de travailler avec votre gestionnaire du succès des clients ou [l’assistance]({{site.baseurl}}/braze_support/) Braze pour activer le filtrage de toutes les propriétés de l’événement pertinentes que vous souhaitez utiliser dans la segmentation et Liquid.
{% endalert %} 

## Déclenchement de campagne et de Canvas 

Avec les événements personnalisés Shopify dans Braze, vous pouvez déclencher des Canvas ou des campagnes comme vous le feriez normalement avec n’importe quel autre [événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-storage). Par exemple, vous pouvez créer un Canvas par événement qui se déclenche suite à un événement `shopify_checkouts_abandon` Shopify au sein des critères d’entrée du Canvas. 

![Canvas par événement qui saisit les utilisateurs qui effectuent l’événement personnalisé « shopify_checkouts_abandon ».][5]

Avec la prise en charge des objets imbriqués pour les propriétés de l’événement personnalisées, les clients peuvent désormais déclencher des campagnes et des Canvas à l’aide d’une propriété de l’événement imbriqué. Voici un exemple de déclenchement d’une campagne utilisant un produit spécifique de l’événement personnalisé `shopify_created_order`. Assurez-vous d’utiliser `list_items[].product_id` pour indexer votre liste d’articles et accéder à l’ID de produit.

![Campagne par événement qui envoie aux utilisateurs qui effectuent l’événement personnalisé « shopify_created_order » où la propriété imbriquée « product_id » est égale à un nombre spécifique.][26]

[5]: {% image_buster /assets/img/Shopify/shopify_integration11.png %}
[12]: {% image_buster /assets/img/Shopify/shopify_segmentation2.png %}
[13]: {% image_buster /assets/img/Shopify/shopify_segmentation3.png %}
[14]: {% image_buster /assets/img/Shopify/shopify_segmentation4.png %}
[26]: {% image_buster /assets/img/Shopify/shopify_integration17.png %}
