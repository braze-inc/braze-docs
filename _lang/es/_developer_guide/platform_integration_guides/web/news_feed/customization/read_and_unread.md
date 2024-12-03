---
nav_title: Indicadores leídos y no leídos
article_title: Indicadores de noticias leídas y no leídas para Web
platform: Web
page_order: 2
page_type: reference
description: "Este artículo explica cómo configurar indicadores no leídos y leídos en tus tarjetas de canal de noticias a través del SDK de Braze."
channel: news feed

---

# Indicadores no leídos y no leídos

> Este artículo explica cómo configurar indicadores no leídos y leídos en tus tarjetas de canal de noticias a través del SDK de Braze.

{% alert note %}
Vamos a dejar de usar el canal de noticias. Braze recomienda a los clientes que utilizan nuestra herramienta de fuente de noticias que se pasen a nuestro canal de mensajería de tarjetas de contenido: es más flexible, personalizable y fiable. Para más información, consulta la [guía de migración]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/).
{% endalert %}

Braze proporciona un indicador de leído y no leído en las tarjetas de canal de noticias, como se muestra en la siguiente imagen:

![Una tarjeta de fuente de noticias que muestra la imagen de un reloj junto con algo de texto. En la esquina superior del texto hay un triángulo azul o gris que indica si una tarjeta se ha leído o no. Un triángulo azul significa que se ha leído una tarjeta.]({% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %})

## Desactivar los indicadores

Para desactivar esta funcionalidad, añade el siguiente estilo a tu CSS:

``` css
.ab-read-dot { display: none; }
.ab-read-indicator { display: none; }
```

