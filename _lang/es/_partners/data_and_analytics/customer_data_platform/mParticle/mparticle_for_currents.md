---
nav_title: mParticle para Currents
article_title: mParticle para Currents
alias: /partners/mparticle_for_currents/
description: "Este artículo de referencia describe la asociación entre Braze Currents y mParticle, una plataforma de datos de los clientes que recopila y encamina información entre las fuentes de tu pila de marketing."
page_type: partner
tool: Currents
search_tag: Partner

---

# mParticle para Currents

> [mParticle](https://www.mparticle.com) es una plataforma de datos de los clientes que recopila y encamina información de múltiples fuentes a una variedad de otras ubicaciones en tu stack de marketing.

La integración de Braze y mParticle te permite controlar fácilmente el flujo de información entre ambos sistemas. Con [Currents]({{site.baseurl}}/user_guide/data/braze_currents/), también puedes conectar los datos a mParticle para que sean procesables en todo el stack de crecimiento. 

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Currents | Para volver a exportar datos a mParticle, debes tener configurado [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) en tu cuenta. |
| Cuenta mParticle | Se necesita una [cuenta mParticle](https://app.mparticle.com/login) para beneficiarse de esta asociación. |
| Clave y secreto mParticle de servidor a servidor | Se pueden obtener navegando hasta tu panel de control de mParticle y creando las [fuentes necesarias](#step-1-create-feeds) que permitan a mParticle recibir datos de interacción Braze para las plataformas iOS, Android y Web.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Acerca de las credenciales mParticle

mParticle tiene credenciales a nivel de aplicación y a nivel de espacio de trabajo que afectan al modo en que se envían tus eventos.

- Nivel de **aplicación:** mParticle separará los eventos por cada aplicación individual, lo que significa que las credenciales de nivel de aplicación que des a tu aplicación de iOS sólo pueden utilizarse para enviar eventos específicos de iOS.
- A nivel de espacio **de trabajo:** mParticle agrupa todos los eventos (que **no** son específicos de una aplicación), lo que significa que las credenciales a nivel de espacio de trabajo que des a tu grupo de aplicaciones se utilizarán para enviar todos tus eventos no específicos de una aplicación.

Puedes pensar en esto como si mParticle ingiriera una "fuente" basada en cada aplicación individual. Por ejemplo, si tienes una aplicación para iOS, otra para Android y otra para Web, tus eventos estarán desarticulados. Esto significa que si proporcionas las mismas credenciales para cada aplicación, se utilizará una fuente mParticle para recibir todos los datos de todas tus aplicaciones, sin duplicación.

## Integración

### Paso 1: Crear fuentes

Desde tu cuenta de administrador de mParticle, ve a **Configuración > Entradas**. Localiza **Braze** en el **Directorio** mParticle y añade la integración de la fuente.

La integración de la fuente Braze admite cuatro fuentes distintas: iOS, Android, Web y Unbound. La fuente no vinculada puede utilizarse para eventos como correos electrónicos que no están conectados a una plataforma. Tendrás que crear una entrada para cada fuente de la plataforma principal. Puedes crear entradas adicionales desde **Configuración > Entradas**, en la pestaña **Configuraciones de la fuente**.

![]({% image_buster /assets/img/braze-feed-inputs.png %})

Para cada fuente, en **Actuar como plataforma** selecciona la plataforma correspondiente de la lista. Si no ves una opción para seleccionar una fuente **act-as**, los datos se tratarán como no enlazados, pero aún pueden reenviarse a las salidas del almacén de datos.

![El primer cuadro de diálogo de integración, que te pide que proporciones un nombre de configuración, determines un estado de la fuente y selecciones una plataforma para actuar como.]({% image_buster /assets/img/braze-feed-act1.png %}){: style="max-width:40%;"}  ![El segundo cuadro de diálogo de integración que muestra la clave de servidor a servidor y el secreto de servidor a servidor.]({% image_buster /assets/img/braze-feed-act2.png %}){: style="max-width:37%;"}

Al crear cada entrada, mParticle te proporcionará una clave y un secreto. Copia estas credenciales, asegurándote de anotar para qué fuente es cada par de credenciales.

### Paso 2: Crear Current

En Braze, ve a **Currents > + Crear corriente > Crear exportación de mParticle**. Proporciona un nombre de integración, un correo electrónico de contacto y la clave de API de mParticle y la clave secreta de mParticle para cada plataforma. A continuación, selecciona los eventos de los que quieres hacer un seguimiento; se proporciona una lista de los eventos disponibles. Por último, haz clic en **Lanzar Current**

![La página de las mParticle Currents en Braze. Aquí puedes encontrar campos para el nombre de la integración, el correo electrónico de contacto, la clave de API y la clave secreta.]({% image_buster /assets/img_archive/currents-mparticle-edit.png %})

{% alert important %}
Es importante que mantengas actualizadas tu clave API y tu clave secreta mParticle; si las credenciales de tu conector caducan, el conector dejará de enviar eventos. Si esto persiste durante más de **48 horas**, los eventos del conector se eliminarán y los datos se perderán permanentemente.
{% endalert %}

Todos los eventos enviados a mParticle incluirán la dirección `external_user_id` del usuario como `customerid`. En este momento, Braze no envía datos de eventos para los usuarios que no tienen configurado su `external_user_id`. Si quieres mapear el `external_user_id` a un ID diferente en mParticle que no sea el predeterminado `customerid`, ponte en contacto con tu CSM de Braze. 

## Eventos Currents compatibles

Braze admite la exportación a mParticle de los siguientes datos enumerados en los glosarios de [comportamiento de usuario]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) e [interacción con mensajes de]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) Currents:

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
- Mensaje in-app (abortar, clic, impresión)
  - `users.messages.inappmessage.Abort`
  - `users.messages.inappmessage.Click`
  - `users.messages.inappmessage.Impression`
- Notificación push (anular, rebotar, abrir, enviar)
  - `users.messages.pushnotification.Abort`
  - `users.messages.pushnotification.Bounce`
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


Para saber más sobre la integración de mParticle, visita su documentación [aquí](http://docs.mparticle.com/integrations/braze/feed).

