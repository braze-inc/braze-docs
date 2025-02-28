---
nav_title: Analytics
article_title: Analytics für React Native
platform: React Native
page_order: 5
description: "In diesem Artikel erfahren Sie, wie Sie grundlegende Analytics wie Session Tracking, die Protokollierung angepasster Events und mehr in der React Native App einrichten und verfolgen können."

---
 
# React Native Analytics

> Dieser Artikel beschreibt, wie Sie grundlegende Analytics in Ihrer React Native App einrichten und tracken.

Bevor Sie beginnen, lesen Sie unseren Artikel [Analytics Overview]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/), um mehr über Braze Analytics zu erfahren und darüber, was bereits standardmäßig aufgezeichnet wird. Wir empfehlen Ihnen auch, sich mit unseren [Namenskonventionen für Events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/) vertraut zu machen.

## Session-Tracking

Das Braze SDK meldet Sitzungsdaten, die vom Braze-Dashboard verwendet werden, um das Nutzer-Engagement und andere Analysen zu berechnen, die für das Verständnis Ihrer Nutzer:innen unerlässlich sind. Basierend auf der folgenden Sitzungssemantik generiert unser SDK Datenpunkte für "start session" und "close session", die die Sitzungslänge und die Anzahl der Sitzungen berücksichtigen, die im Braze-Dashboard angezeigt werden.

Um eine Nutzer-ID festzulegen oder eine Sitzung zu starten, verwenden Sie die Methode `changeUser`, die einen Parameter für die Nutzer-ID benötigt.

```javascript
Braze.changeUser("user_id");
```

## Protokollierung benutzerdefinierter Ereignisse

Sie können in Braze benutzerdefinierte Ereignisse aufzeichnen, um mehr über die Nutzungsmuster Ihrer App zu erfahren und Ihre Benutzer nach ihren Aktionen im Dashboard zu segmentieren.

```javascript
Braze.logCustomEvent("react_native_custom_event");
```

Sie können Metadaten über das Event hinzufügen, indem Sie ein Eigenschaften-Objekt mit Ihrem angepassten Event übergeben.

```javascript
Braze.logCustomEvent("custom_event_with_properties", {
    key1: "value1",
    key2: ["value2", "value3"],
    key3: false,
});
```

## Benutzerdefinierte Attribute protokollieren

Braze bietet Methoden für die Zuweisung von Attributen an Benutzer. Auf dem Dashboard können Sie Ihre Benutzer nach diesen Attributen filtern und segmentieren.

### Standard-Nutzerattribute

Um die automatisch von Braze erfassten Nutzerattribute zuzuweisen, können Sie die Setter-Methoden des SDK verwenden.

```javascript
Braze.setFirstName("Name");
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

Alle String-Werte wie Vorname, Nachname, Land und Wohnort sind auf 255 Zeichen begrenzt.

### Angepasste Nutzerattribute

Zusätzlich zu unseren vordefinierten Methoden für Benutzerattribute bietet Braze auch [benutzerdefinierte Attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types), um Daten aus Ihren Anwendungen zu verfolgen. 

```javascript
Braze.setCustomUserAttribute("attribute_key", "attribute_value", function(){
    // optional onResult callback
});
```

#### Zurücksetzen eines benutzerdefinierten Attributs


```javascript
Braze.unsetCustomUserAttribute("attribute_key", function(){
    // optional onResult callback
});
```

#### Angepasste Attribut-Arrays

```javascript

// Adds a string to a custom atttribute string array, or creates that array if one doesn't exist.
Braze.addToCustomUserAttributeArray("my-attribute-array", "new or existing value", optionalCallback);

// Removes a string from a custom attribute string array.


Braze.removeFromCustomUserAttributeArray("my-attribute-array", "existing value", optionalCallback);
```

## Einkäufe protokollieren

Erfassen Sie In-App-Käufe, um Ihren Umsatz im Zeitverlauf und über verschiedene Umsatzquellen hinweg zu verfolgen und Ihre Nutzer:innen nach ihrem Lifetime-Value zu segmentieren.

Braze unterstützt Einkäufe in mehreren Währungen. Einkäufe, die Sie in einer anderen Währung als dem USD melden, werden im Dashboard in USD auf der Grundlage des Wechselkurses an dem Tag, an dem sie gemeldet wurden, angezeigt.

```javascript
Braze.logPurchase(productId, price, currencyCode, quantity, properties);
```

Zum Beispiel:

```javascript
Braze.logPurchase("product_id", 9.99, "USD", 1, {
    key1: "value"
});
```

{% alert tip %}
Wenn Sie einen Wert von `10 USD` und eine Menge von `3` eingeben, werden drei Käufe zu je 10 Dollar für insgesamt 30 Dollar in das Profil des Benutzers eingetragen. Die Mengen müssen kleiner als oder gleich 100 sein. Die Werte von Käufen können negativ sein.
{% endalert %}

### Käufe auf der Ebene der Bestellung protokollieren
Wenn Sie Einkäufe auf der Bestellebene statt auf der Produktebene protokollieren möchten, können Sie den Bestellnamen oder die Bestellkategorie als `product_id` verwenden. Weitere Informationen finden Sie in unserer [Spezifikation für Kaufobjekte]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions). 

### Reservierte Schlüssel

Die folgenden Schlüssel sind **reserviert** und können **nicht** als Kauf-Details verwendet werden:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

