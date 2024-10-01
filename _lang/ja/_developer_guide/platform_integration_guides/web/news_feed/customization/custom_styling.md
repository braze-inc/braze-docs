---
nav_title: カスタムスタイル
article_title: Webのニュースフィードカスタムスタイル
platform: Web
page_order: 0
page_type: reference
description: "この記事では、Web アプリライケーションのカスタムニュースフィードスタイルオプションについて説明します。"
channel: news feed

---

# カスタムスタイル

> この記事では、Web アプリライケーションのカスタムニュースフィードスタイルオプションについて説明します。

{% alert note %}
ニュースフィードは非推奨になります。Braze では、News Feed ツールを使用するお客様は、コンテンツカードメッセージングチャネルに移動することを推奨しています。これは、より柔軟でカスタマイズ可能で、信頼性が高いチャネルです。詳しくは[マイグレーションガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。
{% endalert %}

Braze の UI 要素は、Braze ダッシュボード内のコンポーザーと一致するデフォルトのルックアンドフィールを備えており、他の Braze モバイルプラットフォームとの一貫性確保を目的としています。Brazeの既定のスタイルは、Braze SDK内のCSSで定義されます。アプリケーションで選択したスタイルを上書きすることで、独自の背景画像、フォントファミリ、スタイル、サイズ、アニメーションなどを使用して標準フィードをカスタマイズできます。

たとえば、次の例はニュースフィードを幅800ピクセルで表示する上書きを示しています。

``` css
body .ab-feed {
  width: 800px;
}
```