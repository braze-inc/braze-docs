---
nav_title: Benutzerdefinierte Attribute einstellen
article_title: Benutzerdefinierte Attribute für iOS einstellen
platform: iOS
page_order: 3
description: "Dieser Referenzartikel beschreibt, wie Sie angepasste Attribute in Ihrer iOS-Anwendung festlegen."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Benutzerdefinierte Attribute für iOS einstellen

Braze bietet Methoden für die Zuweisung von Attributen an Benutzer. Auf dem Dashboard können Sie Ihre Benutzer nach diesen Attributen filtern und segmentieren.

Lesen Sie vor der Implementierung unbedingt die Beispiele für die Segmentierungsoptionen, die benutzerdefinierte Ereignisse, benutzerdefinierte Attribute und Kaufereignisse bieten, in unseren [Best Practices]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection) sowie unsere Hinweise zu den [Namenskonventionen für Ereignisse]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Zuweisen von Standard-Nutzerattributen

Um Nutzerattribute zuzuweisen, müssen Sie das entsprechende Feld für das Objekt `ABKUser` festlegen.

Im Folgenden sehen Sie ein Beispiel für die Einstellung des Attributs Vorname:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy sharedInstance].user.firstName = @"first_name";
```

{% endtab %}
{% tab schnell %}

```swift
Appboy.sharedInstance()?.user.firstName = "first_name"
```

{% endtab %}
{% endtabs %}

Die folgenden Attribute sollten für das Objekt `ABKUser` festgelegt werden:

- `firstName`
- `lastName`
- `email`
- `dateOfBirth`
- `country`
- `language`
- `homeCity`
- `phone`
- `userID`
- `gender`

## Zuweisen von benutzerdefinierten Benutzerattributen

Neben den Standard-Benutzerattributen können Sie in Braze auch benutzerdefinierte Attribute mit verschiedenen Datentypen definieren. Weitere Informationen zu den Segmentierungsoptionen, die Ihnen jedes dieser Attribute bietet, finden Sie in unserer [Sammlung von Nutzerdaten]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/).

### Benutzerdefiniertes Attribut mit einem String-Wert

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andStringValue:"your_attribute_value"];
```

{% endtab %}
{% tab schnell %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andStringValue: "your_attribute_value")
```

{% endtab %}
{% endtabs %}

### Benutzerdefiniertes Attribut mit einem Integer-Wert

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andIntegerValue:yourIntegerValue];
```

{% endtab %}
{% tab schnell %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andIntegerValue: yourIntegerValue)
```

{% endtab %}
{% endtabs %}

### Benutzerdefiniertes Attribut mit einem doppelten Wert

Braze behandelt die Werte von `float` und `double` in unserer Datenbank gleich.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andDoubleValue:yourDoubleValue];
```

{% endtab %}
{% tab schnell %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andDoubleValue: yourDoubleValue)
```

{% endtab %}
{% endtabs %}

### Benutzerdefiniertes Attribut mit einem booleschen Wert

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andBOOLValue:yourBOOLValue];
```

{% endtab %}
{% tab schnell %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andBOOLValue: yourBoolValue)
```

{% endtab %}
{% endtabs %}

### Benutzerdefiniertes Attribut mit einem Datumswert

Datumsangaben, die mit dieser Methode an Braze übergeben werden, müssen entweder im [ISO 8601-Format](http://en.wikipedia.org/wiki/ISO_8601) (e.g `2013-07-16T19:20:30+01:00`) oder im Format `yyyy-MM-dd'T'HH:mm:ss:SSSZ` (`2016-12-14T13:32:31.601-0800`) vorliegen.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andDateValue:yourDateValue];
```

{% endtab %}
{% tab schnell %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andDateValue:yourDateValue)
```

{% endtab %}
{% endtabs %}

### Benutzerdefiniertes Attribut mit einem Array-Wert

Die maximale Anzahl von Elementen in [benutzerdefinierten Attribut-Arrays]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays) ist standardmäßig auf 25 festgelegt. Arrays, die die maximale Anzahl von Elementen überschreiten, werden so abgeschnitten, dass sie die maximale Anzahl von Elementen enthalten. Das Maximum für einzelne Arrays kann auf bis zu 100 erhöht werden. Wenn Sie möchten, dass dieser Höchstbetrag erhöht wird, wenden Sie sich an Ihren Kundenbetreuer. 


{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Setting a custom attribute with an array value
[[Appboy sharedInstance].user setCustomAttributeArrayWithKey:@"array_name" array:@[@"value1",  @"value2"]];
// Adding to a custom attribute with an array value
[[Appboy sharedInstance].user addToCustomAttributeArrayWithKey:@"array_name" value:@"value3"];
// Removing a value from an array type custom attribute
[[Appboy sharedInstance].user removeFromCustomAttributeArrayWithKey:@"array_name" value:@"value2"];
// Removing an entire array and key
[[Appboy sharedInstance].user setCustomAttributeArrayWithKey:@"array_name" array:nil];
```

{% endtab %}
{% tab schnell %}

```swift
// Setting a custom attribute with an array value
Appboy.sharedInstance()?.user.setCustomAttributeArrayWithKey("array_name", array: ["value1",  "value2"])
// Adding to a custom attribute with an array value
Appboy.sharedInstance()?.user.addToCustomAttributeArrayWithKey("array_name", value: "value3")
// Removing a value from an array type custom attribute
Appboy.sharedInstance()?.user.removeFromCustomAttributeArrayWithKey("array_name", value: "value2")
```

{% endtab %}
{% endtabs %}

### Zurücksetzen eines benutzerdefinierten Attributs

Benutzerdefinierte Attribute können auch mit der folgenden Methode deaktiviert werden:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user unsetCustomAttributeWithKey:@"your_attribute_key"];
```

{% endtab %}
{% tab schnell %}

```swift
Appboy.sharedInstance()?.user.unsetCustomAttributeWithKey("your_attribute_key")
```

{% endtab %}
{% endtabs %}

### Inkrementieren/Dekrementieren von angepassten Attributen

Dieser Code ist ein Beispiel für ein inkrementelles benutzerdefiniertes Attribut. Sie können den Wert eines benutzerdefinierten Attributs um jeden positiven oder negativen Integer- oder Long-Wert erhöhen:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user incrementCustomUserAttribute:@"your_attribute_key" by:incrementIntegerValue];
```

{% endtab %}
{% tab schnell %}

```swift
Appboy.sharedInstance()?.user.incrementCustomUserAttribute("your_attribute_key", by: incrementIntegerValue)
```

{% endtab %}
{% endtabs %}

### Setzen eines benutzerdefinierten Attributs über die REST API

Sie können auch unsere REST API verwenden, um Nutzerattribute festzulegen. Einzelheiten finden Sie in der [Benutzer-API-Dokumentation]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

### Benutzerdefinierte Attributwertgrenzen

Angepasste Attributwerte haben eine maximale Länge von 255 Zeichen; längere Werte werden abgeschnitten.

#### Zusätzliche Informationen

- Weitere Einzelheiten finden Sie in der Datei [`ABKUser.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h).
- Weitere Informationen finden Sie in der [Dokumentation`ABKUser` ](http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html).

## Einrichten von Benutzerabonnements

Um ein Abo für Ihre Nutzer einzurichten (entweder E-Mail oder Push), rufen Sie die Funktion `setEmailNotificationSubscriptionType` bzw. `setPushNotificationSubscriptionType` auf. Beide Funktionen nehmen den Enum-Typ `ABKNotificationSubscriptionType` als Argumente an. Dieser Typ hat drei verschiedene Zustände:

| Abostatus | Definition |
| ------------------- | ---------- |
| `ABKOptedin` | Abonniert und ausdrücklich angemeldet |
| `ABKSubscribed` | Abonniert, aber nicht explizit angemeldet |
| `ABKUnsubscribed` | Abbestellt und/oder ausdrücklich abgemeldet |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Benutzer, die einer App die Erlaubnis erteilen, ihnen Push-Benachrichtigungen zu senden, haben standardmäßig den Status `ABKOptedin`, da iOS eine ausdrückliche Zustimmung verlangt.

Die Benutzer werden bei Erhalt einer gültigen E-Mail-Adresse automatisch auf `ABKSubscribed` gesetzt. Wir empfehlen Ihnen jedoch, ein explizites Opt-in-Verfahren einzurichten und diesen Wert bei Erhalt einer ausdrücklichen Zustimmung Ihres Benutzers auf `OptedIn` zu setzen. Weitere Einzelheiten finden Sie unter [Verwalten von Benutzerabonnements]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/).

### Einstellen von E-Mail-Abonnements

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setEmailNotificationSubscriptionType: ABKNotificationSubscriptionType]
```

{% endtab %}
{% tab schnell %}

```swift
Appboy.sharedInstance()?.user.setEmailNotificationSubscriptionType(ABKNotificationSubscriptionType)
```

{% endtab %}
{% endtabs %}

### Abonnements für Push-Benachrichtigungen einstellen

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setPushNotificationSubscriptionType: ABKNotificationSubscriptionType]
```

{% endtab %}
{% tab schnell %}

```swift
Appboy.sharedInstance()?.user.setPushNotificationSubscriptionType(ABKNotificationSubscriptionType)
```

{% endtab %}
{% endtabs %}

Weitere Einzelheiten finden Sie unter [Verwalten von Benutzerabonnements]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/).

