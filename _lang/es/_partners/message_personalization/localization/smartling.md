---
nav_title: Smartling
article_title: Smartling
description: "Este artículo de referencia describe la asociación entre Braze y Smartling, un software basado en la nube para la localización. El conector Braze admite la traducción de plantillas de correo electrónico HTML, bloques de contenido, lienzos y mensajes de correo electrónico de campaña."
alias: /partners/smartling/
page_type: partner
search_tag: Partner
---

# Smartling

> [Smartling](https://www.smartling.com/) es un software integral de gestión de la traducción en la nube para clientes que buscan automatizar la traducción de sitios web, aplicaciones y experiencias de cliente.

_Esta integración está mantenida por Smartling._

## Sobre la integración

El conector Braze admite traducciones para mensajes en campañas y lienzos (correo electrónico, push y mensajes dentro de la aplicación), plantillas de correo electrónico y bloques de contenido. Consulta la tabla siguiente para conocer los canales y características compatibles cuando decidas utilizar el nuevo conector con soporte multilingüe o el flujo de trabajo heredado.

| Canal/Característica | Editor tradicional (ex. HTML) | Editor de arrastrar y soltar |
| --------------- | ----------------------------- | -------------------- |
| [Correo electrónico]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=email) | ✅ | ✅ |
| [IAM]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=in-app%20message) | ✅ | ✅ |
| [Push]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=push) | ✅ | n/a |
| Plantilla de correo electrónico | Flujo de trabajo heredado | Flujo de trabajo heredado|
| Bloques de contenido |  ✅* |  ✅* |

\*Para más información, consulta [Gestionar las traducciones de los bloques de contenido](#managing-translations-for-content-blocks).

### Flujo de trabajo heredado

Dependiendo de tu caso de uso, gestiona las traducciones de los bloques de contenido utilizando el flujo de trabajo de traducción heredado o el flujo de trabajo actualizado. 

En el flujo de trabajo actualizado, utilizando el soporte multilingüe de Braze y las localizaciones en los mensajes, se añaden etiquetas de traducción al Bloque de Contenido. Sin embargo, Smartling ejecuta las traducciones a nivel de mensaje. El contenido sólo se traduce cuando se incluye en una campaña o Canvas y se establece la configuración regional de destino. Para saber más, consulta [Gestionar las traducciones de los bloques de contenido](#managing-translations-for-content-blocks).

Para las plantillas de correo electrónico, sólo se admite el flujo de trabajo heredado. Para saber más, consulta [Gestionar las traducciones mediante el flujo de trabajo heredado](#managing-translations-using-the-legacy-workflow).

## Requisitos previos

| Requisito                   | Descripción                                                                                                                                                         |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cuenta Smartling             | Se necesita una [cuenta Smartling](https://dashboard.smartling.com/) para beneficiarse de esta asociación.                                                          |
| Proyecto de traducción de Smartling | Para conectar tu cuenta Braze con Smartling, primero debes registrarte y [crear un proyecto de traducción](https://help.smartling.com/hc/en-us/articles/115003074093). |
| Clave de API REST de Braze            | Una clave Braze REST API con los siguientes permisos: <br>- campaigns.translations.get<br>- campaigns.translations.update<br>- campaigns.list<br>- campaigns.details<br>- canvas.translations.get<br>- canvas.translations.update<br>- campaigns.details<br>- templates.email.create<br>- templates.email.update<br>- templates.email.list<br>- templates.email.info<br>- templates.translations.get<br>- templates.translations.update<br>- content_blocks.info<br>- content_blocks.list<br>- content_blocks.create<br>- content_blocks.update<br><br> Se puede crear en el panel de Braze desde **Configuración > Claves de API**. |
| Punto final REST Braze           | [La URL de tu punto final REST]({{site.baseurl}}/api/basics/#endpoints). Tu punto final depende de la URL Braze de tu instancia.             |
| Configuración multilingüe Braze | [Configuración multilingüe completa en Braze]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#prerequisites) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Establecer la configuración multilingüe en Braze

Consulta [las instrucciones de configuración multilingüe de Braze]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#prerequisites) para configurar las localizaciones en Braze.

### Paso 2: Configurar el proyecto Braze en Smartling TMS

Consulta la [documentación de Smartling](https://help.smartling.com/hc/en-us/articles/13248549217435) para más detalles sobre la configuración del conector.

### Conexión de Braze a Smartling

1. En tu [cuenta Smartling](https://dashboard.smartling.com/), crea un tipo de proyecto de [conector Braze](https://help.smartling.com/hc/en-us/articles/115003074093).

![Conexión Braze en Smartling.]({% image_buster /assets/img/smartling/image1_Connecting_Braze_to_Smartling.png %})

{: start="2"}
2\. En este proyecto, selecciona **Configuración** > **Configuración de Braze** > **Conectar a Braze**.
3\. Rellena los campos obligatorios, como la URL de la API y la clave de API. Si la conexión de prueba se realiza correctamente, guarda la conexión. Si la prueba no tiene éxito, confirma que has introducido la URL y la clave de API correctas.

![Conexión Braze en la configuración de la API de Smartling.]({% image_buster /assets/img/smartling/image2_API.png %})

{: start="4"}
4\. Añade idiomas adicionales al proyecto.

![Conexión Braze en Lenguajes de Proyecto Smartling.]({% image_buster /assets/img/smartling/image3_project_languages.png %})

{: start="5"}
5\. En Configuración Braze, comprueba que los valores de la columna **Idioma de destino (Braze)** coinciden con las localizaciones configuradas en la configuración multilingüe Braze. La convención de nomenclatura de la localización debe coincidir exactamente.

![Conexión Braze en la Confirmación del Lenguaje Smartling.]({% image_buster /assets/img/smartling/image4_language_confirmation.png %})

### Paso 3: Añadir etiquetas de traducción a tu mensaje Braze

Consulta [las instrucciones de Braze]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales/?tab%3Dhtml%2520editor#prerequisites) sobre cómo añadir etiquetas de traducción a tus mensajes:

- [Correo electrónico]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=email)
- [Push]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=push)
- [Mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=in-app%20message)

Aquí tienes un ejemplo de campaña de correo electrónico HTML con etiquetas de traducción.

![Braze el correo electrónico con etiquetas de traducción.]({% image_buster /assets/img/smartling/image5_translation_tags.png %})

Debes guardar el mensaje como borrador antes de poder seleccionar las localizaciones.

### Paso 4: Gestionar las traducciones en Smartling

Después de conectar y configurar el conector Braze, busca el contenido Braze en la pestaña Braze de tu proyecto Smartling. Para más información, consulta la [documentación de Smartling](https://help.smartling.com/hc/en-us/articles/13248577069979).

Smartling ofrece funciones avanzadas para buscar y seleccionar contenidos por:
- Búsqueda por palabra clave
- Tipo de contenido Braze
- Etiquetado Braze

1. En este ejemplo, la campaña de correo electrónico de promoción de Año Nuevo se creó en [el Paso 3](#step-3-add-translation-tags-to-your-braze-message).

![Braze el correo electrónico con etiquetas de traducción.]({% image_buster /assets/img/smartling/image6_ny_promotion.png %})

{: start="2"}
2\. Después de localizar la campaña que quieres traducir, selecciona la carpeta, elige las variantes y selecciona **Solicitar traducción**.

![Solicita traducciones.]({% image_buster /assets/img/smartling/image7_request_translation.png %})

{: start="3"}
3\. Crea un nuevo trabajo para la traducción.

![Crea un nuevo trabajo para la traducción.]({% image_buster /assets/img/smartling/image8_request_translation.png %})

{: start="4"}
4\. Una vez autorizado el trabajo, edita cada traducción en la herramienta TAO.

![Herramienta TAO de traducción.]({% image_buster /assets/img/smartling/image9_translation_job.png %})

{: start="5"}
5\. Una vez completadas las traducciones, guárdalas y envíalas a Braze.

![Envía la traducción a Braze.]({% image_buster /assets/img/smartling/image10_translations.png %})

### Paso 5: Vista previa del mensaje como usuario multilingüe en Braze

En Braze, obtén una vista previa de tu campaña como usuario multilingüe para confirmar que las traducciones se aplican correctamente.

![Vista previa de usuario en varios idiomas.]({% image_buster /assets/img/smartling/image11_preview.png %})

## Gestionar las traducciones de los bloques de contenido

Los bloques de contenido se gestionan en la sección **Plantillas & Medios de** Braze.

### Traducción almacenada como parte del componente mensaje

Las etiquetas de traducción pertenecen al bloque de contenido. Sin embargo, Smartling ejecuta las traducciones a nivel de mensaje; el contenido sólo se traduce cuando se incluye en una campaña o Canvas y se establece la configuración regional de destino.

### Consideraciones

- Las etiquetas de traducción deben añadirse manualmente al bloque de contenido tanto para los editores HTML como para los editores de arrastrar y soltar bloques de contenido.
- Las localizaciones se seleccionan en el nivel del mensaje, no en los propios bloques de contenido.
- Para Canvas, recomendamos utilizar filas para insertar bloques de contenido en tu mensaje en lugar de añadirlos manualmente con una etiqueta de Liquid. Al arrastrar un Bloque de contenido desde la vista previa a un correo electrónico se hace una copia local; cualquier cambio en el Bloque de contenido "padre" no se propaga a otras campañas que utilicen ese bloque.
- Si utilizas una etiqueta de Liquid de bloque de contenido, asegúrate de incluir al menos una etiqueta de traducción directamente en el cuerpo del correo electrónico. Si añades manualmente la etiqueta de traducción, podrás seleccionar las localizaciones en el desplegable multilingüe. Smartling recoge las etiquetas de traducción del bloque de contenido. Puedes añadir una etiqueta `comment` para que el texto no sea visible para el usuario.

## Gestionar las traducciones mediante el flujo de trabajo heredado

Si prefieres gestionar las traducciones directamente dentro de un bloque de contenido o una plantilla de correo electrónico, consulta las instrucciones heredadas en [la documentación de Smartling.](https://help.smartling.com/hc/en-us/articles/13248577069979-Translating-with-the-Braze-Connector) Este método utiliza un atributo de idioma y la lógica if/else de Liquid para mostrar el texto en distintos idiomas.

## Preguntas más frecuentes

### ¿Son compatibles las etiquetas de traducción con el editor de arrastrar y soltar?

Para el editor de arrastrar y soltar (correo electrónico, bloque de contenido, mensaje dentro de la aplicación), debes añadir manualmente etiquetas de traducción como etiquetas de Liquid.

### ¿Cómo se traduce el texto dentro de una etiqueta de Liquid?

Smartling reconoce las etiquetas de Liquid y las convierte en variables no editables en el compositor. Cualquier otro texto dentro de la etiqueta de Liquid, como el texto predeterminado o filtros como unir, tampoco se puede editar en Smartling. Sin embargo, elimina la etiqueta de Liquid en Smartling y vuelve a crear la etiqueta de Liquid con el texto predeterminado traducido. Aparece una advertencia al guardar la traducción.
