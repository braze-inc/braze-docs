{% multi_lang_include archive/web-v4-rename.md %}

## Requisitos previos

Antes de poder utilizar las Tarjetas de contenido, tendrás que [integrar el SDK Web de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) en tu aplicación. Sin embargo, no es necesaria ninguna configuración adicional. Para crear tu propia interfaz de usuario, consulta la [Guía de personalización de tarjetas de contenido]({{site.baseurl}}/developer_guide/content_cards/).

## IU estándar de la fuente

Para utilizar la interfaz de usuario de las Tarjetas de contenido incluida, tendrás que especificar dónde mostrar la fuente en tu sitio web. 

En este ejemplo, tenemos un `<div id="feed"></div>` en el que queremos colocar la fuente de Content Cards. Utilizaremos tres botones para ocultar, mostrar o alternar (ocultar o mostrar en función de su estado actual) la fuente.

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

Al utilizar los métodos `toggleContentCards(parentNode, filterFunction)` y `showContentCards(parentNode, filterFunction)`, si no se proporcionan argumentos, todas las Content Cards se mostrarán en una barra lateral de posición fija en la parte derecha de la página. De lo contrario, la fuente se colocará en la opción `parentNode` especificada.

|Parámetros | Descripción |
|---|---|
|`parentNode` | El nodo HTML en el que se renderizarán las Content Cards. Si el nodo padre ya tiene una vista de Content Cards de Braze como descendiente directo, se sustituirán las Content Cards existentes. Por ejemplo, debes pasar `document.querySelector(".my-container")`.|
|`filterFunction` | Una función para filtrar u ordenar las tarjetas mostradas en esta vista. Se invoca con la matriz de objetos `Card`, ordenados por `{pinned, date}`. Se espera que devuelva una matriz de objetos `Card` ordenados para renderizar para este usuario. Si se omite, se mostrarán todas las tarjetas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

[Consulta la documentación de referencia del SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards) para obtener más información sobre cómo alternar las Content Cards.

## Probar Content Cards en la web

Puedes probar tu integración de Content Cards utilizando las herramientas de desarrollador de tu navegador.

1. Crea una campaña de tarjeta de contenido y dirígela a tu usuario de prueba.
2. Inicia sesión en el sitio web que tiene tu integración del SDK Web.
3. Abre la consola de tu navegador. En Chrome, haz clic derecho en la página, selecciona **Inspeccionar** y luego selecciona la pestaña **Consola**.
4. Ejecuta estos comandos en la consola:
   - `window.braze.getCachedContentCards()`
   - `window.braze.toggleContentCards()`

## Tipos de tarjeta y propiedades

El modelo de datos de las Content Cards está disponible en el SDK Web y ofrece los siguientes tipos de tarjetas de contenido: [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html), [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html) y [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html). Cada tipo hereda propiedades comunes de un modelo base [Card](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html) y tiene las siguientes propiedades adicionales.

{% alert tip %}
Para registrar los datos de las Content Cards, consulta [Registrar análisis]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/).
{% endalert %}

### Modelo de tarjeta base

Todas las Content Cards tienen estas propiedades compartidas:

|Propiedad|Descripción|
|---|---|
| `expiresAt` | La marca de tiempo UNIX de la fecha de caducidad de la tarjeta.|
| `extras`| (Opcional) Datos de par clave-valor formateados como un objeto de cadena con una cadena de valor. |
| `id` | (Opcional) El ID de la tarjeta. Esto se comunicará a Braze con eventos para fines de análisis. |
| `pinned` | Esta propiedad refleja si la tarjeta se configuró como "anclada" en el dashboard.|
| `updated` | La marca de tiempo UNIX de la última vez que se modificó esta tarjeta. |
| `viewed` | Esta propiedad refleja si el usuario ha visto la tarjeta o no.|
| `isControl` | Esta propiedad es `true` cuando una tarjeta es un grupo de "control" dentro de una prueba A/B.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Solo imagen

Las tarjetas [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html) son imágenes a tamaño completo en las que se puede hacer clic.

|Propiedad|Descripción|
|---|---|
| `aspectRatio` | La relación de aspecto de la imagen de la tarjeta; sirve como referencia antes de que se complete la carga de la imagen. Ten en cuenta que la propiedad puede no estar disponible en determinadas circunstancias. |
| `categories` | Esta propiedad es puramente para la organización en tu implementación personalizada; estas categorías se pueden establecer en el compositor del dashboard. |
| `clicked` | Esta propiedad indica si alguna vez se ha hecho clic en esta tarjeta en este dispositivo. |
| `created` | La marca de tiempo UNIX de la hora de creación de la tarjeta desde Braze. |
| `dismissed` | Esta propiedad indica si esta tarjeta ha sido descartada. |
| `dismissible` | Esta propiedad refleja si el usuario puede descartar la tarjeta, retirándola de la vista. |
| `imageUrl` | La URL de la imagen de la tarjeta.|
| `linkText` | El texto para mostrar de la URL. |
| `url` | La URL que se abrirá al hacer clic en la tarjeta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Imagen subtitulada

Las tarjetas [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html) son imágenes de tamaño completo en las que se puede hacer clic y que van acompañadas de un texto descriptivo.

|Propiedad|Descripción|
|---|---|
| `aspectRatio` | La relación de aspecto de la imagen de la tarjeta; sirve como referencia antes de que se complete la carga de la imagen. Ten en cuenta que la propiedad puede no estar disponible en determinadas circunstancias. |
| `categories` | Esta propiedad es puramente para la organización en tu implementación personalizada; estas categorías se pueden establecer en el compositor del dashboard. |
| `clicked` | Esta propiedad indica si alguna vez se ha hecho clic en esta tarjeta en este dispositivo. |
| `created` | La marca de tiempo UNIX de la hora de creación de la tarjeta desde Braze. |
| `dismissed` | Esta propiedad indica si esta tarjeta ha sido descartada. |
| `dismissible` | Esta propiedad refleja si el usuario puede descartar la tarjeta, retirándola de la vista. |
| `imageUrl` | La URL de la imagen de la tarjeta.|
| `linkText` | El texto para mostrar de la URL. |
| `title` | El texto del título de esta tarjeta. |
| `url` | La URL que se abrirá al hacer clic en la tarjeta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Clásica

El modelo [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html) puede contener una imagen sin texto o un texto con imagen.

|Propiedad|Descripción|
|---|---|
| `aspectRatio` | La relación de aspecto de la imagen de la tarjeta; sirve como referencia antes de que se complete la carga de la imagen. Ten en cuenta que la propiedad puede no estar disponible en determinadas circunstancias. |
| `categories` | Esta propiedad es puramente para la organización en tu implementación personalizada; estas categorías se pueden establecer en el compositor del dashboard. |
| `clicked` | Esta propiedad indica si alguna vez se ha hecho clic en esta tarjeta en este dispositivo. |
| `created` | La marca de tiempo UNIX de la hora de creación de la tarjeta desde Braze. |
| `description` | El texto del cuerpo de esta tarjeta. |
| `dismissed` | Esta propiedad indica si esta tarjeta ha sido descartada. |
| `dismissible` | Esta propiedad refleja si el usuario puede descartar la tarjeta, retirándola de la vista. |
| `imageUrl` | La URL de la imagen de la tarjeta.|
| `linkText` | El texto para mostrar de la URL. |
| `title` | El texto del título de esta tarjeta. |
| `url` | La URL que se abrirá al hacer clic en la tarjeta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Grupo de control

Si utilizas la fuente predeterminada de Content Cards, las impresiones y los clics se rastrearán automáticamente.

Si utilizas una integración personalizada para Content Cards, necesitas [registrar las impresiones]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) cuando se hubiera visto una tarjeta de control. Como parte de este esfuerzo, asegúrate de gestionar las tarjetas de control al registrar las impresiones en una prueba A/B. Estas tarjetas están en blanco y, aunque no las vean los usuarios, debes registrar las impresiones para comparar su rendimiento con el de las tarjetas que no son de control.

Para determinar si una tarjeta de contenido está en el grupo de control de una prueba A/B, comprueba la propiedad `card.isControl` (Web SDK v4.5.0+) o comprueba si la tarjeta es una instancia de `ControlCard` (`card instanceof braze.ControlCard`).

## Métodos de tarjeta

### Métodos de fuente predeterminada

Usa estos métodos cuando muestres Content Cards utilizando la interfaz de usuario predeterminada de Braze:

|Método | Descripción |
|---|---|
|[`showContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards)| Muestra la fuente predeterminada de Content Cards. Renderiza las tarjetas en un elemento HTML `parentNode` proporcionado, o como una barra lateral de posición fija en el lado derecho de la página si no se proporciona ningún elemento. Acepta una `filterFunction` opcional para ordenar o filtrar las tarjetas antes de mostrarlas. |
|[`hideContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#hidecontentcards)| Oculta la fuente predeterminada de Content Cards si se está mostrando actualmente. |
|[`toggleContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards)| Muestra la fuente predeterminada de Content Cards si está oculta, o la oculta si está visible. Si necesitas mostrar varias fuentes de Content Cards simultáneamente, usa `showContentCards` y `hideContentCards` en su lugar. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Métodos de fuente personalizada

Usa estos métodos cuando construyas tu propia interfaz de usuario de Content Cards:

|Método | Descripción |
|---|---|
|[`subscribeToContentCardsUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetocontentcardsupdates)| Registra una función de devolución de llamada que se invoca cada vez que se actualizan las Content Cards para el usuario actual, como al inicio de sesión. Usa esto como la forma principal de recibir datos de tarjetas para tu fuente personalizada. Debe llamarse antes de `openSession()` para recibir actualizaciones en la sesión inicial. |
|[`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards)| Devuelve todas las tarjetas actualmente disponibles de la última actualización de Content Cards. Usa esto para mostrar tarjetas inmediatamente al cargar la página sin esperar una nueva solicitud al servidor, como cuando el usuario vuelve a una página durante una sesión activa. |
|[`requestContentCardsRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh)| Solicita una actualización inmediata de Content Cards desde los servidores de Braze. De forma predeterminada, las tarjetas se actualizan al inicio de sesión y cuando se reabre la fuente predeterminada. Usa esto para forzar una actualización en otros momentos, como después de una acción específica del usuario. Ten en cuenta los [límites de velocidad]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed/#rate-limit). |
|[`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions)| Registra eventos de impresión para una matriz de tarjetas. Llama a esto cuando las tarjetas se renderizan y son visibles para el usuario. Es necesario para informes de campaña precisos cuando se usa una interfaz personalizada, ya que las impresiones no se rastrean automáticamente fuera de la fuente predeterminada. |
|[`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick)| Registra un evento de clic para una sola tarjeta. Llama a esto cuando un usuario interactúa con una tarjeta en tu interfaz personalizada. Es necesario para informes de campaña precisos, ya que los clics no se rastrean automáticamente fuera de la fuente predeterminada. |
|[`handleBrazeAction`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#handlebrazeaction)| Procesa la URL de una tarjeta y ejecuta la acción de clic configurada, incluyendo acciones de Braze (URLs `brazeActions://`) y navegación URL estándar. Llama a esto en tu controlador de clic de tarjeta para asegurar que los comportamientos de clic configurados en el dashboard de Braze se ejecuten. |
|[`dismissCard`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html#dismisscard)| Descarta una tarjeta programáticamente, eliminándola de la fuente del usuario. Usa esto para permitir que los usuarios descarten tarjetas en tu interfaz personalizada. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para más detalles, consulta la [documentación de referencia del SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html).

## Buenas prácticas

### Llama a los métodos en el orden correcto

Para fuentes personalizadas, las Content Cards solo se actualizan al inicio de sesión si `subscribeToContentCardsUpdates()` se llama antes de `openSession()`. Llama a tus métodos de Braze en este orden:

```javascript
import * as braze from "@braze/web-sdk";

// Step 1: Initialize the SDK
braze.initialize("YOUR-API-KEY", { baseUrl: "YOUR-SDK-ENDPOINT" });

// Step 2: Subscribe to card updates
braze.subscribeToContentCardsUpdates((updates) => {
  const cards = updates.cards;
  renderCards(cards);
});

// Step 3: Identify the user
braze.changeUser("USER_ID");

// Step 4: Start the session
braze.openSession();
```

### Usa tarjetas en caché para mantener el contenido entre cargas de página

Dado que `subscribeToContentCardsUpdates()` solo invoca su devolución de llamada cuando hay nuevas actualizaciones (como al inicio de sesión), las tarjetas pueden desaparecer de tu fuente personalizada si un usuario actualiza la página a mitad de sesión. Para evitar esto, usa `getCachedContentCards()` para renderizar tarjetas inmediatamente desde la caché local, junto con tu suscripción para nuevas actualizaciones:

```javascript
import * as braze from "@braze/web-sdk";

function renderCards(cards) {
  const container = document.getElementById("content-cards");
  container.textContent = "";
  const displayedCards = [];

  cards.forEach(card => {
    if (card instanceof braze.ClassicCard || card instanceof braze.CaptionedImage) {
      const cardElement = document.createElement("div");

      const h3 = document.createElement("h3");
      h3.textContent = card.title || "";
      cardElement.appendChild(h3);

      const p = document.createElement("p");
      p.textContent = card.description || "";
      cardElement.appendChild(p);

      if (card.imageUrl) {
        const img = document.createElement("img");
        img.src = card.imageUrl;
        img.alt = card.title || "";
        cardElement.appendChild(img);
      }

      if (card.url) {
        cardElement.addEventListener("click", () => {
          braze.logContentCardClick(card);
          braze.handleBrazeAction(card.url);
        });
      }

      container.appendChild(cardElement);
      displayedCards.push(card);
    }
  });

  if (displayedCards.length > 0) {
    braze.logContentCardImpressions(displayedCards);
  }
}

// Display cached cards immediately
const cached = braze.getCachedContentCards();
if (cached && cached.cards.length > 0) {
  renderCards(cached.cards);
}

// Subscribe to future updates
braze.subscribeToContentCardsUpdates((updates) => {
  renderCards(updates.cards);
});
```

### Registra análisis para fuentes personalizadas

Cuando usas una interfaz personalizada, las impresiones, los clics y los descartes no se rastrean automáticamente. Debes registrar cada evento manualmente:

- **Impresiones:** Llama a `logContentCardImpressions([card1, card2, ...])` con una matriz de objetos de tarjeta cuando las tarjetas sean visibles para el usuario.
- **Clics:** Llama a `logContentCardClick(card)` cuando un usuario interactúe con una tarjeta.
- **Comportamiento de clic:** Llama a `handleBrazeAction(card.url)` para ejecutar la acción de clic configurada de la tarjeta (como navegar a una URL o registrar un evento personalizado).

{% alert warning %}
El argumento pasado a `logContentCardClick()` debe ser un objeto `Card` original de Braze. Si transformas o reconstruyes los datos de la tarjeta (por ejemplo, serializando y deserializando), los clics no se registran y verás el error: "card must be a Card object."
{% endalert %}

## Uso de Google Tag Manager

Google Tag Manager funciona inyectando la [CDN de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#install-cdn) (una versión de nuestro SDK Web) directamente en el código de tu sitio web, lo que significa que todos los métodos del SDK están disponibles igual que si hubieras integrado el SDK sin Google Tag Manager, excepto al implementar Content Cards.

### Configuración de las Content Cards

{% tabs local %}
{% tab google tag manager %}
Para una integración estándar de la fuente de Content Cards, puedes utilizar una etiqueta **HTML personalizada** en Google Tag Manager. Añade lo siguiente a tu etiqueta HTML personalizada, que activará la fuente estándar de Content Cards:

```html
<script>
   window.braze.showContentCards();
</script>
```

![Configuración en Google Tag Manager de una etiqueta HTML personalizada que muestra la fuente de Content Cards.]({% image_buster /assets/img/web-gtm/gtm_content_cards.png %})
{% endtab %}

{% tab manual %}
Para tener más libertad a la hora de personalizar el aspecto de las Content Cards y su fuente, puedes integrar directamente las Content Cards en tu sitio web nativo. Puedes hacerlo de dos formas: utilizando la interfaz de usuario estándar o creando una interfaz de usuario personalizada.

{% subtabs local %}
{% subtab standard feed %}
Al implementar la [IU de fuente estándar]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/#standard-feed-ui), los métodos de Braze deben tener `window.` añadido al principio del método. Por ejemplo, `braze.showContentCards` debería ser `window.braze.showContentCards`.
{% endsubtab %}

{% subtab custom feed %}
Para el estilo [personalizado de la fuente]({{site.baseurl}}/developer_guide/content_cards/creating_cards/), los pasos son los mismos que si hubieras integrado el SDK sin GTM. Por ejemplo, si quieres personalizar la anchura de la fuente de Content Cards, puedes pegar lo siguiente en tu archivo CSS:

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

Para actualizar a la última versión del SDK Web de Braze, sigue los tres pasos siguientes en tu dashboard de Google Tag Manager:

1. **Actualizar plantilla de etiquetas**<br>Ve a la página **Plantillas** dentro de tu espacio de trabajo. Aquí deberías ver un icono que indica que hay una actualización disponible.<br><br>![Página de plantillas que muestra que hay una actualización disponible]({% image_buster /assets/img/web-gtm/gtm-update-available.png %})<br><br>Haz clic en ese icono y, tras revisar el cambio, haz clic en **Aceptar actualización**.<br><br>![Una pantalla comparando las plantillas de etiquetas antigua y nueva con un botón para "Aceptar actualización"]({% image_buster /assets/img/web-gtm/gtm-accept-update.png %})<br><br>
2. **Actualizar número de versión**<br>Una vez actualizada tu plantilla de etiquetas, edita la etiqueta de inicialización de Braze y actualiza la versión del SDK a la versión más reciente de `major.minor`. Por ejemplo, si la última versión es `4.1.2`, introduce `4.1`. Puedes ver una lista de las versiones del SDK en nuestro [registro de cambios](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md).<br><br>![Plantilla de inicialización de Braze con un campo de entrada para cambiar la versión del SDK]({% image_buster /assets/img/web-gtm/gtm-version-number.png %})<br><br>
3. **Control de calidad y publicación**<br>Comprueba que la nueva versión del SDK funciona utilizando la [herramienta de depuración](https://support.google.com/tagmanager/answer/6107056?hl=en) de Google Tag Manager antes de publicar una actualización en tu contenedor de etiquetas.

### Solución de problemas {#troubleshooting}

#### Habilitar la depuración de etiquetas {#debugging}

Cada plantilla de etiqueta de Braze tiene una casilla de verificación opcional **Depuración de etiquetas GTM** que puede utilizarse para registrar mensajes de depuración en la consola JavaScript de tu página web.

![Herramienta de depuración de Google Tag Manager]({% image_buster /assets/img/web-gtm/gtm-tag-debugging.png %})

#### Entrar en modo depuración

Otra forma de ayudar a depurar tu integración con Google Tag Manager es utilizar la característica de [modo de vista previa](https://support.google.com/tagmanager/answer/6107056) de Google.

Esto ayudará a identificar qué valores se envían desde la capa de datos de tu página web a cada etiqueta de Braze desencadenada y también explicará qué etiquetas se desencadenaron o no.

![La página de resumen de la etiqueta de inicialización de Braze proporciona un resumen de la etiqueta, incluyendo información sobre qué etiquetas se desencadenaron.]({% image_buster /assets/img/web-gtm/gtm-debug-mode.png %})

#### Verificar la secuencia de etiquetas para eventos personalizados {#tag-sequencing}

Si los eventos personalizados u otras acciones no se registran en Braze, una causa común es una condición de carrera en la que una etiqueta de acción (como **Evento personalizado** o **Compra**) se dispara antes de que la etiqueta de **inicialización de Braze** haya completado. Para solucionarlo, configura la [secuencia de etiquetas](https://support.google.com/tagmanager/answer/6238868) en GTM:

1. Abre la etiqueta de acción que no se está registrando correctamente.
2. En **Configuración avanzada** > **Secuencia de etiquetas**, selecciona **Una etiqueta que se dispara antes de \[esta etiqueta\]**.
3. Elige tu etiqueta de **inicialización de Braze** como la etiqueta de configuración.

Esto asegura que el SDK esté completamente inicializado antes de que cualquier etiqueta de acción intente enviar datos a Braze.

#### Habilitar el registro detallado

Para capturar registros detallados para la solución de problemas, puedes habilitar el registro detallado en tu integración con Google Tag Manager. Estos registros aparecerán en la pestaña **Consola** de las [herramientas de desarrollador](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools) de tu navegador.

En tu integración de Google Tag Manager, navega hasta tu etiqueta de inicialización de Braze y selecciona **Habilitar registro del SDK Web**.

![La página de resumen de la etiqueta de inicialización de Braze con la opción Habilitar registro del SDK Web activada.]({% image_buster /assets/img/web-gtm/gtm_verbose_logging.png %})

[changelog]: https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md