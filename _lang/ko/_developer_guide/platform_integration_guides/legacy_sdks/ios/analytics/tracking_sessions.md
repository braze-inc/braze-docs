---
nav_title: 추적 세션
article_title: iOS용 세션 추적
platform: iOS
page_order: 0
description: "이 참조 문서에서는 iOS 애플리케이션의 세션 업데이트를 구독하는 방법을 설명합니다."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# iOS용 세션 추적

Braze SDK는 사용자 인게이지먼트를 계산하기 위해 Braze 대시보드에서 사용하는 세션 데이터 및 사용자를 이해하는 데 핵심적인 기타 분석을 보고합니다. SDK는 다음 세션 의미 체계에 따라 Braze 대시보드 내에서 볼 수 있는 세션 길이와 세션 수를 설명하는 '세션 시작' 및 '세션 종료' 데이터 포인트를 생성합니다.

## 세션 수명 주기

`[[Appboy sharedInstance]` `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions]`를 호출하면 세션이 시작되며, 이후 기본적으로 세션은 `UIApplicationWillEnterForegroundNotification` 알림이 실행될 때(예: 앱이 포그라운드에 표시될 때) 시작되고 앱이 포그라운드를 벗어날 때(예: `UIApplicationDidEnterBackgroundNotification` 알림이 실행되거나 앱이 종료될 때) 종료됩니다.

{% alert note %}
새 세션을 강제로 시작해야 하는 경우 사용자를 변경하면 됩니다.
{% endalert %}

## 세션 시간 초과 사용자 지정

Braze iOS SDK v3.14.1부터는 Info.plist 파일을 사용하여 세션 제한 시간을 설정할 수 있습니다. `Info.plist` 파일에 `Braze` 사전을 추가합니다. `Braze` 사전에서 `SessionTimeout` 숫자 하위 항목을 추가하고 값을 커스텀 세션 제한 시간으로 설정합니다. Braze iOS SDK v4.0.2 이전 버전에서는 `Braze` 대신 `Appboy`의 사전 키를 사용해야 합니다.

또는 [`startWithApiKey`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#afd911d60dfe7e5361afbfb364f5d20f9)에 전달된 `appboyOptions` 오브젝트에서 `ABKSessionTimeoutKey` 키를 원하는 정수 값으로 설정할 수 있습니다.

{% tabs %}
{% tab 목표-C %}

```objc
// Sets the session timeout to 60 seconds
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKSessionTimeoutKey : @(60) }];
```

{% endtab %}
{% tab swift %}

```swift
// Sets the session timeout to 60 seconds
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKSessionTimeoutKey : 60 ])
```
{% endtab %}
{% endtabs %}

세션 시간 제한을 설정한 경우 세션 시맨틱은 모두 해당 사용자 지정 시간 제한으로 확장됩니다.

{% alert note %}
`sessionTimeoutInSeconds` 의 최소값은 1초입니다. 기본값은 10초입니다.
{% endalert %}

## 테스트 세션 추적

사용자를 통해 세션을 감지하려면 대시보드에서 사용자를 찾고 고객 프로필에서 **앱 사용**으로 이동합니다. '세션' 측정기준이 예상했던 시점에 증가하는지 확인하여 세션 추적 기술이 작동함을 확인할 수 있습니다.

![사용자 프로필의 앱 사용 섹션에 세션 수, 마지막으로 사용한 날짜, 처음 사용한 날짜가 표시됩니다.]({% image_buster /assets/img_archive/test_session.png %})

