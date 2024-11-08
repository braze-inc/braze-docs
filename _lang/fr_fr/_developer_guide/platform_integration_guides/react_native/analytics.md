---
nav_title: Analyse
article_title: Analyses pour React Native
platform: React Native
page_order: 5
description: "Cet article explique comment configurer et suivre les analyses de base comme le suivi de session, la journalisation d’événements personnalisés, etc., dans l’application React Native."

---
 
# Analytiques pour React Native

> Cet article explique comment configurer et suivre les analyses de base dans votre application React Native.

Avant de commencer, lisez notre article [Aperçu des analyses]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/) pour en savoir plus sur l’analyse de Braze et ce qui fait déjà l’objet d’un suivi par défaut. Nous vous recommandons également de vous familiariser avec les [conventions de dénomination de nos événements]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

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
- Genre
- Date de naissance
- Ville d’origine
- Pays
- Numéro de téléphone
- Langue
- E-mail

Toutes les valeurs de chaîne de caractères telles que le prénom, le nom de famille, le pays et la ville d’origine sont limitées à 255 caractères.

### Attributs utilisateur personnalisés

En plus de nos méthodes prédéfinies d'attributs utilisateur, Braze fournit également des [attributs personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types) pour suivre les données de vos applications. 

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
Si vous transmettez une valeur de `10 USD` et une quantité de `3`, trois achats de 10 dollars pour un total de 30 dollars seront enregistrés sur le profil utilisateur. Les quantités doivent être inférieures ou égales à 100. Les valeurs des achats peuvent être négatives.
{% endalert %}

### Journaliser les achats au niveau de la commande
Si vous souhaitez enregistrer les achats au niveau de la commande plutôt qu'au niveau du produit, vous pouvez utiliser le nom de la commande ou la catégorie de commande comme `product_id`. Pour en savoir plus, reportez-vous aux [spécifications de l'objet de l'achat]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions). 

### Clés réservées

Les clés suivantes sont **réservées** et **ne peuvent pas** être utilisées comme propriétés d'achat :

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

