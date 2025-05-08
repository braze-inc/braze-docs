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

デフォルトでは、Braze は以下の[デバイスレベルプロパティ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty)を収集し、デバイス、言語、タイムゾーンベースのメッセージのパーソナライズを可能にします。

* デバイスの通信事業者 ([`CTCarrier` 非推奨](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty/carrier)に関する注記を参照)
* デバイスのロケール
* デバイスモデル
* デバイス OS のバージョン
* プッシュ認証ステータス
* プッシュ表示オプション
* プッシュ通知が有効
* デバイスの解像度
* デバイスのタイムゾーン

{% alert note %}
Braze SDK はIDFA を自動的に収集しません。アプリはオプションで、以下のメソッドを直接実装することで IDFA を Braze に渡すことができます。アプリは IDFA を Braze に渡す前に、アプリトラッキングの透明性フレームワークを通じてエンドユーザーによるトラッキングへの明示的なオプトインを取得する必要があります。

1. 広告のトラッキング状態を設定するには [`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:)/) を使用します。
2. 広告主の識別子 (IDFA) を設定するには、[`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/) を使用します。
{% endalert %}

設定可能なデバイスフィールドは、[`Braze.Configuration.DeviceProperty`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty) 列挙で定義されます。許可リストに登録したいデバイスフィールドを無効化または指定するには、`configuration` オブジェクトの [`devicePropertyAllowList`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/devicepropertyallowlist) プロパティにフィールドを追加します。

たとえば、許可リストに登録するタイムゾーンとロケール収集を指定するには、次のように設定します。

{% tabs %}
{% tab SWIFT %}

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

自動的に収集されるデバイスプロパティの詳細については、[SDK データ収集]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/)をご覧ください。

