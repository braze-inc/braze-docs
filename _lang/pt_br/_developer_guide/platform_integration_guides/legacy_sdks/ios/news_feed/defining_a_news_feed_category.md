---
nav_title: Definição de uma categoria do feed de notícias
article_title: Definição de uma categoria de feed de notícias para iOS
platform: iOS
page_order: 4
description: "Este artigo de referência mostra como definir uma categoria do Feed de notícias em seu aplicativo iOS."
channel:
  - news feed

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Definição de uma categoria do Feed de notícias

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

As instâncias do Braze News Feed podem ser configuradas para receber apenas cartões de uma determinada categoria. Isso permite a integração eficaz de vários fluxos do Feed de notícias em um único aplicativo. Para saber mais sobre esse recurso, visite nossas [práticas recomendadas]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/) do Feed de notícias.

As categorias do feed de notícias podem ser definidas chamando um dos seguintes métodos à medida que você carrega o feed de notícias:

{% tabs %}
{% tab OBJECTIVE C %}

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


Você também pode preencher um feed com uma combinação de categorias, como no exemplo a seguir:

{% tabs %}
{% tab OBJECTIVE C %}

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

