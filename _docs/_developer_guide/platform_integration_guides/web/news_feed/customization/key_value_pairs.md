---
nav_title: Key-Value Pairs
article_title: News Feed Key-Value Pairs for Web
platform: Web
page_order: 1
page_type: reference
description: "This article covers how to use key-value pairs in your News Feeds cards via the Braze SDK."
channel: news feed

---

# Key-value pairs

> This article covers how to use key-value pairs in your News Feeds cards via the Braze SDK.

{% alert note %}
News Feed is being deprecated. Braze recommends that customers who use our News Feed tool move over to our Content Cards messaging channel—it's more flexible, customizable, and reliable. Check out the [migration guide]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) for more.
{% endalert %}

`Card` objects may optionally carry key-value pairs as `extras`. These can be used to send data down along with a card for further handling by the application. Call `card.extras` to access these values.

See the JSDocs for more information on [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html), [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html), and [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html).

