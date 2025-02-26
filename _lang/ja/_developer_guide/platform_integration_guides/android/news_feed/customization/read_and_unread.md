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

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

> Braze では、オプションでニュースフィードカードの未読と既読のインジケーターを切り替えることができます。

![ニュースフィードのカードに、時計の画像とテキストが表示される。テキストの上隅には、カードが読まれたかどうかを示す青色または灰色の三角形があります。青い三角形はカードが読まれたことを示す。]({% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %})

## インジケーターの有効化

この機能を有効にするには、`braze.xml` ファイルに次の行を追加します。

```xml
<bool name="com_braze_newsfeed_unread_visual_indicator_on">true</bool>
```

## インジケーターのカスタマイズ

これらのインジケーターは、`icon_read` および `icon_unread` ドローアブルを変更することでカスタマイズできます。

