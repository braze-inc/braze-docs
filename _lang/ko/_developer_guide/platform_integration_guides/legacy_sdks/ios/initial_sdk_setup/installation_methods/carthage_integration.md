---
nav_title: 카르타고
article_title: iOS용 Carthage 통합
platform: iOS
page_order: 1
description: "이 참조 문서에서는 iOS용 Carthage를 사용하여 Braze SDK를 통합하는 방법을 설명합니다."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 카르타고 통합

## SDK 가져오기

버전 `4.4.0`부터 Carthage를 통해 통합할 때 Braze SDK는 XCFrameworks를 지원합니다. 전체 SDK를 가져오려면 `Cartfile`에 다음 줄을 포함합니다.
```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk.json"
github "SDWebImage/SDWebImage"
```

SDK 가져오기에 대한 자세한 지침은 [Carthage 빠른 시작 가이드](https://github.com/Carthage/Carthage#quick-start)를 참조하세요.

`4.4.0` 이전 버전에서 마이그레이션하는 경우 [XCFrameworks용 Carthage 마이그레이션 가이드](https://github.com/Carthage/Carthage#migrating-a-project-from-framework-bundles-to-xcframeworks)를 따르세요.

{% alert note %}
`Cartfile`의 구문 또는 버전 고정과 같은 기능에 대한 자세한 내용은 [Carthage 설명서](https://github.com/Carthage/Carthage/blob/master/Documentation/Artifacts.md#cartfile)를 참조하세요.
플랫폼별 Carthage 사용법은 해당 [사용 설명서](https://github.com/Carthage/Carthage#if-youre-building-for-ios-tvos-or-watchos)를 참조하세요.
{% endalert %}

### 이전 버전

`3.24.0`~`4.3.4` 버전의 경우 `Cartfile`에 다음을 포함합니다.
```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk_full.json"
```

`3.24.0` 이전 버전을 가져오려면 `Cartfile`에 다음을 포함합니다.
```
github "Appboy/Appboy-iOS-SDK" "<BRAZE_IOS_SDK_VERSION>"
```

`<BRAZE_IOS_SDK_VERSION>`을 'x.y.z' 형식의 [적절한 버전](https://github.com/Appboy/appboy-ios-sdk/releases)에 해당하는 Braze iOS SDK로 바꾸어야 합니다.

## 다음 단계

[통합을 완료하려면]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/) 지침을 따르세요.

## 코어 전용 통합

UI 구성요소나 종속성 없이 코어 SDK를 사용하려면 `Cartfile`에 다음 줄을 포함하여 Braze Carthage 프레임워크의 코어 버전을 설치합니다.

```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk_core.json"
```

