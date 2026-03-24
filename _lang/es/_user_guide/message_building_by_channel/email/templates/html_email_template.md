---
nav_title: Subir una plantilla de correo electrónico HTML
article_title: Subir una plantilla de correo electrónico HTML
page_order: 2
description: "Este artículo de referencia explica cómo crear, administrar y solucionar problemas de una plantilla de correo electrónico HTML mediante el dashboard de Braze."
tool:
  - Templates
channel:
  - email

---

# Subir una plantilla de correo electrónico HTML

> El dashboard de Braze te permite cargar tus propias plantillas de correo electrónico HTML y guardarlas para utilizarlas posteriormente en campañas. También puedes [crear una plantilla de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template/) utilizando nuestro editor.

## Requisitos previos {#upload-requirements}

En primer lugar, tendrás que crear tu plantilla de correo electrónico HTML. Debe ser un archivo ZIP que contenga lo siguiente:

* Un único archivo HTML: el cuerpo del correo electrónico
* Una carpeta de imágenes a las que se hace referencia en el archivo HTML
* Menos de 50 archivos de imagen
* Un tamaño inferior a 5&nbsp;MB

## Cargar tu plantilla

### Paso 1: Ve al editor de plantillas de correo electrónico

Ve a **Plantillas** > **Plantillas de correo electrónico**.

### Paso 2: Abre el cargador

En la sección **Tipo de plantilla**, selecciona **Editor HTML** y desplázate hacia abajo hasta la sección **Empezar desde una plantilla HTML básica**. Selecciona **De archivo**.

### Paso 3: Sube tu plantilla

Selecciona **Cargar desde archivo** y selecciona la plantilla de tu computadora. Consulta la sección [Requisitos previos](#upload-requirements) para asegurarte de que tu plantilla cumple los requisitos de carga.

### Paso 4: Finaliza y guarda tu plantilla

Asegúrate de guardar tu plantilla seleccionando **Guardar plantilla**. ¡Ya puedes utilizar esta plantilla en cualquier campaña o Canvas que elijas!

{% alert note %}
Si modificas una plantilla existente, los cambios no se reflejarán en las campañas creadas con versiones anteriores de esa plantilla.
{% endalert %}

## Uso de tus plantillas en campañas de API {#api_for_upload_email_templates}

Para utilizar tu correo electrónico en una campaña de API, necesitas el `email_template_id`, que se encuentra en la parte inferior de cualquier plantilla de correo electrónico creada en Braze.

![Sección del identificador de API de una plantilla de correo electrónico HTML.]({% image_buster /assets/img_archive/email_template_id.png %}){: style="max-width:50%;"}

## Administrar plantillas de correo electrónico

Puedes [duplicar]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) y [archivar]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) plantillas de correo electrónico. Obtén más información sobre la creación y administración de plantillas y contenido creativo en [Plantillas]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

## Solución de problemas

Hay varios mensajes de error de correo electrónico que puedes recibir al cargar un archivo de plantilla HTML. Si recibes un error, consulta la siguiente tabla para ver los problemas más comunes y las soluciones recomendadas:

| Error | Solución |
|------|---|
|`.zip over 5&nbsp;MB`| Reduce el tamaño del archivo e intenta cargarlo de nuevo.|
|`.zip corrupt`| Inspecciona tu archivo e intenta cargarlo de nuevo. |
|`Missing HTML`| Añade el archivo HTML a tu archivo ZIP e intenta cargarlo de nuevo.|
|`Multiple HTML`| Elimina uno de los archivos HTML e intenta cargarlo de nuevo.|
|`Images over 5&nbsp;MB`| Reduce el número de imágenes e intenta cargarlas de nuevo. |
|`Extra Images`| Puede haber imágenes adicionales en tu archivo que no estén referenciadas en tu archivo HTML. Esto no provocará un error de fallo, pero se descartarán las imágenes sobrantes. Si esas imágenes debían estar referenciadas en el archivo HTML, comprueba el contenido, corrige los errores e intenta cargarlas de nuevo.|
|`Missing Images`| Si hay imágenes referenciadas en tu archivo HTML, pero esas imágenes no están incluidas en la carpeta de imágenes del archivo ZIP, recibirás un error de archivo. Inspecciona tu archivo y corrige cualquier error (como faltas de ortografía), o añade las imágenes que faltan a tu archivo ZIP e intenta cargarlo de nuevo.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Ten en cuenta que al descargar los archivos de campañas HTML, pasos en Canvas con mensajes de correo electrónico o plantillas en una máquina Windows, el carácter `|` (barra vertical) no es compatible, por lo que es posible que necesites usar una aplicación diferente para extraer el contenido descargado del archivo ZIP.

## Preguntas frecuentes

Para obtener respuestas a las preguntas más frecuentes sobre plantillas de correo electrónico, consulta nuestra página de [preguntas frecuentes sobre plantillas de correo electrónico y enlaces]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/).