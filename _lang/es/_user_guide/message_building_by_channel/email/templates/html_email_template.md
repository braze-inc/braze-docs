---
nav_title: Cargar una plantilla de correo electrónico HTML
article_title: Cargar una plantilla de correo electrónico HTML
page_order: 2
description: "Este artículo de referencia explica cómo crear, gestionar y solucionar problemas de una plantilla de correo electrónico HTML utilizando el panel de Braze."
tool:
  - Templates
channel:
  - email

---

# Cargar una plantilla de correo electrónico HTML

> El panel de Braze te permite subir tus propias plantillas de correo electrónico HTML y guardarlas para utilizarlas posteriormente en campañas. También puedes [crear una plantilla de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template/) utilizando nuestro editor.

## Requisitos previos {#upload-requirements}

En primer lugar, tendrás que crear tu plantilla de correo electrónico HTML. Debe ser un archivo ZIP que contenga lo siguiente:

* Un único archivo HTML: el cuerpo de tu correo electrónico
* Una carpeta de imágenes a las que se hace referencia en el archivo HTML
* Menos de 50 archivos de imagen
* Ser inferior a 5 MB

## Cargar tu plantilla

### Paso 1: Navega hasta el editor de plantillas de correo electrónico

Ve a **Plantillas** > **Plantillas de correo electrónico**.

### Paso 2: Abre el cargador

En la sección **Tipo de plantilla**, selecciona **Editor HTML** y desplázate hacia abajo hasta la sección **Empezar desde una plantilla HTML básica**. Selecciona **Desde Archivo**.

### Paso 3: Sube tu plantilla

Selecciona **Cargar desde archivo** y selecciona la plantilla de tu computadora. Consulta la sección [Requisitos previos](#upload-requirements) para asegurarte de que tu plantilla cumple los requisitos de carga.

#### Solución de problemas de errores de carga de plantillas

Hay varios mensajes de error por correo electrónico que puedes recibir al cargar un archivo de plantilla HTML. Si recibes un error, consulta la siguiente tabla para ver los problemas más comunes y sus soluciones recomendadas:

| Error | Arregla |
|------|---|
|.zip de más de 5 MB| Reduce el tamaño del archivo e intenta subirlo de nuevo.|
|.zip corrupto| Inspecciona tu archivo e intenta subirlo de nuevo. |
|Falta HTML| Añade el archivo HTML a tu archivo ZIP e intenta subirlo de nuevo.|
|HTML múltiple| Elimina uno de los archivos HTML e intenta subirlo de nuevo.|
|Imágenes de más de 5 MB| Reduce el número de imágenes e intenta subirlas de nuevo. |
|Imágenes adicionales| Puede haber imágenes adicionales en tu archivo que no estén referenciadas en tu archivo HTML. Esto no provocará un error de fallo, pero se descartarán las imágenes sobrantes. Si esas imágenes debían estar referenciadas en el archivo HTML, comprueba el contenido, corrige los errores e intenta subirlas de nuevo.|
|Imágenes desaparecidas| Si hay imágenes a las que se hace referencia en tu archivo HTML, pero esas imágenes no están incluidas en la carpeta de imágenes del archivo ZIP, recibirás un error de archivo. Inspecciona tu archivo y corrige cualquier error (como faltas de ortografía), o añade las imágenes que faltan a tu archivo ZIP e intenta subirlas de nuevo.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Paso 4: Termina y guarda tu plantilla

Asegúrate de guardar tu plantilla seleccionando **Guardar plantilla**. Ya puedes utilizar esta plantilla en cualquier campaña o Canvas que elijas.

{% alert note %}
Si realizas modificaciones en una plantilla existente, esos cambios no se reflejarán en las campañas creadas con versiones anteriores de esa plantilla.
{% endalert %}

## Utilizar tus plantillas en campañas API {#api_for_upload_email_templates}

Para utilizar tu correo electrónico en una campaña API, necesitas la dirección `email_template_id`, que se encuentra en la parte inferior de cualquier plantilla de correo electrónico creada en Braze.

\![Sección del identificador API de una plantilla HTML de correo electrónico.]({% image_buster /assets/img_archive/email_template_id.png %}){: style="max-width:50%;"}

## Gestión de plantillas de correo electrónico

¡Puedes [duplicar]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) y [archivar]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) plantillas de correo electrónico! Obtén más información sobre cómo crear y administrar plantillas y contenido creativo en [Plantillas]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

## Preguntas más frecuentes

Para obtener respuestas a las preguntas más frecuentes sobre plantillas de correo electrónico, consulta nuestra página [de preguntas frecuentes sobre plantillas de correo electrónico y enlaces]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/).


