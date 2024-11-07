---
nav_title: その他の SDK カスタマイズ
article_title: Swift用のその他のSDKカスタマイズ
platform: Swift
description: "このドキュメントでは、Braze Swift SDK を設定するための追加手順を説明します。"
page_order: 3

---

# Swift用のその他のSDKカスタマイズ

> Braze Swift SDK は、Braze インスタンスに付加されている `Braze.Configuration` オブジェクトのメンバープロパティを変更することで設定できます。設定は、`Braze(configuration:)` を使用して Braze インスタンスを初期化する前にのみ行えます。

使用可能な設定の完全なリストについては、[Braze.Configuration クラスのドキュメント](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class)を参照してください。

## Braze ログレベル

Braze Swift SDK のデフォルトのログレベルは、次の表の `.error` です。このレベルは、完全に無効化されるロギングを上回る最小のレベルです。

次の使用可能なログレベルのリストを参照してください。

| Swift       | Objective-C              | 説明                                                       |
|-------------|--------------------------|-------------------------------------------------------------------|
| `.debug`    | `BRZLoggerLevelDebug`    | デバッグ情報 + `.info` + `.error` をロギングする                    |
| `.info`     | `BRZLoggerLevelInfo`     | 一般的なSDK情報（ユーザーの変更など）を記録する +`.error` 。 |
| `.error`    | `BRZLoggerLevelError`    | エラーをロギングする。                                                       |
| `.disabled` | `BRZLoggerLevelDisabled` | ロギングは行われない。                                                |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### ログレベルの設定

ログレベルは、`Braze.Configuration` オブジェクトでの実行時に割り当てることができます。

{% tabs %}
{% tab SWIFT %}

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

Braze Logger のすべての使用法については、[ロガークラスのドキュメント](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/logger-swift.class)を参照してください。

