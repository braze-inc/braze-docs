---
nav_title: Événements recommandés pour le commerce électronique
article_title: eCommerce Événements recommandés
page_type: reference
alias: /ecommerce_events/
toc_headers: h2
description: "Cet article de référence décrit les événements et propriétés recommandés pour le commerce électronique, leur utilisation, la segmentation, l'endroit où afficher les analyses pertinentes, et plus encore."
---

# Événements recommandés pour le commerce électronique

> Cette page couvre les événements et propriétés recommandés pour le commerce électronique. Ces événements sont créés pour capturer les comportements d'achat clés dont les marketeurs ont besoin pour déclencher des messages efficaces, comme le ciblage des paniers abandonnés.

{% alert important %}
Les événements recommandés pour le commerce électronique sont actuellement en accès anticipé. Contactez votre gestionnaire satisfaction client Braze si vous souhaitez participer à cet accès anticipé. <br><br>Si vous utilisez le nouveau [connecteur Shopify]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector), ces événements recommandés seront automatiquement disponibles grâce à l'intégration.
{% endalert %}

Braze reconnaît que la planification des données prend du temps. Nous encourageons nos personnalisés à familiariser leurs équipes de développement et à commencer à envoyer ces événements dès maintenant. Bien que certaines fonctionnalités ne soient pas disponibles immédiatement avec les événements recommandés pour le commerce électronique, vous pouvez vous attendre à l'introduction de nouveaux produits tout au long de l'année 2025 qui amélioreront vos capacités de commerce électronique.

## Types d'événements recommandés pour le commerce électronique

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

Toute devise autre que le dollar américain s'affichera dans Braze en dollars américains, sur la base du taux de change en vigueur à la date de la déclaration. Pour éviter la conversion des devises, coder en dur la devise en USD.

{% tabs %}
{% tab ecommerce.product_viewed %}

Vous pouvez utiliser l'événement "produit consulté" pour déclencher une action lorsqu'un client consulte la page détaillée d'un produit.

#### Propriétés

| Nom du bien | Exigée | Type de données | Description | 
|---|---|---|---|
| `product_id` | Oui | Chaîne de caractères | Identifiant unique du produit consulté. <br> Pour les clients non-Shopify, il s'agira de la valeur que vous définissez pour les ID d'articles du catalogue, comme les UGS. |
| `product_name` | Oui | Chaîne de caractères | Le nom du produit qui a été consulté. | 
| `variant_id` | Oui | Chaîne de caractères | Un identifiant unique pour la variante du produit. En voici un exemple `shirt_medium_blue` |
| `image_url` | Non | Chaîne de caractères | URL de l'image du produit. |
| `product_url` | Non | Chaîne de caractères | URL vers la page du produit pour plus de détails. |
| `price` | Oui | Float | Le prix unitaire variante du produit au moment de la consultation. |
| `currency` | Oui | Chaîne de caractères | La devise dans laquelle le prix du produit est indiqué (par exemple "USD" ou "EUR") au [format ISO 4217](https://www.iso.org/iso-4217-currency-codes.html). |
| `source` | Oui | Chaîne de caractères | Source d'où provient l'événement. (Pour Shopify, il s'agit de storefront). |
| `metadata` | Non | Objet | |
| `type` | Non | Objet | Fonctionne avec les [notifications de retour en stock]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications) et les [notifications de baisse de prix]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications). |
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
        }
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

Vous pouvez utiliser l'événement de mise à jour du panier pour suivre l'ajout, la suppression ou la mise à jour de produits dans le panier. L'événement `ecommerce.cart_updated` vérifie les informations suivantes avant de se déclencher :

- L'heure de l'événement est supérieure à l'heure du site `updated_at` pour le panier spécifique de l'utilisateur.
- Le panier n'est pas passé à la caisse.
- Le tableau `products` n'est pas vide.

#### Objet de mappage des chariots

L'événement `ecommerce.cart_updated` possède un objet de mappage des paniers. Cet objet est créé pour le profil utilisateur qui contient un mappage des paniers, lesquels contiennent tous les produits du panier de l'acheteur. Vous pouvez accéder aux produits de leur panier par l'intermédiaire de l'étiquette Liquid : 

{%raw%}
```liquid
{% shopping_cart {{context_properties.${cart_id}}} %}
{% for item in shopping_cart.products %}
{% catalog_items <add_your_catalog> {{item.variant_id}} %}
```
{%endraw%}

Si un panier n'a pas été mis à jour et n'est pas passé à l'étape de la commande dans les 10 jours, nous supprimerons le panier et les produits associés.

{% alert note %}
Les produits par panier ne sont pas limités sur Braze. Cependant, la limite de Shopify est de 500.
{% endalert %}

#### Comportement du chariot lors de la fusion de profils utilisateurs

S'il y a deux paniers, ajoutez les deux à l'utilisateur fusionné. Remettez le Canvas en file d'attente s'il s'agit du même panier ou d'un panier différent afin d'envoyer un message contenant les informations les plus récentes sur le panier. L'événement `ecommerce.cart_updated` contiendra l'ID du dernier panier et les derniers produits du panier.

#### Propriétés

| Nom du bien | Exigée | Type de données | Description | 
|---|---|---|---|
| `cart_id` | Oui | Chaîne de caractères | Identifiant unique du panier. Si aucune valeur n'est transmise, nous déterminerons une valeur par défaut (partagée entre les événements panier, caisse et commande) pour le mappage du panier de l'utilisateur. |
| `total_value` | Oui | Float | Valeur monétaire totale du panier. | 
| `currency` | Oui | Chaîne de caractères | La devise dans laquelle le prix du produit est indiqué (par exemple "USD" ou "EUR") au [format ISO 4217](https://www.iso.org/iso-4217-currency-codes.html). |
| `products` | Oui | Réseau |  |
| `product_id` | Oui | Chaîne de caractères | Identifiant unique du produit consulté. <br> Cette valeur peut être l'ID du produit ou l'unité de gestion des stocks. |
| `product_name` | Oui | Chaîne de caractères | Le nom du produit qui a été consulté. |
| `variant_id` | Oui | Chaîne de caractères | Un identifiant unique pour la variante du produit. En voici un exemple `shirt_medium_blue` |
| `image_url` | Non | Chaîne de caractères | URL de l'image du produit. |
| `product_url` | Non | Chaîne de caractères | URL vers la page du produit pour plus de détails. |
| `quantity` | Oui | Entier | Nombre d'unités du produit dans le panier. |
| `price` | Oui | Float | Le prix unitaire variante du produit au moment de la consultation. |
| `metadata` | Non | Objet | Champ de métadonnées supplémentaires sur le produit que le client souhaite ajouter pour ses cas d'utilisation. Pour Shopify, nous ajouterons l'unité de gestion des stocks. <br> Cette limite est basée sur la limite générale de 50 kb fixée pour les propriétés d'un événement. |
| `sku` | Non | Chaîne de caractères | (Shopify uniquement) Unité de gestion des stocks Shopify. Ce champ peut être configuré comme le champ ID du catalogue. |
| `source` | Oui | Chaîne de caractères | Source d'où provient l'événement. (Pour Shopify, il s'agit de storefront). |
| `metadata` | Non | Objet | Champ de métadonnées supplémentaires sur le produit que le client souhaite ajouter pour ses cas d'utilisation. Pour Shopify, nous ajouterons l'unité de gestion des stocks. <br> Cette limite est basée sur la limite générale de 50 kb fixée pour les propriétés d'un événement. |
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

Vous pouvez utiliser l'événement checkout started pour recibler les clients qui ont commencé le processus de paiement mais n'ont pas passé de commande.

Semblable à l'événement `ecommerce.cart_updated`, cet événement vous permet d'exploiter l'étiquette Liquid du panier d'achat pour accéder à tous les produits contenus dans le panier afin d'envoyer des messages d'abandon de panier :

{%raw%}
```liquid
{% shopping_cart {{context_properties.${cart_id}}} :abort_if_not_abandoned false %}
{% for item in shopping_cart.products %}
{% catalog_items <add_your_catalog> {{item.variant_id}} %}
```
{%endraw%}

#### Propriétés

| Nom du bien | Exigée | Type de données | Description | 
|---|---|---|---|
| `checkout_id` | Oui | Chaîne de caractères | Identifiant unique de la caisse. |
| `cart_id` | Non | Chaîne de caractères | Identifiant unique du panier. Si aucune valeur n'est transmise, nous déterminerons une valeur par défaut (partagée entre les événements panier, caisse et commande) pour le mappage du panier de l'utilisateur... | 
| `total_value` | Oui | Float | Valeur monétaire totale du panier. |
| `currency` | Oui | Chaîne de caractères | Devise dans laquelle le panier est évalué. |
| `products` | Oui | Tableau d'objets |  |
| `product_id` | Oui | Chaîne de caractères | Identifiant unique du produit consulté. Par exemple, cette valeur peut être l'ID du produit ou l'unité de gestion des stocks. |
| `product_name` | Oui | Chaîne de caractères | Le nom du produit qui a été consulté.  |
| `variant_id` | Oui | Chaîne de caractères | Un identifiant unique pour la variante du produit. En voici un exemple `shirt_medium_blue` |
| `image_url` | Non | Chaîne de caractères | URL de l'image du produit. |
| `product_url` | Non | Chaîne de caractères | URL vers la page du produit pour plus de détails. |
| `quantity` | Oui | Entier | Nombre d'unités du produit dans le panier. |
| `price` | Oui | Float | Le prix unitaire variante du produit au moment de la consultation. |
| `metadata` | Non | Objet | Champ de métadonnées supplémentaires sur le produit que le client souhaite ajouter pour ses cas d'utilisation. Pour Shopify, nous ajouterons l'unité de gestion des stocks. <br> Cette limite est basée sur la limite générale de 50 kb fixée pour les propriétés d'un événement. |
| `sku` | Non | Chaîne de caractères | (Shopify uniquement) Unité de gestion des stocks Shopify. Ce champ peut être configuré comme le champ ID du catalogue. |
| `source` | Oui | Chaîne de caractères | Source d'où provient l'événement. (Pour Shopify, il s'agit de storefront). |
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

Vous pouvez utiliser l'événement "commande passée" pour déclencher le processus lorsqu'un client passe à la caisse et passe une commande.

#### Propriétés

| Nom du bien | Exigée | Type de données | Description | 
|---|---|---|---|
| `order_id` | Oui | Chaîne de caractères | Identifiant unique de la commande passée. |
| `cart_id` | Non | Chaîne de caractères | Identifiant unique du panier. Si aucune valeur n'est transmise, nous déterminerons une valeur par défaut (partagée entre les événements panier, caisse et commande) pour le mappage du panier de l'utilisateur. |
| `total_value` | Oui | Float | Valeur monétaire totale du panier. | 
| `currency` | Oui | Chaîne de caractères | Devise dans laquelle le panier est évalué. |
| `total_discounts` | Non | Float | Montant total des réductions appliquées à la commande. | 
| `discounts`| Non | Tableau d'objets | Liste détaillée des réductions appliquées à la commande. |
| `products` | Oui | Tableau d'objets |  |
| `product_id` | Oui | Chaîne de caractères | Identifiant unique du produit consulté. Cette valeur peut être l'ID du produit ou l'unité de gestion des stocks. |
| `product_name` | Oui | Chaîne de caractères | Le nom du produit qui a été consulté. |
| `variant_id` | Oui | Chaîne de caractères | Un identifiant unique pour la variante du produit. En voici un exemple `shirt_medium_blue` |
| `image_url` | Non | Chaîne de caractères | URL de l'image du produit. |
| `product_url` | Non | Chaîne de caractères | URL vers la page du produit pour plus de détails. |
| `quantity` | Oui | Entier | Nombre d'unités du produit dans le panier. |
| `price` | Oui | Float | Le prix unitaire variante du produit au moment de la consultation. |
| `metadata` | Non | Objet | Champ de métadonnées supplémentaires sur le produit que le client souhaite ajouter pour ses cas d'utilisation. Pour Shopify, nous ajouterons l'unité de gestion des stocks. <br> Cette limite est basée sur la limite générale de 50 kb fixée pour les propriétés d'un événement. |
| `sku` | Non | Chaîne de caractères | (Shopify uniquement) Unité de gestion des stocks Shopify. Ce champ peut être configuré comme le champ ID du catalogue. |
| `source` | Oui | Chaîne de caractères | Source d'où provient l'événement. (Pour Shopify, il s'agit de storefront). |
| `metadata` | Non | Objet |  |
| `order_status_url` | Non | Chaîne de caractères | URL pour consulter le statut de la commande. |
| `order_number` | Non | Chaîne de caractères | (Shopify uniquement) Numéro de commande unique pour la commande passée. |
| `tags` | Non | Réseau | (Shopify uniquement) Tags de commande
| `referring_site` | Non | Chaîne de caractères | (Shopify uniquement) Le site d'où provient la commande (comme Meta). |
| `payment_gateway_names` | Non | Réseau | (Shopify uniquement) Source du système de paiement (point de vente ou mobile). |
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

Vous pouvez utiliser l'événement "commande remboursée" pour déclencher le remboursement partiel ou total d'une commande.

#### Propriétés

| Nom du bien       | Exigée | Type de données | Description   |
|---------------|---------|-----------|-------------------------|
| `order_id`            | Oui      | Chaîne de caractères    | Identifiant unique de la commande passée.        |
| `total_value`         | Oui      | Float     | Valeur monétaire totale du panier.    |
| `currency`            | Oui      | Chaîne de caractères    | Devise dans laquelle le panier est évalué.    |
| `total_discounts`     | Non       | Float     | Montant total des réductions appliquées à la commande.   |
| `discounts`           | Non       | Tableau d'objets     | Liste détaillée des réductions appliquées à la commande. |
| `products`            | Oui      | Tableau d'objets     |  |
| `product_id`       | Oui      | Chaîne de caractères    | Identifiant unique du produit consulté. Cette valeur peut être l'ID du produit, l'unité de gestion des stocks ou une valeur similaire. <br>Si un remboursement partiel est effectué et qu'aucune adresse `product_id` n'est attribuée au remboursement (par exemple, un remboursement au niveau de la commande), fournissez une adresse généralisée `product_id`.             |
| `product_name`     | Oui      | Chaîne de caractères    | Le nom du produit qui a été consulté.                                                                      |
| `variant_id`       | Oui      | Chaîne de caractères    | Un identifiant unique pour la variante du produit (tel que `shirt_medium_blue`).                                         |
| `image_url`        | Non       | Chaîne de caractères    | URL de l'image du produit.     |
| `product_url`      | Non       | Chaîne de caractères    | URL vers la page du produit pour plus de détails.  |
| `quantity`         | Oui      | Entier   | Nombre d'unités du produit dans le panier.   |
| `price`            | Oui      | Float     | Le prix unitaire variante du produit au moment de la consultation.  |
| `metadata`         | Non       | Objet    | Champ de métadonnées supplémentaires sur le produit que le client souhaite ajouter pour ses cas d'utilisation. Pour Shopify, nous ajouterons l'unité de gestion des stocks. Cette limite est basée sur la limite générale de 50 kb fixée pour les propriétés d'un événement. |
| `sku`            | Non       | Chaîne de caractères    | (Shopify uniquement) Unité de gestion des stocks Shopify. Ce champ peut être configuré comme le champ ID du catalogue.  |
| `source`              | Oui      | Chaîne de caractères    | Source d'où provient l'événement. (Pour Shopify, il s'agit de storefront).    |
| `metadata`            | Non       | Objet    |                |
| `order_status_url`  | Non       | Chaîne de caractères    | URL pour consulter le statut de la commande.     |
| `order_note`       | Non       | Chaîne de caractères    | (Shopify uniquement) Note ajoutée à la commande par le commerçant.    |
| `order_number`     | Non       | Chaîne de caractères    | (Shopify uniquement) Numéro de commande unique pour la commande passée.   |
| `tags`             | Non       | Réseau     | (Shopify uniquement) Tags de la commande.  |
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

Vous pouvez utiliser l'événement "commande annulée" pour déclencher l'annulation d'une commande par un client.

#### Propriétés

| Nom du bien      | Exigée | Type de données | Description       |
|---------------------|----------|-----------|-------------------|
| `order_id`            | Oui      | Chaîne de caractères    | Identifiant unique de la commande passée.              |
| `cancel_reason`       | Oui      | Chaîne de caractères    | Raison pour laquelle la commande a été annulée.           |
| `total_value`         | Oui      | Float     | Valeur monétaire totale du panier.         |
| `currency`            | Oui      | Chaîne de caractères    | Devise dans laquelle le panier est évalué.           |
| `total_discounts`     | Non       | Float     | Montant total des réductions appliquées à la commande.     |
| `discounts`           | Non       | Tableau d'objets     | Liste détaillée des réductions appliquées à la commande.             |
| `products`            | Oui      | Tableau d'objets     |         |
| `product_id`          | Oui      | Chaîne de caractères    | Identifiant unique du produit consulté. Cette valeur peut être l'ID du produit, l'unité de gestion des stocks ou une valeur similaire.             |
| `product_name`        | Oui      | Chaîne de caractères    | Le nom du produit qui a été consulté.          |
| `variant_id`          | Oui      | Chaîne de caractères    | Un identifiant unique pour la variante du produit (tel que `shirt_medium_blue`).        |
| `image_url`           | Non       | Chaîne de caractères    | URL de l'image du produit.           |
| `product_url`         | Non       | Chaîne de caractères    | URL vers la page du produit pour plus de détails.                                                                     |
| `quantity`            | Oui      | Entier   | Nombre d'unités du produit dans le panier.        |
| `price`               | Oui      | Float     | Le prix unitaire variante du produit au moment de la consultation.     |
| `metadata`            | Non       | Objet    | Champ de métadonnées supplémentaires sur le produit que le client souhaite ajouter pour ses cas d'utilisation. Pour Shopify, nous ajouterons l'unité de gestion des stocks. Cette limite est basée sur la limite générale de 50 kb fixée pour les propriétés d'un événement. |
| `sku`                 | Non       | Chaîne de caractères    | (Shopify uniquement) Unité de gestion des stocks Shopify. Ce champ peut être configuré comme le champ ID du catalogue.        |
| `source`              | Oui      | Chaîne de caractères    | Source d'où provient l'événement. (Pour Shopify, il s'agit de storefront).    |
| `metadata`            | Non       | Objet    |       |
| `order_status_url`    | Non       | Chaîne de caractères    | URL pour consulter le statut de la commande.                                                                          |
| `order_number`        | Non       | Chaîne de caractères    | (Shopify uniquement) Numéro de commande unique pour la commande passée.  |
| `tags`                | Non       | Réseau     | (Shopify uniquement) Tags de la commande.            |
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

## Modèles de canevas pour le commerce électronique

Braze a créé des modèles Canvas préconstruits qui sont alimentés par des événements personnalisés recommandés par l'eCommerce, comme le ciblage des clients qui ont commencé le processus de paiement mais sont partis avant de passer leur commande. Vous pouvez utiliser ces événements pour prendre des décisions éclairées afin d'améliorer votre parcours utilisateur en personnalisant les messages et en ciblant des audiences spécifiques.

Consultez nos [cas d'utilisation]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases) dédiés à [l'e-commerce]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases) pour savoir comment utiliser ces événements avec les modèles Canvas.

## Champs calculés par l'utilisateur

Nous utilisons des calculs normalisés pour les champs suivants : 

- **Chiffre d'affaires total** = somme de la valeur totale des commandes passées - somme de la valeur totale des commandes remboursées
- **Nombre total de commandes** = nombre d'événements distincts de commandes passées - nombre d'annulations de commandes distinctes
- **Valeur totale du remboursement** = somme de la valeur totale de la commande remboursée 

Ces calculs de champ d'utilisateur sont également inclus dans l'onglet **Transactions** des profils utilisateurs.

!L'onglet "Transactions" avec des champs calculés par l'utilisateur.]({% image_buster /assets/img/Shopify/transactions_tab.png %}){: style="max-width:60%;"}
