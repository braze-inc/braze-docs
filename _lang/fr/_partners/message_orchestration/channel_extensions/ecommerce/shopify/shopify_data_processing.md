---
nav_title: Traitement des données
article_title: "Traitement des données Shopify"
description: "Cet article de référence présente la manière dont sont traitées les données de Shopify, notamment les événements pris en charge, la synchronisation des utilisateurs, les paramètres avancés, etc."
page_type: partner
search_tag: Partenaire
alias: "/shopify_processing/"
page_order: 3
---

# Traitement des données

> Une fois l’installation de l’application terminée, Braze crée automatiquement votre intégration de webhook et ScriptTag avec Shopify. Consultez le tableau suivant pour plus de détails sur la façon dont les événements de Shopify pris en charge sont mappés aux événements et attributs personnalisés de Braze.

## Événements Shopify pris en charge

{% tabs local %}
{% tab Shopify Events %}
| Nom de l’événement | Type d’événement Braze | Déclenché lorsque… | Source de l’événement |
| --- | --- | --- | --- |
| `shopify_product_viewed` | [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)| Les vues de produits se déclencheront une fois que les produits seront complètement visibles pour le client sur la boutique Shopify. | Intégration ScriptTag |
| `shopify_product_clicked` | [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Les clics de produit se déclencheront dès que le client clique sur la page d’informations du produit. | Intégration ScriptTag |
| `shopify_abandoned_cart` | [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Dès qu’un client ajoute des articles à son panier, Braze stocke l’ID du jeton de panier. <br><br>Le délai de panier abandonné par défaut est réglé sur 1 heure. Si après une heure, le panier abandonné n’a pas été mis à jour, Braze déclenchera l’événement. Vous pouvez mettre à jour votre délai de panier abandonné dans **Paramètres avancés**. | Intégration ScriptTag |
| `shopify_abandoned_checkout` | [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Tout paiement met à jour un déclencheur de webhook lorsqu’un client ajoute ou retire des articles de son panier ET progresse dans le processus de paiement, notamment en ajoutant ses informations personnelles.<br><br>Braze écoute les webhooks entrants de mise à jour du paiement dans Shopify et déclenche l’événement personnalisé `shopify_abandoned_checkout` lorsque ce paiement est considéré comme abandonné. Le délai de paiement abandonné est fixé par défaut sur 1 heure, mais il est configurable dans la section **Advanced Settings** (Paramètres avancés) de la page partenaire Shopify. | Webhooks Shopify |
| `shopify_created_order` | [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Les événements de création de commande sont déclenchés :<br><br>Automatiquement après qu’un client a effectué un achat dans votre boutique Shopify.<br>**OU**<br>Manuellement via la section [Orders (Commandes)](https://help.shopify.com/en/manual/orders/create-orders) de votre compte Shopify.| Webhooks Shopify |
| Achat | [Événement d’achat Braze]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/) | L’événement créé par Shopify déclenche un événement d’achat dans Braze. | Webhooks Shopify |
| `shopify_paid_order` | [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Les événements de commande payée se déclencheront lorsque le statut de paiement d’une commande passe à « payé ». Une commande est en état payé après qu’un paiement par carte de crédit a été enregistré, ou lorsqu’une commande utilisant un mode de paiement manuel est marquée comme payée. | Webhooks Shopify |
| `shopify_partially_fulfilled_order` | [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Les événements de commande partiellement exécutée seront déclenchés lorsque certaines lignes d’une commande sont exécutées avec succès. | Webhooks Shopify |
| `shopify_fulfilled_order` | [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Les événements de commande partiellement exécutée seront déclenchés lorsque l’exécution de toutes les lignes d’une commande est complétée. | Webhooks Shopify |
| `shopify_cancelled_order` | [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Les événements de commande annulée seront déclenchés lorsqu’un client crée une commande mais annule ensuite la commande avant son exécution. | Webhooks Shopify |
| `shopify_created_refund` | [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Les événements de remboursement créés sont déclenchés lorsqu’un client reçoit un remboursement, partiel ou total, pour sa commande.<br><br> Un remboursement peut également être déclenché lorsqu’un administrateur de compte Shopify traite manuellement le remboursement dans Shopify. | Webhooks Shopify |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

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

### Attributs personnalisés Shopify pris en charge
{% tabs local %}
{% tab Shopify Custom Attributes %}
| Nom de l’attribut | Description |
| --- | --- |
| `shopify_accepts_marketing` | Cet attribut personnalisé correspond à l’état d’abonnement au marketing par e-mail qui est capturé sur la page de paiement.<br><br>Ce champ est désormais obsolète pour les nouveaux clients Shopify en faveur de notre fonctionnalité d’[états d’abonnement et de groupe]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify#step-5-collect-email-or-sms-subscribers). |
| `shopify_sms_consent` | Cet attribut personnalisé correspond à l’état d’abonnement au marketing par SMS qui est capturé sur la page de paiement.<br><br>Ce champ est désormais obsolète pour les nouveaux clients Shopify en faveur de notre fonctionnalité d’[états d’abonnement et de groupe]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify#step-5-collect-email-or-sms-subscribers). |
| `shopify_tags`  | Cet attribut correspond aux [balises client](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/using-tags#tag-types) définies par les administrateurs Shopify. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Example Payload %}
{% subtabs local %}
{% subtab Shopify SMS Consent %}
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
{% subtab Shopify Accepts Marketing (Email) %}
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
{% subtab Shopify Tags %}
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

### Attributs standard de Shopify pris en charge

- E-mail
- Prénom
- Nom
- Téléphone
- Ville
- Pays

{% alert note %}
Braze met à jour uniquement les attributs personnalisés Shopify et les attributs standard Braze s’il y a une différence dans les données du profil utilisateur existant. Par exemple, si les données entrantes de Shopify contiennent un prénom Bob et que Bob existe déjà comme prénom dans le profil utilisateur de Braze, Braze ne déclenchera pas de mise à jour, et le point de données ne vous sera pas facturé.
{% endalert %}

## Paramètres avancés de Shopify

#### Mise à jour du délai d'abandon du panier et de la caisse

Par défaut, Braze règle automatiquement le délai de déclenchement de `shopify_abandoned_checkout` et de l’événement `shopify_abandoned_cart` à une heure d’inactivité. Vous pouvez définir le champ Abandoned Delay (Délai d’abandon) pour chaque événement de 5 minutes à 24 heures en sélectionnant le menu déroulant puis en sélectionnant Set Delay (Définir le délai) sur la page partenaire Shopify.

![Option dans les paramètres avancés pour définir le délai d'abandon de panier et de paiement.][10]{: style="max-width:40%;"}

#### Définir l’identifiant de produit préféré

Si vous avez inclus des événements d’achat Braze dans votre configuration d’intégration à Shopify, Braze définit par défaut l’ID du produit Shopify comme `product_id` utilisé dans l’événement d’achat Braze. Cette information sera utilisée lorsque vous filtrez les produits achetés en Y jours, ou lorsque vous personnalisez le contenu de vos envois de messages à l’aide de Liquid.

Vous pouvez également choisir de définir l’Unité de gestion des stocks ou le titre du produit à partir de Shopify au lieu de l’ID du produit Shopify via les paramètres avancés.

![Option dans les paramètres avancés pour spécifier un champ à utiliser comme identifiant de produit dans l’événement d’achat Braze.][12]{: style="max-width:40%;"}

## Synchronisation des utilisateurs Shopify

Braze mettra à jour les profils utilisateurs existants ou en créera de nouveaux pour les prospects, les inscriptions et les enregistrements de comptes collectés dans votre boutique Shopify. Les données du profil utilisateur peuvent être collectées à partir des méthodes suivantes dans Shopify, mais ne sont pas limitées à celles-ci :

- Le client crée un compte
- L'e-mail ou le téléphone du client est collecté dans un formulaire pop-up Shopify
- L'e-mail du client est collecté dans votre boutique à partir du pied de page de Shopify
- L'e-mail ou le numéro de téléphone du client sont recueillis par un outil tiers connecté à Shopify

Braze tentera premièrement de mapper les données Shopify prises en charge avec tous les profils utilisateur existants en utilisant l’adresse e-mail ou le numéro de téléphone du client.

**Utilisateurs anonymes**<br>
- Si l’adresse e-mail ou le numéro de téléphone est associé à un profil utilisateur anonyme existant ou à un profil d’alias uniquement, nous synchronisons les données Shopify à cet utilisateur. 
  - Pour les profils existants de type alias uniquement, nous ajouterons l’objet Shopify alias pour cet utilisateur.
- Si l’e-mail ou le numéro de téléphone n’est **pas** associé à un profil d’utilisateur dans Braze, Braze génère un utilisateur alias uniquement avec un objet alias Shopify. 
  - Si ces utilisateurs uniquement alias finissent par être identifiés, les clients Braze doivent attribuer un ID externe au profil uniquement alias en appelant l’[endpoint Identification de l’utilisateur]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/). 

**Utilisateurs identifiés**<br>
- Au fur et à mesure que les clients progressent dans la procédure de paiement, Braze vérifie si l’e-mail, le numéro de téléphone ou l’identifiant client Shopify correspond à un [profil utilisateur identifié]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#identified-user-profiles). En cas de correspondance, Braze synchronisera les données utilisateur Shopify à ce profil. 
- Si l’adresse e-mail ou le numéro de téléphone est associé à plusieurs profils d’utilisateurs identifiés, Braze synchronise les données Shopify à celui ayant l’activité la plus récente.  

Si Braze ne trouve pas de correspondance pour l'e-mail ou le numéro de téléphone, nous créerons un nouveau profil d'utilisateur avec les données Shopify prises en charge.

{% alert important %}
Certaines des données utilisateur et certains des événements collectés par l'intégration Shopify seront comptabilisés dans l'utilisation de vos points de données. Consultez notre [politique en matière de points de données]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/) pour plus d'informations.
{% endalert %}

### Les SDK Web et webhooks Shopify

<br>**Utilisateurs anonymes**
1. Avec l’intégration SDK Web, vous commencerez à suivre les sessions de vos clients Shopify. Si les visiteurs de votre magasin sont des clients anonymes, Braze enregistre le `device_id` pour la session du client.
2. Au fur et à mesure que le client progresse dans la procédure de paiement et fournit des informations d’identification supplémentaires, l’e-mail ou le numéro de téléphone par exemple, Braze enregistre les données utilisateur Shopify pertinentes à l’aide des webhooks Shopify.
3. Au cours de ce processus, Braze fera bien correspondre l'utilisateur avec le même `device_id` pour la même session, et fusionnera toutes les données utilisateur enregistrées à partir du Web SDK et des webhooks Shopify en un seul profil utilisateur dans Braze.<br>Braze attribuera également l’ID client Shopify comme [alias d’utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-aliases) sur le profil utilisateur :

```json
{
  "user_alias" :
    { 
      "alias_name" : "4306250531001", 
      "alias_label" : "shopify_customer_id" }
}
```

**Utilisateurs identifiés**<br>
- Au fur et à mesure que les clients progressent dans la procédure de paiement, Braze vérifie si l’e-mail, le numéro de téléphone ou l’identifiant client Shopify correspond à un [profil utilisateur identifié]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#identified-user-profiles). En cas de correspondance, Braze synchronisera les données utilisateur Shopify à ce profil en utilisant notre [fonctionnalité de fusion](#user-profile-merging). 
- Si l’adresse e-mail ou le numéro de téléphone est associé à plusieurs profils d’utilisateurs identifiés, Braze synchronise les données Shopify à celui ayant l’activité la plus récente.  

### Fusion du profil utilisateur

Braze fusionnera les champs suivants de l'utilisateur anonyme créé à partir de notre intégration Shopify avec l'utilisateur identifié lorsque nous trouverons une correspondance sur l'un de ces identifiants, ID client Shopify, e-mail ou numéro de téléphone. Notez que cette fonctionnalité de fusion des données utilisateur est uniquement disponible dans l'intégration Shopify.
- Prénom
- Nom
- E-mail
- Sexe
- Date de naissance
- Numéro de téléphone
- Fuseau horaire
- Ville d’origine
- Pays
- Langue
- Attributs personnalisés
- Données sur les événements d’achats et personnalisés (sauf propriétés de l’événement, compte, horodatages correspondant à la première et dernière dates)
- Propriétés de l’événement d’achat et personnalisées pour la segmentation « X fois en Y jours » (où X <= 50 et Y <= 30)
- Jetons de notification push
- Historique des messages

L’un des champs suivants a été trouvé sur l’utilisateur anonyme ou l’utilisateur identifié :
- Nombre d’événements d’achats et personnalisés, ainsi que les horodatages correspondant à la première et dernière dates
  - Ces champs fusionnés mettront à jour les filtres « pour X événements en Y jours ». Pour les événements d’achat, ces filtres incluent « nombre d’achats en Y jours » et « argent dépensé au cours des Y derniers jours ».

{% alert warning%}
Les données de session ne sont pas encore prises en charge dans le cadre de notre processus de fusion.
{% endalert %}

## RGPD

En ce qui concerne les données à caractère personnel soumises aux services de Braze par ou au nom de ses clients, Braze est le sous-traitant de données, et nos clients sont les responsables du traitement. Par conséquent, Braze traite ces données personnelles uniquement sur instruction de ses clients et, le cas échéant, notifie à ses clients les demandes des personnes concernées. En tant que responsables du traitement, nos clients répondent directement aux demandes des personnes concernées. Dans le cadre de l’intégration Shopify à la plateforme Braze, Braze reçoit automatiquement les [webhooks RGPD de Shopify](https://shopify.dev/tutorials/add-gdpr-webhooks-to-your-app). Cependant, les clients de Braze sont en fin de compte responsables de répondre aux demandes des personnes concernées de leurs clients Shopify par le biais de l’utilisation des [SDK Braze]({{site.baseurl}}/developer_guide/home/) ou des [API REST]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) conformément à nos politiques de [conformité au RGPD]({{site.baseurl}}/help/dp-technical-assistance/).



[10]: {% image_buster /assets/img/Shopify/checkout_cart_delay.png %}
[12]: {% image_buster /assets/img/Shopify/shopify_advanced_settings_product_identifier.png %} 