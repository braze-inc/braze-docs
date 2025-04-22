## Flutter Braze SDKについて

Android およびiOS でBraze Flutter SDK を統合すると、Dart で書かれた[Flutter アプリ](https://flutter.dev/) 内でBraze API を使用できるようになります。このプラグインには、基本的な分析機能が用意されており、iOS と Android 両方のアプリ内メッセージとコンテンツカードを1つのコードベースで統合できます。

## Flutter SDK の統合

### 前提条件

Braze Flutter SDK を統合する前に、以下の作業を完了する必要があります。

| 前提条件 | 説明 |
| --- | --- |
| ブレーズAPI アプリの識別子 | アプリの識別子を見つけるには、**Settings** > **APIs and Identifiers** > **App Identifiers**に移動します。詳細については、[API Identifier Types]({{site.baseurl}}/api/identifier_types/#app-identifier)を参照してください。|
| Braze RESTエンドポイント | REST エンドポイントのURL。エンドポイントはインスタンスの [Braze URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) に応じて異なります。|
| Flutter SDK | 公式の[Flutter SDK](https://docs.flutter.dev/get-started/install)をインストールし、それがBraze Flutter SDKの[サポートされている最小バージョン](https://github.com/braze-inc/braze-flutter-sdk#requirements)を満たしていることを確認します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### ステップ1:Braze ライブラリーを統合する

コマンドラインから Braze Flutter SDK パッケージを追加します。これにより、適切な行が`pubspec.yaml` に追加されます。

```bash
flutter pub add braze_plugin
```

### ステップ2: 完全なネイティブSDKセットアップ

{% tabs %}
{% tab Android %}

Braze サーバーに接続するには、プロジェクトの `android/res/values` フォルダで `braze.xml` ファイルを作成します。以下のコードを貼り付けて、API 識別子キーとエンドポイントを値で置き換えます。

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
<string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

必要な権限をファイル `AndroidManifest.xml` に追加します。

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% endtab %}
{% tab iOS %}
{% subtabs global %}
{% subtab SWIFT %}
`AppDelegate.swift` ファイルの先頭にBraze SDK インポートを追加します。
```swift
import BrazeKit
import braze_plugin
```

同じファイルで、`application(_:didFinishLaunchingWithOptions:)` メソッドで Braze 構成オブジェクトを作成し、API キーとエンドポイントをアプリの値に置き換えます。次に、構成を使用して Braze インスタンスを作成し、簡単にアクセスできるよう `AppDelegate` で静的プロパティを作成します。

```swift
static var braze: Braze? = nil

func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
  // Setup Braze
  let configuration = Braze.Configuration(
    apiKey: "<BRAZE_API_KEY>",
    endpoint: "<BRAZE_ENDPOINT>"
  )
  // - Enable logging or customize configuration here
  configuration.logger.level = .info
  let braze = BrazePlugin.initBraze(configuration)
  AppDelegate.braze = braze

  return true
}
```
{% endsubtab %}
{% subtab OBJECTIVE-C %}
`AppDelegate.m` ファイルの先頭に `BrazeKit` をインポートします。
```objc
@import BrazeKit;
```

同じファイルで、`application:didFinishLaunchingWithOptions:` メソッドで Braze 構成オブジェクトを作成し、API キーとエンドポイントをアプリの値に置き換えます。次に、構成を使用して Braze インスタンスを作成し、簡単にアクセスできるよう `AppDelegate` で静的プロパティを作成します。

```objc
- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Setup Braze
  BRZConfiguration *configuration =
      [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                      endpoint:@"<BRAZE_ENDPOINT>"];
  // - Enable logging or customize configuration here
  configuration.logger.level = BRZLoggerLevelInfo;
  Braze *braze = [BrazePlugin initBraze:configuration];
  AppDelegate.braze = braze;

  [self.window makeKeyAndVisible];
  return YES;
}

#pragma mark - AppDelegate.braze

static Braze *_braze = nil;

+ (Braze *)braze {
  return _braze;
}

+ (void)setBraze:(Braze *)braze {
  _braze = braze;
}
```
{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% endtabs %}

### ステップ 3:プラグインのセットアップ

Dart コードにプラグインをインポートするには、以下を使用します。

```dart
import 'package:braze_plugin/braze_plugin.dart';
```

次に、[サンプルアプリ](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart)のように `new BrazePlugin()` を呼び出して、Braze プラグインのインスタンスを初期化します。

{% alert important %}
未定義の動作を回避するには、Dart コードで`BrazePlugin` の単一インスタンスのみを割り当てて使用します。
{% endalert %}

## 統合のテスト

SDK が統合されていることを確認するには、ダッシュボードでセッション統計を確認します。いずれかのプラットフォームでアプリケーションを実行すると、ダッシュボード ([**概要**] セクション) に新しいセッションが表示されます。

アプリで次のコードを呼び出して、特定のユーザーのセッションを開きます。

```dart
BrazePlugin braze = BrazePlugin();
braze.changeUser("{some-user-id}");
```

**Audience**> **Search Users**のダッシュボードで`{some-user-id}`のユーザーを検索します。そこで、セッションとデバイスデータがロギングされていることを確認できます。

