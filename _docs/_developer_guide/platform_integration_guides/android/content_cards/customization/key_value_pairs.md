---
nav_title: Key-Value Pairs
article_title: Content Card Key-Value Pairs for Android and FireOS
page_order: 4.2
platform: 
  - Android
  - FireOS
description: "This article covers customization options for your Content Cards in your Android application."
channel:
  - content cards

---

# Key-value pairs

`Card` objects may optionally carry key-value pairs as `extras`. These can be used to send data along with a `Card` for further handling by the application.

See our [KDoc][36] for more information.

{% alert note %}
Content Cards have a maximum size limit of 2 KB for content you enter in the Braze dashboard. This includes message text, image URLs, links, and key-value pairs. Exceeding that amount will prevent the card from sending.
{% endalert %}

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/customize/#customization-approaches
[36]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.models.cards/-card/get-extras.html
