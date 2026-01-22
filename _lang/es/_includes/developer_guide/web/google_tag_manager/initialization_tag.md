### Requisitos previos

Antes de poder utilizar este método de integración, tendrás que [crear una cuenta y un contenedor para Google Tag Manager](https://support.google.com/tagmanager/answer/14842164).

### Paso 1: Abrir la galería de plantillas de etiquetas

En [Google Tag Manager](https://tagmanager.google.com/), elige tu espacio de trabajo y, a continuación, selecciona **Plantillas**. En el panel **Plantilla de etiquetas**, selecciona **Buscar en Galería**.

![La página de plantillas de un espacio de trabajo de ejemplo en Google Tag Manager.]({% image_buster /assets/img/web-gtm/search_tag_template_gallery.png %}){: style="max-width:95%;"}

### Paso 2: Añade la plantilla de la etiqueta de inicialización

En la galería de plantillas, busca `braze-inc`, y luego selecciona **Etiqueta de inicialización Braze**.

![La galería de plantillas que muestra las distintas plantillas 'braze-inc'.]({% image_buster /assets/img/web-gtm/template_gallery_results.png %}){: style="max-width:80%;"}

Selecciona **Añadir al espacio de trabajo** > **Añadir**.

![La página "Etiqueta de inicialización de Braze" en Google Tag Manager.]({% image_buster /assets/img/web-gtm/add_to_workspace.png %}){: style="max-width:70%;"}

### Paso 3: Configurar la etiqueta

En la sección **Plantillas**, selecciona la plantilla que acabas de añadir.

![La página "Plantillas" de Google Tag Manager muestra la plantilla de la etiqueta de inicialización de Braze.]({% image_buster /assets/img/web-gtm/select_tag_template.png %}){: style="max-width:95%;"}

Selecciona el icono del lápiz para abrir el desplegable **Configuración de etiquetas**.

![El mosaico de Configuración de Etiquetas con el icono del "lápiz" mostrado.]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

Introduce la información mínima requerida:

| Campo         | Descripción |
| ------------- | ----------- |
| **Clave de API**   | Tu [clave de API de Braze]({{site.baseurl}}/api/basics/#about-rest-api-keys), que se encuentra en el panel de Braze, en **Configuración** > Configuración de la aplicación. |
| **Punto final de API** | La URL de su punto final REST. Tu punto final dependerá de la URL Braze de [tu instancia]({{site.baseurl}}/api/basics/#endpoints). |
| **Versión del SDK**  | La versión más reciente de `MAJOR.MINOR` del SDK de Web Braze que aparece en el [registro de cambios]({{site.baseurl}}/developer_guide/changelogs/?sdktab=web). Por ejemplo, si la última versión es `4.1.2`, introduce `4.1`. Para más información, consulta [Acerca de la gestión de versiones del SDK]({{site.baseurl}}/developer_guide/sdk_integration/version_management/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Para otras configuraciones de inicialización, selecciona **Opciones de Inicialización de Braze** y elige las opciones que necesites.

![La lista de Opciones de Inicialización de Braze en 'Configuración de Etiquetas'.]({% image_buster /assets/img/web-gtm/braze_initialization_options.png %}){: style="max-width:65%;"}

### Paso 4: Configurar para desencadenar en *todas las páginas*

La etiqueta de inicialización debe ejecutarse en todas las páginas de tu sitio. Esto te permite utilizar los métodos del SDK de Braze y registrar los análisis push web.

### Paso 5: Verifica tu integración

Puedes verificar tu integración utilizando cualquiera de las siguientes opciones:

- **Opción 1:** Con la [herramienta de depuración](https://support.google.com/tagmanager/answer/6107056?hl=en) de Google Tag Manager, puedes comprobar si la etiqueta de inicialización de Braze se desencadena correctamente en las páginas o eventos configurados.
- **Opción 2:** Comprueba si se han realizado solicitudes de red a Braze desde tu página Web. Además, ahora debe definirse la biblioteca global `window.braze`.
