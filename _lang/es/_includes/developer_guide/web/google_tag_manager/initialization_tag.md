### Requisitos previos

Antes de poder utilizar este método de integración, deberás [crear una cuenta y un contenedor para Google Tag Manager](https://support.google.com/tagmanager/answer/14842164).

### Paso 1: Abrir la galería de plantillas de etiquetas

En [Google Tag Manager](https://tagmanager.google.com/), elige tu espacio de trabajo y, a continuación, selecciona **Plantillas**. En el panel **Plantilla de etiqueta**, selecciona **Buscar galería**.

![La página de plantillas para un espacio de trabajo de ejemplo en Google Tag Manager.]({% image_buster /assets/img/web-gtm/search_tag_template_gallery.png %}){: style="max-width:95%;"}

### Paso 2: Añade la plantilla de etiqueta de inicialización.

En la galería de plantillas, busca `braze-inc`y selecciona **la etiqueta** de **inicialización de Braze**.

![La galería de plantillas que muestra las distintas plantillas de «Braze-inc».]({% image_buster /assets/img/web-gtm/template_gallery_results.png %}){: style="max-width:80%;"}

Selecciona **Añadir al espacio de trabajo** > **Añadir**.

![La página «Etiqueta de inicialización de Braze» en Google Tag Manager.]({% image_buster /assets/img/web-gtm/add_to_workspace.png %}){: style="max-width:70%;"}

### Paso 3: Configura la etiqueta.

En la sección **Plantillas**, selecciona la plantilla que acabas de añadir.

![La página «Plantillas» de Google Tag Manager muestra la plantilla de etiqueta de inicialización de Braze.]({% image_buster /assets/img/web-gtm/select_tag_template.png %}){: style="max-width:95%;"}

Selecciona el icono del lápiz para abrir el menú desplegable **Configuración de etiquetas**.

![El mosaico Configuración de etiquetas con el icono del «lápiz» mostrado.]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

Introduce la información mínima requerida:

| Campo         | Descripción |
| ------------- | ----------- |
| **Clave de API**   | Tu [clave de API de Braze]({{site.baseurl}}/api/basics/#about-rest-api-keys), que se encuentra en el panel de Braze, en **Configuración** > **Configuración de la aplicación**. |
| **Punto final de API** | La URL de su punto final REST. Tu punto final dependerá de la URL Braze de [tu instancia]({{site.baseurl}}/api/basics/#endpoints). |
| **Versión del SDK**  | La `MAJOR.MINOR`versión más reciente del SDK de Web Braze que aparece en el [registro de cambios]({{site.baseurl}}/developer_guide/changelogs/?sdktab=web). Por ejemplo, si la última versión es `4.1.2`, introduce `4.1`. Para obtener más información, consulta [Acerca de la gestión de versiones del SDK]({{site.baseurl}}/developer_guide/sdk_integration/version_management/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Para obtener configuraciones de inicialización adicionales, selecciona **Opciones de inicialización de Braze** y elige las opciones que necesites.

![La lista de opciones de inicialización de Braze se encuentra en «Configuración de etiquetas».]({% image_buster /assets/img/web-gtm/braze_initialization_options.png %}){: style="max-width:65%;"}

### Paso 4: Elige las opciones de inicialización

La etiqueta de inicialización de Braze muestra las siguientes opciones. La mayoría de ellas están mapeadas directamente al [SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) [web`InitializationOptions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions), y algunas corresponden a métodos del SDK web que la etiqueta llamará durante la inicialización. Selecciona las opciones que se ajusten a tus necesidades de integración:

| Opción GTM | Configuración o método del SDK Web | Descripción |
| --- | --- | --- |
| **Permitir mensajes HTML dentro de la aplicación** | `allowUserSuppliedJavascript` | Habilita mensajes HTML dentro de la aplicación, banners y acciones de clic JavaScript proporcionadas por el usuario. Necesario para [mensajes HTML dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/) y [banners]({{site.baseurl}}/developer_guide/banners/placements/?sdktab=web) que utilizan HTML personalizado. Habilita esta opción solo si confías en el contenido HTML y JavaScript, ya que permite la ejecución de JavaScript proporcionado por el usuario. |
| **Número de versión de la aplicación** | `appVersion`, `appVersionNumber` | Versión de la aplicación para segmentación (por ejemplo, `1.2.3.4`). |
| **Abrir automáticamente una nueva sesión** | `braze.openSession()` | Abre una nueva sesión después de que el SDK se inicialice llamando a este método por ti. |
| **Mostrar automáticamente los mensajes nuevos dentro de la aplicación** | `braze.automaticallyShowInAppMessages()` | Muestra automáticamente los nuevos mensajes dentro de la aplicación cuando llegan del servidor llamando a este método después de la inicialización. |
| **Desactivar el mantenimiento automático de tokens de notificaciones push** | `disablePushTokenMaintenance` | Impide que el SDK sincronice los tokens de notificaciones push con el backend de Braze en las nuevas sesiones. |
| **Desactivar el registro automático de prestadores de servicios** | `manageServiceWorkerExternally` | Úsalo si tú mismo realizas el registro y controlas el prestador de servicios. |
| **Desactivar las cookies** | `noCookies` | Utiliza localStorage en lugar de cookies para los datos de usuario/sesión. Evita el reconocimiento entre subdominios. |
| **Desactivar Font Awesome** | `doNotLoadFontAwesome` | Evita que el SDK cargue Font Awesome desde el CDN. Úsalo si tu sitio web tiene su propio Font Awesome. |
| **Habilitar la autenticación SDK** | `enableSdkAuthentication` | Habilita [la autenticación del SDK]({{site.baseurl}}/developer_guide/sdk_integration/authentication/). |
| **Habilitar el registro del SDK Web** | `enableLogging` | Habilita el registro de la consola para la depuración. Eliminar antes de la producción del producto. |
| **Intervalo mínimo entre mensajes desencadenados** | `minimumIntervalBetweenTriggerActionsInSeconds` | Segundos mínimos entre acciones desencadenantes (predeterminado: 30). |
| **Abrir tarjetas en una nueva pestaña** | `openCardsInNewTab` | Abre los enlaces de las tarjetas de contenido en una nueva pestaña cuando se utiliza la interfaz de usuario predeterminada de la fuente. |
| **Ubicación del prestador de servicios** | `serviceWorkerLocation` | Ruta personalizada para el archivo del prestador de servicios (predeterminado: `/service-worker.js`). |
| **Tiempo de espera de la sesión (segundos)** | `sessionTimeoutInSeconds` | Tiempo de espera de la sesión en segundos (predeterminado: 1800). |

{% alert note %}
Para habilitar [los mensajes HTML personalizados dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/) cuando utilices la etiqueta de inicialización de Braze de Google Tag Manager, selecciona **Permitir mensajes HTML dentro de la aplicación** en **las opciones de inicialización de Braze**. Esta casilla de verificación está mapeada con la opción`allowUserSuppliedJavascript` de inicialización en`braze.initialize()`y la establece en `true`. La etiqueta de inicialización de Braze de Google Tag Manager utiliza esta etiqueta en lugar del nombre de la opción.
{% endalert %}

Para las opciones que no aparecen en la plantilla GTM (como `contentSecurityNonce`, `localization`, o `devicePropertyAllowlist`), utiliza [la inicialización]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) [en tiempo de ejecución]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web).

### Paso 5: Configurar para desencadenar en *todas las páginas*

La etiqueta de inicialización debe ejecutarse en todas las páginas de tu sitio web. Esto te permite utilizar los métodos del SDK de Braze y registrar análisis de notificaciones push web.

### Paso 6: Verifica tu integración

Puedes verificar tu integración utilizando cualquiera de las siguientes opciones:

- **Opción 1:** Con [la herramienta de depuración](https://support.google.com/tagmanager/answer/6107056?hl=en) de Google Tag Manager, puedes comprobar si la etiqueta de inicialización de Braze desencadena correctamente en las páginas o eventos que has configurado.
- **Opción 2:** Comprueba si hay solicitudes de red realizadas a Braze desde tu página Web. Además, ahora se debe definir la biblioteca `window.braze`global.
