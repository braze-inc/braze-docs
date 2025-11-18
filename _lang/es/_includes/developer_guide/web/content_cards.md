{% multi_lang_include archive/web-v4-rename.md %}

## Requisitos previos

Antes de poder utilizar las tarjetas de contenido, tendrás que [integrar el SDK Braze Web]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) en tu aplicación. Sin embargo, no es necesaria ninguna configuración adicional. Para crear tu propia interfaz de usuario, consulta la [Guía de personalización de tarjetas de contenido]({{site.baseurl}}/developer_guide/content_cards/).

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

## Tipos de tarjeta y propiedades

El modelo de datos de las tarjetas de contenido está disponible en el SDK de la Web y ofrece los siguientes tipos de tarjetas de contenido: [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html), [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html) y [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html). Cada tipo hereda propiedades comunes de un modelo base [Tarjeta](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html) y tiene las siguientes propiedades adicionales.

{% alert tip %}
Para registrar los datos de la tarjeta de contenido, consulta [Registrar análisis]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/).
{% endalert %}

### Modelo de tarjeta base

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

### Solo imagen

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

### Imagen subtitulada

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

### Clásica

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

Si utilizas una integración personalizada para tarjetas de contenido, necesitas [registrar las impresiones]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) cuando se hubiera visto una tarjeta de control. Como parte de este esfuerzo, asegúrate de gestionar las tarjetas de Control al registrar las impresiones en una prueba A/B. Estas tarjetas están en blanco y, aunque no las vean los usuarios, debes registrar las impresiones para comparar su rendimiento con el de las tarjetas que no son de Control.

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

## Uso de Google Tag Manager

Google Tag Manager funciona inyectando la [CDN de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#install-cdn) (una versión de nuestro SDK Web) directamente en el código de tu sitio web, lo que significa que todos los métodos del SDK están disponibles igual que si hubieras integrado el SDK sin Google Tag Manager, excepto al implementar tarjetas de contenido.

### Configuración de las tarjetas de contenido

{% tabs local %}
{% tab Google Tag Manager %}
Para una integración estándar de la fuente de la tarjeta de contenido, puedes utilizar una etiqueta **HTML personalizada** en Google Tag Manager. Añade lo siguiente a tu etiqueta HTML personalizada, que activará la fuente estándar de la tarjeta de contenido:

```html
<script>
   window.braze.showContentCards();
</script>
```

![Configuración en Google Tag Manager de una etiqueta HTML personalizada que muestra la fuente de la tarjeta de contenido.]({% image_buster /assets/img/web-gtm/gtm_content_cards.png %})
{% endtab %}

{% tab manual %}
Para tener más libertad a la hora de personalizar el aspecto de las tarjetas de contenido y su fuente, puedes integrar directamente las tarjetas de contenido en tu sitio web nativo. Puedes hacerlo de dos formas: utilizando la interfaz de usuario estándar o creando una interfaz de usuario personalizada.

{% subtabs local %}
{% subtab standard feed %}
Al implementar la [IU de fuente estándar]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/#standard-feed-ui), los métodos de Braze deben tener `window.` añadido al principio del método. Por ejemplo, `braze.showContentCards` debería ser `window.braze.showContentCards`.
{% endsubtab %}

{% subtab custom feed %}
Para el estilo [personalizado de la fuente]({{site.baseurl}}/developer_guide/content_cards/creating_cards/), los pasos son los mismos que si hubieras integrado el SDK sin GTM. Por ejemplo, si quieres personalizar la anchura de la fuente de la tarjeta de contenido, puedes pegar lo siguiente en tu archivo CSS:

{% raw %}
```css
body .ab-feed { 
    width: 800px;
}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Actualización de plantillas {#upgrading}

Para actualizar a la última versión del SDK de la Web de Braze, sigue los tres pasos siguientes en tu panel de Google Tag Manager:

1. **Actualizar plantilla de etiquetas**<br>Ve a la página **Plantillas** dentro de tu espacio de trabajo. Aquí deberías ver un icono que indica que hay una actualización disponible.<br><br>![Página de plantillas que muestra que hay una actualización disponible]({% image_buster /assets/img/web-gtm/gtm-update-available.png %})<br><br>Haz clic en ese icono y, tras revisar el cambio, haz clic en **Aceptar actualización**.<br><br>![Una pantalla comparando las plantillas de etiquetas antigua y nueva con un botón para "Aceptar la actualización"]({% image_buster /assets/img/web-gtm/gtm-accept-update.png %})<br><br>
2. **Actualizar número de versión**<br>Una vez actualizada tu plantilla de etiquetas, edita la etiqueta de inicialización de Braze y actualiza la versión del SDK a la versión más reciente de `major.minor`. Por ejemplo, si la última versión es `4.1.2`, introduce `4.1`. Puedes ver una lista de las versiones del SDK en nuestro [registro de cambios](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md).<br><br>![Plantilla de inicialización de Braze con un campo de entrada para cambiar la versión del SDK]({% image_buster /assets/img/web-gtm/gtm-version-number.png %})<br><br>
3. **Control de calidad y publicación**<br>Comprueba que la nueva versión del SDK funciona utilizando la [herramienta de depuración](https://support.google.com/tagmanager/answer/6107056?hl=en) de Google Tag Manager antes de publicar una actualización en tu contenedor de etiquetas.

### Solución de problemas {#troubleshooting}

#### Habilitar la depuración de etiquetas {#debugging}

Cada plantilla de etiqueta Braze tiene una casilla de verificación opcional **Depuración de etiquetas GTM** que puede utilizarse para registrar mensajes de depuración en la consola JavaScript de tu página Web.

![Herramienta de depuración de Google Tag Manager]({% image_buster /assets/img/web-gtm/gtm-tag-debugging.png %})

#### Entrar en modo depuración

Otra forma de ayudar a depurar tu integración con Google Tag Manager es utilizar la característica de [modo de vista previa](https://support.google.com/tagmanager/answer/6107056) de Google.

Esto ayudará a identificar qué valores se envían desde la capa de datos de tu página Web a cada etiqueta Braze desencadenada y también explicará qué etiquetas se desencadenaron o no.

![La página de resumen de la etiqueta de inicialización Braze proporciona un resumen de la etiqueta, incluyendo información sobre qué etiquetas se desencadenaron.]({% image_buster /assets/img/web-gtm/gtm-debug-mode.png %})

#### Habilitar el registro detallado

Para permitir que el soporte técnico de Braze acceda a los registros durante las pruebas, puedes habilitar el registro detallado en tu integración con Google Tag Manager. Estos registros aparecerán en la pestaña **Consola** de las [herramientas del desarrollador](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools) de tu navegador.

En tu integración de Google Tag Manager, navega hasta tu etiqueta de inicialización de Braze y selecciona **Habilitar registro SDK Web**.

![La página de resumen de la etiqueta de inicialización de Braze con la opción de habilitar el registro del SDK Web activada.]({% image_buster /assets/img/web-gtm/gtm_verbose_logging.png %})

[changelog]: https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md
