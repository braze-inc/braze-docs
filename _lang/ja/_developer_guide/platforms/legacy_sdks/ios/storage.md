---
nav_title: ストレージ
article_title: iOS 用ストレージ
platform: iOS
page_order: 8.9
page_type: reference
description: "この参照記事では、Braze iOS SDKがキャプチャするデバイスレベルのプロパティについて説明します。"

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# ストレージ

この記事では、Braze iOS SDK を使用する際にキャプチャされるさまざまなデバイスレベルのプロパティについて説明します。

## デバイスのプロパティ

デフォルトでは、Braze は以下の[デバイスレベルプロパティ](https://github.com/Appboy/appboy-ios-sdk/blob/16e893f2677af7de905b927505d4101c6fb2091d/AppboyKit/headers/AppboyKitLibrary/Appboy.h#L181)を収集し、デバイス、言語、タイムゾーンベースのメッセージのパーソナライズを可能にします。

* デバイスの解像度
* デバイスの通信事業者
* デバイスのロケール
* デバイスモデル
* デバイス OS のバージョン
* IDFV ([iOS SDK v5.7.0以上](https://github.com/braze-inc/braze-swift-sdk)ではオプション)
* プッシュ通知が有効
* デバイスのタイムゾーン
* プッシュ許可のステータス
* 広告の追跡が有効

{% alert note %}
Braze SDK はIDFA を自動的に収集しません。アプリはオプションで、当社の `ABKIDFADelegate` プロトコルを実装することで IDFA を Braze に渡すことができます。アプリは IDFA を Braze に渡す前に、アプリトラッキングの透明性フレームワークを通じてトラッキングへの明示的なエンドユーザーオプトインを取得する必要があります。
{% endalert %}

設定可能なデバイスフィールドは、[`ABKDeviceOptions`](https://github.com/Appboy/appboy-ios-sdk/blob/4390e9eac8401bccdb81b053fa54eb87b1f6fcaa/Appboy-tvOS-SDK/AppboyTVOSKit.framework/Headers/Appboy.h#L179) 列挙で定義されます。許可リストに登録したいデバイスフィールドを無効化または指定するには、`startWithApiKey:inApplication:withAppboyOptions:` の `appboyOptions` で目的のフィールドのビット単位の `OR` を [`ABKDeviceAllowlistKey`](https://github.com/Appboy/appboy-ios-sdk/blob/fed071000722673754da288cace15c1ff8aca432/AppboyKit/include/Appboy.h#L148) に割り当てます。

たとえば、許可リストに登録するタイムゾーンとロケール収集を指定するには、次のように設定します。
```
appboyOptions[ABKDeviceAllowlistKey] = @(ABKDeviceOptionTimezone | ABKDeviceOptionLocale);
```

デフォルトでは、すべてのフィールドが有効になっています。いくつかのプロパティがないと一部の機能が正しく機能しないことがあるので注意してください。たとえば、ローカルタイムゾーンの配信はタイムゾーンなしでは機能しません。

自動的に収集されるデバイスプロパティの詳細については、[SDK データ収集]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/)をご覧ください。 
