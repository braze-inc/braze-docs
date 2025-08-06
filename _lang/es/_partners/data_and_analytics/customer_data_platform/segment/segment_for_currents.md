---
nav_title: Segmento para corrientes
article_title: Segmento para corrientes
page_order: 2
alias: /partners/segment_for_currents/
description: "Este artículo de referencia describe la asociación entre Braze Currents y Segment, una plataforma de datos de clientes que recopila y encamina información entre fuentes de su pila de marketing."
page_type: partner
tool: Currents
search_tag: Partner

---

# Segmento para corrientes  

> [Segment](https://segment.com) es una plataforma de datos de clientes que le ayuda a recopilar, limpiar y activar los datos de sus clientes. Este artículo de referencia ofrecerá una visión general de la conexión entre Braze Currents y Segment y describirá los requisitos y procesos para una implementación y uso adecuados.

La integración de Braze y Segment le permite aprovechar Braze Currents para exportar sus eventos Braze a Segment y obtener análisis más profundos de las conversiones, la retención y el uso del producto. 

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Segment | Se necesita una [cuenta de Segment](https://app.segment.com/login) para beneficiarse de esta asociación. |
| Destino Braze | Ya debe haber [configurado Braze como destino]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/) en su integración de Segment.<br><br>Esto incluye proporcionar el centro de datos Braze y la clave de API REST correctos en tu [configuración de conexión]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings). |
| Currents | Para volver a exportar datos a Segment, debe tener configurado [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) en su cuenta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Obtener la clave de escritura del segmento

En tu panel de Segment, selecciona tu fuente de Segment. A continuación, ve a **Configuración > Claves de API**. Aquí encontrará la **clave de escritura de segmentos**.

{% alert warning %}
Es importante mantener actualizada la clave de escritura de Segment. Si las credenciales de tu conector caducan, el conector dejará de enviar eventos. Si esto persiste durante más de **48 horas**, los eventos del conector se eliminarán y los datos se perderán permanentemente.
{% endalert %}

### Paso 2: Crear un nuevo conector Currents

1. En Braze, vaya a **Integraciones de socios** > **Exportación de datos**.
2. Haga clic en **\+ Crear nueva corriente** > **Exportar datos de segmento**.
3. A continuación, proporciona el nombre de la integración, el correo electrónico de contacto, la clave de escritura del segmento y la región del segmento.

![La página de Corrientes de Segmento en Braze. Aquí puedes encontrar campos para el nombre de la integración, el correo electrónico de contacto, la región del segmento y la clave de API.]({% image_buster /assets/img/segment/segment_currents_integration_config.png %})

### Paso 3: Exportar eventos de compromiso de mensajes

A continuación, seleccione los eventos de compromiso de mensajes que desea exportar. Consulte la siguiente tabla de eventos y propiedades de exportación. Todos los eventos enviados a Segmento incluirán el `external_user_id` del usuario como `userId` y el `braze_id` del usuario como `anonymousId`.

Ten en cuenta que Braze sólo envía datos de eventos de usuarios sin `external_user_id` si está marcada la opción **Incluir eventos de usuarios anónimos**.

{% alert important %}
La exportación de usuarios anónimos está actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en este acceso anticipado.
{% endalert %}

![Lista de todos los eventos de interacción de mensajes disponibles en la página de Segmentos Currents de Braze.]({% image_buster /assets/img/segment/segment_currents_data_config.png %})

Por último, seleccione **Lanzar corriente**.

{% alert warning %}
Si tiene intención de crear más de uno de los mismos conectores Currents (por ejemplo, dos conectores de eventos de compromiso de mensajes), deben estar en espacios de trabajo diferentes. Dado que la integración Braze Segment Currents no puede aislar los eventos de diferentes aplicaciones en un único espacio de trabajo, si no se hace esto, se producirá una desduplicación de datos innecesaria y se perderán datos.
{% endalert %}

Para saber más, visita la [documentación](https://segment.com/docs/connections/sources/catalog/cloud-apps/braze/) de Segment.

## Actualizar su actual

{% multi_lang_include updating_currents.md %}

## Acontecimientos apoyados por Currents

Braze admite la exportación a Segment de los siguientes datos enumerados en los glosarios de [comportamiento del usuario]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) de Currents y de eventos de [participación en mensajes]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/):
 
### Comportamientos
- Desinstalar: `users.behaviors.Uninstall`
- Suscripción (cambio de estado global): `users.behaviors.subscription.GlobalStateChange`
- Grupo de suscripción (cambio de estado): `users.behaviors.subscriptiongroup.StateChange`
  
### Campañas
- Abortar: `users_campaigns_abort`
- Conversión: `users.campaigns.Conversion`
- EnrollinControl: `users.campaigns.EnrollInControl`
  
### Canvas
- Abortar: `users_canvas_abort`
- Conversión: `users.canvas.Conversion`
- Entrada: `users.canvas.Entry`
- Salida (audiencia emparejada, evento realizado)
  - `users.canvas.exit.MatchedAudience`
  - `users.canvas.exit.PerformedEvent`
- Paso del experimento (conversión, entrada dividida)
  - `users.canvas.experimentstep.Conversion`
  - `users.canvas.experimentstep.SplitEntry`

### Mensajes
- Tarjeta de contenido (abortar, hacer clic, descartar, imprimir, enviar)
  - `users.messages.contentcard.Abort`
  - `users.messages.contentcard.Click`
  - `users.messages.contentcard.Dismiss`
  - `users.messages.contentcard.Impression`
  - `users.messages.contentcard.Send`
- Correo electrónico (abortar, rebote, clic, entrega, markasspam, abrir, enviar, softbounce, cancelar suscripción)
  - `users.messages.email.Abort`
  - `users.messages.email.Bounce`
  - `users.messages.email.Click`
  - `users.messages.email.Delivery`
  - `users.messages.email.MarkAsSpam`
  - `users.messages.email.Open`
  - `users.messages.email.Send`
  - `users.messages.email.SoftBounce`
  - `users.messages.email.Unsubscribe`
- Mensaje in-app (abortar, clic, impresión)
  - `users.messages.inappmessage.Abort`
  - `users.messages.inappmessage.Click`
  - `users.messages.inappmessage.Impression`
- Notificación push (abortar, rebotar, iOSforeground, abrir, enviar)
  - `users.messages.pushnotification.Abort`
  - `users.messages.pushnotification.Bounce`
  - `users.messages.pushnotification.IosForeground`
  - `users.messages.pushnotification.Open`
  - `users.messages.pushnotification.Send`
- SMS (abortar, envío de portadora, entrega, fallo de entrega, recepción entrante, rechazo, envío, clic en enlace corto)
  - `users.messages.sms.Abort`
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.InboundReceive`
  - `users.messages.sms.Rejection`
  - `users.messages.sms.Send`
  - `users.messages.sms.ShortLinkClick`
- Webhook (abortar, enviar)
  - `users.messages.webhook.Abort`
  - `users.messages.webhook.Send`
- WhatsApp (abortar, entrega, fallo, recepción entrante, lectura, envío)
  - `users.messages.whatsapp.Abort`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.InboundReceive`
  - `users.messages.whatsapp.Read`
  - `users.messages.whatsapp.Send`

