## Uso del administrador de etiquetas de Google Tag Manager {#initialization-tag}

### Paso 1: Configuración push (opcional)

Opcionalmente, si quieres poder enviar push a través de Google Tag Manager, sigue primero las directrices de [integración de push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web) a:
1. Configura el prestador de servicios de tu sitio, colocándolo en el directorio raíz de tu sitio
2. Configurar el registro del navegador - Una vez configurado el prestador de servicios, debes establecer el método `braze.requestPushPermission()` de forma nativa en su aplicación o mediante una etiqueta HTML personalizada (a través del panel GTM). También tendrás que asegurarte de que la etiqueta se dispara después de inicializar el SDK.

### Paso 2: Selecciona la etiqueta de inicialización

Busca Braze en la galería de plantillas de la comunidad y selecciona la **etiqueta de inicialización Braze**.

![Un cuadro de diálogo que muestra los ajustes de configuración de la etiqueta de inicialización Braze. Las configuraciones incluidas son "tipo de etiqueta", "clave de API", "punto final de API", "versión de SDK", "ID de usuario externo" e "ID push web de Safari".]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

### Paso 3: Configurar ajustes

Introduce la clave de identificador de tu aplicación API de Braze y el punto final SDK, que puedes encontrar en la página **Administrar configuración** de tu panel. Introduce la versión más reciente del SDK Web `major.minor`. Por ejemplo, si la última versión es `4.1.2`, introduce `4.1`. Puedes ver una lista de las versiones del SDK en nuestro [registro de cambios](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md).

### Paso 4: Elige las opciones de inicialización

Elige entre el conjunto opcional de opciones de inicialización adicionales descritas en la guía [Configuración inicial]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#step-2-initialize-braze).

### Paso 5: Verificación y control de calidad

Una vez que hayas desplegado esta etiqueta, hay dos formas de verificar una integración adecuada:

1. Utilizando la [herramienta de depuración](https://support.google.com/tagmanager/answer/6107056?hl=en) de Google Tag Manager, deberías ver que la etiqueta de inicialización de Braze se ha desencadenado en tus páginas o eventos configurados.
2. Deberías ver que se hacen peticiones de red a Braze, y la biblioteca global `window.braze` debería estar ahora definida en tu página Web.
