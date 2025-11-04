{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Standard-Nutzerattribute

Um Nutzer:innen-Attribute festzulegen, müssen Sie das entsprechende Feld auf dem gemeinsamen Objekt `ABKUser` einstellen. Im Folgenden sehen Sie ein Beispiel für die Einstellung des Attributs Vorname:

{% tabs %}
{% tab schnell %}

```swift
AppDelegate.braze?.user.set(firstName: "Alex")
```

{% endtab %}
{% tab objektiv-c %}

```objc
[AppDelegate.braze.user setFirstName:@"Alex"];
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

## Angepasste Nutzerattribute

Zusätzlich zu den standardmäßigen Nutzer:innen-Attributen können Sie in Braze auch angepasste Attribute unter Verwendung verschiedener Datentypen definieren. Weitere Informationen zu den Segmentierungsoptionen der einzelnen Attribute finden Sie unter [Nutzer:innen-Datenerfassung]({{site.baseurl}}/developer_guide/analytics/).

{% alert important %}
Angepasste Attributwerte haben eine maximale Länge von 255 Zeichen; längere Werte werden abgeschnitten. Weitere Informationen finden Sie unter [`Braze.User`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class).
{% endalert %}

### Anpassen der Attribute

{% tabs local %}
{% tab String %}
So legen Sie ein angepasstes Attribut mit einem `string` Wert fest:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: "your_attribute_value")
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" stringValue:"your_attribute_value"];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Ganzzahl %}
So passen Sie ein angepasstes Attribut mit einem `integer` Wert an:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourIntegerValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andIntegerValue:yourIntegerValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Gleitkommazahlen %}
Braze behandelt die Werte von `float` und `double` in unserer Datenbank gleich. So legen Sie ein angepasstes Attribut mit einem doppelten Wert fest:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourDoubleValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDoubleValue:yourDoubleValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab boolean %}
So legen Sie ein angepasstes Attribut mit einem `boolean` Wert fest:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", value: yourBoolValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andBOOLValue:yourBOOLValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Datum %}
So legen Sie ein angepasstes Attribut mit einem `date` Wert fest:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", dateValue:yourDateValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDateValue:yourDateValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Array %}
Die maximale Anzahl von Elementen in [benutzerdefinierten Attribut-Arrays]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays) ist standardmäßig auf 25 festgelegt. Arrays, die die maximale Anzahl von Elementen überschreiten, werden so abgeschnitten, dass sie die maximale Anzahl von Elementen enthalten. Das Maximum für einzelne Arrays kann auf bis zu 100 erhöht werden. Wenn Sie möchten, dass dieser Höchstbetrag erhöht wird, wenden Sie sich an Ihren Kundenbetreuer.

So passen Sie ein angepasstes Attribut mit einem `array` Wert an:

{% subtabs %}
{% subtab swift %}
```swift
// Setting a custom attribute with an array value
AppDelegate.braze?.user.setCustomAttributeArray(key: "array_name", array: ["value1",  "value2"])
// Adding to a custom attribute with an array value
AppDelegate.braze?.user.addToCustomAttributeArray(key: "array_name", value: "value3")
// Removing a value from an array type custom attribute
AppDelegate.braze?.user.removeFromCustomAttributeArray(key: "array_name", value: "value2")
```
{% endsubtab %}

{% subtab objective-c %}
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
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Inkrementieren oder Dekrementieren angepasster Attribute

Dieser Code ist ein Beispiel für ein inkrementelles benutzerdefiniertes Attribut. Sie können den Wert eines angepassten Attributs um einen beliebigen `integer` oder `long` Wert erhöhen:

{% tabs %}
{% tab schnell %}

```swift
AppDelegate.braze?.user.incrementCustomUserAttribute(key: "your_attribute_key", by: incrementIntegerValue)
```

{% endtab %}
{% tab objektiv-c %}

```objc
[AppDelegate.braze.user incrementCustomUserAttribute:@"your_attribute_key" by:incrementIntegerValue];
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
{% tab objektiv-c %}

```objc
[AppDelegate.braze.user unsetCustomAttributeWithKey:@"your_attribute_key"];
```

{% endtab %}
{% endtabs %}

### Verwendung der REST API

Sie können auch unsere REST API verwenden, um Nutzer:innen-Attribute zu setzen oder zu löschen. Weitere Informationen finden Sie unter [Endpunkte für Nutzerdaten]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data):in.

## Einstellen von Nutzer:in-Abonnements

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
{% tab objektiv-c %}

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
{% tab objektiv-c %}

```objc
[AppDelegate.braze.user setPushNotificationSubscriptionState: BRZUserSubscriptionState]
```

{% endtab %}
{% endtabs %}

Weitere Einzelheiten finden Sie unter [Verwalten von Benutzerabonnements]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/).
