---
nav_title: Fonctionnalités des données de Shopify
article_title: "Fonctionnalités des données de Shopify"
description: "Cet article de référence couvre les fonctionnalités des données de Shopify."
page_type: partner
search_tag: Partner
alias: /shopify_data_features/
page_order: 3
---

# Fonctionnalités des données de Shopify

> Cet article donne un aperçu de nos fonctionnalités Shopify, notamment les données Shopify suivies et des exemples de payloads, de backfill historique et de synchronisation des produits.

## Suivi des événements Shopify

{% tabs %}
{% tab Exemple de charge utile %}
{% subtabs global %}
{% subtab Product viewed %}
```json
{
    "name": "ecommerce.product_viewed",
    "properties": {
        "product_id": "12345",
        "product_name": "product",
        "variant_id": "123",
        "image_url": "www.image-url.com",
        "product_url": "mystorefront.myshopify.com/product",
        "price": 10,
        "currency": "USD",
        "source": "mystorefront.myshopify.com",
        "metadata": {
          "sku": "sku"
        },
        "type": [
          "price_drop",
          "back_in_stock"
        ]
    }
}
```
{% endsubtab %}
{% subtab Cart updated %}
```json
{
    "name": "ecommerce.cart_updated",
    "properties": {
        "cart_id": "Z2NwLXVzLWVhc3QxOjAxSjk3UFg4RlFZMjVTVkRHRlc1RlI3SlRY",
        "currency": "USD",
        "total_value": 2000000,
        "products": [
            {
                "product_id": "8266836345064",
                "product_name": "PANTS!!!",
                "variant_id": "44610569208040",
                "image_url": "https://cdn.shopify.com/s/files/1/0604/4211/6328/files/1200px-Trousers-colourisolated.jpg?v=1689256168",
                "product_url": "https://test-store.myshopify.com/products/pants?variant=44610569208040",
                "quantity": 2,
                "price": 1000000,
                "metadata": {
                    "sku": "007"
                }
            }
        ],
        "source": "https://test-store.myshopify.com",
        "metadata": {}
    }
}
```
{% endsubtab %}
{% subtab Checkout started %}
```json
{
    "name": "ecommerce.checkout_started",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "cart_id": "eeafa272cebfd4b22385bc4b645e762c",
        "total_value": 421.88,
        "currency": "USD",
        "products": [
            {
                "product_id": "632910392",
                "product_name": "IPod Nano - 8GB",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199,
                "metadata": {
                    "sku": "IPOD2008PINK"
                }
            }
        ],
        "source": "braze-mock-storefront.myshopify.com",
        "checkout_id": "123123123",
        "metadata": {
            "checkout_url": "https://checkout.local/548380009/checkouts/123123123/recover?key=example-secret-token"
        }
    }
}
```
{% endsubtab %}
{% subtab Order placed %}
{% raw %}
```json
{
    "name": "ecommerce.order_placed",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "order_id": "820982911946154508",
        "cart_id": "eeafa272cebfd4b22385bc4b645e762c",
        "total_value": 421.88,
        "currency": "USD",
        "total_discounts": 5,
        "discounts": [],
        "products": [
            {
                "product_id": "632910392",
                "product_name": "IPod Nano - 8GB",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199,
                "metadata": {
                    "sku": "IPOD2008PINK"
                }
            }
        ],
        "source": "braze-mock-storefront.myshopify.com",
        "metadata": {
            "order_status_url": "https://apple.myshopify.com/690933842/orders/123456abcd/authenticate?key=abcdefg",
            "order_number": 1234,
            "tags": [
                "heavy",
                "heavy2"
            ],
            "referring_site": "https://www.google.com",
            "payment_gateway_names": [
                "visa",
                "bogus"
            ]
        }
    }
}
```
{% endraw %}
{% endsubtab %}
{% subtab Fulfilled order %}
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
{% subtab Partially fulfilled order %}
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
{% subtab Paid order %}
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
{% subtab Order cancelled %}
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
{% subtab Order refunded %}
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
{% subtab Account login %}
```json
{
	name: "shopify_account_login",
	properties: {
	source: "braze-mock-storefront.myshopify.com"
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Événements Shopify %}
{% subtabs global %}
{% subtab Product viewed %}
**Événement**: `ecommerce.v1.product_viewed`<br>
**Type** : Événement recommandé<br>
**Déclenché**: Lorsqu'un client consulte une page produit<br>
**Cas d'utilisation**: Abandon de navigation

{% raw %}
| Variable | Liquid templating |
| --- | --- |
\|------------------|-----------------------------------------------------|
| `product_id` | `{{event_properties.${product_id}}}` |
| `product_name ` | `{{event_properties.${product_name}}}` |
| `variant_id` | `{{event_properties.${variant_id}}}` |
| `image_url ` | `{{event_properties.${image_url}}}` |
| `product_url` | `<your-store.myshopify.com>{{event_properties.${product_url}}}` <br><br>Ajoutez le domaine de votre site Shopify avant l'URL. |
| `price` | `{{event_properties.${price}}}` |
| `currency` | `{{event_properties.${currency}}}` |
| `source` | `{{event_properties.${source}}}` |
| `sku` | `{{event_properties.${metadata}[0].sku}}` |
| `type` | `event_properties.${type}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Cart updated %}
**Événement**: `ecommerce.v1.cart_updated`<br>
**Type** : Événement recommandé<br>
**Déclenché**: Lorsqu'un client ajoute, supprime ou met à jour son panier d'achat<br>
**Cas d'utilisation**: Abandon de panier

Pour les toiles de panier abandonné, vous devez d'abord ajouter l'étiquette Liquid du panier d'achat initial pour obtenir le contexte du panier d'achat dans votre message. 

{% raw %}
```liquid
{% shopping_cart {{context.${cart_id}}} %}
```
{% endraw %}

Vous pouvez ensuite ajouter les étiquettes Liquid pour panier d'achat suivantes dans votre message.

{% raw %}
| Variable | Liquid templating |
\|------------------|-----------------------------------------------------|
| `cart_id` | `{{ shopping_cart.cart_id }}` |
| `currency` | `{{ shopping_cart.currency }}` |
| `total_value` | `{{ shopping_cart.total_value }}` |
| `product_id` | `{{ shopping_cart.products[0].product_id }}` |
| `product_name` | `{{ shopping_cart.products[0].product_name }}` |
| `variant_id` | `{{ shopping_cart.products[0].variant_id }}` |
| `image_url` | `{{ shopping_cart.products[0].image_url }}` |
| `product_url` | `{{ shopping_cart.products[0].product_url }}` |
| `quantity` | `{{ shopping_cart.products[0].quantity }}` |
| `price` | `{{ shopping_cart.products[0].price }}` |
| `sku` | `{{ shopping_cart.products[0].metadata[0].sku }}` |
| `source` | `{{ shopping_cart.source }}` |
| `metadata (value)` | `{{ shopping_cart.metadata[0].<add_value_here> }}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% alert tip %}
Pour plus d'informations sur la façon de créer une boucle Liquid `for` pour ajouter dynamiquement tous les produits dans votre e-mail, reportez-vous à la section [Personnalisation des produits du panier abandonné pour les e-mails.]({{site.baseurl}}/ecommerce_use_cases/#abandoned-cart)
{% endalert %}

{% endsubtab %}
{% subtab Checkout started %}
**Événement**: `ecommerce.v1.checkout_started`<br>
**Type** : Événement recommandé<br>
**Déclenché**: Lorsqu'un client ajoute, supprime ou met à jour son panier d'achat<br>
**Cas d'utilisation**: Abandon du paiement

Pour les toiles Abandoned Checkout, vous devez d'abord utiliser l'étiquette Liquid suivante :

{% raw %}
```liquid
{% shopping_cart {{context.${cart_id}}} :abort_if_not_abandoned false %}
{{context.${cart_id}}}
```
{% endraw %}

Vous pouvez ensuite ajouter les étiquettes Liquid suivantes dans votre message pour référencer les produits de votre panier au moment du paiement.

{% raw %}
| Variable | Liquid templating |
\|------------------|-----------------------------------------------------|
| `cart_id` | `{{ shopping_cart.cart_id }}` |
| `currency` | `{{ shopping_cart.currency }}` |
| `total_value` | `{{ shopping_cart.total_value }}` |
| `product_id` | `{{ shopping_cart.products[0].product_id }}` |
| `product_name` | `{{ shopping_cart.products[0].product_name }}` |
| `variant_id` | `{{ shopping_cart.products[0].variant_id }}` |
| `image_url` | `{{ shopping_cart.products[0].image_url }}` |
| `product_url` | `{{ shopping_cart.products[0].product_url }}` |
| `quantity` | `{{ shopping_cart.products[0].quantity }}` |
| `price` | `{{ shopping_cart.products[0].price }}` |
| `sku` | `{{ shopping_cart.products[0].metadata.sku }}` |
| `source` | `{{ shopping_cart.source }}` |
| `checkout_url` | `{{ shopping_cart.metadata[0].checkout_url }}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Order placed %}
**Événement**: `ecommerce.v1.order_placed`<br>
**Type** : Événement recommandé<br>
**Déclenché**: Lorsqu'un utilisateur termine avec succès la procédure de paiement et passe une commande<br>
**Cas d'utilisation**: Confirmation de commande, reciblage après achat, ventes incitatives ou croisées. 

{% raw %}
| Variable | Liquid templating |
\|-------------------------|-----------------------------------------------------|
| cart_id | `{{event_properties.${cart_id}}}` |
| devise | `{{event_properties.${currency}}}` |
| réductions | `{{event_properties.${discounts}}}` |
| order_id | `{{event_properties.${order_id}}}` |
| product_id | `{{event_properties.${products}[0].product_id}}` |
| nom_du_produit | `{{event_properties.${products}[0].product_name}}` |
| variant_id | `{{event_properties.${products}[0].variant_id}}` |
| quantité | `{{event_properties.${products}[0].quantity}}` |
| unité de gestion des stocks | `{{event_properties.${products}[0].metadata.sku}}` |
| total_discounts | `{{event_properties.${total_discounts}}}` |
| order_status_url | `{{event_properties.${metadata}.order_status_url}}` |
| numéro_de_commande | `{{event_properties.${metadata}.order_number}}` |
| tags | `{{event_properties.${metadata}.tags}}` |
| site_de_référence | `{{event_properties.${metadata}.referring_site}}` |
| nom_de_la_passerelle_de_paiement | `{{event_properties.${metadata}.payment_gateway_names}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% alert tip %}
Le webhook checkout completed de Shopify ne contient pas d'URL de produits ou d'images. Par conséquent, vous devez utiliser la personnalisation du liquide des catalogues comme indiqué dans la [personnalisation des produits du panier abandonné pour les e-mails.]({{site.baseurl}}/ecommerce_use_cases/#order-confirmation-and-feedback-survey)
{% endalert %}

{% endsubtab %}
{% subtab Fulfilled order %}
**Événement**: `shopify_fulfilled_order`<br>
**Type** : [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events)<br>
**Déclenché**: Lorsque la commande d'un utilisateur est exécutée et prête à être expédiée<br>
**Cas d'utilisation**: (transactionnel) Mise à jour de l'exécution 

{% raw %}
| Variable | Liquid templating |
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
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Partially fulfilled order %}
**Événement**: `shopify_partially_fulfilled_order`<br>
**Type** : [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events)<br>
**Déclenché**: Lorsqu'une partie de la commande d'un utilisateur est remplie et prête à être expédiée<br> 
**Cas d'utilisation**: (transactionnel) Mise à jour de l'exécution 

{% raw %}
| Variable | Liquid templating |
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
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Paid order %}
**Événement**: `shopify_paid_order`<br>
**Type** : [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events)<br>
**Déclenché**: Lorsque la commande d'un utilisateur est marquée comme payée dans Shopify<br>  
**Cas d'utilisation**: (Transactionnel) Confirmation de paiement

{% raw %}
| Variable | Liquid templating |
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
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Order cancelled %}
**Événement**: `shopify_cancelled_order`<br>
**Type** : [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events)<br>
**Déclenché**: Lorsque la commande d'un utilisateur est annulée<br> 
**Cas d'utilisation**: (Transactionnel) Confirmation d'annulation de commande

{% raw %}
| Variable | Liquid templating |
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
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}
{% endsubtab %}
{% subtab Order refunded %}
**Événement**: `shopify_order_refunded`<br>
**Type** : [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events)<br>
**Déclenché**: Lorsque la commande d'un utilisateur est remboursée<br>
**Cas d'utilisation**: (Transactionnel) Confirmation de remboursement

{% raw %}
| Variable | Liquid templating |
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
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Account login %}

**Événement**: `shopify_account_login`<br>
**Type** : [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events)<br>
**Déclenché**: Lorsqu'un utilisateur se connecte à son compte<br>
**Cas d'utilisation**: Série de bienvenue

{% raw %}
| Variable | Liquid templating |
| --- | --- |
| `source` | {{event_properties.${source}}} |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% alert note %}
L'intégration de Shopify ne prend actuellement pas en charge le remplissage de l' [événement d'achat de]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events#purchase-events) Braze. Par conséquent, les filtres d'achat, les étiquettes Liquid, les déclencheurs basés sur l'action et les analyses doivent utiliser l'événement order_placed de ecommerce..
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Attributs personnalisés Shopify pris en charge
{% tabs local %}
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
{% tab Attributs personnalisés Shopify %}
| Nom de l'attribut | Description |
| --- | --- |
| `shopify_total_spent` | Le montant total d'argent que le client a dépensé au cours de son historique de commandes. |
| `shopify_order_count` | Le nombre de commandes associées à ce client. Les commandes test et archivées ne sont pas prises en compte.
| `shopify_last_order_id` | L'ID de la dernière commande du client. |
| `shopify_last_order_name` | Le nom de la dernière commande du client. Ceci est directement lié au champ `name` sur la ressource de la commande. |
| `shopify_zipcode` | Le code postal du client de son adresse par défaut. |
| `shopify_province` | La province du client à partir de son adresse par défaut. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Personnalisation Liquid

Pour ajouter une personnalisation Liquid pour vos attributs personnalisés Shopify, sélectionnez **\+ Personnalisation**. Sélectionnez ensuite **Attributs personnalisés** comme type de personnalisation.

![La section "Ajouter une personnalisation" avec la liste déroulante "Attribut" étendue.]({% image_buster /assets/img/Shopify/add_personalization_2.png %}){: style="max-width:40%;"}

Après avoir sélectionné votre attribut personnalisé, saisissez une valeur par défaut et copiez l'extrait de code Liquid dans votre message.

![Coller un extrait de code Liquid dans un message.]({% image_buster /assets/img/Shopify/copy_liquid_snippet.png %})
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

## Collecte de données SDK 

Pour plus d'informations sur les données collectées par les SDK de [Braze]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/), consultez la rubrique [Collecte de données des SDK]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/). 

## Remblai historique

Lors de l'onboarding de votre boutique Shopify, vous pouvez lancer une synchronisation initiale des données par le biais d'un backfill historique afin d'engager immédiatement le dialogue avec vos clients. Dans le cadre de ce backfill, Braze effectuera une synchronisation initiale des données de tous les clients et de toutes les commandes passées au cours des 90 derniers jours précédant votre connexion à l'intégration Shopify. 

### Mise en place de l'historique de Shopify

1. Activez le remplissage historique dans l'étape **Suivi des données Shopify**.

![L'étape "Suivre les données de Shopify" de l'intégration de Shopify montrant l'historique des remblais sélectionnés.]({% image_buster /assets/img/Shopify/historical_data_backfill_sync.png %}).

{: start="2"}

2. Une fois que vous avez terminé la configuration de votre intégration, Braze commence la synchronisation initiale des données. Vous pouvez suivre la progression dans l'onglet **Données Shopify** de vos paramètres d'intégration. 

![La page des paramètres d'intégration de Shopify avec un curseur indiquant que les événements sont activement synchronisés.]({% image_buster /assets/img/Shopify/historical_data_backfill_syncing.png %})

### Données synchronisées 

Pour la synchronisation initiale des données, Braze importera les clients et les commandes passées au cours des 90 derniers jours précédant votre connexion à l'intégration Shopify. Lorsque Braze importe vos clients Shopify, il leur attribue le type `external_id` que vous avez choisi dans vos paramètres de configuration.