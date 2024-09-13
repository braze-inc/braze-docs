---
nav_title: 스토리지
article_title: iOS용 스토리지
platform: iOS
page_order: 8.9
page_type: reference
description: "이 참조 문서에서는 Braze iOS SDK에서 캡처한 디바이스 수준 프로퍼티에 대해 설명합니다."

noindex: true
---

{% multi_lang_include 사용 중단/목적-c.md %}

# 스토리지

이 문서에서는 Braze iOS SDK를 사용할 때 캡처되는 다양한 디바이스 수준 프로퍼티에 대해 설명합니다.

## 장치 속성

기본적으로 Braze는 다음과 같은 [디바이스 수준 속성을](https://github.com/Appboy/appboy-ios-sdk/blob/16e893f2677af7de905b927505d4101c6fb2091d/AppboyKit/headers/AppboyKitLibrary/Appboy.h#L181) 수집하여 디바이스, 언어, 시간대를 기반으로 메시지를 맞춤 설정할 수 있도록 합니다:

* 장치 해상도
* 기기 통신사
* 기기 로케일
* 기기 모델
* 장치 OS 버전
* IDFV( [iOS SDK v5.7.0 이상](https://github.com/braze-inc/braze-swift-sdk)에서 선택 사항)
* 푸시 활성화됨
* 기기 시간대
* 푸시 인증 상태
* 광고 추적 활성화됨

{% alert note %}
Braze SDK는 IDFA를 자동으로 수집하지 않습니다. 앱은 선택적으로 저희의 `ABKIDFADelegate` 프로토콜을 구현하여 IDFA를 Braze에 전달할 수 있습니다. 앱은 앱 추적 투명성 프레임워크를 통해 추적에 대한 명시적인 최종 사용자의 동의를 얻은 후에 IDFA를 Braze에 전달해야 합니다.
{% endalert %}

구성 가능한 장치 필드는 [`ABKDeviceOptions`](https://github.com/Appboy/appboy-ios-sdk/blob/4390e9eac8401bccdb81b053fa54eb87b1f6fcaa/Appboy-tvOS-SDK/AppboyTVOSKit.framework/Headers/Appboy.h#L179) 열거형에 정의됩니다. 허용 목록에 추가할 장치 필드를 비활성화하거나 지정하려면 원하는 필드의 비트 단위 `OR` 를 [...]에 할당합니다. [`ABKDeviceAllowlistKey`](https://github.com/Appboy/appboy-ios-sdk/blob/fed071000722673754da288cace15c1ff8aca432/AppboyKit/include/Appboy.h#L148) 를 `startWithApiKey:inApplication:withAppboyOptions:` 의 `appboyOptions` 에 지정합니다.

예를 들어 허용 목록에 추가할 시간대 및 로캘 컬렉션을 지정하려면 다음과 같이 설정합니다:
```
appboyOptions[ABKDeviceAllowlistKey] = @(ABKDeviceOptionTimezone | ABKDeviceOptionLocale);
```

기본적으로 모든 필드가 활성화되어 있습니다. 일부 속성이 없으면 모든 기능이 제대로 작동하지 않을 수 있습니다. 예를 들어, 현지 시간대 배달은 시간대가 없으면 작동하지 않습니다.

자동으로 수집된 디바이스 속성에 대한 자세한 내용은 [SDK 데이터 수집을]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/) 참조하세요. 
