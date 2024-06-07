---
nav_title: ストレージ
article_title: iOS 用ストレージ
platform: Swift
page_order: 8.9
page_type: reference
description: "この参照記事では、Braze iOS SDKがキャプチャするデバイスレベルのプロパティについて説明します。"
---

# ストレージ

> この記事では、Braze iOS SDK を使用する際にキャプチャされるさまざまなデバイスレベルのプロパティについて説明します。

## デバイスのプロパティ

デフォルトでは、Braze は以下の[デバイスレベルプロパティ][1]を収集し、デバイス、言語、タイムゾーンベースのメッセージのパーソナライズを可能にします。

* デバイスキャリア(廃止に関する[`CTCarrier`][2]注記を参照)
* デバイスのロケール
* デバイスモデル
* デバイス OS のバージョン
* プッシュ承認ステータス
* プッシュ表示オプション
* プッシュ通知が有効
* デバイスの解像度
* デバイスのタイムゾーン

{% alert note %}
Braze SDK はIDFA を自動的に収集しません。アプリは、すぐ下のメソッドを実装することで、必要に応じてIDFAをBrazeに渡すことができます。アプリは、IDFAをBrazeに渡す前に、App Tracking Transparencyフレームワークを通じてエンドユーザーによるトラッキングへの明示的なオプトインを取得する必要があります。

1. 広告トラッキングの状態を設定するには、 を使用します [`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:)/)。
2. 広告主の識別子(IDFA)を設定するには、 を使用します [`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/)。
{% endalert %}

設定可能なデバイスフィールドは、[`Braze.Configuration.DeviceProperty`][1] 列挙で定義されます。許可リストに登録するデバイスフィールドを無効化または指定するには、オブジェクトのプロパティ`configuration`に[`devicePropertyAllowList`][3]フィールドを追加します。

たとえば、許可リストに登録するタイムゾーンとロケール収集を指定するには、次のように設定します。

{% tabs %}
{% tab swift %}

```swift
configuration.devicePropertyAllowList = [.timeZone, .locale]
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
configuration.devicePropertyAllowList = @[
    BRZDeviceProperty.timeZone,
    BRZDeviceProperty.locale
];
```

{% endtab %}
{% endtabs %}

デフォルトでは、すべてのフィールドが有効になっています。いくつかのプロパティがないと一部の機能が正しく機能しないことがあるので注意してください。たとえば、ローカルタイムゾーンの配信はタイムゾーンなしでは機能しません。

自動的に収集されるデバイスプロパティの詳細については、[SDK データ収集][4]をご覧ください。

[1]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty
[2]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty/carrier
[3]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/devicepropertyallowlist
[4]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/