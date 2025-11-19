## Braze SDKについて

AndroidとiOSでBraze Flutter SDKを統合すると、Dartで書かれた[Flutterアプリ](https://flutter.dev/)内でBraze APIを使えるようになる。このプラグインには、基本的な分析機能が用意されており、iOS と Android 両方のアプリ内メッセージとコンテンツカードを1つのコードベースで統合できます。

## Flutter SDKを統合する

### 前提条件

Braze Flutter SDKを統合する前に、以下を完了する必要がある：

| 前提条件 | 説明 |
| --- | --- |
| Braze APIアプリ識別子 | アプリの識別子を見つけるには、**設定**＞**APIと識別子**＞アプリ識別子と進む。詳細は[API識別子タイプを]({{site.baseurl}}/api/identifier_types/#app-identifier)参照のこと。|
| Braze RESTエンドポイント | REST エンドポイントのURL。エンドポイントはインスタンスの [Braze URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) に応じて異なります。|
| Flutter SDK | 公式[Flutter SDKを](https://docs.flutter.dev/get-started/install)インストールし、Braze Flutter SDKの[最小サポートバージョンを満たして](https://github.com/braze-inc/braze-flutter-sdk#requirements)いることを確認する。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### ステップ1:Braze ライブラリーを統合する

コマンドラインから Braze Flutter SDK パッケージを追加します。これにより、適切な行が`pubspec.yaml` に追加されます。

```bash
flutter pub add braze_plugin
```

### ステップ 2:完全なネイティブSDKのセットアップ

{% tabs %}
{% tab Android %}

Braze サーバーに接続するには、プロジェクトの `android/res/values` フォルダで `braze.xml` ファイルを作成します。以下のコードを貼り付けて、API 識別子キーとエンドポイントを値で置き換えます。

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
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

### ステップ 3:プラグインを設定する

Dart コードにプラグインをインポートするには、以下を使用します。

```dart
import 'package:braze_plugin/braze_plugin.dart';
```

次に、[サンプルアプリ](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart)のように `new BrazePlugin()` を呼び出して、Braze プラグインのインスタンスを初期化します。

{% alert important %}
未定義の動作を避けるため、Dartコード内で`BrazePlugin` のインスタンスを1つだけ割り当てて使用する。
{% endalert %}

## 統合をテストする

SDKが統合されているかどうかは、ダッシュボードのセッション統計をチェックすることで確認できる。いずれかのプラットフォームでアプリケーションを実行すると、ダッシュボード ([**概要**] セクション) に新しいセッションが表示されます。

アプリ内で以下のコードを呼び出して、特定のユーザーのセッションを開封する。

```dart
BrazePlugin braze = BrazePlugin();
braze.changeUser("{some-user-id}");
```

ダッシュボードの**Audience**>**Search Usersで** `{some-user-id}` 、ユーザーを検索する。そこで、セッションとデバイスデータがロギングされていることを確認できます。

