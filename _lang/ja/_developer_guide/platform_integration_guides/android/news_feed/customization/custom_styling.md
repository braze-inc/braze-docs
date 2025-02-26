---
nav_title: カスタムスタイル
article_title: Android および FireOS 向けカスタムニュースフィードスタイル
page_order: 0
platform: 
  - Android
  - FireOS
description: "このリファレンス記事では、Android または FireOS アプリケーションにカスタムニュースフィードスタイルを追加する方法について説明します。"
channel:
  - news feed
  
---

# カスタムスタイル

> このリファレンス記事では、Android または FireOS アプリケーションにカスタムニュースフィードスタイルを追加する方法について説明します。 

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Braze の UI 要素は、Android 標準の UI ガイドラインにマッチしたデフォルトのルックアンドフィールで提供され、シームレスな体験を提供します。これらのデフォルトのスタイルは、Braze SDK ディストリビューション内の `res/values/style.xml` ファイルで確認できます。

```xml
  <style name="Braze"/>
  <!-- Feed -->
  <style name="Braze.Feed"/>
  <style name="Braze.Feed.List">
    <item name="android:background">@android:color/transparent</item>
    <item name="android:divider">@android:color/transparent</item>
    <item name="android:dividerHeight">16.0dp</item>
    <item name="android:paddingLeft">12.5dp</item>
    <item name="android:paddingRight">5.0dp</item>
    <item name="android:scrollbarStyle">outsideInset</item>
  </style>
  ...
  </style>
```

必要に応じて、これらのスタイルをオーバーライドし、アプリにより適したルックアンドフィールを作成することができます。スタイルをオーバーライドするには、スタイル全体をプロジェクトの `styles.xml` ファイルにコピーし、変更を加えます。すべての属性が正しく設定されるようにするには、スタイル全体をローカルの `styles.xml` にコピーする必要があります。

{% tabs local %}
{% tab 正しいスタイルのオーバーライド %}

```xml
<style name="Braze.Feed.List">
  <item name="android:background">@color/mint</item>
  <item name="android:cacheColorHint">@color/mint</item>
  <item name="android:divider">@android:color/transparent</item>
  <item name="android:dividerHeight">16.0dp</item>
  <item name="android:paddingLeft">12.5dp</item>
  <item name="android:paddingRight">5.0dp</item>
  <item name="android:scrollbarStyle">outsideInset</item>
</style>
```
{% endtab %}
{% tab スタイルのオーバーライドが正しくない %}

```xml
<style name="Braze.Feed.List">
  <item name="android:background">@color/mint</item>
  <item name="android:cacheColorHint">@color/mint</item>
</style>
```
{% endtab %}
{% endtabs %}

## フィードのスタイル要素

以下は、テーマ化可能な Braze UI 要素と、スタイル設定を目的としたその名前の説明です。

{% gallery %}{% image_buster /assets/img_archive/Image27Theming.png %}
{% image_buster /assets/img_archive/Image28Theming.png %}
{% image_buster /assets/img_archive/Image29Theming.png %}
{% image_buster /assets/img_archive/Image30Theming.png %}{% endgallery %}

## カスタムフォントの設定

Braze では、[フォントファミリガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization)を使用してカスタムフォントを設定することができます。これを使用するには、カードのスタイルをオーバーライドし、`fontFamily` 属性を使用してカスタムフォントファミリを使用するように Braze に指示します。

たとえば、短いニュースカードのすべてのタイトルのフォントを更新するには、`Braze.Cards.ShortNews.Title` スタイルをオーバーライドし、カスタムフォントファミリを参照します。属性値は、`res/font`ディレクトリのフォントファミリを指す必要があります。

以下は、最後の行でカスタムフォントファミリ `my_custom_font_family` が参照されている部分的なコード例です。

```
<style name="Braze.Cards.ShortNews.Title">
  <item name="android:layout_height">wrap_content</item>
  ...
  <item name="android:fontFamily">@font/my_custom_font_family</item>
  <item name="fontFamily">@font/my_custom_font_family</item>
</style>
```

