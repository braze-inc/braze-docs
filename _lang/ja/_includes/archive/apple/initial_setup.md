Braze SDKをインストールすることで、基本的な分析機能{% if include.platform == 'iOS' %} 、ユーザーをエンゲージできるアプリ内メッセージ{% endif %} 。

{{include.platform}} Braze SDKは、Objective-CおよびSwiftプロジェクトの依存関係マネージャーである[CocoaPodsを][apple_initial_setup_1]使用してインストールまたは更新する必要がある。CocoaPods を使用すると、統合と更新がさらに簡単になります。

## {{include.platform}} SDK CocoaPodsの統合

### ステップ1:CocoaPods をインストールする

{{include.platform}} [CocoaPods][apple_initial_setup_1]経由でSDKをインストールすると、インストール作業の大部分がオートメーション化される。この処理を始める前に、[Rubyのバージョンが2.0.0][apple_initial_setup_2]以上であることを確認すること。なお、このSDKをインストールするのにRubyの構文の知識は必要ない。

以下のコマンドを実行するだけで始められる：

```bash
$ sudo gem install cocoapods
```

**Note**:`rake` 、実行ファイルを上書きするように指示された場合は、[ CocoaPods.org 「Getting Started Directions][apple_initial_setup_3]」を参照のこと。

**Note**:CocoaPodsに関して問題がある場合は、[CocoaPods Troubleshooting Guide][apple_initial_setup_25].

### ステップ2:ポッドファイルを作成する

CocoaPods Ruby Gem をインストールしたら、Xcode プロジェクト ディレクトリに `Podfile` という名前のファイルを作成する必要があります。

Podfileに以下の行を追加する：

```
target 'YourAppTarget' do
  pod 'Appboy-{{include.platform}}-SDK'
end
```

**Note**:ポッドの更新がマイナー バージョンの更新よりも小さいものを自動的に取得するように、Braze をバージョン管理することをお勧めします。これは 'pod 'Appboy-{{include.platform}}-SDK' ~>Major.Minor.Build' のように見える。大きな変更があってもBraze SDKの最新バージョンを自動的に統合したい場合は、Podfileで`pod 'Appboy-{{include.platform}}-SDK'` 。
{% if include.platform == 'iOS' %}
**Note**:BrazeのデフォルトUIを使用せず、SDWebImage依存性を導入したくない場合は、Podfileの`pod 'Appboy-iOS-SDK/Core'` のように、PodfileのBraze依存性をCore subspecに指定してほしい。{% endif %}.

### ステップ 3:Braze SDK のインストール

Braze SDK CocoaPods をインストールするには、ターミナル内で Xcode アプリプロジェクトのディレクトリに移動し、次のコマンドを実行します。
```
pod install
```

この時点で、CocoaPodsによって作成された新しいXcodeプロジェクトのワークスペースを開封できるはずだ。Xcode プロジェクトの代わりに、必ずこの Xcode ワークスペースを使用してください。 

![新しいワークスペース][apple_initial_setup_15]

### ステップ 4:アプリデリゲートの更新

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

SwiftプロジェクトでObjective-Cコードを使用するための詳細については、[Apple Developer Docsを](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html)参照のこと。

`AppDelegate.swift` で、次のスニペットを `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` に追加します。

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions)
```

**Note**:Brazeの`sharedInstance` シングルトンは、`startWithApiKey:` が呼び出される前にnilになる。これは、Brazeの機能を使用するための前提条件だからである。

{% endtab %}
{% endtabs %}

{% alert important %}
必ず「設定の管理」ページから、`YOUR-API-KEY` を正しい値で更新すること。
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
既存のカスタムエンドポイントが与えられた場合...
- Braze iOS SDK v 3.0.2以降では、`Info.plist` ファイルを使用してカスタムエンドポイントを設定できます。`Appboy` ディクショナリを Info.plist ファイルに追加します。`Appboy` ディクショナリの内部で、`Endpoint` 文字列サブエントリを追加し、値をカスタムエンドポイント url の権限に設定する（例えば、`https://sdk.iad-01.braze.com` ではなく、`sdk.iad-01.braze.com` ）。

#### ランタイムエンドポイント構成

既存のカスタムエンドポイントが与えられた場合...
- Braze iOS SDK v 3.17.0以降では、`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` に渡される `appboyOptions` パラメーター内の `ABKEndpointKey` を使用してエンドポイントの設定をオーバーライドできます。値をカスタムエンドポイントURLの権限に設定する（例えば、`https://sdk.iad-01.braze.com` ではなく、`sdk.iad-01.braze.com` ）。

{% alert note %}
`ABKAppboyEndpointDelegate` を使用した実行時のエンドポイントの設定サポートは、Braze iOS SDK v 3.17.0 で削除されました。既に `ABKAppboyEndpointDelegate` を使用している場合は、Braze iOS SDK バージョン v3.14.1 から v3.16.0 では、`getApiEndpoint()` メソッドの `dev.appboy.com` への参照を `sdk.iad-01.braze.com` への参照に置き換える必要があります。
{% endalert %}

{% alert important %}
具体的なクラスタについては、カスタマーサクセスマネージャーにお尋ねいただくか、サポートチームにお問い合わせいただきたい。
{% endalert %}

### SDK 統合の完了

Brazeがアプリケーションからデータを収集するようになり、基本的な統合が完了したはずである。{% if include.platform == 'iOS' %}カスタムイベントトラッキング、プッシュメッセージング、ニュースフィード、そしてBreezeの機能一式をイネーブルメントにするために、以下のセクションを参照してください。{% else %}tvOSアプリやその他のサードパーティライブラリーをコンパイルする際には、Bitcodeをイネーブルにする必要があることに注意してください。{% endif %}

### CocoaPods 経由で Braze SDK を更新する

Cocoapodを更新するには、プロジェクト・ディレクトリ内で以下のコマンドを実行するだけだ：

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

**Note**:この方法は、`startWithApiKey:inApplication:withLaunchOptions:` の初期化方法に取って代わるだろう。

このメソッドは、次のパラメータを使用して呼び出されます。

- `YOUR-API-KEY` - BrazeダッシュボードからアプリケーションのAPI Keyを取得する。
- `application` - 現在のアプリ
- `launchOptions` - オプション`NSDictionary` から得られる。 `application:didFinishLaunchingWithOptions:`
- `appboyOptions` - オプションで、Brazeのスタートアップ設定値を`NSDictionary` 。

Braze起動キーの一覧については、[Appboy.h][apple_initial_setup_5]を参照してください。

## Appboy.sharedInstance() および Swift の nullability
一般的な慣例とは多少異なりますが、`Appboy.sharedInstance()` シングルトンはオプションです。これは、`startWithApiKey:` が呼び出さられる前は `sharedInstance` が `nil` であり、遅延初期化を使用できる非標準で無効ではない実装がいくつかあるためです。

Appboy の `sharedInstance` (標準実装) にアクセスする前に `didFinishLaunchingWithOptions:` デリゲートで `startWithApiKey:` を呼び出すと、`Appboy.sharedInstance()?.changeUser("testUser")` のようなオプションのチェーンを使用して、煩雑なチェックを回避できます。これは、非 null `sharedInstance` を想定した Objective-C 実装と同等になります。

[apple_initial_setup_1]: http://cocoapods.org/
[apple_initial_setup_2]: https://www.ruby-lang.org/en/installation/
[apple_initial_setup_3]: http://guides.cocoapods.org/using/getting-started.html "CocoaPods のインストール手順"
[apple_initial_setup_4]: http://guides.cocoapods.org/syntax/podfile.html
[apple_initial_setup_5]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h
[apple_initial_setup_8]: #manual-sdk-integration
[apple_initial_setup_12]: #appboy-podfiles-for-non-64-bit-apps
[apple_initial_setup_15]: {% image_buster /assets/img_archive/podsworkspace.png %}
[apple_initial_setup_17]: http://guides.cocoapods.org/using/getting-started.html#updating-cocoapods
[apple_initial_setup_19]: https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html
[apple_initial_setup_21]: {{ site.baseurl }}/partner_integrations/#attribution-integration
[apple_initial_setup_25]:http://guides.cocoapods.org/using/troubleshooting.html "CocoaPodsトラブルシューティングガイド"
[apple_initial_setup_27]: https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md "iOS Changelog"
[apple_initial_setup_31]: {{ site.baseurl }}/developer_guide/rest_api/basics/#endpoints
[apple_initial_setup_32]: {{ site.baseurl }}/support_contact/
