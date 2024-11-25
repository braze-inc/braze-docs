---
nav_title: Analyse
article_title: Analyses pour Flutter
platform: Flutter
page_order: 5
description: "Cet article explique comment configurer et suivre les analyses de base dans l’application Flutter."

---
 
# Analytique pour Flutter

> Cet article explique comment configurer et suivre les analyses de base dans votre application Flutter.

Avant de commencer, lisez notre article [Aperçu des analyses]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/) pour en savoir plus sur l’analyse de Braze et ce qui fait déjà l’objet d’un suivi par défaut. Nous vous recommandons également de vous familiariser avec les [conventions de dénomination de nos événements]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Suivi d’une session

Le SDK Braze rapporte les données de session utilisées par le tableau de bord de Braze pour calculer l’engagement des utilisateurs et d’autres analyses essentielles à une meilleure connaissance de vos utilisateurs. Sur la base de la sémantique de session suivante, notre SDK génère des points de données « démarrage de la session » et « fin de la session » qui comptent pour la longueur de session et le nombre de sessions visibles dans le tableau de bord de Braze.

Pour définir un ID utilisateur ou démarrer une session, utilisez la méthode `changeUser`, qui utilise un paramètre d’ID utilisateur.

```dart
braze.changeUser('user_id');
```

## Journalisation des événements personnalisés

Vous pouvez enregistrer des événements personnalisés dans Braze pour en savoir plus sur les modèles d’utilisation de votre application et segmenter vos utilisateurs en fonction de leurs actions dans le tableau de bord.

```dart
braze.logCustomEvent('my_custom_event');
```

Vous pouvez ajouter des métadonnées à l’événement en transmettant un objet de propriétés avec votre événement personnalisé.

```dart
braze.logCustomEvent('custom_event_with_properties', properties: {
    'key1': 'value1',
    'key2': ['value2', 'value3'],
    'key3': false,
});
```

## Enregistrer des attributs personnalisés

Braze fournit des méthodes pour assigner des attributs aux utilisateurs. Vous pourrez filtrer et segmenter vos utilisateurs en fonction de ces attributs sur le tableau de bord.

### Attributs par défaut de l’utilisateur

Pour assigner automatiquement des attributs d’utilisateur collectés par Braze, vous pouvez utiliser des méthodes d’initiateurs fournies avec le SDK.

```dart
braze.setFirstName('Name');
```

Les attributs suivants sont pris en charge :

- Prénom
- Nom
- Genre
- Date de naissance
- Ville d’origine
- Pays
- Numéro de téléphone
- Langue
- E-mail

Toutes les valeurs de chaîne de caractères telles que le prénom, le nom de famille, le pays et la ville d’origine sont limitées à 255 caractères.

### Définir des valeurs d’attributs personnalisés

Au-delà des attributs utilisateur par défaut, Braze vous permet également de définir des attributs personnalisés en utilisant un certain nombre de types de données différents :

{% tabs %}
{% tab Valeur booléenne %}

```dart
braze.setBoolCustomUserAttribute("custom boolean attribute key", boolean);
```

{% endtab %}
{% tab Entier %}

```dart
// Set Integer Attribute
braze.setIntCustomUserAttribute("custom int attribute key", integer);
// Increment Integer Attribute
braze.incrementCustomUserAttribute("key", integer);
```

{% endtab %}
{% tab Double %}
```dart
braze.setDoubleCustomUserAttribute("custom double attribute key", double);
```

{% endtab %}
{% tab Chaîne de caractères %}

```dart
braze.setStringCustomUserAttribute("custom string attribute", "string custom attribute");
```

{% endtab %}
{% tab Date %}

```dart
braze.setDateCustomUserAttribute("custom date attribute key", date);
```
{% endtab %}
{% tab Réseau %}

```dart
// Adding to an Array
braze.addToCustomAttributeArray("key", "attribute");
// Removing an item from an Array
braze.removeFromCustomAttributeArray("key", "attribute");
```
{% endtab %}
{% endtabs %}

### Enlever la configuration d’un attribut personnalisé

```dart
braze.unsetCustomUserAttribute('attribute_key');
```

## Enregistrer les achats

Enregistrez les achats dans l’application afin que vous puissiez suivre vos revenus au fil du temps et entre leurs différentes sources, tout en segmentant vos utilisateurs selon leur valeur à vie.

Braze prend en charge les achats dans plusieurs devises. Les achats que vous effectuez dans une devise autre qu’USD seront affichés dans le tableau de bord en USD en fonction du taux de change à la date à laquelle ils ont été enregistrés.

```dart
braze.logPurchase(productId, currencyCode, price, quantity, properties: properties);
```

Par exemple :

```dart
braze.logPurchase('product_id', 'USD', 9.99, 1, properties: {
    'key1': 'value'
});
```

{% alert tip %}
Si vous transmettez une valeur de `10 USD` et une quantité de `3`, trois achats de 10 dollars pour un total de 30 dollars seront enregistrés sur le profil utilisateur. Les quantités doivent être inférieures ou égales à 100. Les valeurs des achats peuvent être négatives.
{% endalert %}

### Journaliser les achats au niveau de la commande
Si vous souhaitez enregistrer les achats au niveau de la commande plutôt qu'au niveau du produit, vous pouvez utiliser le nom de la commande ou la catégorie de commande comme `product_id`. Pour en savoir plus, reportez-vous aux [spécifications de l'objet de l'achat]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions). 

### Clés réservées

Les clés suivantes sont réservées et ne peuvent pas être utilisées comme propriétés d’achat :

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

