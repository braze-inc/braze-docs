---
nav_title: Pares clave-valor
article_title: Pares clave-valor de fuentes de noticias para la Web
platform: Web
page_order: 1
page_type: reference
description: "Este artículo explica cómo utilizar pares clave-valor en tus tarjetas de canal de noticias a través del SDK de Braze."
channel: news feed

---

# Pares clave-valor

> Este artículo explica cómo utilizar pares clave-valor en tus tarjetas de canal de noticias a través del SDK de Braze.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Los objetos `Card` pueden llevar opcionalmente pares clave-valor como `extras`. Se pueden utilizar para enviar datos hacia abajo junto con una tarjeta para su posterior manipulación por la aplicación. Llama a `card.extras` para acceder a estos valores.

Consulta los JSDocs para obtener más información sobre [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html), [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html) y [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html).

