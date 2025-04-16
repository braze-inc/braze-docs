# 저장

> 이 문서에서는 Braze Android SDK를 사용할 때 캡처되는 다양한 기기 수준의 속성정보를 설명합니다.

## 기기 속성정보

기본적으로 Braze는 기기, 언어, 시간대를 기반으로 메시지를 개인화할 수 있도록 다음과 같은 [기기 수준 속성정보](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.enums/-device-key/index.html)를 수집합니다.

* `AD_TRACKING_ENABLED`
* `ANDROID_VERSION`
* `CARRIER`
* `IS_BACKGROUND_RESTRICTED`
* `LOCALE`
* `MODEL`
* `NOTIFICIATION_ENABLED`
* `RESOLUTION`
* `TIMEZONE`

{% alert note %}
`AD_TRACKING_ENABLED` 및 `TIMEZONE`은 `null` 또는 공백인 경우 수집되지 않습니다. `GOOGLE_ADVERTISING_ID`는 SDK에서 자동 수집되지 않으며, [`setGoogleAdvertisingId`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html)를 통해 전달해야 합니다.
{% endalert %}

[`BrazeConfig.Builder.setDeviceObjectAllowlistEnabled()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html) 및 [`BrazeConfig.Builder.setDeviceObjectAllowlist()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html)를 사용하여 수집할 속성정보를 설정해 해당 속성정보를 비활성화하거나 지정할 수 있습니다.

다음 예제에서는 기기 오브젝트에 Android OS 버전과 기기 로캘만 포함하도록 기기 오브젝트를 허용 목록에 추가하는 방법을 보여줍니다.
```
  new BrazeConfig.Builder()
      .setDeviceObjectAllowlistEnabled(true)
      .setDeviceObjectAllowlist(EnumSet.of(DeviceKey.ANDROID_VERSION, DeviceKey.LOCALE));
```
기본적으로 모든 필드가 활성화되어 있습니다. 일부 속성이 없으면 모든 기능이 제대로 작동하지 않을 수 있습니다. 예를 들어, 현지 시간대 전달은 시간대가 없으면 작동하지 않습니다.

자동으로 수집된 기기 속성정보에 대한 자세한 내용은 [SDK 데이터 수집]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/) 문서를 참조하세요.


