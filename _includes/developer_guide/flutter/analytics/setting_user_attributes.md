{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Default user attributes

### Supported attributes

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

{% alert important %}
All string values such as first name, last name, country, and home city are limited to 255 characters.
{% endalert %}

### Setting default attributes 

To set user attributes automatically collected by Braze, you can use the setter methods included with the SDK.

```dart
braze.setFirstName('Name');
```

## Custom user attributes

### Setting custom attributes

In addition to the default user attributes, Braze also allows you to define custom attributes using a number of different data types:

{% tabs %}
{% tab String %}
To set a custom attribute with a `string` value:

```dart
braze.setStringCustomUserAttribute("custom string attribute", "string custom attribute");
```

{% endtab %}
{% tab Integer %}
To set a custom attribute with an `integer` value:

```dart
// Set Integer Attribute
braze.setIntCustomUserAttribute("custom int attribute key", integer);
// Increment Integer Attribute
braze.incrementCustomUserAttribute("key", integer);
```

{% endtab %}
{% tab Double %}
To set a custom attribute with a `double` value:

```dart
braze.setDoubleCustomUserAttribute("custom double attribute key", double);
```

{% endtab %}
{% tab Boolean %}
To set a custom attribute with a `boolean` value:

```dart
braze.setBoolCustomUserAttribute("custom boolean attribute key", boolean);
```
{% endtab %}

{% tab Date %}
To set a custom attribute with a `date` value:

```dart
braze.setDateCustomUserAttribute("custom date attribute key", date);
```
{% endtab %}
{% tab Array %}
To set a custom attribute with an `array` value:

```dart
// Adding to an Array
braze.addToCustomAttributeArray("key", "attribute");
// Removing an item from an Array
braze.removeFromCustomAttributeArray("key", "attribute");
```
{% endtab %}
{% endtabs %}

{% alert important %}
Custom attribute values have a maximum length of 255 characters; longer values will be truncated.
{% endalert %}

### Unsetting custom attributes

To unset a custom attribute, pass the relevant attribute key to the `unsetCustomUserAttribute` method.

```dart
braze.unsetCustomUserAttribute('attribute_key');
```
