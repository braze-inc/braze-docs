---
nav_title: Shopify
article_title: "Shopify"
description: "Cet article présente le partenariat entre Braze et Shopify, une société de commerce international, qui vous permet de connecter de manière transparente votre boutique Shopify à Braze pour faire passer certains webhooks Shopify dans Braze. Exploitez les stratégies multicanal de Braze et Canvas pour inciter les clients à compléter leurs achats, ou pour recibler les utilisateurs en fonction de leurs achats précédents."
page_type: partner
search_tag: Partenaire

---

# Shopify

> [Shopify](https://www.shopify.com/) est une société leader dans le commerce mondial ; elle fournit des outils fiables pour démarrer, développer, commercialiser et gérer une entreprise de vente en détail, quelle que soit sa taille. Shopify améliore le commerce pour tous les utilisateurs avec une plateforme et des services conçus pour assurer la fiabilité tout en offrant une meilleure expérience d’achat pour les consommateurs où qu’ils soient. 

L’intégration de Shopify et de Braze permet aux marques de connecter leur boutique Shopify de manière transparente pour transmettre certains webhooks Shopify dans Braze. Exploitez les stratégies multicanales de Braze et de Canvas pour recibler vos utilisateurs avec des messages sur les paniers abandonnés afin d’inciter les clients à terminer leur achat ou de recibler les utilisateurs en fonction de leurs achats précédents. 

<!--
For some Canvas and Campaign examples, check out our guide here. 
-->

## Conditions préalables

Tous les clients de Braze souhaitant utiliser l’intégration Shopify doivent signer le formulaire de commande Shopify de Braze. Contactez votre responsable de compte pour plus de détails.

Cette intégration crée des profils d’utilisateurs alias si nous ne sommes pas en mesure de faire correspondre les données Shopify avec l’e-mail ou le numéro de téléphone ([voir ici pour plus de détails sur le rapprochement des utilisateurs Shopify](#shopify-user-syncing)). Consultez vos équipes de développement au sujet des impacts en aval et de la nécessité de fusionner ces profils d’utilisateurs dans le cadre de votre cycle de vie des utilisateurs avant d’activer l’intégration. 

| Configuration requise | Description |
| ----------- | ----------- |
| Boutique Shopify | Vous devez avoir une boutique [Shopify](https://www.shopify.com) active.<br>
<br>
Notez que, pour le moment, vous ne pouvez connecter qu’une boutique Shopify par groupe d’applications. |
| Segmentation de propriété d’événement activée | Pour vous assurer que vous pouvez segmenter les propriétés de vos événements Shopify, vous devez travailler avec votre gestionnaire du succès des clients ou avec [l’assistance de Braze]({{site.baseurl}}/braze_support/) pour confirmer que la segmentation des propriétés d’événements est activée pour votre tableau de bord. |
| Prise en charge des attributs personnalisés imbriqués | Celle-ci sera activée avec l’intégration à Spotify.<br>
<br>
Vous aurez accès à cette fonctionnalité pour recevoir les attributs personnalisés d’abonnement au marketing Shopify. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration

Grâce à l’intégration clé en main de Shopify dans Braze, vous pouvez :
- Connecter sans soucis votre boutique Shopify à Braze
- Autoriser Braze à accepter et traiter les données des utilisateurs de Shopify
- Synchroniser les profils d’utilisateur de Shopify dans Braze

### Étape 1 : Localiser Shopify dans le tableau de bord
Dans Braze, accédez à **Technology Partners** puis recherchez **Shopify**. Sur la page partenaire Shopify, sélectionnez **Begin Setup** (Commencer la configuration) pour démarrer le processus d’intégration.

![Section Importation de données et installation du SDK Web de la page partenaire Shopify dans Braze.][2]{: style="max-width:80%;"}

### Étape 2 : Configurer Shopify
Cette étape prévoit l’interaction avec l’assistant de configuration de Braze. Dans ce flux, vous devez saisir votre **Nom de boutique Shopify**, passer en revue les **Événements de Webhook Shopify** (l’ingestion commence une fois l’intégration connectée), et visiter le marketplace Shopify pour télécharger l’application Shopify non répertoriée de Braze. Sélectionnez **Install Unlisted App** (Installer une application non répertoriée) pour accéder au Tableau de bord de Braze.

#### Configuration de Shopify dans Braze
<br>
![Flux de travail de configuration de Shopify dans Braze ; saisi du nom de la boutique et accès à Shopify pour installer l’application Braze.][3]{: style="max-width:80%;"}

#### Installer l’application Shopify de Braze
<br>
![Page d’installation de l’application Shopify, qui répertorie les autorisations dont disposera l’application Braze après son installation.][7]{: style="max-width:60%;"}

### Étape 3 : Vérifier la fin du processus
C’est tout ! L’état de votre intégration apparaît dans la section **Data Import** (Importation de données) de la page partenaire de Shopify. Une fois l’application Braze installée avec succès et la création du webhook terminée, vous en serez informé par e-mail. En outre, l’état **Connection Pending** (Connexion en attente) sera mis à jour vers **Connected** (Connecté) et affichera l’horodatage du moment où la connexion a été établie.

![Section Data Import (Importation de données) affichant la connexion en attente et l’état de configuration en attente.][8]{: style="max-width:80%;"}
![][4]{: style="max-width:80%;border:0;margin-bottom:5px;"}
![Section Data Import (Importation de données) affichant la connexion en attente et l’état réussi de la configuration.][9]{: style="max-width:80%;"}
![][4]{: style="max-width:80%;border:0;margin-bottom:5px;"}
![Section Data Import (Importation de données) affichant la connexion réussie. Un horodatage s’affiche lorsque la connexion a été établie et qu’il y a un lien vers la boutique connectée.][10]{: style="max-width:80%;"}

## Traitement des données Shopify

Une fois l’installation de l’application terminée, Braze crée automatiquement votre intégration de webhook avec Shopify. Consultez le tableau suivant pour plus de détails sur la façon dont les événements webhooks de Shopify pris en charge sont mappés aux événements et attributs personnalisés de Braze.

### Événements Shopify pris en charge

{% tabs local %}
{% tab Shopify Events %}
| Nom de l’événement | Type d’événement Braze | Déclenché lorsque... |
| --- | --- | --- |
| `shopify_abandoned_checkout` | [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Le paiement dans Shopify met à jour un déclencheur de webhook lorsqu’un client ajoute ou retire des articles de son panier ET poursuit dans le processus de paiement, notamment en ajoutant ses informations personnelles.<br>
<br>
Braze écoute les webhooks entrants de mise à jour du paiement dans Shopify et déclenche l’événement personnalisé `shopify_abandoned_checkout` lorsque ce paiement est considéré comme abandonné. L’abandon est fixé par défaut à **1 heure** mais est configurable dans la section **Advanced Settings** (Paramètres avancés) de la page partenaire Shopify. |
| `shopify_created_order` | [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Les événements de création de commande sont déclenchés :<br>
<br>
Automatiquement après qu’un client a effectué un achat dans votre magasin Shopify.<br>
**OU**<br>
Manuellement via la section [Orders](https://help.shopify.com/en/manual/orders/create-orders) (Commandes) de votre compte Shopify.|
| Achat | [Événement d’achat Braze]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/) | L’événement créé par Shopify déclenche également un événement d’achat dans Braze.<br>
<br>
_Remarque : le champ `product_id` de Braze comprend l’ID du produit Shopify._ |
| `shopify_paid_order` | [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Les événements de commande payée se déclencheront lorsque le statut de paiement d’une commande passe à « payé ». Une commande est en état payé après qu’un paiement par carte de crédit a été capturé, ou lorsqu’une commande utilisant un mode de paiement manuel est marquée comme payée. |
| `shopify_partially_fulfilled_order` | [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Les événements de commande partiellement exécutée seront déclenchés lorsque certaines lignes d’une commande sont exécutées avec succès. |
| `shopify_fulfilled_order` | [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Les événements de commande partiellement exécutée seront déclenchés lorsque l’exécution de toutes les lignes d’une commande est complétée. |
| `shopify_cancelled_order` | [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Les événements de commande annulée seront déclenchés lorsqu’un client crée une commande mais annule ensuite la commande avant son exécution. |
| `shopify_created_refund` | [Événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Les événements de remboursement créés sont déclenchés lorsqu’un client reçoit un remboursement, partiel ou total, pour sa commande. <br>
<br>
En outre, un remboursement peut également être déclenché lorsqu’un administrateur de compte Shopify traite manuellement le remboursement dans Shopify. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Example Payload %}
{% subtabs local %}
{% subtab Checkout Abandoned Event %}
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
{% subtab Order Created Event %}
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
{% subtab Purchase Event %}
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
{% subtab Order Paid Event %}
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
{% subtab Order Partially Fulfilled Event %}
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
{% subtab Order Fulfilled Event %}
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
{% subtab Order Cancelled Event %}
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
{% subtab Refund Created Event %}
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

## Synchronisation des utilisateurs Shopify

Braze mappe les données Shopify prises en charge avec les profils utilisateur en utilisant l’adresse e-mail ou le numéro de téléphone du client. 

**Profils d’utilisateurs identifiés**<br>

- Si l’adresse e-mail ou le numéro de téléphone est associé à un [profil utilisateur identifié]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#identified-user-profiles), Braze synchronise les données Shopify à cet utilisateur.
- Si l’adresse e-mail ou le numéro de téléphone est associé à plusieurs profils d’utilisateurs identifiés, Braze synchronise les données Shopify à celui ayant l’activité la plus récente.

**Utilisateurs anonymes**<br>

- Si l’adresse e-mail ou le numéro de téléphone est associé à un profil utilisateur anonyme existant ou à un profil d’alias uniquement, nous synchronisons les données Shopify à cet utilisateur. 
  - Pour les profils existants uniquement alias, nous ajouterons l’objet Shopify alias pour cet utilisateur.
- Si l’adresse électronique ou le numéro de téléphone n’est **pas** associé à un profil d’utilisateur dans Braze, Braze génère un utilisateur alias uniquement avec un objet alias Shopify. 
  - Si ces utilisateurs uniquement alias finissent par être identifiés, les clients Braze doivent attribuer un ID externe au profil uniquement alias en appelant l’[endpoint Users Identify]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) (Identification de l’utilisateur). 

## Utilisation des données Shopify dans Braze
Une fois votre intégration terminée, consultez notre prochain [article]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/use_cases/) sur Shopify pour apprendre comment utiliser les données Shopify dans Braze pour la personnalisation et la segmentation dans vos campagnes et vos Canvas.

## Paramètres avancés de Shopify

### Mettre à jour le délai de paiement abandonné

Par défaut, Braze règle automatiquement le délai de déclenchement de l’événement `shopify_abandoned_checkout` à une heure d’inactivité. Vous pouvez définir le champ **Abandoned Checkout** (Délai de paiement abandonné) de 5 minutes à 24 heures en sélectionnant le menu déroulant puis en sélectionnant **Set Delay** (Définir le délai) sur la page partenaire Shopify.

![Option dans les paramètres avancés permettant de définir une règle concernant le délai après lequel déclencher l’événement après l’abandon d’un paiement.][11]{: style="max-width:40%;"}

### Définir l’identifiant de produit préféré

Si vous avez inclus des événements d’achat Braze dans votre configuration d’intégration à Shopify, Braze définit par défaut l’ID du produit Shopify comme l’ID du produit utilisé dans l’événement d’achat Braze. Cette information sera ensuite utilisée lorsque vous filtrez les produits achetés en Y jours, ou lorsque vous personnalisez le contenu de votre message à l’aide de Liquid.

Vous pouvez également choisir de définir l’Unité de gestion des stocks ou le titre du produit à partir de Shopify au lieu de l’ID du produit Shopify via les paramètres avancés.

![Option dans les paramètres avancés pour spécifier un champ à utiliser comme identifiant de produit dans l’événement d’achat Braze.][12]{: style="max-width:40%;"}

## Résolution des problèmes

{% details Why is my Shopify app install still pending? %}
Votre installation peut être en attente pour l’une des raisons suivantes : 
  - Lorsque Braze configure vos webhooks Shopify
  - Lorsque Braze communique avec Shopify

Si l’installation de votre application reste en attente pendant 1 heure, Braze arrête l’installation et vous serez invité à réessayer l’opération.<br>
<br>

![Shopify]({% image_buster /assets/img/Shopify/shopify_integration8.png %}){: style="max-width:80%;"}
{% enddetails %}

{% details Why did my Shopify app install fail? %}
Votre installation a échoué pour l’une des raisons suivantes : 
  - Braze n’a pas pu joindre Shopify
  - Échec de traitement de la demande par Braze 
  - Votre jeton d’accès à Shopify n’est pas valide 
  - L’application Braze Shopify a été supprimée de votre page d’administration Shopify

Si cela se produit, vous pourrez sélectionner **Retry Setup** (Réessayer l’installation) et recommencer le processus d’installation.<br>
<br>

![Shopify]({% image_buster /assets/img/Shopify/shopify_integration16.png %}){: style="max-width:80%;"}
{% enddetails %}

{% details How do I uninstall the Braze application from my Shopify store? %}
Vous devrez aller sur votre page d’administration Shopify située sous **Apps** (Applications). Vous verrez alors une option pour supprimer l’application Braze<br>
<br>

![Shopify]({% image_buster /assets/img/Shopify/shopify_integration12.png %}){: style="max-width:80%;"}
{% enddetails %}

## RGPD

En ce qui concerne les données à caractère personnel soumises aux services de Braze par ou au nom de ses clients, Braze est le sous-traitant de données, et nos clients sont les responsables du traitement. Par conséquent, Braze traite ces données personnelles uniquement sur instruction de ses clients et, le cas échéant, notifie à ses clients les demandes des personnes concernées. En tant que responsables du traitement, nos clients répondent directement aux demandes des personnes concernées. Dans le cadre de l’intégration Shopify à la plateforme Braze, Braze reçoit automatiquement les [webhooks RGPD de Shopify](https://shopify.dev/tutorials/add-gdpr-webhooks-to-your-app). Cependant, les clients de Braze sont en fin de compte responsables de répondre aux demandes des personnes concernées de leurs clients Shopify par le biais de l’utilisation des [SDK Braze]({{site.baseurl}}/developer_guide/home/) ou des [API REST]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) conformément à nos politiques de [conformité au RGPD]({{site.baseurl}}/help/dp-technical-assistance/).

[2]: {% image_buster /assets/img/Shopify/shopify_integration2.png %} 
[3]: {% image_buster /assets/img/Shopify/shopify_integration3-6.gif %}
[4]: {% image_buster /assets/img/Shopify/arrow.jpeg %}
[7]: {% image_buster /assets/img/Shopify/shopify_integration7.png %} 
[8]: {% image_buster /assets/img/Shopify/shopify_integration8.png %} 
[9]: {% image_buster /assets/img/Shopify/shopify_integration9.png %} 
[10]: {% image_buster /assets/img/Shopify/shopify_integration10.png %} 
[11]: {% image_buster /assets/img/Shopify/shopify_advanced_settings_abandoned_checkout_delay.png %} 
[12]: {% image_buster /assets/img/Shopify/shopify_advanced_settings_product_identifier.png %} 
