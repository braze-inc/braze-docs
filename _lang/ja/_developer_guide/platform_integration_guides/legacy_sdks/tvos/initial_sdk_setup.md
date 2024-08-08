---
nav_title: SDK の初期セットアップ
article_title: tvOS の初期 SDK セットアップ
platform: tvOS
page_order: 0
page_type: reference
description: "このページでは、tvOS Braze SDK の初期セットアップ手順について説明します。"
search_rank: 1
noindex: true
---

{% multi_lang_include archive/objective-c-deprecation-notice.md %}

# SDK の初期セットアップ

> この参考記事では、tvOS 用 Braze SDK をインストールする方法について説明します。Braze SDK をインストールすると、基本的な分析機能が提供されます。

{% alert note %}
当社の tvOS SDK は現在、分析機能をサポートしています。ダッシュボードに tvOS アプリを追加するには、[サポートチケット]({{site.baseurl}}/braze_support/)を開きます。
{% endalert %}

tvOS Braze SDK は、Objective-C および Swift プロジェクトの依存関係マネージャーである [CocoaPods][apple_initial_setup_1]を使用してインストールまたは更新する必要があります。CocoaPods を使用すると、統合と更新がさらに簡単になります。

## tvOS SDK CocoaPods の統合

### ステップ1: CocoaPods をインストールする

tvOS [CocoaPods][apple_initial_setup_1] を介して SDK をインストールすると、インストール プロセスの大部分が自動化されます。このプロセスを開始する前に、[Ruby バージョン 2.0.0][apple_initial_setup_2] 以降を使用していることを確認してください。

開始するには、次のコマンドを実行します。

```bash
$ sudo gem install cocoapods
```

- `rake` 実行可能ファイルを上書きするように求められた場合は、CocoaPods.org の[はじめに][apple_initial_setup_3] で詳細を確認してください。
- CocoaPods に関する問題がある場合は、[CocoaPods トラブルシューティングガイド][apple\_initial\_setup\_25] を参照してください。

### ステップ2:ポッドファイルの構築

CocoaPods Ruby Gem をインストールしたら、Xcode プロジェクト ディレクトリに `Podfile` という名前のファイルを作成する必要があります。

次の行を Podfile に追加します。

```
target 'YourAppTarget' do
  pod 'Appboy-tvOS-SDK'
end
```

ポッドの更新がマイナー バージョンの更新よりも小さいものを自動的に取得するように、Braze をバージョン管理することをお勧めします。これは次のようになります。`pod 'Appboy-tvOS-SDK' ~> Major.Minor.Build`最新の Braze SDK バージョンを自動的に統合する場合は、大きな変更があっても、Podfileで `pod 'Appboy-tvOS-SDK'` を使用できます。

### ステップ3: Braze SDK のインストール

Braze SDK CocoaPods をインストールするには、ターミナル内で Xcode アプリプロジェクトのディレクトリに移動し、次のコマンドを実行します。
```
pod install
```

この時点で、CocoaPods によって作成された新しい Xcode プロジェクトワークスペースを開くことができるはずです。Xcode プロジェクトの代わりに、必ずこの Xcode ワークスペースを使用してください。 

![][apple\_initial\_setup\_15]

### ステップ 4アプリデリゲートの更新

{% tabs %}
{% tab OBJECTIVE-C %}

次のコード行を `AppDelegate.m` ファイルに追加します。

```objc
#import <AppboyTVOSKit/AppboyKit.h>
```

`AppDelegate.m` ファイル内で、`application:didFinishLaunchingWithOptions` メソッド内に次のスニペットを追加します。

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
         inApplication:application
     withLaunchOptions:launchOptions];
```

最後に、[**設定の管理**] ページの正しい値で `YOUR-API-KEY` を更新します。

{% endtab %}
{% tab swift %}

Braze SDK を CocoaPods または Carthage と統合する場合は、次のコード行を `AppDelegate.swift` ファイルに追加します。

```swift
import AppboyTVOSKit
```

Swift プロジェクトでの Objective-C コードの使用方法について詳しくは、[Apple 開発者ガイド](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html)を参照してください。

`AppDelegate.swift` で、次のスニペットを `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` に追加します。

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions)
```

次に、**設定の管理**ページの正しい値で `YOUR-API-KEY` を更新します。

`sharedInstance` シングルトンは、Braze 機能を使用するための前提条件であるため、`startWithApiKey:` が呼び出される前に nil になります。

{% endtab %}
{% endtabs %}

{% alert warning %}
必ずアプリケーションのメインスレッドで Braze を初期化してください。非同期で初期化すると、機能が破損する可能性があります。
{% endalert %}

### ステップ5: カスタムエンドポイントまたはデータクラスターを指定する

{% alert note %}
2019年12月以降、カスタムエンドポイントは提供されなくなりました。既存のカスタムエンドポイントがある場合は、それを引き続き使用できます。詳細については、<a href="{{site.baseurl}}/api/basics/#endpoints">利用可能なエンドポイントのリスト</a>を参照してください。
{% endalert %}

Braze 担当者は、[正しいエンドポイント\]({{ site.baseurl }} についてすでに通知しているはずです)/user_guide/administrative/access_braze/sdk_endpoints/).

#### コンパイル時のエンドポイント構成 (推奨)
既存のカスタムエンドポイントが指定されている場合:
\- Braze iOS SDK v 3.0.2以降では、`Info.plist` ファイルを使用してカスタムエンドポイントを設定できます。`Appboy` 辞書を Info.plist ファイルに追加してください。`Appboy` 辞書内で、`https://sdk.iad-01.braze.com` 文字列サブエントリを追加し、値をカスタムエンドポイント URL の権限 (たとえば、`sdk.iad-01.braze.com` ではなく `Endpoint`) に設定します。

#### ランタイムエンドポイント構成
既存のカスタムエンドポイントが指定されている場合:
\- Braze iOS SDK v 3.17.0以降では、`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` に渡される `appboyOptions` パラメーター内の `ABKEndpointKey` を使用してエンドポイントの設定をオーバーライドできます。値をカスタムエンドポイント URL 権限に設定します (例: `https://sdk.iad-01.braze.com` ではなく `sdk.iad-01.braze.com`)。

{% alert note %}
`ABKAppboyEndpointDelegate` を使用した実行時のエンドポイントの設定サポートは、Braze iOS SDK v 3.17.0 で削除されました。既に `ABKAppboyEndpointDelegate` を使用している場合は、Braze iOS SDK バージョン v3.14.1 から v3.16.0 では、`getApiEndpoint()` メソッドの `dev.appboy.com` への参照を `sdk.iad-01.braze.com` への参照に置き換える必要があります。
{% endalert %}

### SDK の統合が完了

これで、Braze はアプリケーションからデータを収集しており、基本的な統合は完了しているはずです。tvOS アプリおよびその他のサードパーティライブラリをコンパイルするときは、ビットコードを有効にする必要があることに注意してください。

### CocoaPods 経由で Braze SDK を更新する

CocoaPod を更新するには、プロジェクトディレクトリ内で次のコマンドを実行するだけです。

```
pod update
```

## 起動時の Braze のカスタマイズ

起動時に Braze をカスタマイズする場合は、代わりに Braze 初期化メソッド `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions` を使用し、オプションの Braze 起動キーの `NSDictionary` を渡すことができます。
{% tabs %}
{% tab OBJECTIVE-C %}

`AppDelegate.m` ファイルの `application:didFinishLaunchingWithOptions` メソッド内に、次の Braze メソッドを追加します。

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endtab %}
{% tab swift %}

`AppDelegate.swift` の `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` メソッド内に、次の Braze メソッドを追加します。

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:appboyOptions)
```

ここで、`appboyOptions` はスタートアップ構成値の `Dictionary` です。

{% endtab %}
{% endtabs %}

このメソッドは `startWithApiKey:inApplication:withLaunchOptions:` 初期化メソッドを置き換え、次のパラメーターで呼び出されます。

- `YOUR-API-KEY`:アプリケーションの API キーは、Braze ダッシュボードの [**設定の管理**] にあります。
- `application`:現在のアプリ。
- `launchOptions`:`application:didFinishLaunchingWithOptions:` から取得するオプション `NSDictionary`。
- `appboyOptions`:Braze のスタートアップ構成値を持つオプションの `NSDictionary`。

Braze のスタートアップキーのリストについては、[Appboy.h][apple_initial_setup_5] を参照してください。

## Appboy.sharedInstance() と Swift の nullability
一般的な慣例とは多少異なりますが、`Appboy.sharedInstance()` シングルトンはオプションです。これは、`startWithApiKey:` が呼び出さられる前は `sharedInstance` が `nil` であり、遅延初期化を使用できる非標準で無効ではない実装がいくつかあるためです。

Appboy の `sharedInstance` (標準実装) にアクセスする前に `didFinishLaunchingWithOptions:` デリゲートで `startWithApiKey:` を呼び出すと、`Appboy.sharedInstance()?.changeUser("testUser")` のようなオプションのチェーンを使用して、煩雑なチェックを回避できます。これは、非 null `sharedInstance` を想定した Objective-C 実装と同等になります。

## 手動統合オプション

tvOS SDK を手動で統合することもできます。[パブリックリポジトリ][1]からフレームワークを取得し、前のセクションで説明したように Braze を初期化するだけです。

## ユーザーの特定とレポート分析
ユーザー ID の設定、カスタムイベントのログ記録、ユーザー属性の設定については、[iOS ドキュメント][3]を参照してください。また、[イベントの命名規則]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/)についてもよく理解しておくことをお勧めします。

[1]: https://github.com/appboy/appboy-ios-sdk
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/
[support]: {{site.baseurl}}/braze_support/
[apple_initial_setup_1]: http://cocoapods.org/
[apple_initial_setup_2]: https://www.ruby-lang.org/en/installation/
[apple_initial_setup_3]: http://guides.cocoapods.org/using/getting-started.html "CocoaPods のインストール手順"
[apple_initial_setup_4]: http://guides.cocoapods.org/syntax/podfile.html
[apple_initial_setup_5]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h
[apple_initial_setup_8]: #manual-sdk-integration
[apple_initial_setup_12]: #appboy-podfiles-for-non-64-bit-apps
[apple\_initial\_setup\_15]: {% image_buster /assets/img_archive/podsworkspace.png %}
[apple\_initial\_setup\_17]: http://guides.cocoapods.org/using/getting-started.html#updating-cocoapods
[apple\_initial\_setup\_19]: https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html
[apple\_initial\_setup\_21]: {{ site.baseurl }}/partner_integrations/#attribution-integration
[apple\_initial\_setup\_25]: http://guides.cocoapods.org/using/troubleshooting.html "CocoaPods Troubleshooting Guide"
[apple\_initial\_setup\_27]: https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md "iOS Changelog"
[apple\_initial\_setup\_31]: {{ site.baseurl }}/developer_guide/rest_api/basics/#endpoints
[apple\_initial\_setup\_32]: {{ site.baseurl }}/support_contact/
