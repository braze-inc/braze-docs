---
nav_title: ストレージ
article_title: iOS 用ストレージ
platform: Swift
page_order: 8.9
page_type: reference
description: "このリファレンス記事では、Braze iOS Swift SDKによってキャプチャされたデバイスレベルのプロパティについて説明する。"
---

# ストレージ

> この記事では、Braze iOS Swift SDKを使用する際に取得されるさまざまなデバイスレベルのプロパティについて説明する。

## デバイスのプロパティ

デフォルトでは、Braze は以下の[デバイスレベルプロパティ][1]を収集し、デバイス、言語、タイムゾーンベースのメッセージのパーソナライズを可能にします。

* デバイスキャリア[（`CTCarrier` 非推奨に関する][2]注記を参照のこと）
* デバイスのロケール
* デバイスモデル
* デバイス OS のバージョン
* プッシュ認証ステータス
* プッシュ表示オプション
* プッシュ通知が有効
* デバイスの解像度
* デバイスのタイムゾーン

{% alert note %}
Braze SDK はIDFA を自動的に収集しません。アプリは、以下のメソッドを直接実装することで、オプションでIDFAをBrazeに渡すことができる。アプリは、IDFAをBrazeに渡す前に、App Tracking Transparencyフレームワークを通じてエンドユーザーからトラッキングに対する明示的なオプトインを得なければならない。

1. 広告のトラッキング状態を設定するには [`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:)/).
2. 広告主の識別子（IDFA）を設定するには、以下を使用する。 [`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/).
{% endalert %}

設定可能なデバイスフィールドは、[`Braze.Configuration.DeviceProperty`][1] 列挙で定義されます。許可リストにしたいデバイス・フィールドを無効にしたり指定したりするには、 オブジェクトの [`devicePropertyAllowList`][3]`configuration` プロパティに追加する。

たとえば、許可リストに登録するタイムゾーンとロケール収集を指定するには、次のように設定します。

{% tabs %}
{% tab 速い %}

```swift
configuration.devicePropertyAllowList = [.timeZone, .locale]
```

{% endtab %}
{% tab 目標-C %}

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