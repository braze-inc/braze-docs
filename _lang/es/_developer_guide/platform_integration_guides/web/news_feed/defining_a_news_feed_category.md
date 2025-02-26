---
nav_title: Definir una categoría de canal de noticias
article_title: Definir una categoría de canal de noticias para la Web
platform: Web
page_order: 3
page_type: reference
description: "Este artículo explica cómo definir una categoría de fuente de noticias para tu aplicación Web."
channel: news feed

---

# Definir una categoría de canal de noticias

> Este artículo explica cómo definir una categoría de fuente de noticias para el SDK Web de Braze.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Las instancias de la fuente de noticias Braze pueden configurarse para que sólo reciban tarjetas de una determinada "categoría". Esto permite la integración efectiva de múltiples flujos de fuentes de noticias dentro de una única aplicación.

Las categorías del canal de noticias pueden definirse proporcionando el tercer parámetro `allowedCategories` a `toggleFeed`:

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.NEWS]);
```

También puedes rellenar una fuente con una combinación de categorías como en el siguiente ejemplo:

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.ANNOUNCEMENTS, braze.Card.Category.NEWS]);
```
