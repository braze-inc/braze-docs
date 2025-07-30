---
nav_title: Mensajes HTML en la aplicación
article_title: Mensajes HTML personalizados en la aplicación
page_order: 0
page_type: reference
description: "En este artículo se ofrece una descripción general de los mensajes de código personalizado dentro de la aplicación, incluidos los métodos JavaScript, el seguimiento de botones y el uso de la vista previa HTML interactiva en Braze."
channel:
  - in-app messages
---

# Mensajes HTML personalizados en la aplicación {#custom-html-messages}

> Aunque nuestros mensajes estándar para aplicaciones se pueden personalizar de varias formas, puedes obtener un control aún mayor sobre el aspecto de tus campañas utilizando mensajes diseñados y creados con HTML, CSS y JavaScript. Con una simple composición, puedes desbloquear funcionalidades y marcas personalizadas que se ajusten a cualquiera de tus necesidades. 

Los mensajes HTML in-app permiten un mayor control sobre el aspecto de un mensaje, incluyendo lo siguiente:

- Fuentes y estilos personalizados
- Vídeos
- Varias imágenes
- Comportamientos al hacer clic
- Componentes interactivos
- Animaciones personalizadas

Los mensajes HTML personalizados pueden utilizar los métodos de [JavaScript Bridge](#javascript-bridge) para registrar eventos, establecer atributos personalizados, cerrar el mensaje y mucho más. Echa un vistazo a nuestro [repositorio de GitHub](https://github.com/braze-inc/in-app-message-templates), que contiene instrucciones detalladas sobre cómo utilizar y personalizar los mensajes HTML in-app para tus necesidades, y para un conjunto de plantillas de mensajes HTML5 in-app que te ayudarán a empezar.

{% alert note %}
Para habilitar los mensajes HTML dentro de la aplicación a través del SDK Web, debes proporcionar la opción de inicialización `allowUserSuppliedJavascript` a Braze, por ejemplo `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Esto es por razones de seguridad, ya que los mensajes dentro de la aplicación en HTML pueden ejecutar JavaScript, por lo que requerimos que un mantenedor del sitio los habilite.
{% endalert %}

## Puente JavaScript {#javascript-bridge}

Los mensajes HTML in-app para Web, Android, iOS y Swift SDK admiten un "puente" JavaScript para interactuar con Braze SDK, lo que le permite desencadenar acciones Braze personalizadas cuando los usuarios hacen clic en elementos con enlaces o interactúan de otro modo con su contenido. Estos métodos existen con la variable global `brazeBridge` o `appboyBridge`.

{% alert important %}
Braze recomienda utilizar la variable global `brazeBridge`. La variable global `appboyBridge` está obsoleta pero seguirá funcionando para los usuarios existentes. Si estás utilizando `appboyBridge`, te sugerimos que migres a `brazeBridge`. <br><br> `appboyBridge` quedó obsoleto en las siguientes versiones del SDK:
- Web: [3.3.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/web/changelog/#330)
- Android: [14.0.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog/#1400)
- iOS: [4.2.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog/#420)
{% endalert %}

Por ejemplo, para registrar un atributo personalizado y un evento personalizado y, a continuación, cerrar el mensaje, podría utilizar el siguiente JavaScript dentro de su mensaje HTML in-app:

```html
<button id="button">Set Favorite Color</button>
<script>
// Wait for the `brazeBridge` ready event, "ab.BridgeReady"
window.addEventListener("ab.BridgeReady", function(){
  // Event handler when the button is clicked
  document.querySelector("#button").onclick = function(){
    // Track Button 1 clicks for analytics
    // Note: This requires Android SDK v8.0.0, Web SDK v2.5.0, Swift SDK v5.4.0, and iOS SDK v3.23.0
    brazeBridge.logClick("0");
    // Set the user's custom attribute
    brazeBridge.getUser().setCustomUserAttribute("favorite color", "blue");
    // Track a custom event
    brazeBridge.logCustomEvent("completed survey");
    // Send the enqueued data to Braze
    brazeBridge.requestImmediateDataFlush();
    // Close this in-app message
    brazeBridge.closeMessage();
  };
}, false);
</script>
```

### Métodos puente de JavaScript {#bridge}

Los siguientes métodos de JavaScript son compatibles con los mensajes HTML dentro de la aplicación Braze:

<style>
/* Makes first column wider */
#article-main > table:first-of-type > tbody > tr td:first-child {
    min-width: 470px !important;
}
/* Makes code column smaller font */
#article-main > table:first-of-type > tbody > tr td:first-child code {
    font-size:12px !important;
}
#article-main > table:first-of-type td {
  word-break: break-word;
}
</style>

{% alert note %}
No puedes hacer referencia a Liquid para insertar <code>customAttributes</code> en métodos Bridge de JavaScript.
{% endalert %}

{% multi_lang_include archive/appboyBridge.md %}

## Acciones basadas en enlaces

Además de JavaScript personalizado, los SDK de Braze también pueden enviar datos de análisis con estos cómodos atajos de URL. Tenga en cuenta que estos parámetros de consulta y esquemas de URL distinguen entre mayúsculas y minúsculas.

### Seguimiento de clics en botones (obsoleto)

{% alert warning %}
El uso de `abButtonID` no es compatible con los tipos de mensaje [HTML con Vista previa]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/#html-upload-with-preview/). Para más información, consulta nuestra [guía de actualización]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/preview/#backward-incompatible-changes).
{% endalert %}

Para registrar los clics en los botones para el análisis de mensajes dentro de la aplicación, puede añadir `abButtonId` como parámetro de consulta a cualquier enlace profundo, URL de redirección o elemento de anclaje `<a>`. Utilice `?abButtonId=0` para registrar un clic en el "Botón 1" y `?abButtonId=1` para registrar un clic en el "Botón 2".

Al igual que con otros parámetros de URL, el primer parámetro debe comenzar con un signo de interrogación `?`, mientras que los siguientes deben ir separados por un ampersand `&`.

#### Ejemplos de URL

- `https://example.com/?abButtonId=0` - Botón 1 clic
- `https://example.com/?abButtonId=1` - Clic en el botón 2
- `https://example.com/?utm_source=braze&abButtonId=0` - Botón 1 clic con otros parámetros URL existentes
- `myApp://deep-link?page=home&abButtonId=1` - Vínculo profundo móvil con clic en el botón 2
- `<a href="https://example.com/?abButtonId=1">` - Elemento de anclaje `<a>` con clic en el botón 2

{% alert note %}
Los mensajes dentro de la aplicación sólo admiten pulsaciones del Botón 1 y del Botón 2. Las URL que no especifiquen uno de estos dos ID de botón se registrarán como "clics en el cuerpo" genéricos.
{% endalert %}

### Abrir enlace en una ventana nueva (sólo para móviles)

Para abrir enlaces fuera de su aplicación en una nueva ventana, configure `?abExternalOpen=true`. El mensaje se descartará antes de abrir el enlace.

Para la vinculación en profundidad, Braze abrirá tu URL independientemente del valor de `abExternalOpen`.

### Abrir como enlace profundo (sólo para móviles)

Para que Braze gestione tu enlace HTTP o HTTPS como un vínculo profundo, configura `?abDeepLink=true`.

Cuando este parámetro de cadena de consulta está ausente o establecido en `false`, Braze intentará abrir el enlace web en un navegador web interno dentro de la aplicación host.

### Cerrar mensaje in-app

Para cerrar un mensaje dentro de la aplicación, puedes utilizar el método javascript `brazeBridge.closeMessage()`.

Por ejemplo, `<a onclick="brazeBridge.closeMessage()" href="#">Close</a>` cerrará el mensaje in-app.

## Carga HTML con vista previa

Al crear mensajes HTML personalizados dentro de la aplicación, puedes previsualizar tu contenido interactivo directamente en Braze. 

El panel de vista previa de mensajes del editor muestra una vista previa realista que representa el JavaScript incluido en su mensaje. Puedes previsualizar e interactuar con tus mensajes personalizados desde el panel de previsualización haciendo clic en la paginación, enviando formularios o encuestas, viendo animaciones JavaScript, ¡y mucho más!

![Interactuar con la vista previa HTML deslizando el dedo por las páginas.]({% image_buster /assets/img/iam-beta-javascript-preview.gif %})

{% alert tip %}
Cualquier método JavaScript de `brazeBridge` que utilice en su HTML no actualizará los perfiles de los usuarios durante la vista previa en el panel de control.
{% endalert %}

### Requisitos del SDK {#supported-sdk-versions}

Para utilizar la vista previa HTML para mensajes dentro de la aplicación, debe actualizar a las siguientes versiones mínimas del SDK de Braze:

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

{% alert warning %}
Dado que este tipo de mensaje sólo puede ser recibido por determinadas versiones posteriores del SDK, los usuarios que se encuentren en versiones del SDK no compatibles no recibirán el mensaje. Considere la posibilidad de adoptar este tipo de mensaje después de que una parte significativa de su base de usuarios sea accesible, o diríjase sólo a aquellos usuarios cuya versión de la aplicación sea posterior a los requisitos. Más información sobre [el filtrado por la versión más reciente de la aplicación]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions).
{% endalert %}

### Crear una campaña {#instructions}

Al crear un mensaje de **código personalizado** dentro de la aplicación, elija **Carga HTML con vista previa** como tipo personalizado. Si no has creado previamente mensajes con código personalizado dentro de la aplicación (en directo o borradores), esta opción se aplica automáticamente y no tendrás que hacer ninguna selección.

![Creación de un mensaje dentro de la aplicación que se envía tanto a navegadores móviles como web donde "Tipo de mensaje" es Código personalizado y "Tipo personalizado" es Carga HTML con vista previa.]({% image_buster /assets/img/iam-beta-html-cross-channel.png %})

Tenga en cuenta que los usuarios de su aplicación móvil deben actualizarse a las versiones del SDK compatibles para recibir este mensaje. Le recomendamos que [anime a los usuarios a actualizar]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/) sus aplicaciones móviles antes de lanzar campañas que dependan de versiones más recientes del SDK de Braze.

#### Archivos de activos

Al crear mensajes in-app de código personalizado con carga HTML, puedes cargar activos de campaña a la [biblioteca multimedia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) para hacer referencia a ellos en tu mensaje.

Se pueden cargar los siguientes tipos de archivos:

| Tipo de archivo        | Extensión del archivo                    |
| :--------------- | :-------------------------------- |
| Archivos de fuentes       | `.ttf`, `.woff`, `.otf`, `.woff2` |
| Imágenes SVG       | `.svg`                            |
| Archivos JavaScript | `.js`                             |
| Archivos CSS        | `.css`                            |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Braze recomienda subir activos a la biblioteca multimedia por dos razones:

1. Los elementos añadidos a una campaña a través de la mediateca permiten que sus mensajes se muestren incluso cuando el usuario está desconectado o tiene una mala conexión a Internet.
2. Los activos cargados en Braze pueden reutilizarse en todas las campañas.

##### Añadir archivos de activos

Puede añadir activos nuevos o existentes a su campaña.

Para añadir nuevos activos a su campaña, utilice la sección de arrastrar y soltar para cargar un archivo. Los activos añadidos en esta sección también se añadirán automáticamente a la mediateca. Para añadir activos que ya hayas subido a la biblioteca multimedia, selecciona **Añadir desde biblioteca multimedia**.

Una vez añadidos sus activos, aparecerán en la sección **Activos para esta campaña**. 

Si el nombre de archivo de un activo coincide con el de un activo HTML local, se sustituirá automáticamente (por ejemplo, se carga `cat.png` y existe `<img src="cat.png" />` ). 

Si lo prefiere, pase el ratón por encima de un archivo de la lista y seleccione <i class="fas fa-copy"></i> **Copiar** para copiar la URL del archivo en el portapapeles. A continuación, pegue la URL del activo copiado en su HTML como haría normalmente al hacer referencia a un activo remoto.


### Editor HTML

Los cambios que realice en el HTML se mostrarán automáticamente en el panel de vista previa a medida que escriba. Cualquier método [JavaScript de`brazeBridge` ](#bridge) que utilice en su HTML no actualizará los perfiles de los usuarios durante la vista previa en el panel de control.

Puede configurar **los Ajustes del editor** para activar el texto envolvente, cambiar el tamaño de la fuente o elegir un tema de color. El editor de código incluye diferentes temas de color para resaltar la sintaxis, lo que te ayuda a detectar posibles errores de código directamente en el compositor de mensajes y a organizar mejor tu código (utilizando espacios o tabuladores, sea cual sea el lado de la discusión en el que te encuentres).

![Opciones de resaltado de sintaxis en el menú desplegable "Ajustes del editor" al redactar un mensaje HTML dentro de la aplicación.]({% image_buster /assets/img/iam-beta-html-syntax-highlighting.png %})

{% alert tip %}
Puedes pulsar <kbd>Ctrl</kbd> + <kbd>F</kbd> (Windows) o <kbd>Comando</kbd> + <kbd>F</kbd> (Mac) dentro del editor HTML para buscar dentro de tu código.
{% endalert %}

### Seguimiento de botones {#button-tracking-improvements}

Puedes hacer un seguimiento del rendimiento dentro de tu mensaje dentro de la aplicación de código personalizado utilizando el método [`brazeBridge.logClick(button_id)`]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/) JavaScript. Esto le permite realizar un seguimiento programático de "Botón 1", "Botón 2" y "Clics en el cuerpo" utilizando `brazeBridge.logClick("0")`, `brazeBridge.logClick("1")` o `brazeBridge.logClick()`, respectivamente.

| Clics     | Método                       |
| ---------- | ---------------------------- |
| Botón 1   | `brazeBridge.logClick("0")` |
| Botón 2   | `brazeBridge.logClick("1")` |
| Clic en el cuerpo | `brazeBridge.logClick()`    |
| Seguimiento de botones personalizados |`brazeBridge.logClick("your custom name here")`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Este método de seguimiento de botones sustituye a los anteriores métodos automáticos de seguimiento de clics (como `?abButtonId=0`), que han sido eliminados.
{% endalert %}

Puedes hacer un seguimiento de varios clics de botón por impresión. Por ejemplo, para cerrar un mensaje y registrar un clic en el Botón 2, puede utilizar lo siguiente:

```html
<a href="#" onclick="brazeBridge.logClick('1');brazeBridge.closeMessage()">✖</a>
``` 

También puede hacer un seguimiento de los nuevos nombres de botones personalizados (hasta 100 nombres únicos por campaña). Por ejemplo, `brazeBridge.logClick("blue button")` o `brazeBridge.logClick("viewed carousel page 3")`.

#### Limitaciones

- Puedes tener hasta 100 ID de botón únicos por campaña.
- Los identificadores de los botones pueden tener hasta 255 caracteres cada uno.
- Los identificadores de botón sólo pueden incluir letras, números, espacios, guiones y guiones bajos.

### Cambios incompatibles con versiones anteriores {#backward-incompatible-changes}

1. El cambio incompatible más notable con este nuevo tipo de mensaje son los requisitos del SDK. A los usuarios cuyo SDK de aplicación no cumpla los [requisitos mínimos de versión del SDK](#supported-sdk-versions) no se les mostrará el mensaje.
<br>

2. El vínculo profundo `braze://close`, que antes era compatible con las aplicaciones móviles, se ha eliminado en favor del `brazeBridge.closeMessage()` JavaScript. Esto permite mensajes HTML multiplataforma, ya que la Web no admite vínculos profundos.

3. Se han eliminado el seguimiento automático de clics, que utilizaba `?abButtonId=0` para los ID de los botones, y el seguimiento de "clics en el cuerpo" en los botones de cierre. Los siguientes ejemplos de código muestran cómo cambiar su HTML para utilizar nuestros nuevos métodos JavaScript de seguimiento de clics:

   | Antes de | Después de |
   |:-------- |:------------|
   |<code>&lt;a href="<mem_5ec17036-c4df-416f-abf4-95ce19ae0a52/>"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="brazeBridge.logClick();brazeBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
   |<code>&lt;a href="<mem_cebe8b80-ff43-4bf7-86fb-85db7a5a6c49/>"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="brazeBridge.logClick('0');brazeBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
   |<code>&lt;a href="<mem_4ac4bc1d-13d1-4e00-bcb7-2e59c6f3895c/>">Track button 1&lt;/a&gt;</code>|<code>&lt;a href="<mem_d1f733d1-360e-42d1-8e3d-fa71b847c1e8/>" onclick="brazeBridge.logClick('0')"&gt;Track button 1&lt;/a&gt;</code>|
   |<code>&lt;script&gt;<br>location.href = "<mem_90c1a625-7dad-4568-9672-2cdb067c9512/>"<br>&lt;/script&gt;</code>|<code>&lt;script&gt;<br>window.addEventListener("ab.BridgeReady", function(){<br>&nbsp;&nbsp;brazeBridge.logClick("1");<br>&nbsp;&nbsp;brazeBridge.closeMessage();<br>});<br>&lt;/script&gt;</code>|

