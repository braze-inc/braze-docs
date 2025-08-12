---
nav_title: IAM Studio
article_title: IAM Studio
description: "Este artículo de referencia describe la asociación entre Braze e IAM Studio, una plataforma de personalización de mensajes que permite crear experiencias personalizadas y enriquecidas dentro de la aplicación y ofrecerlas a través de Braze."
alias: /partners/iam_studio/
page_type: partner
search_tag: Partner

---

# IAM Studio

> [IAM Studio](https://www.inappmessage.com) es una plataforma de personalización de mensajes sin código que permite crear experiencias personalizadas y enriquecidas dentro de la aplicación y ofrecerlas a través de Braze.

_Esta integración está mantenida por IAM Studio.\*s._

## Sobre la integración

Con la integración de Braze e IAM Studio, puedes insertar fácilmente plantillas de mensajes personalizables en tus mensajes Braze dentro de la aplicación, que ofrecen sustitución de imágenes, modificación de texto, configuración de enlaces profundos, atributos personalizados y configuración de eventos. Con IAM Studio, puedes reducir el tiempo de producción de mensajes y dedicar más tiempo a la planificación de contenidos. 

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta IAM Studio | Se necesita una [cuenta IAM Studio](https://www.inappmessage.com/register) para beneficiarse de esta asociación. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Casos prácticos

- Fomentar la compra de bienes
- Recogida de información de los usuarios
- Aumentar la inscripción de miembros
- Información sobre la emisión de cupones

## Integración

### Paso 1: Elegir una plantilla

Elige una plantilla de mensaje para la aplicación que quieras utilizar de la galería de plantillas de mensajes para la aplicación.

![La galería de plantillas de IAM Studio muestra diferentes plantillas como "modal carrusel de diapositivas", "modal icono simple", "modal imagen completa", y más.]({% image_buster /assets/img/iam_studio/iam_template_gallery.png %})

### Paso 2: Personalizar la plantilla

En primer lugar, personaliza la imagen, el texto y el botón para tu contenido. Asegúrate de conectar **Deeplink** para la imagen y el botón.

{% tabs local %}
{% tab Imagen %}
![La interfaz de usuario de IAM Studio muestra las opciones para personalizar la imagen. Estas opciones incluyen la imagen, el radio de la imagen y la atenuación de la imagen.]({% image_buster /assets/img/iam_studio/iam_customize_image.png %})
{% endtab %}
{% tab Texto %}
![La interfaz de usuario de IAM Studio muestra las opciones para personalizar el título y el subtítulo del mensaje. Estas opciones incluyen texto, formato y fuente.]({% image_buster /assets/img/iam_studio/iam_customize_text.png %})
{% endtab %}
{% tab Botón %}
![La interfaz de usuario de IAM Studio muestra las opciones para personalizar el botón principal, izquierdo y derecho. Estas opciones incluyen el color, el vínculo profundo, el texto y el formato.]({% image_buster /assets/img/iam_studio/iam_customize_button.png %})
{% endtab %}
{% endtabs %}

A continuación, crea tu mensaje personalizado en la aplicación añadiendo fuentes personalizadas y utilizando etiquetas Liquid. Para habilitar el registro y el seguimiento, selecciona **Registrar datos y realizar un seguimiento del comportamiento del usuario**.

{% tabs local %}
{% tab Fuentes %}
![La interfaz de usuario de IAM Studio muestra las opciones para añadir Liquid. Estas opciones incluyen la realización de frases personalizadas.]({% image_buster /assets/img/iam_studio/iam_custom_font.png %})
{% endtab %}
{% tab Líquido %}
![La interfaz de usuario de IAM Studio muestra las opciones para personalizar el registro de eventos/atributos. Estas opciones incluyen que el registro de comportamiento del usuario.]({% image_buster /assets/img/iam_studio/iam_liquid.png %})
{% endtab %}
{% tab Registro y seguimiento %}
![La interfaz de usuario de IAM Studio muestra las opciones para personalizar la fuente. Estas opciones incluyen que el usuario puede personalizar el estilo de la fuente.]({% image_buster /assets/img/iam_studio/iam_tracking_logging.png  %})
{% endtab %}
{% endtabs %}

### Paso 3: Exportar la plantilla

Una vez finalizada la edición, exporta la plantilla haciendo clic en **Exportar**. Tras la exportación, se generará el código HTML del mensaje dentro de la aplicación. Copia este código haciendo clic en el botón **Copiar código**. 

![]({% image_buster /assets/img/iam_studio/export_iam_code.png %}){: style="max-width:45%;"}

### Paso 4: Utilizar código en Braze 

Ve a Braze y, en el mensaje de la aplicación, pega el código personalizado en el cuadro de **entrada HTML**. Asegúrate de probar tu mensaje para comprobar que se muestra correctamente.

![]({% image_buster /assets/img/iam_studio/braze_campaign_editor.png %}){: style="max-width:85%;"}


