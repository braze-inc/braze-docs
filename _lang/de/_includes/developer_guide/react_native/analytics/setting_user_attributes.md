{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Benutzerdefinierte Attribute protokollieren

Braze bietet Methoden für die Zuweisung von Attributen an Benutzer. Auf dem Dashboard können Sie Ihre Benutzer nach diesen Attributen filtern und segmentieren.

### Standard-Nutzerattribute

Um Nutzer:innen-Attribute zu setzen, die von Braze automatisch gesammelt werden, können Sie die Setter-Methoden verwenden, die mit dem SDK geliefert werden.

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

#### Angepasste Attribute nicht anpassen

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
