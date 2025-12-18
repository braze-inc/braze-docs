{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Standard-Nutzerattribute

### Unterstützte Attribute

Die folgenden Attribute werden unterstützt:

- Vorname
- Nachname
- Geschlecht
- Geburtsdatum
- Heimatstadt
- Land
- Telefonnummer
- Sprache
- E-Mail

{% alert important %}
Alle String-Werte wie Vorname, Nachname, Land und Wohnort sind auf 255 Zeichen begrenzt.
{% endalert %}

### Einstellung von Standardattributen 

Um Nutzer:innen-Attribute zu setzen, die von Braze automatisch erfasst werden, können Sie die im SDK enthaltenen Setter-Methoden verwenden.

```dart
braze.setFirstName('Name');
```

## Angepasste Nutzerattribute

### Anpassen der Attribute

Zusätzlich zu den standardmäßigen Nutzer:innen-Attributen können Sie in Braze auch angepasste Attribute unter Verwendung einer Reihe verschiedener Datentypen definieren:

{% tabs %}
{% tab String %}
So legen Sie ein angepasstes Attribut mit einem `string` Wert fest:

```dart
braze.setStringCustomUserAttribute("custom string attribute", "string custom attribute");
```

{% endtab %}
{% tab Integer %}
So passen Sie ein angepasstes Attribut mit einem `integer` Wert an:

```dart
// Set Integer Attribute
braze.setIntCustomUserAttribute("custom int attribute key", integer);
// Increment Integer Attribute
braze.incrementCustomUserAttribute("key", integer);
```

{% endtab %}
{% tab Double %}
So legen Sie ein angepasstes Attribut mit einem `double` Wert fest:

```dart
braze.setDoubleCustomUserAttribute("custom double attribute key", double);
```

{% endtab %}
{% tab Boolesch %}
So legen Sie ein angepasstes Attribut mit einem `boolean` Wert fest:

```dart
braze.setBoolCustomUserAttribute("custom boolean attribute key", boolean);
```
{% endtab %}

{% tab Datum %}
So legen Sie ein angepasstes Attribut mit einem `date` Wert fest:

```dart
braze.setDateCustomUserAttribute("custom date attribute key", date);
```
{% endtab %}
{% tab Array %}
So passen Sie ein angepasstes Attribut mit einem `array` Wert an:

```dart
// Adding to an Array
braze.addToCustomAttributeArray("key", "attribute");
// Removing an item from an Array
braze.removeFromCustomAttributeArray("key", "attribute");
```
{% endtab %}
{% endtabs %}

{% alert important %}
Angepasste Attributwerte haben eine maximale Länge von 255 Zeichen; längere Werte werden abgeschnitten.
{% endalert %}

### Angepasste Attribute nicht anpassen

Um ein angepasstes Attribut wieder freizugeben, übergeben Sie den entsprechenden Attributschlüssel an die Methode `unsetCustomUserAttribute`.

```dart
braze.unsetCustomUserAttribute('attribute_key');
```
