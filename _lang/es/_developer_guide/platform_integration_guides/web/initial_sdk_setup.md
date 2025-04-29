---
nav_title: Configuración inicial del SDK
article_title: Configuración inicial del SDK Braze Web
platform: Web
page_order: 0
page_type: reference
---

# Configuración inicial del SDK para Web

> En este artículo de referencia se explica cómo instalar el SDK Web de Braze. El SDK Web de Braze te permite recopilar análisis y mostrar mensajes dentro de la aplicación, push y mensajes de tarjeta de contenido a tus usuarios de la web. Consulta nuestra [Documentación de ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html "JavaScriptJSDocs") para obtener una referencia técnica completa.

{% multi_lang_include archive/web-v4-rename.md %}

## Paso 1: Instala la biblioteca Braze

Puedes instalar la biblioteca Braze utilizando uno de los siguientes métodos. Si tu sitio web utiliza `Content-Security-Policy`, consulta nuestra [Guía de cabeceras de la política de seguridad de contenidos]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_security_policy/) antes de instalar la biblioteca.

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

Visita la [guía de integración de Google Tag Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/web/google_tag_manager/) para obtener más información.
{% endtab %}

{% tab braze cdn %}
Añade el SDK Braze Web directamente a tu HTML haciendo referencia a nuestro script alojado en CDN, que carga la biblioteca de forma asíncrona.

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Floading-snippet.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>
{% endtab %}
{% endtabs %}

## Paso 2: Inicializar el SDK

Una vez añadido el SDK Braze Web a tu sitio web, inicializa la biblioteca con la clave de API y la [URL del punto final SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) que encontrarás en **Configuración** > **Configuración de la aplicación** dentro de tu panel Braze.

{% alert note %}
Si has configurado las opciones de inicialización de Braze en un administrador de etiquetas, puedes omitir este paso.
{% endalert %}

Para obtener una lista completa de las opciones de `braze.initialize()`, junto con nuestros otros métodos de JavaScript, consulta nuestra [documentación sobre JavaScript](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize).

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

## Paso 3: Configurar notificaciones push (opcional)

Para configurar las notificaciones push para el SDK Web de Braze, se requiere una configuración adicional. Para un recorrido completo, consulta [Notificaciones push para la Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/).

## Registro

Para habilitar rápidamente el registro, puedes añadir `?brazeLogging=true` como parámetro a la URL de tu sitio web. También puedes habilitar el registro [básico](#basic-logging) o [personalizado](#custom-logging).

### Registro básico

{% tabs local %}
{% tab antes de la inicialización %}
Utiliza `enableLogging` para registrar mensajes básicos de depuración en la consola javascript antes de que se inicialice el SDK.

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
Utiliza `braze.toggleLogging()` para registrar mensajes básicos de depuración en la consola javascript después de inicializar el SDK. Tu método debe ser similar al siguiente

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
Los registros básicos son visibles para todos los usuarios, así que considera desactivarlos, o cambia a [`setLogger`](#custom-logging)antes de poner tu código en producción.
{% endalert %}

### Registro personalizado

Utiliza `setLogger` para registrar mensajes de depuración personalizados en la consola javascript. A diferencia de los registros básicos, estos registros no son visibles para los usuarios.

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

## Métodos alternativos de integración

### Marcos de renderizado del lado del servidor {#ssr}

Si utilizas un framework de renderizado desde el servidor como Next.js, puedes encontrarte con errores porque el SDK está pensado para ejecutarse en un entorno de navegador. Puedes resolver estos problemas importando dinámicamente el SDK.

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

### Soporte de Vite {#vite}

Si utilizas Vite y ves una advertencia sobre dependencias circulares o `Uncaught TypeError: Class extends value undefined is not a constructor or null`, puede que necesites excluir el SDK de Braze de su [descubrimiento de dependencias](https://vitejs.dev/guide/dep-pre-bundling.html#customizing-the-behavior):

```
optimizeDeps: {
    exclude: ['@braze/web-sdk']
},
```

### Soporte de Electron {#electron}

Electron no admite oficialmente notificaciones push web (consulta esta [incidencia de GitHub](https://github.com/electron/electron/issues/6697)). Hay otras [soluciones de código abierto](https://github.com/MatthieuLemoine/electron-push-receiver) que puedes probar y que no han sido probadas por Braze.

### Cargador de módulos AMD

Si utilizas RequireJS u otros cargadores de módulos AMD, te recomendamos que autoalojes una copia de nuestra biblioteca y la referencies como harías con otros recursos:

```javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```
### Alternativa Sin instalación AMD

Si tu sitio utiliza RequireJS u otro cargador de módulos AMD, pero prefieres cargar el SDK de la Web de Braze a través de una de las otras opciones anteriores, puedes cargar una versión de la biblioteca que no incluya compatibilidad con AMD. Esta versión de la biblioteca puede cargarse desde la siguiente ubicación CDN:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fno-amd-library.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

### Tealium iQ
Tealium iQ ofrece una integración básica de Braze llave en mano. Para configurar la integración, busca Braze en la interfaz de gestión de etiquetas de Tealium y proporciona la clave de API de SDK Web desde tu panel.

Para obtener más información o ayuda detallada sobre la configuración de Tealium, consulta nuestra [documentación sobre integración]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#about-tealium) o ponte en contacto con tu director de cuentas de Tealium.

### Otros administradores de etiquetas
Braze también puede ser compatible con otras soluciones de administración de etiquetas siguiendo nuestras instrucciones de integración dentro de una etiqueta HTML personalizada. Ponte en contacto con un representante de Braze si necesitas ayuda para evaluar estas soluciones.

### Solución de problemas del framework Jest {#jest}

Al utilizar Jest, es posible que aparezca un error similar a `SyntaxError: Unexpected token 'export'`. Para solucionarlo, ajusta tu configuración en `package.json` para ignorar el SDK de Braze:

```
"jest": {
  "transformIgnorePatterns": [
    "/node_modules/(?!@braze)"
  ]
}
```
