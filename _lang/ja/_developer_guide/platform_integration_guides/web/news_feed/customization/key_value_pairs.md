---
nav_title: キーと値のペア
article_title: ニュースフィード ウェブ用キー・バリュー・ペア
platform: Web
page_order: 1
page_type: reference
description: "この記事では、Braze SDKを介してニュースフィードカードでキーバリューペアを使用する方法について説明する。"
channel: news feed

---

# キーと値のペア

> この記事では、Braze SDKを介してニュースフィードカードでキーバリューペアを使用する方法について説明する。

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

オプションで、`Card` オブジェクトはキーと値のペアを `extras` として保持できます。これらは、カードと一緒にデータを送信し、アプリケーションでさらに処理するために使用します。`card.extras`を呼び出して、これらの値にアクセスします。

[ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html)、[ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html)、[CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html) については JSDocs を参照してください。

