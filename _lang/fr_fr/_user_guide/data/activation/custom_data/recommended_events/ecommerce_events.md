---
nav_title: Événements recommandés pour le commerce électronique
article_title: Événements recommandés pour le commerce électronique
page_type: reference
alias: /ecommerce_events/
toc_headers: h2
description: "Cet article de référence décrit les événements et propriétés recommandés pour le commerce électronique, leur utilisation, la segmentation, l'endroit où consulter les analyses pertinentes, et plus encore."
---

# Événements recommandés pour le commerce électronique

> Cette page présente les événements et propriétés recommandés pour le commerce électronique. Ces événements sont conçus pour capturer les comportements d'achat clés dont les marketeurs ont besoin pour déclencher des messages efficaces, comme le ciblage des paniers abandonnés.

{% alert important %}
Les événements recommandés pour le commerce électronique sont actuellement en accès anticipé. Contactez votre Customer Success Manager Braze si vous souhaitez participer à cet accès anticipé. <br><br>Si vous utilisez le nouveau [connecteur Shopify]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector), ces événements recommandés seront automatiquement disponibles via l'intégration.
{% endalert %}

Braze sait que la planification des données prend du temps. Nous encourageons nos clients à familiariser leurs équipes de développement avec ces événements et à commencer à les envoyer dès maintenant. Bien que certaines fonctionnalités ne soient pas immédiatement disponibles avec les événements recommandés pour le commerce électronique, de nouveaux produits seront introduits tout au long de l'année 2025 pour enrichir vos capacités e-commerce.

## Types d'événements recommandés pour le commerce électronique

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

Toute devise autre que l'USD sera affichée dans Braze en USD, sur la base du taux de change en vigueur à la date de déclaration. Pour éviter toute conversion monétaire, définissez la devise en USD en dur.

{% tabs %}
{% tab ecommerce.product_viewed %}

Vous pouvez utiliser l'événement « produit consulté » pour déclencher une action lorsqu'un client consulte la page détaillée d'un produit.

#### Propriétés

| Nom de la propriété | Requis | Type de données | Description | 
|---|---|---|---|
| `product_id` | Oui | Chaîne de caractères | Identifiant unique du produit consulté. <br> Pour les clients non-Shopify, il s'agit de la valeur que vous définissez pour les ID d'articles du catalogue, comme les unités de gestion des stocks. |
| `product_name` | Oui | Chaîne de caractères | Le nom du produit consulté. | 
| `variant_id` | Oui | Chaîne de caractères | Identifiant unique de la variante du produit. Par exemple : `shirt_medium_blue` |
| `image_url` | Non | Chaîne de caractères | URL de l'image du produit. |
| `product_url` | Non | Chaîne de caractères | URL vers la page du produit pour plus de détails. |
| `price` | Oui | Float | Le prix unitaire de la variante du produit au moment de la consultation. |
| `currency` | Oui | Chaîne de caractères | La devise dans laquelle le prix du produit est indiqué (par exemple « USD » ou « EUR ») au [format ISO 4217](https://www.iso.org/iso-4217-currency-codes.html). |
| `source` | Oui | Chaîne de caractères | Source d'où provient l'événement (pour Shopify, il s'agit de storefront). |
| `metadata` | Non | Objet | |
| `type` | Non | Objet | Fonctionne avec les [notifications de réapprovisionnement]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications) et les [notifications de baisse de prix]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications). |
| `sku` | Non | Chaîne de caractères | (Shopify uniquement) Unité de gestion des stocks Shopify. Ce champ peut être configuré comme le champ ID du catalogue. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Exemples d'objets

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.product_viewed", {
    "product_id": "4111176",
    "product_name": "Torchie runners",
    "variant_id": "4111176700",
    "image_url": "https://braze-apparel.com/images/products/large/torchie-runners.jpg",
    "product_url": "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/",
    "price": 85,
    "currency": "GBP",
    "source": "https://braze-apparel.com/",
    "metadata": {
        "sku": "",
        "color": "ORANGE",
        "size": "6",
        "brand": "Braze"
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
BrazeProperties properties = new BrazeProperties()
    .addProperty("product_id", "4111176")
    .addProperty("product_name", "Torchie runners")
    .addProperty("variant_id", "4111176700")
    .addProperty("image_url", "https://braze-apparel.com/images/products/large/torchie-runners.jpg")
    .addProperty("product_url", "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/")
    .addProperty("price", 85)
    .addProperty("currency", "GBP")
    .addProperty("source", "https://braze-apparel.com/")
    .addProperty("metadata", new JSONObject()
        .put("sku", "")
        .put("color", "ORANGE")
        .put("size", "6")
        .put("brand", "Braze"));

Braze.getInstance(context).logCustomEvent("ecommerce.product_viewed", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let properties: [String: Any] = [
    "product_id": "4111176",
    "product_name": "Torchie runners",
    "variant_id": "4111176700",
    "image_url": "https://braze-apparel.com/images/products/large/torchie-runners.jpg",
    "product_url": "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/",
    "price": 85,
    "currency": "GBP",
    "source": "https://braze-apparel.com/",
    "metadata": [
        "sku": "",
        "color": "ORANGE",
        "size": "6",
        "brand": "Braze"
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.product_viewed", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.product_viewed",
      "time": "2024-01-15T09:03:45Z",
      "properties": {
        "product_id": "4111176",
        "product_name": "Torchie runners",
        "variant_id": "4111176700",
        "image_url": "https://braze-apparel.com/images/products/large/torchie-runners.jpg",
        "product_url": "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/",
        "price": 85,
        "currency": "GBP",
        "source": "https://braze-apparel.com/",
        "metadata": {
          "sku": "",
          "color": "ORANGE",
          "size": "6",
          "brand": "Braze"
        },
        "type": [
          "price_drop",
          "back_in_stock"
        ]
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.cart_updated %}

Vous pouvez utiliser le déclencheur **Perform Cart Updated Event** pour suivre l'ajout, la suppression ou la mise à jour de produits dans le panier. Cet événement vérifie les informations suivantes avant de se déclencher :

- L'heure de l'événement est postérieure à l'heure `updated_at` du panier spécifique de l'utilisateur.
- Le panier n'est pas passé à l'étape de paiement.
- Le tableau `products` n'est pas vide.

#### Objet de mappage des paniers

L'événement `ecommerce.cart_updated` possède un objet de mappage des paniers. Cet objet est créé sur le profil utilisateur et contient un mappage des paniers, lesquels regroupent tous les produits du panier de l'acheteur. Vous pouvez accéder aux produits du panier via l'étiquette Liquid suivante : 

{%raw%}
```liquid
{% shopping_cart {{context_properties.${cart_id}}} %}
{% for item in shopping_cart.products %}
{% catalog_items <add_your_catalog> {{item.variant_id}} %}
```
{%endraw%}

Si un panier n'a pas été mis à jour et n'a pas abouti à un événement de commande passée dans les 10 jours, le panier et les produits associés seront supprimés.

{% alert note %}
Le nombre de produits par panier n'est pas limité sur Braze. Cependant, la limite de Shopify est de 500.
{% endalert %}

#### Comportement du panier lors de la fusion de profils utilisateurs

S'il y a deux paniers, les deux sont ajoutés à l'utilisateur fusionné. Le Canvas est remis en file d'attente, qu'il s'agisse du même panier ou d'un panier différent, afin d'envoyer un message contenant les informations les plus récentes. L'événement `ecommerce.cart_updated` contiendra l'ID du dernier panier et les derniers produits du panier.

#### Propriétés

| Nom de la propriété | Requis | Type de données | Description | 
|---|---|---|---|
| `cart_id` | Oui | Chaîne de caractères | Si vous n'utilisez pas de plateforme tierce fournissant un `cart_id`, vous pouvez utiliser l'[ID de session Braze]({{site.baseurl}}/developer_guide/analytics/tracking_sessions). |
| `total_value` | Oui | Float | Valeur monétaire totale du panier. | 
| `currency` | Oui | Chaîne de caractères | La devise dans laquelle le prix du produit est indiqué (par exemple « USD » ou « EUR ») au [format ISO 4217](https://www.iso.org/iso-4217-currency-codes.html). |
| `products` | Oui | Tableau |  |
| `product_id` | Oui | Chaîne de caractères | Identifiant unique du produit consulté. <br> Cette valeur peut être l'ID du produit ou l'unité de gestion des stocks. |
| `product_name` | Oui | Chaîne de caractères | Le nom du produit consulté. |
| `variant_id` | Oui | Chaîne de caractères | Identifiant unique de la variante du produit. Par exemple : `shirt_medium_blue` |
| `image_url` | Non | Chaîne de caractères | URL de l'image du produit. |
| `product_url` | Non | Chaîne de caractères | URL vers la page du produit pour plus de détails. |
| `quantity` | Oui | Entier | Nombre d'unités du produit dans le panier. |
| `price` | Oui | Float | Le prix unitaire de la variante du produit au moment de la consultation. |
| `metadata` | Non | Objet | Champ de métadonnées supplémentaires sur le produit que le client souhaite ajouter pour ses cas d'utilisation. Pour Shopify, nous ajouterons l'unité de gestion des stocks. <br> Ce champ est soumis à la limite générale de 50 ko pour les propriétés d'événement. |
| `sku` | Non | Chaîne de caractères | (Shopify uniquement) Unité de gestion des stocks Shopify. Ce champ peut être configuré comme le champ ID du catalogue. |
| `source` | Oui | Chaîne de caractères | Source d'où provient l'événement (pour Shopify, il s'agit de storefront). |
| `metadata` | Non | Objet | Champ de métadonnées supplémentaires sur le produit que le client souhaite ajouter pour ses cas d'utilisation. Pour Shopify, nous ajouterons l'unité de gestion des stocks. <br> Ce champ est soumis à la limite générale de 50 ko pour les propriétés d'événement. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Exemples d'objets

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.cart_updated", {
    "cart_id": "cart_12345",
    "currency": "USD",
    "total_value": 199.98,
    "products": [
        {
            "product_id": "8266836345064",
            "product_name": "Classic T-Shirt",
            "variant_id": "44610569208040",
            "image_url": "https://braze-apparel.com/images/tshirt-blue-medium.jpg",
            "product_url": "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040",
            "quantity": 2,
            "price": 99.99,
            "metadata": {
                "sku": "TSH-BLU-M",
                "color": "BLUE",
                "size": "Medium",
                "brand": "Braze"
            }
        }
    ],
    "source": "https://braze-apparel.com",
    "metadata": {}
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "8266836345064")
    .put("product_name", "Classic T-Shirt")
    .put("variant_id", "44610569208040")
    .put("image_url", "https://braze-apparel.com/images/tshirt-blue-medium.jpg")
    .put("product_url", "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040")
    .put("quantity", 2)
    .put("price", 99.99)
    .put("metadata", new JSONObject()
        .put("sku", "TSH-BLU-M")
        .put("color", "BLUE")
        .put("size", "Medium")
        .put("brand", "Braze"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("cart_id", "cart_12345")
    .addProperty("currency", "USD")
    .addProperty("total_value", 199.98)
    .addProperty("products", products)
    .addProperty("source", "https://braze-apparel.com")
    .addProperty("metadata", new JSONObject());

Braze.getInstance(context).logCustomEvent("ecommerce.cart_updated", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let products: [[String: Any]] = [
    [
        "product_id": "8266836345064",
        "product_name": "Classic T-Shirt",
        "variant_id": "44610569208040",
        "image_url": "https://braze-apparel.com/images/tshirt-blue-medium.jpg",
        "product_url": "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040",
        "quantity": 2,
        "price": 99.99,
        "metadata": [
            "sku": "TSH-BLU-M",
            "color": "BLUE",
            "size": "Medium",
            "brand": "Braze"
        ]
    ]
]

let properties: [String: Any] = [
    "cart_id": "cart_12345",
    "currency": "USD",
    "total_value": 199.98,
    "products": products,
    "source": "https://braze-apparel.com",
    "metadata": [:]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.cart_updated", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.cart_updated",
      "time": "2024-01-15T09:15:30Z",
      "properties": {
        "cart_id": "cart_12345",
        "currency": "USD",
        "total_value": 199.98,
        "products": [
          {
            "product_id": "8266836345064",
            "product_name": "Classic T-Shirt",
            "variant_id": "44610569208040",
            "image_url": "https://braze-apparel.com/images/tshirt-blue-medium.jpg",
            "product_url": "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040",
            "quantity": 2,
            "price": 99.99,
            "metadata": {
              "sku": "TSH-BLU-M",
              "color": "BLUE",
              "size": "Medium",
              "brand": "Braze"
            }
          }
        ],
        "source": "https://braze-apparel.com",
        "metadata": {}
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.checkout_started %}

Vous pouvez utiliser l'événement « checkout started » pour recibler les clients qui ont commencé le processus de paiement mais n'ont pas passé de commande.

Comme pour l'événement `ecommerce.cart_updated`, cet événement vous permet d'exploiter l'étiquette Liquid du panier d'achat pour accéder à tous les produits du panier dans vos messages d'abandon de paiement :

{%raw%}
```liquid
{% shopping_cart {{context_properties.${cart_id}}} :abort_if_not_abandoned false %}
{% for item in shopping_cart.products %}
{% catalog_items <add_your_catalog> {{item.variant_id}} %}
```
{%endraw%}

#### Propriétés

| Nom de la propriété | Requis | Type de données | Description | 
|---|---|---|---|
| `checkout_id` | Oui | Chaîne de caractères | Identifiant unique du paiement. |
| `cart_id` | Non | Chaîne de caractères | Si vous n'utilisez pas de plateforme tierce fournissant un `cart_id`, vous pouvez utiliser l'[ID de session Braze]({{site.baseurl}}/developer_guide/analytics/tracking_sessions). | 
| `total_value` | Oui | Float | Valeur monétaire totale du panier. |
| `currency` | Oui | Chaîne de caractères | Devise dans laquelle le panier est évalué. |
| `products` | Oui | Tableau d'objets |  |
| `product_id` | Oui | Chaîne de caractères | Identifiant unique du produit consulté. Par exemple, cette valeur peut être l'ID du produit ou l'unité de gestion des stocks. |
| `product_name` | Oui | Chaîne de caractères | Le nom du produit consulté.  |
| `variant_id` | Oui | Chaîne de caractères | Identifiant unique de la variante du produit. Par exemple : `shirt_medium_blue` |
| `image_url` | Non | Chaîne de caractères | URL de l'image du produit. |
| `product_url` | Non | Chaîne de caractères | URL vers la page du produit pour plus de détails. |
| `quantity` | Oui | Entier | Nombre d'unités du produit dans le panier. |
| `price` | Oui | Float | Le prix unitaire de la variante du produit au moment de la consultation. |
| `metadata` | Non | Objet | Champ de métadonnées supplémentaires sur le produit que le client souhaite ajouter pour ses cas d'utilisation. Pour Shopify, nous ajouterons l'unité de gestion des stocks. <br> Ce champ est soumis à la limite générale de 50 ko pour les propriétés d'événement. |
| `sku` | Non | Chaîne de caractères | (Shopify uniquement) Unité de gestion des stocks Shopify. Ce champ peut être configuré comme le champ ID du catalogue. |
| `source` | Oui | Chaîne de caractères | Source d'où provient l'événement (pour Shopify, il s'agit de storefront). |
| `metadata` | Non | Objet |  |
| `checkout_url` | Non | Chaîne de caractères | URL de la page de paiement. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Exemples d'objets

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.checkout_started", {
    "checkout_id": "checkout_abc123",
    "cart_id": "cart_12345",
    "total_value": 199.98,
    "currency": "USD",
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "checkout_url": "https://checkout.braze-audio.com/abc123"
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "632910392")
    .put("product_name", "Wireless Headphones")
    .put("variant_id", "808950810")
    .put("quantity", 1)
    .put("price", 199.98)
    .put("metadata", new JSONObject()
        .put("sku", "WH-BLK-PRO")
        .put("color", "Black")
        .put("brand", "AudioTech"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("checkout_id", "checkout_abc123")
    .addProperty("cart_id", "cart_12345")
    .addProperty("total_value", 199.98)
    .addProperty("currency", "USD")
    .addProperty("products", products)
    .addProperty("source", "https://braze-audio.com")
    .addProperty("metadata", new JSONObject()
        .put("checkout_url", "https://checkout.braze-audio.com/abc123"));

Braze.getInstance(context).logCustomEvent("ecommerce.checkout_started", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 199.98,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "checkout_id": "checkout_abc123",
    "cart_id": "cart_12345",
    "total_value": 199.98,
    "currency": "USD",
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "checkout_url": "https://checkout.braze-audio.com/abc123"
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.checkout_started", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.checkout_started",
      "time": "2024-01-15T09:25:45Z",
      "properties": {
        "checkout_id": "checkout_abc123",
        "cart_id": "cart_12345",
        "total_value": 199.98,
        "currency": "USD",
        "products": [
          {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
              "sku": "WH-BLK-PRO",
              "color": "Black",
              "brand": "BrazeAudio"
            }
          }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
          "checkout_url": "https://checkout.braze-audio.com/abc123"
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.order_placed %}

Vous pouvez utiliser l'événement « commande passée » pour déclencher une action lorsqu'un client finalise le processus de paiement et passe une commande.

#### Propriétés

| Nom de la propriété | Requis | Type de données | Description | 
|---|---|---|---|
| `order_id` | Oui | Chaîne de caractères | Identifiant unique de la commande passée. |
| `cart_id` | Non | Chaîne de caractères | Si vous n'utilisez pas de plateforme tierce fournissant un `cart_id`, vous pouvez utiliser l'[ID de session Braze]({{site.baseurl}}/developer_guide/analytics/tracking_sessions). |
| `total_value` | Oui | Float | Valeur monétaire totale du panier. | 
| `currency` | Oui | Chaîne de caractères | Devise dans laquelle le panier est évalué. |
| `total_discounts` | Non | Float | Montant total des réductions appliquées à la commande. | 
| `discounts`| Non | Tableau d'objets | Liste détaillée des réductions appliquées à la commande. |
| `products` | Oui | Tableau d'objets |  |
| `product_id` | Oui | Chaîne de caractères | Identifiant unique du produit consulté. Cette valeur peut être l'ID du produit ou l'unité de gestion des stocks. |
| `product_name` | Oui | Chaîne de caractères | Le nom du produit consulté. |
| `variant_id` | Oui | Chaîne de caractères | Identifiant unique de la variante du produit. Par exemple : `shirt_medium_blue` |
| `image_url` | Non | Chaîne de caractères | URL de l'image du produit. |
| `product_url` | Non | Chaîne de caractères | URL vers la page du produit pour plus de détails. |
| `quantity` | Oui | Entier | Nombre d'unités du produit dans le panier. |
| `price` | Oui | Float | Le prix unitaire de la variante du produit au moment de la consultation. |
| `metadata` | Non | Objet | Champ de métadonnées supplémentaires sur le produit que le client souhaite ajouter pour ses cas d'utilisation. Pour Shopify, nous ajouterons l'unité de gestion des stocks. <br> Ce champ est soumis à la limite générale de 50 ko pour les propriétés d'événement. |
| `sku` | Non | Chaîne de caractères | (Shopify uniquement) Unité de gestion des stocks Shopify. Ce champ peut être configuré comme le champ ID du catalogue. |
| `source` | Oui | Chaîne de caractères | Source d'où provient l'événement (pour Shopify, il s'agit de storefront). |
| `order_status_url` | Non | Chaîne de caractères | URL pour consulter le statut de la commande. |
| `order_number` | Non | Chaîne de caractères | (Shopify uniquement) Numéro de commande unique pour la commande passée. |
| `tags` | Non | Tableau | (Shopify uniquement) Étiquettes de commande
| `referring_site` | Non | Chaîne de caractères | (Shopify uniquement) Le site d'où provient la commande (comme Meta). |
| `payment_gateway_names` | Non | Tableau | (Shopify uniquement) Source du système de paiement (par exemple, point de vente ou mobile). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Exemples d'objets

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.order_placed", {
    "order_id": "order_67890",
    "cart_id": "cart_12345",
    "total_value": 189.98,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": [
        {
            "code": "SAVE10",
            "amount": 10.00
        }
    ],
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["electronics", "audio"],
        "referring_site": "https://www.e-referrals.com",
        "payment_gateway_names": ["tap2pay", "dotcash"]
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray discounts = new JSONArray();
discounts.put(new JSONObject()
    .put("code", "SAVE10")
    .put("amount", 10.00));

JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "632910392")
    .put("product_name", "Wireless Headphones")
    .put("variant_id", "808950810")
    .put("quantity", 1)
    .put("price", 199.98)
    .put("metadata", new JSONObject()
        .put("sku", "WH-BLK-PRO")
        .put("color", "Black")
        .put("brand", "AudioTech"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("order_id", "order_67890")
    .addProperty("cart_id", "cart_12345")
    .addProperty("total_value", 189.98)
    .addProperty("currency", "USD")
    .addProperty("total_discounts", 10.00)
    .addProperty("discounts", discounts)
    .addProperty("products", products)
    .addProperty("source", "https://braze-audio.com")
    .addProperty("metadata", new JSONObject()
        .put("order_status_url", "https://braze-audio.com/orders/67890/status")
        .put("order_number", "ORD-2024-001234")
        .put("tags", new JSONArray().put("electronics").put("audio"))
        .put("referring_site", "https://www.e-referrals.com")
        .put("payment_gateway_names", new JSONArray().put("tap2pay").put("dotcash")));

Braze.getInstance(context).logCustomEvent("ecommerce.order_placed", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let discounts: [[String: Any]] = [
    [
        "code": "SAVE10",
        "amount": 10.00
    ]
]

let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 199.98,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "order_id": "order_67890",
    "cart_id": "cart_12345",
    "total_value": 189.98,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": discounts,
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["electronics", "audio"],
        "referring_site": "https://www.e-referrals.com",
        "payment_gateway_names": ["tap2pay", "dotcash"]
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.order_placed", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.order_placed",
      "time": "2024-01-15T09:35:20Z",
      "properties": {
        "order_id": "order_67890",
        "cart_id": "cart_12345",
        "total_value": 189.98,
        "currency": "USD",
        "total_discounts": 10.00,
        "discounts": [
          {
            "code": "SAVE10",
            "amount": 10.00
          }
        ],
        "products": [
          {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
              "sku": "WH-BLK-PRO",
              "color": "Black",
              "brand": "BrazeAudio"
            }
          }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
          "order_status_url": "https://braze-audio.com/orders/67890/status",
          "order_number": "ORD-2024-001234",
          "tags": ["electronics", "audio"],
          "referring_site": "https://www.e-referrals.com",
          "payment_gateway_names": ["tap2pay", "dotcash"]
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.order_refunded %}

Vous pouvez utiliser l'événement « commande remboursée » pour déclencher une action lorsqu'une commande est partiellement ou totalement remboursée.

#### Propriétés

| Nom de la propriété       | Requis | Type de données | Description   |
|---------------|---------|-----------|-------------------------|
| `order_id`            | Oui      | Chaîne de caractères    | Identifiant unique de la commande passée.        |
| `total_value`         | Oui      | Float     | Valeur monétaire totale du panier.    |
| `currency`            | Oui      | Chaîne de caractères    | Devise dans laquelle le panier est évalué.    |
| `total_discounts`     | Non       | Float     | Montant total des réductions appliquées à la commande.   |
| `discounts`           | Non       | Tableau d'objets     | Liste détaillée des réductions appliquées à la commande. |
| `products`            | Oui      | Tableau d'objets     |  |
| `product_id`       | Oui      | Chaîne de caractères    | Identifiant unique du produit consulté. Cette valeur peut être l'ID du produit, l'unité de gestion des stocks ou une valeur similaire. <br>Si un remboursement partiel est effectué et qu'aucun `product_id` n'est attribué au remboursement (par exemple, un remboursement au niveau de la commande), fournissez un `product_id` générique.             |
| `product_name`     | Oui      | Chaîne de caractères    | Le nom du produit consulté.                                                                      |
| `variant_id`       | Oui      | Chaîne de caractères    | Identifiant unique de la variante du produit (tel que `shirt_medium_blue`).                                         |
| `image_url`        | Non       | Chaîne de caractères    | URL de l'image du produit.     |
| `product_url`      | Non       | Chaîne de caractères    | URL vers la page du produit pour plus de détails.  |
| `quantity`         | Oui      | Entier   | Nombre d'unités du produit dans le panier.   |
| `price`            | Oui      | Float     | Le prix unitaire de la variante du produit au moment de la consultation.  |
| `metadata`         | Non       | Objet    | Champ de métadonnées supplémentaires sur le produit que le client souhaite ajouter pour ses cas d'utilisation. Pour Shopify, nous ajouterons l'unité de gestion des stocks. Ce champ est soumis à la limite générale de 50 ko pour les propriétés d'événement. |
| `sku`            | Non       | Chaîne de caractères    | (Shopify uniquement) Unité de gestion des stocks Shopify. Ce champ peut être configuré comme le champ ID du catalogue.  |
| `source`              | Oui      | Chaîne de caractères    | Source d'où provient l'événement (pour Shopify, il s'agit de storefront).    |
| `metadata`            | Non       | Objet    |                |
| `order_status_url`  | Non       | Chaîne de caractères    | URL pour consulter le statut de la commande.     |
| `order_note`       | Non       | Chaîne de caractères    | (Shopify uniquement) Note ajoutée à la commande par le commerçant.    |
| `order_number`     | Non       | Chaîne de caractères    | (Shopify uniquement) Numéro de commande unique pour la commande passée.   |
| `tags`             | Non       | Tableau     | (Shopify uniquement) Étiquettes de la commande.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Exemples d'objets

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.order_refunded", {
    "order_id": "order_67890",
    "total_value": 99.99,
    "currency": "USD",
    "total_discounts": 5.00,
    "discounts": [
        {
            "code": "SAVE5",
            "amount": 5.00
        }
    ],
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 99.99,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_note": "Customer requested refund due to defective item",
        "order_number": "ORD-2024-001234",
        "tags": ["refund", "defective"]
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray discounts = new JSONArray();
discounts.put(new JSONObject()
    .put("code", "SAVE5")
    .put("amount", 5.00));

JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "632910392")
    .put("product_name", "Wireless Headphones")
    .put("variant_id", "808950810")
    .put("quantity", 1)
    .put("price", 99.99)
    .put("metadata", new JSONObject()
        .put("sku", "WH-BLK-PRO")
        .put("color", "Black")
        .put("brand", "AudioTech"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("order_id", "order_67890")
    .addProperty("total_value", 99.99)
    .addProperty("currency", "USD")
    .addProperty("total_discounts", 5.00)
    .addProperty("discounts", discounts)
    .addProperty("products", products)
    .addProperty("source", "https://braze-audio.com")
    .addProperty("metadata", new JSONObject()
        .put("order_status_url", "https://braze-audio.com/orders/67890/status")
        .put("order_note", "Customer requested refund due to defective item")
        .put("order_number", "ORD-2024-001234")
        .put("tags", new JSONArray().put("refund").put("defective")));

Braze.getInstance(context).logCustomEvent("ecommerce.order_refunded", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let discounts: [[String: Any]] = [
    [
        "code": "SAVE5",
        "amount": 5.00
    ]
]

let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 99.99,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "order_id": "order_67890",
    "total_value": 99.99,
    "currency": "USD",
    "total_discounts": 5.00,
    "discounts": discounts,
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_note": "Customer requested refund due to defective item",
        "order_number": "ORD-2024-001234",
        "tags": ["refund", "defective"]
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.order_refunded", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.order_refunded",
      "time": "2024-01-15T10:15:30Z",
      "properties": {
        "order_id": "order_67890",
        "total_value": 99.99,
        "currency": "USD",
        "total_discounts": 5.00,
        "discounts": [
          {
            "code": "SAVE5",
            "amount": 5.00
          }
        ],
        "products": [
          {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 99.99,
            "metadata": {
              "sku": "WH-BLK-PRO",
              "color": "Black",
              "brand": "BrazeAudio"
            }
          }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
          "order_status_url": "https://braze-audio.com/orders/67890/status",
          "order_note": "Customer requested refund due to defective item",
          "order_number": "ORD-2024-001234",
          "tags": ["refund", "defective"]
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.order_cancelled %}

Vous pouvez utiliser l'événement « commande annulée » pour déclencher une action lorsqu'un client annule une commande.

#### Propriétés

| Nom de la propriété      | Requis | Type de données | Description       |
|---------------------|----------|-----------|-------------------|
| `order_id`            | Oui      | Chaîne de caractères    | Identifiant unique de la commande passée.              |
| `cancel_reason`       | Oui      | Chaîne de caractères    | Raison pour laquelle la commande a été annulée.           |
| `total_value`         | Oui      | Float     | Valeur monétaire totale du panier.         |
| `currency`            | Oui      | Chaîne de caractères    | Devise dans laquelle le panier est évalué.           |
| `total_discounts`     | Non       | Float     | Montant total des réductions appliquées à la commande.     |
| `discounts`           | Non       | Tableau d'objets     | Liste détaillée des réductions appliquées à la commande.             |
| `products`            | Oui      | Tableau d'objets     |         |
| `product_id`          | Oui      | Chaîne de caractères    | Identifiant unique du produit consulté. Cette valeur peut être l'ID du produit, l'unité de gestion des stocks ou une valeur similaire.             |
| `product_name`        | Oui      | Chaîne de caractères    | Le nom du produit consulté.          |
| `variant_id`          | Oui      | Chaîne de caractères    | Identifiant unique de la variante du produit (tel que `shirt_medium_blue`).        |
| `image_url`           | Non       | Chaîne de caractères    | URL de l'image du produit.           |
| `product_url`         | Non       | Chaîne de caractères    | URL vers la page du produit pour plus de détails.                                                                     |
| `quantity`            | Oui      | Entier   | Nombre d'unités du produit dans le panier.        |
| `price`               | Oui      | Float     | Le prix unitaire de la variante du produit au moment de la consultation.     |
| `metadata`            | Non       | Objet    | Champ de métadonnées supplémentaires sur le produit que le client souhaite ajouter pour ses cas d'utilisation. Pour Shopify, nous ajouterons l'unité de gestion des stocks. Ce champ est soumis à la limite générale de 50 ko pour les propriétés d'événement. |
| `sku`                 | Non       | Chaîne de caractères    | (Shopify uniquement) Unité de gestion des stocks Shopify. Ce champ peut être configuré comme le champ ID du catalogue.        |
| `source`              | Oui      | Chaîne de caractères    | Source d'où provient l'événement (pour Shopify, il s'agit de storefront).    |
| `metadata`            | Non       | Objet    |       |
| `order_status_url`    | Non       | Chaîne de caractères    | URL pour consulter le statut de la commande.                                                                          |
| `order_number`        | Non       | Chaîne de caractères    | (Shopify uniquement) Numéro de commande unique pour la commande passée.  |
| `tags`                | Non       | Tableau     | (Shopify uniquement) Étiquettes de la commande.            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Exemples d'objets

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.order_cancelled", {
    "order_id": "order_67890",
    "cancel_reason": "customer changed mind",
    "total_value": 189.98,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": [
        {
            "code": "SAVE10",
            "amount": 10.00
        }
    ],
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["cancelled", "customer_request"]
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray discounts = new JSONArray();
discounts.put(new JSONObject()
    .put("code", "SAVE10")
    .put("amount", 10.00));

JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "632910392")
    .put("product_name", "Wireless Headphones")
    .put("variant_id", "808950810")
    .put("quantity", 1)
    .put("price", 199.98)
    .put("metadata", new JSONObject()
        .put("sku", "WH-BLK-PRO")
        .put("color", "Black")
        .put("brand", "AudioTech"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("order_id", "order_67890")
    .addProperty("cancel_reason", "customer changed mind")
    .addProperty("total_value", 189.98)
    .addProperty("currency", "USD")
    .addProperty("total_discounts", 10.00)
    .addProperty("discounts", discounts)
    .addProperty("products", products)
    .addProperty("source", "https://braze-audio.com")
    .addProperty("metadata", new JSONObject()
        .put("order_status_url", "https://braze-audio.com/orders/67890/status")
        .put("order_number", "ORD-2024-001234")
        .put("tags", new JSONArray().put("cancelled").put("customer_request")));

Braze.getInstance(context).logCustomEvent("ecommerce.order_cancelled", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let discounts: [[String: Any]] = [
    [
        "code": "SAVE10",
        "amount": 10.00
    ]
]

let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 199.98,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "order_id": "order_67890",
    "cancel_reason": "customer changed mind",
    "total_value": 189.98,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": discounts,
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["cancelled", "customer_request"]
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.order_cancelled", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.order_cancelled",
      "time": "2024-01-15T10:45:15Z",
      "properties": {
        "order_id": "order_67890",
        "cancel_reason": "customer changed mind",
        "total_value": 189.98,
        "currency": "USD",
        "total_discounts": 10.00,
        "discounts": [
          {
            "code": "SAVE10",
            "amount": 10.00
          }
        ],
        "products": [
          {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
              "sku": "WH-BLK-PRO",
              "color": "Black",
              "brand": "BrazeAudio"
            }
          }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
          "order_status_url": "https://braze-audio.com/orders/67890/status",
          "order_number": "ORD-2024-001234",
          "tags": ["cancelled", "customer_request"]
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% endtabs %}

## Modèles Canvas pour le commerce électronique

Braze propose des modèles Canvas préconstruits alimentés par les événements recommandés pour le commerce électronique, comme le ciblage des clients qui ont commencé le processus de paiement mais sont partis avant de passer leur commande. Vous pouvez utiliser ces événements pour prendre des décisions éclairées afin d'améliorer le parcours utilisateur en personnalisant les messages et en ciblant des audiences spécifiques.

Consultez nos [cas d'utilisation dédiés au commerce électronique]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases) pour découvrir d'autres façons d'utiliser ces événements avec les modèles Canvas.

## Champs calculés de l'utilisateur

Nous utilisons des calculs normalisés pour les champs suivants : 

- **Chiffre d'affaires total** = somme de la valeur totale des commandes passées - somme de la valeur totale des commandes remboursées
- **Nombre total de commandes** = nombre d'événements distincts de commandes passées - nombre d'annulations de commandes distinctes
- **Valeur totale des remboursements** = somme de la valeur totale des commandes remboursées 

Ces champs calculés sont également disponibles dans l'onglet **Transactions** des profils utilisateurs.

![L'onglet « Transactions » avec les champs calculés de l'utilisateur.]({% image_buster /assets/img/Shopify/transactions_tab.png %}){: style="max-width:70%;"}

## Foire aux questions

### Où puis-je consulter les données d'achat au niveau des produits ?

L'onglet **Transactions** du profil utilisateur affiche des champs calculés de haut niveau (tels que le chiffre d'affaires total et le nombre total de commandes). Pour afficher les détails au niveau du produit pour un utilisateur spécifique, utilisez le [générateur de requêtes]({{site.baseurl}}/user_guide/analytics/query_builder/) pour interroger les données d'événements e-commerce, ou exportez les données d'événements via [Currents]({{site.baseurl}}/user_guide/data/braze_currents/).

Contrairement aux événements d'achat hérités, les événements recommandés pour le commerce électronique stockent les détails des produits sous forme de propriétés de l'événement imbriquées dans le tableau `products`. Ces propriétés sont disponibles dans l'envoi de messages via Liquid et dans la segmentation via les [extensions de segments]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/).

### Comment segmenter les utilisateurs en fonction d'un produit spécifique ?

Le segmenteur vous permet de filtrer en fonction du nombre de fois qu'un utilisateur a effectué un événement e-commerce. Pour filtrer selon des propriétés spécifiques du produit (telles que `product_id` ou `product_name`), utilisez les [extensions de segments]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/), qui prennent en charge le filtrage des propriétés de l'événement imbriqué. Par exemple, vous pouvez identifier tous les utilisateurs ayant acheté le produit « SKU-123 » au cours des 90 derniers jours.

### Quelle est la différence entre les événements d'achat hérités et les événements recommandés pour le commerce électronique ?

Les événements d'achat hérités utilisent l'[objet d'achat]({{site.baseurl}}/api/objects_filters/purchase_object/) de Braze et enregistrent les achats de produits individuels avec un `product_id` et un `price`. Les événements recommandés pour le commerce électronique (tels que `ecommerce.order_placed`) utilisent des propriétés d'événement personnalisées et capturent le contexte complet de la commande, y compris les produits multiples, les réductions et les métadonnées, le tout dans un seul événement.

Avec le lancement des événements recommandés pour le commerce électronique, Braze supprimera progressivement l'événement d'achat hérité à l'avenir. Si vous utilisez actuellement les événements d'achat, vous recevrez un préavis. En attendant, vous pouvez continuer à utiliser les événements d'achat jusqu'à la date officielle de dépréciation. Consultez l'[aperçu des événements recommandés]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/) pour plus de détails.

### Puis-je ajouter des propriétés personnalisées aux événements recommandés pour le commerce électronique ?

Les événements recommandés pour le commerce électronique suivent un schéma défini avec des champs obligatoires et facultatifs. Vous pouvez inclure des données personnalisées supplémentaires dans l'objet `metadata` de chaque événement. En revanche, les étiquettes personnalisées au niveau de la commande ou les champs propriétaires (tels que le canal d'achat ou les informations sur le magasin) ne sont pas pris en charge en tant que propriétés de niveau supérieur. Si vous avez besoin de ces champs pour la segmentation, continuez à les envoyer en tant qu'événements personnalisés distincts en parallèle de vos événements e-commerce.

### Dois-je inclure `external_id` lors de l'envoi d'événements e-commerce ?

Cela dépend de la manière dont vous transmettez les événements :

- **Via le SDK** : Non. Lorsque vous utilisez un SDK Braze, les événements sont automatiquement associés au contexte utilisateur actuel du SDK (anonyme ou identifié). Il n'est pas nécessaire de transmettre un identifiant utilisateur à chaque appel d'événement ; vous pouvez identifier l'utilisateur pour ce contexte à l'aide de méthodes telles que `changeUser`.
- **Via l'API REST** (`/users/track`) : Oui. Chaque requête API doit inclure un identifiant utilisateur, tel que `external_id`, `braze_id`, `user_alias`, `email` ou `phone`, car l'API ne dispose pas de contexte « utilisateur actuel ».

### Pourquoi les propriétés de produit imbriquées n'apparaissent-elles pas dans le menu déroulant de configuration des recommandations par intelligence artificielle ?

Lors de la configuration des [recommandations d'articles par intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/recommendations/), le menu déroulant **Nom de la propriété** ne répertorie que les propriétés d'événement de niveau supérieur (telles que `order_id`, `total_value` et `currency`). Les propriétés imbriquées dans le tableau `products` (par exemple, `products.product_id` ou `products.variant_id`) peuvent ne pas apparaître dans cette liste, mais vous pouvez les saisir manuellement en utilisant la notation par points dans le champ. Pour la plupart des implémentations e-commerce, Braze recommande d'utiliser `products.product_id` comme identifiant d'article et de l'associer à un [catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/) dont les ID d'articles correspondent à vos valeurs `product_id` ou `variant_id`.

### Pourquoi certains de mes événements e-commerce n'apparaissent-ils pas dans Braze ?

Si les événements n'apparaissent pas dans les profils utilisateurs ou les journaux, vérifiez les points suivants :

- **Délai de vidage des données du SDK** : Le SDK Braze met les données en cache localement et les téléverse périodiquement (généralement dans un délai de 10 à 60 secondes). Appelez `requestImmediateDataFlush()` après `logCustomEvent()` pour forcer un envoi immédiat.
- **Propriétés requises** : les événements e-commerce ont des propriétés obligatoires. Si une propriété requise est manquante ou si son type de données n'est pas valide, l'événement peut être rejeté. Vérifiez que le payload de votre événement correspond au [schéma requis](#types-of-ecommerce-recommended-events).
- **Précision du nom de l'événement** : les noms des événements e-commerce sont sensibles à la casse et doivent correspondre exactement (par exemple, `ecommerce.checkout_started` et non `ecommerce.checkoutStarted`).