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

{% multi_lang_include archive/objective-c-deprecation-notice.md %}

# カスタムスタイリング

{% alert note %}
ニュースフィードは非推奨になります。Braze では、ニュースフィードツールを使用しているお客様に、より柔軟でカスタマイズ可能で信頼性の高いコンテンツカードメッセージングチャネルに移行することをお勧めします。詳細については、[移行ガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。
{% endalert %}

iOS のアプリ内メッセージ、ニュースフィード、コンテンツカード内に画像を表示するために Braze UI を使用する場合は、`SDWebImage` の統合が必要です。

## デフォルト画像を上書きする

Braze では、クライアントが既存のデフォルト画像を独自のカスタム画像に置き換えることができます。そのためには、カスタム画像で新しい `png` ファイルを作成し、アプリの画像バンドルに追加します。次に、ファイルの名前を画像の名前に変更して、ライブラリー内の既定の画像をオーバーライドします。また、さまざまな携帯電話のサイズに対応できるよう、`@2x` と `@3x` のバージョンの画像を必ずアップロードしてください。コンテンツカードでオーバーライド可能な画像は以下の通りです。ニュースフィードでオーバーライド可能な画像は以下の通りです。

* 読み取りアイコンのインジケーター： `Icons_Read`
* プレースホルダー image: `img-noimage-lrg`

{% alert important %}
Xamarin の iOS の統合では、デフォルト画像のオーバーライドは現在サポートされていません。
{% endalert %}

