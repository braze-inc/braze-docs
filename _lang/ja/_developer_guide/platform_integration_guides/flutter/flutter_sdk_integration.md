---
nav_title: SDK の初期セットアップ
article_title: Flutter の初期 SDK セットアップ
platform: Flutter
page_order: 1
description: "このリファレンスでは、Flutter SDK を紹介し、Android と iOS でのネイティブ統合の方法について説明します。"
search_rank: 1
---

# SDK の初期セットアップ

> このリファレンス記事では、Flutter 向け Braze SDK のインストール方法について説明します。以下の手順に従って、[Braze Flutter SDK](https://pub.dev/packages/braze_plugin) をインストールします。これには、Dart で記述された [Flutter アプリ](https://flutter.dev/)でインテグレーターが Braze API を使用できるようにするパッケージが含まれています。

このプラグインには、基本的な分析機能が用意されており、iOS と Android 両方のアプリ内メッセージとコンテンツカードを1つのコードベースで統合できます。

{% alert note %}
両方のプラットフォームで個別にインストール手順を実行する必要があります。
{% endalert %}

## 前提条件

インストールを完了するには、[アプリ識別子 API キー]({{site.baseurl}}/api/identifier_types/)と [SDK エンドポイント]({{site.baseurl}}/api/basics/#endpoints)が必要です。どちらもダッシュボードの [**設定の管理**] の下にあります。

これらの手順を実行する前に、[Flutter SDK](https://docs.flutter.dev/get-started/install) をインストールしてセットアップします。マシンとプロジェクトで、必要な最小限の Flutter バージョンと Dart バージョン ([こちらに記載](https://github.com/braze-inc/braze-flutter-sdk#readme)) が実行されていることを確認します。

## ステップ 1:Braze ライブラリーを統合する

コマンドラインから Braze Flutter SDK パッケージを追加します。

```bash
flutter pub add braze_plugin
```

これにより、適切な行が`pubspec.yaml` に追加されます。

## ステップ 2:ネイティブセットアップを完了する

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

## ステップ 3: 使用

Dart コードにプラグインをインポートするには、以下を使用します。

```dart
import 'package:braze_plugin/braze_plugin.dart';
```

次に、[サンプルアプリ](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart)のように `new BrazePlugin()` を呼び出して、Braze プラグインのインスタンスを初期化します。

## 基本的な統合のテスト

この時点で、ダッシュボードでセッション統計を確認することで、SDK が統合されていることを確認できます。いずれかのプラットフォームでアプリケーションを実行すると、ダッシュボード ([**概要**] セクション) に新しいセッションが表示されます。

アプリで次のコードを呼び出すことで、特定のユーザーのセッションを開くことができます。

```dart
BrazePlugin braze = BrazePlugin();
braze.changeUser("{some-user-id}");
```

その後、ダッシュボードの [**オーディエンス**] > [**ユーザー検索**] で `{some-user-id}` を使用してユーザーを検索します。そこで、セッションとデバイスデータがロギングされていることを確認できます。

{% alert note %}
[以前のナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、[**ユーザー**] > [**ユーザー検索**] からユーザーを検索できます。
{% endalert %}

