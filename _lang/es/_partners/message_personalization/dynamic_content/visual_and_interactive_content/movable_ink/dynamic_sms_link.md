---
nav_title: Vista previa del enlace SMS dinámico
article_title: Vista previa del enlace SMS dinámico
description: "Este artículo de referencia describe cómo activar y utilizar la característica de vista previa de enlaces SMS de Movable Ink."
page_type: partner
search_tag: Partner
---

# Vista previa del enlace SMS dinámico

> Con la vista previa dinámica de enlaces SMS de Movable Ink, puedes aprovechar la inmersión de los MMS al mismo coste que los SMS. Esto te permite utilizar Braze y Movable Ink para entregar experiencias de mensajería enriquecida rentables y personalizadas.

## Requisitos previos

| Requisito | Descripción |
| --- | --- |
| Cuenta Movable Ink | Se necesita una cuenta Movable Ink para beneficiarse de esta asociación. |
| Origen de datos | Necesitas conectar un origen de datos a Movable Ink. Esto puede hacerse mediante CSV, importación del sitio web o API. |
| Capacidad de envío de MMS | Confirma que estás configurado para MMS a través de Braze.
| [Acortamiento de enlaces]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/) | Confirma que el acortamiento de enlaces está activado. | 
| Tarjeta de contacto | Tu marca (el remitente) debe estar guardada como contacto en el teléfono del usuario para que la vista previa del enlace funcione con iOS. Esto puede hacerse con una tarjeta de contacto u otro método. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

Sigue los pasos que se indican a continuación para enviar enlaces SMS dinámicos para los sistemas operativos iOS y Android.

### iOS

{% alert important %}
Para permitir imágenes de vista previa de enlaces para iOS, los usuarios deben añadir tu marca (el remitente) como contacto.
{% endalert %}

#### Paso 1: Crea una campaña de tarjetas de contacto

Después de que los usuarios guarden tu marca como contacto, ya sea a través de una [tarjeta de contacto]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/contact_card/) o de otro método, podrán ver las indicaciones de **Tocar para cargar vista previa** y los enlaces de Movable Ink.

![1]{: style="max-width:30%;"}

#### Paso 2: Enviar enlaces de Movable Ink

1. Crea una campaña SMS en Movable Ink y genera tu URL click-through.
2. En el panel de Braze, ve a **Campañas** y configura una nueva campaña SMS/MMS desde el desplegable **Crear campaña**.
3. En el creador de campañas SMS:
    - Configura tu grupo de suscripción.
    - Introduce tu mensaje.
    - Añade tu enlace Movable Ink **en último lugar**, después del resto del texto del cuerpo del mensaje. <br><br>![2]{: style="max-width:50%;"}

{% alert tip %}
Echa un vistazo a [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) para conocer la personalización de Liquid.  
{% endalert %}

{: start="4"}
4\. Ya estás listo para probar y lanzar tu campaña de vista previa de enlaces SMS dinámicos.

![3]{: style="max-width:70%;"}

Cuando los usuarios carguen la vista previa del enlace, se mostrará una imagen personalizada con la posibilidad de enlazar con tu sitio web, aplicación o página de destino.

![4]{: style="max-width:30%;"}

### Android (dispositivos Google y Samsung)

Los usuarios de Android no están obligados a guardar tu marca como contacto para recibir vistas previas de enlaces SMS dinámicos. Sin embargo, sigue siendo recomendable para que el dispositivo pueda cargar automáticamente las vistas previas de los enlaces.

![5]{: style="max-width:30%;"}

Los usuarios que no hayan guardado tu marca como contacto y hayan activado las vistas previas automáticas tendrán que seleccionar **Tocar para cargar vista previa** para cargar la imagen de vista previa.

![6]{: style="max-width:30%;"}

## Consideraciones

- Incluye sólo un enlace de vista previa en tu mensaje. No se generarán contenidos con varios enlaces en el cuerpo de tu SMS. 
- No incluyas ningún carácter después de tu enlace de vista previa o la experiencia podría romperse.


[1]: {% image_buster /assets/img/movable_ink/ios_link.png %}
[2]: {% image_buster /assets/img/movable_ink/ios_message.png %}
[3]: {% image_buster /assets/img/movable_ink/ios_test_launch.png %}
[4]: {% image_buster /assets/img/movable_ink/ios_example.png %}
[5]: {% image_buster /assets/img/movable_ink/android_automatic.png %}
[6]: {% image_buster /assets/img/movable_ink/android_tap.png %}
