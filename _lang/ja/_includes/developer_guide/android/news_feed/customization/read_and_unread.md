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

