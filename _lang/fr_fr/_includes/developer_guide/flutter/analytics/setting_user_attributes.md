{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Attributs par défaut de l’utilisateur

### Attributs pris en charge

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

{% alert important %}
Toutes les valeurs de chaîne de caractères telles que le prénom, le nom de famille, le pays et la ville d’origine sont limitées à 255 caractères.
{% endalert %}

### Définition des attributs par défaut 

Pour définir les attributs utilisateur collectés automatiquement par Braze, vous pouvez utiliser les méthodes setter incluses dans le SDK.

```dart
braze.setFirstName('Name');
```

## Attributs utilisateur personnalisés

### Définition des attributs personnalisés

Outre les attributs par défaut, Braze vous permet de définir des attributs personnalisés à l'aide de différents types de données :

{% tabs %}
{% tab Chaîne de caractères %}
Pour définir un attribut personnalisé avec une valeur `string`:

```dart
braze.setStringCustomUserAttribute("custom string attribute", "string custom attribute");
```

{% endtab %}
{% tab Entier %}
Pour définir un attribut personnalisé avec une valeur `integer`:

```dart
// Set Integer Attribute
braze.setIntCustomUserAttribute("custom int attribute key", integer);
// Increment Integer Attribute
braze.incrementCustomUserAttribute("key", integer);
```

{% endtab %}
{% tab Double %}
Pour définir un attribut personnalisé avec une valeur `double`:

```dart
braze.setDoubleCustomUserAttribute("custom double attribute key", double);
```

{% endtab %}
{% tab Booléen %}
Pour définir un attribut personnalisé avec une valeur `boolean`:

```dart
braze.setBoolCustomUserAttribute("custom boolean attribute key", boolean);
```
{% endtab %}

{% tab Date %}
Pour définir un attribut personnalisé avec une valeur `date`:

```dart
braze.setDateCustomUserAttribute("custom date attribute key", date);
```
{% endtab %}
{% tab Réseau %}
Pour définir un attribut personnalisé avec une valeur `array`:

```dart
// Adding to an Array
braze.addToCustomAttributeArray("key", "attribute");
// Removing an item from an Array
braze.removeFromCustomAttributeArray("key", "attribute");
```
{% endtab %}
{% endtabs %}

{% alert important %}
Les valeurs d’attribut personnalisé ont une longueur maximale de 255 caractères ; les valeurs plus longues seront tronquées.
{% endalert %}

### Désactivation des attributs personnalisés

Pour désactiver un attribut personnalisé, transmettez la clé de l'attribut concerné à la méthode `unsetCustomUserAttribute`.

```dart
braze.unsetCustomUserAttribute('attribute_key');
```
