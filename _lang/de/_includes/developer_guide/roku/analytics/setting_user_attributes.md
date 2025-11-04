{% multi_lang_include developer_guide/prerequisites/roku.md %}

## Standard-Nutzerattribute

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

Sie können einen Vornamen zum Beispiel wie folgt einrichten:

```brightscript
m.Braze.setFirstName("Alex")
```

## Angepasste Nutzerattribute

Zusätzlich zu den standardmäßigen Nutzer:innen-Attributen können Sie in Braze auch angepasste Attribute unter Verwendung verschiedener Datentypen definieren.

### Einstellungen angepasste Attribute

{% tabs %}
{% tab String %}
So legen Sie für ein angepasstes Attribut einen `string` Wert fest:

```brightscript
m.Braze.setCustomAttribute("stringAttribute", "stringValue")
```
{% endtab %}

{% tab Integer %}
So passen Sie ein angepasstes Attribut mit einem `integer` Wert an:

```brightscript
m.Braze.setCustomAttribute("intAttribute", 5)
```
{% endtab %}

{% tab Gleitkommazahlen %}
Braze behandelt die Werte von `float` und `double` genau gleich. So legen Sie ein angepasstes Attribut mit einem der beiden Werte fest:

```brightscript
m.Braze.setCustomAttribute("floatAttribute", 3.5)
```
{% endtab %}

{% tab Boolesch %}
So legen Sie ein angepasstes Attribut mit einem `boolean` Wert fest:

```brightscript
m.Braze.setCustomAttribute("boolAttribute", true)
```
{% endtab %}

{% tab Datum %}
So legen Sie ein angepasstes Attribut mit einem `date` Wert fest:

```brightscript
dateAttribute = CreateObject("roDateTime")
dateAttribute.fromISO8601String("1992-11-29 00:00:00.000")
m.Braze.setCustomAttribute("dateAttribute", dateAttribute)
```
{% endtab %}

{% tab Array %}
So passen Sie ein angepasstes Attribut mit einem `array` Wert an:

```brightscript
stringArray = createObject("roArray", 3, true)
stringArray.Push("string1")
stringArray.Push("string2")
stringArray.Push("string3")
m.Braze.setCustomAttribute("arrayAttribute", stringArray)
```
{% endtab %}
{% endtabs %}

{% alert important %}
Angepasste Attributwerte haben eine maximale Länge von 255 Zeichen; längere Werte werden abgeschnitten.
{% endalert %}

### Inkrementieren und Dekrementieren von angepassten Attributen

Dieser Code ist ein Beispiel für ein inkrementelles benutzerdefiniertes Attribut. Sie können den Wert eines angepassten Attributs um jeden positiven oder negativen ganzzahligen Wert erhöhen.

```brightscript
m.Braze.incrementCustomUserAttribute("intAttribute", 3)
```

### Angepasste Attribute nicht anpassen

Benutzerdefinierte Attribute können auch mit der folgenden Methode deaktiviert werden:

```brightscript
m.Braze.unsetCustomAttribute("attributeName")
```

### Verwendung der REST API

Sie können auch unsere REST API verwenden, um Nutzer:innen-Attribute zu setzen oder zu löschen. Weitere Informationen finden Sie unter [Endpunkte für Nutzerdaten]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data):in.

## Einstellen von E-Mail-Abonnements

Sie können die folgenden E-Mail Abo-Status für Ihre Nutzer programmatisch über das SDK einstellen.

| Abostatus | Definition |
| ------------------- | ---------- |
| `OptedIn` | Abonniert und ausdrücklich angemeldet |
| `Subscribed` | Abonniert, aber nicht explizit angemeldet |
| `UnSubscribed` | Abbestellt und/oder ausdrücklich abgemeldet |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Diese Typen fallen unter `BrazeConstants().SUBSCRIPTION_STATES`.
{% endalert %}

Die Methode zum Einstellen des Status eines E-Mail-Abos lautet `setEmailSubscriptionState()`. Nutzer:innen werden bei Erhalt einer gültigen E-Mail Adresse automatisch auf `Subscribed` gesetzt. Wir empfehlen Ihnen jedoch, ein explizites Opt-in Verfahren einzurichten und diesen Wert bei Erhalt einer expliziten Zustimmung Ihrer Nutzer:innen auf `OptedIn` zu setzen. Weitere Informationen finden Sie unter [Verwalten von Nutzer:innen-Abonnements]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions).

```brightscript
m.Braze.setEmailSubscriptionState(BrazeConstants().SUBSCRIPTION_STATES.OPTED_IN)
```
