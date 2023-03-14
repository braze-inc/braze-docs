---
nav_title: Analytique
article_title: Analytiques pour React Native
platform: React Native
page_order: 5
description: "Cet article explique comment configurer et suivre l’analytique de base dans l’application React Native."

---
 
# Analytique

Cet article explique comment configurer et suivre l’analytique de base dans votre application React Native.

Avant de commencer, lisez notre article [Aperçu de l’analytique][0] pour en savoir plus sur l’analytique de Braze et ce qui est déjà suivi par défaut. Nous vous recommandons également de vous familiariser avec nos [conventions de dénomination des événements][1].

## Suivi d’une session

Le SDK Braze rapporte les données de session utilisées par le tableau de bord de Braze pour calculer l’engagement des utilisateurs et autres analyses intégrales pour comprendre vos utilisateurs. En fonction des sémantiques de sessions suivants, notre SDK génère des points de données « démarrage de session » et « fin de session » qui comptent pour la longueur de session et le comptage de sessions visibles dans le tableau de bord de Braze.

Pour définir un ID utilisateur ou démarrer une session, utilisez la méthode `changeUser`, qui utilise un paramètre d’ID utilisateur.

```javascript
Braze.changeUser("user_id");
```

## Journalisation des événements personnalisés

Vous pouvez enregistrer des événements personnalisés dans Braze pour en savoir plus sur les modèles d’utilisation de votre application et segmenter vos utilisateurs en fonction de leurs actions dans le tableau de bord.

```javascript
Braze.logCustomEvent("react_native_custom_event");
```

Vous pouvez ajouter des métadonnées à l’événement en transmettant un objet de propriétés avec votre événement personnalisé.

```javascript
Braze.logCustomEvent("custom_event_with_properties", {
    key1: "value1",
    key2: ["value2", "value3"],
    key3: false,
});
```

## Enregistrer des attributs personnalisés

Braze fournit des méthodes pour assigner des attributs aux utilisateurs. Vous pourrez filtrer et segmenter vos utilisateurs en fonction de ces attributs sur le tableau de bord.

### Attributs par défaut de l’utilisateur

Pour assigner automatiquement des attributs d’utilisateur collectés par Braze, vous pouvez utiliser des méthodes d’initiateurs fournies avec le SDK.

```javascript
Braze.setFirstName("Name");
```

Les attributs suivants sont pris en charge :

- Prénom
- Nom
- Sexe
- Date de naissance
- Ville d’origine
- Pays
- Numéro de téléphone
- Langue
- E-mail

Toutes les valeurs de chaîne de caractères telles que le prénom, le nom de famille, le pays et la ville d’origine sont limitées à 255 caractères.

### Attributs utilisateur personnalisés

En plus des attributs utilisateur par défaut, Braze vous permet également de définir des attributs personnalisés vous permettant de définir des attributs personnalisés pour vos utilisateurs. Les types de données pris en charge pour les valeurs incluent `Date`, `Array`, `boolean`, `string`, `number`, et `float`.
Les valeurs de chaîne de caractères ont une longueur maximale de 255 caractères.

```javascript
Braze.setCustomUserAttribute("attribute_key", "attribute_value", function(){
    // optional onResult callback
});
```

#### Enlever la configuration d’un attribut personnalisé


```javascript
Braze.unsetCustomUserAttribute("attribute_key", function(){
    // optional onResult callback
});
```

#### Tableaux d’attribut personnalisé

```javascript

// Adds a string to a custom atttribute string array, or creates that array if one doesn't exist.
Braze.addToCustomUserAttributeArray("my-attribute-array", "new or existing value", optionalCallback);

// Removes a string from a custom attribute string array.


Braze.removeFromCustomUserAttributeArray("my-attribute-array", "existing value", optionalCallback);
```

## Enregistrer les achats

Enregistrez les achats dans l’application afin que vous puissiez suivre vos revenus au fil du temps et entre leurs différentes sources, tout en segmentant vos utilisateurs selon leur valeur à vie.

Braze prend en charge les achats dans plusieurs devises. Les achats que vous effectuez dans une devise autre qu’USD seront affichés dans le tableau de bord en USD en fonction du taux de change à la date à laquelle ils ont été enregistrés.

```javascript
Braze.logPurchase(productId, price, currencyCode, quantity, properties);
```

Par exemple :

```javascript
Braze.logPurchase("product_id", 9.99, "USD", 1, {
    key1: "value"
});
```

{% alert tip %}
Si vous transmettez une valeur de `10 USD` et une quantité de `3`, trois achats de 10 dollars pour un total de 30 dollars seront enregistrés sur le profil utilisateur. Les quantités doivent être inférieures ou égales à 100. Les valeurs des achats peuvent être négatives.
{% endalert %}

### Journaliser les achats au niveau de la commande
Si vous souhaitez journaliser les achats au niveau de la commande au lieu du niveau de produit, vous pouvez utiliser le nom de la commande ou la catégorie de commande comme `product_id`. Consultez notre [spécification d’objet d’achat]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) pour en savoir plus. 

### Clés réservées

Les clés suivantes sont **réservées** et **ne peuvent pas** être utilisées comme propriétés d’achat :

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

[0]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/
[1]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/
