---
nav_title: Benutzerdefinierte Ereignisse protokollieren
article_title: Protokollierung angepasster Events über das Braze SDK
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

![Ein Dialogfeld mit den Konfigurationseinstellungen für Braze Action Tags. Enthaltene Einstellungen sind "Tag-Typ" (angepasstes Event), "Event-Name" (Button-Klick) und "Event-Eigenschaften".]({% image_buster /assets/img/web-gtm/gtm-custom-event.png %})
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

Wenn Sie ein angepasstes Event protokollieren, haben Sie die Möglichkeit, Metadaten über dieses angepasste Event hinzuzufügen, indem Sie ein Objekt mit Eigenschaften mit dem Event übergeben. Eigenschaften werden als Schlüssel-Werte-Paare definiert. Die Schlüssel sind Strings und die Werte können `string`, `numeric`, `boolean` sein, [`Date`](http://www.w3schools.com/jsref/jsref_obj_date.asp) Objekte, Arrays oder verschachtelte JSON-Objekte sein.

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

Es gibt drei wichtige Prüfungen, die Sie durchführen müssen, damit Ihre angepassten Event-Eigenschaften wie erwartet protokolliert werden:

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
3. Wählen Sie für Ihr Ereignis **Eigenschaften verwalten** aus, um die Namen der mit einem Ereignis verbundenen Eigenschaften anzuzeigen.

### Werte überprüfen

Nachdem [Sie Ihren Nutzer:in als Testnutzer]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/#adding-test-users): [in hinzugefügt haben]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/#adding-test-users), folgen Sie diesen Schritten, um Ihre Werte zu überprüfen: 

1. Führen Sie das angepasste Event innerhalb der App aus.
2. Warten Sie etwa 10 Sekunden, bis die Daten geleert sind.
3. Aktualisieren Sie das [Event-Benutzerprotokoll]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/), um das angepasste Event und den Wert der mit ihm übergebenen Eigenschaft anzuzeigen.
