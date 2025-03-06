{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Setting custom attributes

Braze provides methods for assigning attributes to users. You'll be able to filter and segment your users according to these attributes on the dashboard.

### Default user attributes

To set user attributes automatically collected by Braze, you can use setter methods that come with the SDK.

```dart
braze.setFirstName('Name');
```

The following attributes are supported:

- First Name
- Last Name
- Gender
- Date of Birth
- Home City
- Country
- Phone Number
- Language
- Email

All string values such as first name, last name, country, and home city are limited to 255 characters.

### Setting custom attribute values

Beyond the default user attributes, Braze also allows you to define custom attributes using a number of different data types:

{% tabs %}
{% tab Boolean Value %}

```dart
braze.setBoolCustomUserAttribute("custom boolean attribute key", boolean);
```

{% endtab %}
{% tab Integer %}

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
{% tab String %}

```dart
braze.setStringCustomUserAttribute("custom string attribute", "string custom attribute");
```

{% endtab %}
{% tab Date %}

```dart
braze.setDateCustomUserAttribute("custom date attribute key", date);
```
{% endtab %}
{% tab Array %}

```dart
// Adding to an Array
braze.addToCustomAttributeArray("key", "attribute");
// Removing an item from an Array
braze.removeFromCustomAttributeArray("key", "attribute");
```
{% endtab %}
{% endtabs %}

### Unsetting a custom attribute

```dart
braze.unsetCustomUserAttribute('attribute_key');
```
