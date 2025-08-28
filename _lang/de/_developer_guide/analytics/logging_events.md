---
nav_title: Protokollierung angepasster Events
article_title: Protokollierung angepasster Events über das Braze SDK
page_order: 3.1
description: "Erfahren Sie, wie Sie angepasste Events über das Braze SDK protokollieren können."

---

# Protokollierung angepasster Events

> Erfahren Sie, wie Sie angepasste Events über das Braze SDK protokollieren können.

{% alert note %}
Für Wrapper-SDKs, die nicht aufgeführt sind, verwenden Sie stattdessen die entsprechende native Android- oder Swift-Methode.
{% endalert %}

## Protokollieren eines angepassten Events

Um ein angepasstes Event zu protokollieren, verwenden Sie die folgende Event-Protokollierungsmethode.

{% tabs %}
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

{% tab schnell %}
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

{% tab Internet %}
Für eine Standard Internet SDK-Implementierung können Sie die folgende Methode verwenden:

```javascript
braze.logCustomEvent("YOUR_EVENT_NAME");
```

Wenn Sie stattdessen den Google Tag Manager verwenden möchten, können Sie den Tag-Typ **Angepasstes Event** verwenden, um die [Methode`logCustomEvent` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent) aufzurufen und angepasste Events an Braze zu senden, optional mit angepassten Event-Eigenschaften. Um dies zu tun:

1. Geben Sie den **Event-Namen** an, indem Sie entweder eine Variable verwenden oder einen Namen eingeben.
2. Verwenden Sie den Button **Zeile hinzufügen**, um Event-Eigenschaften hinzuzufügen.

![Ein Dialogfeld mit den Konfigurationseinstellungen für Braze Action Tags. Zu den Einstellungen gehören "Tag-Typ" (Angepasstes Event), "Event-Name" (Button-Klick) und "Event-Eigenschaften".]({% image_buster /assets/img/web-gtm/gtm-custom-event.png %})
{% endtab %}

{% tab flattern %}
```dart
braze.logCustomEvent('YOUR_EVENT_NAME');
```
{% endtab %}

{% tab Infillion %}
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

{% tab React Native %}
```javascript
Braze.logCustomEvent("YOUR_EVENT_NAME");
```
{% endtab %}

{% tab roku %}
```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME")
```
{% endtab %}

{% tab Unity %}
```csharp
AppboyBinding.LogCustomEvent("YOUR_EVENT_NAME");
```
{% endtab %}

{% tab Unreal Engine %}
```cpp
UBraze->LogCustomEvent(TEXT("YOUR_EVENT_NAME"));
```
{% endtab %}
{% endtabs %}

## Hinzufügen von Eigenschaften der Metadaten

Wenn Sie ein angepasstes Event protokollieren, haben Sie die Möglichkeit, Metadaten zu diesem angepassten Event hinzuzufügen, indem Sie ein Objekt mit den Eigenschaften des Events übergeben. Eigenschaften werden als Schlüssel-Werte-Paare definiert. Die Schlüssel sind Strings und die Werte können `string`, `numeric`, `boolean`, oder [`Date`](http://www.w3schools.com/jsref/jsref_obj_date.asp) Objekte sein.

Um Eigenschaften von Metadaten hinzuzufügen, verwenden Sie die folgende Methode zur Ereignisprotokollierung.

{% tabs %}
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

{% tab schnell %}
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

{% tab Internet %}
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

{% tab flattern %}
```dart
braze.logCustomEvent('custom_event_with_properties', properties: {
    'key1': 'value1',
    'key2': ['value2', 'value3'],
    'key3': false,
});
```
{% endtab %}

{% tab React Native %}
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

{% tab Unity %}
```csharp
AppboyBinding.LogCustomEvent("event name", properties(Dictionary<string, object>));
```
{% endtab %}

{% tab Unreal Engine %}
```cpp
TMap<FString, FString> Properties;
Properties.Add(TEXT("you"), TEXT("can"));
Properties.Add(TEXT("pass"), TEXT("false"));
Properties.Add(TEXT("orNumbers"), FString::FromInt(42));
Properties.Add(TEXT("orDates"), FDateTime::Now().ToString());
Properties.Add(TEXT("or"), TEXT("any,array,here")); // Arrays are stored as comma-separated strings
Properties.Add(TEXT("andEven"), TEXT("deeply:nested,json"));

UBraze->LogCustomEventWithProperties(TEXT("YOUR_EVENT_NAME"), Properties);
```
{% endtab %}
{% endtabs %}

{% alert important %}
Die Schlüssel `time` und `event_name` sind reserviert und können nicht als angepasste Event-Eigenschaften verwendet werden.
{% endalert %}
