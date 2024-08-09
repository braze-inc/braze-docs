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

[CocoaPods][apple_initial_setup_1] 経由で iOS SDK をインストールすると、インストールプロセスの大部分が自動化されます。このプロセスを開始する前に、[Ruby バージョン 2.0.0][apple_initial_setup_2] 以降を使用していることを確認してください。この SDK のインストールに Ruby 構文の知識は必要ありませんのでご安心ください。

開始するには、次のコマンドを実行します。

```bash
$ sudo gem install cocoapods
```

CocoaPods に関して問題がある場合は、CocoaPods [トラブルシューティングガイド][apple\_initial\_setup\_25] を参照してください。

{% alert note %}
`rake` 実行ファイルを上書きするよう求められた場合は、CocoaPods.org の「[の概要](http://guides.cocoapods.org/using/getting-started.html " CocoaPodsインストール手順")」を参照してください。
{% endalert %}

## ステップ2:Podfile の構築

CocoaPods Ruby Gem をインストールしたら、Xcode プロジェクトのディレクトリに `Podfile` という名前のファイルを作成する必要があります。

Podfile に次の行を追加します。

```
target 'YourAppTarget' do
  pod 'Appboy-iOS-SDK'
end
```

ポッドのアップデートがマイナーバージョンのアップデートよりも小さなものを自動的に取得するように、Braze のバージョンを設定することをお勧めします。これは `pod 'Appboy-iOS-SDK' ~> Major.Minor.Build` のように見えます。大きな変更があっても、Braze SDK の最新バージョンを自動的に統合したい場合は、Podfile で `pod 'Appboy-iOS-SDK'` を使用できます。

#### サブスペック

インテグレータは、弊社の完全な SDK をインポートすることをお勧めします。ただし、特定の Braze 機能のみを統合することが決まっている場合は、SDK 全体ではなく、目的の UIサブスペックのみをインポートできます。

| サブスペック |詳細 |
| ------- | ------- |
| `pod 'Appboy-iOS-SDK/InAppMessage'` | `InAppMessage` のサブスペックには、Braze のアプリ内メッセージ UI とCore SDK が含まれています。|
| `pod 'Appboy-iOS-SDK/ContentCards'` | `ContentCards` のサブスペックには、Braze Content Card UI と Core SDKが含まれています。|
| `pod 'Appboy-iOS-SDK/NewsFeed'` | `NewsFeed` のサブスペックには Braze Core SDK が含まれています。|
| `pod 'Appboy-iOS-SDK/Core'` | `Core` のサブスペックには、カスタムイベントや属性などの分析のサポートが含まれています。|
{: .ws-td-nw-1}

## ステップ3:Braze SDK のインストール

Braze SDK CocoaPods をインストールするには、ターミナル内で Xcode アプリプロジェクトのディレクトリに移動し、次のコマンドを実行します。
```
pod install
```

この時点で、CocoaPods で作成した新しい Xcode プロジェクトのワークスペースを開くことができるはずです。Xcode プロジェクトではなく、必ずこの Xcode ワークスペースを使用してください。 

![新しい \`AppbpyExample.workspace\`を表示するために展開された Appboy Example フォルダ。][apple\_initial\_setup\_15]

## 次のステップ

指示に従って[統合を完了]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/)します。

## CocoaPods による Braze SDK のアップデート

CocoaPod を更新するには、プロジェクトディレクトリ内で以下のコマンドを実行するだけです。

```
pod update
```

[apple_initial_setup_1]: http://cocoapods.org/
[apple_initial_setup_2]: https://www.ruby-lang.org/en/installation/
[apple_initial_setup_3]: http://guides.cocoapods.org/using/getting-started.html "CocoaPods のインストール手順"
[apple_initial_setup_5]: https://github.com/braze-inc/braze-ios-sdk/blob/master/AppboyKit/include/Appboy.h
[apple\_initial\_setup\_15]: {% image_buster /assets/img_archive/podsworkspace.png %}
[apple\_initial\_setup\_25]: http://guides.cocoapods.org/using/troubleshooting.html "CocoaPods Troubleshooting Guide"
