---
nav_title: ストレージ
article_title: iOS 用ストレージ
platform: Swift
page_order: 8.9
page_type: reference
description: "このリファレンス記事では、Braze iOS Swift SDK によってキャプチャされたデバイスレベルのプロパティについて説明します。"
---

# ストレージ

> この記事では、Braze iOS Swift SDK を使用するときにキャプチャされるさまざまなデバイスレベルのプロパティについて説明します。

## デバイスのプロパティ

デフォルトでは、Braze は以下の[デバイスレベルプロパティ][1]を収集し、デバイス、言語、タイムゾーンベースのメッセージのパーソナライズを可能にします。

* デバイスキャリア ([`CTCarrier`廃止予定に関する注記を参照][2])
* デバイスのロケール
* デバイスモデル
* デバイス OS のバージョン
* プッシュ認証ステータス
* プッシュ表示オプション
* プッシュ通知が有効
* デバイスの解像度
* デバイスのタイムゾーン

{% alert note %}
Braze SDK はIDFA を自動的に収集しません。アプリは、以下のメソッドを直接実装することで、オプションで IDFA を Braze に渡すことができます。アプリは、IDFAをBrazeに渡す前に、アプリ追跡透明性フレームワークを通じてエンドユーザーによる追跡への明示的なオプトインを取得する必要があります。

1. 広告トラッキング状態を設定するには、を使用します[`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:)/)。
2. 広告主の識別子 (IDFA) を設定するには、を使用します。[`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/)
{% endalert %}

設定可能なデバイスフィールドは、[`Braze.Configuration.DeviceProperty`][1] 列挙で定義されます。許可リストに追加するデバイスフィールドを無効化または指定するには、[`devicePropertyAllowList`][3]`configuration`そのフィールドをオブジェクトのプロパティに追加します。

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