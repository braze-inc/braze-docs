---
nav_title: Eventos Currents Registro de cambios
page_order: 6
description: "Esta página incluye los cambios en los eventos para cada versión de Currents."
tool: Currents
---

# Registro de cambios de Currents

## Cambios en la versión 6 (fecha de lanzamiento: 04-03-2026)

### Cambios en el almacenamiento

* Cambios de campo al tipo de evento`agentconsole.AgentExecuted`:
    * Se ha añadido un nuevo`string`campo`error`: Descripción del error

* Cambios de campo al tipo de evento`agentconsole.ToolInvocation`:
    * Se ha añadido un nuevo`string`campo`request_id`: ID único para esta solicitud LLM global y ejecución completa.

* Cambios de campo al tipo de evento`users.messages.rcs.InboundReceive`:
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario

### Cambios en el intercambio de datos

* Cambios de campo al tipo de evento`agentconsole.AgentExecuted`:
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas
    * Se ha añadido un nuevo`string`campo`error`: Nombre del error

* Cambios de campo al tipo de evento`agentconsole.ToolInvocation`:
    * Se ha añadido un nuevo`string`campo`request_id`: ID único para esta solicitud LLM global y ejecución completa.

* Cambios de campo al tipo de evento`users.behaviors.subscription.GlobalStateChange`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.behaviors.subscriptiongroup.StateChange`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.campaigns.Conversion`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`conversion_behavior`: Cadena codificada en JSON que describe el comportamiento de la conversión.

* Cambios de campo al tipo de evento`users.campaigns.EnrollInControl`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje

* Cambios de campo al tipo de evento`users.canvas.Conversion`:
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas
    * Se ha añadido un nuevo`string`campo`conversion_behavior`: Cadena codificada en JSON que describe el comportamiento de la conversión.

* Cambios de campo al tipo de evento`users.canvas.Entry`:
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.canvas.exit.MatchedAudience`:
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.canvas.exit.PerformedEvent`:
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.canvas.experimentstep.Conversion`:
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas
    * Se ha añadido un nuevo`string`campo`experiment_split_name`: Nombre de la división del experimento
    * Se ha añadido un nuevo`string`campo`conversion_behavior`: Cadena codificada en JSON que describe el comportamiento de la conversión.

* Cambios de campo al tipo de evento`users.canvas.experimentstep.SplitEntry`:
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas
    * Se ha añadido un nuevo`string`campo`experiment_split_name`: Nombre de la división del experimento

* Cambios de campo al tipo de evento`users.canvasstep.Progression`:
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.banner.Abort`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje

* Cambios de campo al tipo de evento`users.messages.banner.Click`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje

* Cambios de campo al tipo de evento`users.messages.banner.Impression`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje

* Cambios de campo al tipo de evento`users.messages.contentcard.Abort`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.contentcard.Click`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.contentcard.Dismiss`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.contentcard.Impression`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.contentcard.Send`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.email.Abort`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.email.Bounce`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.email.Click`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.email.Deferral`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.email.Delivery`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.email.MarkAsSpam`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.email.Open`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.email.Retry`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.email.Send`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.email.SoftBounce`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.email.Unsubscribe`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.featureflag.Impression`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje

* Cambios de campo al tipo de evento`users.messages.inappmessage.Abort`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.inappmessage.Click`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.inappmessage.Impression`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.line.Retry`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.pushnotification.Abort`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.pushnotification.Bounce`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.pushnotification.InfluencedOpen`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.pushnotification.IosForeground`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.pushnotification.Open`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.pushnotification.Retry`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.pushnotification.Send`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.rcs.InboundReceive`:
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario

* Cambios de campo al tipo de evento`users.messages.sms.Abort`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.sms.CarrierSend`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.sms.Delivery`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.sms.DeliveryFailure`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.sms.InboundReceive`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.sms.Rejection`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.sms.Retry`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.sms.Send`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.sms.ShortLinkClick`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.webhook.Abort`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.webhook.Failure`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje

* Cambios de campo al tipo de evento`users.messages.webhook.Retry`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.webhook.Send`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.whatsapp.Abort`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.whatsapp.Click`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.whatsapp.Delivery`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.whatsapp.Failure`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.whatsapp.InboundReceive`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje

* Cambios de campo al tipo de evento`users.messages.whatsapp.Read`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.whatsapp.Retry`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas

* Cambios de campo al tipo de evento`users.messages.whatsapp.Send`:
    * Se ha añadido un nuevo`string`campo`campaign_name`: Nombre de la campaña
    * Se ha añadido un nuevo`string`campo`canvas_name`: Nombre del Canvas
    * Se ha añadido un nuevo`string`campo`canvas_step_name`: Nombre del paso en Canvas
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * Se ha añadido un nuevo`string`campo`message_variation_name`: Nombre de la variación del mensaje

## Cambios en la versión 5 (fecha de lanzamiento: 04/02/2026)

### Cambios en el almacenamiento

* Se ha añadido un nuevo tipo de evento`agentconsole.AgentExecuted`.

* Se ha añadido un nuevo tipo de evento`agentconsole.ToolInvocation`.

* Se ha añadido un nuevo tipo de evento`users.messages.email.Retry`.

* Se ha añadido un nuevo tipo de evento`users.messages.line.Retry`.

* Se ha añadido un nuevo tipo de evento`users.messages.pushnotification.Retry`.

* Se ha añadido un nuevo tipo de evento`users.messages.sms.Retry`.

* Se ha añadido un nuevo tipo de evento`users.messages.webhook.Retry`.

* Se ha añadido un nuevo tipo de evento`users.messages.whatsapp.Retry`.

* Cambios de campo al tipo de evento`users.behaviors.pushnotification.TokenStateChange`:
    * Se ha añadido un nuevo`long`campo`time_ms`: Tiempo en milisegundos en el que ocurrió el evento.

### Cambios en el intercambio de datos

* Se ha añadido un nuevo tipo de evento`agentconsole.AgentExecuted`.

* Se ha añadido un nuevo tipo de evento`agentconsole.ToolInvocation`.

* Se ha añadido un nuevo tipo de evento`users.messages.email.Retry`.

* Se ha añadido un nuevo tipo de evento`users.messages.line.Retry`.

* Se ha añadido un nuevo tipo de evento`users.messages.pushnotification.Retry`.

* Se ha añadido un nuevo tipo de evento`users.messages.sms.Retry`.

* Se ha añadido un nuevo tipo de evento`users.messages.webhook.Retry`.

* Se ha añadido un nuevo tipo de evento`users.messages.whatsapp.Retry`.

* Cambios de campo al tipo de evento`users.behaviors.pushnotification.TokenStateChange`:
    * Se ha añadido un nuevo`long`campo`time_ms`: Tiempo en milisegundos en el que ocurrió el evento.

## Cambios en la versión 4 (fecha de lanzamiento: 7 de enero de 2026)

### Cambios en el almacenamiento

* Cambios de campo al tipo de evento`users.behaviors.pushnotification.TokenStateChange`:
    * Se ha añadido un nuevo`string`campo`push_token`: Envía el token del evento.

* Cambios de campo al tipo de evento`users.messages.pushnotification.Bounce`:
    * Se ha añadido un nuevo`string`campo`push_token`: Envía el token del evento.

* Cambios de campo al tipo de evento`users.messages.pushnotification.Send`:
    * Se ha añadido un nuevo`string`campo`push_token`: Envía el token del evento.

* Cambios de campo al tipo de evento`users.messages.rcs.Click`:
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * El campo  ahora`user_phone_number` es *opcional*.

* Cambios de campo al tipo de evento`users.messages.rcs.InboundReceive`:
    * El campo  ahora`user_id` es *opcional*.

* Cambios de campo al tipo de evento`users.messages.rcs.Rejection`:
    * Se ha añadido un nuevo`string`campo`canvas_step_message_variation_id`: API ID de la variación del mensaje del paso Canvas que recibió este usuario

### Cambios en el intercambio de datos

* Cambios de campo al tipo de evento`users.messages.rcs.Click`:
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * El campo  ahora`user_phone_number` es *opcional*.

* Cambios de campo al tipo de evento`users.messages.rcs.InboundReceive`:
    * El campo  ahora`user_id` es *opcional*.

* Cambios de campo al tipo de evento`users.messages.rcs.Rejection`:
    * Se ha añadido un nuevo`string`campo`canvas_step_message_variation_api_id`: API ID de la variación del mensaje del paso Canvas que recibió este usuario

## Cambios en la versión 3 (fecha de lanzamiento: 08-10-2025)

### Cambios en el almacenamiento

* Se ha añadido un nuevo tipo de evento`users.messages.line.Abort`.

* Se ha añadido un nuevo tipo de evento`users.messages.line.Click`.

* Se ha añadido un nuevo tipo de evento`users.messages.line.InboundReceive`.

* Se ha añadido un nuevo tipo de evento`users.messages.line.Send`.

* Se ha añadido un nuevo tipo de evento`users.messages.rcs.Abort`.

* Se ha añadido un nuevo tipo de evento`users.messages.rcs.Click`.

* Se ha añadido un nuevo tipo de evento`users.messages.rcs.Delivery`.

* Se ha añadido un nuevo tipo de evento`users.messages.rcs.InboundReceive`.

* Se ha añadido un nuevo tipo de evento`users.messages.rcs.Read`.

* Se ha añadido un nuevo tipo de evento`users.messages.rcs.Rejection`.

* Se ha añadido un nuevo tipo de evento`users.messages.rcs.Send`.

* Cambios de campo al tipo de evento`users.messages.sms.Delivery`:
    * Se ha añadido un nuevo`boolean`campo`is_sms_fallback`: Indica que se ha enviado un mensaje SMS alternativo debido a que se ha rechazado un mensaje RCS. El mensaje puede ser entregado, no entregado o rechazado. Se puede vincular al evento de rechazo RCS mediante un ID de envío y un ID de despacho.

* Cambios de campo al tipo de evento`users.messages.sms.DeliveryFailure`:
    * Se ha añadido un nuevo`boolean`campo`is_sms_fallback`: Indica que se ha enviado un mensaje SMS alternativo debido a que se ha rechazado un mensaje RCS. El mensaje puede ser entregado, no entregado o rechazado. Se puede vincular al evento de rechazo RCS mediante un ID de envío y un ID de despacho.

* Cambios de campo al tipo de evento`users.messages.sms.Rejection`:
    * Se ha añadido un nuevo`boolean`campo`is_sms_fallback`: Indica que se ha enviado un mensaje SMS alternativo debido a que se ha rechazado un mensaje RCS. El mensaje puede ser entregado, no entregado o rechazado. Se puede vincular al evento de rechazo RCS mediante un ID de envío y un ID de despacho. Se puede vincular al evento de rechazo RCS mediante un ID de envío y un ID de despacho. (Propiedad del evento)

* Cambios de campo al tipo de evento`users.messages.whatsapp.Delivery`:
    * Se ha añadido un nuevo`string`campo`flow_id`: El ID único del flujo en el administrador de WhatsApp. Presente si el mensaje incluye una llamada a la acción para responder a un flujo de WhatsApp.
    * Se ha añadido un nuevo`string`campo`template_name`: [PII] Nombre de la plantilla en el administrador de WhatsApp. Presente si envías un mensaje de plantilla
    * Se ha añadido un nuevo`string`campo`message_id`: El ID único generado por Meta para este mensaje.

* Cambios de campo al tipo de evento`users.messages.whatsapp.Failure`:
    * Se ha añadido un nuevo`string`campo`message_id`: El ID único generado por Meta para este mensaje.
    * Se ha añadido un nuevo`string`campo`template_name`: [PII] Nombre de la plantilla en el administrador de WhatsApp. Presente si envías un mensaje de plantilla
    * Se ha añadido un nuevo`string`campo`flow_id`: El ID único del flujo en el administrador de WhatsApp. Presente si el mensaje incluye una llamada a la acción para responder a un flujo de WhatsApp.

* Cambios de campo al tipo de evento`users.messages.whatsapp.InboundReceive`:
    * Se ha añadido un nuevo`string`campo`catalog_id`: ID de catálogo de un producto si se hace referencia a un producto en el mensaje de entrada. Si no, vacío.
    * Se ha añadido un nuevo`string`campo`product_id`: El SKU del producto si se hace referencia a un producto en el mensaje de entrada. Si no, vacío.
    * Se ha añadido un nuevo`string`campo`flow_id`: El ID único del flujo en el administrador de WhatsApp. Presente si el usuario está respondiendo a un flujo de WhatsApp.
    * Se ha añadido un nuevo`string`campo`flow_response_json`: [PII] Los valores del formulario que el usuario ha respondido. Presente si el usuario está respondiendo a un flujo de WhatsApp.
    * Se ha añadido un nuevo`string`campo`message_id`: El ID único generado por Meta para este mensaje.
    * Se ha añadido un nuevo`string`campo`in_reply_to`: Elmessage_id  del mensaje al que respondía este mensaje.

* Cambios de campo al tipo de evento`users.messages.whatsapp.Read`:
    * Se ha añadido un nuevo`string`campo`template_name`: [PII] Nombre de la plantilla en el administrador de WhatsApp. Presente si envías un mensaje de plantilla
    * Se ha añadido un nuevo`string`campo`message_id`: El ID único generado por Meta para este mensaje.
    * Se ha añadido un nuevo`string`campo`flow_id`: El ID único del flujo en el administrador de WhatsApp. Presente si el mensaje incluye una llamada a la acción para responder a un flujo de WhatsApp.

* Cambios de campo al tipo de evento`users.messages.whatsapp.Send`:
    * Se ha añadido un nuevo`string`campo`flow_id`: El ID único del flujo en el administrador de WhatsApp. Presente si el mensaje incluye una llamada a la acción para responder a un flujo de WhatsApp.
    * Se ha añadido un nuevo`string`campo`template_name`: [PII] Nombre de la plantilla en WhatsApp Administrador. Presente si envías un mensaje de plantilla
    * Se ha añadido un nuevo`string`campo`message_id`: El ID único generado por Meta para este mensaje.

### Cambios en el intercambio de datos

* Se ha añadido un nuevo tipo de evento`users.messages.line.Abort`.

* Se ha añadido un nuevo tipo de evento`users.messages.line.Click`.

* Se ha añadido un nuevo tipo de evento`users.messages.line.InboundReceive`.

* Se ha añadido un nuevo tipo de evento`users.messages.line.Send`.

* Se ha añadido un nuevo tipo de evento`users.messages.rcs.Abort`.

* Se ha añadido un nuevo tipo de evento`users.messages.rcs.Click`.

* Se ha añadido un nuevo tipo de evento`users.messages.rcs.Delivery`.

* Se ha añadido un nuevo tipo de evento`users.messages.rcs.InboundReceive`.

* Se ha añadido un nuevo tipo de evento`users.messages.rcs.Read`.

* Se ha añadido un nuevo tipo de evento`users.messages.rcs.Rejection`.

* Se ha añadido un nuevo tipo de evento`users.messages.rcs.Send`.

* Cambios de campo al tipo de evento`users.messages.sms.Delivery`:
    * Se ha añadido un nuevo`boolean`campo`is_sms_fallback`: Indica si se intentó la alternativa por SMS para este mensaje RCS rechazado. Está vinculado/emparejado al evento de entrega de SMS.

* Cambios de campo al tipo de evento`users.messages.sms.DeliveryFailure`:
    * Se ha añadido un nuevo`boolean`campo`is_sms_fallback`: Indica si se intentó la alternativa por SMS para este mensaje RCS rechazado. Está vinculado/emparejado al evento de entrega de SMS.

* Cambios de campo al tipo de evento`users.messages.sms.Rejection`:
    * Se ha añadido un nuevo`boolean`campo`is_sms_fallback`: Indica si se intentó la alternativa por SMS para este mensaje RCS rechazado. Está vinculado/emparejado al evento de entrega de SMS.

* Cambios de campo al tipo de evento`users.messages.whatsapp.Delivery`:
    * Se ha añadido un nuevo`string`campo`flow_id`: El ID único del flujo en el administrador de WhatsApp. Presente si el usuario está respondiendo a un flujo de WhatsApp.
    * Se ha añadido un nuevo`string`campo`template_name`: [PII] Nombre de la plantilla en el administrador de WhatsApp. Presente si envías un mensaje de plantilla
    * Se ha añadido un nuevo`string`campo`message_id`: El ID único generado por Meta para este mensaje.

* Cambios de campo al tipo de evento`users.messages.whatsapp.Failure`:
    * Se ha añadido un nuevo`string`campo`message_id`: El ID único generado por Meta para este mensaje.
    * Se ha añadido un nuevo`string`campo`template_name`: [PII] Nombre de la plantilla en el administrador de WhatsApp. Presente si envías un mensaje de plantilla
    * Se ha añadido un nuevo`string`campo`flow_id`: El ID único del flujo en el administrador de WhatsApp. Presente si el usuario está respondiendo a un flujo de WhatsApp.

* Cambios de campo al tipo de evento`users.messages.whatsapp.InboundReceive`:
    * Se ha añadido un nuevo`string`campo`catalog_id`: ID de catálogo de un producto si se hace referencia a un producto en el mensaje de entrada. Si no, vacío.
    * Se ha añadido un nuevo`string`campo`product_id`: ID del producto adquirido
    * Se ha añadido un nuevo`string`campo`flow_id`: El ID único del flujo en el administrador de WhatsApp. Presente si el usuario está respondiendo a un flujo de WhatsApp.
    * Se ha añadido un nuevo`string`campo`flow_response_json`: [PII] Los valores del formulario que el usuario ha respondido. Presente si el usuario está respondiendo a un flujo de WhatsApp.
    * Se ha añadido un nuevo`string`campo`message_id`: El ID único generado por Meta para este mensaje.
    * Se ha añadido un nuevo`string`campo`in_reply_to`: Elmessage_id  del mensaje al que respondía este mensaje.

* Cambios de campo al tipo de evento`users.messages.whatsapp.Read`:
    * Se ha añadido un nuevo`string`campo`template_name`: [PII] Nombre de la plantilla en el administrador de WhatsApp. Presente si envías un mensaje de plantilla
    * Se ha añadido un nuevo`string`campo`message_id`: El ID único generado por Meta para este mensaje.
    * Se ha añadido un nuevo`string`campo`flow_id`: El ID único del flujo en el administrador de WhatsApp. Presente si el usuario está respondiendo a un flujo de WhatsApp.

* Cambios de campo al tipo de evento`users.messages.whatsapp.Send`:
    * Se ha añadido un nuevo`string`campo`flow_id`: El ID único del flujo en el administrador de WhatsApp. Presente si el usuario está respondiendo a un flujo de WhatsApp.
    * Se ha añadido un nuevo`string`campo`template_name`: [PII] Nombre de la plantilla en el administrador de WhatsApp. Presente si envías un mensaje de plantilla
    * Se ha añadido un nuevo`string`campo`message_id`: El ID único generado por Meta para este mensaje.

## Cambios en la versión 2 (fecha de lanzamiento nula)

### Cambios en el almacenamiento

* Se ha añadido un nuevo tipo de evento`users.behaviors.app.FirstSession`.

* Se ha añadido un nuevo tipo de evento`users.behaviors.app.SessionEnd`.

* Se ha añadido un nuevo tipo de evento`users.behaviors.app.SessionStart`.

* Se ha añadido un nuevo tipo de evento`users.behaviors.CustomEvent`.

* Se ha añadido un nuevo tipo de evento`users.behaviors.InstallAttribution`.

* Se ha añadido un nuevo tipo de evento`users.behaviors.liveactivity.PushToStartTokenChange`.

* Se ha añadido un nuevo tipo de evento`users.behaviors.liveactivity.UpdateTokenChange`.

* Se ha añadido un nuevo tipo de evento`users.behaviors.Location`.

* Se ha añadido un nuevo tipo de evento`users.behaviors.Purchase`.

* Se ha añadido un nuevo tipo de evento`users.behaviors.pushnotification.TokenStateChange`.

* Se ha añadido un nuevo tipo de evento`users.behaviors.subscription.GlobalStateChange`.

* Se ha añadido un nuevo tipo de evento`users.behaviors.subscriptiongroup.StateChange`.

* Se ha añadido un nuevo tipo de evento`users.behaviors.Uninstall`.

* Se ha añadido un nuevo tipo de evento`users.campaigns.Conversion`.

* Se ha añadido un nuevo tipo de evento`users.campaigns.EnrollInControl`.

* Se ha añadido un nuevo tipo de evento`users.canvas.Conversion`.

* Se ha añadido un nuevo tipo de evento`users.canvas.Entry`.

* Se ha añadido un nuevo tipo de evento`users.canvas.exit.MatchedAudience`.

* Se ha añadido un nuevo tipo de evento`users.canvas.exit.PerformedEvent`.

* Se ha añadido un nuevo tipo de evento`users.canvas.experimentstep.Conversion`.

* Se ha añadido un nuevo tipo de evento`users.canvas.experimentstep.SplitEntry`.

* Se ha añadido un nuevo tipo de evento`users.canvasstep.Progression`.

* Se ha añadido un nuevo tipo de evento`users.messages.banner.Abort`.

* Se ha añadido un nuevo tipo de evento`users.messages.banner.Click`.

* Se ha añadido un nuevo tipo de evento`users.messages.banner.Impression`.

* Se ha añadido un nuevo tipo de evento`users.messages.contentcard.Abort`.

* Se ha añadido un nuevo tipo de evento`users.messages.contentcard.Click`.

* Se ha añadido un nuevo tipo de evento`users.messages.contentcard.Dismiss`.

* Se ha añadido un nuevo tipo de evento`users.messages.contentcard.Impression`.

* Se ha añadido un nuevo tipo de evento`users.messages.contentcard.Send`.

* Se ha añadido un nuevo tipo de evento`users.messages.email.Abort`.

* Se ha añadido un nuevo tipo de evento`users.messages.email.Bounce`.

* Se ha añadido un nuevo tipo de evento`users.messages.email.Click`.

* Se ha añadido un nuevo tipo de evento`users.messages.email.Deferral`.

* Se ha añadido un nuevo tipo de evento`users.messages.email.Delivery`.

* Se ha añadido un nuevo tipo de evento`users.messages.email.MarkAsSpam`.

* Se ha añadido un nuevo tipo de evento`users.messages.email.Open`.

* Se ha añadido un nuevo tipo de evento`users.messages.email.Send`.

* Se ha añadido un nuevo tipo de evento`users.messages.email.SoftBounce`.

* Se ha añadido un nuevo tipo de evento`users.messages.email.Unsubscribe`.

* Se ha añadido un nuevo tipo de evento`users.messages.featureflag.Impression`.

* Se ha añadido un nuevo tipo de evento`users.messages.inappmessage.Abort`.

* Se ha añadido un nuevo tipo de evento`users.messages.inappmessage.Click`.

* Se ha añadido un nuevo tipo de evento`users.messages.inappmessage.Impression`.

* Se ha añadido un nuevo tipo de evento`users.messages.liveactivity.Outcome`.

* Se ha añadido un nuevo tipo de evento`users.messages.liveactivity.Send`.

* Se ha añadido un nuevo tipo de evento`users.messages.pushnotification.Abort`.

* Se ha añadido un nuevo tipo de evento`users.messages.pushnotification.Bounce`.

* Se ha añadido un nuevo tipo de evento`users.messages.pushnotification.IosForeground`.

* Se ha añadido un nuevo tipo de evento`users.messages.pushnotification.Open`.

* Se ha añadido un nuevo tipo de evento`users.messages.pushnotification.Send`.

* Se ha añadido un nuevo tipo de evento`users.messages.sms.Abort`.

* Se ha añadido un nuevo tipo de evento`users.messages.sms.CarrierSend`.

* Se ha añadido un nuevo tipo de evento`users.messages.sms.Delivery`.

* Se ha añadido un nuevo tipo de evento`users.messages.sms.DeliveryFailure`.

* Se ha añadido un nuevo tipo de evento`users.messages.sms.InboundReceive`.

* Se ha añadido un nuevo tipo de evento`users.messages.sms.Rejection`.

* Se ha añadido un nuevo tipo de evento`users.messages.sms.Send`.

* Se ha añadido un nuevo tipo de evento`users.messages.sms.ShortLinkClick`.

* Se ha añadido un nuevo tipo de evento`users.messages.webhook.Abort`.

* Se ha añadido un nuevo tipo de evento`users.messages.webhook.Failure`.

* Se ha añadido un nuevo tipo de evento`users.messages.webhook.Send`.

* Se ha añadido un nuevo tipo de evento`users.messages.whatsapp.Abort`.

* Se ha añadido un nuevo tipo de evento`users.messages.whatsapp.Click`.

* Se ha añadido un nuevo tipo de evento`users.messages.whatsapp.Delivery`.

* Se ha añadido un nuevo tipo de evento`users.messages.whatsapp.Failure`.

* Se ha añadido un nuevo tipo de evento`users.messages.whatsapp.InboundReceive`.

* Se ha añadido un nuevo tipo de evento`users.messages.whatsapp.Read`.

* Se ha añadido un nuevo tipo de evento`users.messages.whatsapp.Send`.

* Se ha añadido un nuevo tipo de evento`users.RandomBucketNumberUpdate`.

### Cambios en el intercambio de datos

* Se ha añadido un nuevo tipo de evento`changelogs.GlobalControlGroup`.

* Se ha añadido un nuevo tipo de evento`users.behaviors.app.FirstSession`.

* Se ha añadido un nuevo tipo de evento`users.behaviors.app.NewsFeedImpression`.

* Se ha añadido un nuevo tipo de evento`users.behaviors.app.SessionEnd`.

* Se ha añadido un nuevo tipo de evento`users.behaviors.app.SessionStart`.

* Se ha añadido un nuevo tipo de evento`users.behaviors.CustomEvent`.

* Se ha añadido un nuevo tipo de evento`users.behaviors.geofence.DataEvent`.

* Se ha añadido un nuevo tipo de evento`users.behaviors.geofence.RecordEvent`.

* Se ha añadido un nuevo tipo de evento`users.behaviors.InstallAttribution`.

* Se ha añadido un nuevo tipo de evento`users.behaviors.liveactivity.PushToStartTokenChange`.

* Se ha añadido un nuevo tipo de evento`users.behaviors.liveactivity.UpdateTokenChange`.

* Se ha añadido un nuevo tipo de evento`users.behaviors.Location`.

* Se ha añadido un nuevo tipo de evento`users.behaviors.Purchase`.

* Se ha añadido un nuevo tipo de evento`users.behaviors.pushnotification.TokenStateChange`.

* Se ha añadido un nuevo tipo de evento`users.behaviors.subscription.GlobalStateChange`.

* Se ha añadido un nuevo tipo de evento`users.behaviors.subscriptiongroup.StateChange`.

* Se ha añadido un nuevo tipo de evento`users.behaviors.Uninstall`.

* Se ha añadido un nuevo tipo de evento`users.behaviors.UpgradedApp`.

* Se ha añadido un nuevo tipo de evento`users.campaigns.Conversion`.

* Se ha añadido un nuevo tipo de evento`users.campaigns.EnrollInControl`.

* Se ha añadido un nuevo tipo de evento`users.campaigns.FrequencyCap`.

* Se ha añadido un nuevo tipo de evento`users.campaigns.Revenue`.

* Se ha añadido un nuevo tipo de evento`users.canvas.Conversion`.

* Se ha añadido un nuevo tipo de evento`users.canvas.Entry`.

* Se ha añadido un nuevo tipo de evento`users.canvas.exit.MatchedAudience`.

* Se ha añadido un nuevo tipo de evento`users.canvas.exit.PerformedEvent`.

* Se ha añadido un nuevo tipo de evento`users.canvas.experimentstep.Conversion`.

* Se ha añadido un nuevo tipo de evento`users.canvas.experimentstep.SplitEntry`.

* Se ha añadido un nuevo tipo de evento`users.canvas.FrequencyCap`.

* Se ha añadido un nuevo tipo de evento`users.canvas.Revenue`.

* Se ha añadido un nuevo tipo de evento`users.canvasstep.Progression`.

* Se ha añadido un nuevo tipo de evento`users.messages.banner.Abort`.

* Se ha añadido un nuevo tipo de evento`users.messages.banner.Click`.

* Se ha añadido un nuevo tipo de evento`users.messages.banner.Impression`.

* Se ha añadido un nuevo tipo de evento`users.messages.contentcard.Abort`.

* Se ha añadido un nuevo tipo de evento`users.messages.contentcard.Click`.

* Se ha añadido un nuevo tipo de evento`users.messages.contentcard.Dismiss`.

* Se ha añadido un nuevo tipo de evento`users.messages.contentcard.Impression`.

* Se ha añadido un nuevo tipo de evento`users.messages.contentcard.Send`.

* Se ha añadido un nuevo tipo de evento`users.messages.email.Abort`.

* Se ha añadido un nuevo tipo de evento`users.messages.email.Bounce`.

* Se ha añadido un nuevo tipo de evento`users.messages.email.Click`.

* Se ha añadido un nuevo tipo de evento`users.messages.email.Deferral`.

* Se ha añadido un nuevo tipo de evento`users.messages.email.Delivery`.

* Se ha añadido un nuevo tipo de evento`users.messages.email.MarkAsSpam`.

* Se ha añadido un nuevo tipo de evento`users.messages.email.Open`.

* Se ha añadido un nuevo tipo de evento`users.messages.email.Send`.

* Se ha añadido un nuevo tipo de evento`users.messages.email.SoftBounce`.

* Se ha añadido un nuevo tipo de evento`users.messages.email.Unsubscribe`.

* Se ha añadido un nuevo tipo de evento`users.messages.featureflag.Impression`.

* Se ha añadido un nuevo tipo de evento`users.messages.inappmessage.Abort`.

* Se ha añadido un nuevo tipo de evento`users.messages.inappmessage.Click`.

* Se ha añadido un nuevo tipo de evento`users.messages.inappmessage.Impression`.

* Se ha añadido un nuevo tipo de evento`users.messages.liveactivity.Outcome`.

* Se ha añadido un nuevo tipo de evento`users.messages.liveactivity.Send`.

* Se ha añadido un nuevo tipo de evento`users.messages.newsfeedcard.Abort`.

* Se ha añadido un nuevo tipo de evento`users.messages.newsfeedcard.Click`.

* Se ha añadido un nuevo tipo de evento`users.messages.newsfeedcard.Impression`.

* Se ha añadido un nuevo tipo de evento`users.messages.pushnotification.Abort`.

* Se ha añadido un nuevo tipo de evento`users.messages.pushnotification.Bounce`.

* Se ha añadido un nuevo tipo de evento`users.messages.pushnotification.InfluencedOpen`.

* Se ha añadido un nuevo tipo de evento`users.messages.pushnotification.IosForeground`.

* Se ha añadido un nuevo tipo de evento`users.messages.pushnotification.Open`.

* Se ha añadido un nuevo tipo de evento`users.messages.pushnotification.Send`.

* Se ha añadido un nuevo tipo de evento`users.messages.sms.Abort`.

* Se ha añadido un nuevo tipo de evento`users.messages.sms.CarrierSend`.

* Se ha añadido un nuevo tipo de evento`users.messages.sms.Delivery`.

* Se ha añadido un nuevo tipo de evento`users.messages.sms.DeliveryFailure`.

* Se ha añadido un nuevo tipo de evento`users.messages.sms.InboundReceive`.

* Se ha añadido un nuevo tipo de evento`users.messages.sms.Rejection`.

* Se ha añadido un nuevo tipo de evento`users.messages.sms.Send`.

* Se ha añadido un nuevo tipo de evento`users.messages.sms.ShortLinkClick`.

* Se ha añadido un nuevo tipo de evento`users.messages.webhook.Abort`.

* Se ha añadido un nuevo tipo de evento`users.messages.webhook.Failure`.

* Se ha añadido un nuevo tipo de evento`users.messages.webhook.Send`.

* Se ha añadido un nuevo tipo de evento`users.messages.whatsapp.Abort`.

* Se ha añadido un nuevo tipo de evento`users.messages.whatsapp.Click`.

* Se ha añadido un nuevo tipo de evento`users.messages.whatsapp.Delivery`.

* Se ha añadido un nuevo tipo de evento`users.messages.whatsapp.Failure`.

* Se ha añadido un nuevo tipo de evento`users.messages.whatsapp.InboundReceive`.

* Se ha añadido un nuevo tipo de evento`users.messages.whatsapp.Read`.

* Se ha añadido un nuevo tipo de evento`users.messages.whatsapp.Send`.

* Se ha añadido un nuevo tipo de evento`users.RandomBucketNumberUpdate`.

* Se ha añadido un nuevo tipo de evento`users.UserDeleteRequest`.

* Se ha añadido un nuevo tipo de evento`users.UserOrphan`.
