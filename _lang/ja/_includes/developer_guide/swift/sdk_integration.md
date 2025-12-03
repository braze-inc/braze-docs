## Swift SDKを統合する

Swiftパッケージマネージャー(SPM)、CocoaPods、または手動の統合方法を使用して、Braze Swift SDKを統合し、カスタマイズすることができる。様々なSDKシンボルの詳細については、[Braze Swiftリファレンスドキュメントを](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/)参照のこと。

### 前提条件

開始する前に、お使いの環境が[最新のBraze Swift SDKバージョンで](https://github.com/braze-inc/braze-swift-sdk#version-information)サポートされていることを確認する。

### ステップ 1: Braze Swift SDKをインストールする。

[Swift Package Manager（SwiftPM）](https://swift.org/package-manager/)または[CocoaPodsを](http://cocoapods.org/)使用して、Braze Swift SDKをインストールすることを推奨する。あるいは、SDKを手動でインストールすることもできる。

{% tabs local %}
{% tab Swift Package Manager %}
#### ステップ1.1：SDK バージョンのインポート

プロジェクトを開き、プロジェクトの設定に移動します。[**Swift パッケージ**] タブを選択し、パッケージリストの下にある <i class="fas fa-plus"></i>[追加] ボタンをクリックします。

![]({% image_buster /assets/img/swiftpackages.png %})

{% alert note %}
バージョン7.4.0から、Braze SWIFT SDKには、[静的XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static)および[ダイナミックなXCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic)としての追加の配布チャネルがあります。これらの形式のいずれかを使用したい場合は、それぞれのリポジトリのインストール手順に従ってください。
{% endalert %}

iOS Swift SDK リポジトリーのURL `https://github.com/braze-inc/braze-swift-sdk` をテキストフィールドに入力します。**依存関係ルール**セクションで、SDKバージョンを選択します。最後に、**パッケージを追加**をクリックします。

![]({% image_buster /assets/img/importsdk_example.png %})

#### ステップ1.2：パッケージを選択する

Braze Swift SDK は、開発者がどの機能をプロジェクトにインポートするかをより詳細に制御できるように、機能をスタンドアロンライブラリーに分離しています。

| パッケージ         | 詳細                                                                                                                                                         |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `BrazeKit`      | 分析とプッシュ通知をサポートする主な SDK ライブラリー                                                                                        |
| `BrazeLocation` | 位置情報ライブラリーは、位置情報分析とジオフェンス監視をサポートします。                                                                              |
| `BrazeUI`       | アプリ内メッセージ、コンテンツカード、バナー用のBraze提供のユーザーインターフェイスライブラリー。デフォルトのUIコンポーネントを使用する場合は、このライブラリーをインポートする。 |

{: .ws-td-nw-1}

##### エクステンション・ライブラリーについて

{% alert warning %}
[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) と [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories) は追加機能を提供する拡張モジュールであり、メインアプリケーションターゲットに直接追加しないでください。代わりにリンクされたガイドに従って、それぞれをそれぞれのターゲット拡張機能に個別に統合してください。
{% endalert %}

| パッケージ                    | 詳細                                                                               |
| -------------------------- | ------------------------------------------------------------------------------------- |
| `BrazeNotificationService` | リッチプッシュ通知をサポートする通知サービス拡張ライブラリー。 |
| `BrazePushStory`           | プッシュストーリーをサポートする通知コンテンツ拡張ライブラリーを提供します。            |

{: .ws-td-nw-1}

ご自身のニーズに最も適したパッケージを選択し、**パッケージを追加**をクリックしてください。必ず最低でも`BrazeKit`を選択してください。

![]({% image_buster /assets/img/add_package.png %})
{% endtab %}

{% tab CocoaPods %}
#### ステップ1.1：CocoaPods をインストールする

完全なウォークスルーは、CocoaPodsの[入門ガイドを](https://guides.cocoapods.org/using/getting-started.html)参照のこと。そうでなければ、以下のコマンドを実行すればすぐに始められる：

```bash
$ sudo gem install cocoapods
```

行き詰まったら、CocoaPodsの[トラブルシューティングガイドを](http://guides.cocoapods.org/using/troubleshooting.html)チェックしよう。

#### ステップ1.2：ポッドファイルの構築

次に、Xcodeプロジェクトのディレクトリに、`Podfile` という名前のファイルを作成する。

{% alert note %}
バージョン7.4.0から、Braze SWIFT SDKには、[静的XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static)および[ダイナミックなXCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic)としての追加の配布チャネルがあります。これらの形式のいずれかを使用したい場合は、それぞれのリポジトリのインストール手順に従ってください。
{% endalert %}

次の行を Podfile に追加します。

```
target 'YourAppTarget' do
  pod 'BrazeKit'
end
```

`BrazeKit` にはメイン SDK ライブラリーが含まれており、分析とプッシュ通知のサポートが提供されています。

ポッドの更新がマイナー バージョンの更新よりも小さいものを自動的に取得するように、Braze をバージョン管理することをお勧めします。これは `pod 'BrazeKit' ~> Major.Minor.Build` のように見えます。大きな変更があっても、Braze SDK の最新バージョンを自動的に統合したい場合は、Podfile で `pod 'BrazeKit'` を使用できます。

##### 追加ライブラリーについて

Braze Swift SDK は、開発者がどの機能をプロジェクトにインポートするかをより詳細に制御できるように、機能をスタンドアロンライブラリーに分離しています。`BrazeKit` に加えて、以下のライブラリーを Podfile に追加できます。

| 図書館               | 詳細                                                                                                                                                         |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pod 'BrazeLocation'` | 位置情報ライブラリーは、位置情報分析とジオフェンス監視をサポートします。                                                                              |
| `pod 'BrazeUI'`       | アプリ内メッセージ、コンテンツカード、バナー用のBraze提供のユーザーインターフェイスライブラリー。デフォルトのUIコンポーネントを使用する場合は、このライブラリーをインポートする。 |

{: .ws-td-nw-1}

###### 拡張ライブラリ

[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) と [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories) は、追加機能を提供するエクステンションモジュールであり、メインアプリケーションターゲットに直接追加すべきではありません。その代わりに、これらのモジュールごとに個別の拡張ターゲットを作成し、対応するターゲットにBrazeモジュールをインポートする必要がある。

| 図書館                          | 詳細                                                                               |
| -------------------------------- | ------------------------------------------------------------------------------------- |
| `pod 'BrazeNotificationService'` | リッチプッシュ通知をサポートする通知サービス拡張ライブラリー。 |
| `pod 'BrazePushStory'`           | プッシュストーリーをサポートする通知コンテンツ拡張ライブラリーを提供します。            |

{: .ws-td-nw-1}

#### ステップ1.3：SDKをインストールする

Braze SDK CocoaPod をインストールするには、ターミナル内で Xcode アプリプロジェクトのディレクトリに移動し、次のコマンドを実行します。
```
pod install
```

この時点で、CocoaPods によって作成された新しい Xcode プロジェクトワークスペースを開くことができるはずです。Xcode プロジェクトの代わりに、必ずこの Xcode ワークスペースを使用してください。

![新しい`BrazeExample.workspace` を表示するために拡張された Braze Example フォルダ]({% image_buster /assets/img/braze_example_workspace.png %})

#### CocoaPodsを使用してSDKを更新する

CocoaPod を更新するには、プロジェクトディレクトリ内で以下のコマンドを実行するだけです。

```
pod update
```
{% endtab %}

{% tab マニュアル %}
#### ステップ1.1：Braze SDKをダウンロード

[GitHubのBraze SDKリリースページ](https://github.com/braze-inc/braze-swift-sdk/releases)に移動し、`braze-swift-sdk-prebuilt.zip`をダウンロードします。

![「GitHub の Braze SDK リリースページ。」]({% image_buster /assets/img/swift/sdk_integration/download-braze-swift-sdk-prebuilt.png %})

#### ステップ1.2：フレームワークを選択してください

Braze SWIFT SDK には、さまざまなスタンドアロンの XCFramework が含まれており、すべてを統合する必要はなく、必要な機能を自由に統合できます。次の表を参照して、XCFrameworksを選択してください:

| パッケージ                    | 必要か | 説明                                                                                                                                                                                                                                                                                                                          |
| -------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `BrazeKit`                 | はい       | メインSDKライブラリーは、分析とプッシュ通知をサポートします。                                                                                                                                                                                                                                                         |
| `BrazeLocation`            | いいえ        | 位置情報ライブラリーは、位置情報分析とジオフェンス監視をサポートします。                                                                                                                                                                                                                                               |
| `BrazeUI`                  | いいえ        | アプリ内メッセージ、コンテンツカード、バナー用のBraze提供のユーザーインターフェイスライブラリー。デフォルトのUIコンポーネントを使用する場合は、このライブラリーをインポートする。                                                                                                                                                                      |
| `BrazeNotificationService` | いいえ        | リッチプッシュ通知をサポートする通知サービス拡張ライブラリー。このライブラリーを直接メインアプリケーションターゲットに追加しないでください。代わりに[この`BrazeNotificationService`ライブラリーを別々に追加してください](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications)。                 |
| `BrazePushStory`           | いいえ        | 通知コンテンツ拡張ライブラリーは、プッシュストーリーをサポートします。このライブラリーを直接メインアプリケーションターゲットに追加しないでください。代わりに[この`BrazePushStory`ライブラリーを別々に追加してください](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories)。                                                 |
| `BrazeKitCompat`           | いいえ        | `Appboy-iOS-SDK` バージョン 4.X.X で使用可能だったすべての `Appboy` および `ABK*` クラスとメソッドを含む互換性ライブラリ。使用の詳細については、[移行ガイド](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/)の最小限の移行シナリオを参照してください。            |
| `BrazeUICompat`            | いいえ        | `Appboy-iOS-SDK` バージョン4.X.Xの `AppboyUI`ライブラリで使用可能だったすべての`ABK*` クラスとメソッドを含む互換性ライブラリ。使用の詳細については、[移行ガイド](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/)の最小限の移行シナリオを参照してください。 |
| `SDWebImage`               | いいえ        | 最小限の移行シナリオで `BrazeUICompat` によってのみ使用される依存関係。                                                                                                                                                                                                                                                           |

{: .ws-td-nw-1 .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### ステップ1.3：ファイルを準備してください

**静的** XCFrameworks または**動的** XCFrameworks のどちらを使用するかを決定してから、ファイルを準備します。

1. XCFrameworks 用の一時ディレクトリーを作成します。
2. `braze-swift-sdk-prebuilt` で、`dynamic` ディレクトリを開き、`BrazeKit.xcframework` を自分のディレクトリに移動します。あなたのディレクトリは次のようになります:
    ```bash
    temp_dir
    └── BrazeKit.xcframework
    ```
3. [選択した各 XCFramework](#swift_step-2-choose-your-frameworks) を一時ディレクトリに移動します。あなたのディレクトリは次のようになります:
    ```bash
    temp_dir
    ├── BrazeKit.xcframework
    ├── BrazeKitCompat.xcframework
    ├── BrazeLocation.xcframework
    └── SDWebImage.xcframework
    ```

#### ステップ1.4:フレームワークを統合する

次に、[以前に準備した](#swift_step-3-prepare-your-files)**動的な** XCFrameworks または**静的な** XCFrameworks を統合します。

Xcodeプロジェクトでビルドターゲットを選択し、次に**一般**を選択します。**フレームワーク、ライブラリ、および埋め込みコンテンツ**の下に、[以前に準備したファイル](#swift_step-3-prepare-your-files)をドラッグ＆ドロップします。

![「各Brazeライブラリーが「埋め込みと署名」に設定されたXcodeプロジェクトの例」]({% image_buster /assets/img/swift/sdk_integration/embed-and-sign.png %})

{% alert note %}
Swift SDK 12.0.0から、スタティックとダイナミックなバリアントの両方で、常にBraze XCFrameworksの**Embed & Signを**選択する必要がある。これにより、フレームワークのリソースがアプリバンドルに適切に埋め込まれるようになる。
{% endalert %}

{% alert tip %}
GIFサポートをイネーブルメントにするには、`braze-swift-sdk-prebuilt/static` か`braze-swift-sdk-prebuilt/dynamic` のどちらかに`SDWebImage.xcframework` を追加する。
{% endalert %}

#### Objective-Cプロジェクトの一般的なエラー

XcodeプロジェクトにOBJECTIVE-Cファイルのみが含まれている場合、プロジェクトのビルドを試みると「シンボルが見つかりません」というエラーが発生することがあります。これらのエラーを修正するには、プロジェクトを開封し、ファイルツリーに空のSWIFTファイルを追加します。これにより、ビルドツールチェーンが[SWIFTランタイム](https://support.apple.com/kb/dl1998)を埋め込み、ビルド時に適切なフレームワークにリンクするようになります。

```bash
FILE_NAME.swift
```

任意のスペースのない文字列で`FILE_NAME`を置き換えます。ファイルは次のようになります。

```bash
empty_swift_file.swift
```
{% endtab %}
{% endtabs local %}

### ステップ 2:遅延初期化の設定（オプション）

アプリがSDKを開始する前に設定を読み込んだり、ユーザーの同意を待つ必要がある場合に便利な、Braze Swift SDKが初期化されるタイミングを遅らせるように選択できる。遅延初期化により、SDKの準備が整うまでBrazeプッシュ通知はキューに入れられる。

これを可能にするには、`Braze.prepareForDelayedInitialization()` にできるだけ早く、できれば`application(_:didFinishLaunchingWithOptions:)` の内部かその前に電話すること。

{% alert note %}
Brazeからのプッシュ通知にのみ適用される。その他のプッシュ通知は、システムデリゲートによって通常通り処理される。
{% endalert %}

{% tabs %}
{% tab Swift %}
{% subtabs local %}
{% subtab UIKit %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
  // Prepare the SDK for delayed initialization
  Braze.prepareForDelayedInitialization()

  // ... Additional non-Braze setup code

  return true
}
```
{% endsubtab %}

{% subtab SwiftUI %}
```swift
@main
struct MyApp: App {
  @UIApplicationDelegateAdaptor var appDelegate: AppDelegate

  var body: some Scene {
    WindowGroup {
      ContentView()
    }
  }
}

class AppDelegate: NSObject, UIApplicationDelegate {
  func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {
    // Prepare the SDK for delayed initialization
    Braze.prepareForDelayedInitialization()

    // ... Additional non-Braze setup code

    return true
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Objective-C %}
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Prepare the SDK for delayed initialization
  [Braze prepareForDelayedInitialization];
  
  // ... Additional non-Braze setup code

  return YES;
}
```
{% endtab %}
{% endtabs %}

{% alert note %}
[`Braze.prepareForDelayedInitialization(pushAutomation:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/preparefordelayedinitialization(pushautomation:)) オプションで`pushAutomation` 。`nil` に設定すると、起動時にプッシュ認証を要求する以外は、すべてのプッシュオートメーション機能がイネーブルメントになる。
{% endalert %}

### ステップ 3:アプリデリゲートを更新する

{% alert important %}
以下は、すでにプロジェクトに`AppDelegate` （デフォルトでは生成されない）を追加していることを前提としている。使用する予定がない場合は、アプリの起動時など、できるだけ早い段階でBraze SDKを初期化しておくこと。
{% endalert %}

{% subtabs local %}
{% subtab swift %}
`AppDelegate.swift` ファイルに以下のコード行を追加して Braze Swift SDK に含まれる機能をインポートします。

```swift
import BrazeKit
```

次に、`AppDelegate` クラスに static プロパティを追加し、アプリケーションの有効期間を通して Braze インスタンスへの強い参照を保持します。

```swift
class AppDelegate: UIResponder, UIApplicationDelegate {
  static var braze: Braze? = nil
}
```

最後に、`AppDelegate.swift` で、`application:didFinishLaunchingWithOptions:` メソッドに次のスニペットを追加します。

```swift
let configuration = Braze.Configuration(
    apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
    endpoint: "YOUR-BRAZE-ENDPOINT"
)
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

**アプリの設定**ページから、`YOUR-APP-IDENTIFIER-API-KEY` と`YOUR-BRAZE-ENDPOINT` を正しい値に更新する。アプリ識別子のAPIキーがどこにあるかについては、[API識別子の種類を]({{site.baseurl}}/api/identifier_types/?tab=app%20ids)チェックしてほしい。

{% endsubtab %}
{% subtab OBJECTIVE-C %}

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

{% endsubtab %}
{% endsubtabs local %}

## オプション構成

### ロギング

#### ログレベル

Braze Swift SDKのデフォルトのログレベルは、`.error`。これは、ログがイネーブルメントである場合にサポートされる最小レベルでもある。以上がログレベルの全リストである：

| Swift       | Objective-C              | 説明                                                  |
| ----------- | ------------------------ | ------------------------------------------------------------ |
| `.debug`    | `BRZLoggerLevelDebug`    | デバッグ情報をログに残す +`.info` +`.error`.                      |
| `.info`     | `BRZLoggerLevelInfo`     | 一般的なSDK情報（ユーザーの変更など）を記録する +`.error` 。 |
| `.error`    | `BRZLoggerLevelError`    | エラーをロギングする。                                                  |
| `.disabled` | `BRZLoggerLevelDisabled` | ロギングは行われない。                                           |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### ログレベルの設定

`Braze.Configuration` 、実行時にログレベルを割り当てることができる。完全な使用法の詳細については、以下を参照のこと。 [`Braze.Configuration.Logger`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/logger-swift.class).

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
