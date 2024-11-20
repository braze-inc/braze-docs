---
nav_title: 커스텀 보기 컨트롤러
article_title: iOS용 커스텀 보기 컨트롤러의 인앱 메시지
platform: iOS
page_order: 7
description: "이 참조 문서에서는 iOS 애플리케이션에 커스텀 인앱 메시징 보기 컨트롤러를 활용하는 방법을 다룹니다."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 사용자 지정 보기 컨트롤러에 인앱 메시지 표시

인앱 메시지는 커스텀 보기 컨트롤러 내에 표시할 수도 있으며, 이를 Braze에 전달할 수도 있습니다. Braze는 사용자 지정된 인앱 메시지를 애니메이션으로 표시하거나 해제하고 인앱 메시지 분석을 처리합니다. 뷰 컨트롤러는 다음 요구 사항을 충족해야 합니다:

- `ABKInAppMessageViewController` 의 서브클래스 또는 인스턴스여야 합니다.
- 반환된 보기 컨트롤러의 보기는 `ABKInAppMessageView`의 인스턴스 또는 해당 서브클래스여야 합니다.

다음 UI 위임 메서드는 인앱 메시지를 `ABKInAppMessageViewController`로 제공할 때마다 호출되어 앱이 인앱 메시지 표시를 위해 커스텀 보기 컨트롤러를 Braze에 전달할 수 있도록 합니다.

{% tabs %}
{% tab 목표-C %}

```objc
- (ABKInAppMessageViewController *)inAppMessageViewControllerWithInAppMessage:(ABKInAppMessage *)inAppMessage;
```

{% endtab %}
{% tab swift %}

```swift
func inAppMessageViewControllerWithInAppMessage(inAppMessage: ABKInAppMessage!) -> ABKInAppMessageViewController!
```

{% endtab %}
{% endtabs %}

[인앱 메시지 보기 컨트롤러는](https://github.com/Appboy/appboy-ios-sdk/tree/master/AppboyUI/ABKInAppMessage/ViewControllers) 사용자 지정할 수 있습니다. 하위 클래스 또는 카테고리를 사용하여 인앱 메시지의 표시 또는 동작을 사용자 지정할 수 있습니다.

## 메서드 선언

추가 정보는 다음 헤더 파일을 참조하십시오:

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)

## 구현 샘플

인앱 메시지 샘플 앱에서 [`ViewController.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/ViewController.m) 및 [`CustomInAppMessageViewController.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/)을 참조하세요.

