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

{% alert note %}
ニュースフィードは非推奨になります。Braze では、News Feed ツールを使用するお客様は、コンテンツカードメッセージングチャネルに移動することを推奨しています。これは、より柔軟でカスタマイズ可能で、信頼性が高いチャネルです。詳しくは[マイグレーションガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。
{% endalert %}

Brazeは、次の画像に示すように、ニュースフィードカードに未読および既読のインジケーターを提供します:

![ニュースフィードカードが、時計の画像といくつかのテキストを表示しています。テキストの上隅には、カードが読まれたかどうかを示す青色または灰色の三角形があります。青い三角形はカードが読み取られたことを示します。][25]

## インジケーターを無効にする

この機能を無効にするには、次のスタイルをCSSに追加します:

``` css
.ab-read-dot { display: none; }
.ab-read-indicator { display: none; }
```

[25]: {% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %}
