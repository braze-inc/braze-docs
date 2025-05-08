---
nav_title: 방향 사용자 지정
article_title: iOS용 인앱 메시지 방향 사용자 지정하기
platform: iOS
page_order: 3
description: "이 참조 문서에서는 iOS 애플리케이션의 인앱 메시지 방향을 설정하는 방법을 다룹니다."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 방향 사용자 지정

## 모든 인앱 메시지의 방향 설정하기

모든 인앱 메시지에 고정 방향을 설정하려면 `ABKInAppMessageUIController`에서 `supportedOrientationMask` 속성정보를 설정하면 됩니다. 앱 호출 후 다음 코드를 `startWithApiKey:inApplication:withLaunchOptions:` 에 추가합니다:

{% tabs %}
{% tab 목표-C %}

```objc
// Set fixed in-app message orientation to portrait.
// Use UIInterfaceOrientationMaskLandscape to display in-app messages in landscape
id<ABKInAppMessageUIControlling> inAppMessageUIController = [Appboy sharedInstance].inAppMessageController.inAppMessageUIController;
((ABKInAppMessageUIController *)inAppMessageUIController).supportedOrientationMask = UIInterfaceOrientationMaskPortrait;
```

{% endtab %}
{% tab swift %}

```swift
// Set fixed in-app message orientation to portrait
// Use .landscape to display in-app messages in landscape
if let controller = Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController as? ABKInAppMessageUIController {
  controller.supportedOrientationMask = .portrait
}
```

{% endtab %}
{% endtabs %}

이렇게 하면 기기 방향에 관계없이 모든 인앱 메시지가 지원되는 방향으로 표시됩니다. 기기의 방향이 인앱 메시지의 `orientation` 속성정보에서도 지원해야 메시지가 표시됩니다.

## 인앱 메시지별 방향 설정

또는 메시지별로 방향을 설정할 수도 있습니다. 이렇게 하려면 [인앱 메시지 위임자를]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/) 설정하세요. 그런 다음, `beforeInAppMessageDisplayed:` 위임 메서드의 `ABKInAppMessage`에서 `orientation` 속성정보를 설정합니다.

{% tabs %}
{% tab 목표-C %}

```objc
// Set inAppMessage orientation to portrait
inAppMessage.orientation = ABKInAppMessageOrientationPortrait;

// Set inAppMessage orientation to landscape
inAppMessage.orientation = ABKInAppMessageOrientationLandscape;
```

{% endtab %}
{% tab swift %}

```swift    
  // Set inAppMessage orientation to portrait
  inAppMessage.orientation = ABKInAppMessageOrientation.portrait

  // Set inAppMessage orientation to landscape
  inAppMessage.orientation = ABKInAppMessageOrientation.landscape
```

{% endtab %}
{% endtabs %}

기기 방향이 인앱 메시지의 `orientation` 속성정보와 일치하지 않으면 인앱 메시지가 표시되지 않습니다.

{% alert note %}
iPads의 경우 인앱 메시지는 실제 화면 방향과 관계없이 사용자가 선호하는 방향 스타일로 표시됩니다.
{% endalert %}

## 메서드 선언

자세한 내용은 다음 헤더 파일을 참조하세요:

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)

