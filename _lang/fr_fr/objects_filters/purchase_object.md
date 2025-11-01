---
nav_title: "Objet Achat"
article_title: Objet Achat de l’API
page_order: 8
page_type: reference
description: "Cet article de référence explique les différents composants d’un objet Achat, comment l’utiliser correctement et des exemples dont vous pouvez vous inspirer."

---

# Objet Achat

> Cet article explique les différents composants d’un objet Achat, comment l’utiliser correctement, les bonnes pratiques et des exemples dont vous pouvez vous inspirer.

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

## Qu’est-ce qu’un objet Achat ?

Un objet Achat est un objet qui passe par l’API lorsqu’un achat a été effectué. Chaque objet Achat est situé dans un tableau d’achat, chaque objet représentant un seul achat par un utilisateur particulier à un moment donné. L'objet personnalisé comporte de nombreux champs différents qui permettent au backend de Braze de stocker et d'utiliser ces informations à des fins de personnalisation, de collecte de données et de personnalisation.

### Corps de l’objet

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required.
  "external_id" : (optional, string) External user ID,
  "user_alias" : (optional, User Alias Object) User alias object,
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  "app_id" : (optional, string) see App Identifier,
  // See the following product_id naming conventions for clarification.
  "product_id" : (required, string) identifier for the purchase, for example, Product Name or Product Category,
  "currency" : (required, string) ISO 4217 Alphabetic Currency Code,
  //Revenue from a purchase object is calculated as the product of quantity and price.
  "price" : (required, float) value in the base currency unit (for example, Dollars for USD, Yen for JPY),
  "quantity" : (optional, integer) the quantity purchased (defaults to 1, must be <= 100 -- currently, Braze treats a quantity _X_ as _X_ separate purchases with quantity 1),
  "time" : (required, datetime as string in ISO 8601) Time of purchase,
  // See the following purchase object explanation for clarification.
  "properties" : (optional, Properties Object) properties of the event,
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean)
}
```

- [ID utilisateur externe]({{site.baseurl}}/api/basics/#user-ids)
- [Identifiant d’application]({{site.baseurl}}/api/identifier_types/)
- [ISO 4217 Code des devises Wiki](http://en.wikipedia.org/wiki/ISO_4217)
- [ISO 8601 Time Code Wiki](https://en.wikipedia.org/wiki/ISO_8601)

## ID du produit d'achat

Dans l'objet Achat, le `product_id` est un identifiant pour l'achat (tel que `Product Name` ou `Product Category`) :

- Braze vous permet de stocker jusqu'à 5 000 `product_id` dans le tableau de bord.
- Le site `product_id` peut contenir jusqu'à 255 caractères.

### Conventions de nommage

Chez Braze, nous proposons des conventions générales de nommage pour l’objet Achat `product_id`. Lorsque vous choisissez `product_id`, Braze suggère d’utiliser des noms simples tels que le nom du produit ou la catégorie de produit (au lieu des unités de gestion des stocks) dans l’intention de regrouper tous les éléments enregistrés par ce `product_id`.

Cela permet de faciliter l’identification des produits pour la segmentation et le déclenchement.

### Journaliser les achats au niveau de la commande

Si vous souhaitez enregistrer les achats au niveau de la commande plutôt qu'au niveau du produit, vous pouvez utiliser le nom de la commande ou la catégorie de commande comme `product_id` (par exemple `Online Order` ou `Completed Order`).

Par exemple, pour enregistrer des achats au niveau de la commande dans le SDK Web :

```html
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "purchases" : [
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "Completed Order",
      "currency" : "USD",
      "price" : 219.98,
      "time" : "2013-07-16T19:20:30+01:00",
      "properties" : {
        "products" : [ { "name": "Monitor", "category": "Gaming", "product_amount": 19.99, },
        { "name": "Gaming Keyboard", "category": "Gaming ", "product_amount": 199.99, }
        ]
      }
    }
  ]
}
```

## Objet Propriétés d’achat

Les événements et achats personnalisés peuvent avoir des propriétés d’événement. Les valeurs des « Properties (Propriétés) » doivent être un objet dont les clés sont les noms de propriétés et les valeurs sont les valeurs de propriété. Les noms de propriété doivent être des chaînes de caractères non vides de moins de 255 caractères, qui ne commencent pas par un symbole de dollar. 

Les valeurs de propriété peuvent être l’un des types de données suivants :

| Type de données | Description |
| --- | --- |
| Chiffres | Peuvent être des [nombres entiers](https://en.wikipedia.org/wiki/Integer) ou des [floats](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| Booléens |  |
| Datetimes | Formatés sous forme de chaînes de caractères au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) ou `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Non pris en charge dans les tableaux. |
| Chaînes de caractères | 255 caractères ou moins. |
| Tableaux | Les tableaux ne peuvent pas inclure des dates/horodatages. |
| Objets | Les objets seront ingérés en tant que chaînes de caractères. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Les objets de propriété d'événement qui contiennent des valeurs de tableau ou d'objet peuvent avoir une charge utile de propriété d'événement allant jusqu'à 50 Ko.

### Propriétés d’achat

Les [propriétés d'achat]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#purchase-properties) peuvent être utilisées pour déclencher des messages et pour la personnalisation à l'aide de Liquid, ce qui vous permet également de segmenter en fonction de ces propriétés.

#### Conventions de nommage

Il est important de noter que cette fonctionnalité est activée **par produit**, et non par achat. Par exemple, si vous avez un volume élevé de produits distincts, mais que chacun d'entre eux possède les mêmes propriétés, la segmentation peut s'avérer plus inutile.

Dans cette instance, nous vous recommandons d'utiliser des noms de produits au "niveau du groupe" plutôt que quelque chose de granulaire lors de la définition des structures de données. Par exemple, une société de vente de billets de train devrait avoir des produits pour "voyage simple", "voyage aller-retour", "multi-villes", et non des transactions spécifiques telles que la "transaction 123" ou la "transaction 046". Autre exemple, pour l'événement d'achat "nourriture", il serait préférable que les propriétés soient "gâteau" et "sandwich".

{% alert important %}
Notez que les produits peuvent être ajoutés via l'API REST de Braze. Par exemple, si vous envoyez un appel à l'endpoint `/users/track` et que vous incluez un nouvel ID d'achat, un produit sera automatiquement créé dans la section **Paramètres des données** > **Produits** du tableau de bord.
{% endalert %}

### Exemple d’objet Achat

```html
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "purchases" : [
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "backpack",
      "currency" : "USD",
      "price" : 40.00,
      "time" : "2013-07-16T19:20:30+01:00",
      "properties" : {
        "color" : "red",
        "monogram" : "ABC",
        "checkout_duration" : 180,
        "size" : "Large",
        "brand" : "Backpack Locker"
      }
    },
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "pencil",
      "currency" : "USD",
      "price" : 2.00,
      "time" : "2013-07-17T19:20:20+01:00",
      "properties" : {
        "number" : 2,
        "sharpened" : true
      }
    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "pen",
      "currency" : "USD",
      "price" : 2.50,
      "time" : "2013-07-17T19:20:20+01:00",
      "properties" : {
        "color" : "blue",
      }
    }
  ]
}
```

### Objets Achat, objets d’événement et webhooks

À l’aide de l’exemple fourni, nous pouvons voir que quelqu’un a acheté un sac à dos avec les propriétés : couleur, monogramme, durée d’achat, taille et marque. Nous pouvons ensuite créer des segments avec ces propriétés en utilisant les [propriétés d'event d'achat]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#purchase-properties) ou envoyer des messages personnalisés par le biais d'un canal à l'aide de Liquid. Par exemple, « Bonjour **Ann F.**, merci d'avoir acheté ce **sac à dos rouge de taille moyenne** pour **40 euros** ! Merci d'avoir acheté chez **Backpack Locker**!"

Si vous souhaitez enregistrer, stocker et suivre les propriétés avec lesquelles segmenter, vous devez les configurer comme attributs personnalisés. Pour ce faire, vous pouvez utiliser les [extensions de segments]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/), qui vous permettent de cibler les utilisateurs en fonction d'un événement personnalisé ou d'un comportement d'achat stocké pendant toute la durée de vie de ce profil utilisateur.


