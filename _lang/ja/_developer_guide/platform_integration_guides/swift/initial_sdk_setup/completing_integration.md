---
nav_title: 統合の完了
article_title: Swift SDK統合の完了
platform: Swift
description: "この参考記事では、統合オプションの1つを使用して Braze SDK をインストールした後に統合を完了する方法を示します。"
page_order: 2

---

# 統合の完了

> これらの手順を実行する前に、 [Swift Package Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/) または [CocoaPods]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/cocoapods/) を使用して iOS 用 Swift SDK を統合していることを確認してください。

## アプリデリゲートを更新する

{% tabs %}
{% tab swift %}

次のコード行をファイルに追加し `AppDelegate.swift` て、Braze Swift SDKに含まれる機能をインポートします。

```swift
import BrazeKit
```


次に、静的プロパティをクラスに追加し `AppDelegate` て、アプリケーションの有効期間を通じてBrazeインスタンスへの強い参照を維持します。

```swift
class AppDelegate: UIResponder, UIApplicationDelegate {
  static var braze: Braze? = nil
}
```

最後に、 で `AppDelegate.swift`、次のスニペットをメソッドに追加します `application:didFinishLaunchingWithOptions:` 。

```swift
let configuration = Braze.Configuration(
    apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
    endpoint: "YOUR-BRAZE-ENDPOINT"
)
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

`YOUR-BRAZE-ENDPOINT` **アプリ設定**ページから正しい値で更新`YOUR-APP-IDENTIFIER-API-KEY`します。アプリ識別子の API キーの場所の詳細については、 [API 識別子の種類]({{site.baseurl}}/api/identifier_types/?tab=app%20ids) をご覧ください。

{% endtab %}
{% tab OBJECTIVE-C %}

次のコード行を `AppDelegate.m` ファイルに追加します。

```objc
@import BrazeKit;
```

次に、静的変数 `AppDelegate.m` をファイルに追加して、アプリケーションの存続期間を通じて Braze インスタンスへの参照を保持します。

\`\`\`objc
static Braze \*_braze;

@implementation AppDelegate
\+ (Braze \*)braze {
  return \_braze;
}

+ (void)setBraze:(Braze \*)braze {
  \_braze = braze;
}
@end
\`\`\`

次に、`AppDelegate.m` ファイル内の `application:didFinishLaunchingWithOptions:` メソッド内に以下のスニペットを追加します。

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:"YOUR-APP-IDENTIFIER-API-KEY"
                                                                  endpoint:"YOUR-BRAZE-ENDPOINT"];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

[`YOUR-BRAZE-ENDPOINT`**設定の管理**] ページから正しい値で更新`YOUR-APP-IDENTIFIER-API-KEY`します。アプリ識別子の API キーの場所について詳しくは、[API ドキュメント]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key)をご覧ください。

{% endtab %}
{% endtabs %}


## SDK 統合の完了

この時点で、基本的な統合は完了しているはずです。これで、Brazeはアプリケーションからデータを収集しているはずです。この統合ガイドの他の記事に従って、Brazeの全機能とメッセージングチャネルを実装およびカスタマイズしてください。

## その他のリソース

[SDK リファレンス ドキュメント][1]には、各 SDK シンボルに関する追加情報とガイダンスが記載されています。

[1]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/ "iOS クラスの完全なドキュメント"
