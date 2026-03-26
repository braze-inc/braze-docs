La siguiente tabla enumera los posibles valores de `abort_type`. Un tipo de cancelación describe la razón específica por la que no se envió un mensaje.

{% if include.channel %}
{% assign ch = include.channel %}
{% else %}
{% assign ch = "all" %}
{% endif %}

### General

Estos tipos de cancelación pueden ocurrir en cualquier canal de mensajería.

| Valor de `abort_type` | Descripción |
| --- | --- |
| `liquid_abort_message` | Se llamó a la etiqueta de Liquid [abort_message]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/), por lo que se canceló el envío. |
| `template_parse_error` | La plantilla del mensaje no se pudo analizar debido a un error de sintaxis o de renderizado, por lo que se canceló el envío. |
| `rate_limit` | El mensaje se canceló porque superó el [límite de velocidad]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) configurado. |
| `campaign_disabled` | La campaña se desactivó antes de que se pudiera enviar el mensaje. |
| `campaign_does_not_exist` | La campaña asociada a este mensaje ya no existe. |
| `campaign_action_does_not_exist` | La acción de campaña asociada a este mensaje ya no existe. |
| `message_variation_does_not_exist` | La variación de mensaje asignada a este usuario ya no existe. |
| `user_not_in_segment` | El usuario no está en el segmento objetivo, por lo que no se envió el mensaje. |
| `trigger_event_blacklisted` | El evento desencadenante está en la lista negra, por lo que no se envió el mensaje. |
| `exhausted_retries` | No se pudo enviar el mensaje después del número máximo de intentos de reintento. |
| `frequency_capped` | El usuario ya recibió el número máximo de mensajes permitidos por las reglas de [limitación de frecuencia]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#about-frequency-capping) de tu espacio de trabajo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% unless ch == "newsfeedcard" or ch == "rcs" %}

### Contenido y renderizado

| Valor de `abort_type` | Descripción |
| --- | --- |
| `exhausted_cc_retries` | El contenido conectado falló después del número máximo de reintentos, por lo que se canceló el mensaje. |
| `connected_content_not_supported` | El [contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) no es compatible en este contexto, por lo que se canceló el mensaje. |
| `promo_codes_not_supported` | Los códigos promocionales no son compatibles en este contexto, por lo que se canceló el mensaje. |
| `catalog_items_rerender_not_supported` | La re-renderización de elementos del Catálogo no es compatible en este contexto, por lo que se canceló el mensaje. |
{% if ch == "all" or ch == "email" or ch == "push" or ch == "inappmessage" or ch == "contentcard" or ch == "webhook" or ch == "banner" %}| `blacklisted_media_url` | La URL del medio está en la lista negra y no se puede usar en mensajes. |
| `blocked_media_url` | La URL del medio fue bloqueada por políticas de seguridad. |
| `invalid_media_url` | La URL del medio no es válida o no se pudo resolver. |{% endif %}
{% if ch == "all" or ch == "email" or ch == "webhook" %}| `ssl_error` | Ocurrió un error SSL al realizar una solicitud. |
| `invalid_http_status` | Una solicitud HTTP devolvió un código de estado no exitoso. |
| `http_timeout` | Una solicitud HTTP agotó el tiempo de espera antes de recibir una respuesta. |
| `missing_hostname` | La URL de la solicitud no tiene un nombre de host. |{% endif %}
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endunless %}

{% if ch == "all" or ch == "email" %}

### Correo electrónico

| Valor de `abort_type` | Descripción |
| --- | --- |
| `exhausted_link_shortening_retries` | El acortamiento de enlaces falló después del número máximo de reintentos. |
| `missing_email` | El usuario no tiene una dirección de correo electrónico en su perfil. |
| `invalid_domain` | La dirección de correo electrónico tiene un dominio no válido. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "push" %}

### Push

| Valor de `abort_type` | Descripción |
| --- | --- |
| `invalid_push_payload` | La carga útil de la notificación push no es válida o tiene un formato incorrecto. |
| `sdk_not_supported` | La versión del SDK en el dispositivo del usuario no es compatible con este tipo de notificación push. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "sms" %}

### SMS/MMS

| Valor de `abort_type` | Descripción |
| --- | --- |
| `exhausted_link_shortening_retries` | El acortamiento de enlaces falló después del número máximo de reintentos. |
| `sms_empty_payload` | El cuerpo del mensaje SMS está vacío. |
| `sms_no_sending_numbers` | No hay números de teléfono de envío disponibles para este grupo de suscripción. |
| `sms_fatal_provider_error` | Ocurrió un error fatal con el proveedor de SMS, lo que impidió la entrega del mensaje. |
| `sms_gateway_domain_not_allowed` | El dominio de la pasarela SMS no está en la lista de permitidos. |
| `blocked_recipient_country` | El número de teléfono del destinatario está en un país bloqueado por tus [permisos geográficos]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_geographic_permissions/). |
| `mms_not_supported` | MMS no es compatible para este destinatario o número de envío. |
| `no_current_messaging_service` | No hay un servicio de mensajería activo configurado para este grupo de suscripción. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "whatsapp" %}

### WhatsApp

| Valor de `abort_type` | Descripción |
| --- | --- |
| `whats_app_no_sending_numbers` | No hay números de teléfono de envío disponibles para este grupo de suscripción de WhatsApp. |
| `whats_app_invalid_template_message` | El mensaje de plantilla de WhatsApp no es válido o no está aprobado. |
| `whats_app_invalid_response_message` | El mensaje de respuesta de WhatsApp no es válido. |
| `whats_app_fatal_provider_error` | Ocurrió un error fatal con el proveedor de WhatsApp, lo que impidió la entrega del mensaje. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "line" %}

### LINE

| Valor de `abort_type` | Descripción |
| --- | --- |
| `line_fatal_provider_error` | Ocurrió un error fatal con el proveedor de LINE, lo que impidió la entrega del mensaje. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "kakao" %}

### Kakao

| Valor de `abort_type` | Descripción |
| --- | --- |
| `kakao_fatal_provider_error` | Ocurrió un error fatal con el proveedor de Kakao, lo que impidió la entrega del mensaje. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "contentcard" %}

### Tarjetas de contenido

| Valor de `abort_type` | Descripción |
| --- | --- |
| `content_card_size_exceeded` | La carga útil de la tarjeta de contenido supera el límite de tamaño máximo (2 KB). |
| `content_card_content_invalid` | El contenido de la tarjeta de contenido no es válido o contiene caracteres no compatibles. |
| `content_card_expiration_invalid` | La fecha de expiración de la tarjeta de contenido no es válida. |
| `content_card_general` | No se pudo crear la tarjeta de contenido debido a un error general. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "inappmessage" %}

### Mensajes dentro de la aplicación

| Valor de `abort_type` | Descripción |
| --- | --- |
| `no_longer_in_availability_window` | El mensaje no se pudo enviar dentro de la ventana de disponibilidad configurada, por lo que se canceló. |
| `maximum_impressions_reached` | El mensaje dentro de la aplicación ya alcanzó su número máximo de impresiones. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "webhook" %}

### Webhooks

| Valor de `abort_type` | Descripción |
| --- | --- |
| `blocked_webhook_url` | La URL del webhook fue bloqueada por políticas de seguridad. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}