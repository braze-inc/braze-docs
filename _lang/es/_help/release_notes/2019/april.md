---
nav_title: Abril
page_order: 9
noindex: true
page_type: update
description: "Este artículo contiene notas de la versión de abril de 2019."
---

# Abril de 2019

## Eventos y campos de New Currents

Además de algunas correcciones en la sección, se ha añadido un nuevo [Evento de suscripción]({{ site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/#subscription-events) a la página de Eventos de interacción de mensajes. 

Ahora puedes exportar los datos de cambio de estado del grupo de suscripción de Braze a [Segmentar]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/#integration-details) y [mParticle]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mParticle/mparticle_for_currents/), así como los Eventos de atribución de instalación y eso en [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/).

Además, se ha añadido la propiedad `canvas_step_id` a los [Eventos de conversión]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/#conversion-events) disponibles.

{% alert important %}
Para aprovechar estas actualizaciones, tendrás que editar la configuración de tu conector Currents y habilitar los eventos que quieras utilizar. Ponte en contacto con tu director de cuentas si tienes alguna pregunta.
{% endalert %}

## Archivo de grupos de suscripción

¡Ahora puedes [archivar Grupos de suscripción]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#archiving-groups)! Los Grupos de suscripción archivados no se pueden editar y ya no aparecerán en los Filtros de segmentos.  Si intentas archivar un grupo que se está utilizando como filtro de segmento en cualquier correo electrónico, campaña o Canvas, recibirás un mensaje de error que te impedirá archivar el grupo hasta que elimines todos sus usos.
