---
nav_title: 사용자 지정 이벤트 로깅
article_title: Braze SDK를 통해 사용자 지정 이벤트 로깅하기
page_order: 3.1
description: "Braze SDK를 통해 사용자 지정 이벤트를 기록하는 방법을 알아보세요."

---

# 사용자 지정 이벤트 로깅

> Braze SDK를 통해 사용자 지정 이벤트를 기록하는 방법을 알아보세요.

{% alert note %}
목록에 없는 래퍼 SDK의 경우 관련 네이티브 Android 또는 Swift 메서드를 대신 사용하세요.
{% endalert %}

## 사용자 지정 이벤트 로깅하기

사용자 지정 이벤트를 기록하려면 다음 이벤트 로깅 방법을 사용하세요.

{% tabs %}
{% tab Android %}
네이티브 Android의 경우 다음 방법을 사용할 수 있습니다:

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

[인필리온 비콘을](https://infillion.com/software/beacons/) 앱에 통합한 경우 `visit.getPlace()` 을 추가로 사용하여 위치별 이벤트를 기록할 수 있습니다. `requestImmediateDataFlush` 은 앱이 백그라운드에 있는 경우에도 이벤트가 기록되는지 확인합니다.

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

{% tab 웹 %}
표준 웹 SDK 구현의 경우 다음 방법을 사용할 수 있습니다:

```javascript
braze.logCustomEvent("YOUR_EVENT_NAME");
```

대신 Google 태그 관리자를 사용하려면 **사용자 지정 이벤트** 태그 유형을 사용하여 [`logCustomEvent` 메서드를](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent) 호출하고 사용자 지정 이벤트 속성을 포함하여 선택적으로 사용자 지정 이벤트를 Braze에 전송할 수 있습니다. 이렇게 하려면

1. 변수를 사용하거나 이벤트 이름을 입력하여 이벤트 **이름**을 입력합니다.
2. **행 추가** 버튼을 사용하여 이벤트 속성을 추가합니다.

![Braze 작업 태그 구성 설정을 보여주는 대화상자. 포함된 설정은 '태그 유형'(사용자 지정 이벤트), '이벤트 이름'(버튼 클릭), '이벤트 속성'입니다.]({% image_buster /assets/img/web-gtm/gtm-custom-event.png %})
{% endtab %}

{% tab flutter %}
```dart
braze.logCustomEvent('YOUR_EVENT_NAME');
```
{% endtab %}

{% tab 리액트 네이티브 %}
```javascript
Braze.logCustomEvent("YOUR_EVENT_NAME");
```
{% endtab %}

{% tab roku %}
```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME")
```
{% endtab %}

{% tab 유니티 %}
```csharp
AppboyBinding.LogCustomEvent("YOUR_EVENT_NAME");
```
{% endtab %}

{% tab 언리얼 엔진 %}
```cpp
UBraze->LogCustomEvent(TEXT("YOUR_EVENT_NAME"));
```
{% endtab %}
{% endtabs %}

## 메타데이터 속성 추가하기

사용자 지정 이벤트를 기록할 때 이벤트와 함께 속성 개체를 전달하여 해당 사용자 지정 이벤트에 대한 메타데이터를 추가하는 옵션이 있습니다. 속성은 키-값 쌍으로 정의됩니다. 키는 문자열이며 값은 `string`, `numeric`, `boolean` 또는 [`Date`](http://www.w3schools.com/jsref/jsref_obj_date.asp) 오브젝트일 수 있습니다.

메타데이터 속성을 추가하려면 다음 이벤트 로깅 메서드를 사용합니다.

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

{% tab 웹 %}
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

{% tab flutter %}
```dart
braze.logCustomEvent('custom_event_with_properties', properties: {
    'key1': 'value1',
    'key2': ['value2', 'value3'],
    'key3': false,
});
```
{% endtab %}

{% tab 리액트 네이티브 %}
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

{% tab 유니티 %}
```csharp
AppboyBinding.LogCustomEvent("event name", properties(Dictionary<string, object>));
```
{% endtab %}

{% tab 언리얼 엔진 %}
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
`time` 및 `event_name` 키는 예약되어 있으며 사용자 지정 이벤트 속성으로 사용할 수 없습니다.
{% endalert %}
