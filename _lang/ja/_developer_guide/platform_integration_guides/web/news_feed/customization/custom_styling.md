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

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Braze の UI 要素は、Braze ダッシュボード内のコンポーザーと一致するデフォルトのルックアンドフィールを備えており、他の Braze モバイルプラットフォームとの一貫性確保を目的としています。Brazeの既定のスタイルは、Braze SDK内のCSSで定義されます。アプリケーションで選択したスタイルを上書きすることで、独自の背景画像、フォントファミリ、スタイル、サイズ、アニメーションなどを使用して標準フィードをカスタマイズできます。

たとえば、次の例はニュースフィードを幅800ピクセルで表示する上書きを示しています。

``` css
body .ab-feed {
  width: 800px;
}
```