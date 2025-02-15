---
nav_title: CocoaPods
article_title: iOS 用 CocoaPods 統合
platform: Swift
page_order: 2
description: "この参照記事では、iOS 用 CocoaPods を使用して Braze Swift SDK を統合する方法を説明します。"

---

# CocoaPods との統合

## ステップ1:CocoaPods のインストール

[CocoaPods](http://cocoapods.org/) 経由で iOS SDK をインストールすると、インストールプロセスの大部分が自動化されます。CocoaPods をインストールするには、CocoaPods の[入門ガイド](https://guides.cocoapods.org/using/getting-started.html)を参照してください。

開始するには、次のコマンドを実行します。

```bash
$ sudo gem install cocoapods
```

CocoaPods に関して問題がある場合は、CocoaPods [[トラブルシューティングガイド](http://guides.cocoapods.org/using/troubleshooting.html "CocoaPods トラブルシューティングガイド")] を参照してください。

## ステップ 2:Podfile の構築

CocoaPods Ruby Gem をインストールしたら、Xcode プロジェクトのディレクトリに `Podfile` という名前のファイルを作成する必要があります。

{% alert note %}
バージョン7.4.0から、Braze SWIFT SDKには、[静的XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static)および[ダイナミックなXCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic)としての追加の配布チャネルがあります。これらの形式のいずれかを使用したい場合は、それぞれのリポジトリのインストール手順に従ってください。
{% endalert %}

次の行を Podfile に追加します。

```
target 'YourAppTarget' do
  pod 'BrazeKit'
end
```

`BrazeKit` にはメイン SDK ライブラリーが含まれており、分析とプッシュ通知のサポートが提供されています。

ポッドの更新がマイナー バージョンの更新よりも小さいものを自動的に取得するように、Braze をバージョン管理することをお勧めします。これは `pod 'BrazeKit' ~> Major.Minor.Build` のように見えます。大きな変更があっても、Braze SDK の最新バージョンを自動的に統合したい場合は、Podfile で `pod 'BrazeKit'` を使用できます。

#### 追加ライブラリー

Braze Swift SDK は、開発者がどの機能をプロジェクトにインポートするかをより詳細に制御できるように、機能をスタンドアロンライブラリーに分離しています。`BrazeKit` に加えて、以下のライブラリーを Podfile に追加できます。

| 図書館 | 詳細 |
| ------- | ------- |
| `pod 'BrazeLocation'` | 位置情報ライブラリーは、位置情報分析とジオフェンス監視をサポートします。 |
| `pod 'BrazeUI'` | アプリ内メッセージおよびコンテンツカード用のBraze提供のユーザーインターフェイスライブラリー。 |
{: .ws-td-nw-1}

##### 拡張ライブラリ

[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) と [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories) は、追加機能を提供するエクステンションモジュールであり、メインアプリケーションターゲットに直接追加すべきではありません。その代わりに、これらのモジュールごとに個別の拡張ターゲットを作成し、対応するターゲットにBrazeモジュールをインポートする必要がある。

| 図書館 | 詳細 |
| ------- | ------- |
| `pod 'BrazeNotificationService'` | リッチプッシュ通知をサポートする通知サービス拡張ライブラリー。 |
| `pod 'BrazePushStory'` | プッシュストーリーをサポートする通知コンテンツ拡張ライブラリーを提供します。 |
{: .ws-td-nw-1}

## ステップ3:Braze SDK のインストール

Braze SDK CocoaPod をインストールするには、ターミナル内で Xcode アプリプロジェクトのディレクトリに移動し、次のコマンドを実行します。
```
pod install
```

この時点で、CocoaPods によって作成された新しい Xcode プロジェクトワークスペースを開くことができるはずです。Xcode プロジェクトの代わりに、必ずこの Xcode ワークスペースを使用してください。

![新しい`BrazeExample.workspace` を表示するために拡張された Braze Example フォルダ]({% image_buster /assets/img/braze_example_workspace.png %})

## 次のステップ

指示に従って[統合を完了]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/)します。

## CocoaPods による Braze SDK のアップデート

CocoaPod を更新するには、プロジェクトディレクトリ内で以下のコマンドを実行するだけです。

```
pod update
```

