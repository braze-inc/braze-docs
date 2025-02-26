---
nav_title: Definir una categoría de canal de noticias
article_title: Definir una categoría de canal de noticias para iOS
platform: iOS
page_order: 4
description: "Este artículo de referencia muestra cómo definir una categoría de canal de noticias en tu aplicación iOS."
channel:
  - news feed

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Definir una categoría de canal de noticias

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Las instancias de la fuente de noticias Braze pueden configurarse para que sólo reciban tarjetas de una categoría determinada. Esto permite la integración efectiva de múltiples flujos de fuentes de noticias dentro de una única aplicación. Para obtener más información sobre esta característica, visita nuestras [mejores prácticas]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/) de la fuente de noticias.

Las categorías de la fuente de noticias pueden definirse llamando a uno de los siguientes métodos cuando cargas la fuente de noticias:

{% tabs %}
{% tab OBJETIVO-C %}

```objc
[newsFeed setCategories:ABKCardCategoryAll];
[newsFeed setCategories:ABKCardCategoryAnnouncements];
[newsFeed setCategories:ABKCardCategoryAdvertising];
[newsFeed setCategories:ABKCardCategorySocial];
[newsFeed setCategories:ABKCardCategoryNews];
[newsFeed setCategories:ABKCardCategoryNoCategory];
```

{% endtab %}
{% tab swift %}

```swift
newsFeed.categories = ABKCardCategory.all
newsFeed.categories = ABKCardCategory.announcements
newsFeed.categories = ABKCardCategory.advertising
newsFeed.categories = ABKCardCategory.social
newsFeed.categories = ABKCardCategory.news
newsFeed.categories = ABKCardCategory.noCategory
```

{% endtab %}
{% endtabs %}


También puedes rellenar una fuente con una combinación de categorías, como en el ejemplo siguiente:

{% tabs %}
{% tab OBJETIVO-C %}

```objc
[newsFeed setCategories:ABKCardCategoryAnnouncements|ABKCardCategoryAdvertising];
```

{% endtab %}
{% tab swift %}

```swift
newsFeed.categories = ABKCardCategory([.announcements, .advertising])
```

{% endtab %}
{% endtabs %}

