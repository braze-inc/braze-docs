---
nav_title: 統合の完了
article_title: Swift SDKの統合を完了する
platform: Swift
description: "この参考記事では、Braze Swift SDKを統合オプションの1つを介してインストールした後、統合を完了する方法を示す。"
page_order: 2

---

# 統合の完了

> これらのステップに従う前に、[Swift Package Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/)または[CocoaPodsの]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/cocoapods/)いずれかを使用してiOS用のSwift SDKを統合していることを確認する。

## アプリデリゲートを更新する

{% tabs %}
{% tab 速い %}

Braze Swift SDKに含まれる機能をインポートするために、`AppDelegate.swift` ファイルに以下のコード行を追加する：

```swift
import BrazeKit
```


次に、`AppDelegate` クラスに static プロパティを追加し、アプリケーションのライフタイムを通して Braze インスタンスへの強い参照を保持する：

```swift
class AppDelegate: UIResponder, UIApplicationDelegate {
  static var braze: Braze? = nil
}
```

最後に、`AppDelegate.swift` 、以下のスニペットを`application:didFinishLaunchingWithOptions:` メソッドに追加する：

```swift
let configuration = Braze.Configuration(
    apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
    endpoint: "YOUR-BRAZE-ENDPOINT"
)
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

**アプリの設定**ページから、`YOUR-APP-IDENTIFIER-API-KEY` と`YOUR-BRAZE-ENDPOINT` を正しい値に更新する。アプリ識別子のAPIキーがどこにあるかについては、[API識別子の種類を]({{site.baseurl}}/api/identifier_types/?tab=app%20ids)チェックしてほしい。

{% endtab %}
{% tab 目標-C %}

次のコード行を `AppDelegate.m` ファイルに追加します。

```objc
@import BrazeKit;
```

次に、`AppDelegate.m` ファイルに静的変数を追加して、アプリケーションのライフタイムを通してBrazeインスタンスへの参照を保持する：

```objc
static Braze *_braze;

@implementation AppDelegate
+ (Braze *)braze {
  return _braze;
}

+ (void)setBraze:(Braze *)braze {
  _braze = braze;
}
@end
```

最後に、`AppDelegate.m` ファイル内で、`application:didFinishLaunchingWithOptions:` メソッド内に以下のスニペットを追加する：

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:"YOUR-APP-IDENTIFIER-API-KEY"
                                                                  endpoint:"YOUR-BRAZE-ENDPOINT"];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

**Manage Settings**ページから、`YOUR-APP-IDENTIFIER-API-KEY` と`YOUR-BRAZE-ENDPOINT` を正しい値で更新する。アプリ識別子の API キーの場所について詳しくは、[API ドキュメント]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key)をご覧ください。

{% endtab %}
{% endtabs %}


## SDK 統合の完了

この時点で、基本的な統合は完了しているはずだ。これでBrazeはアプリケーションからデータを収集するようになるはずだ。この統合ガイドの他の記事に従って、Brazeの全機能とメッセージングチャンネルを実装し、カスタマイズする。

## その他のリソース

[SDKリファレンス・ドキュメントには][1]、各SDKシンボルに関する追加情報とガイダンスが記載されている。

[1]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/ "iOS クラスの完全なドキュメント"
