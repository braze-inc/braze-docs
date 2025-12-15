---
nav_title: 統合の完了
article_title: iOS SDK の統合を完了する
platform: iOS
description: "この参考記事では、統合オプションの1つを使用して Braze SDK をインストールした後に統合を完了する方法を示します。"
page_order: 2

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 統合の完了

これらの手順に従う前に、[Carthage]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/carthage_integration/)、[CocoaPods]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/cocoapods/)、[Swift Package Manager]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/swift_package_manager/)、または[手動]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options/)統合のいずれかを使用して SDK を統合していることを確認してください。

## ステップ1:アプリデリゲートを更新する

{% tabs %}
{% tab OBJECTIVE-C %}

Braze SDK を CocoaPods、Carthage、または[ダイナミックな手動統合]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options/)と統合している場合は、次のコード行を `AppDelegate.m` ファイルに追加します。

```objc
#import "Appboy-iOS-SDK/AppboyKit.h"
```

Swift Package Manager または[静的な手動統合]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options/)を使用して統合している場合は、代わりに次の行を使用します。

```objc
#import "AppboyKit.h"
```

次に、`AppDelegate.m` ファイル内の `application:didFinishLaunchingWithOptions:` メソッド内に以下のスニペットを追加します。

```objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFIER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions];
```

**設定の管理**ページの正しい値で `YOUR-APP-IDENTIFIER-API-KEY` を更新してください。アプリ識別子の API キーの場所について詳しくは、[API ドキュメント]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key)をご覧ください。

{% endtab %}
{% tab swift %}

Braze SDK を CocoaPods、Carthage、または[ダイナミックな手動統合]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options/)と統合している場合は、次のコード行を `AppDelegate.swift` ファイルに追加します。

```swift
import Appboy_iOS_SDK
```

Swift Package Manager または[静的な手動統合]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options/)を使用して統合している場合は、代わりに次の行を使用します。

```swift
import AppboyKit
```
Swift プロジェクトでの Objective-C コードの使用の詳細については、[Apple 開発者ドキュメント](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html)を参照してください。

次に、`AppDelegate.swift` で、次のスニペットを `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` に追加します。

```swift
Appboy.start(withApiKey: "YOUR-APP-IDENTIFIER-API-KEY", in:application, withLaunchOptions:launchOptions)
```

**設定の管理**ページの正しい値で `YOUR-APP-IDENTIFIER-API-KEY` を更新してください。アプリ識別子の API キーの場所について詳しくは、[API ドキュメント]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key)をご覧ください。

{% endtab %}
{% endtabs %}

{% alert note %}
Braze 機能を使用するための前提条件であるため、`sharedInstance`シングルトンは`startWithApiKey:`が呼び出される前に nil になります。
{% endalert %}

{% alert warning %}
必ずアプリケーションのメインスレッドで Braze を初期化してください。非同期で初期化すると、機能が破損する可能性があります。
{% endalert %}


## ステップ2:データクラスターを指定する

{% alert note %}
2019年12月の時点で、カスタムエンドポイントは提供されなくなっていることに注意してください。既存のカスタムエンドポイントがある場合は、それを引き続き使用できます。詳細については、<a href="{{site.baseurl}}/api/basics/#endpoints">利用可能なエンドポイントのリスト</a>を参照してください。
{% endalert %}

### コンパイル時のエンドポイント構成 (推奨)

既存のカスタムエンドポイントが指定されている場合:
- Braze iOS SDK v 3.0.2以降では、`Info.plist` ファイルを使用してカスタムエンドポイントを設定できます。`Braze` ディクショナリを `Info.plist` ファイルに追加します。`Braze` 辞書内で、`Endpoint` 文字列サブエントリを追加し、値をカスタムエンドポイント URL の権限 (たとえば、`https://sdk.iad-01.braze.com` ではなく `sdk.iad-01.braze.com`) に設定します。Braze iOS SDK v4.0.2 より前では、辞書キー `Appboy` を `Braze` の代わりに使用する必要があります。

Braze 担当者は、[正しいエンドポイント]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/)についてすでに通知しているはずです。

### ランタイムエンドポイント構成

既存のカスタムエンドポイントが指定されている場合:
- Braze iOS SDK v 3.17.0以降では、`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` に渡される `appboyOptions` パラメーター内の `ABKEndpointKey` を使用してエンドポイントの設定をオーバーライドできます。値をカスタムエンドポイント URL 権限 (たとえば、`https://sdk.iad-01.braze.com`ではなく`sdk.iad-01.braze.com`) に設定します。

## SDK の統合が完了

Braze はアプリケーションからデータを収集しており、基本的な統合は完了しているはずです。[カスタムイベントトラッキング]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift)、[プッシュ メッセージング]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration/)、および Braze 機能の完全なスイートを有効にするには、次の記事を参照してください。

## 起動時の Braze のカスタマイズ

起動時に Braze をカスタマイズする場合は、代わりに Braze 初期化メソッド `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` を使用し、オプションの Braze 起動キーの `NSDictionary` を渡すことができます。
{% tabs %}
{% tab OBJECTIVE-C %}

`AppDelegate.m` ファイルの `application:didFinishLaunchingWithOptions:` メソッド内に、次の Braze メソッドを追加します。

```objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFIER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

このメソッドは `startWithApiKey:inApplication:withLaunchOptions:` 初期化メソッドを置き換えることに注意してください。

{% endtab %}
{% tab swift %}

`AppDelegate.swift` の `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` メソッド内に、次の Braze メソッドを追加します。`appboyOptions` はスタートアップ構成値の `Dictionary` です。

```swift
Appboy.start(withApiKey: "YOUR-APP-IDENTIFIER-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:appboyOptions)
```

このメソッドは `startWithApiKey:inApplication:withLaunchOptions:` 初期化メソッドを置き換えることに注意してください。

{% endtab %}
{% endtabs %}

このメソッドは、次のパラメータを使用して呼び出されます。

- `YOUR-APP-IDENTIFIER-API-KEY` – Braze ダッシュボードの[アプリ識別子]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) API キー。
- `application` – 現在のアプリ。
- `launchOptions` – `application:didFinishLaunchingWithOptions:` から取得するオプション `NSDictionary`。
- `appboyOptions` – Braze のスタートアップ構成値を持つオプションの `NSDictionary`。

Braze のスタートアップキーのリストについては、[Appboy.h](https://github.com/braze-inc/braze-ios-sdk/blob/master/AppboyKit/include/Appboy.h) を参照してください。

## Appboy.sharedInstance() および Swift の nullability
一般的な慣例とは多少異なりますが、`Appboy.sharedInstance()` シングルトンはオプションです。これは、`startWithApiKey:` が呼び出さられる前は `sharedInstance` が `nil` であり、遅延初期化を使用できる非標準で無効ではない実装がいくつかあるためです。

Appboy の `sharedInstance` (標準実装) にアクセスする前に `didFinishLaunchingWithOptions:` デリゲートで `startWithApiKey:` を呼び出すと、`Appboy.sharedInstance()?.changeUser("testUser")` のようなオプションのチェーンを使用して、煩雑なチェックを回避できます。これは、非 null `sharedInstance` を想定した Objective-C 実装と同等になります。

## その他のリソース

[iOS クラスの完全なドキュメント](http://appboy.github.io/appboy-ios-sdk/docs/annotated.html) を使用して SDK メソッドに関する追加のガイダンスを提供できます。

