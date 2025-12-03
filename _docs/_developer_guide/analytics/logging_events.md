---
nav_title: Logging custom events
article_title: Logging custom events through the Braze SDK
page_order: 3.1
description: "Learn how to log custom events through the Braze SDK."

---

# Logging custom events

> Learn how to log custom events through the Braze SDK.

{% alert note %}
For wrapper SDKs not listed, use the relevant native Android or Swift method instead.
{% endalert %}

## Logging a custom event

To log a custom event, use the following event-logging method.

{% tabs %}
{% tab web %}
For a standard Web SDK implementation, you can use the following method:

```javascript
braze.logCustomEvent("YOUR_EVENT_NAME");
```

If you'd like to use Google Tag Manager instead, you can use the **Custom Event** tag type to call the [`logCustomEvent` method](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent) and send custom events to Braze, optionally including custom event properties. To do this:

1. Enter the **Event Name** by either using a variable or typing an event name.
2. Use the **Add Row** button to add event properties.

![A dialog box showing the Braze Action Tag configuration settings. Settings included are "tag type"(custom event), "event name" (button click), and "event properties".]({% image_buster /assets/img/web-gtm/gtm-custom-event.png %})
{% endtab %}

{% tab android %}
For native Android, you can use the following method:

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
If you've integrated [Infillion Beacons](https://infillion.com/software/beacons/) into your Android app, you can optionally use `visit.getPlace()` to log location-specific events. `requestImmediateDataFlush` verifies that your event will log even if your app is in the background.

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

{% tab unreal engine %}
```cpp
UBraze->LogCustomEvent(TEXT("YOUR_EVENT_NAME"));
```
{% endtab %}
{% endtabs %}

## Adding metadata properties

When you log a custom event, you have the option to add metadata about that custom event by passing a properties object with the event. Properties are defined as key-value pairs. Keys are strings and values can be `string`, `numeric`, `boolean`, [`Date`](http://www.w3schools.com/jsref/jsref_obj_date.asp) objects, arrays, or nested JSON objects.

To add metadata properties, use the following event-logging method.

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

{% tab unreal engine %}
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
The `time` and `event_name` keys are reserved and cannot be used as custom event properties.
{% endalert %}

## Best practices

There are three important checks to carry out so that your custom event properties log as expected:

* [Establish which events are logged](#verify-events)
* [Verify log](#verify-log)
* [Verify values](#verify-values)

Multiple properties may be logged each time a custom event is logged.

### Verify events

Check with your developers which event properties are being tracked. Keep in mind that all event properties are case-sensitive. For additional information on tracking custom events, check out these articles based on your platform:

* [Android]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android)
* [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift)
* [Web]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)

### Verify log

To confirm that the event properties are successfully tracked, you can view all event properties from the **Custom Events** page.

1. Go to **Data Settings** > **Custom Events**.
2. Locate your custom event from the list.
3. For your event, select **Manage Properties** to view the names of the properties associated with an event.

### Verify values

After [adding your user as a test user]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/#adding-test-users), follow these steps to verify your values: 

1. Perform the custom event within the app.
2. Wait for roughly 10 seconds for the data to flush.
3. Refresh the [Event User Log]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) to view the custom event and the event property value that was passed with it.