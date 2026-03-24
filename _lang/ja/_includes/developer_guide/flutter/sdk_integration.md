## Flutter Braze SDKについて

AndroidとiOSでBraze Flutter SDKを統合した後、Dartで書かれた[Flutterアプリ](https://flutter.dev/)内でBraze APIを利用できるようになります。このプラグインには、基本的な分析機能が用意されており、iOS と Android 両方のアプリ内メッセージとコンテンツカードを1つのコードベースで統合できます。

## Flutter SDKの統合

### 前提条件

Braze Flutter SDKを統合する前に、以下を完了する必要があります。

| 前提条件 | 説明 |
| --- | --- |
| Braze API アプリ識別子 | アプリの識別子を確認するには、**設定** > **APIと識別子** > **アプリ識別子**に移動します。詳細については、[API識別子の種類]({{site.baseurl}}/api/identifier_types/#app-identifier)を参照してください。|
| Braze SDK エンドポイント | SDK エンドポイントのURL（例：`sdk.<cluster>.braze.com`）。エンドポイントはインスタンスの [Braze URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) に応じて異なります。|
| Flutter SDK | 公式の[Flutter SDK](https://docs.flutter.dev/get-started/install)をインストールし、Braze Flutter SDKの[最低サポートバージョン](https://github.com/braze-inc/braze-flutter-sdk#requirements)を満たしていることを確認してください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### ステップ 1: Braze ライブラリーを統合する

コマンドラインから Braze Flutter SDK パッケージを追加します。これにより、適切な行が`pubspec.yaml` に追加されます。

```bash
flutter pub add braze_plugin
```

### ステップ 2: ネイティブSDKの設定を完了する

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

#### 2.1 Androidの設定

##### コンパイル時に認証情報を提供する

プロジェクトの `android/res/values` フォルダに `braze.xml` ファイルを作成します。API キーとエンドポイントは Dart から実行時に提供されるため、このファイルでは不要です。遅延初期化を有効にするには、`com_braze_enable_delayed_initialization` をファイルに追加します。

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <bool name="com_braze_enable_delayed_initialization">true</bool>
  <!-- API key and endpoint are not required here. They are set at runtime via Dart. -->
</resources>
```

##### 実行時に認証情報を提供する

または、`MainActivity.kt` でプログラム的に遅延初期化を有効にすることもできます。

```kotlin
import com.braze.Braze

class MainActivity : FlutterActivity() {
  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    Braze.enableDelayedInitialization(context = this)
  }
}
```

必要な権限を `AndroidManifest.xml` ファイルに追加します。

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

#### 2.2 iOSの設定

既存の `application(_:didFinishLaunchingWithOptions:)` メソッド内で、`BrazePlugin.configure(_:postInitialization:)` を呼び出して設定を保存します。Braze インスタンスは、後で Dart から `initialize()` が呼び出されたときに作成されます。ここでは API キーとエンドポイントは設定しません。

{% subtabs %}
{% subtab SWIFT %}

以下のコードを `AppDelegate.swift` に追加します。

```swift
import BrazeKit
import braze_plugin

// ...

override func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
  // ... your existing didFinishLaunchingWithOptions setup ...

  BrazePlugin.configure(
    { configuration in
      configuration.logger.level = .info
      // Set other non-API-key configurations here, such as:
      // configuration.push.automation = true
      // configuration.sessionTimeout = 60
    },
    postInitialization: { braze in
      // Optional: Customize the Braze instance after creation.
      // For example, set a custom in-app message presenter:
      // let customPresenter = CustomInAppMessagePresenter()
      // braze.inAppMessagePresenter = customPresenter
    }
  )

  return true
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

以下のコードを `AppDelegate.m` に追加します。

```objc
@import BrazeKit;
@import braze_plugin;

// ...

- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [BrazePlugin configure:^(BRZConfiguration *configuration) {
    configuration.logger.level = BRZLoggerLevelInfo;
    // Set other non-API-key configurations here, such as:
    // configuration.push.automation = ...
    // configuration.sessionTimeout = 60;
  } postInitialization:^(Braze *braze) {
    // Optional: customize the Braze instance after creation.
  }];

  return YES;
}
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
`BrazePlugin.configure()` は設定を保存するだけです。Dart から `initialize()` が呼び出されるまで Braze インスタンスは存在しないため、`configure()` の後に AppDelegate で Braze SDK メソッドを呼び出さないでください。
{% endalert %}

{% endtab %}
{% tab Flutter SDK 17.1.0 and earlier %}

#### 2.1 Androidの設定

Braze サーバーに接続するには、プロジェクトの `android/res/values` フォルダに `braze.xml` ファイルを作成します。以下のコードを貼り付けて、API 識別子キーとエンドポイントをご自身の値に置き換えます。

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

必要な権限を `AndroidManifest.xml` ファイルに追加します。

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

#### 2.2 iOSの設定

{% subtabs %}
{% subtab SWIFT %}
`AppDelegate.swift` ファイルの先頭に Braze SDK のインポートを追加します。
```swift
import BrazeKit
import braze_plugin
```

同じファイルの `application(_:didFinishLaunchingWithOptions:)` メソッドで Braze 設定オブジェクトを作成し、API キーとエンドポイントをアプリの値に置き換えます。次に、設定を使用して Braze インスタンスを作成し、簡単にアクセスできるよう `AppDelegate` に静的プロパティを作成します。

```swift
static var braze: Braze? = nil

override func application(
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
`AppDelegate.m` ファイルの先頭に Braze SDK をインポートします。
```objc
@import BrazeKit;
@import braze_plugin;
```

同じファイルの `application:didFinishLaunchingWithOptions:` メソッドで Braze 設定オブジェクトを作成し、API キーとエンドポイントをアプリの値に置き換えます。次に、設定を使用して Braze インスタンスを作成し、簡単にアクセスできるよう `AppDelegate` に静的プロパティを作成します。

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

### ステップ 3: プラグインを設定する

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

プラグインをインポートし、`BrazePlugin` の単一インスタンスを作成します。

```dart
import 'package:braze_plugin/braze_plugin.dart';

final BrazePlugin braze = BrazePlugin();
```

次に、アプリ識別子 API キーと SDK エンドポイントを指定して `initialize()` を呼び出し、Braze インスタンスを作成します。アプリ内でこのメソッドを呼び出す場所については、以下のオプションを参照してください。

#### 標準初期化

アプリの起動時に SDK を初期化するには、`initState()` 内で `initialize()` を呼び出します。

```dart
@override
void initState() {
  super.initState();
  braze.initialize("<BRAZE_API_KEY>", "<BRAZE_ENDPOINT>");
}
```

#### 遅延初期化

SDK の初期化をセッション内の後のタイミングまで延期するには（例：ユーザーが同意を付与した後やログインを完了した後）、準備ができた時点で `initialize()` を呼び出します。

```dart
// ...
void onUserConsent() {
  braze.initialize("<BRAZE_API_KEY>", "<BRAZE_ENDPOINT>");
}
```

{% alert warning %}
`initialize()` が呼び出される前に受信したプッシュ通知とディープリンクは、iOSでは処理されません。Androidでは、SDK が初期化を待っている間、プッシュ通知からのディープリンクは解決されません。アプリが起動時にプッシュ通知やディープリンクに依存している場合は、代わりに[標準初期化](#standard-initialization)を使用してください。
{% endalert %}

#### プラットフォーム固有の API キー

Android と iOS のアプリは異なる API キーを使用するため、プラットフォーム検出を使用します。

```dart
import 'dart:io' show Platform;

if (Platform.isAndroid) {
  braze.initialize("<ANDROID_API_KEY>", "<BRAZE_ENDPOINT>");
} else if (Platform.isIOS) {
  braze.initialize("<IOS_API_KEY>", "<BRAZE_ENDPOINT>");
}
```

#### 再初期化

セッション中に異なる API キーとエンドポイントで SDK を再初期化するために、`initialize()` を複数回呼び出すことができます。呼び出すたびに、以前の Braze インスタンスが破棄され、新しいインスタンスが作成されます。

{% alert important %}
未定義の動作を避けるため、Dart コード内では単一の `BrazePlugin` インスタンスのみを割り当てて使用してください。`initialize()` の前に行われたすべての SDK メソッド呼び出しは iOS では無視されるため、他の Braze メソッドを使用する前に `initialize()` を呼び出してください。
{% endalert %}

{% endtab %}
{% tab Flutter SDK 17.1.0 and earlier %}

Dart コードにプラグインをインポートするには、以下を使用します。

```dart
import 'package:braze_plugin/braze_plugin.dart';
```

次に、[サンプルアプリ](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart)のように `new BrazePlugin()` を呼び出して、Braze プラグインのインスタンスを初期化します。

{% alert important %}
未定義の動作を避けるため、Dart コード内では単一の `BrazePlugin` インスタンスのみを割り当てて使用してください。
{% endalert %}

{% endtab %}
{% endtabs %}

## 統合のテスト
ダッシュボードでセッション統計を確認することで、SDK が統合されていることを検証できます。いずれかのプラットフォームでアプリケーションを実行すると、ダッシュボード（**概要**セクション）に新しいセッションが表示されます。

アプリ内で以下のコードを呼び出すことで、特定のユーザーのセッションを開始できます。

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

```dart
BrazePlugin braze = BrazePlugin();
braze.initialize("<BRAZE_API_KEY>", "<BRAZE_ENDPOINT>");
braze.changeUser("{some-user-id}");
```

{% endtab %}
{% tab Flutter SDK 17.1.0 and earlier %}

```dart
BrazePlugin braze = BrazePlugin();
braze.changeUser("{some-user-id}");
```

{% endtab %}
{% endtabs %}

ダッシュボードの**オーディエンス** > **ユーザーの検索**で `{some-user-id}` のユーザーを検索します。そこで、セッションとデバイスデータが記録されていることを確認できます。