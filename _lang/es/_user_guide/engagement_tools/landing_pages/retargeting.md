---
nav_title: Reorientar a los usuarios
article_title: Reorientar a los usuarios a través de una página de destino
description: "Aprende a reorientar a los usuarios que han enviado un formulario a través de una página de destino."
page_order: 3
---

# Reorientar a los usuarios a través de una página de destino

> Aprende a reorientar a los usuarios que han enviado un formulario a través de una página de destino creando un segmento dedicado o desencadenando un mensaje cuando se envía el formulario.

## Requisitos previos

Antes de empezar, tendrás que crear una [página de aterrizaje]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/).

## Reorientar usuarios

Braze realiza un seguimiento automático cuando un usuario envía un formulario de página de destino. Puedes ver el número total de envíos de un formulario en el [análisis de la página de destino]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#viewing-analytics). Sin embargo, para reorientar a usuarios específicos, tendrás que reorientar a los usuarios a través del formulario de tu página de destino utilizando uno de los siguientes métodos:

- **Utilizando un segmento:** Puedes crear un nuevo segmento para identificar automáticamente a los usuarios que han enviado o no un formulario de la página de destino.
- **Utilizando un desencadenador de mensajes:** Puedes configurar un desencadenador de mensajes para enviar automáticamente mensajes a los usuarios o introducirlos en un Canvas después de que envíen el formulario.

{% tabs local %}
{% tab Utilizar un segmento %}
Cuando [crees un segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), en el grupo "Reorientación", elige **Formulario de envío en la página de destino**.

![Creación de segmento con el grupo de filtrado seleccionado como "Formulario enviado en la página de destino"]({% image_buster /assets/img/landing_pages/segmentation_selected.png %})

Desde aquí, puedes segmentar a los usuarios en función de si han enviado o no un formulario para tu página de destino.
{% endtab %}

{% tab Utilizar un desencadenador de mensajes %}
Cuando elijas la opción de entrega para tu [campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/) o [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/), selecciona **Entrega basada en acciones** y, a continuación, **el formulario Página de destino enviada**.

Todos los usuarios que envíen un formulario a través de este formulario de la página de destino recibirán un mensaje a través del canal de mensajería elegido o entrarán en el Canvas elegido.

![Acción desencadenante de página de destino en mensajería]({% image_buster /assets/img/landing_pages/trigger.png %})
{% endtab %}
{% endtabs %}
