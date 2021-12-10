---
nav_title: "Objet d'achat"
article_title: Objet d'achat de l'API
page_order: 8
page_type: Référence
description: "Cet article explique les différents composants d'un objet d'achat, comment l'utiliser correctement, et des exemples à en tirer."
---

# Spécification de l'objet d'achat

> Cet article explique les différents composants d'un objet d'achat, comment l'utiliser correctement, les meilleures pratiques et les exemples à en tirer.

## Qu'est-ce qu'un objet d'achat?

Un objet Achat est un objet qui passe par l'API lorsqu'un achat a été effectué. Chaque objet d'achat se trouve dans un tableau d'achat, chaque objet étant un seul achat par un utilisateur particulier à un moment donné. L'objet d'achat a de nombreux champs différents qui permettent à Braze de stocker et d'utiliser ces informations pour la personnalisation, la collecte de données et la personnalisation.

### Acheter un objet

```json
{
  // Un de "external_id" ou "user_alias" ou "braze_id" est requis.
  "external_id" : (optionnel, string) ID utilisateur externe,
  "user_alias" : (optionnel, objet alias utilisateur), alias utilisateur,
  "braze_id" : (optionnel, string) Braze Identificateur d'utilisateur,
  "app_id" : (requis, chaîne) voir Identifiant de l'application ci-dessous,
  // Veuillez voir les conventions de nommage product_id ci-dessous pour plus de précisions.
  "product_id" : (obligatoire, chaîne), identifiant pour l'achat, e.g. Nom du produit ou catégorie du produit,
  "devise" : (obligatoire, chaîne) ISO 4217 Code de la devise alphabétique,
  //Le produit d'un objet d'achat est calculé comme le produit de la quantité et du prix.
  « prix» : (obligatoire, float) valeur dans l'unité de la devise de base (par ex. Dollars pour USD, Yen pour JPY),
  "quantité" : (facultatif, integer) la quantité achetée (par défaut 1, doit être <= 100 -- actuellement, Le braze traite une quantité _X_ en _X_ avec la quantité 1),
  "temps" : (obligatoire, datetime en tant que chaîne dans ISO 8601), Heure d'achat,
  // Les propriétés stockées ici ne sont valides que pour 30 jours.
  // Veuillez consulter l’explication d’achat de l’objet ci-dessous pour plus de précisions.
  "properties" : (optionnel, Properties Object) des propriétés de l'événement,
  // Mettre ce drapeau à true mettra l'API en mode "Update only".
  // Lorsque vous utilisez un "user_alias", le mode "Update only" est toujours vrai.
  "_update_existing_only" : (optionnel, booléen)
}
```

- [Wiki du code de devise ISO 4217][20]
- [ISO 8601 Time Code Wiki][22]
- [App Identifier][21]

## ID du produit d'achat

Dans l'objet d'achat, le `product_id` est un identifiant pour l'achat, par exemple le nom du produit ou la catégorie du produit
- Braze vous permet de stocker un maximum de 5000 `product_id`s dans le tableau de bord.
- `product_id` le maximum est de 255 caractères

### Conventions de nommage des identifiants de produit

Chez Braze, nous offrons quelques conventions de nommage générales pour l'objet d'achat `product_id`. En choisissant `product_id`, Braze suggère d'utiliser des noms simplistes tels que le nom du produit ou la catégorie de produit (au lieu des REFs) dans l'intention de regrouper tous les éléments logués par ce `product_id`.

Cela aide à faciliter l'identification des produits pour la segmentation et le déclenchement.

## Acheter un objet de propriétés

Les événements personnalisés et les achats peuvent avoir des propriétés d'événement. Les valeurs « propriétés » doivent être un objet où les clés sont les noms de propriété et les valeurs sont les valeurs de la propriété. Les noms de propriété doivent être des chaînes de caractères non vides inférieures ou égales à 255 caractères, sans signe de dollar principal.

Les valeurs de la propriété peuvent être l'un des types de données suivants :

| Type de données       | Libellé                                                                                                                                                        |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Numéros               | En tant que [entiers](https://en.wikipedia.org/wiki/Integer) ou [flottent](https://en.wikipedia.org/wiki/Floating-point_arithmetic)                            |
| Booléens              |                                                                                                                                                                |
| Datetimes             | Formaté en tant que chaînes au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) ou `yyyy-MM-dd'T'H:mm:ss:SSSZ`. Non pris en charge dans les tableaux. |
| Chaînes de caractères | 255 caractères ou moins.                                                                                                                                       |
| Tableaux              | Les tableaux ne peuvent pas inclure les dates.                                                                                                                 |
| Objets                | Les objets seront ingérés en tant que chaînes.                                                                                                                 |
{: .reset-td-br-1 .reset-td-br-2}

Les objets de propriété événement qui contiennent des valeurs de tableau ou d'objet peuvent avoir une charge utile de propriété événement allant jusqu'à 50 Ko.

### Propriétés de l'achat

[Les propriétés d'achat]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#purchase-properties) __ne persistent pas__ et ne sont pas enregistrées sur le profil d'un utilisateur. Ces propriétés peuvent cependant être utilisées pour déclencher des messages et pour la personnalisation à l'aide de Liquid, vous permettant également de segmenter (jusqu'à 30 jours) en fonction de ces propriétés. Braze vous permet de "sauvegarder" ces propriétés pendant 30 jours en activant cette fonction pour garder ces propriétés vivantes et utilisables pour la personnalisation des messages. Pour activer cette fonctionnalité dans votre propre groupe d'applications, contactez votre responsable du service client.

Bien qu'inhabituel, si vous avez besoin de ces propriétés pour persister au-delà de la limite de 30 jours, contactez votre Responsable du Service Clientèle ou, voir nos suggestions de webhooks ci-dessous pour voir comment vous pouvez incorporer des webhooks pour enregistrer ces propriétés en tant qu'attributs personnalisés.

### Acheter des conventions de nommage de propriété

Il est important de noter que cette fonctionnalité est activée __par produit__, pas par achat. Par exemple, si un client a un volume élevé de produits distincts, mais que chacun a les mêmes propriétés, la segmentation devient plutôt dénuée de sens.

Dans ce cas, c'est pourquoi lors de la configuration des structures de données, nous recommandons d'utiliser les noms de produits au niveau du "groupe" au lieu de quelque chose de granulaire. Par exemple, une compagnie de billets de train devrait avoir des produits pour "un seul voyage", "un aller-retour", "multi-ville", et non des transactions spécifiques telles que "transaction 123", "transaction 046", etc. Ou par exemple, avec l'événement d'achat «nourriture», les propriétés seraient mieux placées comme «gâteau» et «sandwich».

### Exemple d'objet d'achat
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
      "price" : 40. 0,
      "temps" : "2013-07-16T19:20:30+01:00",
      "properties" : {
        "color" : "red",
        "monogramme" : "ABC",
        "checkout_duration" : 180,
        "size" : "Large",
        "marque" : "Bloqueur de sac à dos"
      }
    },
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "crayon",
      "currency" : "USD",
      "prix" : 2. 0,
      "temps" : "2013-07-17T19:20:20+01:00",
      "properties" : {
        "number" : 2,
        "aiguisé" : vrai
      }
    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "mon_device_identifier"},
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "stylo",
      "currency" : "USD",
      "prix" : 2. 0,
      "temps" : "2013-07-17T19:20:20+01:00",
      "properties" : {
        "color" : "blue",
      }
    }
  ]
}
```

## Acheter des objets, des objets événementiels et des webhooks

En utilisant l'exemple ci-dessus, nous pouvons voir que quelqu'un a acheté un sac à dos avec les propriétés : couleur, monogramme, durée de la commande, taille et marque. Bien que nous ne puissions pas entrer dans une campagne et segmenter les utilisateurs en fonction de ces propriétés, nous pouvons utiliser ces propriétés stratégiquement en les utilisant sous la forme d'un reçu, pour envoyer un message personnalisé via un canal à l'aide de Liquid. Par exemple, "Bonjour __Ann F.__, Merci d'avoir acheté ce __rouge, sac à dos moyen__ pour __40,00 $__! Merci pour vos achats dans __Backpack Locker__!

Si vous voulez sauvegarder, stocker et suivre les propriétés dans un segment, vous devez les configurer en tant qu'attributs personnalisés. Cela peut être fait avec la puissance des webhooks ! Utilisation de webhooks, vous pouvez dire à Braze de "écouter" quand un événement d'achat se produit, puis de configurer le webhook pour qu'il analyse les propriétés et les sauvegarde en tant qu'attributs personnalisés. Maintenant que ces propriétés sont des attributs personnalisés, nous pouvons voir et segmenter ces propriétés dans le tableau de bord.

Pour plus d'informations sur la façon de configurer les webhooks, consultez notre documentation [Webhook][1].

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
[20]: http://en.wikipedia.org/wiki/ISO_4217 "Code de devise ISO 4217"
[21]: {{site.baseurl}}/api/api_key/#the-app-identifier-api-key
[22]: https://en.wikipedia.org/wiki/ISO_8601 "ISO 8601 Time Code"