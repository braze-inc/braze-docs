---
nav_title: CocoaPods
article_title: iOS 用 CocoaPods 統合
platform: iOS
page_order: 2
description: "この参照記事では、iOS 用 CocoaPods を使用して Braze SDK を統合する方法を説明します。"

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# CocoaPods との統合

## ステップ1:CocoaPods のインストール

[CocoaPods](http://cocoapods.org/) 経由で iOS SDK をインストールすると、インストールプロセスの大部分が自動化されます。このプロセスを開始する前に、[Ruby バージョン 2.0.0](https://www.ruby-lang.org/en/installation/) 以降を使用していることを確認してください。この SDK のインストールに Ruby 構文の知識は必要ありませんのでご安心ください。

開始するには、次のコマンドを実行します。

```bash
$ sudo gem install cocoapods
```

CocoaPodsに関して問題がある場合は、CocoaPods[トラブルシューティングガイドを](http://guides.cocoapods.org/using/troubleshooting.html)参照すること。

{% alert note %}
`rake` 実行可能ファイルを上書きするプロンプトが表示された場合、詳細については CocoaPods.org の [Getting started Directions](http://guides.cocoapods.org/using/getting-started.html) を参照してください。
{% endalert %}

## ステップ2:Podfile の構築

CocoaPods Ruby Gem をインストールしたら、Xcode プロジェクトのディレクトリに `Podfile` という名前のファイルを作成する必要があります。

次の行を Podfile に追加します。

```
target 'YourAppTarget' do
  pod 'Appboy-iOS-SDK'
end
```

ポッドの更新がマイナー バージョンの更新よりも小さいものを自動的に取得するように、Braze をバージョン管理することをお勧めします。これは `pod 'Appboy-iOS-SDK' ~> Major.Minor.Build` のように見えます。大きな変更があっても、Braze SDK の最新バージョンを自動的に統合したい場合は、Podfile で `pod 'Appboy-iOS-SDK'` を使用できます。

#### サブスペック

インテグレータは、弊社の完全な SDK をインポートすることをお勧めします。ただし、特定の Braze 機能のみを統合することが決まっている場合は、SDK 全体ではなく、目的の UIサブスペックのみをインポートできます。

| 亜種 | 詳細 |
| ------- | ------- |
| `pod 'Appboy-iOS-SDK/InAppMessage'` | `InAppMessage` のサブスペックには、Braze のアプリ内メッセージ UI と Core SDK が含まれています。|
| `pod 'Appboy-iOS-SDK/ContentCards'` | `ContentCards` のサブスペックには、Braze Content Card UI と Core SDK が含まれています。 |
| `pod 'Appboy-iOS-SDK/NewsFeed'` | `NewsFeed` サブスペックにはBraze Core SDKが含まれている。 |
| `pod 'Appboy-iOS-SDK/Core'` | `Core` サブスペックは、カスタムイベントやアトリビュートなどのアナリティクスをサポートしている。 |
{: .ws-td-nw-1}

## ステップ3:Braze SDK のインストール

Braze SDK CocoaPods をインストールするには、ターミナル内で Xcode アプリプロジェクトのディレクトリに移動し、次のコマンドを実行します。
```
pod install
```

この時点で、CocoaPods によって作成された新しい Xcode プロジェクトワークスペースを開くことができるはずです。Xcode プロジェクトの代わりに、必ずこの Xcode ワークスペースを使用してください。 

![Appboy Exampleフォルダが展開され、新しい\`AppbpyExample.workspace\`が表示される。]({% image_buster /assets/img_archive/podsworkspace.png %})

## 次のステップ

指示に従って[統合を完了]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/completing_integration/)します。

## CocoaPods による Braze SDK のアップデート

CocoaPod を更新するには、プロジェクトディレクトリ内で以下のコマンドを実行するだけです。

```
pod update
```

