---
nav_title: Données Shopify dans Braze
article_title: "Données Shopify dans Braze"
description: "Cet article explique comment utiliser les données Shopify dans Braze pour la personnalisation et la segmentation."
page_type: partner
search_tag: Partenaire
permalink: "/shopify_data/"
hidden: true

---

# Données Shopify dans Braze

## Webhooks Shopify

Braze propose une solution clé en main pour prend en charge les paiements abandonnés, les achats, et les campagnes avec cycle de vie post-achat via les [webhooks Shopify](https://shopify.dev/api/admin-rest/2022-04/resources/webhook#top). En fonction des événements que vous sélectionnez pendant votre processus d’onboarding, Braze déterminera les rubriques d’événements Shopify auxquelles vous pouvez vous abonner. Dès que vous aurez réussi à intégrer votre boutique Shopify, Braze recevra instantanément votre activité client Shopify.

### Événements Shopify pris en charge

{% tabs local %}
{% tab Shopify Events %}
| Nom de l’événement | Type d’événement Braze | Déclenché lorsque... |
| --- | --- | --- |
| `shopify_product_viewed` | [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)| Les vues de produits se déclencheront une fois que les produits seront complètement visibles pour le client sur la boutique Shopify. |
| `shopify_product_clicked` | [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Les clics de produit se déclencheront dès que le client clique sur la page d’informations du produit. |
| `shopify_abandoned_cart` | [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Dès qu’un client ajoute des articles à son panier, Braze stocke l’ID du jeton de panier. <br><br>Le délai de panier abandonné par défaut est réglé sur 1 heure. Si après une heure, le panier abandonné n’a pas été mis à jour, Braze déclenchera l’événement. Vous pouvez mettre à jour votre délai de panier abandonné dans **Paramètres avancés**. | 
| `shopify_abandoned_checkout` | [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Tout paiement met à jour un déclencheur de webhook lorsqu’un client ajoute ou retire des articles de son panier ET progresse dans le processus de paiement, notamment en ajoutant ses informations personnelles.<br><br>Braze écoute les webhooks entrants de mise à jour du paiement dans Shopify et déclenche l’événement personnalisé `shopify_abandoned_checkout` lorsque ce paiement est considéré comme abandonné. Le délai de paiement abandonné est fixé par défaut sur 1 heure, mais il est configurable dans la section **Advanced Settings** (Paramètres avancés) de la page partenaire Shopify. |
| `shopify_created_order` | [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Les événements de création de commande sont déclenchés :<br><br>Automatiquement après qu’un client a effectué un achat dans votre boutique Shopify.<br>**OU**<br>Manuellement via la section [Orders](https://help.shopify.com/en/manual/orders/create-orders) (Commandes) de votre compte Shopify.|
| Achat | [Événement d’achat Braze]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/) | L’événement créé par Shopify déclenche un événement d’achat dans Braze. |
| `shopify_paid_order` | [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Les événements de commande payée se déclencheront lorsque le statut de paiement d’une commande passe à « payé ». Une commande est en état payé après qu’un paiement par carte de crédit a été enregistré, ou lorsqu’une commande utilisant un mode de paiement manuel est marquée comme payée. |
| `shopify_partially_fulfilled_order` | [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Les événements de commande partiellement exécutée seront déclenchés lorsque certaines lignes d’une commande sont exécutées avec succès. |
| `shopify_fulfilled_order` | [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Les événements de commande partiellement exécutée seront déclenchés lorsque l’exécution de toutes les lignes d’une commande est complétée. |
| `shopify_cancelled_order` | [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Les événements de commande annulée seront déclenchés lorsqu’un client crée une commande mais annule ensuite la commande avant son exécution. |
| `shopify_created_refund` | [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Les événements de remboursement créés sont déclenchés lorsqu’un client reçoit un remboursement, partiel ou total, pour sa commande.<br><br> Un remboursement peut également être déclenché lorsqu’un administrateur de compte Shopify traite manuellement le remboursement dans Shopify. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Example Payload %}
{% subtabs local %}
{% subtab Viewed Product %}
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
{% subtab Clicked Product %}
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
    "name" => "shopify_abandoned_cart",
    "time" => "2021-10-01T21:12:15.773Z",
    "properties" => {
      "cart_id"=>"eeafa272cebfd4b22385bc4b645e762c",
      "line_items" => [
        {
          "product_id" => 788032119674292922,
          "quantity" => 3,
          "sku" => "example-shirt-s",
          "title" => "Example T-Shirt - ",
          "vendor" => "Acme",
          "properties" => {},
          "price" => "19.99",
        },
      ],
    }
}
```
{% endsubtab %}
{% subtab Checkout Abandoned %}
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
        "product_id": 632910392,
        "quantity": 1,
        "sku": "IPOD2008PINK",
        "title": "IPodNano-8GB",
        "vendor": "Apple",
        "properties": "nil",
        "price": "199.00"
      }
    ],
    "abandoned_checkout_url": "https://checkout.local/690933842/checkouts/123123123/recover?key=example-secret-token",
    "checkout_id": "123123123"
  }
}
```
{% endsubtab %}
{% subtab Order Created %}
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
        "vendor": "nil",
        "name": "IPodNano-8GB",
        "properties": [],
        "price": "199.00"
      },
      {
        "product_id": 632910392,
        "quantity": 1,
        "sku": "IPOD2008PINK",
        "title": "IPodNano-8GB",
        "vendor": "nil",
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
    "title": "IPodNano-8GB",
    "variant_title": "nil",
    "vendor": "nil",
    "properties": []
  }
}
```
{% endsubtab %}
{% subtab Order Paid %}
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
    "cancelled_at": null,
    "tags": "",
    "closed_at": null,
    "fulfillment_status": null,
    "fulfillments": []
  },
  "braze_id": "123abc123abc"
}
```
{% endsubtab %}
{% subtab Order Partially Fulfilled %}
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
{% subtab Order Fulfilled %}
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
{% subtab Order Cancelled %}
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
{% subtab Refund Created %}
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
        "vendor": "partners-demo",
        "properties": [],
        "price": "80.00"
      },
      {
        "quantity": 1,
        "product_id": 6143032852671,
        "sku": null,
        "title": "Chequered Red Shirt",
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

### Attributs personnalisés Shopify pris en charge
{% tabs local %}
{% tab Shopify Custom Attributes %}
| Nom de l’attribut | Description |
| --- | --- |
| `shopify_accepts_marketing` | Cet attribut personnalisé correspond à l’état d’abonnement au marketing par e-mail qui est capturé sur la page de paiement. |
| `shopify_sms_consent` | Cet attribut personnalisé correspond à l’état d’abonnement au marketing par SMS qui est capturé sur la page de paiement. |
| `shopify_tags`  | Cet attribut correspond aux [balises client](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/using-tags#tag-types) définies par les administrateurs Shopify. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Example Payload %}
{% subtabs local %}
{% subtab SMS Consent %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "shopify_sms_consent": {
        "state": "subscribed",
        "opt_in_level": "single_opt_in",
        "collected_from": "other"
      }
    }
  ]
}
```
{% endsubtab %}
{% subtab Accepts Marketing (Email) %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "shopify_accepts_marketing": true
    }
  ]
}
```
{% endsubtab %}
{% subtab Tags %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "shopify_tags": "VIP_customer"
    }
  ]
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### Attributs standard de Shopify pris en charge

- E-mail
- Prénom
- Nom
- Téléphone
- Ville
- Pays

{% alert note %}
Braze met à jour uniquement les attributs personnalisés Shopify et les attributs standard Braze s’il y a une différence dans les données du profil utilisateur existant. Par exemple, si les données entrantes de Shopify contiennent un prénom Bob et que Bob existe déjà comme prénom dans le profil utilisateur de Braze, Braze ne déclenchera pas de mise à jour, et le point de données ne sera pas facturé au client.
{% endalert %}

## Rapprochement des utilisateurs

#### Les SDK Web et webhooks Shopify

##### Utilisateurs anonymes
1. Avec l’intégration SDK Web, vous commencerez à suivre les sessions de vos clients Shopify. Si les visiteurs de votre magasin sont des clients anonymes, Braze enregistre le `device_id` pour la session du client.<br><br>
2. Au fur et à mesure que le client progresse dans la procédure de paiement et fournit des informations d’identification supplémentaires, l’e-mail ou le numéro de téléphone par exemple, Braze enregistre les données utilisateur Shopify pertinentes à l’aide des webhooks Shopify.<br><br>
3. Au cours de ce processus, Braze fera bien correspondre l'utilisateur avec le même `device_id` pour la même session, et fusionnera toutes les données utilisateur enregistrées à partir du Web SDK et des webhooks Shopify en un seul profil utilisateur dans Braze.<br><br>Braze attribuera également l’ID client Shopify comme [alias d’utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-aliases) sur le profil utilisateur.

##### Utilisateurs identifiés

- Au fur et à mesure que les clients progressent dans la procédure de paiement, Braze vérifie si l’e-mail, le numéro de téléphone ou l’identifiant client Shopify correspond à un [profil utilisateur identifié]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#identified-user-profiles). En cas de correspondance, Braze synchronisera les données utilisateur Shopify à ce profil. 
- Si l’adresse e-mail ou le numéro de téléphone est associé à plusieurs profils d’utilisateurs identifiés, Braze synchronise les données Shopify à celui ayant l’activité la plus récente.

#### Webhooks Shopify uniquement
Braze mappe les données Shopify prises en charge avec les profils utilisateur en utilisant l’adresse e-mail ou le numéro de téléphone du client. 

##### Profils d’utilisateurs identifiés

- Si l’adresse e-mail ou le numéro de téléphone est associé à un [profil utilisateur identifié]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#identified-user-profiles), Braze synchronise les données Shopify à cet utilisateur.
- Si l’adresse e-mail ou le numéro de téléphone est associé à plusieurs profils d’utilisateurs identifiés, Braze synchronise les données Shopify à celui ayant l’activité la plus récente.

##### Utilisateurs anonymes

- Si l’adresse e-mail ou le numéro de téléphone est associé à un profil utilisateur anonyme existant ou à un profil d’alias uniquement, nous synchronisons les données Shopify à cet utilisateur.
  - Pour les profils existants de type alias uniquement, nous ajouterons l’objet Shopify alias pour cet utilisateur. 
- Si l’adresse e-mail ou le numéro de téléphone n’est pas associé à un profil d’utilisateur dans Braze, Braze génère un utilisateur alias uniquement avec un objet alias Shopify.
  - Si ces utilisateurs uniquement alias finissent par être identifiés, les clients Braze doivent attribuer un ID externe au profil uniquement alias en appelant [l’endpoint d’identification des utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/). 

## Personnalisation

Grâce à la prise en charge des objets imbriqués pour les événements personnalisés, les clients de Braze Shopify peuvent utiliser les variables de modèle Liquid des propriétés de l’événement imbriqué. Les tableaux suivants répertorient les variables du modèle Liquid pour chaque événement.

{% tabs %}
{% tab Product Viewed %}
**Event**: `shopify_product_viewed`<br>
**Type**: [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Modèle Liquid |
| --- | --- |
| Unité de gestion des stocks de l’article | `{{event_properties.${id}}}` |
| Titre de l'élément  | `{{event_properties.${title}}}` |
| Prix de l’article | `{{event_properties.${price}}}` |
| Fournisseur de l’article | `{{event_properties.${vendor}}}` |
| Images de l’article | `{{event_properties.${images}}}` |

{% endraw %}
{% endtab %}

{% tab Product Clicked %}
**Event**: `shopify_product_clicked`<br>
**Type**: [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Modèle Liquid |
| --- | --- |
| Unité de gestion des stocks de l’article | `{{event_properties.${id}}}` |
| Titre de l'élément  | `{{event_properties.${title}}}` |
| Prix de l’article | `{{event_properties.${price}}}` |
| Fournisseur de l’article | `{{event_properties.${vendor}}}` |
| Images de l’article | `{{event_properties.${images}}}` |
{% endraw %}
{% endtab %}

{% tab Abandon Cart %}
**Event**: `shopify_abandoned_cart`<br>
**Type**: [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Modèle Liquid |
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
**Event**: `shopify_abandoned_checkout`<br>
**Type**: [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Modèle Liquid |
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

**Event**: `shopify_created_order`<br>
**Type**: [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Modèle Liquid |
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

**Event**: Achat<br>
**Type**: [Événement d’achat Braze]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/)

{% raw %}
| Variable | Modèle Liquid |
| --- | --- |
| Unité de gestion des stocks de l’article | `{{event_properties.${line_items}[0].sku}}` |
| Titre de l'élément  | `{{event_properties.${line_items}[0].title}}` |
| Fournisseur de l’article | `{{event_properties.${line_items}[0].vendor}}` |
| Propriétés de l’élément | `{{event_properties.${line_items}[0].properties}}` |
{% endraw %}

{% endtab %}
{% tab Order Paid %}
**Event**: `shopify_paid_order`<br>
**Type**: [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Modèle Liquid |
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
**Event**: `shopify_partially_fulfilled_order`<br>
**Type**: [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Modèle Liquid |
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
**Event**: `shopify_fulfilled_order`<br>
**Type**: [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Modèle Liquid |
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
**Event**: `shopify_cancelled_order`<br>
**Type**: [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Modèle Liquid |
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
**Event**: `shopify_created_refund`<br>
**Type**: [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Modèle Liquid |
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

![Page de détails du segment pour un segment Shopify_Test avec le filtre pour l’événement personnalisé « abandon_paiement_shopify » mis en évidence.][22]{: style="max-width:80%;"}

En outre, vous pouvez également utiliser le filtre d’étendue des achats de Braze pour créer des segments d’utilisateurs basés sur :
- Premier/dernier achat
- Premier/dernier achat pour une application spécifique
- Produits déjà achetés au cours des 30 derniers jours
- Nombre d’achats qu’ils ont effectués

![Filtre de segmentation pour les utilisateurs ayant effectué leur premier achat après le 17 octobre 2020.][23]

![Recherche d’un ID du produit spécifique comme filtre de segmentation.][24]

{% alert note %}
Si vous cherchez à segmenter par propriétés d’événement personnalisées, assurez-vous de travailler avec votre gestionnaire du succès des clients ou [l’assistance]({{site.baseurl}}/braze_support/) Braze pour activer le filtrage de toutes les propriétés d’événement pertinentes que vous souhaitez utiliser dans la segmentation et Liquid.
{% endalert %} 

## Déclenchement de campagne et de Canvas 

Avec les événements personnalisés Shopify dans Braze, vous pouvez déclencher des Canvas ou des campagnes comme vous le feriez normalement avec n’importe quel autre [événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-storage). Par exemple, vous pouvez créer un Canvas par événement qui se déclenche suite à un événement `shopify_checkouts_abandon` Shopify au sein des critères d’entrée du Canvas. 

![Canvas par événement qui saisit les utilisateurs qui effectuent l’événement personnalisé « abandon_paiement_shopify ».][22]

Avec la prise en charge des objets imbriqués pour les propriétés d’événement personnalisées, les clients peuvent désormais déclencher des campagnes et des Canvas à l’aide d’une propriété de l’événement imbriqué. Voici un exemple de déclenchement d’une campagne utilisant un produit spécifique de l’événement personnalisé `shopify_created_order`.

![Campagne par événement qui envoie aux utilisateurs qui effectuent l’événement personnalisé « commande_créée_shopify » où la propriété imbriquée « product_id » est égale à un nombre spécifique.][26]

## Paramètres avancés de Shopify

#### Mettre à jour le délai de panier abandonné
Par défaut, Braze règle automatiquement le délai de déclenchement de l’événement `shopify_abandoned_cart` à une heure d’inactivité. Vous pouvez définir le champ **Abandoned Cart Delay** (Délai de panier abandonné) de 5 minutes à 24 heures en sélectionnant le menu déroulant puis en sélectionnant **Set Delay** (Définir le délai) sur la page partenaire Shopify.

![Option dans les paramètres avancés permettant de définir une règle concernant le délai après lequel déclencher l’événement après l’abandon d’un panier.][13]{: style="max-width:40%;"}

#### Mettre à jour le délai de paiement abandonné

Par défaut, Braze règle automatiquement le délai de déclenchement de l’événement `shopify_abandoned_checkout` à une heure d’inactivité. Vous pouvez définir le champ **Abandoned Checkout** (Délai de paiement abandonné) de 5 minutes à 24 heures en sélectionnant le menu déroulant puis en sélectionnant **Set Delay** (Définir le délai) sur la page partenaire Shopify.

![Option dans les paramètres avancés permettant de définir une règle concernant le délai après lequel déclencher l’événement après l’abandon d’un paiement.][11]{: style="max-width:40%;"}

#### Définir l’identifiant de produit préféré

Si vous avez inclus des événements d’achat Braze dans votre configuration d’intégration à Shopify, Braze définit par défaut l’ID du produit Shopify comme l’ID du produit utilisé dans l’événement d’achat Braze. Cette information sera ensuite utilisée lorsque vous filtrez les produits achetés en Y jours, ou lorsque vous personnalisez le contenu de votre message à l’aide de Liquid.

Vous pouvez également choisir de définir l’Unité de gestion des stocks ou le titre du produit à partir de Shopify au lieu de l’ID du produit Shopify via les paramètres avancés.

![Option dans les paramètres avancés pour spécifier un champ à utiliser comme identifiant de produit dans l’événement d’achat Braze.][12]{: style="max-width:40%;"}

## RGPD

En ce qui concerne les données à caractère personnel soumises aux services de Braze par ou au nom de ses clients, Braze est le sous-traitant de données, et nos clients sont les responsables du traitement. Par conséquent, Braze traite ces données personnelles uniquement sur instruction de ses clients et, le cas échéant, notifie à ses clients les demandes des personnes concernées. En tant que responsables du traitement, nos clients répondent directement aux demandes des personnes concernées. Dans le cadre de l’intégration Shopify à la plateforme Braze, Braze reçoit automatiquement les [webhooks RGPD de Shopify](https://shopify.dev/tutorials/add-gdpr-webhooks-to-your-app). Cependant, les clients de Braze sont en fin de compte responsables de répondre aux demandes des personnes concernées de leurs clients Shopify par le biais de l’utilisation des [SDK Braze]({{site.baseurl}}/developer_guide/home/) ou des [API REST]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) conformément à nos politiques de [conformité au RGPD]({{site.baseurl}}/help/dp-technical-assistance/).

[11]: {% image_buster /assets/img/Shopify/shopify_advanced_settings_abandoned_checkout_delay.png %} 
[12]: {% image_buster /assets/img/Shopify/shopify_advanced_settings_product_identifier.png %} 
[13]: {% image_buster /assets/img/Shopify/abandoned_cart_delay.png %} 


[22]: {% image_buster /assets/img/Shopify/shopify_integration11.png %}  
[22]: {% image_buster /assets/img/Shopify/shopify_segmentation2.png %} 
[23]: {% image_buster /assets/img/Shopify/shopify_segmentation3.png %} 
[24]: {% image_buster /assets/img/Shopify/shopify_segmentation4.png %}   
[26]: {% image_buster /assets/img/Shopify/shopify_integration17.png %}
