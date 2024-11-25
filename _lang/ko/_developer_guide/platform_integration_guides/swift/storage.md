---
nav_title: 저장
article_title: iOS용 저장소
platform: Swift
page_order: 8.9
page_type: reference
description: "이 참조 문서에서는 Braze iOS Swift SDK에서 캡처한 기기 수준의 속성정보를 설명합니다."
---

# 저장

> 이 문서에서는 Braze iOS Swift SDK를 사용할 때 캡처되는 다양한 기기 수준의 속성정보를 설명합니다.

## 기기 속성정보

기본적으로 Braze는 기기, 언어, 시간대를 기반으로 메시지를 개인화할 수 있도록 다음과 같은 [기기 수준 속성정보](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty)를 수집합니다.

* 기기 통신사([`CTCarrier` 지원 중단](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty/carrier)의 메모 참조)
* 기기 로케일
* 기기 모델
* 기기 OS 버전
* 푸시 권한 부여 상태
* 푸시 디스플레이 옵션
* 푸시 활성화됨
* 기기 해상도
* 기기 시간대

{% alert note %}
Braze 소프트웨어 개발 키트는 IDFA를 자동으로 수집하지 않습니다. 앱은 바로 아래의 메서드를 구현하여 선택적으로 IDFA를 Braze에 전달할 수 있습니다. 앱은 앱 추적 투명성 프레임워크를 통해 최종사용자로부터 추적에 대한 명시적인 옵트인을 확보한 후에 IDFA를 Braze에 전달해야 합니다.

1. 광고 추적 상태를 설정하려면 [`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:)/)을 사용하십시오.
2. 광고주 식별자(IDFA)를 설정하려면 [`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/)를 사용합니다
{% endalert %}

구성 가능한 기기 필드는 [`Braze.Configuration.DeviceProperty`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty) 열거형에 정의되어 있습니다. 허용 목록에 추가하려는 기기 필드를 지정하거나 비활성화하려면 필드를 `configuration` 오브젝트의 [`devicePropertyAllowList`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/devicepropertyallowlist) 속성정보에 추가합니다.

예를 들어 허용 목록에 추가할 시간대 및 로캘 컬렉션을 지정하려면 다음과 같이 설정합니다.

{% tabs %}
{% tab swift %}

```swift
configuration.devicePropertyAllowList = [.timeZone, .locale]
```

{% endtab %}
{% tab 목표-C %}

```objc
configuration.devicePropertyAllowList = @[
    BRZDeviceProperty.timeZone,
    BRZDeviceProperty.locale
];
```

{% endtab %}
{% endtabs %}

기본적으로 모든 필드가 활성화되어 있습니다. 일부 속성이 없으면 모든 기능이 제대로 작동하지 않을 수 있습니다. 예를 들어, 현지 시간대 전달은 시간대가 없으면 작동하지 않습니다.

자동으로 수집된 기기 속성정보에 대한 자세한 내용은 [SDK 데이터 수집]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/)을 참조하세요.

