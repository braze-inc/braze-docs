---
nav_title: Estilo personalizado
article_title: Fuente de noticias con estilo personalizado para Web
platform: Web
page_order: 0
page_type: reference
description: "Este artículo trata de las opciones de estilo personalizado de las fuentes de noticias para tu aplicación Web."
channel: news feed

---

# Estilo personalizado

> Este artículo trata de las opciones de estilo personalizado de las fuentes de noticias para tu aplicación Web.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Los elementos de la interfaz de usuario Braze vienen con un aspecto predeterminado que coincide con los compositores del panel Braze y busca la coherencia con otras plataformas móviles Braze. Los estilos predeterminados en Braze se definen en CSS dentro del SDK de Braze. Anulando los estilos seleccionados en tu aplicación, es posible personalizar nuestra fuente estándar con tus propias imágenes de fondo, familias de fuentes, estilos, tamaños, animaciones y mucho más.

Por ejemplo, el siguiente es un ejemplo de modificación que hará que la fuente de noticias aparezca con un ancho de 800 px:

``` css
body .ab-feed {
  width: 800px;
}
```