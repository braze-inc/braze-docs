---
nav_title: Definição de uma categoria do feed de notícias
article_title: Definição de uma categoria de feed de notícias para Android e FireOS
page_order: 3
platform: 
  - Android
  - FireOS
description: "Este artigo de referência mostra como definir uma categoria de Feed de notícias em seu aplicativo para Android ou FireOS."
channel:
  - news feed
  
---

# Definição de uma categoria do Feed de notícias

Este artigo de referência mostra como definir uma categoria de Feed de notícias em seu aplicativo para Android ou FireOS.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

As instâncias do feed de notícias da Braze podem ser configuradas para receber apenas cartões de uma determinada "categoria". Isso permite a integração eficaz de vários fluxos do Feed de notícias em um único aplicativo. Para saber mais sobre esse recurso, consulte nossas [práticas recomendadas]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/) do Feed de notícias

As categorias do Feed de notícias podem ser definidas chamando os seguintes métodos à medida que você carrega o Feed de notícias:

```xml
newsFeed.setCategories(CardCategory.ALL_CATEGORIES);
newsFeed.setCategories(CardCategory.ADVERTISING);
newsFeed.setCategories(CardCategory.ANNOUNCEMENTS);
newsFeed.setCategories(CardCategory.NEWS);
newsFeed.setCategories(CardCategory.SOCIAL);
newsFeed.setCategories(CardCategory.NO_CATEGORY);
```

Você também pode preencher um feed com uma combinação de categorias, como no exemplo a seguir:

```xml
newsFeed.setCategories:EnumSet.of(CardCategory.ANNOUNCEMENTS, CardCategory.NEWS);
```


