---
nav_title: Données Shopify dans Braze
article_title: "Utilisation des données Shopify dans Braze"
description: "Cet article de référence explique comment utiliser les données Shopify dans Braze pour la personnalisation et la segmentation."
page_type: partner
search_tag: Partner
alias: "/shopify_data_legacy/"
page_order: 1
---

# Données Shopify dans Braze

> En utilisant la prise en charge des objets imbriqués pour les événements personnalisés, les clients de Braze Shopify peuvent utiliser les variables de modèle Liquid des propriétés de l'événement imbriqué.

Une fois l'installation de l'application terminée, Braze crée automatiquement votre webhook et l'intégration ScriptTag avec Shopify. Voir le tableau suivant pour plus de détails sur la façon dont les événements Shopify pris en charge correspondent aux événements personnalisés et aux attributs personnalisés de Braze.

## Événements Shopify pris en charge

{% tabs %}
{% tab Événements Shopify %}
{% subtabs global %}
{% subtab Product Viewed %}
**Événement**: `shopify_product_viewed`<br>
**Type** : [événement personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | liquid Templating |
| --- | --- |
| Identifiant de l'article | `{{event_properties.${id}}}` |
| titre de l'article | `{{event_properties.${title}}}` |
| Prix de l'article | `{{event_properties.${price}}}` |
| Vendeur de l’article | `{{event_properties.${vendor}}}` |
| Images de l’article | `{{event_properties.${images}}}` |


{% endraw %}
{% endsubtab %}


{% subtab Product Clicked %}
**Événement**: `shopify_product_clicked`<br>
**Type** : [événement personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | liquid Templating |
| --- | --- |
| Identifiant de l'article | `{{event_properties.${id}}}` |
| titre de l'article | `{{event_properties.${title}}}` |
| Prix de l'article | `{{event_properties.${price}}}` |
| Vendeur de l’article | `{{event_properties.${vendor}}}` |
| Images de l’article | `{{event_properties.${images}}}` |
{% endraw %}
{% endsubtab %}


{% subtab Abandoned Cart %}
**Événement**: `shopify_abandoned_cart`<br>
**Type** : [événement personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | liquid Templating |
| --- | --- |
| ID panier | `{{event_properties.${cart_id}}}` |
| Identifiant de l'article | `{{event_properties.${line_items}[0].product_id}}` |
| Quantité d'articles | `{{event_properties.${line_items}[0].quantity}}` |
| Référence de l'article | `{{event_properties.${line_items}[0].sku}}` |
| Titre de l'article | `{{event_properties.${line_items}[0].title}}` |
| Vendeur de l’article | `{{event_properties.${line_items}[0].vendor}}` |
| Propriétés de l'article | `{{event_properties.${line_items}[0].properties}}` |
| Prix de l'article | `{{event_properties.${line_items}[0].price}}` |
| ID de la variante | `{{event_properties.${line_items}[0].variant_id}}` |
{% endraw %}
{% endsubtab %}


{% subtab Abandoned Checkout %}
**Événement**: `shopify_abandoned_checkout`<br>
**Type** : [événement personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | liquid Templating |
| --- | --- |
| ID de paiement | `{{event_properties.${checkout_id}}}` |
| URL de panier abandonné | `{{event_properties.${abandoned_checkout_url}}}` |
| Code de réduction | `{{event_properties.${discount_code}}}` |
| Prix total | `{{event_properties.${total_price}}}` |
| Montant de la remise | `{{event_properties.${applied_discount}[0].amount}}` |
| Titre de la remise | `{{event_properties.${applied_discount}[0].title}}` |
| Description de la remise | `{{event_properties.${applied_discount}[0].description}}` |
| Identifiant de l'article | `{{event_properties.${line_items}[0].product_id}}` |
| Quantité d'articles | `{{event_properties.${line_items}[0].quantity}}` |
| Référence de l'article | `{{event_properties.${line_items}[0].sku}}` |
| Titre de l'article | `{{event_properties.${line_items}[0].title}}` |
| Vendeur de l’article | `{{event_properties.${line_items}[0].vendor}}` |
| Propriétés de l'article | `{{event_properties.${line_items}[0].properties}}` |
| Prix de l'article | `{{event_properties.${line_items}[0].price}}` |
| ID de la variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Titre de la variante | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}


{% subtab Created Order %}


**Événement**: `shopify_created_order`<br>
**Type** : [événement personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)

{% raw %}
| Variable | liquid Templating |
| --- | --- |
| ID de commande | `{{event_properties.${order_id}}}` |
Statut Confirmé | `{{event_properties.${confirmed}}}` |
| URL de statut de la commande | `{{event_properties.${order_status_url}}}` |
| Numéro de commande | `{{event_properties.${order_number}}}` |
| Horodatage annulé | `{{event_properties.${cancelled_at}}}` |
| Réductions totales | `{{event_properties.${total_discounts}}}` |
| Prix total | `{{event_properties.${total_price}}}` |
| tags | `{{event_properties.${tags}}}` |
| Codes de réduction | `{{event_properties.${discount_codes}}}` |
| Identifiant de l'article | `{{event_properties.${line_items}[0].product_id}}` |
| Quantité d'articles | `{{event_properties.${line_items}[0].quantity}}` |
| Référence de l'article | `{{event_properties.${line_items}[0].sku}}` |
| Titre de l'article | `{{event_properties.${line_items}[0].title}}` |
| Vendeur de l’article | `{{event_properties.${line_items}[0].vendor}}` |
| Propriétés de l'article | `{{event_properties.${line_items}[0].properties}}` |
| Prix de l'article | `{{event_properties.${line_items}[0].price}}` |
| ID de la variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Titre de la variante | `{{event_properties.${line_items}[0].variant_title}}` |
| Titre d'expédition | `{{event_properties.${shipping}[0].title}}` |
| Prix d'expédition | `{{event_properties.${shipping}[0].price}}` |
Boutique Shopify | `{{event_properties.${shopify_storefront}}}` |
| État d’achèvement | `{{event_properties.${fulfillment_status}}}` |
| Site référent | `{{event_properties.${referring_site}}}` |
| Noms des passerelles de paiement | `{{event_properties.${payment_gateway_names}}}` |
| Adresse de livraison ligne 1 | `{{event_properties.${shipping_address[0].address1}}}` |
Adresse de livraison ligne 2 | `{{event_properties.${shipping_address[0].address2}}}` |
| Adresse de livraison Ville | `{{event_properties.${shipping_address[0].city}}}` |
| Pays de l'adresse de livraison | `{{event_properties.${shipping_address[0].country}}}` |
| Prénom de l'adresse de livraison | `{{event_properties.${shipping_address[0].first_name}}}` |
| Nom de famille de l'adresse de livraison | `{{event_properties.${shipping_address[0].last_name}}}` |
| Adresse de livraison Province | `{{event_properties.${shipping_address[0].province}}}` |
| Adresse de livraison Code postal | `{{event_properties.${shipping_address[0].zip}}}` |
Adresse de facturation ligne 1 | `{{event_properties.${billing_address[0].address1}}}` |
Adresse de facturation ligne 2 | `{{event_properties.${billing_address[0].address2}}}` |
| Ville de l'adresse de facturation | `{{event_properties.${billing_address[0].city}}}` |
| Pays de l'adresse de facturation | `{{event_properties.${billing_address[0].country}}}` |
| Prénom de l'adresse de facturation | `{{event_properties.${billing_address[0].first_name}}}` |
| Nom de famille de l'adresse de facturation | `{{event_properties.${shipping_address[0].last_name}}}` |
| Adresse de facturation Province | `{{event_properties.${billing_address[0].province}}}` |
| Adresse de facturation Code postal | `{{event_properties.${billing_address[0].zip}}}` |
{% endraw %}


{% endsubtab %}
{% subtab Purchase %}


**Événement**: Achat<br>
**Type** : [Événement d’achat Braze]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/)


{% raw %}
| Variable | liquid Templating |
| --- | --- |
| Référence de l'article | `{{event_properties.${line_items}[0].sku}}` |
| titre de l'article | `{{event_properties.${line_items}[0].title}}` |
| Vendeur de l’article | `{{event_properties.${line_items}[0].vendor}}` |
| Propriétés de l'article | `{{event_properties.${line_items}[0].properties}}` |
| ID de la variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Titre de la variante | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}


{% endsubtab %}
{% subtab Paid Order %}
**Événement**: `shopify_paid_order`<br>
**Type** : [événement personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | liquid Templating |
| --- | --- |
| ID de commande | `{{event_properties.${order_id}}}` |
Statut Confirmé | `{{event_properties.${confirmed}}}` |
| URL de statut de la commande | `{{event_properties.${order_status_url}}}` |
| Numéro de commande | `{{event_properties.${order_number}}}` |
| Horodatage annulé | `{{event_properties.${cancelled_at}}}` |
| Réductions totales | `{{event_properties.${total_discounts}}}` |
| Prix total | `{{event_properties.${total_price}}}` |
| tags | `{{event_properties.${tags}}}` |
| Codes de réduction | `{{event_properties.${discount_codes}}}` |
| Identifiant de l'article | `{{event_properties.${line_items}[0].product_id}}` |
| Quantité d'articles | `{{event_properties.${line_items}[0].quantity}}` |
| Référence de l'article | `{{event_properties.${line_items}[0].sku}}` |
| Titre de l'article | `{{event_properties.${line_items}[0].title}}` |
| Vendeur de l’article | `{{event_properties.${line_items}[0].vendor}}` |
| Propriétés de l'article | `{{event_properties.${line_items}[0].properties}}` |
| Prix de l'article | `{{event_properties.${line_items}[0].price}}` |
| Titre d'expédition | `{{event_properties.${shipping}[0].title}}` |
| Prix d'expédition | `{{event_properties.${shipping}[0].price}}` |
| ID de la variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Titre de la variante | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}


{% subtab Partially Fulfilled Order %}
**Événement**: `shopify_partially_fulfilled_order`<br>
**Type** : [événement personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | liquid Templating |
| --- | --- |
| ID de commande | `{{event_properties.${order_id}}}` |
| Prix total | `{{event_properties.${total_price}}}` |
| Réductions totales | `{{event_properties.${total_discounts}}}` |
Statut Confirmé | `{{event_properties.${confirmed}}}` |
| URL de statut de la commande | `{{event_properties.${order_status_url}}}` |
| Numéro de commande | `{{event_properties.${order_number}}}` |
| Horodatage annulé | `{{event_properties.${cancelled_at}}}` |
| Horodatage fermé | `{{event_properties.${closed_at}}}` |
| Identifiant de l'article | `{{event_properties.${line_items}[0].product_id}}` |
| Quantité d'articles | `{{event_properties.${line_items}[0].quantity}}` |
| Référence de l'article | `{{event_properties.${line_items}[0].sku}}` |
| Titre de l'article | `{{event_properties.${line_items}[0].title}}` |
| Vendeur de l’article | `{{event_properties.${line_items}[0].vendor}}` |
| Nom de l'article | `{{event_properties.${line_items}[0].name}}` |
| Propriétés de l'article | `{{event_properties.${line_items}[0].properties}}` |
| Prix de l'article | `{{event_properties.${line_items}[0].price}}` |
| Titre d'expédition | `{{event_properties.${shipping}[0].title}}` |
| Prix d'expédition | `{{event_properties.${shipping}[0].price}}` |
| État d’achèvement | `{{event_properties.${fulfillment_status}}}` |
| État de l'expédition | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| État d’achèvement | `{{event_properties.${fulfillments}[0].status}}` |
| Société de suivi des commandes | `{{event_properties.${fulfillments}[0].tracking_company}}` |
| Numéro de suivi de l'exécution | `{{event_properties.${fulfillments}[0].tracking_number}}` |
| Numéros de suivi de la commande | `{{event_properties.${fulfillments}[0].tracking_numbers}}` |
| URL de suivi de l'exécution | `{{event_properties.${fulfillments}[0].tracking_url}}` |
| URL de suivi de l'exécution des commandes | `{{event_properties.${fulfillments}[0].tracking_urls}}` |
| État d’achèvement | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| Nom de réalisation | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| Prix de l’exécution des commandes | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| ID de produit de la commande | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| Quantité commandée | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| Expédition de la commande | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| UGS de la commande | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
Titre de la commande | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| Fournisseur de la commande | `{{event_properties.${fulfillments}[0].line_items[0].vendor` |
| ID de la variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Titre de la variante | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}


{% subtab Fulfilled Order %}
**Événement**: `shopify_fulfilled_order`<br>
**Type** : [événement personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | liquid Templating |
| --- | --- |
| ID de commande | `{{event_properties.${order_id}}}` |
| Prix total | `{{event_properties.${total_price}}}` |
| Réductions totales | `{{event_properties.${total_discounts}}}` |
Statut Confirmé | `{{event_properties.${confirmed}}}` |
| URL de statut de la commande | `{{event_properties.${order_status_url}}}` |
| Numéro de commande | `{{event_properties.${order_number}}}` |
| Horodatage annulé | `{{event_properties.${cancelled_at}}}` |
| Horodatage fermé | `{{event_properties.${closed_at}}}` |
| Identifiant de l'article | `{{event_properties.${line_items}[0].product_id}}` |
| Quantité d'articles | `{{event_properties.${line_items}[0].quantity}}` |
| Référence de l'article | `{{event_properties.${line_items}[0].sku}}` |
| Titre de l'article | `{{event_properties.${line_items}[0].title}}` |
| Vendeur de l’article | `{{event_properties.${line_items}[0].vendor}}` |
| Nom de l'article | `{{event_properties.${line_items}[0].name}}` |
| Propriétés de l'article | `{{event_properties.${line_items}[0].properties}}` |
| Prix de l'article | `{{event_properties.${line_items}[0].price}}` |
| Titre d'expédition | `{{event_properties.${shipping}[0].title}}` |
| Prix d'expédition | `{{event_properties.${shipping}[0].price}}` |
| État d’achèvement | `{{event_properties.${fulfillment_status}}}` |
| État de l'expédition | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| État | `{{event_properties.${fulfillments}[0].status}}` |
| Société de suivi des commandes | `{{event_properties.${fulfillments}[0].Fulfillment tracking_company}}` |
| Numéro de suivi de l'exécution | `{{event_properties.${fulfillments}[0].Fulfillment tracking_number}}` |
| Numéros de suivi de la commande | `{{event_properties.${fulfillments}[0].Fulfillment tracking_numbers}}` |
| URL de suivi de l'exécution | `{{event_properties.${fulfillments}[0].Fulfillment tracking_url}}` |
| URL de suivi de l'exécution des commandes | `{{event_properties.${fulfillments}[0].Fulfillment tracking_urls}}` |
| État d’achèvement | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| Nom de réalisation | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| Prix de l’exécution des commandes | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| ID de produit de la commande | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| Quantité commandée | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| Expédition de la commande | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| UGS de la commande | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
Titre de la commande | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| Fournisseur de la commande | `{{event_properties.${fulfillments}[0].line_items[0].vendor` |
| ID de la variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Titre de la variante | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}


{% subtab Cancelled Order %}
**Événement**: `shopify_cancelled_order`<br>
**Type** : [événement personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | liquid Templating |
| --- | --- |
| ID de commande | `{{event_properties.${order_id}}}` |
| Prix total | `{{event_properties.${total_price}}}` |
| Réductions totales | `{{event_properties.${total_discounts}}}` |
Confirmé | `{{event_properties.${confirmed}}}` |
| URL de statut de la commande | `{{event_properties.${order_status_url}}}` |
| Numéro de commande | `{{event_properties.${order_number}}}` |
| Horodatage annulé | `{{event_properties.${cancelled_at}}}` |
| tags | `{{event_properties.${tags}}}` |
| Codes de réduction | `{{event_properties.${discount_codes}}}` |
| État d’achèvement | `{{event_properties.${fulfillment_status}}}` |
| Exécutions | `{{event_properties.${fulfillments}}}` |
| Identifiant de l'article | `{{event_properties.${line_items}[0].product_id}}` |
| Quantité d'articles | `{{event_properties.${line_items}[0].quantity}}` |
| Référence de l'article | `{{event_properties.${line_items}[0].sku}}` |
| Titre de l'article | `{{event_properties.${line_items}[0].title}}` |
| Vendeur de l’article | `{{event_properties.${line_items}[0].vendor}}` |
| Nom de l'article | `{{event_properties.${line_items}[0].name}}` |
| Propriétés de l'article | `{{event_properties.${line_items}[0].properties}}` |
| État d’achèvement | `{{event_properties.${line_items}[0].fulfillment_status}}` |
| Titre d'expédition | `{{event_properties.${shipping}[0].title}}` |
| Prix d'expédition | `{{event_properties.${shipping}[0].price}}` |
| ID de la variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Titre de la variante | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}

{% subtab Created Refund %}
**Événement**: `shopify_created_refund`<br>
**Type** : [événement personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | liquid Templating |
| --- | --- |
| ID de commande | `{{event_properties.${order_id}}}` |
| Note de commande | `{event_properties.${note}}}` |
| Identifiant de l'article | `{{event_properties.${line_items}[0].product_id}}` |
| Quantité d'articles | `{{event_properties.${line_items}[0].quantity}}` |
| Référence de l'article | `{{event_properties.${line_items}[0].sku}}` |
| Titre de l'article | `{{event_properties.${line_items}[0].title}}` |
| Vendeur de l’article | `{{event_properties.${line_items}[0].vendor}}` |
| Nom de l'article | `{{event_properties.${line_items}[0].name}}` |
| Propriétés de l'article | `{{event_properties.${line_items}[0].properties}}` |
| Prix de l'article | `{{event_properties.${line_items}[0].price}}` |
| ID de la variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Titre de la variante | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Exemple de charge utile %}
{% subtabs global %}
{% subtab Product Viewed %}
```json
{
 "name": "shopify_product_viewed",
 "properties": {
     "id": 5971657097407,
     "title": "Example T-Shirt",
     "price": 1999,
     "vendor": "Acme",
     "images": [
         "//cdn.shopify.com/s/files/1/0503/3849/6703/products/green-t-shirt.jpg?v=1603397913"
     ]
 }
}
```
{% endsubtab %}
{% subtab Product Clicked %}
```json
{
   "name": "shopify_product_clicked",
   "properties": {
       "id": 5971657097407,
       "title": "Example T-Shirt",
       "price": 1999,
       "vendor": "Acme",
       "images": [
           "//cdn.shopify.com/s/files/1/0503/3849/6703/products/green-t-shirt.jpg?v=1603397913"
       ]
   }
}
```
{% endsubtab %}
{% subtab Abandoned Cart %}
```json
{
   "name": "shopify_abandoned_cart",
   "time": "2022-10-14T15:08:31.571Z",
   "properties": {
     "cart_id": "163989958f6b0de13f3b4f702fa5ee0d",
     "line_items": [
       {
         "price": 60,
         "product_id": 7110622675033,
         "properties": null,
         "quantity": 1,
         "sku": null,
         "title": "Spinach Surprise Smoothie - 12 Pack",
         "variant_id": 40094740545625,
         "vendor": "Jennifer's Juice"
       }
     ]
   },
   "braze_id": "63497b3ca3eabd0053380451"
 }

```
{% endsubtab %}
{% subtab Abandoned Checkout %}
```json
{
 "name": "shopify_abandoned_checkout",
 "time": "2020-09-10T18:53:37-04:00",
 "properties": {
   "applied_discount": {
     "amount": "30.00",
     "title": "XYZPromotion",
     "description": "Promotionalitemforblackfriday."
   },
   "discount_code": "30_DOLLARS_OFF",
   "total_price": "398.00",
   "line_items": [
     {
   "price": "199.00",
   "properties": {},       
   "product_id": 632910392,
       "quantity": 1,
       "sku": "IPOD2008PINK",
       "title": "IPodNano-8GB",
       "variant_id": 40094740545625,
       "variant_title": "Pink iPod Nano 8 GB",
       "vendor": "Apple",
     }
   ],
   "abandoned_checkout_url": "https://checkout.local/690933842/checkouts/123123123/recover?key=example-secret-token",
   "checkout_id": "123123123"
 }
}
```
{% endsubtab %}
{% subtab Created Order %}
```json
{
 "name": "shopify_created_order",
 "time": "2020-09-10T18:53:45-04:00",
 "properties": {
   "total_discounts": "5.00",
   "total_price": "403.00",
   "discount_codes": [],
   "line_items": [
     {
       "product_id": 632910392,
       "quantity": 1,
       "sku": "IPOD2008PINK",
       "title": "IPodNano-8GB",
       "variant_id": 40094740545625,
       "variant_title": "Pink iPod Nano 8 GB",
       "vendor": null,
       "name": "IPodNano-8GB",
       "properties": [],
       "price": "199.00"
     },
     {
       "product_id": 632910393,
       "quantity": 1,
       "sku": "IPOD2008SILVER",
       "title": "IPodNano-8GB",
       "variant_id": 40094740545626,
       "variant_title": "Silver iPod Nano 8 GB",
       "vendor": null,
       "name": "IPodNano-8GB",
       "properties": [],
       "price": "199.00"
     }
   ],
   "order_id": 820982911946154500,
   "confirmed": false,
   "order_status_url": "https://apple.myshopify.com/690933842/orders/123456abcd/authenticate?key=abcdefg",
   "order_number": 1234,
   "cancelled_at": "2020-09-10T18:53:45-04:00",
   "shipping": [
     {
       "title": "Standard",
       "price": "10.00"
     },
     {
       "title": "Expedited",
       "price": "25.00"
     }
   ],
   "tags": "heavy"
 }
}
```
{% endsubtab %}
{% subtab Purchase %}
```json
{
 "product_id": 632910392,
 "currency": "USD",
 "price": "199.00",
 "time": "2020-09-10T18:53:45-04:00",
 "quantity": 1,
 "source": "shopify",
 "properties": {
   "name": "IPodNano-8GB",
   "sku": "IPOD2008PINK",
   "variant_id": 40094740545626,
   "variant_title": "Silver iPod Nano 8 GB",
   "vendor": null,
   "properties": []
 }
}
```
{% endsubtab %}
{% subtab Paid Order %}
```json
{
 "name": "shopify_paid_order",
 "time": "2022-05-23T13:52:38-04:00",
 "properties": {
   "order_id": 4444596371647,
   "line_items": [
     {
       "quantity": 1,
       "product_id": 6143033344191,
       "sku": null,
       "title": "LED High Tops",
       "variant_id": 40094740549876,
       "variant_title": null,
       "vendor": "partners-demo",
       "name": "LED High Tops",
       "properties": [],
       "price": "80.00",
       "fulfillment_status": null
     }
   ],
 }
}
```
{% endsubtab %}
{% subtab Partially Fulfilled Order %}
```json
{
 "name": "shopify_partially_fulfilled_order",
 "time": "2022-05-23T14:43:34-04:00",
 "properties": {
   "order_id": 4444668657855,
   "line_items": [
     {
       "quantity": 1,
       "product_id": 6143032066239,
       "sku": null,
       "title": "Dark Denim Top",
       "variant_id": 40094740549876,
       "variant_title": "",
       "vendor": "partners-demo",
       "name": "Dark Denim Top",
       "properties": [],
       "price": "60.00",
       "fulfillment_status": "fulfilled"
     }
   ],
   "shipping": [
     {
       "title": "Standard",
       "price": "0.00"
     }
   ],
   "total_price": "130.66",
   "confirmed": true,
   "total_discounts": "0.00",
   "discount_codes": [],
   "order_number": 1093,
   "order_status_url": "https://test-store.myshopify.com/",
   "cancelled_at": null,
   "tags": "",
   "closed_at": null,
   "fulfillment_status": "partial",
   "fulfillments": [
     {
       "shipment_status": null,
       "status": "success",
       "tracking_company": "Other",
       "tracking_number": "123",
       "tracking_numbers": [
         "123"
       ],
       "tracking_url": "https://braze.com",
       "tracking_urls": [
         "https://braze.com"
       ],
       "line_items": [
         {
           "fulfillment_status": "fulfilled",
           "name": "Dark Denim Top",
           "price": "60.00",
           "product_id": 6143032066239,
           "properties": [],
           "quantity": 1,
           "requires_shipping": true,
           "sku": null,
           "title": "Dark Denim Top",
           "variant_id": 40094740549876,
           "variant_title": "",
           "vendor": "partners-demo"
         }
       ]
     }
   ]
 },
 "braze_id": "abc123abc123"
}
```
{% endsubtab %}
{% subtab Fulfilled Order %}
```json
{
 "name": "shopify_fulfilled_order",
 "time": "2022-05-23T14:44:34-04:00",
 "properties": {
   "order_id": 4444668657855,
   "line_items": [
     {
       "quantity": 1,
       "product_id": 6143032066239,
       "sku": null,
       "title": "Dark Denim Top",
  "variant_id": 40094740549876,
       "variant_title": "Small Dark Denim Top",


       "vendor": "partners-demo",
       "name": "Dark Denim Top",
       "properties": [],
       "price": "60.00",
       "fulfillment_status": "fulfilled"
     }
   ],
   "shipping": [
     {
       "title": "Standard",
       "price": "0.00"
     }
   ],
   "total_price": "130.66",
   "confirmed": true,
   "total_discounts": "0.00",
   "discount_codes": [],
   "order_number": 1093,
   "order_status_url": "https://test-store.myshopify.com/",
   "cancelled_at": null,
   "tags": "",
   "closed_at": "2022-05-23T14:44:34-04:00",
   "fulfillment_status": "fulfilled",
   "fulfillments": [
     {
       "shipment_status": null,
       "status": "success",
       "tracking_company": "Other",
       "tracking_number": "456",
       "tracking_numbers": [
         "456"
       ],
       "tracking_url": "https://braze.com",
       "tracking_urls": [
         "https://braze.com"
       ],
       "line_items": [
         {
           "fulfillment_status": "fulfilled",
           "name": "Dark Denim Top",
           "price": "60.00",
           "product_id": 6143032066239,
           "quantity": 1,
           "requires_shipping": true,
           "sku": null,
           "title": "Dark Denim Top",
           "variant_id": 40094740549876,
           "variant_title": "Small Dark Denim Top",
           "vendor": "partners-demo"
         }
       ]
     }
   ]
 },
 "braze_id": "123abc123abc"
}
```
{% endsubtab %}
{% subtab Cancelled Order %}
```json
{
 "name": "shopify_cancelled_order",
 "time": "2022-05-23T14:40:52-04:00",
 "properties": {
   "order_id": 4444596371647,
   "line_items": [
     {
       "quantity": 1,
       "product_id": 6143033344191,
       "sku": null,
       "title": "LED High Tops",
       "variant_id": 40094740549876,
       "variant_title": "",
       "vendor": "partners-demo",
       "name": "LED High Tops",
       "properties": [],
       "price": "80.00",
       "fulfillment_status": null
     }
   ],
   "shipping": [
     {
       "title": "Standard",
       "price": "0.00"
     }
   ],
   "total_price": "141.54",
   "confirmed": true,
   "total_discounts": "0.00",
   "discount_codes": [],
   "order_number": 1092,
   "order_status_url": "https://test-store.myshopify.com/",
   "cancelled_at": "2022-05-23T14:40:52-04:00",
   "tags": "",
   "closed_at": "2022-05-23T14:40:51-04:00",
   "fulfillment_status": null,
   "fulfillments": []
 },
 "braze_id": "123abc123abc"
}
```
{% endsubtab %}
{% subtab Created Refund %}
```json
{
 "name": "shopify_created_refund",
 "time": "2022-05-23T14:40:50-04:00",
 "properties": {
   "order_id": 4444596371647,
   "note": null,
   "line_items": [
     {
       "quantity": 1,
       "product_id": 6143033344191,
       "sku": null,
       "title": "LED High Tops",
       "variant_id": 40094740549876,
       "variant_title": "",
       "vendor": "partners-demo",
       "properties": [],
       "price": "80.00"
     },
     {
       "quantity": 1,
       "product_id": 6143032852671,
       "sku": null,
       "title": "Chequered Red Shirt",
       "variant_id": 40094796619876,
       "variant_title": "",
       "vendor": "partners-demo",
       "properties": [],
       "price": "50.00"
     }
   ]
 },
 "braze_id": "abc123abc123"
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Attributs personnalisés Shopify pris en charge
{% tabs local %}
{% tab Attributs personnalisés Shopify %}
| Nom de l'attribut | Description |
| --- | --- |
| `shopify_tags`  | Tags que le propriétaire de la boutique a attachées au client, formatées comme une chaîne de caractères de valeurs séparées par des virgules. Un client peut avoir jusqu'à 250 étiquette. Chaque étiquette peut avoir jusqu'à 255 caractères. |
| `shopify_total_spent` | Le montant total d'argent que le client a dépensé au cours de son historique de commandes. |
| `shopify_order_count` | Le nombre de commandes associées à ce client. Les commandes test et archivées ne sont pas prises en compte.
| `shopify_last_order_id` | L'ID de la dernière commande du client. |
| `shopify_last_order_name` | Le nom de la dernière commande du client. Ceci est directement lié au champ `name` sur la ressource de la commande. |
| `shopify_zipcode` | Le code postal du client de son adresse par défaut. |
| `shopify_province` | La province du client à partir de son adresse par défaut. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Personnalisation Liquid

Pour ajouter une personnalisation Liquid pour vos attributs personnalisés Shopify, sélectionnez **\+ Personnalisation**. Sélectionnez ensuite **Attributs personnalisés** comme type de personnalisation.

![La section "Ajouter une personnalisation" avec la liste déroulante "Attribut" étendue.]({% image_buster /assets/img/Shopify/add_personalization_2.png %}){: style="max-width:40%;"}

Après avoir sélectionné votre attribut personnalisé, saisissez une valeur par défaut et copiez l'extrait de code Liquid dans votre message.

![Coller un extrait de code Liquid dans un message.]({% image_buster /assets/img/Shopify/copy_liquid_snippet.png %})

#### Exemple de charge utile

```json
{
  "attributes": [
    {
      "shopify_tags": "VIP_customer",
      "shopify_total_spent": "60.00",
      "shopify_order_count": "3",
      "shopify_last_order_id": "1234567",
      "shopify_last_order_name": "test_order",
      "shopify_zipcode": "10001",
      "shopify_province": "null"
    }
  ]
}
```

{% endtab %}
{% tab Exemple de charge utile %}
{% subtabs %}
{% subtab Shopify Tags %}
```json
{
  "attributes": [
    {
      "shopify_tags": "VIP_customer",
      "shopify_total_spent": "60.00",
      "shopify_order_count": "3",
      "shopify_last_order_id": "1234567",
      "shopify_last_order_name": "test_order",
      "shopify_zipcode": "10001",
      "shopify_province": "null"
    }
  ]
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Attributs standard Shopify pris en charge

- e-mail
- Prénom
- Nom de famille
- Téléphone
- Ville
- Pays

{% alert note %}
Braze ne mettra à jour que les attributs personnalisés Shopify pris en charge et les attributs standard Braze s'il y a une différence dans les données du profil utilisateur existant. Par exemple, si les données entrantes de Shopify contiennent un prénom de Bob et que Bob existe déjà comme prénom sur le profil utilisateur de Braze, Braze ne déclenchera pas de mise à jour, et vous ne serez pas facturé un point de donnée.
{% endalert %}

## segmentation

Vous pouvez filtrer les événements de Shopify avec tous les [filtres personnalisés existants]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) dans la segmentation. 

![Page de détails du segment pour un segment d'essai Shopify_Test avec le filtre pour l'événement personnalisé "shopify_checkouts_abandon" en surbrillance.][12]{: style="max-width:80%;"}

En outre, vous pouvez utiliser le filtre d'étendue des achats dans Braze pour créer des segmentations d'utilisateurs basées sur :
- Premier/dernier achat
- Premier/dernier achat pour une application spécifique
- Produits qu'ils ont achetés au cours des 30 derniers jours
- Le nombre d'achats qu'ils ont effectués

![Filtre de segmentation pour les utilisateurs ayant effectué leur premier achat après le 17 octobre 2020.][13]

![Recherche d'un produit ID spécifique comme filtre de segmentation.][14]

{% alert note %}
Si vous cherchez à segmenter par propriétés d'événement personnalisé, assurez-vous de travailler avec votre gestionnaire de la satisfaction client ou le [support]({{site.baseurl}}/braze_support/) de Braze pour activer le filtrage de toutes les propriétés d'événement pertinentes que vous souhaitez utiliser dans la segmentation et liquid.
{% endalert %} 

## Déclenchement de campagnes et canvas 

Avec les événements personnalisés de Shopify dans Braze, vous pouvez déclencher des canvas ou des campagnes comme vous le feriez normalement avec tout autre [événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-storage). Par exemple, vous pouvez créer un canvas basé sur l'action qui se déclenche à partir de l'événement Shopify `shopify_checkouts_abandon` dans les critères d'entrée du canvas. 

![Canvas basé sur l'action qui entre les utilisateurs qui effectuent l'événement personnalisé "shopify_checkouts_abandon".][5]

Grâce à la prise en charge des objets imbriqués pour les propriétés d'événement personnalisé, les clients peuvent déclencher des campagnes et des Canvases à l'aide d'une propriété d'événement imbriquée. L'exemple suivant montre comment déclencher une campagne en utilisant un produit spécifique de l’événement personnalisé '`shopify_created_order`. Assurez-vous d'utiliser `list_items[0].product_id` pour indexer votre liste d'articles et accéder à l'ID du produit.

![Campagne basée sur l'action qui envoie aux utilisateurs qui effectuent l'événement personnalisé "shopify_created_order" où la propriété imbriquée "product_id" est égale à un nombre spécifique.][26]

[5]: {% image_buster /assets/img/Shopify/shopify_integration11.png %}
[12]: {% image_buster /assets/img/Shopify/shopify_segmentation2.png %}
[13]: {% image_buster /assets/img/Shopify/shopify_segmentation3.png %}
[14]: {% image_buster /assets/img/Shopify/shopify_segmentation4.png %}
[26]: {% image_buster /assets/img/Shopify/shopify_integration17.png %}
