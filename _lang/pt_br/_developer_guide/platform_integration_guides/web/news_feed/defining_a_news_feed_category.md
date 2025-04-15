---
nav_title: Definindo uma Categoria de feed de notícias
article_title: Definindo uma Categoria de feed de notícias para a Web
platform: Web
page_order: 3
page_type: reference
description: "Este artigo aborda como definir uma categoria de feed de notícias para seu aplicativo web."
channel: news feed

---

# Definindo uma categoria de feed de notícias

> Este artigo aborda como definir uma categoria de feed de notícias para o Braze Web SDK.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

As instâncias do feed de notícias da Braze podem ser configuradas para receber apenas cartões de uma determinada "categoria". Isso permite a integração eficaz de vários fluxos do Feed de notícias em um único aplicativo.

Categorias de feed de notícias podem ser definidas fornecendo o terceiro parâmetro `allowedCategories` para `toggleFeed`:

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.NEWS]);
```

Você também pode preencher um feed com uma combinação de categorias, como no exemplo a seguir:

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.ANNOUNCEMENTS, braze.Card.Category.NEWS]);
```
