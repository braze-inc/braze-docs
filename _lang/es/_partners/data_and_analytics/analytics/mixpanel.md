---
nav_title: Mixpanel
article_title: Mixpanel
alias: /partners/mixpanel/
description: "Este artículo de referencia describe la asociación entre Braze y Mixpanel, una plataforma de análisis empresarial, que te permite importar cohortes de Mixpanel a Braze para crear segmentos Braze que pueden utilizarse para segmentar usuarios en futuras campañas o Canvas de Braze."
page_type: partner
search_tag: Partner
tool: Currents

---
 
# [![Curso de Braze Learning] ({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/mixpanel-integration-with-braze/339085/scorm/2u7y2e6qrldh2){: style="float:right;width:120px;border:0;" class="noimgborder"}Mixpanel

> [Mixpanel](https://mixpanel.com/) es una plataforma de análisis empresarial que te permite exportar eventos de Mixpanel a otras plataformas para realizar análisis más profundos. Los datos recopilados pueden utilizarse para elaborar informes personalizados y medir la interacción con los usuarios y su retención.

La integración de Braze y Mixpanel te permite [importar cohortes de Mixpanel a Braze]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/mixpanel_cohort_import/) para crear segmentos Braze que pueden utilizarse para dirigirse a usuarios en futuras campañas Braze o Canvases. También puedes aprovechar Braze Currents para [exportar tus eventos de Braze a Mixpanel](#data-export-integration) y obtener análisis más profundos de las conversiones, la retención y el uso del producto. 

## Requisitos previos

| Requisito | Descripción |
|---|---|
| Cuenta Mixpanel | Se requiere una [cuenta de Mixpanel](https://mixpanel.com/) para beneficiarse de esta asociación. |
| Currents | Para volver a exportar datos a Mixpanel, debes tener configurado [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) en tu cuenta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## Integración de exportación de datos

A continuación encontrarás una lista completa de los eventos que se pueden exportar de Braze a Mixpanel. Todos los eventos enviados a Mixpanel incluirán la dirección `external_user_id` del usuario como ID distintivo de Mixpanel. En este momento, Braze no envía datos de eventos para los usuarios que no tienen configurado su `external_user_id`.

Puedes exportar dos tipos de eventos a Mixpanel: Eventos de [interacción con los mensajes](#supported-currents-events), que consisten en los Eventos Braze directamente relacionados con el envío de mensajes, y [Eventos de comportamiento del cliente](#supported-currents-events), que incluyen otras actividades de la aplicación o del sitio web, como sesiones, eventos personalizados y compras rastreadas a través de la plataforma. Todos los eventos personalizados llevan el prefijo `[Braze Custom Event]`. Las propiedades del evento personalizado y las propiedades de la compra llevan como prefijo `[Custom event property]` y `[Purchase property]`, respectivamente.

Ponte en contacto con tu director de cuentas o abre un [ticket de soporte]({{site.baseurl}}/braze_support/) si necesitas acceder a derechos de eventos adicionales.

### Paso 1: Obtener credenciales de Mixpanel

En tu panel de Mixpanel, haz clic en **Configuración del proyecto** en un proyecto nuevo o existente. Aquí encontrarás el secreto de la API de Mixpanel y el token de Mixpanel. Estas credenciales se utilizarán en el siguiente paso para crear tu conexión Currents. 

### Paso 2: Crear Braze Currents

En Braze, ve a \*\*Currents > **\+ Crear Current** > **Crear Exportación Mixpanel**. Proporciona un nombre de integración, correo electrónico de contacto, secreto de API de Mixpanel y token de Mixpanel en los campos de la lista. A continuación, selecciona los eventos de los que quieres hacer un seguimiento; se proporciona una lista de los eventos disponibles. Por último, haz clic en **Lanzar Current**.

![La página Braze Mixpanel Currents. Esta página incluye campos para el nombre de la integración, el correo electrónico de contacto, el secreto de la API y el token de exportación de Mixpanel. La mitad inferior de la página Currents enumera los eventos Currents disponibles que puedes enviar.]({% image_buster /assets/img_archive/mixpanel4.png %}){: style="max-width:80%;"}

{% tab nota %}
Consulta [los documentos de integración](https://help.mixpanel.com/hc/en-us/articles/360001243663) de Mixpanel para obtener más información.
{% endtab %}

## Eventos Currents compatibles

Braze admite la exportación a Mixpanel de los siguientes datos enumerados en los glosarios de eventos de [comportamiento de usuario]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) e [interacción con mensajes de]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) Currents:

### Comportamientos
- Evento personalizado: `users.behaviors.CustomEvent`
- Atribución de la instalación: `users.behaviors.InstallAttribution`
- Ubicación: `users.behaviors.Location`
- Compra: `users.behaviors.Purchase`
- Desinstalar: `users.behaviors.Uninstall`
- App (primera sesión, fin de sesión, inicio de sesión)
  - `users.behaviors.app.FirstSession`
  - `users.behaviors.app.SessionEnd`
  - `users.behaviors.app.SessionStart`
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
  
