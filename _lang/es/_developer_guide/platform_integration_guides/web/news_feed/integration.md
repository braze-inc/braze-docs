---
nav_title: Integración
article_title: Integración de fuentes de noticias para Web
platform: Web
page_order: 0
page_type: reference
description: "Este artículo trata del tipo de tarjeta de fuente de noticias y de cómo integrar la fuente de noticias en tu aplicación Web a través del SDK de Braze."
channel: news feed

---

# Integración de la fuente de noticias

> Este artículo explica cómo configurar la fuente de noticias para el SDK Web de Braze.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

El Canal de noticias es una fuente de contenido totalmente personalizable dentro de la aplicación para tus usuarios. Nuestra orientación y segmentación te permiten crear un flujo de contenido adaptado individualmente a los intereses de cada usuario. Dependiendo de su posición en el ciclo de vida del usuario y de la naturaleza de tu aplicación, podría ser un servidor de contenidos de incorporación, un centro de anuncios, un centro de logros o un centro de noticias genérico.

## Ejemplo de fuente de noticias

<img src="{% image_buster /assets/img_archive/WebNewsFeed.png %}" alt="Un ejemplo de fuente de noticias que muestra varias notificaciones, como solicitudes de seguimiento, avisos de actualización, anuncios, etc." height="600" />

## Integración

Para alternar la visualización del canal de noticias a través del SDK Web de Braze, simplemente llama a:

``` javascript
braze.toggleFeed();
```

Esto mostrará las tarjetas de fuente de noticias almacenadas en caché más recientes (iniciando una actualización si estas tarjetas tienen más de 1 minuto de antigüedad, o si la fuente de noticias nunca se ha actualizado) y actualizará automáticamente la pantalla cuando se reciban nuevas tarjetas de los servidores Braze durante todo el tiempo que esté en pantalla.

Por predeterminado, la fuente se mostrará en una barra lateral de posición fija en el lado derecho del sitio web (o como una superposición a pantalla completa en dispositivos móviles, mediante CSS receptivo). Si deseas anular este comportamiento y mostrar una Fuente de noticias posicionada estáticamente dentro de tu propio elemento padre, proporciona el siguiente elemento como primer argumento a `showFeed`:

``` javascript
braze.toggleFeed(document.getElementById('my-news-feed-parent'));
```

Si deseas mostrar un conjunto estático específico de tarjetas de canal de noticias, filtrar las tarjetas del servidor o proporcionar tu propia semántica de actualización, puedes desactivar la actualización automática y proporcionar tus propias tarjetas:

``` javascript
braze.subscribeToFeedUpdates(function(feed) {
  var cards = feed.cards;
  braze.showFeed(undefined, cards);
});
braze.requestFeedRefresh();
```

Consulta [los JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showfeed) para obtener documentación completa sobre `showFeed`, `destroyFeed`, y `toggleFeed`.

## Tipos de tarjeta

El SDK para Web de Braze admite 3 tipos únicos de tarjeta de canal de noticias, [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html), [Banner](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html), [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html), que comparten un modelo base, [Card](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html).

### Solicitar recuento de tarjetas no leídas

Puedes solicitar el número de tarjetas no leídas en cualquier momento llamando por teléfono:

``` javascript
braze.getCachedFeed().getUnreadCardCount();
```

Suele utilizarse para activar señales que indican cuántas tarjetas de canal de noticias hay sin leer. Consulta [los Documentos de referencia JS](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.feed.html) para obtener más información. Ten en cuenta que Braze no actualizará las tarjetas de canal de noticias al cargar una nueva página (y, por tanto, esta función devolverá 0) hasta que muestres la fuente o llames a `braze.requestFeedRefresh();`

### Pares clave-valor

Los objetos `Card` pueden llevar opcionalmente pares clave-valor como `extras`. Se pueden utilizar para enviar datos hacia abajo junto con una tarjeta para su posterior manipulación por la aplicación. Sólo tienes que llamar a `card.extras` para acceder a estos valores.

## Personalización

Los elementos de la interfaz de usuario Braze vienen con un aspecto predeterminado que coincide con los compositores del panel Braze y busca la coherencia con otras plataformas móviles Braze. Los estilos predeterminados en Braze se definen en CSS dentro del SDK de Braze. Anulando los estilos seleccionados en tu aplicación, es posible personalizar nuestra fuente estándar con tus propias imágenes de fondo, familias de fuentes, estilos, tamaños, animaciones y mucho más.

Por ejemplo, el siguiente es un ejemplo de modificación que hará que la fuente de noticias aparezca con un ancho de 800 px:

``` css
body .ab-feed {
  width: 800px;
}
```

## Categorías

Las instancias de la fuente de noticias Braze pueden configurarse para que sólo reciban tarjetas de una determinada "categoría". Esto permite la integración efectiva de múltiples flujos de fuentes de noticias dentro de una única aplicación.

Las categorías del canal de noticias pueden definirse proporcionando el tercer parámetro `allowedCategories` a `toggleFeed`:

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.NEWS]);
```

También puedes rellenar una fuente con una combinación de categorías como en el siguiente ejemplo:

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.ANNOUNCEMENTS, braze.Card.Category.NEWS]);
```

## Indicadores no leídos y no leídos

Braze proporciona un indicador de leído y no leído en las tarjetas de canal de noticias, como se muestra a continuación:

![Una tarjeta de fuente de noticias que muestra la imagen de un reloj junto con algo de texto. En la esquina superior derecha del texto hay un triángulo azul o gris que indica si una tarjeta se ha leído o no. Un triángulo azul significa que se ha leído una tarjeta.]({% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %})

### Desactivar los indicadores

Para desactivar esta funcionalidad, añade el siguiente estilo a tu CSS:

``` css
.ab-read-dot { display: none; }
.ab-read-indicator { display: none; }
```

