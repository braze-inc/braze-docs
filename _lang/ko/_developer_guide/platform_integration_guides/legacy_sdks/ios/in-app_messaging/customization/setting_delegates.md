---
nav_title: 대리인 설정
article_title: iOS용 인앱 메시지 델리게이트 설정하기
platform: iOS
page_order: 2
description: "이 참조 문서에서는 iOS 애플리케이션의 인앱 메시징 위임 설정을 다룹니다."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 대리인 설정

인앱 메시지 표시 및 전달을 위임(선택 사항)을 설정하여 코드에서 사용자 지정할 수 있습니다.

## 인앱 메시지 위임

[`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h) 위임은 추가 처리를 위해 트리거된 인앱 메시지 페이로드를 수신하고 표시 생애주기 이벤트를 수신하며 표시 타이밍을 제어하는 데 사용할 수 있습니다. 

다음을 호출하여 `ABKInAppMessageUIDelegate` Braze 인스턴스에서 위임 오브젝트를 설정합니다.

{% tabs %}
{% tab 목표-C %}

```objc
[[Appboy sharedInstance].inAppMessageController.inAppMessageUIController setInAppMessageUIDelegate:self];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController?.setInAppMessageUIDelegate?(self)
```

{% endtab %}
{% endtabs %}

구현 예제는 인앱 메시지 [샘플 앱](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/ViewController.m)을 확인하세요. 프로젝트에 Braze UI 라이브러리를 포함하지 않은 경우(흔하지 않음) 이 위임은 사용할 수 없습니다.

## 핵심 인앱 메시지 위임

프로젝트에 Braze UI 라이브러리를 포함하지 않고 앱에서 커스텀 표시 또는 추가 처리를 위해 트리거된 인앱 메시지 페이로드를 수신하려는 경우 [`ABKInAppMessageControllerDelegate`]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/) 프로토콜을 구현합니다.

다음을 호출하여 `ABKInAppMessageControllerDelegate` Braze 인스턴스에서 위임 오브젝트를 설정합니다.

{% tabs %}
{% tab 목표-C %}

```objc
[Appboy sharedInstance].inAppMessageController.delegate = self;
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.inAppMessageController.delegate = self
```

{% endtab %}
{% endtabs %}

또는 `ABKInAppMessageControllerDelegateKey` 키를 사용하여 `appboyOptions`를 통해 초기화할 때 핵심 인앱 메시지 위임을 설정할 수도 있습니다.
{% tabs %}
{% tab 목표-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKInAppMessageControllerDelegateKey : self }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKInAppMessageControllerDelegateKey : self ])
```
{% endtab %}
{% endtabs %}

## 메서드 선언

추가 정보는 다음 헤더 파일을 참조하십시오:

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)
- [`ABKInAppMessageControllerDelegate.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageControllerDelegate.h)

## 구현 샘플

인앱 메시지 샘플 앱에서 [`ViewController.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/ViewController.m)을 참조하세요.


