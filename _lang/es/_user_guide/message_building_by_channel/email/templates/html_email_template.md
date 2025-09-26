---
nav_title: Cargar una plantilla de correo electrónico HTML
article_title: Cargar una plantilla de correo electrónico HTML
page_order: 2
description: "Este artículo de referencia explica cómo crear, gestionar y solucionar problemas de una plantilla de correo electrónico HTML mediante el panel de control de Braze."
tool:
  - Templates
channel:
  - email

---

# Cargar una plantilla de correo electrónico HTML

> El panel de control de Braze le permite cargar sus propias plantillas de correo electrónico HTML y guardarlas para utilizarlas posteriormente en campañas. También puede [crear una plantilla de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template/) utilizando nuestro editor.

## Requisitos previos {#upload-requirements}

En primer lugar, tendrás que crear tu plantilla de correo electrónico HTML. Debe ser un archivo ZIP que contenga lo siguiente:

* Un único archivo HTML: el cuerpo del mensaje
* Una carpeta de imágenes a las que se hace referencia en el archivo HTML
* Menos de 50 archivos de imagen
* Ser inferior a 5 MB

## Cargar la plantilla

### Paso 1: Vaya al editor de plantillas de correo electrónico

Vaya a **Plantillas** > **Plantillas de correo electrónico**.

### Paso 2: Abre el cargador

En la sección **Tipo de plantilla**, seleccione **Editor HTML** y desplácese hacia abajo hasta la sección **Empezar desde una plantilla HTML básica**. Seleccione **De archivo**.

### Paso 3: Sube tu plantilla

Selecciona **Cargar desde archivo** y selecciona la plantilla de tu computadora. Consulte la sección [Requisitos previos](#upload-requirements) para asegurarse de que su plantilla cumple los requisitos de carga.

#### Solucionar errores de carga de plantillas

Hay varios mensajes de error de correo electrónico que puede recibir al cargar un archivo de plantilla HTML. Si recibe un error, consulte la siguiente tabla para ver los problemas más comunes y las soluciones recomendadas:

| Error | Arregla |
|------|---|
|.zip de más de 5 MB| Reduzca el tamaño del archivo e intente cargarlo de nuevo.|
|el .zip corrupto| Inspeccione su archivo e intente subirlo de nuevo. |
|Falta el archivo HTML| Añade el archivo HTML a tu archivo ZIP e intenta subirlo de nuevo.|
|HTML múltiple| Elimine uno de los archivos HTML e intente cargarlo de nuevo.|
|Imágenes de más de 5 MB| Reduzca el número de imágenes e intente cargarlas de nuevo. |
|Imágenes adicionales| Puede haber imágenes adicionales en su archivo que no estén referenciadas en su archivo HTML. Esto no provocará un error de fallo, pero se descartarán las imágenes sobrantes. Si esas imágenes debían estar referenciadas en el archivo HTML, compruebe el contenido, corrija los errores e intente subirlas de nuevo.|
|Imágenes perdidas| Si hay imágenes referenciadas en su archivo HTML, pero esas imágenes no están incluidas en la carpeta de imágenes del archivo ZIP, recibirá un error de archivo. Inspeccione su archivo y corrija cualquier error (como faltas de ortografía), o añada las imágenes que faltan a su archivo ZIP e intente subirlas de nuevo.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Paso 4: Finaliza y guarda tu plantilla

Asegúrate de guardar tu plantilla seleccionando **Guardar plantilla**. Ya puedes utilizar esta plantilla en cualquier campaña o lienzo que elijas.

{% alert note %}
Si modifica una plantilla existente, los cambios no se reflejarán en las campañas creadas con versiones anteriores de esa plantilla.
{% endalert %}

## Utilización de sus plantillas en campañas API {#api_for_upload_email_templates}

Para utilizar su correo electrónico en una campaña API, necesita la dirección `email_template_id`, que se encuentra en la parte inferior de cualquier plantilla de correo electrónico creada en Braze.

![Sección del identificador API de una plantilla de correo electrónico HTML.]({% image_buster /assets/img_archive/email_template_id.png %}){: style="max-width:50%;"}

## Gestión de plantillas de correo electrónico

Puede [duplicar]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) y [archivar]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) plantillas de correo electrónico. Más información sobre la creación y gestión de plantillas y contenido creativo en [Plantillas]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

## Preguntas más frecuentes

Para obtener respuestas a las preguntas más frecuentes sobre plantillas de correo electrónico, consulta nuestra página [de preguntas frecuentes sobre plantillas de correo electrónico y enlaces]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/).


