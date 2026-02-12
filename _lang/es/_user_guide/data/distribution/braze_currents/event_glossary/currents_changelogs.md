---
nav_title: Registros de cambios de los eventos de Currents
page_order: 6
description: "Esta página incluye los cambios de eventos para cada versión de Currents."
tool: Currents
---

# Registro de cambios de Currents

## Cambios en la Versión 5 (fecha de publicación 2026-02-04)

* Añadido un nuevo tipo de evento `agentconsole.AgentExecuted`.

* Añadido un nuevo tipo de evento `agentconsole.ToolInvocation`.

* Añadido un nuevo tipo de evento `users.messages.email.Retry`.

* Añadido un nuevo tipo de evento `users.messages.line.Retry`.

* Añadido un nuevo tipo de evento `users.messages.pushnotification.Retry`.

* Añadido un nuevo tipo de evento `users.messages.sms.Retry`.

* Añadido un nuevo tipo de evento `users.messages.webhook.Retry`.

* Añadido un nuevo tipo de evento `users.messages.whatsapp.Retry`.

* El campo cambia al tipo de evento `users.behaviors.pushnotification.TokenStateChange`:
    * Añadido el nuevo campo `long` `time_ms` : Hora en milisegundos en que se produjo el suceso


## Cambios en la Versión 4 (fecha de publicación 2026-01-08)

* El campo cambia al tipo de evento `users.behaviors.pushnotification.TokenStateChange`:
    * Añadido el nuevo campo `string` `push_token` : Token de notificaciones push del evento

* El campo cambia al tipo de evento `users.messages.pushnotification.Bounce`:
    * Añadido el nuevo campo `string` `push_token` : Token de notificaciones push del evento

* El campo cambia al tipo de evento `users.messages.pushnotification.Send`:
    * Añadido el nuevo campo `string` `push_token` : Token de notificaciones push del evento

* El campo cambia al tipo de evento `users.messages.rcs.Click`:
    * Añadido el nuevo campo `string` `canvas_variation_name` : Nombre de la variación de Canvas que recibió este usuario
    * El campo `user_phone_number` es ahora *opcional*.

* El campo cambia al tipo de evento `users.messages.rcs.InboundReceive`:
    * El campo `user_id` es ahora *opcional*.

* El campo cambia al tipo de evento `users.messages.rcs.Rejection`:
    * Añadido el nuevo campo `string` `canvas_step_message_variation_id` : API ID de la variación del mensaje del paso Canvas que recibió este usuario


## Cambios en la Versión 3 (fecha de lanzamiento 2025-10-08)

* Añadido un nuevo tipo de evento `users.messages.line.Abort`.

* Añadido un nuevo tipo de evento `users.messages.line.Click`.

* Añadido un nuevo tipo de evento `users.messages.line.InboundReceive`.

* Añadido un nuevo tipo de evento `users.messages.line.Send`.

* Añadido un nuevo tipo de evento `users.messages.rcs.Abort`.

* Añadido un nuevo tipo de evento `users.messages.rcs.Click`.

* Añadido un nuevo tipo de evento `users.messages.rcs.Delivery`.

* Añadido un nuevo tipo de evento `users.messages.rcs.InboundReceive`.

* Añadido un nuevo tipo de evento `users.messages.rcs.Read`.

* Añadido un nuevo tipo de evento `users.messages.rcs.Rejection`.

* Añadido un nuevo tipo de evento `users.messages.rcs.Send`.

* El campo cambia al tipo de evento `users.messages.sms.Delivery`:
    * Añadido el nuevo campo `boolean` `is_sms_fallback` : Indica que se ha enviado un mensaje SMS de alternativa debido a un mensaje RCS rechazado. El mensaje puede ser entregado, no entregado o rechazado. Puede vincularse al evento RCS Rechazo mediante un ID de envío y un ID de expedición

* El campo cambia al tipo de evento `users.messages.sms.DeliveryFailure`:
    * Añadido el nuevo campo `boolean` `is_sms_fallback` : Indica que se ha enviado un mensaje SMS de alternativa debido a un mensaje RCS rechazado. El mensaje puede ser entregado, no entregado o rechazado. Puede vincularse al evento RCS Rechazo mediante un ID de envío y un ID de expedición

* El campo cambia al tipo de evento `users.messages.sms.Rejection`:
    * Añadido el nuevo campo `boolean` `is_sms_fallback` : Indica que se ha enviado un mensaje SMS de alternativa debido a un mensaje RCS rechazado. El mensaje puede ser entregado, no entregado o rechazado. Puede vincularse al evento Rechazo RCS mediante un ID de envío y un ID de expedición Puede vincularse al evento Rechazo RCS mediante un ID de envío y un ID de expedición. (Propiedad del evento)

* El campo cambia al tipo de evento `users.messages.whatsapp.Delivery`:
    * Añadido el nuevo campo `string` `flow_id` : El ID único del Flujo en el administrador de WhatsApp. Presente si el mensaje incluye una CTA para responder a un flujo de WhatsApp
    * Añadido el nuevo campo `string` `template_name` : [PII] Nombre de la plantilla en el administrador de WhatsApp. Presentar si se envía una plantilla de mensaje
    * Añadido el nuevo campo `string` `message_id` : El ID único generado por Meta para este mensaje

* El campo cambia al tipo de evento `users.messages.whatsapp.Failure`:
    * Añadido el nuevo campo `string` `message_id` : El ID único generado por Meta para este mensaje
    * Añadido el nuevo campo `string` `template_name` : [PII] Nombre de la plantilla en el administrador de WhatsApp. Presentar si se envía una plantilla de mensaje
    * Añadido el nuevo campo `string` `flow_id` : El ID único del Flujo en el administrador de WhatsApp. Presente si el mensaje incluye una CTA para responder a un flujo de WhatsApp

* El campo cambia al tipo de evento `users.messages.whatsapp.InboundReceive`:
    * Añadido el nuevo campo `string` `catalog_id` : ID de catálogo de un producto si se hace referencia a un producto en el mensaje de entrada. Si no, vacío.
    * Añadido el nuevo campo `string` `product_id` : El SKU del producto si se hace referencia a un producto en el mensaje de entrada. Si no, vacío.
    * Añadido el nuevo campo `string` `flow_id` : El ID único del Flujo en el administrador de WhatsApp. Presente si el usuario está respondiendo a un Flujo de WhatsApp.
    * Añadido el nuevo campo `string` `flow_response_json` : [PII] Los valores del formulario con los que respondió el usuario. Presente si el usuario está respondiendo a un Flujo de WhatsApp.
    * Añadido el nuevo campo `string` `message_id` : El ID único generado por Meta para este mensaje
    * Añadido el nuevo campo `string` `in_reply_to` : La dirección message_id del mensaje al que respondía este mensaje

* El campo cambia al tipo de evento `users.messages.whatsapp.Read`:
    * Añadido el nuevo campo `string` `template_name` : [PII] Nombre de la plantilla en el administrador de WhatsApp. Presentar si se envía una plantilla de mensaje
    * Añadido el nuevo campo `string` `message_id` : El ID único generado por Meta para este mensaje
    * Añadido el nuevo campo `string` `flow_id` : El ID único del Flujo en el administrador de WhatsApp. Presente si el mensaje incluye una CTA para responder a un flujo de WhatsApp

* El campo cambia al tipo de evento `users.messages.whatsapp.Send`:
    * Añadido el nuevo campo `string` `flow_id` : El ID único del Flujo en el administrador de WhatsApp. Presente si el mensaje incluye una CTA para responder a un flujo de WhatsApp
    * Añadido el nuevo campo `string` `template_name` : [PII] Nombre de la plantilla en el administrador de WhatsApp. Presentar si se envía una plantilla de mensaje
    * Añadido el nuevo campo `string` `message_id` : El ID único generado por Meta para este mensaje

