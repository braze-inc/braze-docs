---
nav_title: 既読 / 未読インジケーター
article_title: Web のニュースフィード読み取りおよび未読インジケータ
platform: Web
page_order: 2
page_type: reference
description: "この記事では、Braze SDK を使用して、ニュースフィードカードに読み込みインジケータと未読インジケータを設定する方法について説明します。"
channel: news feed

---

# 既読 / 未読インジケーター

> この記事では、Braze SDK を使用して、ニュースフィードカードに読み込みインジケータと未読インジケータを設定する方法について説明します。

{% alert note %}
ニュースフィードは非推奨になります。Braze では、News Feed ツールを使用するお客様は、コンテンツカードメッセージングチャネルに移動することを推奨しています。これは、より柔軟でカスタマイズ可能で、信頼性が高いチャネルです。詳しくは[マイグレーションガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。
{% endalert %}

Braze は、次のように、News Feed カードに未読および読み取りインジケータを提供します image:

![時計の画像とテキストを表示するニュースフィードカード。テキストの上隅には、カードが読まれたかどうかを示す青色または灰色の三角形があります。青い三角形はカードが読まれたことを示します。][25]

## インジケータの無効化

この機能を無効にするには、以下のスタイルをCSS に追加します。

``` css
.ab-read-dot { display: none; }
.ab-read-indicator { display: none; }
```

[25]: {% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %}
