---
nav_title: アプリ内メッセージ
article_title: tvOS のアプリ内メッセージ
platform: tvOS
page_type: reference
description: "この参照記事では、tvOS プラットフォームのアプリ内メッセージング統合ガイドラインについて説明します。"
page_order: 3
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# アプリ内メッセージとコンテンツカードの統合

> この記事では、アプリ内メッセージおよび tvOS 用のコンテンツカードをセットアップする方法について説明します。tvOS でのアプリ内メッセージとコンテンツカードのサポートは、弊社の Swift SDK を使用する場合にのみ利用可能です。

tvOS では、[Braze Swift SDK][swift-sdk] を統合することで、アプリ内メッセージとコンテンツカードチャンネルの両方でメッセージングを実行できます。tvOS アプリの Xcode プロジェクトに Braze SDK を追加した後、設定中に次の詳細を確認してください。

**1\.**tvOS アプリの Braze ダッシュボードの [**設定の管理**] で新しい iOS アプリを作成します。<br>![][1]{: style="width:70%"}<br>
{% alert warning %}
チェックボックスリストから tvOS を選択しないでください。これを行うと、コンテンツカードやアプリ内メッセージを利用できなくなります。
{% endalert %}

**2\.**Xcode プロジェクトで SDK 設定中に API キーを参照する場合は、[**設定の管理**] にリストされている API キーを使用します。<br>![][2]{: style="width:70%"}

## カスタマイズ

Braze では、tvOS のコンテンツカードまたはアプリ内メッセージのデフォルトUI は提供されません。

統合時に tvOS でこれらのチャネルをさらにカスタマイズするには、弊社の[アプリ内メッセージカスタム UI](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/in-app-message-customization) および[コンテンツカードカスタム UI](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/content-cards-customization) の記事を参照してください。また、統合をサポートするため、参照用の[サンプルプロジェクト](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples)も提供しています。 

[1]: {% image_buster /assets/img/tvos.png %}
[2]: {% image_buster /assets/img/tvos1.png %}
[swift-sdk]: https://github.com/braze-inc/braze-swift-sdk
