---
nav_title: Mensajes HTML dentro de la aplicación
article_title: Mensajes HTML personalizados dentro de la aplicación
page_order: 0
page_type: reference
description: "Este artículo proporciona un resumen de los mensajes dentro de la aplicación de código personalizado, incluidos los métodos JavaScript, el seguimiento de botones y el uso de la vista previa HTML interactiva en Braze."
channel:
  - in-app messages
---

# Mensajes HTML personalizados dentro de la aplicación {#custom-html-messages}

> Aunque nuestros mensajes dentro de la aplicación estándar pueden personalizarse de diversas formas, puedes obtener un control aún mayor sobre el aspecto y la sensación de tus campañas utilizando mensajes diseñados y creados con HTML, CSS y JavaScript. Con una simple composición, puedes desbloquear funcionalidades y marcas personalizadas que se ajusten a cualquiera de tus necesidades. 

Los mensajes dentro de la aplicación en HTML permiten un mayor control sobre el aspecto de un mensaje, incluyendo lo siguiente:

- Fuentes y estilos personalizados
- Videos
- Varias imágenes
- Comportamientos al hacer clic
- Componentes interactivos
- Animaciones personalizadas

Los mensajes HTML personalizados pueden utilizar los métodos de [JavaScript Bridge](#javascript-bridge) para registrar eventos, establecer atributos personalizados, cerrar el mensaje, ¡y mucho más! Consulta nuestro [repositorio de GitHub](https://github.com/braze-inc/in-app-message-templates), que contiene instrucciones detalladas sobre cómo utilizar y personalizar los mensajes HTML dentro de la aplicación según tus necesidades, y un conjunto de plantillas de mensajes HTML5 dentro de la aplicación que te ayudarán a empezar.

{% alert note %}
Para habilitar los mensajes HTML dentro de la aplicación a través del SDK Web, debes proporcionar la opción de inicialización `allowUserSuppliedJavascript` a Braze: por ejemplo `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Esto es por razones de seguridad, ya que los mensajes dentro de la aplicación en HTML pueden ejecutar JavaScript, por lo que requerimos que un mantenedor del sitio los habilite.
{% endalert %}

## Puente JavaScript {#javascript-bridge}

Los mensajes HTML dentro de la aplicación para Web, Android, iOS y SDK Swift admiten un "puente" JavaScript para interactuar con el SDK Braze, lo que te permite desencadenar acciones Braze personalizadas cuando los usuarios hacen clic en elementos con enlaces o interactúan de otro modo con tu contenido. Estos métodos existen con la variable global `brazeBridge` o `appboyBridge`.

{% alert important %}
Braze recomienda que utilices la variable global `brazeBridge`. La variable global `appboyBridge` está obsoleta, pero seguirá funcionando para los usuarios existentes. Si estás utilizando `appboyBridge`, te sugerimos que migres a `brazeBridge`. <br><br> `appboyBridge` quedó obsoleto en las siguientes versiones del SDK:
- Web: [3.3.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/web/changelog/#330)
- Android: [14.0.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog/#1400)
- iOS: [4.2.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog/#420)
{% endalert %}

Por ejemplo, para registrar un atributo personalizado y un evento personalizado, y luego cerrar el mensaje, podrías utilizar el siguiente JavaScript dentro de tu mensaje HTML dentro de la aplicación:

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

Además de JavaScript personalizado, los SDK de Braze también pueden enviar datos de análisis con estos cómodos atajos de URL. Nota que estos parámetros de consulta y esquemas de URL distinguen entre mayúsculas y minúsculas.

### Seguimiento de clics en botones (obsoleto)

{% alert warning %}
El uso de `abButtonID` no es compatible en [HTML con los]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/#html-upload-with-preview/) tipos de mensaje de [vista previa]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/#html-upload-with-preview/). Para más información, consulta nuestra [guía de actualización]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/preview/#backward-incompatible-changes).
{% endalert %}

Para registrar los clics en los botones para el análisis de mensajes dentro de la aplicación, puedes añadir `abButtonId` como parámetro de consulta a cualquier vínculo profundo, URL de redireccionamiento o elemento de anclaje `<a>`. Utiliza `?abButtonId=0` para registrar un clic en el "Botón 1", y `?abButtonId=1` para registrar un clic en el "Botón 2".

Al igual que con otros parámetros de URL, el primer parámetro debe comenzar con un signo de interrogación `?`, mientras que los siguientes deben ir separados por un ampersand `&`.

#### Ejemplos de URL

- `https://example.com/?abButtonId=0` - Botón 1 clic
- `https://example.com/?abButtonId=1` - Botón 2 clic
- `https://example.com/?utm_source=braze&abButtonId=0` - Botón 1 clic con otros parámetros de URL existentes
- `myApp://deep-link?page=home&abButtonId=1` - Enlace profundo móvil con botón 2 clic
- `<a href="https://example.com/?abButtonId=1">` - Elemento de anclaje `<a>` con clic en el botón 2

{% alert note %}
Los mensajes dentro de la aplicación sólo admiten clics en el Botón 1 y el Botón 2. Las URL que no especifiquen uno de estos dos ID de botón se registrarán como "clics en el cuerpo" genéricos.
{% endalert %}

### Abrir enlace en ventana nueva (sólo móvil)

Para abrir enlaces fuera de tu aplicación en una ventana nueva, configura `?abExternalOpen=true`. El mensaje se descartará antes de abrir el enlace.

Para la vinculación en profundidad, Braze abrirá tu URL independientemente del valor de `abExternalOpen`.

### Abrir como enlace profundo (sólo móvil)

Para que Braze gestione tu enlace HTTP o HTTPS como un vínculo profundo, configura `?abDeepLink=true`.

Cuando este parámetro de cadena de consulta está ausente o establecido en `false`, Braze intentará abrir el enlace Web en un navegador web interno dentro de la aplicación anfitriona.

### Cerrar mensaje dentro de la aplicación

Para cerrar un mensaje dentro de la aplicación, puedes utilizar el método javascript `brazeBridge.closeMessage()`.

Por ejemplo, `<a onclick="brazeBridge.closeMessage()" href="#">Close</a>` cerrará el mensaje dentro de la aplicación.

## Carga HTML con vista previa

Al crear mensajes HTML personalizados dentro de la aplicación, puedes obtener una vista previa de tu contenido interactivo directamente en Braze. 

El panel de vista previa de mensajes del editor muestra una vista previa realista que representa el JavaScript incluido en tu mensaje. Puedes obtener una vista previa e interactuar con tus mensajes personalizados desde el panel de vista previa haciendo clic a través de la paginación, enviando formularios o cuestionarios, viendo animaciones JavaScript, ¡y mucho más!

\![Interactuar con la vista previa HTML deslizando el dedo por las páginas.]({% image_buster /assets/img/iam-beta-javascript-preview.gif %})

{% alert tip %}
Cualquier método JavaScript de `brazeBridge` que utilices en tu HTML no actualizará los perfiles de usuario durante la vista previa en el panel.
{% endalert %}

### Requisitos del SDK {#supported-sdk-versions}

Para utilizar la vista previa HTML para los mensajes dentro de la aplicación, debes actualizarte a las siguientes versiones mínimas del SDK de Braze:

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

{% alert warning %}
Dado que este tipo de mensaje sólo puede ser recibido por determinadas versiones posteriores del SDK, los usuarios que se encuentren en versiones del SDK no compatibles no recibirán el mensaje. Considera la posibilidad de adoptar este tipo de mensaje una vez alcanzada una parte significativa de tu base de usuarios, o dirígete sólo a aquellos usuarios cuya versión de la aplicación sea posterior a los requisitos. Más información sobre cómo [filtrar por la versión más reciente de la aplicación]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions).
{% endalert %}

### Crear una campaña {#instructions}

Los usuarios de tu aplicación móvil deben actualizarse a las versiones SDK compatibles para recibir un mensaje dentro de la aplicación de **código personalizado**. Te recomendamos que [animes a los usuarios a actualizar]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/) sus aplicaciones móviles antes de lanzar campañas que dependan de versiones más recientes del SDK de Braze.

#### Ficheros de activos

Al crear mensajes dentro de la aplicación con código personalizado y carga HTML, puedes cargar activos de la campaña a la [biblioteca multimedia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) para hacer referencia a ellos en tu mensaje.

Se pueden cargar los siguientes tipos de archivos:

| Tipo de archivo        | Extensión del archivo                    |
| :--------------- | :-------------------------------- |
| Archivos de fuentes       | `.ttf`, `.woff`, `.otf`, `.woff2` |
| Imágenes SVG       | `.svg`                            |
| Archivos JavaScript | `.js`                             |
| Archivos CSS        | `.css`                            |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Braze recomienda subir activos a la biblioteca multimedia por dos razones:

1. Los activos añadidos a una campaña a través de la biblioteca multimedia permiten que tus mensajes se muestren incluso cuando el usuario está desconectado o tiene una mala conexión a Internet.
2. Los activos cargados en Braze pueden reutilizarse en distintas campañas.

##### Añadir archivos de activos

Puedes añadir activos nuevos o existentes a tu campaña.

Para añadir nuevos activos a tu campaña, utiliza la sección arrastrar y soltar para subir un archivo. Los activos añadidos en esta sección también se añadirán automáticamente a la biblioteca multimedia. Para añadir activos que ya hayas subido a la biblioteca multimedia, selecciona **Añadir desde biblioteca multimedia**.

Una vez añadidos tus activos, aparecerán en la sección **Activos para esta campaña**. 

Si el nombre de archivo de un activo coincide con el de un activo HTML local, se sustituirá automáticamente (por ejemplo, se carga `cat.png` y existe `<img src="cat.png" />` ). 

Si no, pasa el ratón por encima de un activo de la lista y selecciona <i class="fas fa-copy"></i> **Copiar** para copiar la URL del archivo en tu portapapeles. A continuación, pega la URL del activo copiado en tu HTML como harías normalmente al hacer referencia a un activo remoto.


### Editor HTML

Los cambios que hagas en el HTML se mostrarán automáticamente en el panel de vista previa mientras escribes. Cualquier método [JavaScript de`brazeBridge` ](#bridge) que utilices en tu HTML no actualizará los perfiles de usuario durante la vista previa en el panel.

{% alert tip %}
Puedes seleccionar <i class="fa-solid fa-magnifying-glass"></i> **¡Buscar** dentro del editor HTML para buscar dentro de tu código!
{% endalert %}

### Seguimiento de botones {#button-tracking-improvements}

Puedes hacer un seguimiento del rendimiento dentro de tu mensaje dentro de la aplicación de código personalizado utilizando el método [`brazeBridge.logClick(button_id)`]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/) método JavaScript. Esto te permite hacer un seguimiento programado de los "Botón 1", "Botón 2" y "Clics en el cuerpo" utilizando `brazeBridge.logClick('0')`, `brazeBridge.logClick('1')` o `brazeBridge.logClick()`, respectivamente.

| Clics     | Método                       |
| ---------- | ---------------------------- |
| Botón 1   | `brazeBridge.logClick('0')` |
| Botón 2   | `brazeBridge.logClick('1')` |
| Cuerpo clic | `brazeBridge.logClick()`    |
| Seguimiento personalizado de botones |`brazeBridge.logClick('your custom name here')`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Este método de seguimiento de botones sustituye a los anteriores métodos automáticos de seguimiento de clics (como `?abButtonId=0`), que han sido eliminados.
{% endalert %}

Puedes hacer un seguimiento de varios clics de botón por impresión. Por ejemplo, para cerrar un mensaje y registrar un clic en el Botón 2, puedes utilizar lo siguiente:

```html
<a href="#" onclick="brazeBridge.logClick('1');brazeBridge.closeMessage()">✖</a>
``` 

También puedes hacer un seguimiento de los nuevos nombres de botones personalizados: hasta 100 nombres únicos por campaña. Por ejemplo, `brazeBridge.logClick('blue button')` o `brazeBridge.logClick('viewed carousel page 3')`.

{% alert tip %}
Cuando utilices métodos JavaScript dentro de un atributo `onclick`, encierra los valores de cadena entre comillas simples para evitar conflictos con el atributo HTML de comillas dobles.
{% endalert %}

#### Limitaciones

- Puedes tener hasta 100 ID de botón únicos por campaña.
- Los ID de los botones pueden tener hasta 255 caracteres cada uno.
- Los ID de botón sólo pueden incluir letras, números, espacios, guiones y guiones bajos.

### Cambios incompatibles con el pasado {#backward-incompatible-changes}

1. El cambio incompatible más notable con este nuevo tipo de mensaje son los requisitos del SDK. A los usuarios cuyo SDK de aplicación no cumpla los [requisitos](#supported-sdk-versions) mínimos [de versión del SDK](#supported-sdk-versions) no se les mostrará el mensaje.
<br>

2. El enlace profundo `braze://close`, que antes era compatible con las aplicaciones móviles, se ha eliminado en favor del JavaScript `brazeBridge.closeMessage()`. Esto permite mensajes HTML multiplataforma, ya que la Web no admite enlaces profundos.

3. Se ha eliminado el seguimiento automático de los clics, que utilizaba `?abButtonId=0` para los ID de los botones, y el seguimiento del "cuerpo del clic" en los botones de cierre. Los siguientes ejemplos de código muestran cómo cambiar tu HTML para utilizar nuestros nuevos métodos JavaScript de seguimiento de clics:

   | Antes de | Después de |
   |:-------- |:------------|
   |<code><a href="braze://close">Botón Cerrar</a></code>|<code><a href="#" onclick="brazeBridge.logClick();brazeBridge.closeMessage()">Botón Cerrar</a></code>|
   |<code><a href="braze://close?abButtonId=0">Botón Cerrar</a></code>|<code><a href="#" onclick="brazeBridge.logClick('0');brazeBridge.closeMessage()">Botón Cerrar</a></code>|
   |<code><a href="app://deeplink?abButtonId=0">Botón de seguimiento 1</a></code>|<code><a href="app://deeplink" onclick="brazeBridge.logClick('0')">Botón de seguimiento 1</a></code>|
   |<code><script><br>location.href = "braze://close?abButtonId=1"<br></script></code>|<code><script><br>window.addEventListener("ab.BridgeReady", function(){<br>  brazeBridge.logClick("1");<br>  brazeBridge.closeMessage();<br>});<br></script></code>|

