---
nav_title: Analytics
article_title: Analytik für Flutter
platform: Flutter
page_order: 5
description: "In diesem Artikel erfahren Sie, wie Sie grundlegende Analysen in der Flutter-App einrichten und verfolgen können."

---
 
# Flutter-Analytics

> In diesem Artikel erfahren Sie, wie Sie grundlegende Analysen in Ihrer Flutter-App einrichten und verfolgen können.

Bevor Sie beginnen, lesen Sie unseren Artikel [Analytics Overview]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/), um mehr über Braze Analytics zu erfahren und darüber, was bereits standardmäßig aufgezeichnet wird. Wir empfehlen Ihnen auch, sich mit unseren [Namenskonventionen für Events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/) vertraut zu machen.

## Sitzungs-Tracking

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

Um die automatisch von Braze erfassten Nutzerattribute zuzuweisen, können Sie die Setter-Methoden des SDK verwenden.

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

Neben den Standard-Benutzerattributen können Sie in Braze auch benutzerdefinierte Attribute mit einer Reihe verschiedener Datentypen definieren:

{% tabs %}
{% tab Boolescher Wert %}

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

Erfassen Sie In-App-Käufe, um Ihren Umsatz im Zeitverlauf und über verschiedene Umsatzquellen hinweg zu verfolgen und Ihre Nutzer nach ihrem Lifetime-Value zu segmentieren.

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

### Käufe auf der Ebene der Bestellung protokollieren
Wenn Sie Einkäufe auf der Bestellebene statt auf der Produktebene protokollieren möchten, können Sie den Bestellnamen oder die Bestellkategorie als `product_id` verwenden. Weitere Informationen finden Sie in unserer [Spezifikation für Kaufobjekte]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions). 

### Reservierte Tasten

Die folgenden Schlüssel sind reserviert und können nicht als Kaufeigenschaften verwendet werden:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

