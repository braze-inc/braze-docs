---
nav_title: 비콘 통합
article_title: iOS용 비콘 통합
platform: iOS
page_order: 4
description: "이 문서에서는 iOS용 인필리온 비콘을 사용하여 사용자 지정 이벤트를 로깅하는 방법에 대해 설명합니다."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 비콘 통합

여기에서는 특정 종류의 비콘을 Braze와 통합하여 세분화 및 메시징을 허용하는 방법을 안내합니다.

## 인필리온 비콘

인피리언 비콘을 설정하고 앱에 통합하면 방문 시작 또는 종료 또는 비콘이 목격되는 등의 사용자 지정 이벤트를 기록할 수 있습니다. 장소 이름이나 체류 시간과 같은 이벤트의 속성을 기록할 수도 있습니다.

사용자가 장소를 입력할 때 사용자 지정 이벤트를 기록하려면 `didBeginVisit` 메서드에 이 코드를 입력합니다:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logCustomEvent:@"Entered %@", visit.place.name];
[[Appboy sharedInstance] flushDataAndProcessRequestQueue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logCustomEvent("Entered %@", visit.place.name)
Appboy.sharedInstance()?.flushDataAndProcessRequestQueue()
```

{% endtab %}
{% endtabs %}

`flushDataAndProcessRequestQueue`를 사용하면 앱이 백그라운드 상태에 있더라도 이벤트가 기록되며, 장소를 떠나는 경우에 대해서도 동일한 프로세스를 구현할 수 있습니다. 이렇게 하면 사용자가 새로 입력하는 장소마다 고유한 사용자 지정 이벤트가 생성되고 증가한다는 점에 유의하세요. 50개 이상의 장소를 생성할 예정이라면 일반 '장소 입력' 사용자 지정 이벤트를 하나 만들고 장소 이름을 이벤트 속성으로 포함시키는 것이 좋습니다.
