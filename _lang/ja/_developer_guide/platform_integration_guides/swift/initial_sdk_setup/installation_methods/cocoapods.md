---
nav_title: CocoaPods
article_title: iOS 用 CocoaPods 統合
platform: Swift
page_order: 2
description: "この参考記事では、CocoaPods for iOSを使ってBraze Swift SDKを統合する方法を紹介する。"

---

# CocoaPods との統合

## ステップ1:CocoaPods のインストール

[CocoaPods][apple_initial_setup_1] 経由で iOS SDK をインストールすると、インストールプロセスの大部分が自動化されます。CocoaPodsをインストールするには、CocoaPods[入門ガイドを][cocoapods_getting_started]参照する。

開始するには、次のコマンドを実行します。

```bash
$ sudo gem install cocoapods
```

CocoaPodsに関して問題がある場合は、CocoaPods \[トラブルシューティングガイド]\[apple_initial_setup_25].

## ステップ2:Podfile の構築

CocoaPods Ruby Gem をインストールしたら、Xcode プロジェクトのディレクトリに `Podfile` という名前のファイルを作成する必要があります。

{% alert note %}
バージョン7.4.0から、Braze Swift SDKには、[静的XCFrameworksと](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static) [動的XCFrameworksという](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic)追加の配布チャネルがある。これらのフォーマットのいずれかを代わりに使いたい場合は、それぞれのリポジトリからインストール手順に従ってほしい。
{% endalert %}

次の行を Podfile に追加します。

```
target 'YourAppTarget' do
  pod 'BrazeKit'
end
```

`BrazeKit` メインSDKライブラリが含まれており、アナリティクスとプッシュ通知をサポートしている。

ポッドの更新がマイナー バージョンの更新よりも小さいものを自動的に取得するように、Braze をバージョン管理することをお勧めします。これは `pod 'BrazeKit' ~> Major.Minor.Build` のように見えます。大きな変更があっても、Braze SDK の最新バージョンを自動的に統合したい場合は、Podfile で `pod 'BrazeKit'` を使用できます。

#### 追加ライブラリー

Braze Swift SDKは、開発者がどの機能をプロジェクトにインポートするかをよりコントロールできるように、機能をスタンドアロン・ライブラリに分離している。`BrazeKit` に加えて、以下のライブラリをPodfileに追加することができる：

| 図書館 | 詳細 |
| ------- | ------- |
| `pod 'BrazeLocation'` | ロケーション・ライブラリは、ロケーション分析とジオフェンス・モニタリングをサポートする。 |
| `pod 'BrazeUI'` | Brazeが提供するアプリ内メッセージやコンテンツカード用のユーザーインターフェイスライブラリ。 |
{: .ws-td-nw-1}

##### 拡張ライブラリ

[BrazeNotificationServiceと](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) [BrazePushStoryは](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories)、追加機能を提供する拡張モジュールであり、メインのアプリケーションターゲットに直接追加すべきではない。その代わりに、これらのモジュールごとに個別の拡張ターゲットを作成し、対応するターゲットにBrazeモジュールをインポートする必要がある。

| 図書館 | 詳細 |
| ------- | ------- |
| `pod 'BrazeNotificationService'` | リッチなプッシュ通知をサポートする通知サービス拡張ライブラリ。 |
| `pod 'BrazePushStory'` | プッシュストーリーをサポートする通知コンテンツ拡張ライブラリ。 |
{: .ws-td-nw-1}

## ステップ3:Braze SDK のインストール

Braze SDK CocoaPodをインストールするには、ターミナルでXcodeアプリプロジェクトのディレクトリに移動し、以下のコマンドを実行する：
```
pod install
```

この時点で、CocoaPods によって作成された新しい Xcode プロジェクトワークスペースを開くことができるはずです。Xcode プロジェクトの代わりに、必ずこの Xcode ワークスペースを使用してください。

![新しい`BrazeExample.workspace` を表示するために展開されたBraze Exampleフォルダ]\[apple_initial_setup_15]

## 次のステップ:

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
\[apple_initial_setup_15]: {% image_buster /assets/img/braze_example_workspace.png %}
\[apple_initial_setup_25]:http://guides.cocoapods.org/using/troubleshooting.html "CocoaPodsトラブルシューティングガイド"
