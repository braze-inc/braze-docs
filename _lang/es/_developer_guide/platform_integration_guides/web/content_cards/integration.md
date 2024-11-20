---
nav_title: Integración
article_title: Integración de tarjetas de contenido para Web
page_order: 0
platform: Web
channel: content cards
page_type: reference
description: "Este artículo trata de la integración de la tarjeta de contenido para la Web, incluidos los modelos de datos de la tarjeta de contenido, las opciones de interfaz de usuario de la fuente estándar y los métodos de tarjeta adicionales."
search_rank: 1
---

# Integración de la tarjeta de contenido

> Este artículo trata de la integración de la tarjeta de contenido para la Web, incluidos los modelos de datos de la tarjeta de contenido, las opciones de interfaz de usuario de la fuente estándar y los métodos de tarjeta adicionales.

{% multi_lang_include archive/web-v4-rename.md %}

El SDK de la Web de Braze incluye una interfaz de usuario de fuente de tarjetas de contenido para acelerar tus esfuerzos de integración. Si prefieres crear tu propia interfaz de usuario, consulta la [Guía de personalización de la tarjeta de contenido]({{site.baseurl}}/developer_guide/customization_guides/content_cards).

## IU estándar de la fuente

Para utilizar la interfaz de usuario de las tarjetas de contenido incluidas, tendrás que especificar dónde mostrar la fuente en tu sitio web. 

En este ejemplo, tenemos un `<div id="feed"></div>` en el que queremos colocar la fuente Tarjetas de contenido. Utilizaremos tres botones para ocultar, mostrar o alternar (ocultar o mostrar en función de su estado actual) la fuente.

```html

<button id="toggle" type="button">Toggle Cards Feed</button>
<button id="hide" type="button">Hide Cards Feed</button>
<button id="show" type="button">Show Cards Feed</button>

<nav>
    <h1>Your Personalized Feed</h1>
    <div id="feed"></div>
</nav>

<script> 
   const toggle = document.getElementById("toggle");
   const hide = document.getElementById("hide");
   const show = document.getElementById("show");
   const feed = document.getElementById("feed");
    
   toggle.onclick = function(){
      braze.toggleContentCards(feed);    
   }
    
   hide.onclick = function(){
      braze.hideContentCards();
   }
    
   show.onclick = function(){
      braze.showContentCards(feed);    
   }
</script>
```

Al utilizar los métodos `toggleContentCards(parentNode, filterFunction)` y `showContentCards(parentNode, filterFunction)`, si no se proporcionan argumentos, todas las tarjetas de contenido se mostrarán en una barra lateral de posición fija en la parte derecha de la página. De lo contrario, la fuente se colocará en la opción `parentNode` especificada.

|Parámetros | Descripción |
|---|---|
|`parentNode` | El nodo HTML en el que se convertirán las tarjetas de contenido. Si el nodo padre ya tiene una vista de Tarjetas de contenido Braze como descendiente directo, se sustituirán las Tarjetas de contenido existentes. Por ejemplo, debes introducir `document.querySelector(".my-container")`.|
|`filterFunction` | Una función para filtrar u ordenar las tarjetas mostradas en esta vista. Se invoca con la matriz de objetos `Card`, ordenados por `{pinned, date}`. Se espera que devuelva una matriz de objetos ordenados `Card` para renderizar para este usuario. Si se omite, se mostrarán todas las tarjetas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

[Consulta la documentación de referencia del SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards) para obtener más información sobre cómo alternar la tarjeta de contenido.

## Modelo de datos de la tarjeta de contenido {#data-models}

El modelo de datos de las tarjetas de contenido está disponible en el SDK Web.

El SDK para Web de Braze ofrece tres tipos de tarjetas de contenido: [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html), [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html) y [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html). Cada tipo hereda propiedades comunes de un modelo base [Tarjeta](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html) y tiene las siguientes propiedades adicionales.

Consulta [Análisis de]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics) tarjetas para obtener información sobre cómo suscribirte a los datos de las tarjetas.

### Propiedades del modelo de tarjeta de contenido base - Tarjeta

Todas las tarjetas de contenido tienen estas propiedades compartidas:

|Propiedad|Descripción|
|---|---|
| `expiresAt` | La fecha UNIX de caducidad de la tarjeta.|
| `extras`| (Opcional) Datos del par clave-valor formateados como un objeto de cadena con una cadena de valor. |
| `id` | (Opcional) El ID de la tarjeta. Esto se comunicará a Braze con eventos para fines de análisis. |
| `pinned` | Esta propiedad refleja si la tarjeta se configuró como "anclada" en el panel.|
| `updated` | La marca de tiempo UNIX de la última vez que se modificó esta tarjeta. |
| `viewed` | Esta propiedad refleja si el usuario ha visto la tarjeta o no.|
| `isControl` | Esta propiedad es `true` cuando una tarjeta es un grupo de "control" dentro de una prueba A/B.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propiedades de la tarjeta de contenido sólo imagen - ImageOnly

Las tarjetas [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html) son imágenes a tamaño completo en las que se puede hacer clic.

|Propiedad|Descripción|
|---|---|
| `aspectRatio` | La relación de aspecto de la imagen de la tarjeta y sirve como pista antes de que se complete la carga de la imagen. Ten en cuenta que la propiedad puede no suministrarse en determinadas circunstancias. |
| `categories` | Esta propiedad es puramente para la organización en tu implementación personalizada; estas categorías se pueden establecer en el compositor del panel. |
| `clicked` | Esta propiedad indica si alguna vez se ha hecho clic en esta tarjeta en este dispositivo. |
| `created` | La marca de tiempo UNIX de la hora de creación de la tarjeta desde Braze. |
| `dismissed` | Esta propiedad indica si esta tarjeta ha sido descartada. |
| `dismissible` | Esta propiedad refleja si el usuario puede descartar la tarjeta, retirándola de la vista. |
| `imageUrl` | La URL de la imagen de la tarjeta.|
| `linkText` | El texto para mostrar la URL. |
| `url` | La URL que se abrirá al hacer clic en la tarjeta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propiedades de la tarjeta de contenido con imagen subtitulada - CaptionedImage

Las tarjetas de [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html) son imágenes de tamaño completo en las que se puede hacer clic y que van acompañadas de un texto descriptivo.

|Propiedad|Descripción|
|---|---|
| `aspectRatio` | La relación de aspecto de la imagen de la tarjeta y sirve como pista antes de que se complete la carga de la imagen. Ten en cuenta que la propiedad puede no suministrarse en determinadas circunstancias. |
| `categories` | Esta propiedad es puramente para la organización en tu implementación personalizada; estas categorías se pueden establecer en el compositor del panel. |
| `clicked` | Esta propiedad indica si alguna vez se ha hecho clic en esta tarjeta en este dispositivo. |
| `created` | La marca de tiempo UNIX de la hora de creación de la tarjeta desde Braze. |
| `dismissed` | Esta propiedad indica si esta tarjeta ha sido descartada. |
| `dismissible` | Esta propiedad refleja si el usuario puede descartar la tarjeta, retirándola de la vista. |
| `imageUrl` | La URL de la imagen de la tarjeta.|
| `linkText` | El texto para mostrar la URL. |
| `title` | El texto del título de esta tarjeta. |
| `url` | La URL que se abrirá al hacer clic en la tarjeta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propiedades de la tarjeta de contenido clásica - ClassicCard

El modelo [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html) puede contener una imagen sin texto o un texto con imagen.

|Propiedad|Descripción|
|---|---|
| `aspectRatio` | La relación de aspecto de la imagen de la tarjeta y sirve como pista antes de que se complete la carga de la imagen. Ten en cuenta que la propiedad puede no suministrarse en determinadas circunstancias. |
| `categories` | Esta propiedad es puramente para la organización en tu implementación personalizada; estas categorías se pueden establecer en el compositor del panel. |
| `clicked` | Esta propiedad indica si alguna vez se ha hecho clic en esta tarjeta en este dispositivo. |
| `created` | La marca de tiempo UNIX de la hora de creación de la tarjeta desde Braze. |
| `description` | El texto del cuerpo de esta tarjeta. |
| `dismissed` | Esta propiedad indica si esta tarjeta ha sido descartada. |
| `dismissible` | Esta propiedad refleja si el usuario puede descartar la tarjeta, retirándola de la vista. |
| `imageUrl` | La URL de la imagen de la tarjeta.|
| `linkText` | El texto para mostrar la URL. |
| `title` | El texto del título de esta tarjeta. |
| `url` | La URL que se abrirá al hacer clic en la tarjeta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Grupo de control 

Si utilizas la fuente predeterminada de tarjetas de contenido, las impresiones y los clics se seguirán automáticamente.

Si utilizas una integración personalizada para tarjetas de contenido, necesitas [registrar las impresiones]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics/) cuando se hubiera visto una tarjeta de control. Como parte de este esfuerzo, asegúrate de gestionar las tarjetas de Control al registrar las impresiones en una prueba A/B. Estas tarjetas están en blanco y, aunque no las vean los usuarios, debes registrar las impresiones para comparar su rendimiento con el de las tarjetas que no son de Control.

Para determinar si una tarjeta de contenido está en el grupo de control para una prueba A/B, comprueba la propiedad `card.isControl` (Web SDK v4.5.0+) o comprueba si la tarjeta es una instancia de `ControlCard` (`card instanceof braze.ControlCard`).

## Métodos de tarjeta

|Método | Descripción |
|---|---|
|[`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions)| Registra un evento de impresión para la lista de tarjetas dada. Esto es necesario cuando se utiliza una IU personalizada y no la IU de Braze.|
|[`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick)| Registra un evento de clic para una tarjeta determinada. Esto es necesario cuando se utiliza una IU personalizada y no la IU de Braze.| 
|[`showContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards)| Muestra las tarjetas de contenido del usuario. |
|[`hideContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#hidecontentcards)| Ocultar las tarjetas de contenido Braze que se muestran actualmente. | 
|[`toggleContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards)| Muestra las tarjetas de contenido del usuario. | 
|[`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards)|Obtén todas las tarjetas actualmente disponibles desde la última actualización de las Tarjetas de Contenido.|
|[`subscribeToContentCardsUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetocontentcardsupdates)| Suscríbete a las actualizaciones de las tarjetas de contenido. <br> Se llamará a la devolución de llamada del suscriptor cada vez que se actualicen las tarjetas de contenido. | 
|[`dismissCard`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html#dismisscard)|Descarta la tarjeta mediante programación (disponible en v2.4.1).|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Para más detalles, consulta la [documentación de referencia del SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)

{% alert note %}
¿Listo para ir más lejos? Cuando entiendas los conceptos básicos de las tarjetas de contenido, consulta la [Guía de personalización de tarjetas de contenido]({{site.baseurl}}/developer_guide/customization_guides/content_cards) para empezar con la personalización.
{% endalert %}
