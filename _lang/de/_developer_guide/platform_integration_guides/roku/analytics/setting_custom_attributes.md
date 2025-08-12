---
nav_title: Benutzerdefinierte Attribute einstellen
article_title: Anpassen von Attributen für Roku
platform: Roku
page_order: 4
page_type: reference
description: "Dieser referenzierte Artikel beschreibt Methoden, um Nutzern angepasste Attribute für Roku über das Braze SDK zuzuweisen."

---

# Benutzerdefinierte Attribute einstellen

> Braze bietet Methoden für die Zuweisung von Attributen an Benutzer. Auf dem Dashboard können Sie Ihre Benutzer nach diesen Attributen filtern und segmentieren.

Lesen Sie vor der Implementierung unbedingt in unseren [Best Practices]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection) die Beispiele für die Segmentierungsoptionen von angepassten Events, Nutzerattributen und Kauf-Events. Wir empfehlen auch, sich mit unseren [Event-Benennungskonventionen]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/) vertraut zu machen.

## Zuweisen von Standard-Benutzerattributen

Die Attribute der Nutzer:innen werden dem gerade aktiven Nutzer zugewiesen. Die folgenden Standardfelder können eingestellt werden:

- `FirstName`
- `LastName`
- `Email`
- `Gender`
- `DateOfBirth`
- `Country`
- `Language`
- `HomeCity`
- `PhoneNumber`

**Implementierungsbeispiel**<br>So würde das Setzen eines Vornamens im Code aussehen:

```brightscript
m.Braze.setFirstName("User's First Name")
```

## Zuweisen von benutzerdefinierten Benutzerattributen

Neben den Standard-Benutzerattributen können Sie in Braze auch benutzerdefinierte Attribute mit verschiedenen Datentypen definieren.

### Einstellungen angepasste Attribut-Werte
{% tabs %}
{% tab Boolesch %}
```brightscript
m.Braze.setCustomAttribute("boolAttribute", true)
```
{% endtab %}
{% tab Integer %}
```brightscript
m.Braze.setCustomAttribute("intAttribute", 5)
```
{% endtab %}
{% tab Gleitkommazahl oder Double %}
```brightscript
m.Braze.setCustomAttribute("floatAttribute", 3.5)
```
Braze behandelt FLOAT- und DOUBLE-Werte in unserer Datenbank genau gleich.
{% endtab %}
{% tab String %}
```brightscript
m.Braze.setCustomAttribute("stringAttribute", "stringValue")
```
{% endtab %}
{% tab Datum %}
```brightscript
dateAttribute = CreateObject("roDateTime")
dateAttribute.fromISO8601String("1992-11-29 00:00:00.000")
m.Braze.setCustomAttribute("dateAttribute", dateAttribute)
```
{% endtab %}
{% tab Array %}
```brightscript
stringArray = createObject("roArray", 3, true)
stringArray.Push("string1")
stringArray.Push("string2")
stringArray.Push("string3")
m.Braze.setCustomAttribute("arrayAttribute", stringArray)
```
{% endtab %}
{% endtabs %}

### Inkrementieren/Dekrementieren von angepassten Attributen

Dieser Code ist ein Beispiel für ein inkrementelles benutzerdefiniertes Attribut. Sie können den Wert eines angepassten Attributs um jeden positiven oder negativen ganzzahligen Wert erhöhen.

```brightscript
m.Braze.incrementCustomUserAttribute("intAttribute", 3)
```

### Zurücksetzen eines benutzerdefinierten Attributs

Benutzerdefinierte Attribute können auch mit der folgenden Methode deaktiviert werden:

```brightscript
m.Braze.unsetCustomAttribute("attributeName")
```

### Setzen eines benutzerdefinierten Attributs über die REST API

Sie können auch unsere REST API verwenden, um Benutzerattribute festzulegen. Einzelheiten finden Sie in der [API-Dokumentation für Benutzer]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

### Benutzerdefinierte Attributwertgrenzen

Angepasste Attribut-Werte haben eine maximale Länge von 255 Zeichen.

## Verwalten des Status von E-Mail-Abonnements

Sie können die folgenden E-Mail Abo-Status für Ihre Nutzer programmatisch über das SDK einstellen.

| Abostatus | Definition |
| ------------------- | ---------- |
| `OptedIn` | Abonniert und ausdrücklich angemeldet |
| `Subscribed` | Abonniert, aber nicht explizit angemeldet |
| `UnSubscribed` | Abbestellt und/oder ausdrücklich abgemeldet |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

>  Diese Typen fallen unter `BrazeConstants().SUBSCRIPTION_STATES`

Die Methode zum Einstellen des Status eines E-Mail-Abos lautet `setEmailSubscriptionState()`. Nutzer:innen werden bei Erhalt einer gültigen E-Mail Adresse automatisch auf `Subscribed` gesetzt. Wir empfehlen Ihnen jedoch, ein explizites Opt-in Verfahren einzurichten und diesen Wert bei Erhalt einer expliziten Zustimmung Ihrer Nutzer:innen auf `OptedIn` zu setzen. Weitere Informationen finden Sie unter [Verwalten von Nutzer:innen-Abonnements]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions).

Verwendungsbeispiel:
```brightscript
m.Braze.setEmailSubscriptionState(BrazeConstants().SUBSCRIPTION_STATES.OPTED_IN)
```

