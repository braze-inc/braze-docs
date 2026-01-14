# ストレージ

> この記事では、Braze Android SDK を使用する際にキャプチャされるさまざまなデバイスレベルのプロパティについて説明します。

## デバイスのプロパティ

デフォルトでは、Braze は以下の[デバイスレベルプロパティ](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.enums/-device-key/index.html)を収集し、デバイス、言語、タイムゾーンベースのメッセージのパーソナライズを可能にします。

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
`AD_TRACKING_ENABLED` と `TIMEZONE` は `null` または空白の場合は収集されません。`GOOGLE_ADVERTISING_ID` は SDK によって自動的に収集されないため、[`setGoogleAdvertisingId`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html) 経由で渡す必要があります。
{% endalert %}

収集するプロパティを無効にしたり指定したりするには、[`BrazeConfig.Builder.setDeviceObjectAllowlistEnabled()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html) と [`BrazeConfig.Builder.setDeviceObjectAllowlist()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html) を使用してプロパティを設定します。

次の例では、デバイスオブジェクトに Android OS のバージョンとデバイスのロケールのみを含めるようにデバイスオブジェクトを許可リストに登録する方法を示します。
```
  new BrazeConfig.Builder()
      .setDeviceObjectAllowlistEnabled(true)
      .setDeviceObjectAllowlist(EnumSet.of(DeviceKey.ANDROID_VERSION, DeviceKey.LOCALE));
```
デフォルトでは、すべてのフィールドが有効になっています。いくつかのプロパティがないと一部の機能が正しく機能しないことがあるので注意してください。たとえば、ローカルタイムゾーンの配信はタイムゾーンなしでは機能しません。

自動的に収集されるデバイスプロパティの詳細については、[SDK データ収集]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/)に関する記事をご確認ください。


