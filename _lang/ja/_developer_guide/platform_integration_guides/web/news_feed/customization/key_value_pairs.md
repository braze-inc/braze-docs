---
nav_title: キーと値のペア
article_title: ニュースフィード ウェブ用キー・バリュー・ペア
platform: Web
page_order: 1
page_type: reference
description: "この記事では、Braze SDKを介してニュースフィードカードでキーバリューペアを使用する方法について説明します。"
channel: news feed

---

# キーと値のペア

> この記事では、Braze SDKを介してニュースフィードカードでキーバリューペアを使用する方法について説明します。

{% alert note %}
ニュースフィードは非推奨になります。Braze では、News Feed ツールを使用するお客様は、コンテンツカードメッセージングチャネルに移動することを推奨しています。これは、より柔軟でカスタマイズ可能で、信頼性が高いチャネルです。詳しくは[マイグレーションガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。
{% endalert %}

オプションで、`Card` オブジェクトはキーと値のペアを `extras` として保持できます。これらは、カードと一緒にデータを送信し、アプリケーションでさらに処理するために使用します。`card.extras`を呼び出して、これらの値にアクセスします。

[ClassicCard][3]、[ImageOnly][4]、[CaptionedImage][5] の詳細については、JSDocs を参照してください。

[3]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html
[4]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html
[5]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html
