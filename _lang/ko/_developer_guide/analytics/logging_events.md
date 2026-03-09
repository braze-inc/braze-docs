---
nav_title: 사용자 지정 이벤트 로그
article_title: Braze SDK를 통해 커스텀 이벤트를 기록합니다.
page_order: 3.1
description: "Braze SDK를 통해 사용자 지정 이벤트를 기록하는 방법을 알아보세요."

---

# 사용자 지정 이벤트 로그

> Braze SDK를 통해 사용자 지정 이벤트를 기록하는 방법을 알아보세요.

{% alert note %}
목록에 없는 래퍼 SDK의 경우 관련 네이티브 Android 또는 Swift 메서드를 대신 사용하세요.
{% endalert %}

## 사용자 지정 이벤트 로깅하기

사용자 지정 이벤트를 기록하려면 다음 이벤트 로깅 방법을 사용하세요.

{% tabs %}
{% tab web %}
표준 웹 SDK 구현의 경우 다음 방법을 사용할 수 있습니다:

```javascript
braze.logCustomEvent("YOUR_EVENT_NAME");
```

대신 Google 태그 관리자를 사용하려면 **사용자 지정 이벤트** 태그 유형을 사용하여 [`logCustomEvent` 메서드를](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent) 호출하고 사용자 지정 이벤트 속성을 포함하여 선택적으로 사용자 지정 이벤트를 Braze에 전송할 수 있습니다. 이렇게 하려면

1. 변수를 사용하거나 이벤트 이름을 입력하여 이벤트 **이름**을 입력합니다.
2. **행 추가** 버튼을 사용하여 이벤트 속성을 추가합니다.

![Braze 작업 태그 구성 설정을 보여주는 대화상자. 포함된 설정은 "태그 유형"(커스텀 이벤트), "이벤트 이름"(버튼 클릭), 및 "이벤트 속성"입니다.]({% image_buster /assets/img/web-gtm/gtm-custom-event.png %})
{% endtab %}

{% tab android %}
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
Braze Cordova 플러그인 메서드를 사용하세요:

```javascript
BrazePlugin.logCustomEvent("YOUR_EVENT_NAME");
```

`logCustomEvent` API는 다음을 수락합니다:
- `eventName` (필수 문자열): 최대 255자를 사용하세요. 이름을 `$`로 시작하지 마세요. 영숫자 및 구두점을 사용하세요.
- `eventProperties` (선택적 객체): 이벤트 메타데이터에 대한 키-값 쌍을 추가하세요. 키는 최대 255자를 사용하고, 키를 `$`로 시작하지 마세요.

속성 값의 경우, `string` (최대 255자), `numeric`, `boolean`, 배열 또는 중첩된 JSON 객체를 사용하세요.

구현 세부정보는 Braze Cordova SDK 소스를 참조하세요:
- [`www/BrazePlugin.js` `logCustomEvent` 메서드 (138-140행)<1>
- [`www/BrazePlugin.js` JSDoc (128-140행)<1>
- [Android 핸들러 `src/android/BrazePlugin.kt` (108-115행)<1>
- [iOS 핸들러 `src/ios/BrazePlugin.m` (308-313행)<1>
- [iOS 메서드 선언 `src/ios/BrazePlugin.h` (24행)<1>
{% endtab %}

{% tab infillion %}
[인필리온 비콘을](https://infillion.com/software/beacons/) Android 앱에 통합한 경우 선택적으로 `visit.getPlace()` 을 사용하여 위치별 이벤트를 기록할 수 있습니다. `requestImmediateDataFlush` 은 앱이 백그라운드에 있는 경우에도 이벤트가 기록되는지 확인합니다.

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

## 메타데이터 속성 추가하기

커스텀 이벤트를 기록할 때, 이벤트와 함께 속성 객체를 전달하여 해당 커스텀 이벤트에 대한 메타데이터를 추가할 수 있는 옵션이 있습니다. 속성은 키-값 쌍으로 정의됩니다. 키는 문자열이며 값은 `string`, `numeric`, `boolean`, [`Date`](http://www.w3schools.com/jsref/jsref_obj_date.asp) 객체, 배열 또는 중첩된 JSON 객체일 수 있습니다.

메타데이터 속성을 추가하려면 다음 이벤트 로깅 메서드를 사용하세요.

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
속성 객체로 커스텀 이벤트 기록하기:

```javascript
var properties = {};
properties["key1"] = "value1";
properties["key2"] = ["value2", "value3"];
properties["key3"] = false;
BrazePlugin.logCustomEvent("YOUR-EVENT-NAME", properties);
```

속성을 인라인으로 전달할 수도 있습니다:

```javascript
BrazePlugin.logCustomEvent("YOUR-EVENT-NAME", {
  "key": "value",
  "amount": 42,
});
```

공식 Cordova 샘플 앱에는 문자열, 숫자, 불리언, 배열 및 중첩 객체 속성이 포함되어 있습니다:
- [`sample-project/www/js/index.js` (230-251행)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/sample-project/www/js/index.js#L230-L251)

샘플 프로젝트 발췌:

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

API 및 네이티브 브리지 세부정보는 다음을 참조하십시오:
- [`www/BrazePlugin.js` JSDoc (128-140행)<1>
- [Android 핸들러 `src/android/BrazePlugin.kt` (108-115행)<1>
- [iOS 핸들러 `src/ios/BrazePlugin.m` (308-313행)<1>
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
`time` 및 `event_name` 키는 예약되어 있으며 사용자 지정 이벤트 속성으로 사용할 수 없습니다.
{% endalert %}

## Best practices

커스텀 이벤트 속성이 예상대로 기록되도록 수행해야 할 세 가지 중요한 확인 사항이 있습니다:

* [어떤 이벤트가 기록되는지 확인](#verify-events)
* [로그 확인](#verify-log)
* [값 확인](#verify-values)

커스텀 이벤트가 기록될 때마다 여러 속성이 기록될 수 있습니다.

### 이벤트 확인

개발자에게 어떤 이벤트 속성정보가 추적되고 있는지 확인하세요. 모든 이벤트 속성은 대소문자를 구분한다는 점을 명심하세요. 커스텀 이벤트 추적에 대한 추가 정보는 플랫폼에 따라 다음 기사를 확인하세요.

* [Android]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android)
* [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift)
* [웹]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)

### 로그 확인

이벤트 속성이 성공적으로 추적되었는지 확인하려면 **커스텀 이벤트** 페이지에서 모든 이벤트 속성을 볼 수 있습니다.

1. **데이터 설정** > **사용자 지정 이벤트로** 이동합니다.
2. 목록에서 커스텀 이벤트를 찾으세요.
3. 이벤트에 대해 **속성 관리**를 선택하여 이벤트와 관련된 속성의 이름을 확인하십시오.

### 값 확인

[테스트 사용자로 사용자 추가한 후]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/#adding-test-users), 값을 확인하려면 다음 단계를 따르십시오: 

1. 앱 내에서 커스텀 이벤트를 수행합니다.
2. 데이터가 플러시될 때까지 약 10초 정도 기다리세요.
3. [이벤트 사용자 로그]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/)를 새로고침하여 커스텀 이벤트 및 함께 전달된 이벤트 속성정보 값을 확인하세요.
