---
nav_title: GIF の埋め込み
article_title: コンテンツカードへのGIF の埋め込み
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

# コンテンツカードへのGIF の埋め込み

> Braze SDK を使用してGIF をコンテンツカードに埋め込む方法について説明します。

{% alert note %}
リストされていないラッパーSDK の場合は、代わりに関連するネイティブAndroid またはSwift メソッドを使用します。Android およびSwift Braze SDK はアニメーションGIF をネイティブにサポートしていないため、代わりにサードパーティツールを使用してコンテンツカードGIF を実装します。
{% endalert %}

{% sdktabs %}
{% sdktab web %}
現時点では、Web Braze SDK ではコンテンツカードGIF はサポートされていません。
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/_global/gifs.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/gifs.md %}
{% endsdktab %}
{% endsdktabs %}
