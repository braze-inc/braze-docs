---
nav_title: 既読 / 未読インジケーター
article_title: Android および FireOS 用のニュースフィードの既読 / 未読インジケーター
page_order: 3.1
platform: 
  - Android
  - FireOS
description: "このリファレンス記事では、Android または FireOS アプリケーションのニュースフィードの既読 / 未読インジケーターについて説明します。"
channel:
  - news feed
  
---

# 既読 / 未読インジケーター

{% alert note %}
ニュースフィードは非推奨になります。Braze では、ニュースフィードツールを利用しているお客様に、コンテンツカードのメッセージングチャネルへの移行をお勧めしています。移行により、柔軟性、カスタマイズ性、信頼性が向上します。詳細については、[移行ガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。
{% endalert %}

> Braze では、オプションでニュースフィードカードの未読と既読のインジケーターを切り替えることができます。

![時計の画像とテキストを表示するニュースフィードカード。テキストの上隅には、カードが読まれたかどうかを示す青色または灰色の三角形があります。青い三角形はカードが読まれたことを示します。][25]

## インジケーターの有効化

この機能を有効にするには、`braze.xml` ファイルに次の行を追加します。

```xml
<bool name="com_braze_newsfeed_unread_visual_indicator_on">true</bool>
```

## インジケーターのカスタマイズ

これらのインジケーターは、`icon_read` および `icon_unread` ドローアブルを変更することでカスタマイズできます。

[25]: {% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %}
