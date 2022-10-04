---
nav_title: "Objet d’achat"
article_title: Objet d’achat de l’API
page_order: 8
page_type: reference
description: "Cet article explique les différents composants d’un objet d’achat, comment l’utiliser correctement et des exemples dont vous pouvez vous inspirer."

---

# Spécification d’objet d’achat

> Cet article explique les différents composants d’un objet d’achat, comment l’utiliser correctement, les bonnes pratiques et des exemples dont vous pouvez vous inspirer.

## Qu’est-ce qu’un objet d’achat ?

Un objet d’achat est un objet qui passe par l’API lorsqu’un achat a été effectué. Chaque objet d’achat est situé dans un tableau d’achat, chaque objet représentant un seul achat par un utilisateur particulier à un moment donné. L’objet d’achat possède de nombreux champs différents qui permettent au backend de Braze de stocker et d’utiliser ces informations pour la personnalisation et la collecte des données.

### Objet d’achat

```json
{
  // One of "external_id" or "user_alias" or "braze_id" is required.
  "external_id" : (optional, string) External User ID,
  "user_alias" : (optional, User Alias Object), User Alias,
  "braze_id" : (optional, string) Braze User Identifier,
  "app_id" : (required, string) see App Identifier,
  // See the following product_id naming conventions for clarification.
  "product_id" : (required, string), identifier for the purchase, e.g., Product Name or Product Category,
  "currency" : (required, string) ISO 4217 Alphabetic Currency Code,
  //Revenue from a purchase object is calculated as the product of quantity and price.
  "price" : (required, float) value in the base currency unit (e.g., Dollars for USD, Yen for JPY),
  "quantity" : (optional, integer) the quantity purchased (defaults to 1, must be <= 100 -- currently, Braze treats a quantity _X_ as _X_ separate purchases with quantity 1),
  "time" : (required, datetime as string in ISO 8601), Time of purchase,
  // Properties stored here are only valid for 30 days.
  // See the following purchase object explanation for clarification.
  "properties" : (optional, Properties Object) properties of the event,
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean)
}
```

- [ID utilisateur externe][23]
- [Identifiant d’application][21]
- [Wiki du code de devise ISO 4217][20]
- [Wiki du code horaire ISO 8601][22]

## Id_acheter un produit

Dans l’objet d’achat, le `product_id` est un identifiant de l’achat (par ex., `Product Name` ou `Product Category`) :

- Braze vous permet de stocker un maximum de 5 000 `product_id` dans le tableau de bord.
- L’`product_id` maximum est de 255 caractères

### Conventions de nommage des ID de produit

Chez Braze, nous proposons des conventions générales de nommage pour l’objet d’achat `product_id`.
Lorsque vous choisissez `product_id`, Braze suggère d’utiliser des noms simples tels que le nom du produit ou la catégorie de produit (au lieu des unités de gestion des stocks) dans l’intention de regrouper tous les éléments enregistrés par ce `product_id`.

Cela permet de faciliter l’identification des produits pour la segmentation et le déclenchement.

## Objet de propriétés d’achat

Les événements et achats personnalisés peuvent avoir des propriétés d’événement. Les valeurs des « propriétés » doivent être un objet dont les clés sont les noms de propriétés et les valeurs sont les valeurs de propriétés. Les noms de propriété doivent être des chaînes de caractères non vides de moins de 255 caractères, qui ne commencent pas un symbole de dollar. 

Les valeurs de propriété peuvent être l’un des types de données suivants :

| Type de données | Description |
| --- | --- |
| Chiffres | Ces attributs peuvent être des [entiers (integer)](https://en.wikipedia.org/wiki/Integer) ou des [floats ](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| Booléens |  |
| Datetimes | Chaînes de caractères au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) ou `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Non pris en charge dans les tableaux. |
| Chaînes de caractères | 255 caractères ou moins. |
| Tableaux | Les tableaux ne peuvent pas inclure des dates/horodatages. |
| Objets | Les objets seront ingérés en tant que chaînes de caractères. |
{: .reset-td-br-1 .reset-td-br-2}

Les objets de propriété d’événement qui contiennent des valeurs de tableau ou d’objet peuvent avoir une charge utile de propriété d’événement de 50 Ko maximum.

### Propriétés d’achat

Les [propriétés d’achat]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#purchase-properties) **ne sont ni** permanentes, ni enregistrées sur le profil d’un utilisateur. Ces propriétés peuvent toutefois être utilisées pour déclencher des messages et pour la personnalisation à l’aide de Liquid, ce qui vous permet également de segmenter (jusqu’à 30 jours) en fonction de ces propriétés. Braze vous permet d’« enregistrer » ces propriétés pendant 30 jours en activant cette fonction de retournement pour maintenir ces propriétés actives et utilisables pour la personnalisation des messages. Pour activer cette fonction dans votre propre groupe d’apps, contactez votre gestionnaire du service client.

Bien que peu fréquent, si vous avez besoin que ces propriétés soient conservées au-delà de la limite de 30 jours, contactez votre gestionnaire du succès des clients ou consultez nos [suggestions de webhooks](#purchase-objects-event-objects-and-webhooks) pour voir comment incorporer des webhooks afin d’enregistrer ces propriétés en tant qu’attributs personnalisés.

### Conventions de nommage des propriétés d’achat

Il est important de noter que cette fonctionnalité est activée **par produit**, et non par achat. Par exemple, si un client a un volume élevé de produits distincts, mais qui ont tous les mêmes propriétés, la segmentation devient plutôt inutile, 

C’est pourquoi, dans ce cas, nous vous recommandons d’utiliser les noms de produits au « niveau du groupe », plutôt que quelque chose de granulaire lors de la définition des structures de données. Par exemple, une société de billetterie doit avoir des produits pour un « aller simple », un « aller-retour », un « multi-ville », et non des transactions spécifiques telles que « transaction 123 », « transaction 046 », etc. Ou, par exemple, avec l’événement d’achat « nourriture », il serait préférable de définir les propriétés comme « gâteau » et « sandwich ».

### Exemple d’objet d’achat
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

## Objets d’achat, objets d’événement et webhooks

À l’aide de l’exemple fourni, nous pouvons voir que quelqu’un a acheté un sac à dos avec les propriétés : couleur, monogramme, durée d’achat, taille et marque. Bien que nous ne puissions pas accéder à une campagne et segmenter les utilisateurs en fonction de ces propriétés, nous pouvons utiliser ces propriétés stratégiquement en les exploitant sous forme de reçu, pour envoyer un message personnalisé via un canal grâce à Liquid. Par exemple, « Bonjour **Ann F.**, Merci d’avoir acheté ce **sac à dos rouge de taille moyenne** pour **40,00 $** ! Merci d’avoir acheté chez **Backpack Locker** !"

Si vous souhaitez enregistrer, stocker et suivre les propriétés avec lesquelles segmenter, vous devez les configurer comme attributs personnalisés. Vous pouvez le faire grâce la puissance des webhooks ! À l’aide des webhooks, vous pouvez dire à Braze d’« écouter » chaque fois qu’un événement d’achat se produit, puis configurer le webhook afin qu’il analyse les propriétés et les enregistre comme attributs personnalisés. Maintenant que ces propriétés sont des attributs personnalisés, nous pouvons voir et segmenter ces propriétés dans le tableau de bord.

Pour plus d’informations sur la configuration de ce type de webhook, consultez [Webhook Braze à Braze][1].

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/
[20]: http://en.wikipedia.org/wiki/ISO_4217 "ISO 4217 Currency Code"
[21]: {{site.baseurl}}/api/api_key/#the-app-identifier-api-key
[22]: https://en.wikipedia.org/wiki/ISO_8601 "ISO 8601 Time Code"
[23]: {{site.baseurl}}/api/basics/#external-user-id-explanation