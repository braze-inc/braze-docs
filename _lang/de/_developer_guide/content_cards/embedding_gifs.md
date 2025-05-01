---
nav_title: GIFs einbetten
article_title: GIFs in Content-Cards einbetten
page_order: 5
description: "Erfahren Sie, wie Sie mit dem Braze SDK GIFs in Content-Cards einbetten können."
channel:
  - content cards
platform:
  - Android
  - Swift
  - Web
  - FireOS
---

# GIFs in Content-Cards einbetten

> Erfahren Sie, wie Sie mit dem Braze SDK GIFs in Content-Cards einbetten können.

{% alert note %}
Für Wrapper-SDKs, die nicht aufgeführt sind, verwenden Sie stattdessen die entsprechende native Android- oder Swift-Methode. Denken Sie daran, dass die Android und Swift Braze SDKs animierte GIFs nicht nativ unterstützen, so dass Sie Content-Card-GIFs stattdessen mit Tools von Drittanbietern implementieren werden.
{% endalert %}

{% sdktabs %}
{% sdktab android %}
{% multi_lang_include developer_guide/android/_global/gifs.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/gifs.md %}
{% endsdktab %}

{% sdktab web %}
Zur Zeit werden Content-Card-GIFs für das Internet Braze SDK nicht unterstützt.
{% endsdktab %}
{% endsdktabs %}
