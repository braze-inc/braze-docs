---
nav_title: Categorías de noticias
page_order: 9

page_type: reference
description: "Este artículo de referencia describe las categorías de noticias, que permiten integrar varias instancias del canal de noticias en una aplicación."
tool: Dashboard
channel: news feed
hidden: true

---

# Categorías de noticias

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

> Las categorías de noticias permiten integrar varias instancias de noticias en su aplicación. Es posible integrar feeds dentro de diferentes ventanas que sólo muestren tarjetas de News Feed de una determinada categoría.

![¡El panel de noticias con una vista previa de tarjeta de imagen subtitulada para una noticia titulada "Sweet Teeth - Buy candy in bulk!" con el mensaje "¡Satisface tu antojo de dulces y pásate por nuestra tienda! Menciona este anuncio y consigue un 50 % de descuento en tu primera bolsa de caramelos". Hay cuatro casillas de verificación de categorías de noticias: Noticias, Anuncios, Publicidad y Social. No se selecciona ninguna de las categorías.][1]

Marcar una fuente de noticias como perteneciente a una categoría específica no es visible para el usuario final. Por defecto, la fuente de noticias Braze mostrará tarjetas de todas las categorías, a menos que una fuente esté configurada específicamente en el código de la aplicación para mostrar categorías específicas. Para más información sobre la configuración del código de la aplicación, consulta [Definir una categoría de canal de noticias][2].

[1]: {% image_buster /assets/img_archive/Newsfeed_category.png %}
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/news_feed/defining_a_news_feed_category/
