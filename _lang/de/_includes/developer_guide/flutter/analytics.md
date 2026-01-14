{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Session-Tracking

Das Braze SDK meldet Sitzungsdaten, die vom Braze Dashboard verwendet werden, um das Nutzer-Engagement und andere Analysen zu berechnen, die für das Verständnis Ihrer Nutzer wichtig sind. Auf der Grundlage der folgenden Sitzungssemantik generiert unser SDK Datenpunkte für "Sitzungsbeginn" und "Sitzungsende", die die Sitzungsdauer und die Anzahl der Sitzungen berücksichtigen, die im Braze-Dashboard angezeigt werden.

Um eine Nutzer-ID festzulegen oder eine Sitzung zu starten, verwenden Sie die Methode `changeUser`, die einen Parameter für die Nutzer-ID benötigt.

```dart
braze.changeUser('user_id');
```

## Protokollierung benutzerdefinierter Ereignisse

Sie können in Braze benutzerdefinierte Ereignisse aufzeichnen, um mehr über die Nutzungsmuster Ihrer App zu erfahren und Ihre Benutzer nach ihren Aktionen im Dashboard zu segmentieren.

```dart
braze.logCustomEvent('my_custom_event');
```

Sie können Metadaten über das Event hinzufügen, indem Sie ein Eigenschaften-Objekt mit Ihrem angepassten Event übergeben.

```dart
braze.logCustomEvent('custom_event_with_properties', properties: {
    'key1': 'value1',
    'key2': ['value2', 'value3'],
    'key3': false,
});
```

## Benutzerdefinierte Attribute protokollieren

Braze bietet Methoden für die Zuweisung von Attributen an Benutzer. Auf dem Dashboard können Sie Ihre Benutzer nach diesen Attributen filtern und segmentieren.

### Standard-Nutzerattribute

Um Nutzer:innen-Attribute zu setzen, die von Braze automatisch gesammelt werden, können Sie die Setter-Methoden verwenden, die mit dem SDK geliefert werden.

```dart
braze.setFirstName('Name');
```

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

Alle String-Werte wie Vorname, Nachname, Land und Heimatort sind auf 255 Zeichen begrenzt.

### Benutzerdefinierte Attributwerte festlegen

Zusätzlich zu den standardmäßigen Nutzer:innen-Attributen können Sie in Braze auch angepasste Attribute unter Verwendung einer Reihe verschiedener Datentypen definieren:

{% tabs %}
{% tab Boolesch %}

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
{% tab Datum %}

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

### Zurücksetzen eines benutzerdefinierten Attributs

```dart
braze.unsetCustomUserAttribute('attribute_key');
```

## Einkäufe protokollieren

Erfassen Sie In-App-Käufe, damit Sie Ihre Einnahmen im Laufe der Zeit und über verschiedene Einnahmequellen hinweg verfolgen und Ihre Nutzer nach ihrem Lifetime-Value segmentieren können.

Braze unterstützt Einkäufe in mehreren Währungen. Einkäufe, die Sie in einer anderen Währung als dem USD melden, werden im Dashboard in USD auf der Grundlage des Wechselkurses an dem Tag, an dem sie gemeldet wurden, angezeigt.

```dart
braze.logPurchase(productId, currencyCode, price, quantity, properties: properties);
```

Zum Beispiel:

```dart
braze.logPurchase('product_id', 'USD', 9.99, 1, properties: {
    'key1': 'value'
});
```

{% alert tip %}
Wenn Sie einen Wert von `10 USD` und eine Menge von `3` eingeben, werden drei Käufe zu je 10 Dollar für insgesamt 30 Dollar in das Profil des Benutzers eingetragen. Die Mengen müssen kleiner als oder gleich 100 sein. Die Werte von Käufen können negativ sein.
{% endalert %}

### Tracking auf der Ebene der Bestellung
Wenn Sie Einkäufe auf der Bestellebene statt auf der Produktebene protokollieren möchten, können Sie den Bestellnamen oder die Bestellkategorie als `product_id` verwenden. Weitere Informationen finden Sie in unserer [Spezifikation für Kaufobjekte]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions). 

### Reservierte Tasten

Die folgenden Schlüssel sind reserviert und können nicht als Kaufeigenschaften verwendet werden:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

