---
nav_title: 저장
article_title: iOS용 저장소
page_order: 3.60
page_type: reference
description: "Braze SDK에 저장되는 다양한 기기 수준 등록정보에 대해 알아보세요."
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# 저장

> Braze SDK에 저장되는 다양한 기기 수준 등록정보에 대해 알아보세요.

## 기기 등록정보

기본적으로 Braze는 다음과 같은 기기 수준 등록정보를 수집하여 기기, 언어, 시간대 기반 메시지 개인화를 지원합니다:

{% tabs %}
{% tab web %}
- `BROWSER`
- `BROWSER_VERSION`
- `LANGUAGE`
- `OS`
- `RESOLUTION`
- `TIME_ZONE`
- `USER_AGENT`
{% endtab %}

{% tab android %}
- `AD_TRACKING_ENABLED`
- `ANDROID_VERSION`
- `CARRIER`
- `IS_BACKGROUND_RESTRICTED`
- `LOCALE`
- `MODEL`
- `NOTIFICATION_ENABLED`
- `RESOLUTION`
- `TIMEZONE`

{% alert note %}
`AD_TRACKING_ENABLED` 및 `TIMEZONE`은 `null` 또는 공백인 경우 수집되지 않습니다. `GOOGLE_ADVERTISING_ID`는 SDK에서 자동으로 수집되지 않으며, [`setGoogleAdvertisingId`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html)를 통해 전달해야 합니다.
{% endalert %}
{% endtab %}

{% tab swift %}
- 기기 통신사([`CTCarrier` 지원 중단](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty/carrier)에 대한 참고 사항 참조)
- 기기 로케일
- 기기 모델
- 기기 OS 버전
- 푸시 승인 상태
- 푸시 표시 옵션
- 푸시 활성화됨
- 기기 해상도
- 기기 시간대

{% alert note %}
Braze SDK는 IDFA를 자동으로 수집하지 않습니다. 앱은 바로 아래의 메서드를 구현하여 선택적으로 IDFA를 Braze에 전달할 수 있습니다. 앱은 앱 추적 투명성 프레임워크를 통해 최종 사용자로부터 추적에 대한 명시적인 옵트인을 확보한 후에 IDFA를 Braze에 전달해야 합니다.

1. 광고 추적 상태를 설정하려면 [`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:)/)을 사용하세요.
2. 광고주 식별자(IDFA)를 설정하려면 [`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/)를 사용하세요.
{% endalert %}
{% endtab %}
{% endtabs %}

기본적으로 모든 등록정보가 활성화되어 있습니다. 그러나 수동으로 활성화 또는 비활성화할 수 있습니다. 일부 Braze SDK 기능에는 특정 등록정보(예: 현지 시간대 전달 및 시간대)가 필요하므로 프로덕션에 릴리스하기 전에 구성을 테스트해야 합니다.

{% tabs %}
{% tab web %}
예를 들어 허용 목록에 추가할 기기 언어를 지정할 수 있습니다. 자세한 내용은 [`InitializationOptions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions)의 `devicePropertyAllowlist` 옵션을 참조하세요.

```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    devicePropertyAllowlist: [ braze.DeviceProperties.LANGUAGE ] // list of `DeviceProperties` you want to collect
});
```
{% endtab %}

{% tab android %}
예를 들어 허용 목록에 추가할 Android OS 버전과 기기 로캘을 지정할 수 있습니다. 자세한 내용은 [`setDeviceObjectAllowlistEnabled()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html) 및 [`setDeviceObjectAllowlist()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html) 메서드를 참조하세요. 

```java
new BrazeConfig.Builder()
    .setDeviceObjectAllowlistEnabled(true)
    .setDeviceObjectAllowlist(EnumSet.of(DeviceKey.ANDROID_VERSION, DeviceKey.LOCALE));
```
{% endtab %}

{% tab swift %}
예를 들어 허용 목록에 추가할 시간대 및 로캘 수집을 지정할 수 있습니다. 자세한 내용은 `configuration` 오브젝트의 [`devicePropertyAllowList`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/devicepropertyallowlist) 등록정보를 참조하세요.

{% subtabs %}
{% subtab swift %}

```swift
configuration.devicePropertyAllowList = [.timeZone, .locale]
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
configuration.devicePropertyAllowList = @[
    BRZDeviceProperty.timeZone,
    BRZDeviceProperty.locale
];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert tip %}
자동으로 수집되는 기기 등록정보에 대해 자세히 알아보려면 [SDK 데이터 수집]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/)을 참조하세요.
{% endalert %}

## 쿠키 저장(웹 전용) {#cookies}

[웹 Braze SDK를 초기화](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)하면 새 세션에서 자동으로 갱신되는 400일 만료 쿠키가 생성되어 저장됩니다.

다음과 같은 쿠키가 저장됩니다:

|쿠키|설명|크기|
|---|----|---|---|
|`ab.storage.userId.[your-api-key]`|현재 로그인한 사용자의 변경 여부를 확인하고 이벤트를 현재 사용자와 연결하는 데 사용됩니다.|`changeUser`에 전달된 값의 크기에 따라 다름|
|`ab.storage.sessionId.[your-api-key]`|사용자가 새 세션을 시작하는지 기존 세션을 시작하는지 확인하여 메시지를 동기화하고 세션 분석을 계산하는 데 사용되는 무작위 생성 문자열입니다.|~200바이트|
|`ab.storage.deviceId.[your-api-key]`|익명 사용자를 식별하고 사용자의 기기를 구분하여 기기 기반 메시징을 활성화하는 데 사용되는 무작위 생성 문자열입니다.|~200바이트|
|`ab.optOut`|`disableSDK` 호출 시 사용자의 옵트아웃 환경설정을 저장하는 데 사용됩니다.|~40바이트|
|`ab._gd`|루트 수준 쿠키 도메인을 결정하기 위해 임시로 생성(후 삭제)되며, 이를 통해 SDK가 하위 도메인에서 올바르게 작동할 수 있습니다.|해당 없음|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### 쿠키 만료 변경하기 {#cookie-expiry}

기본적으로 Braze 쿠키는 400일 후에 만료됩니다. 이를 변경하려면 웹 SDK를 초기화할 때 `cookieExpiryInDays` 옵션을 사용하세요. 값은 0보다 커야 하며, 이 옵션을 생략하거나 0 이하로 설정하면 400일 기본값이 적용됩니다. 이 옵션은 웹 SDK 6.6.0 이상이 필요합니다.

```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("API-KEY", {
  baseUrl: "BASE-URL",
  cookieExpiryInDays: 30 // expires after 30 days
});
```

### 쿠키 비활성화하기 {#disable-cookies}

모든 쿠키를 비활성화하려면 웹 SDK를 초기화할 때 [`noCookies`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) 옵션을 사용하세요. 이렇게 하면 하위 도메인 간에 이동하는 익명 사용자를 연결할 수 없으며 각 하위 도메인에 새로운 사용자가 생성됩니다.

```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("API-KEY", {
  baseUrl: "BASE-URL",
  noCookies: true
});
```

일반적으로 Braze 추적을 중지하거나 저장된 브라우저 데이터를 모두 지우려면 각각 [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disableSDK) 및 [`wipeData`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#wipedata) SDK 메서드를 참조하세요. 이 두 가지 메서드는 사용자가 동의를 철회하거나 SDK가 이미 초기화된 후 모든 Braze 기능을 중지하려는 경우에 유용할 수 있습니다.