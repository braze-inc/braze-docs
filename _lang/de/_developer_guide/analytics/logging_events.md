---
nav_title: Benutzerdefinierte Ereignisse protokollieren
article_title: Protokollieren Sie angepasste Events über das Braze SDK.
page_order: 3.1
description: "Erfahren Sie, wie Sie angepasste Events über das Braze SDK protokollieren können."

---

# Benutzerdefinierte Ereignisse protokollieren

> Erfahren Sie, wie Sie angepasste Events über das Braze SDK protokollieren können.

{% alert note %}
Für Wrapper-SDKs, die nicht aufgeführt sind, verwenden Sie stattdessen die entsprechende native Android- oder Swift-Methode.
{% endalert %}

## Protokollieren eines angepassten Events

Um ein angepasstes Event zu protokollieren, verwenden Sie die folgende Event-Protokollierungsmethode.

{% tabs %}
{% tab web %}
Für eine Standard Internet SDK-Implementierung können Sie die folgende Methode verwenden:

```javascript
braze.logCustomEvent("YOUR_EVENT_NAME");
```

Wenn Sie stattdessen den Google Tag Manager verwenden möchten, können Sie den Tag-Typ **Angepasstes Event** verwenden, um die [Methode`logCustomEvent` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent) aufzurufen und angepasste Events an Braze zu senden, optional mit angepassten Event-Eigenschaften. Um dies zu tun:

1. Geben Sie den **Event-Namen** an, indem Sie entweder eine Variable verwenden oder einen Namen eingeben.
2. Verwenden Sie den Button **Zeile hinzufügen**, um Event-Eigenschaften hinzuzufügen.

![Ein Dialogfeld mit den Konfigurationseinstellungen für Braze Action Tags. Die Einstellungen umfassen „Tag-Typ“ (angepasstes Event), „Ereignisname“ (Klick auf Button) und „Event-Eigenschaften“.]({% image_buster /assets/img/web-gtm/gtm-custom-event.png %})
{% endtab %}

{% tab android %}
Für natives Android können Sie die folgende Methode verwenden:

{% subtabs %}
{% subtab java %}
```java
Braze.getInstance(context).logCustomEvent(YOUR_EVENT_NAME);
```
{% endsubtab %}
{% subtab kotlin %}
```kotlin
Braze.getInstance(context).logCustomEvent(YOUR_EVENT_NAME)
```
{% endsubtab %}
{% endsubtabs %}

{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.logCustomEvent(name: "YOUR_EVENT_NAME")
```
{% endsubtab %}
{% subtab objective-c %}
```objc
[AppDelegate.braze logCustomEvent:@"YOUR_EVENT_NAME"];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab flutter %}
```dart
braze.logCustomEvent('YOUR_EVENT_NAME');
```
{% endtab %}

{% tab cordova %}
Bitte verwenden Sie die Braze-cordova-Plugin-Methode:

```javascript
BrazePlugin.logCustomEvent("YOUR_EVENT_NAME");
```

Die`logCustomEvent`API akzeptiert:
- `eventName` (erforderliche String): Bitte verwenden Sie bis zu 255 Zeichen. Bitte beginnen Sie den Namen nicht mit `$`. Bitte verwenden Sie alphanumerische Zeichen und Satzzeichen.
- `eventProperties` (optionales Objekt): Fügen Sie Schlüssel-Wert-Paare für Ereignismetadaten hinzu. Verwenden Sie Schlüssel mit bis zu 255 Zeichen und beginnen Sie Schlüssel nicht mit einem `$`Punkt.

Für Eigenschaftswerte verwenden Sie bitte`string`(maximal 255 Zeichen), `numeric`,`boolean` , Objekt-Arrays oder verschachtelte JSON-Objekte.

Für Details zur Implementierung, sehen Sie bitte die Braze cordova SDK-Quelle:
- [`www/BrazePlugin.js` `logCustomEvent` Methode (Zeilen 138–140)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/www/BrazePlugin.js#L138-L140)
- [`www/BrazePlugin.js` JSDoc (Zeilen 128–140)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/www/BrazePlugin.js#L128-L140)
- [Android-Handler in`src/android/BrazePlugin.kt`(Zeilen 108–115)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/android/BrazePlugin.kt#L108-L115)
- [iOS-Handler in`src/ios/BrazePlugin.m`(Zeilen 308–313)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/ios/BrazePlugin.m#L308-L313)
- [iOS-Methodendeklaration in`src/ios/BrazePlugin.h`(Zeile 24)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/ios/BrazePlugin.h#L24)
{% endtab %}

{% tab infillion %}
Wenn Sie [Infillion Beacons](https://infillion.com/software/beacons/) in Ihre Android App integriert haben, können Sie optional `visit.getPlace()` verwenden, um standortspezifische Ereignisse zu protokollieren. `requestImmediateDataFlush` überprüft, ob Ihr Ereignis auch dann protokolliert wird, wenn Ihre App im Hintergrund läuft.

{% subtabs %}
{% subtab java %}
```java
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace());
Braze.getInstance(context).requestImmediateDataFlush();
```
{% endsubtab %}

{% subtab kotlin %}
```kotlin
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace())
Braze.getInstance(context).requestImmediateDataFlush()
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab react native %}
```javascript
Braze.logCustomEvent("YOUR_EVENT_NAME");
```
{% endtab %}

{% tab roku %}
```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME")
```
{% endtab %}

{% tab unity %}
```csharp
AppboyBinding.LogCustomEvent("YOUR_EVENT_NAME");
```
{% endtab %}
{% endtabs %}

## Hinzufügen von Eigenschaften der Metadaten

Wenn Sie ein angepasstes Event protokollieren, haben Sie die Möglichkeit, Metadaten zu diesem angepassten Event hinzuzufügen, indem Sie ein Objekt mit den Eigenschaften des Events übergeben. Eigenschaften werden als Schlüssel-Werte-Paare definiert. Schlüssel sind Strings, und Werte können , `numeric`, `boolean`,[`Date`](http://www.w3schools.com/jsref/jsref_obj_date.asp)  Objekte, Arrays oder `string`verschachtelte JSON-Objekte sein.

Um Eigenschaften von Metadaten hinzuzufügen, verwenden Sie die folgende Methode zur Ereignisprotokollierung.

{% tabs %}
{% tab web %}
```javascript
braze.logCustomEvent("YOUR-EVENT-NAME", {
  you: "can", 
  pass: false, 
  orNumbers: 42,
  orDates: new Date(),
  or: ["any", "array", "here"],
  andEven: {
     deeply: ["nested", "json"]
  }
});
```
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab java %}
```java
Braze.logCustomEvent("YOUR-EVENT-NAME",
    new BrazeProperties(new JSONObject()
        .put("you", "can")
        .put("pass", false)
        .put("orNumbers", 42)
        .put("orDates", new Date())
        .put("or", new JSONArray()
            .put("any")
            .put("array")
            .put("here"))
        .put("andEven", new JSONObject()
            .put("deeply", new JSONArray()
                .put("nested")
                .put("json"))
        )
));
```
{% endsubtab %}
{% subtab kotlin %}
```kotlin
Braze.logCustomEvent("YOUR-EVENT-NAME",
    BrazeProperties(JSONObject()
        .put("you", "can")
        .put("pass", false)
        .put("orNumbers", 42)
        .put("orDates", Date())
        .put("or", JSONArray()
            .put("any")
            .put("array")
            .put("here"))
        .put("andEven", JSONObject()
            .put("deeply", JSONArray()
                .put("nested")
                .put("json"))
        )
))
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.logCustomEvent(
  name: "YOUR-EVENT-NAME",
  properties: [
    "you": "can",
    "pass": false,
    "orNumbers": 42,
    "orDates": Date(),
    "or": ["any", "array", "here"],
    "andEven": [
      "deeply": ["nested", "json"]
    ]
  ]
)
```
{% endsubtab %}
{% subtab objective-c %}
```objc
[AppDelegate.braze logCustomEvent:@"YOUR-EVENT-NAME"
                       properties:@{
  @"you": @"can",
  @"pass": @(NO),
  @"orNumbers": @42,
  @"orDates": [NSDate date],
  @"or": @[@"any", @"array", @"here"],
  @"andEven": @{
    @"deeply": @[@"nested", @"json"]
  }
}];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab flutter %}
```dart
braze.logCustomEvent('custom_event_with_properties', properties: {
    'key1': 'value1',
    'key2': ['value2', 'value3'],
    'key3': false,
});
```
{% endtab %}

{% tab cordova %}
Protokollieren Sie angepasste Events mit einem Eigenschaftenobjekt:

```javascript
var properties = {};
properties["key1"] = "value1";
properties["key2"] = ["value2", "value3"];
properties["key3"] = false;
BrazePlugin.logCustomEvent("YOUR-EVENT-NAME", properties);
```

Sie können Eigenschaften auch inline übergeben:

```javascript
BrazePlugin.logCustomEvent("YOUR-EVENT-NAME", {
  "key": "value",
  "amount": 42,
});
```

Die offizielle Cordova-BeispielApp umfasst Strings, numerische Werte, Boolesche Werte, Arrays und verschachtelte Objekteigenschaften:
- [`sample-project/www/js/index.js` (Zeilen 230–251)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/sample-project/www/js/index.js#L230-L251)

Beispielprojekt-Auszug:

```javascript
var properties = {};
properties["One"] = "That's the Way of the World";
properties["Two"] = "After the Love Has Gone";
properties["Three"] = "Can't Hide Love";
BrazePlugin.logCustomEvent("cordovaCustomEventWithProperties", properties);
BrazePlugin.logCustomEvent("cordovaCustomEventWithoutProperties");
BrazePlugin.logCustomEvent("cordovaCustomEventWithFloatProperties", {
  "Cart Value": 4.95,
  "Cart Item Name": "Spicy Chicken Bites 5 pack"
});
BrazePlugin.logCustomEvent("cordovaCustomEventWithNestedProperties", {
  "array key": [1, "2", false],
  "object key": {
    "k1": "1",
    "k2": 2,
    "k3": false,
  },
  "deep key": {
    "key": [1, "2", true]
  }
});
```

Für Details zu API und nativer Bridge, siehe:
- [`www/BrazePlugin.js` JSDoc (Zeilen 128–140)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/www/BrazePlugin.js#L128-L140)
- [Android-Handler in`src/android/BrazePlugin.kt`(Zeilen 108–115)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/android/BrazePlugin.kt#L108-L115)
- [iOS-Handler in`src/ios/BrazePlugin.m`(Zeilen 308–313)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/ios/BrazePlugin.m#L308-L313)
{% endtab %}

{% tab react native %}
```javascript
Braze.logCustomEvent("custom_event_with_properties", {
    key1: "value1",
    key2: ["value2", "value3"],
    key3: false,
});
```
{% endtab %}

{% tab roku %}
```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME", {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```
{% endtab %}

{% tab unity %}
```csharp
AppboyBinding.LogCustomEvent("event name", properties(Dictionary<string, object>));
```
{% endtab %}
{% endtabs %}

{% alert important %}
Die Schlüssel `time` und `event_name` sind reserviert und können nicht als angepasste Event-Eigenschaften verwendet werden.
{% endalert %}

## Bewährte Praktiken

Es sind drei wichtige Überprüfungen durchzuführen, damit Ihre angepassten Event-Eigenschaften wie erwartet protokolliert werden:

* [Festlegen, welche Ereignisse protokolliert werden](#verify-events)
* [Protokoll überprüfen](#verify-log)
* [Werte überprüfen](#verify-values)

Bei der Protokollierung eines angepassten Events können mehrere Eigenschaften protokolliert werden.

### Ereignisse überprüfen

Erkundigen Sie sich bei Ihren Entwickler:in, welche Event-Eigenschaften getrackt werden. Beachten Sie, dass bei allen Event-Eigenschaften zwischen Groß- und Kleinschreibung unterschieden wird. Weitere Informationen zum Tracking angepasster Events finden Sie in diesen Artikeln, die auf Ihrer Plattform basieren:

* [Android]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android)
* [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift)
* [Internet]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)

### Protokoll überprüfen

Um zu bestätigen, dass die Event-Eigenschaften erfolgreich getrackt wurden, können Sie alle Event-Eigenschaften auf der Seite **Angepasste Events** einsehen.

1. Gehen Sie zu **Dateneinstellungen** > **Benutzerdefinierte Ereignisse**.
2. Suchen Sie Ihr angepasstes Event in der Liste.
3. Wählen Sie für Ihre Veranstaltung **„Eigenschaften verwalten**”, um die Namen der mit einer Veranstaltung verbundenen Eigenschaften anzuzeigen.

### Werte überprüfen

Nachdem [Sie Ihren Nutzer als Testnutzer:in hinzugefügt haben]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/#adding-test-users), führen Sie bitte die folgenden Schritte aus, um Ihre Werte zu überprüfen: 

1. Führen Sie das angepasste Event innerhalb der App aus.
2. Warten Sie etwa 10 Sekunden, bis die Daten geleert sind.
3. Aktualisieren Sie das [Event-Benutzerprotokoll]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/), um das angepasste Event und den Wert der mit ihm übergebenen Eigenschaft anzuzeigen.
