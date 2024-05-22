---
nav_title: カスタムスタイル
article_title: Web 用ニュースフィードカスタムスタイル
platform: Web
page_order: 0
page_type: reference
description: "この記事では、Web アプリケーションのカスタムニュースフィードスタイルオプションについて説明します。"
channel: news feed

---

# カスタムスタイル

> この記事では、Web アプリケーションのカスタムニュースフィードスタイルオプションについて説明します。

{% alert note %}
ニュースフィードは非推奨になります。Braze では、News Feed ツールを使用するお客様は、コンテンツカードメッセージングチャネルに移動することを推奨しています。これは、より柔軟でカスタマイズ可能で、信頼性が高いチャネルです。詳しくは[マイグレーションガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。
{% endalert %}

Braze UI要素には、Brazeダッシュボード内の作曲家に合わせたデフォルトのルックアンドフィールがあり、他のBrazeモバイルプラットフォームとの一貫性を目指しています。Braze のデフォルトスタイルは Braze SDK 内の CSS で定義されています。アプリケーションで選択したスタイルを上書きすることで、独自の背景画像、フォントファミリ、スタイル、サイズ、アニメーションなどを使用して標準フィードをカスタマイズできます。

たとえば、以下はニュースフィードの幅を 800 px にするオーバーライドの例です。

``` css
body .ab-feed {
  width: 800px;
}
```