---
nav_title: 사용자 지정 이벤트 추적
article_title: iOS용 사용자 지정 이벤트 추적
platform: Swift
page_order: 2
description: "이 참조 문서에서는 Swift SDK에 대한 커스텀 이벤트를 추가하고 추적하는 방법을 다룹니다."

---

# 사용자 지정 이벤트 추적

> Braze에서 커스텀 이벤트를 기록하여 앱의 사용 패턴에 대해 자세히 알아보고 대시보드에서 사용자의 작업에 따라 사용자를 세분화할 수 있습니다.

구현하기 전에 [이벤트 명명 규칙]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/)의 참고 사항과 함께 [모범 사례]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection)에서 커스텀 이벤트, 커스텀 속성 및 구매 이벤트가 제공하는 세분화 옵션 예제를 검토하세요.

## 사용자 지정 이벤트 추가하기

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.logCustomEvent(name: "YOUR_EVENT_NAME")
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze logCustomEvent:@"YOUR_EVENT_NAME"];
```

{% endtab %}
{% endtabs %}

### 속성정보 추가

`Int`, `Double`, `String`, `Bool` 또는 `Date` 값으로 채워진 `Dictionary`를 전달하여 커스텀 이벤트에 대한 메타데이터를 추가할 수 있습니다.

{% tabs %}
{% tab swift %}

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

{% endtab %}
{% tab 목표-C %}

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

{% endtab %}
{% endtabs %}

### 예약 키 {#event-reserved-keys}

다음 키는 예약되어 있으며 사용자 지정 이벤트 속성으로 사용할 수 없습니다:

- `time`
- `event_name`

## 추가 리소스

- 로그 커스텀 이벤트에 대한 [`logCustomEvent`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/logcustomevent(name:properties:fileid:line:) "로그 커스텀 이벤트 문서") 문서를 참조하세요.

