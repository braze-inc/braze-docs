# Indicadores no leídos y no leídos

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

> Braze te permite alternar opcionalmente los indicadores no leídos y leídos en las tarjetas de canal de noticias.

![Una tarjeta de fuente de noticias que muestra la imagen de un reloj junto con algo de texto. En la esquina superior del texto hay un triángulo azul o gris que indica si una tarjeta se ha leído o no. Un triángulo azul significa que se ha leído una tarjeta.]({% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %})

## Habilitación de los indicadores

Para habilitar esta funcionalidad, añade la siguiente línea a tu archivo `braze.xml`:

```xml
<bool name="com_braze_newsfeed_unread_visual_indicator_on">true</bool>
```

## Personalizar los indicadores

Estos indicadores pueden personalizarse modificando los dibujables `icon_read` y `icon_unread`.

