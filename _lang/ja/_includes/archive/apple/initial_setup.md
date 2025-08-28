Braze SDK をインストールすると、基本的な分析機能{% if include.platform == 'iOS' %}と、ユーザーエンゲージメントのためのアプリ内メッセージが提供されます{% endif %}。

{{include.platform}} Braze SDK は、Objective-C および Swift プロジェクトの依存関係マネージャーである [CocoaPods](http://cocoapods.org/) を使用してインストールまたは更新する必要があります。CocoaPods を使用すると、統合と更新がさらに簡単になります。

## {{include.platform}} SDK CocoaPodsの統合

### ステップ1:CocoaPods をインストールする

{{include.platform}} [CocoaPods](http://cocoapods.org/)経由でSDKをインストールすると、インストール作業の大部分がオートメーション化される。この処理を始める前に、[Rubyのバージョンが2.0.0](https://www.ruby-lang.org/en/installation/)以上であることを確認すること。なお、このSDKをインストールするのにRubyの構文の知識は必要ない。

以下のコマンドを実行するだけで始められる：

```bash
$ sudo gem install cocoapods
```

**注**:`rake` 実行可能ファイルを上書きするプロンプトが表示された場合、詳細については [CocoaPods.org の Getting started Directions](http://guides.cocoapods.org/using/getting-started.html) を参照してください。

**Note**:CocoaPods に関する問題がある場合は、[CocoaPods トラブルシューティングガイド](http://guides.cocoapods.org/using/troubleshooting.html)を参照してください。

### ステップ2: ポッドファイルを作成する

CocoaPods Ruby Gem をインストールしたら、Xcode プロジェクト ディレクトリに `Podfile` という名前のファイルを作成する必要があります。

次の行を Podfile に追加します。

```
target 'YourAppTarget' do
  pod 'Appboy-{{include.platform}}-SDK'
end
```

**注**:ポッドの更新がマイナー バージョンの更新よりも小さいものを自動的に取得するように、Braze をバージョン管理することをお勧めします。これは次のようになります。'pod 'Appboy-{{include.platform}}-SDK' ~> Major.Minor.Build'大きな変更があっても最新バージョンの Braze SDK を自動的に統合する場合は、Podfileで `pod 'Appboy-{{include.platform}}-SDK'` を使用できます。
{% if include.platform == 'iOS' %}
**注**:Braze のデフォルトの UI を使用せず、SDWebImage 依存関係を導入したくない場合は、Podfile の `pod 'Appboy-iOS-SDK/Core'` のように、Podfile の Braze 依存関係を Core subspec に指定してください。{% endif %}。

### ステップ 3:Braze SDK のインストール

Braze SDK CocoaPods をインストールするには、ターミナル内で Xcode アプリプロジェクトのディレクトリに移動し、次のコマンドを実行します。
```
pod install
```

この時点で、CocoaPods によって作成された新しい Xcode プロジェクトワークスペースを開くことができるはずです。Xcode プロジェクトの代わりに、必ずこの Xcode ワークスペースを使用してください。 

![新しいワークスペース]({% image_buster /assets/img_archive/podsworkspace.png %})

### ステップ 4: アプリデリゲートの更新

{% tabs %}
{% tab OBJECTIVE-C %}

次のコード行を `AppDelegate.m` ファイルに追加します。

```objc
{% if include.platform == 'iOS' %}#import "Appboy-iOS-SDK/AppboyKit.h"{% else %}#import <AppboyTVOSKit/AppboyKit.h>{% endif %}
```

`AppDelegate.m` ファイル内で、`application:didFinishLaunchingWithOptions` メソッド内に次のスニペットを追加します。

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
         inApplication:application
     withLaunchOptions:launchOptions];
```

{% endtab %}
{% tab SWIFT %}

Braze SDK を CocoaPods または Carthage と統合する場合は、次のコード行を `AppDelegate.swift` ファイルに追加します。

```swift
{% if include.platform == 'iOS' %}import Appboy_iOS_SDK{% else %}import AppboyTVOSKit{% endif %}
```

Swift プロジェクトでの Objective-C コードの使用方法について詳しくは、[Apple 開発者ガイド](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html)を参照してください。

`AppDelegate.swift` で、次のスニペットを `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` に追加します。

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions)
```

**Note**:Braze の `sharedInstance` シングルトンは、Braze 機能を使用するための前提条件であるため、`startWithApiKey:` が呼び出される前に nil になります。

{% endtab %}
{% endtabs %}

{% alert important %}
必ず設定の管理ページの正しい値で `YOUR-API-KEY` を更新します。
{% endalert %}

{% alert warning %}
必ずアプリケーションのメインスレッドで Braze を初期化してください。非同期で初期化すると、機能が破損する可能性があります。
{% endalert %}


### ステップ5: カスタムエンドポイントまたはデータクラスターを指定する

{% alert note %}
なお、2019年12月現在、カスタムエンドポイントの配布は終了しているが、既存のカスタムエンドポイントを持っている場合は、引き続き使用することができる。詳細については、<a href="{{site.baseurl}}/api/basics/#endpoints">利用可能なエンドポイントのリスト</a>を参照してください。
{% endalert %}

Braze 担当者は、[正しいエンドポイント]({{ site.baseurl }}/user_guide/administrative/access_braze/sdk_endpoints/).についてすでに通知しているはずです。

#### コンパイル時のエンドポイント構成 (推奨)
既存のカスタムエンドポイントが指定されている場合...
- Braze iOS SDK v 3.0.2以降では、`Info.plist` ファイルを使用してカスタムエンドポイントを設定できます。`Appboy` ディクショナリを Info.plist ファイルに追加します。`Appboy` 辞書内で、`Endpoint` 文字列サブエントリを追加し、値をカスタムエンドポイント URL の権限 (たとえば、`https://sdk.iad-01.braze.com` ではなく `sdk.iad-01.braze.com`) に設定します。

#### ランタイムエンドポイント構成

既存のカスタムエンドポイントが指定されている場合...
- Braze iOS SDK v 3.17.0以降では、`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` に渡される `appboyOptions` パラメーター内の `ABKEndpointKey` を使用してエンドポイントの設定をオーバーライドできます。値をカスタムエンドポイント URL 権限 (たとえば、`https://sdk.iad-01.braze.com` ではなく `sdk.iad-01.braze.com`) に設定します。

{% alert note %}
`ABKAppboyEndpointDelegate` を使用した実行時のエンドポイントの設定サポートは、Braze iOS SDK v 3.17.0 で削除されました。既に `ABKAppboyEndpointDelegate` を使用している場合は、Braze iOS SDK バージョン v3.14.1 から v3.16.0 では、`getApiEndpoint()` メソッドの `dev.appboy.com` への参照を `sdk.iad-01.braze.com` への参照に置き換える必要があります。
{% endalert %}

{% alert important %}
具体的なクラスターについては、カスタマーサクセスマネージャーにお尋ねいただくか、サポートチームにお問い合わせください。
{% endalert %}

### SDK 統合の完了

Brazeがアプリケーションからデータを収集するようになり、基本的な統合が完了したはずである。{% if include.platform == 'iOS' %}カスタムイベント追跡、プッシュメッセージング、ニュースフィード、および Braze 機能の完全なスイートを有効にするには、次のセクションを参照してください。{% else %}tvOS アプリとその他のサードパーティー製ライブラリをコンパイルする場合は、ビットコードを有効にする必要があることに注意してください。{% endif %}

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
{% tab SWIFT %}

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

**注**:このメソッドは `startWithApiKey:inApplication:withLaunchOptions:` 初期化メソッドを置き換えます。

このメソッドは、次のパラメータを使用して呼び出されます。

- `YOUR-API-KEY` – Braze ダッシュボードのアプリケーションの API キー
- `application` - 現在のアプリ
- `launchOptions` – `application:didFinishLaunchingWithOptions:` から取得するオプション `NSDictionary`
- `appboyOptions` – Braze のスタートアップ構成値を持つオプションの `NSDictionary`

Braze起動キーの一覧については、[Appboy.h](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h)を参照してください。

## Appboy.sharedInstance() および Swift の nullability
一般的な慣例とは多少異なりますが、`Appboy.sharedInstance()` シングルトンはオプションです。これは、`startWithApiKey:` が呼び出さられる前は `sharedInstance` が `nil` であり、遅延初期化を使用できる非標準で無効ではない実装がいくつかあるためです。

Appboy の `sharedInstance` (標準実装) にアクセスする前に `didFinishLaunchingWithOptions:` デリゲートで `startWithApiKey:` を呼び出すと、`Appboy.sharedInstance()?.changeUser("testUser")` のようなオプションのチェーンを使用して、煩雑なチェックを回避できます。これは、非 null `sharedInstance` を想定した Objective-C 実装と同等になります。

