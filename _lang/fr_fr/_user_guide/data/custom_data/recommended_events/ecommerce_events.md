---
nav_title: eCommerce Événements recommandés
article_title: eCommerce Événements recommandés
page_type: reference
alias: /ecommerce_events/
toc_headers: h2
description: "Cet article de référence décrit les événements et propriétés recommandés pour le commerce électronique, leur utilisation, la segmentation, l'endroit où afficher les analyses pertinentes, et plus encore."
---

# Événements recommandés pour le commerce électronique

> Cette page couvre les événements et propriétés recommandés pour le commerce électronique. Ces événements sont créés pour capturer les comportements d'achat clés dont les marketeurs ont besoin pour déclencher des messages efficaces, comme le ciblage des paniers abandonnés.

Braze reconnaît que la planification des données prend du temps. Nous encourageons nos personnalisés à familiariser leurs équipes de développement et à commencer à envoyer ces événements dès maintenant. Bien que certaines fonctionnalités ne soient pas disponibles immédiatement avec les événements recommandés pour le commerce électronique, vous pouvez vous attendre à l'introduction de nouveaux produits tout au long de l'année 2025 qui amélioreront vos capacités de commerce électronique.

{% alert important %}
Les événements recommandés pour le commerce électronique sont actuellement en accès anticipé. Contactez votre gestionnaire satisfaction client Braze si vous souhaitez participer à cet accès anticipé. <br><br>Si vous exploitez le nouveau [connecteur Shopify]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector), ces événements recommandés seront automatiquement disponibles grâce à l'intégration.
{% endalert %}


## Types d'événements recommandés pour le commerce électronique

{% tabs %}
{% tab ecommerce.produit_vu %}

Vous pouvez utiliser l'événement "produit consulté" pour déclencher une action lorsqu'un client consulte la page détaillée d'un produit.

#### Propriétés

| Nom de la propriété | Requis | Type de données | Description | 
|---|---|---|---|
| `product_id` | Oui | Chaîne de caractères | Identifiant unique du produit consulté. <br> Pour les clients non-Shopify, il s'agira de la valeur que vous définissez pour les ID d'articles du catalogue, comme les UGS. |
| `product_name` | Oui | Chaîne de caractères | Le nom du produit qui a été consulté. | 
| `variant_id` | Oui | Chaîne de caractères | Un identifiant unique pour la variante du produit. En voici un exemple `shirt_medium_blue` |
| `image_url` | Non | Chaîne de caractères | URL de l'image du produit. |
| `product_url` | Non | Chaîne de caractères | URL vers la page du produit pour plus de détails. |
| `price` | Oui | float | Le prix unitaire variante du produit au moment de la consultation. |
| `currency` | Oui | Chaîne de caractères | La devise dans laquelle le prix du produit est indiqué (par exemple "USD" ou "EUR") au [format ISO 4217](https://www.iso.org/iso-4217-currency-codes.html). |
| `source` | Oui | Chaîne de caractères | Source d'où provient l'événement. (Pour Shopify, il s'agit de storefront). |
| `metadata` | Non | Objet | |
| `sku` | Non | Chaîne de caractères | (Shopify uniquement) Unité de gestion des stocks Shopify. Ce champ peut être configuré comme le champ ID du catalogue. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Exemple d'objet

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
        }
    }
}
```
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

| Nom de la propriété | Requis | Type de données | Description | 
|---|---|---|---|
| `cart_id` | Oui | Chaîne de caractères | Identifiant unique du panier. Si aucune valeur n'est transmise, nous déterminerons une valeur par défaut (partagée entre les événements panier, caisse et commande) pour le mappage du panier de l'utilisateur. |
| `total_value` | Oui | float | Valeur monétaire totale du panier. | 
| `currency` | Oui | Chaîne de caractères | La devise dans laquelle le prix du produit est indiqué (par exemple "USD" ou "EUR") au [format ISO 4217](https://www.iso.org/iso-4217-currency-codes.html). |
| `products` | Oui | Tableau |  |
| `product_id` | Oui | Chaîne de caractères | Identifiant unique du produit consulté. <br> Cette valeur peut être l'ID du produit ou l'unité de gestion des stocks. |
| `product_name` | Oui | Chaîne de caractères | Le nom du produit qui a été consulté. |
| `variant_id` | Oui | Chaîne de caractères | Un identifiant unique pour la variante du produit. En voici un exemple `shirt_medium_blue` |
| `image_url` | Non | Chaîne de caractères | URL de l'image du produit. |
| `product_url` | Non | Chaîne de caractères | URL vers la page du produit pour plus de détails. |
| `quantity` | Oui | Entier | Nombre d'unités du produit dans le panier. |
| `price` | Oui | float | Le prix unitaire variante du produit au moment de la consultation. |
| `metadata` | Non | Objet | Champ de métadonnées supplémentaires sur le produit que le client souhaite ajouter pour ses cas d'utilisation. Pour Shopify, nous ajouterons l'unité de gestion des stocks. <br> Cette limite est basée sur la limite générale de 50 kb fixée pour les propriétés d'un événement. |
| `sku` | Non | Chaîne de caractères | (Shopify uniquement) Unité de gestion des stocks Shopify. Ce champ peut être configuré comme le champ ID du catalogue. |
| `source` | Oui | Chaîne de caractères | Source d'où provient l'événement. (Pour Shopify, il s'agit de storefront). |
| `metadata` | Non | Objet | Champ de métadonnées supplémentaires sur le produit que le client souhaite ajouter pour ses cas d'utilisation. Pour Shopify, nous ajouterons l'unité de gestion des stocks. <br> Cette limite est basée sur la limite générale de 50 kb fixée pour les propriétés d'un événement. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Exemple d'objet

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

| Nom de la propriété | Requis | Type de données | Description | 
|---|---|---|---|
| `checkout_id` | Oui | Chaîne de caractères | Identifiant unique de la caisse. |
| `cart_id` | Non | Chaîne de caractères | Identifiant unique du panier. Si aucune valeur n'est transmise, nous déterminerons une valeur par défaut (partagée entre les événements panier, caisse et commande) pour le mappage du panier de l'utilisateur... | 
| `total_value` | Oui | float | Valeur monétaire totale du panier. |
| `currency` | Oui | Chaîne de caractères | Devise dans laquelle le panier est évalué. |
| `products` | Oui | Tableau d’objets |  |
| `product_id` | Oui | Chaîne de caractères | Identifiant unique du produit consulté. Par exemple, cette valeur peut être l'ID du produit ou l'unité de gestion des stocks. |
| `product_name` | Oui | Chaîne de caractères | Le nom du produit qui a été consulté.  |
| `variant_id` | Oui | Chaîne de caractères | Un identifiant unique pour la variante du produit. En voici un exemple `shirt_medium_blue` |
| `image_url` | Non | Chaîne de caractères | URL de l'image du produit. |
| `product_url` | Non | Chaîne de caractères | URL vers la page du produit pour plus de détails. |
| `quantity` | Oui | Entier | Nombre d'unités du produit dans le panier. |
| `price` | Oui | float | Le prix unitaire variante du produit au moment de la consultation. |
| `metadata` | Non | Objet | Champ de métadonnées supplémentaires sur le produit que le client souhaite ajouter pour ses cas d'utilisation. Pour Shopify, nous ajouterons l'unité de gestion des stocks. <br> Cette limite est basée sur la limite générale de 50 kb fixée pour les propriétés d'un événement. |
| `sku` | Non | Chaîne de caractères | (Shopify uniquement) Unité de gestion des stocks Shopify. Ce champ peut être configuré comme le champ ID du catalogue. |
| `source` | Oui | Chaîne de caractères | Source d'où provient l'événement. (Pour Shopify, il s'agit de storefront). |
| `metadata` | Non | Objet |  |
| `checkout_url` | Non | Chaîne de caractères | URL de la page de paiement. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Exemple d'objet

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
{% endtab %}
{% tab ecommerce.order_placed %}

Vous pouvez utiliser l'événement "commande passée" pour déclencher le processus lorsqu'un client passe à la caisse et passe une commande.

#### Propriétés

| Nom de la propriété | Requis | Type de données | Description | 
|---|---|---|---|
| `order_id` | Oui | Chaîne de caractères | Identifiant unique de la commande passée. |
| `cart_id` | Non | Chaîne de caractères | Identifiant unique du panier. Si aucune valeur n'est transmise, nous déterminerons une valeur par défaut (partagée entre les événements panier, caisse et commande) pour le mappage du panier de l'utilisateur. |
| `total_value` | Oui | float | Valeur monétaire totale du panier. | 
| `currency` | Oui | Chaîne de caractères | Devise dans laquelle le panier est évalué. |
| `total_discounts` | Non | float | Montant total des réductions appliquées à la commande. | 
| `discounts`| Non | Tableau d’objets | Liste détaillée des réductions appliquées à la commande. |
| `products` | Oui | Tableau d’objets |  |
| `product_id` | Oui | Chaîne de caractères | Identifiant unique du produit consulté. Cette valeur peut être l'ID du produit ou l'unité de gestion des stocks. |
| `product_name` | Oui | Chaîne de caractères | Le nom du produit qui a été consulté. |
| `variant_id` | Oui | Chaîne de caractères | Un identifiant unique pour la variante du produit. En voici un exemple `shirt_medium_blue` |
| `image_url` | Non | Chaîne de caractères | URL de l'image du produit. |
| `product_url` | Non | Chaîne de caractères | URL vers la page du produit pour plus de détails. |
| `quantity` | Oui | Entier | Nombre d'unités du produit dans le panier. |
| `price` | Oui | float | Le prix unitaire variante du produit au moment de la consultation. |
| `metadata` | Non | Objet | Champ de métadonnées supplémentaires sur le produit que le client souhaite ajouter pour ses cas d'utilisation. Pour Shopify, nous ajouterons l'unité de gestion des stocks. <br> Cette limite est basée sur la limite générale de 50 kb fixée pour les propriétés d'un événement. |
| `sku` | Non | Chaîne de caractères | (Shopify uniquement) Unité de gestion des stocks Shopify. Ce champ peut être configuré comme le champ ID du catalogue. |
| `source` | Oui | Chaîne de caractères | Source d'où provient l'événement. (Pour Shopify, il s'agit de storefront). |
| `metadata` | Non | Objet |  |
| `order_status_url` | Non | Chaîne de caractères | URL pour consulter le statut de la commande. |
| `order_number` | Non | Chaîne de caractères | (Shopify uniquement) Numéro de commande unique pour la commande passée. |
| `tags` | Non | Tableau | (Shopify uniquement) Tags de commande
| `referring_site` | Non | Chaîne de caractères | (Shopify uniquement) Le site d'où provient la commande (comme Meta). |
| `payment_gateway_names` | Non | Tableau | (Shopify uniquement) Source du système de paiement (point de vente ou mobile). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Exemple d'objet

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
{% endtab %}
{% tab ecommerce.commande_remboursée %}

Vous pouvez utiliser l'événement "commande remboursée" pour déclencher le remboursement partiel ou total d'une commande.

#### Propriétés

| Nom de la propriété       | Requis | Type de données | Description   |
|---------------|---------|-----------|-------------------------|
| `order_id`            | Oui      | Chaîne de caractères    | Identifiant unique de la commande passée.        |
| `total_value`         | Oui      | float     | Valeur monétaire totale du panier.    |
| `currency`            | Oui      | Chaîne de caractères    | Devise dans laquelle le panier est évalué.    |
| `total_discounts`     | Non       | float     | Montant total des réductions appliquées à la commande.   |
| `discounts`           | Non       | Tableau d’objets     | Liste détaillée des réductions appliquées à la commande. |
| `products`            | Oui      | Tableau d’objets     |  |
| `product_id`       | Oui      | Chaîne de caractères    | Identifiant unique du produit consulté. Cette valeur peut être l'ID du produit, l'unité de gestion des stocks ou une valeur similaire. <br>Si un remboursement partiel est effectué et qu'aucune adresse `product_id` n'est attribuée au remboursement (par exemple, un remboursement au niveau de la commande), fournissez une adresse généralisée `product_id`.             |
| `product_name`     | Oui      | Chaîne de caractères    | Le nom du produit qui a été consulté.                                                                      |
| `variant_id`       | Oui      | Chaîne de caractères    | Un identifiant unique pour la variante du produit (tel que `shirt_medium_blue`).                                         |
| `image_url`        | Non       | Chaîne de caractères    | URL de l'image du produit.     |
| `product_url`      | Non       | Chaîne de caractères    | URL vers la page du produit pour plus de détails.  |
| `quantity`         | Oui      | Entier   | Nombre d'unités du produit dans le panier.   |
| `price`            | Oui      | float     | Le prix unitaire variante du produit au moment de la consultation.  |
| `metadata`         | Non       | Objet    | Champ de métadonnées supplémentaires sur le produit que le client souhaite ajouter pour ses cas d'utilisation. Pour Shopify, nous ajouterons l'unité de gestion des stocks. Cette limite est basée sur la limite générale de 50 kb fixée pour les propriétés d'un événement. |
| `sku`            | Non       | Chaîne de caractères    | (Shopify uniquement) Unité de gestion des stocks Shopify. Ce champ peut être configuré comme le champ ID du catalogue.  |
| `source`              | Oui      | Chaîne de caractères    | Source d'où provient l'événement. (Pour Shopify, il s'agit de storefront).    |
| `metadata`            | Non       | Objet    |                |
| `order_status_url`  | Non       | Chaîne de caractères    | URL pour consulter le statut de la commande.     |
| `order_note`       | Non       | Chaîne de caractères    | (Shopify uniquement) Note ajoutée à la commande par le commerçant.    |
| `order_number`     | Non       | Chaîne de caractères    | (Shopify uniquement) Numéro de commande unique pour la commande passée.   |
| `tags`             | Non       | Tableau     | (Shopify uniquement) Tags de la commande.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Exemple d'objet

```json
{
    "name": "ecommerce.order_refunded",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "order_id": "820982911946154508",
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
			"order_note": "item was broken",
            "order_number": 1234,
            "tags": [
                "heavy",
                "heavy2"
            ]
        }
    }
}
```
{% endtab %}
{% tab ecommerce.commande_annulée %}

Vous pouvez utiliser l'événement "commande annulée" pour déclencher l'annulation d'une commande par un client.

#### Propriétés

| Nom de la propriété      | Requis | Type de données | Description       |
|---------------------|----------|-----------|-------------------|
| `order_id`            | Oui      | Chaîne de caractères    | Identifiant unique de la commande passée.              |
| `cancel_reason`       | Oui      | Chaîne de caractères    | Raison pour laquelle la commande a été annulée.           |
| `total_value`         | Oui      | float     | Valeur monétaire totale du panier.         |
| `currency`            | Oui      | Chaîne de caractères    | Devise dans laquelle le panier est évalué.           |
| `total_discounts`     | Non       | float     | Montant total des réductions appliquées à la commande.     |
| `discounts`           | Non       | Tableau d’objets     | Liste détaillée des réductions appliquées à la commande.             |
| `products`            | Oui      | Tableau d’objets     |         |
| `product_id`          | Oui      | Chaîne de caractères    | Identifiant unique du produit consulté. Cette valeur peut être l'ID du produit, l'unité de gestion des stocks ou une valeur similaire.             |
| `product_name`        | Oui      | Chaîne de caractères    | Le nom du produit qui a été consulté.          |
| `variant_id`          | Oui      | Chaîne de caractères    | Un identifiant unique pour la variante du produit (tel que `shirt_medium_blue`).        |
| `image_url`           | Non       | Chaîne de caractères    | URL de l'image du produit.           |
| `product_url`         | Non       | Chaîne de caractères    | URL vers la page du produit pour plus de détails.                                                                     |
| `quantity`            | Oui      | Entier   | Nombre d'unités du produit dans le panier.        |
| `price`               | Oui      | float     | Le prix unitaire variante du produit au moment de la consultation.     |
| `metadata`            | Non       | Objet    | Champ de métadonnées supplémentaires sur le produit que le client souhaite ajouter pour ses cas d'utilisation. Pour Shopify, nous ajouterons l'unité de gestion des stocks. Cette limite est basée sur la limite générale de 50 kb fixée pour les propriétés d'un événement. |
| `sku`                 | Non       | Chaîne de caractères    | (Shopify uniquement) Unité de gestion des stocks Shopify. Ce champ peut être configuré comme le champ ID du catalogue.        |
| `source`              | Oui      | Chaîne de caractères    | Source d'où provient l'événement. (Pour Shopify, il s'agit de storefront).    |
| `metadata`            | Non       | Objet    |       |
| `order_status_url`    | Non       | Chaîne de caractères    | URL pour consulter le statut de la commande.                                                                          |
| `order_number`        | Non       | Chaîne de caractères    | (Shopify uniquement) Numéro de commande unique pour la commande passée.  |
| `tags`                | Non       | Tableau     | (Shopify uniquement) Tags de la commande.            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Exemple d'objet

```json
{
    "name": "ecommerce.order_cancelled",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "order_id": "820982911946154508",
        "cancel_reason": "no longer necessary",
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
            ]
        }
    }
}
```

{% endtab %}
{% endtabs %}

## Modèles de canevas pour le commerce électronique

Braze a créé des modèles Canvas préconstruits qui sont alimentés par des événements personnalisés recommandés par l'eCommerce, comme le ciblage des clients qui ont commencé le processus de paiement mais sont partis avant de passer leur commande. Vous pouvez utiliser ces événements pour prendre des décisions éclairées afin d'améliorer votre parcours utilisateur en personnalisant les messages et en ciblant des audiences spécifiques.

Consultez nos [cas d'utilisation dédiés à l'e-commerce]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases) pour savoir comment utiliser ces événements avec les modèles Canvas.

## Champs calculés par l'utilisateur

Nous utilisons des calculs normalisés pour les champs suivants : 

- **Chiffre d'affaires total** = somme de la valeur totale des commandes passées - somme de la valeur totale des commandes remboursées
- **Nombre total de commandes** = nombre d'événements distincts de commandes passées - nombre d'annulations de commandes distinctes
- **Valeur totale du remboursement** = somme de la valeur totale de la commande remboursée 

Ces calculs de champ d'utilisateur sont également inclus dans l'onglet **Transactions** des profils utilisateurs.

![L'onglet "Transactions" avec des champs calculés par l'utilisateur.]({% image_buster /assets/img/Shopify/transactions_tab.png %}){: style="max-width:60%;"}

{% alert important %}
Les plans de suppression progressive de l'événement d'achat seront annoncés à la fin de l'année 2025. À long terme, l'événement d'achat sera remplacé par de nouveaux [événements recommandés par l'eCommerce]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/), qui s'accompagneront de fonctionnalités améliorées en matière de segmentation, de rapports, d'analyse/analyse, etc. Cependant, les nouveaux événements eCommerce ne prendront pas en charge les fonctionnalités existantes liées à l'événement d'achat, telles que la valeur à vie (LTV) ou les rapports sur les chiffres d'affaires dans les Canvases ou les campagnes. Pour une liste complète des fonctionnalités liées aux événements d'achat, veuillez consulter la section sur l'[enregistrement des événements d'achat]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/#logging-purchase-events).
{% endalert %}
