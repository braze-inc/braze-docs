---
nav_title: Angepasste Attribute festlegen
article_title: Angepasste Attribute für iOS festlegen
platform: iOS
page_order: 3
description: "Dieser Referenzartikel beschreibt, wie Sie angepasste Attribute in Ihrer iOS-Anwendung festlegen."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Angepasste Attribute für iOS festlegen

Braze bietet Methoden für die Zuweisung von Attributen an Nutzer:innen. Im Dashboard können Sie Ihre Nutzer:innen nach diesen Attributen filtern und segmentieren.

Lesen Sie vor der Implementierung unbedingt die Beispiele für die Segmentierungsoptionen, die angepasste Events, Angepasste Attribute und Kauf-Events bieten, in unseren [Best Practices]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection) sowie unsere Hinweise zu den [Namenskonventionen für Events]({{site.baseurl}}/user_guide/data/custom_data/event_naming_conventions/).

## Zuweisen von Standard-Nutzerattributen

Um Nutzerattribute zuzuweisen, müssen Sie das entsprechende Feld für das gemeinsame `ABKUser`-Objekt festlegen.

Im Folgenden sehen Sie ein Beispiel für das Festlegen des Vorname-Attributs:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy sharedInstance].user.firstName = @"first_name";
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.firstName = "first_name"
```

{% endtab %}
{% endtabs %}

Die folgenden Attribute sollten für das `ABKUser`-Objekt festgelegt werden:

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

## Zuweisen von angepassten Nutzerattributen

Neben den Standard-Nutzerattributen können Sie in Braze auch angepasste Attribute mit verschiedenen Datentypen definieren. Weitere Informationen zu den Segmentierungsoptionen, die Ihnen jedes dieser Attribute bietet, finden Sie in unserer Dokumentation zur [Datenerfassung]({{site.baseurl}}/developer_guide/analytics/).

### Angepasstes Attribut mit einem String-Wert

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andStringValue:"your_attribute_value"];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andStringValue: "your_attribute_value")
```

{% endtab %}
{% endtabs %}

### Angepasstes Attribut mit einem Integer-Wert

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andIntegerValue:yourIntegerValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andIntegerValue: yourIntegerValue)
```

{% endtab %}
{% endtabs %}

### Angepasstes Attribut mit einem Double-Wert

Braze behandelt `float`- und `double`-Werte in der Datenbank gleich.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andDoubleValue:yourDoubleValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andDoubleValue: yourDoubleValue)
```

{% endtab %}
{% endtabs %}

### Angepasstes Attribut mit einem booleschen Wert

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andBOOLValue:yourBOOLValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andBOOLValue: yourBoolValue)
```

{% endtab %}
{% endtabs %}

### Angepasstes Attribut mit einem Datumswert

Datumsangaben, die mit dieser Methode an Braze übergeben werden, müssen entweder im [ISO 8601-Format](http://en.wikipedia.org/wiki/ISO_8601) (z. B. `2013-07-16T19:20:30+01:00`) oder im Format `yyyy-MM-dd'T'HH:mm:ss:SSSZ` (`2016-12-14T13:32:31.601-0800`) vorliegen.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andDateValue:yourDateValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andDateValue:yourDateValue)
```

{% endtab %}
{% endtabs %}

### Angepasstes Attribut mit einem Array-Wert

Die Standard- und Höchstzahl an Elementen in einem Array beträgt 500. Sie können die Höchstzahl an Elementen im Braze-Dashboard unter **Dateneinstellungen** > **Angepasste Attribute** aktualisieren. Arrays, die die Höchstzahl an Elementen überschreiten, werden gekürzt, sodass nur die Höchstzahl an Elementen enthalten bleibt.


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
{% tab swift %}

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

### Aufheben eines angepassten Attributs

Angepasste Attribute können auch mit der folgenden Methode aufgehoben werden:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user unsetCustomAttributeWithKey:@"your_attribute_key"];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.unsetCustomAttributeWithKey("your_attribute_key")
```

{% endtab %}
{% endtabs %}

### Inkrementieren/Dekrementieren von angepassten Attributen

Dieser Code ist ein Beispiel für ein inkrementierendes angepasstes Attribut. Sie können den Wert eines angepassten Attributs um jeden positiven oder negativen Integer- oder Long-Wert erhöhen:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user incrementCustomUserAttribute:@"your_attribute_key" by:incrementIntegerValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.incrementCustomUserAttribute("your_attribute_key", by: incrementIntegerValue)
```

{% endtab %}
{% endtabs %}

### Festlegen eines angepassten Attributs über die REST API

Sie können auch die REST API verwenden, um Nutzerattribute festzulegen. Einzelheiten finden Sie in der [Nutzer-API-Dokumentation]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

### Wertgrenzen für angepasste Attribute

Angepasste Attributwerte haben eine maximale Länge von 255 Zeichen; längere Werte werden abgeschnitten.

#### Zusätzliche Informationen

- Weitere Einzelheiten finden Sie in der Datei [`ABKUser.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h).
- Weitere Informationen finden Sie in der [`ABKUser`-Dokumentation](http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html).

## Einrichten von Nutzer-Abos

Um ein Abo für Ihre Nutzer:innen einzurichten (entweder E-Mail oder Push), rufen Sie die Funktion `setEmailNotificationSubscriptionType` bzw. `setPushNotificationSubscriptionType` auf. Beide Funktionen nehmen den enum-Typ `ABKNotificationSubscriptionType` als Argumente an. Dieser Typ hat drei verschiedene Zustände:

| Abostatus | Definition |
| ------------------- | ---------- |
| `ABKOptedin` | Abonniert und ausdrücklich angemeldet |
| `ABKSubscribed` | Abonniert, aber nicht ausdrücklich angemeldet |
| `ABKUnsubscribed` | Abbestellt und/oder ausdrücklich abgemeldet |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Nutzer:innen, die einer App die Erlaubnis erteilen, ihnen Push-Benachrichtigungen zu senden, haben standardmäßig den Status `ABKOptedin`, da iOS eine ausdrückliche Zustimmung verlangt.

Nutzer:innen werden bei Erhalt einer gültigen E-Mail-Adresse automatisch auf `ABKSubscribed` gesetzt. Wir empfehlen Ihnen jedoch, ein ausdrückliches Opt-in-Verfahren einzurichten und diesen Wert bei Erhalt einer ausdrücklichen Zustimmung auf `OptedIn` zu setzen. Weitere Einzelheiten finden Sie unter [Verwalten von Nutzer-Abos]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/).

### Einstellen von E-Mail-Abos

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setEmailNotificationSubscriptionType: ABKNotificationSubscriptionType]
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setEmailNotificationSubscriptionType(ABKNotificationSubscriptionType)
```

{% endtab %}
{% endtabs %}

### Abos für Push-Benachrichtigungen einstellen

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setPushNotificationSubscriptionType: ABKNotificationSubscriptionType]
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setPushNotificationSubscriptionType(ABKNotificationSubscriptionType)
```

{% endtab %}
{% endtabs %}

Weitere Einzelheiten finden Sie unter [Verwalten von Nutzer-Abos]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/).