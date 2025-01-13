---
nav_title: Crear un elemento de noticias
article_title: Crear un elemento de noticias
page_order: 3
page_type: reference
description: "Este artículo de referencia explica cómo crear un elemento de noticias. Los elementos de noticias le permiten insertar contenido permanente directamente en su aplicación desde nuestro panel web."
channel: news feed
hidden: true


---

# Crear un elemento del canal de noticias

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

> Los elementos de noticias le permiten insertar contenido permanente directamente en su aplicación desde nuestro panel web. Y lo que es mejor, las noticias también se pueden dirigir a segmentos individuales, al igual que los demás tipos de mensajes. Esto significa que lo que usted ve en el feed puede ser completamente diferente de lo que ve otra persona. Las posibilidades del canal de noticias son casi ilimitadas.

Consulte nuestros [casos prácticos][13], [casos de uso][15], y [mejores prácticas][16] para ver ejemplos y consejos útiles para News Feeds.

## Paso 1: Haga clic en crear tarjeta

En primer lugar, debes elegir el tipo de elemento del canal de noticias que quieres enviar a tus usuarios. En el menú desplegable, puede seleccionar cualquiera de nuestros cuatro tipos de tarjetas de noticias.

![El botón Crear tarjeta en el panel de Braze. Las opciones desplegables ampliadas para crear una tarjeta: Clásico, Imagen subtitulada y Banner.][1]

### Especificaciones de la tarjeta de noticias

#### Tarjetas de noticias

<br>![Una vista previa de la tarjeta clásica con el ícono de Facebook, un encabezado que dice "¡Dale a Me gusta en Facebook!" con dos líneas de texto: "¡Haga clic aquí!" y "www.facebook.com".][2]{: style="max-width:40%;"}

Las tarjetas de noticias estándar consisten en:

- Imagen 110x110
- Título
- Cuerpo del texto
- Enlace (dentro de la aplicación/web)

#### Tarjetas con imágenes subtituladas

<br>![Una vista previa de tarjeta de imagen subtitulada con una imagen de una tarta de manzana y manzanas. Debajo de la foto hay un encabezado que dice "¡Rebajas navideñas! Ahorra casi 50 dólares" con el siguiente texto: "Sólo por tiempo limitado, consigue 4 tartas de manzana premium por el precio de 3. ¡Date prisa! Esta oferta se terminará pronto". Haga clic aquí para canjear. www.example.com".][3]{: style="max-width:40%;"}

Las tarjetas de imagen con subtítulos constan de:

- Imagen 600x450
- Título
- Cuerpo del texto
- Enlace (dentro de la aplicación/web)

#### Tarjetas banner

<br>![Vista previa de una tarjeta de banner con una imagen que dice "Esto es un banner".][4]{: style="max-width:40%;"}

Las tarjetas banner incluyen:

- Imagen 600x100
- Enlace (dentro de la aplicación/web)

#### Directrices de imagen

|          Tipo de tarjeta         |          Relación de aspecto         | Tamaño de imagen recomendado | Tamaño máximo de imagen |   Tipos de archivo  |
|:-----------------------------:|:----------------------:|:------------------:|:-------------:|
|          Clásica         | 1:1 (110 píxeles de ancho mínimo) |          500 KB         |         1 MB        | PNG, JPEG, GIF |
|          Imagen subtitulada         | 4:3 (600 píxeles de ancho mínimo) |          500 KB         |         1 MB        | PNG, JPEG, GIF |
|          Banner         | 6:1 (600 píxeles de ancho mínimo) |          500 KB         |         1 MB        | PNG, JPEG, GIF |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

- Se recomiendan los archivos PNG.
- Se necesita una biblioteca de carga de imágenes personalizada para mostrar GIFs en Android. Recomendamos Glide.
- Las imágenes más pequeñas y de alta calidad se cargarán más rápido, por lo que se recomienda utilizar el activo más pequeño posible para lograr el resultado deseado.

## Paso 2: Añade un título, un resumen, una imagen y enlaces

¡Es hora de componer tu tarjeta de canal de noticias! Crea un título y un resumen para tu tarjeta y sube una imagen para acompañarla. También puede configurar el comportamiento de los enlaces en esta página. Este enlace puede ser un enlace estándar o un [enlace profundo][7] al contenido de la aplicación.

![Editor de elementos del canal de noticias que muestra el nombre de la tarjeta, la vista previa de la tarjeta y los detalles de personalización del idioma.][6]

## Paso 3: Selecciona un horario

En el editor de la tarjeta de noticias, encontrará opciones sobre cuándo publicar este elemento. Puede elegir publicarlo inmediatamente después de crearlo o fijar una hora en el futuro para publicarlo. También puede elegir entregar la tarjeta de noticias a una hora determinada en la hora local de sus usuarios seleccionando la casilla **Publicar a usuarios en su zona horaria local**.

![][8]

## Paso 4: Seleccione un segmento

Puede configurar su tarjeta de noticias para que se dirija a cualquier [segmento][10] que haya definido en el panel de control en el horario que desee. Seleccione su segmento objetivo haciendo clic en el menú desplegable. Aquí puede ver estadísticas de alto nivel, incluida la disponibilidad de correo electrónico y el valor de vida por usuario.

![][11]

## Paso 5: Revisar detalles y publicar

A continuación, accederá a una página en la que se muestran todos los detalles de su tarjeta (y el mensaje de acompañamiento de la aplicación, si procede). Puede revisar cualquiera de los detalles sobre estos elementos y editarlos si lo necesita haciendo clic en el icono del lápiz en cualquiera de los encabezados.

![][12]

Eso es todo. ¡Listo! Has publicado tu primera tarjeta de noticias.

## Opcional: Vincular una tarjeta de noticias a un mensaje de la aplicación

Las campañas multicanal suelen generar mejores tasas de conversión y participación, por lo que Braze ha facilitado la vinculación de un mensaje integrado en la aplicación a una tarjeta de noticias específica. 

Después de lanzar una tarjeta de noticias, aparecerá un botón en la nueva página de estadísticas de noticias que te permitirá "crear un mensaje asociado en la aplicación". Al hacer clic en esta opción, accederá al compositor de campañas para una nueva campaña de mensajes in-app. Mientras tú introduces el texto, el aspecto y el estilo del mensaje de la aplicación, Braze copia automáticamente las reglas de entrega y segmentación de la tarjeta de noticias asociada para asegurarse de que las campañas se lanzan juntas.

## Organizar tu canal de noticias

Puedes reordenar tus tarjetas dentro de la página de noticias.
- Las tarjetas del feed se ordenan primero en función de si han sido vistas o no por el usuario, los elementos no vistos aparecen en la parte superior del feed.
  - Una tarjeta se considera leída si ha recibido una impresión en el feed.
  - Las impresiones sólo se contabilizan si la tarjeta se puede ver en el feed (es decir, si un usuario no se desplaza hacia abajo para leer una tarjeta, no se contabiliza una impresión).
- Las tarjetas se ordenan por fecha y hora de creación, y las más recientes aparecen en primer lugar.

[1]: {% image_buster /assets/img_archive/newsfeed1_new.png %}
[2]: {% image_buster /assets/img_archive/classiccard.png %}
[3]: {% image_buster /assets/img_archive/captionedimage.png %}
[4]: {% image_buster /assets/img_archive/newsfeedbanner.png %}
[6]: {% image_buster /assets/img_archive/news-feed-title-summary_new.png %}
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/
[8]: {% image_buster /assets/img_archive/newsfeed2_new.png %}
[10]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[11]: {% image_buster /assets/img_archive/targetsegment_new.png %}
[12]: {% image_buster /assets/img_archive/newsfeedpreview_new.png %}
[13]: https://www.braze.com/customers
[14]: {% image_buster /assets/img_archive/linked-in-app_new.png %}
[15]: {{site.baseurl}}/user_guide/engagement_tools/news_feed/news_feed_use_cases/
[16]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/
