---
nav_title: CocoaPods
article_title: iOS 用 CocoaPods 統合
platform: Swift
page_order: 2
description: "この参照記事では、CocoaPods for iOS を使用してBraze Swift SDK を統合する方法について説明します。"

---

# CocoaPods との統合

## ステップ1:CocoaPods のインストール

[CocoaPods][apple_initial_setup_1] 経由で iOS SDK をインストールすると、インストールプロセスの大部分が自動化されます。CocoaPodsをインストールするには、CocoaPods[入門ガイド][cocoapods_getting_started]を参照してください。

開始するには、次のコマンドを実行します。

```bash
$ sudo gem install cocoapods
```

CocoaPods に関して問題がある場合は、CocoaPods [トラブルシューティングガイド][apple\_initial\_setup\_25] を参照してください。

## ステップ 2: Podfile の構築

CocoaPods Ruby Gem をインストールしたら、Xcode プロジェクトのディレクトリに `Podfile` という名前のファイルを作成する必要があります。

{% alert note %}
バージョン7.4.0 以降、Braze Swift SDK には、[static XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static) および[dynamic XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic) として追加の配布チャネルがあります。これらの形式のいずれかを代わりに使用する場合は、それぞれのリポジトリからのインストール手順に従います。
{% endalert %}

Podfile に次の行を追加します。

```
target 'YourAppTarget' do
  pod 'BrazeKit'
end
```

`BrazeKit` メインのSDK ライブラリが含まれ、分析およびプッシュ通知のサポートが提供されます。

ポッドの更新がマイナー バージョンの更新よりも小さいものを自動的に取得するように、Braze をバージョン管理することをお勧めします。これは `pod 'BrazeKit' ~> Major.Minor.Build` のように見えます。大きな変更があっても、Braze SDK の最新バージョンを自動的に統合したい場合は、Podfile で `pod 'BrazeKit'` を使用できます。

#### 追加ライブラリ

Braze Swift SDK は、機能をスタンドアロンライブラリに分割し、開発者がプロジェクトにインポートする機能をより詳細に制御できるようにします。`BrazeKit` に加えて、以下のライブラリをPodfile に追加できます。

| ライブラリ| 詳細|
| ------- | ------- |
| `pod 'BrazeLocation'` | ロケーション分析とジオフェンスモニタリングのサポートを提供するロケーションライブラリ|
| `pod 'BrazeUI'` | アプリ内メッセージおよびコンテンツカード用の Braze 提供ユーザーインタフェースライブラリ。|
{: .ws-td-nw-1}

##### 拡張ライブラリ

[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications)および[BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories)は、追加機能を提供する拡張モジュールであり、メインアプリケーションターゲットに直接追加することはできません。代わりに、これらのモジュールごとに個別の拡張ターゲットを作成し、対応するターゲットに Braze モジュールをインポートする必要があります。

| ライブラリ| 詳細|
| ------- | ------- |
| `pod 'BrazeNotificationService'` | リッチプッシュ通知のサポートを提供する通知サービス拡張ライブラリ|
| `pod 'BrazePushStory'` | プッシュストーリーのサポートを提供する通知コンテンツ拡張ライブラリ|
{: .ws-td-nw-1}

## ステップ3:Braze SDK のインストール

Braze SDK CocoaPods をインストールするには、ターミナル内で Xcode アプリプロジェクトのディレクトリに移動し、次のコマンドを実行します。
```
pod install
```

この時点で、CocoaPods によって作成された新しい Xcode プロジェクトワークスペースを開くことができるはずです。Xcode プロジェクトの代わりに、必ずこの Xcode ワークスペースを使用してください。

![ろう付けの例のフォルダが展開され、新しい\`Braze Example.workspace\`.][apple\_initial\_setup\_15] が表示されます。

## 次のステップ

指示に従って[統合を完了]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/)します。

## CocoaPods による Braze SDK のアップデート

CocoaPod を更新するには、プロジェクトディレクトリ内で以下のコマンドを実行するだけです。

```
pod update
```

[apple_initial_setup_1]: http://cocoapods.org/
[cocoapods_getting_started]: https://guides.cocoapods.org/using/getting-started.html
[apple_initial_setup_2]: https://www.ruby-lang.org/en/installation/
[apple_initial_setup_3]: http://guides.cocoapods.org/using/getting-started.html "CocoaPods のインストール手順"
[apple_initial_setup_5]: https://github.com/braze-inc/braze-ios-sdk/blob/master/AppboyKit/include/Appboy.h
[apple\_initial\_setup\_15]: {% image_buster /assets/img/braze_example_workspace.png %}
[apple\_initial\_setup\_25]: http://guides.cocoapods.org/using/troubleshooting.html "CocoaPods Troubleshooting Guide"
