---
nav_title: カスタムスタイリング
article_title: iOS 用カスタムニュースフィードスタイリング
platform: iOS
page_order: 0
description: "この参照記事では、iOS アプリケーションでカスタムニュースフィードスタイルを実装し、デフォルト画像をオーバーライドする方法について説明します。"
channel:
  - news feed

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# カスタムスタイリング

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

iOS のアプリ内メッセージ、ニュースフィード、コンテンツカード内に画像を表示するために Braze UI を使用する場合は、`SDWebImage` の統合が必要です。

## デフォルト画像を上書きする

Braze では、クライアントが既存のデフォルト画像を独自のカスタム画像に置き換えることができます。そのためには、カスタム画像で新しい `png` ファイルを作成し、アプリの画像バンドルに追加します。次に、ファイルの名前を画像の名前に変更して、ライブラリー内の既定の画像をオーバーライドします。また、さまざまなスマートフォンのサイズに対応できるよう、`@2x` と `@3x` のバージョンの画像を必ずアップロードしてください。コンテンツカードでオーバーライド可能な画像は以下の通りです。ニュースフィードでオーバーライド可能な画像は以下の通りです。

* 読み取りアイコンのインジケーター： `Icons_Read`
* プレースホルダ画像： `img-noimage-lrg`

{% alert important %}
Xamarin の iOS の統合では、デフォルト画像のオーバーライドは現在サポートされていません。
{% endalert %}

