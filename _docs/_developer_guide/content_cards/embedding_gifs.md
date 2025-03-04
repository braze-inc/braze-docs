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

{% sdktabs %}
{% sdktab android %}
{% multi_lang_include developer_guide/android/_global/gifs.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/gifs.md %}
{% endsdktab %}

{% sdktab web %}
At this time, Content Card GIFs are not supported for the Web Braze SDK.
{% endsdktab %}

{% sdktab fireos %}
{% multi_lang_include developer_guide/android/_global/gifs.md %}
{% endsdktab %}

{% sdktab other wrappers %}
To embed GIFs in your wrapper SDK's Content Card, you'll need to follow the steps for native Android and Swift. Keep in mind, the Android and Swift Braze SDKs don't support animated GIFs natively, so we'll show you how to implement Content Card GIFs using third-party tools instead.
{% endsdktab %}
{% endsdktabs %}
