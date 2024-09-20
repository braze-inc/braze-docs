---
nav_title: その他の SDK カスタマイズ
article_title: Swift用のその他のSDKカスタマイズ
platform: Swift
description: "この文書では、Braze Swift SDKを設定するための追加手順を説明する。"
page_order: 3

---

# Swift用のその他のSDKカスタマイズ

> Braze Swift SDKは、Brazeインスタンスにアタッチされた`Braze.Configuration` オブジェクトのメンバープロパティを変更することで設定できる。設定は、Brazeインスタンスを`Braze(configuration:)` で初期化する前にのみ行えることに注意。

利用可能なコンフィギュレーションの全リストは、[Braze.Configuration クラスのドキュメントを][1]参照のこと。

## Braze ログレベル

Braze Swift SDKのデフォルトのログレベルは、次の表の`.error` 。このレベルは、完全に無効化されたロギングを上回る最も最小のレベルである。

次の使用可能なログレベルのリストを参照してください。

| Swift       | Objective-C              | 説明                                                       |
|-------------|--------------------------|-------------------------------------------------------------------|
| `.debug`    | `BRZLoggerLevelDebug`    | デバッグ情報のログ`.info` + `.error`                    |
| `.info`     | `BRZLoggerLevelInfo`     | 一般的なSDK情報（ユーザーの変更など）を記録する +`.error` 。 |
| `.error`    | `BRZLoggerLevelError`    | ログのエラー。                                                       |
| `.disabled` | `BRZLoggerLevelDisabled` | ロギングは行われない。                                                |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### ログレベルの設定

ログ・レベルは、`Braze.Configuration` オブジェクトの実行時に割り当てることができる：

{% tabs %}
{% tab 速い %}

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
{% tab 目標-C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:self.APIKey
                                                                  endpoint:self.apiEndpoint];
// Enable logging of general SDK information (such as user changes, etc.)
[configuration.logger setLevel:BRZLoggerLevelInfo];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
```

{% endtab %}
{% endtabs %}

Braze Loggerの完全な使い方については、[Loggerクラスのドキュメントを][2]参照のこと。

[1]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class
[2]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/logger-swift.class
