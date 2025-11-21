---
nav_title: Embedding GIFs
article_title: Embedding GIFs in Content Cards
page_order: 5
description: "Learn how to embed GIFs into Content Cards using the Braze SDK."
channel:
  - content cards
platform:
  - Android
  - Swift
  - Web
  - FireOS
---

# Embedding GIFs in Content Cards

> Learn how to embed GIFs into Content Cards using the Braze SDK.

{% alert note %}
For wrapper SDKs not listed, use the relevant native Android or Swift method instead. Keep in mind, the Android and Swift Braze SDKs don't support animated GIFs natively, so you'll implement Content Card GIFs using third-party tools instead.
{% endalert %}

{% sdktabs %}
{% sdktab web %}
At this time, Content Card GIFs are not supported for the Web Braze SDK.
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/_global/gifs.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/gifs.md %}
{% endsdktab %}
{% endsdktabs %}
