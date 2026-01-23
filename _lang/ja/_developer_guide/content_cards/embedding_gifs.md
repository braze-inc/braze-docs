---
nav_title: GIFを埋め込む
article_title: コンテンツカードにGIFを埋め込む
page_order: 5
description: "Braze SDK を使用してGIF をコンテンツカードに埋め込む方法について説明します。"
channel:
  - content cards
platform:
  - Android
  - Swift
  - Web
  - FireOS
---

# コンテンツカードにGIFを埋め込む

> Braze SDK を使用してGIF をコンテンツカードに埋め込む方法について説明します。

{% alert note %}
リストされていないラッパーSDK の場合は、代わりに関連するネイティブAndroid またはSwift メソッドを使用します。Android およびSwift Braze SDK はアニメーションGIF をネイティブにサポートしていないため、代わりにサードパーティツールを使用してコンテンツカードGIF を実装します。
{% endalert %}

{% sdktabs %}
{% sdktab web %}
GIF のサポートは、Web SDK 統合にデフォルトで含まれています。
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/_global/gifs.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/gifs.md %}
{% endsdktab %}
{% endsdktabs %}
