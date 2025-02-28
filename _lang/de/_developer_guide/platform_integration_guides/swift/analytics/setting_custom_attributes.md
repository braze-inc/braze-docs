---
nav_title: Benutzerdefinierte Attribute einstellen
article_title: Benutzerdefinierte Attribute für iOS einstellen
platform: Swift
page_order: 3
description: "Dieser Referenzartikel beschreibt, wie Sie angepasste Attribute für das Swift SDK festlegen."

---

# Benutzerdefinierte Attribute einstellen

> Braze bietet Methoden für die Zuweisung von Attributen an Benutzer. Auf dem Dashboard können Sie Ihre Benutzer nach diesen Attributen filtern und segmentieren.

Lesen Sie vor der Implementierung unbedingt die Beispiele für die Segmentierungsoptionen, die benutzerdefinierte Ereignisse, benutzerdefinierte Attribute und Kaufereignisse bieten, in unseren [Best Practices]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection) sowie unsere Hinweise zu den [Namenskonventionen für Ereignisse]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Zuweisen von Standard-Nutzerattributen

Um Nutzerattribute zuzuweisen, müssen Sie das entsprechende Feld für das Objekt `ABKUser` festlegen.

Im Folgenden sehen Sie ein Beispiel für die Einstellung des Attributs Vorname:

{% tabs %}
{% tab schnell %}

```swift
AppDelegate.braze?.user.set(firstName: "first_name")
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.user setFirstName:@"first_name"];
```

{% endtab %}
{% endtabs %}

Die folgenden Attribute sollten für das Objekt `Braze.User` festgelegt werden:

- `firstName`
- `lastName`
- `email`
- `dateOfBirth`
- `country`
- `language`
- `homeCity`
- `phone`
- `gender`

## Zuweisen von benutzerdefinierten Benutzerattributen

Neben den Standard-Benutzerattributen können Sie in Braze auch benutzerdefinierte Attribute mit verschiedenen Datentypen definieren. Weitere Informationen zu den Segmentierungsoptionen, die Ihnen jedes dieser Attribute bietet, finden Sie in unserer [Sammlung von Nutzerdaten]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/).

### Benutzerdefiniertes Attribut mit einem String-Wert

{% tabs %}
{% tab schnell %}

```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: "your_attribute_value")
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" stringValue:"your_attribute_value"];
```

{% endtab %}
{% endtabs %}

### Benutzerdefiniertes Attribut mit einem Integer-Wert

{% tabs %}
{% tab schnell %}

```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourIntegerValue)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andIntegerValue:yourIntegerValue];
```

{% endtab %}
{% endtabs %}

### Benutzerdefiniertes Attribut mit einem doppelten Wert

Braze behandelt die Werte von `float` und `double` in unserer Datenbank gleich.

{% tabs %}
{% tab schnell %}

```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourDoubleValue)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDoubleValue:yourDoubleValue];
```

{% endtab %}
{% endtabs %}

### Benutzerdefiniertes Attribut mit einem booleschen Wert

{% tabs %}
{% tab schnell %}

```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", value: yourBoolValue)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andBOOLValue:yourBOOLValue];
```

{% endtab %}
{% endtabs %}

### Benutzerdefiniertes Attribut mit einem Datumswert

{% tabs %}
{% tab schnell %}

```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", dateValue:yourDateValue)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDateValue:yourDateValue];
```

{% endtab %}
{% endtabs %}

### Benutzerdefiniertes Attribut mit einem Array-Wert

Die maximale Anzahl von Elementen in [benutzerdefinierten Attribut-Arrays]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays) ist standardmäßig auf 25 festgelegt. Arrays, die die maximale Anzahl von Elementen überschreiten, werden so abgeschnitten, dass sie die maximale Anzahl von Elementen enthalten. Das Maximum für einzelne Arrays kann auf bis zu 100 erhöht werden. Wenn Sie möchten, dass dieser Höchstbetrag erhöht wird, wenden Sie sich an Ihren Kundenbetreuer. 


{% tabs %}
{% tab schnell %}

```swift
// Setting a custom attribute with an array value
AppDelegate.braze?.user.setCustomAttributeArray(key: "array_name", array: ["value1",  "value2"])
// Adding to a custom attribute with an array value
AppDelegate.braze?.user.addToCustomAttributeArray(key: "array_name", value: "value3")
// Removing a value from an array type custom attribute
AppDelegate.braze?.user.removeFromCustomAttributeArray(key: "array_name", value: "value2")
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
// Setting a custom attribute with an array value
[AppDelegate.braze.user setCustomAttributeArrayWithKey:@"array_name" array:@[@"value1",  @"value2"]];
// Adding to a custom attribute with an array value
[AppDelegate.braze.user addToCustomAttributeArrayWithKey:@"array_name" value:@"value3"];
// Removing a value from an array type custom attribute
[AppDelegate.braze.user removeFromCustomAttributeArrayWithKey:@"array_name" value:@"value2"];
// Removing an entire array and key
[AppDelegate.braze.user setCustomAttributeArrayWithKey:@"array_name" array:nil];
```

{% endtab %}
{% endtabs %}

### Zurücksetzen eines benutzerdefinierten Attributs

Benutzerdefinierte Attribute können auch mit der folgenden Methode deaktiviert werden:

{% tabs %}
{% tab schnell %}

```swift
AppDelegate.braze?.user.unsetCustomAttribute(key: "your_attribute_key")
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.user unsetCustomAttributeWithKey:@"your_attribute_key"];
```

{% endtab %}
{% endtabs %}

### Inkrementieren/Dekrementieren von angepassten Attributen

Dieser Code ist ein Beispiel für ein inkrementelles benutzerdefiniertes Attribut. Sie können den Wert eines benutzerdefinierten Attributs um jeden positiven oder negativen Integer- oder Long-Wert erhöhen:

{% tabs %}
{% tab schnell %}

```swift
AppDelegate.braze?.user.incrementCustomUserAttribute(key: "your_attribute_key", by: incrementIntegerValue)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.user incrementCustomUserAttribute:@"your_attribute_key" by:incrementIntegerValue];
```

{% endtab %}
{% endtabs %}

### Setzen eines benutzerdefinierten Attributs über die REST API

Sie können auch unsere REST API verwenden, um Nutzerattribute festzulegen. Einzelheiten finden Sie in der [Benutzer-API-Dokumentation]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

### Benutzerdefinierte Attributwertgrenzen

Angepasste Attributwerte haben eine maximale Länge von 255 Zeichen; längere Werte werden abgeschnitten.

#### Zusätzliche Informationen

- Weitere Informationen finden Sie in der [Dokumentation`Braze.User` ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class).

## Einrichten von Benutzerabonnements

Um ein Abo für Ihre Nutzer einzurichten (entweder E-Mail oder Push), rufen Sie die Funktion `set(emailSubscriptionState:)` bzw. `set(pushNotificationSubscriptionState:)` auf. Beide Funktionen nehmen den Enum-Typ `Braze.User.SubscriptionState` als Argumente an. Dieser Typ hat drei verschiedene Zustände:

| Abostatus | Definition |
| ------------------- | ---------- |
| `optedIn` | Abonniert und ausdrücklich angemeldet |
| `subscribed` | Abonniert, aber nicht explizit angemeldet |
| `unsubscribed` | Abbestellt und/oder ausdrücklich abgemeldet |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Benutzer, die einer App die Erlaubnis erteilen, ihnen Push-Benachrichtigungen zu senden, haben standardmäßig den Status `optedIn`, da iOS eine ausdrückliche Zustimmung verlangt.

Die Benutzer werden bei Erhalt einer gültigen E-Mail-Adresse automatisch auf `subscribed` gesetzt. Wir empfehlen Ihnen jedoch, ein explizites Opt-in-Verfahren einzurichten und diesen Wert bei Erhalt einer ausdrücklichen Zustimmung Ihres Benutzers auf `optedIn` zu setzen. Weitere Einzelheiten finden Sie unter [Verwalten von Benutzerabonnements]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/).

### Einstellen von E-Mail-Abonnements

{% tabs %}
{% tab schnell %}

```swift
AppDelegate.braze?.user.set(emailSubscriptionState: Braze.User.SubscriptionState)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.user setEmailSubscriptionState: BRZUserSubscriptionState]
```

{% endtab %}
{% endtabs %}

### Abonnements für Push-Benachrichtigungen einstellen

{% tabs %}
{% tab schnell %}

```swift
AppDelegate.braze?.user.set(pushNotificationSubscriptionState: Braze.User.SubscriptionState)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.user setPushNotificationSubscriptionState: BRZUserSubscriptionState]
```

{% endtab %}
{% endtabs %}

Weitere Einzelheiten finden Sie unter [Verwalten von Benutzerabonnements]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/).

