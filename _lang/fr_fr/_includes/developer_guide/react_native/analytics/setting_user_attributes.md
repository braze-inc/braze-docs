{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Enregistrer des attributs personnalisés

Braze fournit des méthodes pour assigner des attributs aux utilisateurs. Vous pourrez filtrer et segmenter vos utilisateurs en fonction de ces attributs sur le tableau de bord.

### Attributs par défaut de l’utilisateur

Pour définir les attributs utilisateur collectés automatiquement par Braze, vous pouvez utiliser les méthodes setter fournies avec le SDK.

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

#### Désactivation des attributs personnalisés

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
