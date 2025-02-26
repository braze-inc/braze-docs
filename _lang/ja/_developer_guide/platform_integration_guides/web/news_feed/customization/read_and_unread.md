---
nav_title: 既読および未読のインジケーター
article_title: ニュースフィードのWeb用既読および未読インジケーター
platform: Web
page_order: 2
page_type: reference
description: "この記事では、Braze SDKを使用してニュースフィードカードに既読および未読のインジケーターを設定する方法について説明します。"
channel: news feed

---

# 既読 / 未読インジケーター

> この記事では、Braze SDKを使用してニュースフィードカードに既読および未読のインジケーターを設定する方法について説明します。

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Brazeは、次の画像に示すように、ニュースフィードカードに未読および既読のインジケーターを提供します:

![ニュースフィードカードが、時計の画像といくつかのテキストを表示しています。テキストの上隅には、カードが読まれたかどうかを示す青色または灰色の三角形があります。青い三角形はカードが読まれたことを示す。]({% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %})

## インジケーターを無効にする

この機能を無効にするには、CSSに以下のスタイルを追加する：

``` css
.ab-read-dot { display: none; }
.ab-read-indicator { display: none; }
```

