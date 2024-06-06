---
nav_title: その他の SDK カスタマイズ
article_title: iOS 向けのその他の SDK カスタマイズ
platform: Swift
description: "本書では、Braze Swift SDK を設定するための追加手順について説明します。"
page_order: 3

---

# その他の SDK のカスタマイズ

> Braze Swift SDK は、Braze インスタンスにアタッチされた`Braze.Configuration` オブジェクトのメンバープロパティを変更することで設定できます。設定は、`Braze(configuration:)` でBraze インスタンスを初期化する前にのみ行うことができます。

使用可能な設定の完全なリストについては、[Braze.Configurationクラスのドキュメント][1]を参照してください。

## Braze ログレベル

Braze Swift SDK のデフォルトのログレベルは、次のチャートの`.error` です。このレベルは、完全に無効化されたロギングを上回る最小レベルです。

次の使用可能なログレベルのリストを参照してください。

| Swift | Objective-C | 説明|
|-------------|--------------------------|-------------------------------------------------------------------|
| `.debug` | `BRZLoggerLevelDebug` | デバッグ情報+ `.info` + `.error` |
| `.info` | `BRZLoggerLevelInfo` | 一般的なSDK 情報(ユーザーの変更など) + `.error`. |
| `.error` | `BRZLoggerLevelError` | ログエラー|
| `.disabled` | `BRZLoggerLevelDisabled` | ロギングは発生しません。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### ログレベルの設定

ログレベルは、`Braze.Configuration` オブジェクトで実行時に割り当てることができます。

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
// Enable logging of general SDK information (such as user changes, etc.)
configuration.logger.level = .info
let braze = Braze(configuration: configuration)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:self.APIKey
                                                                  endpoint:self.apiEndpoint];
// Enable logging of general SDK information (such as user changes, etc.)
[configuration.logger setLevel:BRZLoggerLevelInfo];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
```

{% endtab %}
{% endtabs %}

ろう付けロガーの使用については、[ロガークラスのドキュメント][2]を参照してください。

[1]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class
[2]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/logger-swift.class