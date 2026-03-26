## Swift SDKの統合

Braze Swift SDKは、Swift Package Manager（SPM）、CocoaPods、または手動での統合方法を使って統合しカスタマイズできる。各種SDKシンボルに関する詳細情報は、[Braze SWIFTリファレンスドキュメントを](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/)参照せよ。

### 前提条件

始める前に、[最新のBraze SWIFT SDKバージョン](https://github.com/braze-inc/braze-swift-sdk#version-information)が環境をサポートしていることを確認せよ。

### ステップ 1: Braze SWIFT SDKをインストールする

Braze Swift SDKのインストールには[、Swift Package Manager（SwiftPM）](https://swift.org/package-manager/)または[CocoaPods](http://cocoapods.org/)の使用を推奨する。あるいは、SDKを手動でインストールすることもできる。

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

#### ステップ1.2：パッケージを選択せよ

Braze Swift SDK は、開発者がどの機能をプロジェクトにインポートするかをより詳細に制御できるように、機能をスタンドアロンライブラリーに分離しています。

| パッケージ         | 詳細                                                                                                                                                         |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `BrazeKit`      | 分析とプッシュ通知をサポートする主な SDK ライブラリー                                                                                        |
| `BrazeLocation` | 位置情報ライブラリーは、位置情報分析とジオフェンス監視をサポートします。                                                                              |
| `BrazeUI`       | アプリ内メッセージ、コンテンツカード、バナー用のBraze提供ユーザーインターフェイスライブラリー。デフォルトのUIコンポーネントを使用する場合は、このライブラリーをインポートせよ。 |

{: .ws-td-nw-1}

##### 拡張ライブラリーについて

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

完全な手順については、CocoaPodsの入門[ガイドを](https://guides.cocoapods.org/using/getting-started.html)参照せよ。そうでなければ、以下のコマンドを実行すればすぐに始められる：

```bash
$ sudo gem install cocoapods
```

行き詰まったら、CocoaPodsの[トラブルシューティングガイド](http://guides.cocoapods.org/using/troubleshooting.html)を確認しろ。

#### ステップ1.2：ポッドファイルの構築

次に、Xcodeプロジェクトディレクトリ内に「`Podfile`.」という名前のファイルを作成する。

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
| `pod 'BrazeUI'`       | アプリ内メッセージ、コンテンツカード、バナー用のBraze提供ユーザーインターフェイスライブラリー。デフォルトのUIコンポーネントを使用する場合は、このライブラリーをインポートせよ。 |

{: .ws-td-nw-1}

###### 拡張ライブラリ

[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) と [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories) は、追加機能を提供するエクステンションモジュールであり、メインアプリケーションターゲットに直接追加すべきではありません。その代わりに、これらのモジュールごとに個別の拡張ターゲットを作成し、対応するターゲットにBrazeモジュールをインポートする必要がある。

| 図書館                          | 詳細                                                                               |
| -------------------------------- | ------------------------------------------------------------------------------------- |
| `pod 'BrazeNotificationService'` | リッチプッシュ通知をサポートする通知サービス拡張ライブラリー。 |
| `pod 'BrazePushStory'`           | プッシュストーリーをサポートする通知コンテンツ拡張ライブラリーを提供します。            |

{: .ws-td-nw-1}

#### ステップ1.3：SDK をインストール

Braze SDK CocoaPod をインストールするには、ターミナル内で Xcode アプリプロジェクトのディレクトリに移動し、次のコマンドを実行します。
```
pod install
```

この時点で、CocoaPods によって作成された新しい Xcode プロジェクトワークスペースを開くことができるはずです。Xcode プロジェクトの代わりに、必ずこの Xcode ワークスペースを使用してください。

![Brazeのサンプルフォルダが展開され、新しい「BrazeExample.workspace.」が表示された。]({% image_buster /assets/img/braze_example_workspace.png %})

#### CocoaPodsを使ってSDKを更新する

CocoaPod を更新するには、プロジェクトディレクトリ内で以下のコマンドを実行するだけです。

```
pod update
```
{% endtab %}

{% tab Manual %}
#### ステップ1.1：Braze SDKをダウンロード

[GitHubのBraze SDKリリースページ](https://github.com/braze-inc/braze-swift-sdk/releases)に移動し、`braze-swift-sdk-prebuilt.zip`をダウンロードします。

![GitHub上のBraze SDKリリースページ。]({% image_buster /assets/img/swift/sdk_integration/download-braze-swift-sdk-prebuilt.png %})

#### ステップ1.2：フレームワークを選択してください

Braze SWIFT SDK には、さまざまなスタンドアロンの XCFramework が含まれており、すべてを統合する必要はなく、必要な機能を自由に統合できます。次の表を参照して、XCFrameworksを選択してください:

| パッケージ                    | 必要か | 説明                                                                                                                                                                                                                                                                                                                          |
| -------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `BrazeKit`                 | はい       | メインSDKライブラリーは、分析とプッシュ通知をサポートします。                                                                                                                                                                                                                                                         |
| `BrazeLocation`            | いいえ        | 位置情報ライブラリーは、位置情報分析とジオフェンス監視をサポートします。                                                                                                                                                                                                                                               |
| `BrazeUI`                  | いいえ        | アプリ内メッセージ、コンテンツカード、バナー用のBraze提供ユーザーインターフェイスライブラリー。デフォルトのUIコンポーネントを使用する場合は、このライブラリーをインポートせよ。                                                                                                                                                                      |
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

![各Brazeライブラリーが「Embed&Sign」に設定されたXcodeプロジェクトの例。]({% image_buster /assets/img/swift/sdk_integration/embed-and-sign.png %})

{% alert note %}
Swift SDK 12.0.0 以降では、静的およびダイナミックな両方のバリアントにおいて、Braze XCFrameworks の署**名**方式として常に**「埋め込み&署名」**を選択すべきである。これにより、フレームワークのリソースがアプリバンドルに適切に組み込まれる。
{% endalert %}

{% alert tip %}
GIFのイネーブルメントを行うには、\`<HEAD>\` または \`<BODY`braze-swift-sdk-prebuilt/static``braze-swift-sdk-prebuilt/dynamic`>\` 内に \`<SCRIPT>\``SDWebImage.xcframework` を追加する。
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

### ステップ 2:遅延初期化を設定する（任意）

Braze SWIFT SDKの初期化を遅らせる選択ができる。これは、アプリが設定を読み込む必要がある場合や、SDKを開始する前にユーザーの同意を待つ必要がある場合に有用だ。遅延初期化により、SDK初期化前に受信したBrazeプッシュ通知とプッシュトークンは、SDKが初期化された時点でキューに入れられ処理される。

遅延初期化を使用するには、最低限のBraze SDKバージョンが必要だ。
{% sdk_min_versions swift:11.2.0 %}

#### ステップ 2.1: 初期化が遅れることに備えよ

アプリのライフサイクルにおいて、できるだけ早い`Braze.prepareForDelayedInitialization()`段階で呼び出すこと。理想的には、またはそれ以前に`application(_:didFinishLaunchingWithOptions:)`呼び出すこと。これにより、SDKが初期化される前に受信したプッシュ通知が確実に捕捉され、後で適切に処理される。

{% alert note %}
これはBrazeからのプッシュ通知にのみ適用される。その他のプッシュ通知は、システムデリゲートによって通常通り処理される。
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

遅延初期化を使用する場合、プッシュ通知のオートメーションは暗黙的にイネーブルメントされる。パラメータ`pushAutomation`を渡すことで、[プッシュオートメーション](#swift_step-23-customize-push-automation-optional)の設定[をカスタマイズ](#swift_step-23-customize-push-automation-optional)できる。

#### ステップ 2.2:プッシュ分析の動作を設定する（任意）

遅延初期化のイネーブルメントが有効な場合、プッシュ分析はデフォルトでキューに格納される。ただし、代わりにプッシュ分析を明示的にキューに入れるか破棄するかを選択できる。

##### 明示的にキューに入れる

明示的にキューにプッシュ分析を送信するには（デフォルト動作）、`analyticsBehavior`パラメータに  `.queue`を渡す。初期化前にキューに追加されたプッシュ分析イベントは、初期化時に処理されサーバーに送信される。

{% tabs local %}
{% tab Swift %}
```swift
Braze.prepareForDelayedInitialization(analyticsBehavior: .queue)
```
{% endtab %}
{% tab Objective-C %}
```objc
[Braze prepareForDelayedInitializationWithAnalyticsBehavior:BRZPushEnqueueBehaviorQueue];
```
{% endtab %}
{% endtabs %}

##### 落とす

SDK初期化前に受信したプッシュ分析を破棄するには、`analyticsBehavior`パラメータに`.drop` を渡す。このオプションでは、SDKが初期化されていない間に発生したプッシュ分析イベントはすべて無視される。

{% tabs local %}
{% tab Swift %}
```swift
Braze.prepareForDelayedInitialization(analyticsBehavior: .drop)
```
{% endtab %}
{% tab Objective-C %}
```objc
[Braze prepareForDelayedInitializationWithAnalyticsBehavior:BRZPushEnqueueBehaviorDrop];
```
{% endtab %}
{% endtabs %}

#### ステップ 2.3:プッシュ通知のオートメーションをカスタマイズする（任意）

パラメータ`pushAutomation`を渡すことで、プッシュオートメーションの設定をカスタマイズできる。デフォルトでは、すべてのオートメーション機能がイネーブルされている。`requestAuthorizationAtLaunch`ただし、以下を除く。

{% tabs local %}
{% tab SWIFT %}
```swift
// Enable all push automation
featuresBraze.prepareForDelayedInitialization(pushAutomation: true)

// Or customize specific automation options
let automation = Braze.Configuration.Push.Automation()
automation.automaticSetup = true
automation.requestAuthorizationAtLaunch = false
Braze.prepareForDelayedInitialization(pushAutomation: automation)
```
{% endtab %}

{% tab OBJECTIVE-C %}
```objc
// Enable all push automation features
[Braze prepareForDelayedInitializationWithPushAutomation:[[BRZConfigurationPushAutomation alloc] initWithAutomationEnabled:YES]];

// Or customize specific automation options
BRZConfigurationPushAutomation *automation = [[BRZConfigurationPushAutomation alloc] init];
automation.automaticSetup = YES;
automation.requestAuthorizationAtLaunch = NO;
[Braze prepareForDelayedInitializationWithPushAutomation:automation analyticsBehavior:BRZPushEnqueueBehaviorQueue];
```
{% endtab %}
{% endtabs %}

#### ステップ 2.4:SDK の初期化

選択した遅延期間の後（例えば、サーバーから設定を取得した後やユーザーの同意を得た後）、通常通りSDKを初期化する：

{% tabs local %}
{% tab SWIFT %}
```swift
func initializeBraze() {  
  let configuration = Braze.Configuration(apiKey: "YOUR-API-KEY", endpoint: "YOUR-ENDPOINT")    
  
  // Enable push automation to match the delayed initialization configuration  
  configuration.push.automation = true    
  let braze = Braze(configuration: configuration)    
  
  // Store the Braze instance for later use 
  AppDelegate.braze = braze
}
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
- (void)initializeBraze {
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"YOUR-API-KEY" endpoint:@"YOUR-ENDPOINT"];
  
  // Enable push automation to match the delayed initialization configuration
  configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initWithAutomationEnabled:YES];
  Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
  
  // Store the Braze instance for later use
  AppDelegate.braze = braze;
}
```
{% endtab %}
{% endtabs %}

{% alert note %}
SDKが初期化されると、キューに蓄積されたプッシュ通知、プッシュトークン、ディープリンクは自動的に処理される。
{% endalert %}

### ステップ 3:アプリデリゲートを更新する

{% alert important %}
以下は、プロジェクトに既に  `AppDelegate`を追加済み（デフォルトでは生成されない）であり、遅延初期化機能を使用していないことを前提とする。アプリ起動時など、できるだけ早い段階でBraze SDKを初期化するようにするんだ`AppDelegate`。遅延初期化機能を使用している場合は、SDKの初期化については[ステップ2.4](#swift_step-24-initialize-the-sdk)を参照し、このステップは無視する。
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

## オプション設定

### ロギング

すべてのプラットフォームにわたる一元的な概要については、[詳細ログを]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)参照せよ。ログ出力の解釈方法の学習については、[「詳細ログの読み方」]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs)を参照せよ。

#### ログレベル

Braze SWIFT SDKのデフォルトのログレベルは`.error`—である。ログのイネーブルメントが有効化されている場合、これがサポートされる最低レベルでもある。これがログレベルの一覧だ：

| Swift       | Objective-C              | 説明                                                  |
| ----------- | ------------------------ | ------------------------------------------------------------ |
| `.debug`    | `BRZLoggerLevelDebug`    | ログにデバッグ情報を記録`.info`する`.error`。              |
| `.info`     | `BRZLoggerLevelInfo`     | 一般的なSDK情報（ユーザーの変更など）を記録する +`.error` 。 |
| `.error`    | `BRZLoggerLevelError`    | エラーをロギングする。                                                  |
| `.disabled` | `BRZLoggerLevelDisabled` | ロギングは行われない。                                           |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### ログレベルの設定

実行時にオブジェクト`Braze.Configuration`内でログレベルを割り当てることができる。完全な使用方法の詳細については、を参照せよ[`Braze.Configuration.Logger`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/logger-swift.class)。

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
