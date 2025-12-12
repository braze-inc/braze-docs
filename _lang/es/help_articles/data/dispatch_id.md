---
nav_title: Comportamiento del ID de envío
article_title: Comportamiento de la ID de Despacho
page_order: 0

page_type: solution
description: "En este artículo de ayuda se cubre el comportamiento del ID de envío, incluyendo su uso, implicaciones y limitaciones."
---

# Comportamiento del ID de envío

Un `dispatch_id` es el ID del envío del mensaje, un ID único para cada "transmisión" enviada desde Braze. Los usuarios a los que se envía un mensaje programado reciben el mismo `dispatch_id`. Normalmente, los mensajes basados en acciones o desencadenados por la API recibirán un `dispatch_id` único por usuario, pero los mensajes enviados muy cerca de otro pueden compartir el mismo `dispatch_id` entre varios usuarios.

Esto puede dar lugar a que dos usuarios distintos tengan ID de envío diferentes para una misma campaña si los mensajes se enviaron en dos momentos distintos. Esto suele deberse a que las solicitudes a la API se hicieron por separado. Si ambos usuarios estuvieran en la misma audiencia de campaña en un mismo envío, sus ID de envío serían los mismos.

## Comportamiento del ID de envío en las campañas

Los mensajes de campaña programados reciben el mismo `dispatch_id`. Los mensajes de campaña basados en acciones o desencadenados por la API pueden tener un `dispatch_id` único por usuario, o el `dispatch_id` puede ser el mismo para varios usuarios cuando se envían muy cerca o en la misma llamada a la API, como se ha descrito anteriormente. Por ejemplo, dos usuarios de la audiencia de tu campaña programada tendrán el mismo `dispatch_id` cada vez que se programe la campaña. Sin embargo, dos usuarios de la audiencia de una campaña desencadenada por la API pueden tener ID de envío diferentes si se enviaron en llamadas a la API separadas y no muy próximas entre sí.

Las campañas multicanal tendrán el mismo comportamiento que el descrito para su tipo de entrega.

{% alert warning %}
Se genera un `dispatch_id` aleatoriamente para todos los pasos en Canvas porque Braze trata los pasos en Canvas como eventos desencadenados, incluso cuando están "programados". Esto puede dar lugar a incoherencias en la generación de los ID. A veces, un componente Canvas tendrá un único `dispatch_id` por usuario por envío, o puede tener IDs de envío compartidos entre usuarios por envío.
{% endalert %}

## Plantilla del ID de envío en mensajes con Liquid

Si quieres hacer un seguimiento del envío de un mensaje desde dentro del mensaje (en una URL, por ejemplo), puedes utilizar la plantilla `dispatch_id`. Puedes encontrar el formato para esto en Atributos de Canvas en nuestra lista de [etiquetas de personalización admitidas]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

Esto se comporta igual que `api_id`, en el sentido de que como `api_id` no está disponible en el momento de crear la campaña, se incluye en la plantilla como marcador de posición y se previsualizará como `dispatch_id_for_unsent_campaign`. El ID se genera antes de enviar el mensaje, y se incluirá en la hora de envío.

{% alert warning %}
La plantilla Liquid de `dispatch_id_for_unsent_campaign` no funciona con los mensajes dentro de la aplicación, ya que los mensajes dentro de la aplicación no tienen `dispatch_id`.
{% endalert %}

## Campo de ID de envío de Currents para correo electrónico

En un esfuerzo por seguir mejorando nuestras capacidades en Currents, `dispatch_id` también es un campo en los eventos de correo electrónico de Currents en todos los tipos de conectores. El `dispatch_id` es el ID único generado para cada transmisión, o envío, enviado desde la plataforma Braze.

Mientras que todos los clientes a los que se envía un mensaje programado reciben el mismo `dispatch_id`, los clientes que reciben mensajes basados en acciones o desencadenados por la API recibirán un `dispatch_id` único por mensaje. El campo `dispatch_id` te habilita para identificar qué instancia de una campaña recurrente es responsable de la conversión, dotándote así de más información sobre qué tipos de campañas están ayudando a empujar la aguja de tus objetivos de negocio.

Puedes utilizar `dispatch_id` como [etiqueta de personalización]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags), en [eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) o cuando utilices [Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/#integration-details), [Mixpanel]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/#email-events) o [Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_for_currents/) para Currents.

_Última actualización el 15 de julio de 2021_
