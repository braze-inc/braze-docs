## Acerca del SDK de Web Braze

El SDK de Web Braze te permite recopilar análisis y mostrar mensajes dentro de la aplicación, push y mensajes de tarjeta de contenido a tus usuarios de la Web. Para más información, consulta la [documentación de referencia de JavaScript de ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html "BrazeJSDocs").

{% multi_lang_include archive/web-v4-rename.md %}

## Integración del SDK de la Web

{% alert tip %}
¿No estás seguro de si el método de integración estándar es el adecuado para ti? Consulta nuestros [otros métodos de integración](#web_other-integration-methods) antes de continuar.
{% endalert %}

### Paso 1: Instala la biblioteca Braze

Puedes instalar la biblioteca Braze utilizando uno de los siguientes métodos. Si tu sitio web utiliza `Content-Security-Policy`, consulta nuestra [Guía de cabeceras de la política de seguridad de contenidos]({{site.baseurl}}/developer_guide/platforms/web/content_security_policy/) antes de instalar la biblioteca.

{% alert important %}
Aunque la mayoría de los bloqueadores de anuncios no bloquearán el SDK de la Web de Braze, se sabe que algunos bloqueadores de anuncios más restrictivos causan problemas.
{% endalert %}

{% tabs local %}
{% tab administrador de paquetes %}
Si tu sitio utiliza los administradores de paquetes NPM o Yarn, puedes añadir el [paquete NPM de Braze](https://www.npmjs.com/package/@braze/web-sdk) como dependencia.

A partir de la versión 3.0.0, se incluyen definiciones tipográficas. Para obtener notas sobre la actualización de 2.x a 3.x, consulta nuestro [registro de cambios](https://github.com/braze-inc/braze-web-sdk/blob/master/UPGRADE_GUIDE.md).

```bash
npm install --save @braze/web-sdk
# or, using yarn:
# yarn add @braze/web-sdk
```

Una vez instalado, puedes `import` o `require` la biblioteca de la forma típica:

```typescript
import * as braze from "@braze/web-sdk";
// or, using `require`
const braze = require("@braze/web-sdk");
```
{% endtab %}

{% tab Google Tag Manager %}
El SDK de Braze Web puede instalarse desde la biblioteca de plantillas de Google Tag Manager. Se admiten dos etiquetas:

1. Etiqueta de inicialización: carga el SDK Web en tu sitio web y, opcionalmente, establece el ID de usuario externo.
2. Etiqueta de acciones: se utiliza para desencadenar eventos personalizados, compras, cambiar ID de usuario o alternar el seguimiento del SDK.

Visita la [guía de integración de Google Tag Manager]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web#web_google-tag-manager) para obtener más información.
{% endtab %}

{% tab braze cdn %}
Añade el SDK Braze Web directamente a tu HTML haciendo referencia a nuestro script alojado en CDN, que carga la biblioteca de forma asíncrona.

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Floading-snippet.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>
{% endtab %}
{% endtabs %}

### Paso 2: Inicializar el SDK (opcional)

Si has configurado las opciones de inicialización de Braze en un administrador de etiquetas, puedes omitir este paso.

De lo contrario, después de añadir el SDK Braze Web a tu sitio web, inicializa la biblioteca con la clave de API y la [URL del punto final SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) que se encuentran en **Configuración** > **Configuración de la aplicación** dentro de tu panel Braze. Para obtener una lista completa de las opciones de `braze.initialize()`, junto con nuestros otros métodos de JavaScript, consulta la [documentación de JavaScript de Braze](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize).

```javascript
// initialize the SDK
braze.initialize('YOUR-API-KEY-HERE', {
    baseUrl: "YOUR-SDK-ENDPOINT-HERE"
});

// optionally show all in-app messages without custom handling
braze.automaticallyShowInAppMessages();

// if you use Content Cards
braze.subscribeToContentCardsUpdates(function(cards){
    // cards have been updated
});

// optionally set the current user's external ID before starting a new session
// you can also call `changeUser` later in the session after the user logs in
if (isLoggedIn){
    braze.changeUser(userIdentifier);
}

// `openSession` should be called last - after `changeUser` and `automaticallyShowInAppMessages`
braze.openSession();
```

{% alert important %}
Los usuarios anónimos en dispositivos móviles o Web pueden contabilizarse en tu [MAU]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data/#monthly-active-users). Como resultado, puede que quieras cargar o inicializar condicionalmente el SDK para excluir a estos usuarios de tu recuento de MAU.
{% endalert %}

## Configuraciones opcionales

### Registro

Para habilitar rápidamente el registro, puedes añadir `?brazeLogging=true` como parámetro a la URL de tu sitio web. También puedes habilitar el registro [básico](#web_basic-logging) o [personalizado](#web_custom-logging).

#### Registro básico

{% tabs local %}
{% tab antes de la inicialización %}
Utiliza `enableLogging` para registrar mensajes básicos de depuración en la consola de JavaScript antes de que se inicialice el SDK.

```javascript
enableLogging: true
```

Tu método debe ser similar al siguiente

```javascript
braze.initialize('API-KEY', {
    baseUrl: 'API-ENDPOINT',
    enableLogging: true
});
braze.openSession();
```
{% endtab %}

{% tab después de la inicialización %}
Utiliza `braze.toggleLogging()` para registrar mensajes básicos de depuración en la consola de JavaScript después de inicializar el SDK. Tu método debe ser similar al siguiente

```javascript
braze.initialize('API-KEY', {
    baseUrl: 'API-ENDPOINT',
});
braze.openSession();
...
braze.toggleLogging();
```
{% endtab %}
{% endtabs %}

{% alert important %}
Los registros básicos son visibles para todos los usuarios, así que considera desactivarlos, o cambia a [`setLogger`](#web_custom-logging)antes de poner tu código en producción.
{% endalert %}

#### Registro personalizado

Utiliza `setLogger` para registrar mensajes de depuración personalizados en la consola de JavaScript. A diferencia de los registros básicos, estos registros no son visibles para los usuarios.

```javascript
setLogger(loggerFunction: (message: STRING) => void): void
```

Sustituye `STRING` por tu mensaje como parámetro de una sola cadena. Tu método debe ser similar al siguiente

```javascript
braze.initialize('API-KEY');
braze.setLogger(function(message) {
    console.log("Braze Custom Logger: " + message);
});
braze.openSession();
```

## Actualizar el SDK

{% multi_lang_include archive/web-v4-rename.md %}

Cuando hagas referencia al SDK de Braze Web desde nuestra red de entrega de contenidos, por ejemplo, `https://js.appboycdn.com/web-sdk/a.a/braze.min.js` (como recomiendan nuestras instrucciones de integración predeterminadas), tus usuarios recibirán actualizaciones menores (correcciones de errores y características compatibles con versiones anteriores, versiones `a.a.a` a `a.a.z` en los ejemplos anteriores) automáticamente cuando actualicen tu sitio.

Sin embargo, cuando publicamos cambios importantes, te pedimos que actualices el SDK Braze Web manualmente para asegurarte de que nada en tu integración se verá afectado por los cambios de última hora. Además, si descargas nuestro SDK y lo alojas tú mismo, no recibirás ninguna actualización de versión automáticamente y deberás actualizarlo manualmente para recibir las últimas características y correcciones de errores.

Puedes mantenerte al día de nuestra última versión [siguiendo nuestra fuente de versiones](https://github.com/braze-inc/braze-web-sdk/tags.atom) con el lector RSS o el servicio que prefieras, y consultar [nuestro registro de cambios](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md) para conocer el historial completo de versiones de nuestro SDK para la Web. Para actualizar el SDK Web de Braze:

- Actualiza la versión de la biblioteca Braze cambiando el número de versión de `https://js.appboycdn.com/web-sdk/[OLD VERSION NUMBER]/braze.min.js`, o en las dependencias de tu administrador de paquetes.
- Si tienes integrado el push web, actualiza el archivo del prestador de servicios en tu sitio: por defecto, se encuentra en `/service-worker.js`, en el directorio raíz de tu sitio, pero la ubicación puede estar personalizada en algunas integraciones. Debes acceder al directorio raíz para alojar un archivo de prestador de servicios.

Estos dos archivos deben actualizarse coordinadamente para que funcionen correctamente.

## Google Tag Manager {#google-tag-manager}

[Google Tag Manager (GTM](https://support.google.com/tagmanager/answer/6103696) ) te permite añadir, eliminar y editar etiquetas de forma remota en tu sitio web sin necesidad de liberar código de producción ni recursos de ingeniería. Braze ofrece las siguientes plantillas GTM:

|Tipo de etiqueta|Casos de uso|
|--------|--------|
| **Etiqueta de inicialización:** | La etiqueta de inicialización puede utilizarse para [inicializar el SDK de Web Braze]({{site.baseurl}}/developer_guide/sdk_integration/initialization/?sdktabs=web).|
| **Etiqueta de acción:** | La etiqueta de acción puede utilizarse para [gestionar tarjetas de contenido]({{site.baseurl}}/docs/developer_guide/content_cards/?sdktab=web#web_using-google-tag-manager) y [registrar análisis]({{site.baseurl}}/docs/developer_guide/analytics/).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Ambas etiquetas pueden añadirse a tu espacio de trabajo desde [la galería de la comunidad de Google](https://tagmanager.google.com/gallery/#/?filter=braze) o buscando Braze al añadir una nueva etiqueta desde las plantillas de la comunidad.

![imagen de búsqueda de la galería]({% image_buster /assets/img/web-gtm/gtm-community-gallery-search.png %})

### Política de consentimiento del usuario de la UE actualizada de Google

{% alert important %}
Google está actualizando su [Política de Consentimiento de Usuario de la UE](https://www.google.com/about/company/user-consent-policy/) en respuesta a los cambios en la [Ley de Mercados Digitales (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html), que entrará en vigor el 6 de marzo de 2024. Este nuevo cambio obliga a los anunciantes a revelar determinada información a sus usuarios finales del EEE y del Reino Unido, así como a obtener de ellos los consentimientos necesarios. Consulte la siguiente documentación para obtener más información.
{% endalert %}

Como parte de la Política de consentimiento del usuario de la UE de Google, los siguientes atributos personalizados booleanos deben registrarse en los perfiles de usuario:

- `$google_ad_user_data`
- `$google_ad_personalization`

Si los configuras a través de la integración GTM, los atributos personalizados requieren la creación de una etiqueta HTML personalizada. A continuación se muestra un ejemplo de cómo registrar estos valores como tipos de datos booleanos (no como cadenas):

```js
<script>
window.braze.getUser().setCustomUserAttribute("$google_ad_personalization", true);
</script>
```

Para más información, consulta [Sincronización de audiencias con Google]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/).

## Otros métodos de integración

### Páginas móviles aceleradas (AMP)
{% details Ver más %}
#### Paso 1: Incluir script de notificación push web AMP

Añade la siguiente etiqueta de script asíncrono a tu cabecera:

```js
<script async custom-element="amp-web-push" src="https://cdn.ampproject.org/v0/amp-web-push-0.1.js"></script>
```

#### Paso 2: Añadir widgets de suscripción

Añade un widget al cuerpo de tu HTML que permita a los usuarios suscribirse y cancelar suscripción desde push.

```js
<!-- A subscription widget -->
<amp-web-push-widget visibility="unsubscribed" layout="fixed" width="250" height="80">
  <button on="tap:amp-web-push.subscribe">Subscribe to Notifications</button>
</amp-web-push-widget>

<!-- An unsubscription widget -->
<amp-web-push-widget visibility="subscribed" layout="fixed" width="250" height="80">
  <button on="tap:amp-web-push.unsubscribe">Unsubscribe from Notifications</button>
</amp-web-push-widget>
```

#### Paso 3: Añade `helper-iframe` y `permission-dialog`

El componente AMP Web Push crea una ventana emergente para gestionar las suscripciones push, por lo que tendrás que añadir los siguientes archivos de ayuda a tu proyecto para habilitar esta característica:

- [`helper-iframe.html`](https://cdn.ampproject.org/v0/amp-web-push-helper-frame.html)
- [`permission-dialog.html`](https://cdn.ampproject.org/v0/amp-web-push-permission-dialog.html)

#### Paso 4: Crear un archivo de prestador de servicios

Crea un archivo `service-worker.js` en el directorio raíz de tu sitio web y añade el siguiente fragmento de código:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### Paso 5: Configurar el elemento HTML de notificación push web de AMP

Añade el siguiente elemento HTML `amp-web-push` al cuerpo de tu HTML. Ten en cuenta que tienes que añadir tus [`apiKey` y `baseUrl`](https://documenter.getpostman.com/view/4689407/SVYrsdsG) como parámetros de consulta a `service-worker-URL`.

```js
<amp-web-push
layout="nodisplay"
id="amp-web-push"
helper-iframe-url="FILE_PATH_TO_YOUR_HELPER_IFRAME"
permission-dialog-url="FILE_PATH_TO_YOUR_PERMISSION_DIALOG"
service-worker-url="FILE_PATH_TO_YOUR_SERVICE_WORKER?apiKey={YOUR_API_KEY}&baseUrl={YOUR_BASE_URL}"
>
```
{% enddetails %}

### AMD: Desactivar soporte

Si tu sitio utiliza RequireJS u otro cargador de módulos AMD, pero prefieres cargar el SDK de la Web de Braze a través de una de las otras opciones de esta lista, puedes cargar una versión de la biblioteca que no incluya compatibilidad con AMD. Esta versión de la biblioteca puede cargarse desde la siguiente ubicación CDN:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fno-amd-library.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

### AMD: Cargador de módulos

Si utilizas RequireJS u otros cargadores de módulos AMD, te recomendamos que autoalojes una copia de nuestra biblioteca y la referencies como harías con otros recursos:

```javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```

### Electrón {#electron}

Electron no admite oficialmente notificaciones push web (consulta esta [incidencia de GitHub](https://github.com/electron/electron/issues/6697)). Hay otras [soluciones de código abierto](https://github.com/MatthieuLemoine/electron-push-receiver) que puedes probar y que no han sido probadas por Braze.

### Marco Jest {#jest}

Al utilizar Jest, es posible que aparezca un error similar a `SyntaxError: Unexpected token 'export'`. Para solucionarlo, ajusta tu configuración en `package.json` para ignorar el SDK de Braze:

```
"jest": {
  "transformIgnorePatterns": [
    "/node_modules/(?!@braze)"
  ]
}
```

### Marcos SSR {#ssr}

Si utilizas un marco de renderizado del lado del servidor (SSR) como Next.js, puedes encontrar errores porque el SDK está pensado para ejecutarse en un entorno de navegador. Puedes resolver estos problemas importando dinámicamente el SDK.

Puedes conservar las ventajas de la arborescencia al hacerlo exportando las partes del SDK que necesites en un archivo aparte y luego importando dinámicamente ese archivo en tu componente.

```javascript
// MyComponent/braze-exports.js
// export the parts of the SDK you need here
export { initialize, openSession } from "@braze/web-sdk";

// MyComponent/MyComponent.js
// import the functions you need from the braze exports file
useEffect(() => {
    import("./braze-exports.js").then(({ initialize, openSession }) => {
        initialize("YOUR-API-KEY-HERE", {
            baseUrl: "YOUR-SDK-ENDPOINT",
            enableLogging: true,
        });
        openSession();
    });
}, []);
```

Alternativamente, si utilizas webpack para empaquetar tu aplicación, puedes aprovechar sus comentarios mágicos para importar dinámicamente sólo las partes del SDK que necesites.

```javascript
// MyComponent.js
useEffect(() => {
    import(
        /* webpackExports: ["initialize", "openSession"] */
        "@braze/web-sdk"
    ).then(({ initialize, openSession }) => {
        initialize("YOUR-API-KEY-HERE", {
            baseUrl: "YOUR-SDK-ENDPOINT",
            enableLogging: true,
        });
        openSession();
    });
}, []);
```

### Tealium iQ

Tealium iQ ofrece una integración básica de Braze llave en mano. Para configurar la integración, busca Braze en la interfaz de gestión de etiquetas de Tealium y proporciona la clave de API de SDK Web desde tu panel.

Para obtener más información o ayuda detallada sobre la configuración de Tealium, consulta nuestra [documentación sobre integración]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#about-tealium) o ponte en contacto con tu director de cuentas de Tealium.

### Vite {#vite}

Si utilizas Vite y ves una advertencia sobre dependencias circulares o `Uncaught TypeError: Class extends value undefined is not a constructor or null`, puede que necesites excluir el SDK de Braze de su [descubrimiento de dependencias](https://vitejs.dev/guide/dep-pre-bundling.html#customizing-the-behavior):

```
optimizeDeps: {
    exclude: ['@braze/web-sdk']
},
```

### Otros administradores de etiquetas

Braze también puede ser compatible con otras soluciones de administración de etiquetas siguiendo nuestras instrucciones de integración dentro de una etiqueta HTML personalizada. Ponte en contacto con un representante de Braze si necesitas ayuda para evaluar estas soluciones.
