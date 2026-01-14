---
nav_title: Entrega desencadenada por API
article_title: Entrega desencadenada por API
page_order: 2
page_type: reference
description: "Este artículo de referencia describe cómo programar y configurar una campaña desencadenada por la API."
tool: Campaigns
platform: API

---

# Entrega desencadenada por API

> Las campañas desencadenadas por la API o las campañas desencadenadas por el servidor son ideales para casos de uso transaccional más avanzados. Las campañas desencadenadas por la API de Braze permiten a los especialistas en marketing gestionar la copia de la campaña, las pruebas multivariantes y las reglas de reelegibilidad dentro del panel de Braze, a la vez que desencadenan la entrega de ese contenido desde sus propios servidores y sistemas. La solicitud de la API para desencadenar el mensaje también puede incluir datos adicionales que se incorporarán al mensaje en tiempo real.

## Configurar una campaña desencadenada por la API

Configurar una campaña desencadenada por la API requiere unos pocos pasos. Primero, crea una nueva campaña multicanal o monocanal (con pruebas multivariantes).

{% alert note %}
Una campaña desencadenada por la [API]({{site.baseurl}}/developer_guide/rest_api/api_campaigns/#api-campaigns) es diferente de una [campaña API]({{site.baseurl}}/developer_guide/rest_api/api_campaigns/#api-campaigns).
{% endalert %}

A continuación, configura la copia y las notificaciones del mismo modo que lo harías normalmente para las notificaciones programadas y selecciona **Entrega desencadenada por API**. Para obtener más información sobre cómo desencadenar estas campañas desde tu servidor, consulta este artículo sobre [el envío de campañas desencadenadas por la API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/).

\![]({% image_buster /assets/img_archive/api_triggered_campaign_delivery.png %})

## Utilizar el contenido de la plantilla incluido en una solicitud API

Además de desencadenar el mensaje, también puedes incluir contenido con la solicitud de la API para que forme parte de la plantilla del mensaje dentro del objeto `trigger_properties`. Se puede hacer referencia a este contenido en el cuerpo del mensaje. Por ejemplo, puedes incluir:
``{% raw %} {{ api_trigger_properties.${ some_value_included_with_request }}} {% endraw %}``. Consulta el siguiente ejemplo de notificación social para obtener más información:

¡\![La mencionada propiedad desencadenante incluida en el mensaje para autorellenar el nombre del usuario seguido del texto: "¡Me ha gustado tu foto! Haz clic aquí para ver lo que han estado haciendo".]({% image_buster /assets/img_archive/api_triggered_photo_social_example_1.png %}){: style="max-width:70%;"}

## Reelegibilidad con campañas desencadenadas por la API

El número de veces que un usuario recibe una campaña desencadenada por la API puede limitarse utilizando la configuración de reelegibilidad. Esto significa que el usuario recibirá la campaña sólo una vez o una vez en una ventana determinada, independientemente de cuántas veces se desencadene la API.

Por ejemplo, supongamos que utilizas una campaña desencadenada por la API para enviar al usuario una campaña sobre un artículo que ha visto recientemente. En este caso, puedes limitar la campaña para que envíe un máximo de un mensaje al día, independientemente de cuántos artículos hayan visto, mientras disparas el desencadenador de la API para cada artículo. Por otro lado, si tu campaña desencadenada por la API es transaccional, querrás asegurarte de que el usuario recibe la campaña cada vez que realiza la transacción, configurando el retraso a cero minutos.

\![]({% image_buster /assets/img_archive/api_triggered_reeligible.png %})


