---
nav_title: Estilo personalizado
article_title: Estilo personalizado de la fuente de noticias para iOS
platform: iOS
page_order: 0
description: "Este artículo de referencia explica cómo implementar un estilo personalizado en la fuente de noticias y sustituir las imágenes predeterminadas en tu aplicación iOS."
channel:
  - news feed

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Estilo personalizado

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

La integración de `SDWebImage` es necesaria si planeas utilizar nuestra interfaz de usuario Braze para mostrar imágenes dentro de los mensajes dentro de la aplicación, la fuente de noticias o las tarjetas de contenido de iOS.

## Sustitución de imágenes predeterminadas

Braze permite a los clientes sustituir las imágenes predeterminadas existentes por sus propias imágenes personalizadas. Para ello, crea un nuevo archivo `png` con la imagen personalizada y añádelo al paquete de imágenes de la aplicación. A continuación, renombra el archivo con el nombre de la imagen para anular la imagen predeterminada en nuestra biblioteca. Además, asegúrate de subir las versiones `@2x` y `@3x` de las imágenes para adaptarlas a los distintos tamaños de teléfono. Las imágenes disponibles para anular en las tarjetas de contenido incluyen: Las imágenes disponibles para una sustitución en el canal de noticias incluyen lo siguiente:

* Indicador de icono de lectura: `Icons_Read`
* Imagen del marcador de posición: `img-noimage-lrg`

{% alert important %}
La sustitución de imágenes predeterminadas no se admite actualmente en nuestra integración con iOS de Xamarin.
{% endalert %}

