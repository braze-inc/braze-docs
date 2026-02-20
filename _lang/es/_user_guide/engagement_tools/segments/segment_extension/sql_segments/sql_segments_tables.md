---
nav_title: "Referencia de tabla SQL"
article_title: Referencia de tablas SQL
page_order: 3
page_type: reference
toc_headers: h2
description: "Este artículo contiene tablas y columnas disponibles para ser consultadas en el Generador de Consultas o al generar Extensiones de Segmento SQL."
tool: Segments
---

<style>
table td {
   word-break: keep-all;
}
</style>

# Referencia de tabla SQL

Esta página es una referencia de las tablas y columnas disponibles para ser consultadas en el [Generador de Consultas]({{site.baseurl}}/user_guide/analytics/query_builder/) o al generar [Extensiones de Segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/). 

## Índice

Tabla | Descripción
------|------------
[CATALOGS_ITEMS_SHARED](#CATALOGS_ITEMS_SHARED) | Elementos de catálogo no eliminados
[CHANGELOGS_GLOBALCONTROLGROUP_SHARED](#CHANGELOGS_GLOBALCONTROLGROUP_SHARED) | Cuando se cambia el grupo de control global
[USERS_BEHAVIORS_CUSTOMEVENT_SHARED](#USERS_BEHAVIORS_CUSTOMEVENT_SHARED) | Cuando un usuario realiza un evento personalizado
[USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED](#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED) | Cuando un usuario instala una aplicación y se la atribuimos a un socio
[USERS_BEHAVIORS_LOCATION_SHARED](#USERS_BEHAVIORS_LOCATION_SHARED) | Cuando un usuario registra una ubicación
[USERS_BEHAVIORS_PURCHASE_SHARED](#USERS_BEHAVIORS_PURCHASE_SHARED) | Cuando un usuario realiza una compra
[USERS_BEHAVIORS_UNINSTALL_SHARED](#USERS_BEHAVIORS_UNINSTALL_SHARED) | Cuando un usuario desinstala una aplicación
[USERS_BEHAVIORS_UPGRADEDAPP_SHARED](#USERS_BEHAVIORS_UPGRADEDAPP_SHARED) | Cuando un usuario actualiza la aplicación
[USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED](#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED) | Cuando un usuario tiene su primera sesión
[USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED](#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED) | Cuando un usuario consulta las noticias
[USERS_BEHAVIORS_APP_SESSIONEND_SHARED](#USERS_BEHAVIORS_APP_SESSIONEND_SHARED) | Cuando un usuario termina una sesión en una aplicación
[USERS_BEHAVIORS_APP_SESSIONSTART_SHARED](#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED) | Cuando un usuario inicia una sesión en una aplicación
[USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED) | Cuando un usuario activa una zona geovallada (por ejemplo, cuando entra o sale de una geovalla). Este evento se agrupó con otros eventos y se recibió a través del punto final de eventos estándar, por lo que es posible que el punto final no lo haya recibido en tiempo real.
[USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED) | Cuando un usuario activa una zona geovallada (por ejemplo, cuando entra o sale de una geovalla). Este evento se recibió a través del punto final de geovalla dedicado y, por tanto, se recibe en tiempo real en cuanto el dispositivo de un usuario detecta que ha desencadenado una geovalla. <br><br>Además, debido al límite de velocidad en el punto final de geovalla, es posible que algunos eventos de geovalla no se reflejen como RecordEvent. Todos los sucesos de geovalla, sin embargo, están representados por DataEvent (pero potencialmente con cierto retraso debido al procesamiento por lotes).
[USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED](#USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED) | Cuando cambia un token de notificaciones push de actividad en vivo
[USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED](#USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED) | Cuando cambia un token de actualización de Actividad en vivo
[USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED](#USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED) | Cuando cambia el estado de un token de notificaciones push
[USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED) | Cuando un usuario se suscribe o se da de baja globalmente de un canal como el correo electrónico
[USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED) | Cuando un usuario se suscribe o se da de baja de un grupo de suscripción
[USERS_CAMPAIGNS_CONVERSION_SHARED](#USERS_CAMPAIGNS_CONVERSION_SHARED) | Cuando un usuario se convierte para una campaña
[USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED](#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED) | Cuando un usuario se inscribe en el grupo de control de una campaña
[USERS_CAMPAIGNS_FREQUENCYCAP_SHARED](#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED) | Cuando se limita la frecuencia de un usuario en una campaña
[USERS_CAMPAIGNS_REVENUE_SHARED](#USERS_CAMPAIGNS_REVENUE_SHARED) | Cuando un usuario genera ingresos dentro del periodo de conversión primario
[USERS_CANVASSTEP_PROGRESSION_SHARED](#USERS_CANVASSTEP_PROGRESSION_SHARED) | Cuando un usuario avanza a un paso en Canvas
[USERS_CANVAS_CONVERSION_SHARED](#USERS_CANVAS_CONVERSION_SHARED) | Cuando un usuario convierte para un evento de conversión Canvas
[USERS_CANVAS_ENTRY_SHARED](#USERS_CANVAS_ENTRY_SHARED) | Cuando un usuario entra en un Canvas
[USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED](#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED) | Cuando un usuario sale de un Canvas porque cumple los criterios de salida del público
[USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED](#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED) | Cuando un usuario sale de un Canvas porque ha realizado un evento de excepción
[USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED) | Cuando un usuario se convierte para un paso del Experimento Canvas
[USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED) | Cuando un usuario entra en una ruta de paso de Experimento
[USERS_CANVAS_FREQUENCYCAP_SHARED](#USERS_CANVAS_FREQUENCYCAP_SHARED) | Cuando a un usuario se le limita la frecuencia de un paso de Canvas
[USERS_CANVAS_REVENUE_SHARED](#USERS_CANVAS_REVENUE_SHARED) | Cuando un usuario genera ingresos dentro del periodo del evento de conversión principal
[USERS_MESSAGES_BANNER_ABORT_SHARED](#USERS_MESSAGES_BANNER_ABORT_SHARED) | Un mensaje de banner programado originalmente fue abortado por alguna razón
[USERS_MESSAGES_BANNER_CLICK_SHARED](#USERS_MESSAGES_BANNER_CLICK_SHARED) | Cuando un usuario hace clic en un banner
[USERS_MESSAGES_BANNER_IMPRESSION_SHARED](#USERS_MESSAGES_BANNER_IMPRESSION_SHARED) | Cuando un usuario ve un banner
[USERS_MESSAGES_CONTENTCARD_ABORT_SHARED](#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED) | Un mensaje de tarjeta de contenido programado originalmente se ha cancelado por algún motivo.
[USERS_MESSAGES_CONTENTCARD_CLICK_SHARED](#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED) | Cuando un usuario hace clic en una tarjeta de contenido
[USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED](#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED) | Cuando un usuario descarta una tarjeta de contenido
[USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED](#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED) | Cuando un usuario visualiza una tarjeta de contenido
[USERS_MESSAGES_CONTENTCARD_SEND_SHARED](#USERS_MESSAGES_CONTENTCARD_SEND_SHARED) | Cuando enviamos una tarjeta de contenido a un usuario
[USERS_MESSAGES_EMAIL_ABORT_SHARED](#USERS_MESSAGES_EMAIL_ABORT_SHARED) | Un mensaje de correo electrónico programado originalmente fue abortado por alguna razón.
[USERS_MESSAGES_EMAIL_BOUNCE_SHARED](#USERS_MESSAGES_EMAIL_BOUNCE_SHARED) | Un proveedor de servicios de correo electrónico devolvió un rebote duro. Un rebote duro significa un fallo permanente en la capacidad de entrega.
[USERS_MESSAGES_EMAIL_CLICK_SHARED](#USERS_MESSAGES_EMAIL_CLICK_SHARED) | Cuando un usuario hace clic en un enlace de un correo electrónico
[USERS_MESSAGES_EMAIL_DEFERRAL_SHARED](#USERS_MESSAGES_EMAIL_DEFERRAL_SHARED) | Cuando se aplaza un correo electrónico
[USERS_MESSAGES_EMAIL_DELIVERY_SHARED](#USERS_MESSAGES_EMAIL_DELIVERY_SHARED) | Cuando se entrega un correo electrónico
[USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED](#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED) | Cuando un correo se marca como spam
[USERS_MESSAGES_EMAIL_OPEN_SHARED](#USERS_MESSAGES_EMAIL_OPEN_SHARED) | Cuando un usuario abre un correo electrónico
[USERS_MESSAGES_EMAIL_SEND_SHARED](#USERS_MESSAGES_EMAIL_SEND_SHARED) | Cuando enviamos un correo electrónico a un usuario
[USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED](#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED) | Cuando un correo electrónico devuelve un rebote blando
[USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED](#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED) | Cuando un usuario se da de baja del correo electrónico
[USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED](#USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED) | Cuando un usuario ve una bandera de característica
[USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED](#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED) | Un mensaje dentro de la aplicación programado originalmente se ha cancelado por algún motivo.
[USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED](#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED) | Cuando un usuario pulsa un mensaje in-app
[USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED](#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED) | Cuando un usuario ve un mensaje in-app
[USERS_MESSAGES_LINE_ABORT_SHARED](#USERS_MESSAGES_LINE_ABORT_SHARED) | Cuando no se pueda entregar un mensaje programado de LINE, antes de enviarlo a LINE
[USERS_MESSAGES_LINE_CLICK_SHARED](#USERS_MESSAGES_LINE_CLICK_SHARED) | Cuando un usuario hace clic en un enlace de un mensaje de LINE
[USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED) | Cuando se recibe un mensaje LINE de un usuario
[USERS_MESSAGES_LINE_SEND_SHARED](#USERS_MESSAGES_LINE_SEND_SHARED) | Cuando se envía un mensaje LINE a LINE
[USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED](#USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED) | Cuando una Actividad en vivo tiene un evento de resultado
[USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED](#USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED) | Cuando se envía un mensaje de Actividad en vivo
[USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED) | Un mensaje de tarjeta de fuente de noticias programado originalmente se abortó por algún motivo
[USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED) | Cuando un usuario hace clic en una tarjeta de noticias
[USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED) | Cuando un usuario ve una tarjeta de noticias
[USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED) | Un mensaje de notificación push programado originalmente se ha cancelado por algún motivo.
[USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED) | Cuando una notificación push rebota
[USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED) | Cuando un usuario abre la aplicación tras recibir una notificación sin hacer clic en ella
[USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED) | Cuando un usuario recibe una notificación push mientras la aplicación está abierta. <br><br>Este evento no es compatible con el [SDK de Swift](https://github.com/braze-inc/braze-swift-sdk) y está obsoleto en el [SDK de Obj-C](https://github.com/Appboy/appboy-ios-sdk).
[USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED) | Cuando un usuario abre una notificación push o pulsa un botón de notificación push (incluido un botón CERRAR que NO abre la aplicación). <br><br> Las acciones con pulsador tienen múltiples resultados. Las acciones No, Rechazar y Cancelar son "clics", y las acciones Aceptar son "aperturas". Ambos están representados en esta tabla, pero pueden distinguirse en la columna **BUTTON_ACTION_TYPE** columna. Por ejemplo, se puede utilizar una consulta para agrupar por un `BUTTON_ACTION_TYPE` que no sea No, Rechazar o Cancelar.
[USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED) | Cuando enviamos una notificación push a un usuario
[USERS_MESSAGES_RCS_ABORT_SHARED](#USERS_MESSAGES_RCS_ABORT_SHARED) | Cuando un envío RCS se interrumpe debido a un error detectado en Braze y el mensaje se abandona
[USERS_MESSAGES_RCS_CLICK_SHARED](#USERS_MESSAGES_RCS_CLICK_SHARED) | Cuando el usuario final interactúa con un mensaje RCS tocando o haciendo clic en un elemento de la IU
[USERS_MESSAGES_RCS_DELIVERY_SHARED](#USERS_MESSAGES_RCS_DELIVERY_SHARED) | Cuando se entrega correctamente un mensaje RCS al dispositivo móvil de un usuario final
[USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED) | Cuando Braze recibe un mensaje RCS originado por el usuario final
[USERS_MESSAGES_RCS_READ_SHARED](#USERS_MESSAGES_RCS_READ_SHARED) | Cuando el usuario final abre un mensaje RCS en su dispositivo
[USERS_MESSAGES_RCS_REJECTION_SHARED](#USERS_MESSAGES_RCS_REJECTION_SHARED) | Cuando un mensaje RCS no se entrega debido a la intervención del operador
[USERS_MESSAGES_RCS_SEND_SHARED](#USERS_MESSAGES_RCS_SEND_SHARED) | Cuando se envía un mensaje RCS desde los sistemas de Braze a socios de entrega de última milla
[USERS_MESSAGES_SMS_ABORT_SHARED](#USERS_MESSAGES_SMS_ABORT_SHARED) | Un mensaje SMS programado originalmente se ha cancelado por algún motivo.
[USERS_MESSAGES_SMS_CARRIERSEND_SHARED](#USERS_MESSAGES_SMS_CARRIERSEND_SHARED) | Cuando se envía un mensaje SMS al operador
[USERS_MESSAGES_SMS_DELIVERY_SHARED](#USERS_MESSAGES_SMS_DELIVERY_SHARED) | Cuando se entrega un mensaje SMS
[USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED](#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED) | Cuando Braze no puede entregar el mensaje SMS al proveedor de servicios SMS
[USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED) | Cuando se recibe un mensaje SMS de un usuario
[USERS_MESSAGES_SMS_REJECTION_SHARED](#USERS_MESSAGES_SMS_REJECTION_SHARED) | Cuando un mensaje SMS no se entrega a un usuario
[USERS_MESSAGES_SMS_SEND_SHARED](#USERS_MESSAGES_SMS_SEND_SHARED) | Cuando se envía un mensaje SMS
[USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED](#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED) | Cuando un usuario hace clic en una URL acortada Braze incluida en un mensaje SMS
[USERS_MESSAGES_WEBHOOK_ABORT_SHARED](#USERS_MESSAGES_WEBHOOK_ABORT_SHARED) | Un mensaje webhook programado originalmente se ha cancelado por algún motivo.
[USERS_MESSAGES_WEBHOOK_FAILURE_SHARED](#USERS_MESSAGES_WEBHOOK_FAILURE_SHARED) | Cuando se entrega un mensaje de webhook pero falla con una respuesta de error del punto final
[USERS_MESSAGES_WEBHOOK_SEND_SHARED](#USERS_MESSAGES_WEBHOOK_SEND_SHARED) | Cuando enviamos un webhook para un usuario
[USERS_MESSAGES_WHATSAPP_ABORT_SHARED](#USERS_MESSAGES_WHATSAPP_ABORT_SHARED) | Un mensaje de WhatsApp programado inicialmente se ha cancelado por algún motivo
[USERS_MESSAGES_WHATSAPP_CLICK_SHARED](#USERS_MESSAGES_WHATSAPP_CLICK_SHARED) | Cuando un usuario hace clic en un enlace o botón de un mensaje de WhatsApp
[USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED](#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED) |Cuando se envía un mensaje de WhatsApp
[USERS_MESSAGES_WHATSAPP_FAILURE_SHARED](#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED) | Cuando un mensaje de WhatsApp no llega a un usuario
[USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED) | Cuando se recibe un mensaje de WhatsApp de un usuario
[USERS_MESSAGES_WHATSAPP_READ_SHARED](#USERS_MESSAGES_WHATSAPP_READ_SHARED) | Cuando un usuario abre un mensaje de WhatsApp
[USERS_MESSAGES_WHATSAPP_SEND_SHARED](#USERS_MESSAGES_WHATSAPP_SEND_SHARED) | Cuando enviamos un mensaje de WhatsApp para un usuario
[USERS_RANDOMBUCKETNUMBERUPDATE_SHARED](#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED) | Cuando se cambia el número de cubo aleatorio de un usuario
[USERS_USERDELETEREQUEST_SHARED](#USERS_USERDELETEREQUEST_SHARED) | Cuando un usuario se elimina por petición de un cliente
[USERS_USERORPHAN_SHARED](#USERS_USERORPHAN_SHARED) | Cuando un usuario se fusiona con el perfil de otro usuario y el perfil original queda huérfano


## Catálogos

### CATALOGS_ITEMS_SHARED {#CATALOGS_ITEMS_SHARED}

Campo | Tipo | Descripción
------|------|------------
`catalog_id` | `string` | ID BSON del catálogo
`item_id` | `string` | ID BSON del elemento del catálogo
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones
`app_group_api_id` | `null,` `string` | API ID del grupo de aplicaciones
`field_name` | `null,` `string` | Nombre del campo
`field_value` | `null,` `string` | Valor del campo
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Registros de cambios

### CHANGELOGS_GLOBALCONTROLGROUP_SHARED {#CHANGELOGS_GLOBALCONTROLGROUP_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`app_group_api_id` | `null,` `string` | API ID del grupo de aplicaciones al que pertenece este usuario
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el suceso
`random_bucket_number` | `null, int` | Nuevo número de contenedor aleatorio
`global_control_group` | `null, boolean` | Con este cambio, el número de contenedor se incluye como grupo de control global
`previous_global_control_group` | `null, boolean` | Antes de este cambio, el número de contenedor se incluía como grupo de control global, pero ya no es así.
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


## Comportamientos

### USERS_BEHAVIORS_CUSTOMEVENT_SHARED {#USERS_BEHAVIORS_CUSTOMEVENT_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó el evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se produjo esta acción
`time` | `int` | Marca de tiempo Unix en la que el usuario realizó el evento
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`device_id` | `null,` `string` | ID del dispositivo en el que se ha producido el evento personalizado
`sdk_version` | `null,` `string` | Versión del SDK Braze en uso durante el evento
`platform` | `null,` `string` | Plataforma del dispositivo
`os_version` | `null,` `string` | Versión del sistema operativo del dispositivo
`device_model` | `null,` `string` | Modelo del dispositivo
`name` | `string` | Nombre del evento personalizado
`properties` | `string` | Propiedades personalizadas del evento almacenadas como cadena codificada JSON
`ad_id` | `null,` `string` | [PII] Identificador de publicidad
`ad_id_type` | `null,` `string` | Uno de `ios_idfa`, `google_ad_id`, `windows_ad_id`, O `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si el seguimiento publicitario está activado para el dispositivo
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED {#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que instaló
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`device_id` | `null,` `string` | `device_id` que está vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que el usuario instaló
`source` | `string` | la fuente de la atribución
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_LOCATION_SHARED {#USERS_BEHAVIORS_LOCATION_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que registra la localización
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se registró esta ubicación
`time` | `int` | Marca de tiempo Unix en la que se registró la ubicación
`latitude` | `float` | [PII] Latitud de la ubicación registrada
`longitude` | `float` | [PII] Longitud de la ubicación registrada
`altitude` | `null, float` | [PII] altitud de la ubicación registrada
`ll_accuracy` | `null, float` | precisión de latitud y longitud de la ubicación registrada
`alt_accuracy` | `null, float` | precisión de altitud de la ubicación registrada
`device_id` | `null,` `string` | ID del dispositivo en el que se registró la ubicación
`sdk_version` | `null,` `string` | Versión del SDK Braze en uso cuando se registró la localización
`platform` | `null,` `string` | Plataforma del dispositivo
`os_version` | `null,` `string` | Versión del sistema operativo del dispositivo
`device_model` | `null,` `string` | Modelo del dispositivo
`ad_id` | `null,` `string` | [PII] Identificador de publicidad
`ad_id_type` | `null,` `string` | Uno de `ios_idfa`, `google_ad_id`, `windows_ad_id`, O `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si el seguimiento publicitario está activado para el dispositivo
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_PURCHASE_SHARED {#USERS_BEHAVIORS_PURCHASE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó una compra
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se produjo la compra
`time` | `int` | Marca de tiempo Unix en la que el usuario realizó la compra
`device_id` | `null,` `string` | ID del dispositivo en el que se produjo la compra
`sdk_version` | `null,` `string` | Versión del SDK Braze en uso durante la compra
`platform` | `null,` `string` | Plataforma del dispositivo
`os_version` | `null,` `string` | Versión del sistema operativo del dispositivo
`device_model` | `null,` `string` | Modelo del dispositivo
`product_id` | `string` | ID del producto adquirido
`price` | `float` | Precio de compra
`currency` | `string` | Divisa de la compra
`properties` | `string` | Propiedades personalizadas de la compra almacenadas como cadena codificada JSON
`ad_id` | `null,` `string` | [PII] Identificador de publicidad
`ad_id_type` | `null,` `string` | Uno de `ios_idfa`, `google_ad_id`, `windows_ad_id`, O `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si el seguimiento publicitario está activado para el dispositivo
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_UNINSTALL_SHARED {#USERS_BEHAVIORS_UNINSTALL_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que desinstaló
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`device_id` | `null,` `string` | `device_id` que está vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`app_api_id` | `null,` `string` | API ID de la aplicación desinstalada
`time` | `int` | Marca de tiempo Unix en la que el usuario desinstaló
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_UPGRADEDAPP_SHARED {#USERS_BEHAVIORS_UPGRADEDAPP_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que actualizó la aplicación
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`app_api_id` | `null,` `string` | ID de API de la aplicación que el usuario ha actualizado
`time` | `int` | Marca de tiempo Unix en la que el usuario actualizó la aplicación
`device_id` | `null,` `string` | ID del dispositivo en el que el usuario actualizó la aplicación
`sdk_version` | `null,` `string` | Versión del SDK Braze en uso
`platform` | `null,` `string` | Plataforma del dispositivo
`os_version` | `null,` `string` | Versión del sistema operativo del dispositivo
`device_model` | `null,` `string` | Modelo del dispositivo
`old_app_version` | `null,` `string` | Versión antigua de la aplicación
`new_app_version` | `null,` `string` | Nueva versión de la aplicación
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED {#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realiza esta acción
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se produjo esta sesión
`time` | `int` | Marca de tiempo Unix en la que se inició la sesión
`session_id` | `string` | UUID de la sesión
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`device_id` | `null,` `string` | ID del dispositivo en el que se produjo la sesión
`sdk_version` | `null,` `string` | Versión del SDK Braze en uso durante la sesión
`platform` | `null,` `string` | Plataforma del dispositivo
`os_version` | `null,` `string` | Versión del sistema operativo del dispositivo
`device_model` | `null,` `string` | Modelo del dispositivo
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED {#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID de usuario del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`app_group_api_id` | `null,` `string` | API ID del grupo de aplicaciones al que pertenece este usuario
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se ha producido este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el suceso
`device_id` | `null,` `string` | ID del dispositivo en el que se ha producido el evento
`sdk_version` | `null,` `string` | Versión del SDK Braze en uso durante el evento
`platform` | `null,` `string` | Plataforma del dispositivo
`os_version` | `null,` `string` | Versión del sistema operativo del dispositivo
`device_model` | `null,` `string` | Modelo del dispositivo
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_SESSIONEND_SHARED {#USERS_BEHAVIORS_APP_SESSIONEND_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realiza esta acción
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se produjo esta sesión
`time` | `int` | Marca de tiempo Unix en la que finalizó la sesión
`duration` | `null, float` | Duración de la sesión en segundos
`session_id` | `string` | UUID de la sesión
`device_id` | `null,` `string` | ID del dispositivo en el que se produjo la sesión
`sdk_version` | `null,` `string` | Versión del SDK Braze en uso durante la sesión
`platform` | `null,` `string` | Plataforma del dispositivo
`os_version` | `null,` `string` | Versión del sistema operativo del dispositivo
`device_model` | `null,` `string` | Modelo del dispositivo
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_SESSIONSTART_SHARED {#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realiza esta acción
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se produjo esta sesión
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que se inició la sesión
`session_id` | `string` | UUID de la sesión
`device_id` | `null,` `string` | ID del dispositivo en el que se produjo la sesión
`sdk_version` | `null,` `string` | Versión del SDK Braze en uso durante la sesión
`platform` | `null,` `string` | Plataforma del dispositivo
`os_version` | `null,` `string` | Versión del sistema operativo del dispositivo
`device_model` | `null,` `string` | Modelo del dispositivo
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó el evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se produjo esta acción
`time` | `int` | Marca de tiempo Unix en la que el usuario realizó el evento
`device_id` | `null,` `string` | ID del dispositivo en el que se ha producido el evento personalizado
`sdk_version` | `null,` `string` | Versión del SDK Braze en uso durante el evento
`platform` | `null,` `string` | Plataforma del dispositivo
`os_version` | `null,` `string` | Versión del sistema operativo del dispositivo
`device_model` | `null,` `string` | Modelo del dispositivo
`event_type` | `string` | Qué tipo de evento de geovalla se activó. (por ejemplo, 'entrar' o 'salir').
`location_set_id` | `string` | ID del conjunto de ubicaciones de la geo-valla que se activó
`geofence_id` | `string` | ID de la geovalla desencadenada
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó el evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se produjo esta acción
`time` | `int` | Marca de tiempo Unix en la que el usuario realizó el evento
`device_id` | `null,` `string` | ID del dispositivo en el que se ha producido el evento personalizado
`sdk_version` | `null,` `string` | Versión del SDK Braze en uso durante el evento
`platform` | `null,` `string` | Plataforma del dispositivo
`os_version` | `null,` `string` | Versión del sistema operativo del dispositivo
`device_model` | `null,` `string` | Modelo del dispositivo
`event_type` | `string` | Qué tipo de evento de geovalla se activó. (por ejemplo, 'entrar' o 'salir').
`location_set_id` | `string` | ID del conjunto de ubicaciones de la geo-valla que se activó
`geofence_id` | `string` | ID de la geovalla desencadenada
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED {#USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID de usuario del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el suceso
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`activity_attributes_type` | `null,` `string` | Tipo de atributo de actividad en vivo
`push_to_start_token` | `null,` `string` | Token de notificaciones push de actividad en vivo
`device_id` | `null,` `string` | ID del dispositivo en el que se ha producido el evento
`sdk_version` | `null,` `string` | Versión del SDK Braze en uso durante el evento
`ios_push_token_apns_gateway` | `null, int` | Pasarela APNS del token de notificaciones push, sólo se aplica a los tokens de notificaciones push de iOS, 1 para desarrollo, 2 para producción
`push_token_state_change_type` | `null,` `string` | Una descripción del tipo de cambio de estado del token de notificaciones push
`app_group_api_id` | `null,` `string` | API ID del grupo de aplicaciones al que pertenece este usuario
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se ha producido este evento
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED {#USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID de usuario del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el suceso
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`activity_id` | `null,` `string` | Identificador de actividad en vivo
`update_token` | `null,` `string` | Token de actualización de actividad en vivo
`device_id` | `null,` `string` | ID del dispositivo en el que se ha producido el evento
`sdk_version` | `null,` `string` | Versión del SDK Braze en uso durante el evento
`ios_push_token_apns_gateway` | `null, int` | Pasarela APNS del token de notificaciones push, sólo se aplica a los tokens de notificaciones push de iOS, 1 para desarrollo, 2 para producción
`push_token_state_change_type` | `null,` `string` | Una descripción del tipo de cambio de estado del token de notificaciones push
`app_group_api_id` | `null,` `string` | API ID del grupo de aplicaciones al que pertenece este usuario
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se ha producido este evento
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED {#USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el suceso
`user_id` | `string` | Braze ID de usuario del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`sdk_version` | `null,` `string` | Versión del SDK Braze en uso durante el evento
`platform` | `null,` `string` | Plataforma del dispositivo
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`push_token` | `null,` `string` | Token de notificaciones push del evento
`push_token_created_at` | `null, int` | Marca de tiempo UNIX en la que se creó el token de notificaciones push
`push_token_updated_at` | `null, int` | Fecha UNIX en la que se actualizó por última vez el token de notificaciones push
`push_token_foreground_push_disabled` | `null, boolean` | Bandera de desactivación de push en primer plano del token de notificaciones push
`push_token_device_id` | `null,` `string` | ID del dispositivo del token de notificaciones push
`push_token_provisionally_opted_in` | `null, boolean` | Bandera de adhesión voluntaria provisional del token de notificaciones push
`ios_push_token_apns_gateway` | `null, int` | Pasarela APNS del token de notificaciones push, sólo se aplica a los tokens de notificaciones push de iOS, 1 para desarrollo, 2 para producción
`web_push_token_public_key` | `null,` `string` | Clave pública del token de notificaciones push, sólo se aplica a los tokens de notificaciones push web
`web_push_token_user_auth` | `null,` `string` | Autenticación de usuario del token de notificaciones push, sólo se aplica a los tokens de notificaciones push web
`web_push_token_vapid_public_key` | `null,` `string` | VAPID clave pública del token de notificaciones push, sólo se aplica a los tokens de notificaciones push web
`push_token_state_change_type` | `null,` `string` | Una descripción del tipo de cambio de estado del token de notificaciones push
`app_group_api_id` | `null,` `string` | API ID del grupo de aplicaciones al que pertenece este usuario
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se ha producido este evento
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario afectado
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`email_address` | `null,` `string` | [PII] dirección de correo electrónico del usuario
`state_change_source` | `null,` `string` | fuente del cambio de estado (REST, SDK, Dashboard, etc.)
`subscription_status` | `string` | Estado de la suscripción: Suscrito", "Desuscrito" o "Adhesión voluntaria".
`channel` | `null,` `string` | Canal del estado de suscripción global, como el correo electrónico
`time` | `int` | Marca de tiempo Unix en la que cambió el estado de la suscripción
`timezone` | `null,` `string` | Zona horaria del usuario
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`app_api_id` | `null,` `string` | API ID de la aplicación a la que pertenece el evento
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje a la que pertenece este evento
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`send_id` | `null,` `string` | ID de envío del mensaje desde el que se originó esta acción de cambio de estado de suscripción
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`channel_identifier` | `null,` `string` | [PII] El identificador del usuario en el canal para el que es el evento.
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario afectado
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`device_id` | `null,` `string` | `device_id` que está vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`email_address` | `null,` `string` | [PII] dirección de correo electrónico del usuario
`phone_number` | `null,` `string` | [PII] número de teléfono del usuario en formato e164
`app_api_id` | `null,` `string` | API ID de la aplicación a la que pertenece el evento
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje a la que pertenece este evento
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`subscription_group_api_id` | `string` | ID API del grupo de suscripción
`channel` | `null,` `string` | Canal: "email" o "sms", según el tipo de canal del grupo de suscripción
`subscription_status` | `string` | Estado de la suscripción: Suscrito", "Desuscrito" o "Adhesión voluntaria".
`time` | `int` | Marca de tiempo Unix en la que cambió el estado de la suscripción
`timezone` | `null,` `string` | Zona horaria del usuario
`send_id` | `null,` `string` | ID de envío del mensaje desde el que se originó esta acción de cambio de estado de suscripción
`state_change_source` | `null,` `string` | Fuente del cambio de estado (REST, SDK, Dashboard, etc.)
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`channel_identifier` | `null,` `string` | [PII] El identificador del usuario en el canal para el que es el evento.
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Campañas

### USERS_CAMPAIGNS_CONVERSION_SHARED {#USERS_CAMPAIGNS_CONVERSION_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`device_id` | `null,` `string` | `device_id` que está vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se ha producido este evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`conversion_behavior_index` | `null, int` | Índice del comportamiento de conversión
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED {#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`device_id` | `null,` `string` | `device_id` que está vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se ha producido este evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_FREQUENCYCAP_SHARED {#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`device_id` | `null,` `string` | `device_id` que está vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`channel` | `null,` `string` | Canal al que pertenece este evento
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_REVENUE_SHARED {#USERS_CAMPAIGNS_REVENUE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`device_id` | `null,` `string` | `device_id` que está vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se ha producido este evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`revenue` | `long` | El importe de los ingresos en USD en céntimos generados
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Canvas

### USERS_CANVASSTEP_PROGRESSION_SHARED {#USERS_CANVASSTEP_PROGRESSION_SHARED}

| Campo                                  | Tipo                     | Descripción                                                                                                     |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | ID global único para este evento                                                                               |
| `user_id`                              | `string`, `null`    | Braze ID del usuario que realizó este evento                                                                   |
| `external_user_id`                     | `string`, `null`    | [PII] ID externo del usuario                                                                              |
| `device_id`                            | `string`, `null`    | ID del dispositivo que está vinculado a este usuario, si el usuario es anónimo                                            |
| `app_group_id`                         | `string`, `null`    | Braze ID del espacio de trabajo al que pertenece este usuario                                                                   |
| `app_group_api_id`                     | `string`, `null`    | API ID del espacio de trabajo al que pertenece este usuario                                                                    |
| `time`                                 | `int`, `null`       | Marca de tiempo Unix en la que ocurrió el evento                                                                      |
| `canvas_id`                            | `string`, `null`    | (Sólo para uso de Braze) ID del Canvas al que pertenece este evento                                                     |
| `canvas_api_id`                        | `string`, `null`    | API ID del Canvas al que pertenece este evento        |         
| `canvas_variation_api_id`              | `string`, `null`    | API ID de la variación de Canvas a la que pertenece este evento                                                            |
| `canvas_step_api_id`                   | `string`, `null`    | API ID del paso Canvas al que pertenece este evento                                                                 |
| `progression_type`                     | `string`, `null`    | Tipo de evento de progresión escalonada |
| `is_canvas_entry`                      | `boolean`, `null`   | Si se trata de la entrada en un primer paso en Canvas        |
| `exit_reason`                          | `string`, `null`    | Si se trata de una salida, la razón por la que un usuario salió del Canvas durante el paso                  |
| `canvas_entry_id`                      | `string`, `null`    | Identificador único para esta instancia de un usuario en un Canvas  |
| `next_step_id`                         | `string`, `null`    | BSON ID del siguiente paso en el Canvas |
| `next_step_api_id`                     | `string`, `null`    | API ID del siguiente paso en Canvas |
| `sf_created_at`                        | `timestamp`, `null` | Cuando este evento fue recogido por el Snowpipe                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_CONVERSION_SHARED {#USERS_CANVAS_CONVERSION_SHARED}

| Campo                                  | Tipo                     | Descripción                                                                                                     |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | ID global único para este evento                                                                               |
| `user_id`                              | `string`, `null`    | Braze ID del usuario que realizó este evento                                                                   |
| `external_user_id`                     | `string`, `null`    | [PII] ID externo del usuario                                                                              |
| `device_id`                            | `string`, `null`    | ID del dispositivo que está vinculado a este usuario, si el usuario es anónimo                                            |
| `app_group_id`                         | `string`, `null`    | Braze ID del espacio de trabajo al que pertenece este usuario                                                                   |
| `app_group_api_id`                     | `string`, `null`    | API ID del espacio de trabajo al que pertenece este usuario                                                                    |
| `time`                                 | `int`, `null`       | Marca de tiempo Unix en la que ocurrió el evento                                                                      |
| `app_api_id`                           | `string`, `null`    | ID de API de la aplicación en la que se ha producido este evento                                                                  |
| `canvas_id`                            | `string`, `null`    | (Sólo para uso de Braze) ID del Canvas al que pertenece este evento                                                     |
| `canvas_api_id`                        | `string`, `null`    | API ID del Canvas al que pertenece este evento                                                                      |
| `canvas_variation_api_id`              | `string`, `null`    | API ID de la variación de Canvas a la que pertenece este evento                                                            |
| `canvas_step_api_id`                   | `string`, `null`    | API ID del paso Canvas al que pertenece este evento                                                                 |
| `canvas_step_message_variation_api_id` | `string`, `null`    | API ID de la variación del mensaje del paso Canvas que recibió este usuario                                                  |
| `conversion_behavior_index`            | `int`, `null`       | Tipo de conversión realizada por el usuario, siendo "0" una conversión primaria y "1" una conversión secundaria. |
| `gender`                               | `string`, `null`    | [PII] Sexo del usuario                                                                                        |
| `country`                              | `string`, `null`    | [PII] País del usuario                                                                                       |
| `timezone`                             | `string`, `null`    | Zona horaria del usuario                                                                                            |
| `language`                             | `string`, `null`    | [PII] Idioma del usuario                                                                                      |
| `sf_created_at`                        | `timestamp`, `null` | Cuando este evento fue recogido por el Snowpipe                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_ENTRY_SHARED {#USERS_CANVAS_ENTRY_SHARED}

| Campo                     | Tipo                     | Descripción                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | ID global único para este evento                                    |
| `user_id`                 | `string`, `null`    | Braze ID del usuario que realizó este evento                        |
| `external_user_id`        | `string`, `null`    | [PII] ID externo del usuario                                   |
| `device_id`               | `string`, `null`    | ID del dispositivo que está vinculado a este usuario, si el usuario es anónimo |
| `app_group_id`            | `string`, `null`    | Braze ID del espacio de trabajo al que pertenece este usuario                        |
| `app_group_api_id`        | `string`, `null`    | API ID del espacio de trabajo al que pertenece este usuario                         |
| `time`                    | `int`, `null`       | Marca de tiempo Unix en la que ocurrió el evento                           |
| `canvas_id`               | `string`, `null`    | (Sólo para uso de Braze) ID del Canvas al que pertenece este evento          |
| `canvas_api_id`           | `string`, `null`    | API ID del Canvas al que pertenece este evento                           |
| `canvas_variation_api_id` | `string`, `null`    | API ID de la variación de Canvas a la que pertenece este evento                 |
| `canvas_step_api_id`      | `string`, `null`    | [Deprecated] API ID del paso en Canvas al que pertenece este evento         |
| `gender`                  | `string`, `null`    | [PII] Sexo del usuario                                             |
| `country`                 | `string`, `null`    | [PII] País del usuario                                            |
| `timezone`                | `string`, `null`    | Zona horaria del usuario                                                 |
| `language`                | `string`, `null`    | [PII] Idioma del usuario                                           |
| `in_control_group`        | `boolean`, `null`   | Verdadero si el usuario estaba inscrito en el grupo de control                   |
| `sf_created_at`           | `timestamp`, `null` | Cuando este evento fue recogido por el Snowpipe                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED {#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED}

| Campo                     | Tipo                     | Descripción                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | ID global único para este evento                                    |
| `user_id`                 | `string`, `null`    | Braze ID del usuario que realizó este evento                        |
| `external_user_id`        | `string`, `null`    | [PII] ID externo del usuario                                   |
| `app_group_id`            | `string`, `null`    | Braze ID del espacio de trabajo al que pertenece este usuario                        |
| `app_group_api_id`        | `string`, `null`    | API ID del espacio de trabajo al que pertenece este usuario                         |
| `time`                    | `int`, `null`       | Marca de tiempo Unix en la que ocurrió el evento                           |
| `canvas_id`               | `string`, `null`    | (Sólo para uso de Braze) ID del Canvas al que pertenece este evento          |
| `canvas_api_id`           | `string`, `null`    | API ID del Canvas al que pertenece este evento                           |
| `canvas_variation_api_id` | `string`, `null`    | API ID de la variación de Canvas a la que pertenece este evento                 |
| `canvas_step_api_id`      | `string`, `null`    | API ID del paso Canvas al que pertenece este evento                      |
| `sf_created_at`           | `timestamp`, `null` | Cuando este evento fue recogido por el Snowpipe                        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED {#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED}

| Campo                     | Tipo                     | Descripción                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | ID global único para este evento                                    |
| `user_id`                 | `string`, `null`    | Braze ID del usuario que realizó este evento                        |
| `external_user_id`        | `string`, `null`    | [PII] ID externo del usuario                                   |
| `app_group_id`            | `string`, `null`    | Braze ID del espacio de trabajo al que pertenece este usuario                        |
| `app_group_api_id`        | `string`, `null`    | API ID del espacio de trabajo al que pertenece este usuario                         |
| `time`                    | `int`, `null`       | Marca de tiempo Unix en la que ocurrió el evento                           |
| `canvas_id`               | `string`, `null`    | (Sólo para uso de Braze) ID del Canvas al que pertenece este evento          |
| `canvas_api_id`           | `string`, `null`    | API ID del Canvas al que pertenece este evento                           |
| `canvas_variation_api_id` | `string`, `null`    | API ID de la variación de Canvas a la que pertenece este evento                 |
| `canvas_step_api_id`      | `string`, `null`    | API ID del paso Canvas al que pertenece este evento                      |
| `sf_created_at`           | `timestamp`, `null` | Cuando este evento fue recogido por el Snowpipe                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED}

| Campo                       | Tipo                     | Descripción                                                                                                     |
| --------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                        | `string`, `null`    | ID global único para este evento                                                                               |
| `user_id`                   | `string`, `null`    | Braze ID del usuario que realizó este evento                                                                   |
| `external_user_id`          | `string`, `null`    | [PII] ID externo del usuario                                                                              |
| `app_group_id`              | `string`, `null`    | Braze ID del espacio de trabajo al que pertenece este usuario                                                                   |
| `time`                      | `int`, `null`       | Marca de tiempo Unix en la que ocurrió el evento                                                                      |
| `app_api_id`                | `string`, `null`    | ID de API de la aplicación en la que se ha producido este evento                                                                  |
| `canvas_id`                 | `string`, `null`    | (Sólo para uso de Braze) ID del Canvas al que pertenece este evento                                                     |
| `canvas_api_id`             | `string`, `null`    | API ID del Canvas al que pertenece este evento                                                                      |
| `canvas_variation_api_id`   | `string`, `null`    | API ID de la variación de Canvas a la que pertenece este evento                                                            |
| `canvas_step_api_id`        | `string`, `null`    | API ID del paso Canvas al que pertenece este evento                                                                 |
| `experiment_step_api_id`    | `string`, `null`    | API ID del paso del Experimento al que pertenece este evento                                                             |
| `conversion_behavior_index` | `int`, `null`       | Tipo de conversión realizada por el usuario, siendo "0" una conversión primaria y "1" una conversión secundaria. |
| `sf_created_at`             | `timestamp`, `null` | Cuando este evento fue recogido por el Snowpipe                                                                   |
| `experiment_split_api_id` | `string`, `null` | API ID de la división del experimento en la que se inscribió el usuario |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED}

| Campo                     | Tipo                     | Descripción                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | ID global único para este evento                                    |
| `user_id`                 | `string`, `null`    | Braze ID del usuario que realizó este evento                        |
| `external_user_id`        | `string`, `null`    | [PII] ID externo del usuario                                   |
| `app_group_id`            | `string`, `null`    | Braze ID del espacio de trabajo al que pertenece este usuario                        |
| `time`                    | `int`, `null`       | Marca de tiempo Unix en la que ocurrió el evento                           |
| `canvas_id`               | `string`, `null`    | (Sólo para uso de Braze) ID del Canvas al que pertenece este evento          |
| `canvas_api_id`           | `string`, `null`    | API ID del Canvas al que pertenece este evento                           |
| `canvas_variation_api_id` | `string`, `null`    | API ID de la variación de Canvas a la que pertenece este evento                 |
| `canvas_step_api_id`      | `string`, `null`    | API ID del paso Canvas al que pertenece este evento                      |
| `experiment_step_api_id`  | `string`, `null`    | API ID del paso del Experimento al que pertenece este evento                  |
| `in_control_group`        | `boolean`, `null`   | Verdadero si el usuario estaba inscrito en el grupo de control                   |
| `sf_created_at`           | `timestamp`, `null` | Cuando este evento fue recogido por el Snowpipe                        |

| `experiment_split_api_id` | `string`, `null` | API ID de la división del experimento en la que se inscribió el usuario | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_FREQUENCYCAP_SHARED {#USERS_CANVAS_FREQUENCYCAP_SHARED}

| Campo                                  | Tipo                     | Descripción                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | ID global único para este evento                                    |
| `user_id`                              | `string`, `null`    | Braze ID del usuario que realizó este evento                        |
| `external_user_id`                     | `string`, `null`    | [PII] ID externo del usuario                                   |
| `device_id`                            | `string`, `null`    | ID del dispositivo que está vinculado a este usuario, si el usuario es anónimo |
| `app_group_id`                         | `string`, `null`    | Braze ID del espacio de trabajo al que pertenece este usuario                        |
| `app_group_api_id`                     | `string`, `null`    | API ID del espacio de trabajo al que pertenece este usuario                         |
| `time`                                 | `int`, `null`       | Marca de tiempo Unix en la que ocurrió el evento                           |
| `canvas_id`                            | `string`, `null`    | (Sólo para uso de Braze) ID del Canvas al que pertenece este evento          |
| `canvas_api_id`                        | `string`, `null`    | API ID del Canvas al que pertenece este evento                           |
| `canvas_variation_api_id`              | `string`, `null`    | API ID de la variación de Canvas a la que pertenece este evento                 |
| `canvas_step_api_id`                   | `string`, `null`    | API ID del paso Canvas al que pertenece este evento                      |
| `canvas_step_message_variation_api_id` | `string`, `null`    | API ID de la variación del mensaje del paso Canvas que recibió este usuario       |
| `channel`                              | `string`, `null`    | Canal de mensajería al que pertenece este evento (correo electrónico, push, etc.)          |
| `gender`                               | `string`, `null`    | [PII] Sexo del usuario                                             |
| `country`                              | `string`, `null`    | [PII] País del usuario                                            |
| `timezone`                             | `string`, `null`    | Zona horaria del usuario                                                 |
| `language`                             | `string`, `null`    | [PII] Idioma del usuario                                           |
| `sf_created_at`                        | `timestamp`, `null` | Cuando este evento fue recogido por el Snowpipe                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_REVENUE_SHARED {#USERS_CANVAS_REVENUE_SHARED}

| Campo                                  | Tipo                     | Descripción                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | ID global único para este evento                                    |
| `user_id`                              | `string`, `null`    | Braze ID del usuario que realizó este evento                        |
| `external_user_id`                     | `string`, `null`    | [PII] ID externo del usuario                                   |
| `device_id`                            | `string`, `null`    | ID del dispositivo que está vinculado a este usuario, si el usuario es anónimo |
| `app_group_id`                         | `string`, `null`    | Braze ID del espacio de trabajo al que pertenece este usuario                        |
| `app_group_api_id`                     | `string`, `null`    | API ID del espacio de trabajo al que pertenece este usuario                         |
| `time`                                 | `int`, `null`       | Marca de tiempo Unix en la que ocurrió el evento                           |
| `canvas_id`                            | `string`, `null`    | (Sólo para uso de Braze) ID del Canvas al que pertenece este evento          |
| `canvas_api_id`                        | `string`, `null`    | API ID del Canvas al que pertenece este evento                           |
| `canvas_variation_api_id`              | `string`, `null`    | API ID de la variación de Canvas a la que pertenece este evento                 |
| `canvas_step_api_id`                   | `string`, `null`    | API ID del paso Canvas al que pertenece este evento                      |
| `canvas_step_message_variation_api_id` | `string`, `null`    | API ID de la variación del mensaje del paso Canvas que recibió este usuario       |
| `gender`                               | `string`, `null`    | [PII] Sexo del usuario                                             |
| `country`                              | `string`, `null`    | [PII] País del usuario                                            |
| `timezone`                             | `string`, `null`    | Zona horaria del usuario                                                 |
| `language`                             | `string`, `null`    | [PII] Idioma del usuario                                           |
| `revenue`                              | `int`, `null`       | Importe de los ingresos generados en USD, mostrados en céntimos               |
| `sf_created_at`                        | `timestamp`, `null` | Cuando este evento fue recogido por el Snowpipe                        |
| `app_api_id` | `string`, `null` | ID de API de la aplicación en la que se ha producido este evento |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Mensajes


### USERS_MESSAGES_BANNER_ABORT_SHARED {#USERS_MESSAGES_BANNER_ABORT_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID de usuario del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`app_group_api_id` | `null,` `string` | API ID del grupo de aplicaciones al que pertenece este usuario
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el suceso
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se ha producido este evento
`campaign_id` | `null,` `string` | ID BSON de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`device_id` | `null,` `string` | ID del dispositivo en el que se ha producido el evento
`sdk_version` | `null,` `string` | Versión del SDK Braze en uso durante el evento
`platform` | `null,` `string` | Plataforma del dispositivo
`os_version` | `null,` `string` | Versión del sistema operativo del dispositivo
`device_model` | `null,` `string` | Modelo del dispositivo
`resolution` | `null,` `string` | Resolución del dispositivo
`carrier` | `null,` `string` | Operador del dispositivo
`browser` | `null,` `string` | Navegador del dispositivo -extraído de user_agent \- en el que se produjo la apertura
`ad_id` | `null,` `string` | [PII] Identificador de publicidad
`ad_id_type` | `null,` `string` | Uno de ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | Si el seguimiento publicitario está activado para el dispositivo
`abort_type` | `null,` `string` | Tipo de aborto, uno de ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] Mensaje de registro que describe los detalles de la interrupción (hasta 128 caracteres)
`banner_placement_id` | `null,` `string` | ID de colocación del banner especificado por el cliente
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_BANNER_CLICK_SHARED {#USERS_MESSAGES_BANNER_CLICK_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID de usuario del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`app_group_api_id` | `null,` `string` | API ID del grupo de aplicaciones al que pertenece este usuario
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el suceso
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se ha producido este evento
`campaign_id` | `null,` `string` | ID BSON de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`device_id` | `null,` `string` | ID del dispositivo en el que se ha producido el evento
`sdk_version` | `null,` `string` | Versión del SDK Braze en uso durante el evento
`platform` | `null,` `string` | Plataforma del dispositivo
`os_version` | `null,` `string` | Versión del sistema operativo del dispositivo
`device_model` | `null,` `string` | Modelo del dispositivo
`resolution` | `null,` `string` | Resolución del dispositivo
`carrier` | `null,` `string` | Operador del dispositivo
`browser` | `null,` `string` | Navegador del dispositivo -extraído de user_agent \- en el que se produjo la apertura
`button_id` | `null,` `string` | ID del botón pulsado, si este clic representa un clic en un botón
`ad_id` | `null,` `string` | [PII] Identificador de publicidad
`ad_id_type` | `null,` `string` | Uno de ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | Si el seguimiento publicitario está activado para el dispositivo
`banner_placement_id` | `null,` `string` | ID de colocación del banner especificado por el cliente
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_BANNER_IMPRESSION_SHARED {#USERS_MESSAGES_BANNER_IMPRESSION_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID de usuario del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`app_group_api_id` | `null,` `string` | API ID del grupo de aplicaciones al que pertenece este usuario
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el suceso
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se ha producido este evento
`campaign_id` | `null,` `string` | ID BSON de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`device_id` | `null,` `string` | ID del dispositivo en el que se ha producido el evento
`sdk_version` | `null,` `string` | Versión del SDK Braze en uso durante el evento
`platform` | `null,` `string` | Plataforma del dispositivo
`os_version` | `null,` `string` | Versión del sistema operativo del dispositivo
`device_model` | `null,` `string` | Modelo del dispositivo
`resolution` | `null,` `string` | Resolución del dispositivo
`carrier` | `null,` `string` | Operador del dispositivo
`browser` | `null,` `string` | Navegador del dispositivo -extraído de user_agent \- en el que se produjo la apertura
`ad_id` | `null,` `string` | [PII] Identificador de publicidad
`ad_id_type` | `null,` `string` | Uno de ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | Si el seguimiento publicitario está activado para el dispositivo
`banner_placement_id` | `null,` `string` | ID de colocación del banner especificado por el cliente
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_ABORT_SHARED {#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`device_id` | `null,` `string` | `device_id` que está vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`abort_type` | `null,` `string` | Tipo de aborto, uno de ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] Mensaje de registro que describe los detalles de la interrupción (máximo de 2.000 caracteres)
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_CLICK_SHARED {#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`content_card_id` | `string` | ID de la tarjeta que generó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se ha producido este evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`device_id` | `null,` `string` | ID del dispositivo en el que se ha producido el evento
`sdk_version` | `null,` `string` | Versión del SDK Braze en uso durante el evento
`platform` | `null,` `string` | Plataforma del dispositivo
`os_version` | `null,` `string` | Versión del sistema operativo del dispositivo
`device_model` | `null,` `string` | Modelo del dispositivo
`resolution` | `null,` `string` | Resolución del dispositivo
`carrier` | `null,` `string` | Operador del dispositivo
`browser` | `null,` `string` | Navegador del dispositivo
`ad_id` | `null,` `string` | [PII] Identificador de publicidad
`ad_id_type` | `null,` `string` | Uno de `ios_idfa`, `google_ad_id`, `windows_ad_id`, O `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si el seguimiento publicitario está activado para el dispositivo
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED {#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`content_card_id` | `string` | ID de la tarjeta que generó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se ha producido este evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`device_id` | `null,` `string` | ID del dispositivo en el que se ha producido el evento
`sdk_version` | `null,` `string` | Versión del SDK Braze en uso durante el evento
`platform` | `null,` `string` | Plataforma del dispositivo
`os_version` | `null,` `string` | Versión del sistema operativo del dispositivo
`device_model` | `null,` `string` | Modelo del dispositivo
`resolution` | `null,` `string` | Resolución del dispositivo
`carrier` | `null,` `string` | Operador del dispositivo
`browser` | `null,` `string` | Navegador del dispositivo
`ad_id` | `null,` `string` | [PII] Identificador de publicidad
`ad_id_type` | `null,` `string` | Uno de `ios_idfa`, `google_ad_id`, `windows_ad_id`, O `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si el seguimiento publicitario está activado para el dispositivo
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED {#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`content_card_id` | `string` | ID de la tarjeta que generó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se ha producido este evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`device_id` | `null,` `string` | ID del dispositivo en el que se ha producido el evento
`sdk_version` | `null,` `string` | Versión del SDK Braze en uso durante el evento
`platform` | `null,` `string` | Plataforma del dispositivo
`os_version` | `null,` `string` | Versión del sistema operativo del dispositivo
`device_model` | `null,` `string` | Modelo del dispositivo
`resolution` | `null,` `string` | Resolución del dispositivo
`carrier` | `null,` `string` | Operador del dispositivo
`browser` | `null,` `string` | Navegador del dispositivo
`ad_id` | `null,` `string` | [PII] Identificador de publicidad
`ad_id_type` | `null,` `string` | Uno de `ios_idfa`, `google_ad_id`, `windows_ad_id`, O `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si el seguimiento publicitario está activado para el dispositivo
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_SEND_SHARED {#USERS_MESSAGES_CONTENTCARD_SEND_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`device_id` | `null,` `string` | `device_id` que está vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`content_card_id` | `string` | ID de la tarjeta que generó este evento
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`message_extras` | `null,` `string` | [PII] Una cadena JSON de los pares clave-valor etiquetados durante la renderización de Liquid.
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_ABORT_SHARED {#USERS_MESSAGES_EMAIL_ABORT_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`device_id` | `null,` `string` | `device_id` que está vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`email_address` | `string` | [PII] dirección de correo electrónico del usuario
`ip_pool` | `null,` `string` | Grupo de IP desde el que se realizó el envío del correo electrónico
`abort_type` | `null,` `string` | Tipo de aborto, uno de ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] Mensaje de registro que describe los detalles de la interrupción (máximo de 2.000 caracteres)
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_BOUNCE_SHARED {#USERS_MESSAGES_EMAIL_BOUNCE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`device_id` | `null,` `string` | `device_id` que está vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`email_address` | `string` | [PII] dirección de correo electrónico del usuario
`sending_ip` | `null,` `string` | Dirección IP desde la que se envió el correo electrónico
`ip_pool` | `null,` `string` | Grupo de IP desde el que se realizó el envío del correo electrónico
`bounce_reason` | `null,` `string` | [PII] El código de motivo SMTP y el mensaje fácil de usar recibidos para este evento de rebote
`esp` | `null,` `string` | ESP relacionado con el evento (SparkPost, SendGrid o Amazon SES)
`from_domain` | `null,` `string` | Dominio de envío del correo electrónico
`is_drop` | `null, boolean` | Indica que este evento cuenta como un evento de caída
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_CLICK_SHARED {#USERS_MESSAGES_EMAIL_CLICK_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`device_id` | `null,` `string` | `device_id` que está vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`email_address` | `string` | [PII] dirección de correo electrónico del usuario
`url` | `null,` `string` | URL en la que ha hecho clic el usuario
`user_agent` | `null,` `string` | Agente de usuario en el que se ha hecho clic
`ip_pool` | `null,` `string` | Grupo de IP desde el que se realizó el envío del correo electrónico
`link_id` | `null,` `string` | ID único del enlace en el que se ha hecho clic, creado por Braze
`link_alias` | `null,` `string` | Alias asociado a este ID de enlace
`esp` | `null,` `string` | ESP relacionado con el evento (SparkPost, SendGrid o Amazon SES)
`from_domain` | `null,` `string` | Dominio de envío del correo electrónico
`is_amp` | `null, boolean` | Indica que se trata de un evento AMP
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`is_suspected_bot_click` | `null, boolean` | Si este evento se procesó como un evento bot
`suspected_bot_click_reason` | `null, object` | Por qué este evento fue clasificado como bot
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_EMAIL_DEFERRAL_SHARED {#USERS_MESSAGES_EMAIL_DEFERRAL_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el suceso
`user_id` | `string` | Braze ID de usuario del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`app_group_api_id` | `null,` `string` | API ID del grupo de aplicaciones al que pertenece este usuario
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,` `string` | ID BSON de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID BSON del Canvas al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`email_address` | `null,` `string` | [PII] Dirección de correo electrónico del usuario
`recipient_domain` | `null,` `string` | Dominio de correo electrónico del destinatario
`esp` | `null,` `string` | ESP relacionado con el evento (Sparkpost o SendGrid, o Amazon SES)
`from_domain` | `null,` `string` | Dominio de envío del correo electrónico
`ip_pool` | `null,` `string` | IP desde la que se realizó el envío electrónico
`sending_ip` | `null,` `string` | Dirección IP desde la que se envió el correo electrónico
`timezone` | `null,` `string` | Zona horaria del usuario
`deferral_reason` | `null,` `string` | [PII] El código de motivo SMTP y el mensaje fácil de usar recibidos para este evento de aplazamiento
`attempt_count` | `null, int` | Número de intentos realizados para enviar el mensaje
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_DELIVERY_SHARED {#USERS_MESSAGES_EMAIL_DELIVERY_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`device_id` | `null,` `string` | `device_id` que está vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`email_address` | `string` | [PII] dirección de correo electrónico del usuario
`sending_ip` | `null,` `string` | Dirección IP desde la que se envió el correo electrónico
`ip_pool` | `null,` `string` | Grupo de IP desde el que se realizó el envío del correo electrónico
`esp` | `null,` `string` | ESP relacionado con el evento (SparkPost, SendGrid o Amazon SES)
`from_domain` | `null,` `string` | Dominio de envío del correo electrónico
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED {#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`device_id` | `null,` `string` | `device_id` que está vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`email_address` | `string` | [PII] dirección de correo electrónico del usuario
`user_agent` | `null,` `string` | Agente de usuario en el que se produjo el informe de spam
`ip_pool` | `null,` `string` | Grupo de IP desde el que se realizó el envío del correo electrónico
`esp` | `null,` `string` | ESP relacionado con el evento (SparkPost, SendGrid o Amazon SES)
`from_domain` | `null,` `string` | Dominio de envío del correo electrónico
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_OPEN_SHARED {#USERS_MESSAGES_EMAIL_OPEN_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`device_id` | `null,` `string` | `device_id` que está vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`email_address` | `string` | [PII] dirección de correo electrónico del usuario
`user_agent` | `null,` `string` | Agente de usuario en el que se produjo la apertura
`ip_pool` | `null,` `string` | Grupo de IP desde el que se realizó el envío del correo electrónico
`machine_open` | `null,` `string` | Se rellena con "true" si el evento de apertura se activa sin la participación del usuario, por ejemplo, por un dispositivo Apple con la Protección de privacidad de correo activada. El valor puede cambiar con el tiempo para proporcionar más granularidad.
`esp` | `null,` `string` | ESP relacionado con el evento (SparkPost, SendGrid o Amazon SES)
`from_domain` | `null,` `string` | Dominio de envío del correo electrónico
`is_amp` | `null, boolean` | Indica que se trata de un evento AMP
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_SEND_SHARED {#USERS_MESSAGES_EMAIL_SEND_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`device_id` | `null,` `string` | `device_id` que está vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`email_address` | `string` | [PII] dirección de correo electrónico del usuario
`ip_pool` | `null,` `string` | Grupo de IP desde el que se realizó el envío del correo electrónico
`message_extras` | `null,` `string` | [PII] Una cadena JSON de los pares clave-valor etiquetados durante la renderización de Liquid.
`esp` | `null,` `string` | ESP relacionado con el evento (SparkPost, SendGrid o Amazon SES)
`from_domain` | `null,` `string` | Dominio de envío del correo electrónico
`sf_created_at` | `timestamp`, `null` | Cuando este evento fue recogido por el Snowpipe
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED {#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`device_id` | `null,` `string` | `device_id` que está vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`email_address` | `string` | [PII] dirección de correo electrónico del usuario
`sending_ip` | `null,` `string` | Dirección IP desde la que se envió el correo electrónico
`ip_pool` | `null,` `string` | Grupo de IP desde el que se realizó el envío del correo electrónico
`bounce_reason` | `null,` `string` | [PII] El código de motivo SMTP y el mensaje fácil de usar recibidos para este evento de rebote
`esp` | `null,` `string` | ESP relacionado con el evento (SparkPost, SendGrid o Amazon SES)
`from_domain` | `null,` `string` | Dominio de envío del correo electrónico
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED {#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`device_id` | `null,` `string` | `device_id` que está vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`email_address` | `string` | [PII] dirección de correo electrónico del usuario
`ip_pool` | `null,` `string` | Grupo de IP desde el que se realizó el envío del correo electrónico
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED {#USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se ha producido este evento
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`app_group_api_id` | `null,` `string` | API ID del grupo de aplicaciones al que pertenece este usuario
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`campaign_id` | `null,` `string` | ID BSON de la campaña a la que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_id` | `null,` `string` | ID BSON del Canvas al que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`feature_flag_id_name` | `null,` `string` | Identificador del rodillo de la bandera de características
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`device_id` | `null,` `string` | ID del dispositivo en el que se ha producido el evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el suceso
`gender` | `null,` `string` | [PII] Sexo del usuario
`browser` | `null,` `string` | Navegador del dispositivo -extraído de user_agent \- en el que se produjo la apertura
`carrier` | `null,` `string` | Operador del dispositivo
`country` | `null,` `string` | [PII] País del usuario
`device_model` | `null,` `string` | Modelo del dispositivo
`language` | `null,` `string` | [PII] Idioma del usuario
`os_version` | `null,` `string` | Versión del sistema operativo del dispositivo
`platform` | `null,` `string` | Plataforma del dispositivo
`resolution` | `null,` `string` | Resolución del dispositivo
`sdk_version` | `null,` `string` | Versión del SDK Braze en uso durante el evento
`timezone` | `null,` `string` | Zona horaria del usuario
`user_id` | `string` | Braze ID de usuario del usuario que realizó este evento
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED {#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se ha producido este evento
`card_api_id` | `null,` `string` | ID de API de la tarjeta
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`device_id` | `null,` `string` | ID del dispositivo en el que se ha producido el evento
`sdk_version` | `null,` `string` | Versión del SDK Braze en uso durante el evento
`platform` | `null,` `string` | Plataforma del dispositivo
`os_version` | `null,` `string` | Versión del sistema operativo del dispositivo
`device_model` | `null,` `string` | Modelo del dispositivo
`resolution` | `null,` `string` | Resolución del dispositivo
`carrier` | `null,` `string` | Operador del dispositivo
`browser` | `null,` `string` | Navegador del dispositivo
`version` | `string` | ¿Qué versión de mensaje in-app, heredada o activada?
`ad_id` | `null,` `string` | [PII] Identificador de publicidad
`ad_id_type` | `null,` `string` | Uno de `ios_idfa`, `google_ad_id`, `windows_ad_id`, O `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si el seguimiento publicitario está activado para el dispositivo
`abort_type` | `null,` `string` | Tipo de aborto, uno de ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] Mensaje de registro que describe los detalles de la interrupción (máximo de 2.000 caracteres)
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED {#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se ha producido este evento
`card_api_id` | `null,` `string` | ID de API de la tarjeta
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`device_id` | `null,` `string` | ID del dispositivo en el que se ha producido el evento
`sdk_version` | `null,` `string` | Versión del SDK Braze en uso durante el evento
`platform` | `null,` `string` | Plataforma del dispositivo
`os_version` | `null,` `string` | Versión del sistema operativo del dispositivo
`device_model` | `null,` `string` | Modelo del dispositivo
`resolution` | `null,` `string` | resolución del dispositivo
`carrier` | `null,` `string` | operador del dispositivo
`browser` | `null,` `string` | navegador del dispositivo
`version` | `string` | qué versión de mensaje in-app, legacy o triggered
`button_id` | `null,` `string` | ID del botón pulsado, si este clic representa un clic en un botón
`ad_id` | `null,` `string` | [PII] Identificador de publicidad
`ad_id_type` | `null,` `string` | Uno de `ios_idfa`, `google_ad_id`, `windows_ad_id`, O `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si el seguimiento publicitario está activado para el dispositivo
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED {#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se ha producido este evento
`card_api_id` | `null,` `string` | ID de API de la tarjeta
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`device_id` | `null,` `string` | ID del dispositivo en el que se ha producido el evento
`sdk_version` | `null,` `string` | Versión del SDK Braze en uso durante el evento
`platform` | `null,` `string` | Plataforma del dispositivo
`os_version` | `null,` `string` | Versión del sistema operativo del dispositivo
`device_model` | `null,` `string` | Modelo del dispositivo
`resolution` | `null,` `string` | resolución del dispositivo
`carrier` | `null,` `string` | operador del dispositivo
`browser` | `null,` `string` | navegador del dispositivo
`version` | `string` | qué versión de mensaje in-app, legacy o triggered
`ad_id` | `null,` `string` | [PII] Identificador de publicidad
`ad_id_type` | `null,` `string` | Uno de `ios_idfa`, `google_ad_id`, `windows_ad_id`, O `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si el seguimiento publicitario está activado para el dispositivo
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`message_extras` | `null,` `string` | [PII] Una cadena JSON de los pares clave-valor etiquetados durante la renderización de Liquid.
`locale_key` | `null,` `string` | [PII] La clave correspondiente a las traducciones (por ejemplo "en-us") utilizadas para componer este mensaje (nula por defecto).
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_ABORT_SHARED {#USERS_MESSAGES_LINE_ABORT_SHARED}

Campo | Tipo | Descripción
------|------|------------
`app_group_api_id` | `null,` `string` | API ID del grupo de aplicaciones al que pertenece este usuario
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`id` | `string` | ID global único para este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el suceso
`user_id` | `string` | Braze ID de usuario del usuario que realizó este evento
`abort_log` | `null,` `string` | [PII] Mensaje de registro que describe los detalles de la interrupción (hasta 128 caracteres)
`abort_type` | `null,` `string` | Tipo de aborto, uno de ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`device_id` | `null,` `string` | ID del dispositivo en el que se ha producido el evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`line_channel_id` | `null,` `string` | El ID del canal LINE al que se envió o del que se recibió el mensaje
`line_channel_name` | `null,` `string` | El nombre del canal LINE al que se envió o del que se recibió el mensaje
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`native_line_id` | `null,` `string` | [PII] ID de línea del usuario desde el que se envió o recibió el mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`subscription_group_api_id` | `string` | ID API del grupo de suscripción
`timezone` | `null,` `string` | Zona horaria del usuario
`campaign_name` | `null,` `string` | Nombre de la campaña
`canvas_step_name` | `null,` `string` | Nombre del paso en Canvas
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_CLICK_SHARED {#USERS_MESSAGES_LINE_CLICK_SHARED}

Campo | Tipo | Descripción
------|------|------------
`app_group_api_id` | `null,` `string` | API ID del grupo de aplicaciones al que pertenece este usuario
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`id` | `string` | ID global único para este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el suceso
`user_id` | `string` | Braze ID de usuario del usuario que realizó este evento
`timezone` | `null,` `string` | Zona horaria del usuario
`native_line_id` | `null,` `string` | [PII] ID de línea del usuario desde el que se envió o recibió el mensaje
`line_channel_id` | `null,` `string` | El ID del canal LINE al que se envió o del que se recibió el mensaje
`line_channel_name` | `null,` `string` | El nombre del canal LINE al que se envió o del que se recibió el mensaje
`subscription_group_api_id` | `string` | ID API del grupo de suscripción
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`campaign_name` | `null,` `string` | Nombre de la campaña
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`canvas_step_name` | `null,` `string` | Nombre del paso en Canvas
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`device_id` | `null,` `string` | ID del dispositivo en el que se ha producido el evento
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`is_suspected_bot_click` | `null, boolean` | Si este evento se procesó como un evento bot
`short_url` | `null,` `string` | URL acortada en la que se ha hecho clic
`url` | `null,` `string` | URL en la que ha hecho clic el usuario
`user_agent` | `null,` `string` | Agente de usuario en el que se produjo el informe de spam
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`app_group_api_id` | `null,` `string` | API ID del grupo de aplicaciones al que pertenece este usuario
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`id` | `string` | ID global único para este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el suceso
`user_id` | `string` | Braze ID de usuario del usuario que realizó este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`campaign_name` | `null,` `string` | Nombre de la campaña
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`canvas_step_name` | `null,` `string` | Nombre del paso en Canvas
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`device_id` | `null,` `string` | ID del dispositivo en el que se ha producido el evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`line_channel_id` | `null,` `string` | El ID del canal LINE al que se envió o del que se recibió el mensaje
`line_channel_name` | `null,` `string` | El nombre del canal LINE al que se envió o del que se recibió el mensaje
`media_id` | `null,` `string` | El ID generado por LINE que puede utilizarse para recuperar medios entrantes de LINE
`message_body` | `null,` `string` | Respuesta escrita del usuario
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`native_line_id` | `null,` `string` | [PII] ID de línea del usuario desde el que se envió o recibió el mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`subscription_group_api_id` | `string` | ID API del grupo de suscripción
`timezone` | `null,` `string` | Zona horaria del usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_SEND_SHARED {#USERS_MESSAGES_LINE_SEND_SHARED}

Campo | Tipo | Descripción
------|------|------------
`app_group_api_id` | `null,` `string` | API ID del grupo de aplicaciones al que pertenece este usuario
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`id` | `string` | ID global único para este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el suceso
`user_id` | `string` | Braze ID de usuario del usuario que realizó este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`campaign_name` | `null,` `string` | Nombre de la campaña
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`canvas_step_name` | `null,` `string` | Nombre del paso en Canvas
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`device_id` | `null,` `string` | ID del dispositivo en el que se ha producido el evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`line_channel_id` | `null,` `string` | El ID del canal LINE al que se envió o del que se recibió el mensaje
`line_channel_name` | `null,` `string` | El nombre del canal LINE al que se envió o del que se recibió el mensaje
`message_extras` | `null,` `string` | [PII] Una cadena JSON de los pares clave-valor etiquetados durante la renderización de Liquid.
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`native_line_id` | `null,` `string` | [PII] ID de línea del usuario desde el que se envió o recibió el mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`subscription_group_api_id` | `string` | ID API del grupo de suscripción
`timezone` | `null,` `string` | Zona horaria del usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED {#USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID de usuario del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el suceso
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`activity_id` | `null,` `string` | Identificador de actividad en vivo
`activity_attributes_type` | `null,` `string` | Tipo de atributo de actividad en vivo
`push_to_start_token` | `null,` `string` | Token de notificaciones push de actividad en vivo
`update_token` | `null,` `string` | Token de actualización de actividad en vivo
`live_activity_event_type` | `null,` `string` | Tipo de evento de Actividad en vivo. Una de ['inicio', 'actualización', 'fin'].
`live_activity_event_outcome` | `null,` `string` | Resultado de la actividad en vivo
`app_group_api_id` | `null,` `string` | API ID del grupo de aplicaciones al que pertenece este usuario
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se ha producido este evento
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED {#USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID de usuario del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el suceso
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`activity_id` | `null,` `string` | Identificador de actividad en vivo
`activity_attributes_type` | `null,` `string` | Tipo de atributo de actividad en vivo
`push_to_start_token` | `null,` `string` | Token de notificaciones push de actividad en vivo
`update_token` | `null,` `string` | Token de actualización de actividad en vivo
`live_activity_event_type` | `null,` `string` | Tipo de evento de Actividad en vivo. Una de ['inicio', 'actualización', 'fin'].
`app_group_api_id` | `null,` `string` | API ID del grupo de aplicaciones al que pertenece este usuario
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se ha producido este evento
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID de usuario del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`app_group_api_id` | `null,` `string` | API ID del grupo de aplicaciones al que pertenece este usuario
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el suceso
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se ha producido este evento
`card_api_id` | `null,` `string` | ID de API de la tarjeta
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`device_id` | `null,` `string` | ID del dispositivo en el que se ha producido el evento
`sdk_version` | `null,` `string` | Versión del SDK Braze en uso durante el evento
`platform` | `null,` `string` | Plataforma del dispositivo
`os_version` | `null,` `string` | Versión del sistema operativo del dispositivo
`device_model` | `null,` `string` | Modelo del dispositivo
`resolution` | `null,` `string` | Resolución del dispositivo
`carrier` | `null,` `string` | Operador del dispositivo
`browser` | `null,` `string` | Navegador del dispositivo -extraído de user_agent \- en el que se produjo la apertura
`abort_type` | `null,` `string` | Tipo de aborto, uno de ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] Mensaje de registro que describe los detalles de la interrupción (hasta 128 caracteres)
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID de usuario del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`app_group_api_id` | `null,` `string` | API ID del grupo de aplicaciones al que pertenece este usuario
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el suceso
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se ha producido este evento
`card_api_id` | `null,` `string` | ID de API de la tarjeta
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`device_id` | `null,` `string` | ID del dispositivo en el que se ha producido el evento
`sdk_version` | `null,` `string` | Versión del SDK Braze en uso durante el evento
`platform` | `null,` `string` | Plataforma del dispositivo
`os_version` | `null,` `string` | Versión del sistema operativo del dispositivo
`device_model` | `null,` `string` | Modelo del dispositivo
`resolution` | `null,` `string` | Resolución del dispositivo
`carrier` | `null,` `string` | Operador del dispositivo
`browser` | `null,` `string` | Navegador del dispositivo -extraído de user_agent \- en el que se produjo la apertura
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID de usuario del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`app_group_api_id` | `null,` `string` | API ID del grupo de aplicaciones al que pertenece este usuario
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el suceso
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se ha producido este evento
`card_api_id` | `null,` `string` | ID de API de la tarjeta
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`device_id` | `null,` `string` | ID del dispositivo en el que se ha producido el evento
`sdk_version` | `null,` `string` | Versión del SDK Braze en uso durante el evento
`platform` | `null,` `string` | Plataforma del dispositivo
`os_version` | `null,` `string` | Versión del sistema operativo del dispositivo
`device_model` | `null,` `string` | Modelo del dispositivo
`resolution` | `null,` `string` | Resolución del dispositivo
`carrier` | `null,` `string` | Operador del dispositivo
`browser` | `null,` `string` | Navegador del dispositivo -extraído de user_agent \- en el que se produjo la apertura
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`device_id` | `null,` `string` | `device_id` al que hicimos un intento de entrega
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se ha producido este evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`platform` | `string` | Plataforma del dispositivo
`abort_type` | `null,` `string` | Tipo de aborto, uno de ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] Mensaje de registro que describe los detalles de la interrupción (máximo de 2.000 caracteres)
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`push_token` | `null,` `string` | Token de notificaciones push que rebotó
`device_id` | `null,` `string` | `device_id` que hicimos un intento de entrega que rebotó
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se ha producido este evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`platform` | `null,` `string` | Plataforma del dispositivo
`ad_id` | `null,` `string` | [PII] ID de publicidad del dispositivo al que hicimos un intento de entrega
`ad_id_type` | `null,` `string` | Tipo de identificador publicitario
`ad_tracking_enabled` | `null, boolean` | Si el seguimiento está activado o no para la publicidad
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se ha producido este evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`device_id` | `null,` `string` | ID del dispositivo en el que se ha producido el evento
`sdk_version` | `null,` `string` | Versión del SDK Braze en uso durante el evento
`platform` | `null,` `string` | Plataforma del dispositivo
`os_version` | `null,` `string` | Versión del sistema operativo del dispositivo
`device_model` | `null,` `string` | Modelo del dispositivo
`resolution` | `null,` `string` | Resolución del dispositivo
`carrier` | `null,` `string` | Operador del dispositivo
`browser` | `null,` `string` | Navegador del dispositivo
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED}

{% alert important %}
Este evento no es compatible con el [SDK de Swift](https://github.com/braze-inc/braze-swift-sdk) y está obsoleto en el [SDK de Obj-C](https://github.com/Appboy/appboy-ios-sdk).
{% endalert %}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se ha producido este evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`device_id` | `null,` `string` | ID del dispositivo en el que se ha producido el evento
`sdk_version` | `null,` `string` | Versión del SDK Braze en uso durante el evento
`platform` | `null,` `string` | Plataforma del dispositivo
`os_version` | `null,` `string` | Versión del sistema operativo del dispositivo
`device_model` | `null,` `string` | Modelo del dispositivo
`resolution` | `null,` `string` | Resolución del dispositivo
`carrier` | `null,` `string` | Operador del dispositivo
`browser` | `null,` `string` | Navegador del dispositivo
`ad_id` | `null,` `string` | [PII] ID de publicidad del dispositivo al que hicimos un intento de entrega
`ad_id_type` | `null,` `string` | Tipo de identificador publicitario
`ad_tracking_enabled` | `null, boolean` | Si el seguimiento está activado o no para la publicidad
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se ha producido este evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`device_id` | `null,` `string` | ID del dispositivo en el que se ha producido el evento
`sdk_version` | `null,` `string` | Versión del SDK Braze en uso durante el evento
`platform` | `null,` `string` | Plataforma del dispositivo
`os_version` | `null,` `string` | Versión del sistema operativo del dispositivo
`device_model` | `null,` `string` | Modelo del dispositivo
`resolution` | `null,` `string` | Resolución del dispositivo
`carrier` | `null,` `string` | Operador del dispositivo
`browser` | `null,` `string` | Navegador del dispositivo
`button_string` | `null,` `string` | Identificador (button_string) del botón de notificación push pulsado. null si no procede de un clic en el botón
`button_action_type` | `null,` `string` | Tipo de acción del botón de notificación push. Uno de [URI, DEEP_LINK, NONE, CLOSE]. null si no procede de un clic en el botón
`slide_id` | `null,` `string` | Identificador de la diapositiva del carrusel push en la que el usuario hace clic
`slide_action_type` | `null,` `string` | Tipo de acción de la corredera del carrusel de empuje
`ad_id` | `null,` `string` | [PII] ID de publicidad del dispositivo al que hicimos un intento de entrega
`ad_id_type` | `null,` `string` | Tipo de identificador publicitario
`ad_tracking_enabled` | `null, boolean` | Si el seguimiento está activado o no para la publicidad
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`push_token` | `null,` `string` | Token de notificaciones push al que hicimos un intento de entrega
`device_id` | `null,` `string` | `device_id` al que hicimos un intento de entrega
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`app_api_id` | `null,` `string` | ID de API de la aplicación en la que se ha producido este evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`platform` | `string` | Plataforma del dispositivo
`ad_id` | `null,` `string` | [PII] ID de publicidad del dispositivo al que hicimos un intento de entrega
`ad_id_type` | `null,` `string` | Tipo de identificador publicitario
`ad_tracking_enabled` | `null, boolean` | Si el seguimiento está activado o no para la publicidad
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`message_extras` | `null,` `string` | [PII] Una cadena JSON de los pares clave-valor etiquetados durante la renderización de Liquid.
`is_sampled` | `null,` `string` | Indica si el envío push fue muestreado y se esperaba un evento de entrega
`locale_key` | `null,` `string` | [PII] La clave correspondiente a las traducciones (por ejemplo "en-us") utilizadas para componer este mensaje (nula por defecto).
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_ABORT_SHARED {#USERS_MESSAGES_RCS_ABORT_SHARED}

Campo | Tipo | Descripción
------|------|------------
`app_group_api_id` | `null,` `string` | API ID del grupo de aplicaciones al que pertenece este usuario
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`id` | `string` | ID global único para este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el suceso
`user_id` | `string` | Braze ID de usuario del usuario que realizó este evento
`abort_log` | `null,` `string` | [PII] Mensaje de registro que describe los detalles de la interrupción (hasta 128 caracteres)
`abort_type` | `null,` `string` | Tipo de aborto, uno de ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`campaign_name` | `null,` `string` | Nombre de la campaña
`canvas_id` | `null,` `string` | ID BSON del Canvas al que pertenece este evento
`canvas_name` | `null,` `string` | Nombre del Canvas
`canvas_step_name` | `null,` `string` | Nombre del paso en Canvas
`canvas_variation_name` | `null,` `string` | Nombre de la variación de Canvas que recibió este usuario
`message_variation_name` | `null,` `string` | Nombre de la variación del mensaje
`subscription_group_api_id` | `string` | ID API del grupo de suscripción
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_CLICK_SHARED {#USERS_MESSAGES_RCS_CLICK_SHARED}

Campo | Tipo | Descripción
------|------|------------
`app_group_api_id` | `null,` `string` | API ID del grupo de aplicaciones al que pertenece este usuario
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`id` | `string` | ID global único para este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el suceso
`user_id` | `string` | Braze ID de usuario del usuario que realizó este evento
`campaign_name` | `null,` `string` | Nombre de la campaña
`canvas_id` | `null,` `string` | ID BSON del Canvas al que pertenece este evento
`canvas_name` | `null,` `string` | Nombre del Canvas
`canvas_step_name` | `null,` `string` | Nombre del paso en Canvas
`device_id` | `null,` `string` | ID del dispositivo en el que se ha producido el evento
`is_suspected_bot_click` | `null, boolean` | Si este evento se procesó como un evento bot
`message_variation_name` | `null,` `string` | Nombre de la variación del mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`short_url` | `null,` `string` | URL acortada en la que se ha hecho clic
`suspected_bot_click_reason` | `null,` `string` | Por qué este evento fue clasificado como bot
`user_agent` | `null,` `string` | Agente de usuario en el que se produjo el informe de spam
`user_phone_number` | `null,` `string` | [PII] Número de teléfono del usuario desde el que se recibió el mensaje
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`interaction_type` | `null,` `string` | El tipo de interacción que generó el clic. Ejemplo de valores de cadena: Texto URL, Responder, OpenURL
`element_label` | `null,` `string` | Detalles opcionales sobre el elemento en el que se ha hecho clic, como el texto de una respuesta sugerida o un botón
`element_type` | `null,` `string` | Especifica si un interaction_type común a sugerencias y botones procede de una sugerencia o de un botón. Ejemplos: Sugerencia, botón
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`url` | `null,` `string` | URL en la que ha hecho clic el usuario
`subscription_group_api_id` | `string` | ID API del grupo de suscripción
`canvas_variation_name` | `null,` `string` | Nombre de la variación de Canvas que recibió este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_DELIVERY_SHARED {#USERS_MESSAGES_RCS_DELIVERY_SHARED}

Campo | Tipo | Descripción
------|------|------------
`app_group_api_id` | `null,` `string` | API ID del grupo de aplicaciones al que pertenece este usuario
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`id` | `string` | ID global único para este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el suceso
`user_id` | `string` | Braze ID de usuario del usuario que realizó este evento
`campaign_name` | `null,` `string` | Nombre de la campaña
`canvas_id` | `null,` `string` | ID BSON del Canvas al que pertenece este evento
`canvas_name` | `null,` `string` | Nombre del Canvas
`canvas_step_name` | `null,` `string` | Nombre del paso en Canvas
`canvas_variation_name` | `null,` `string` | Nombre de la variación de Canvas que recibió este usuario
`device_id` | `null,` `string` | ID del dispositivo en el que se ha producido el evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`message_variation_name` | `null,` `string` | Nombre de la variación del mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`subscription_group_api_id` | `string` | ID API del grupo de suscripción
`to_phone_number` | `null,` `string` | [PII] Número de teléfono del usuario que recibe el mensaje en formato e.164 (por ejemplo +14155552671)
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`from_rcs_sender` | `null,` `string` | El ID del remitente RCS o el nombre del agente utilizado para enviar el mensaje
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`app_group_api_id` | `null,` `string` | API ID del grupo de aplicaciones al que pertenece este usuario
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`id` | `string` | ID global único para este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el suceso
`user_id` | `string` | Braze ID de usuario del usuario que realizó este evento
`action` | `null,` `string` | Acción realizada en respuesta a este mensaje. (por ejemplo Suscrito, Desuscrito o Ninguna).
`campaign_name` | `null,` `string` | Nombre de la campaña
`canvas_id` | `null,` `string` | ID BSON del Canvas al que pertenece este evento
`canvas_name` | `null,` `string` | Nombre del Canvas
`canvas_step_name` | `null,` `string` | Nombre del paso en Canvas
`media_urls` | `null,` `string` | URL multimedia del usuario
`message_variation_name` | `null,` `string` | Nombre de la variación del mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`user_phone_number` | `null,` `string` | [PII] Número de teléfono del usuario desde el que se recibió el mensaje
`subscription_group_api_id` | `string` | ID API del grupo de suscripción
`message_body` | `null,` `string` | Respuesta escrita del usuario
`to_rcs_sender` | `null,` `string` | El remitente RCS entrante al que se envió el mensaje
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`campaign_id` | `null,` `string` | ID BSON de la campaña a la que pertenece este evento
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_READ_SHARED {#USERS_MESSAGES_RCS_READ_SHARED}

Campo | Tipo | Descripción
------|------|------------
`app_group_api_id` | `null,` `string` | API ID del grupo de aplicaciones al que pertenece este usuario
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`id` | `string` | ID global único para este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el suceso
`user_id` | `string` | Braze ID de usuario del usuario que realizó este evento
`campaign_name` | `null,` `string` | Nombre de la campaña
`canvas_id` | `null,` `string` | ID BSON del Canvas al que pertenece este evento
`canvas_name` | `null,` `string` | Nombre del Canvas
`canvas_step_name` | `null,` `string` | Nombre del paso en Canvas
`canvas_variation_name` | `null,` `string` | Nombre de la variación de Canvas que recibió este usuario
`message_variation_name` | `null,` `string` | Nombre de la variación del mensaje
`to_phone_number` | `null,` `string` | [PII] Número de teléfono del usuario que recibe el mensaje en formato e.164 (por ejemplo +14155552671)
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_REJECTION_SHARED {#USERS_MESSAGES_RCS_REJECTION_SHARED}

Campo | Tipo | Descripción
------|------|------------
`app_group_api_id` | `null,` `string` | API ID del grupo de aplicaciones al que pertenece este usuario
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`id` | `string` | ID global único para este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el suceso
`user_id` | `string` | Braze ID de usuario del usuario que realizó este evento
`campaign_name` | `null,` `string` | Nombre de la campaña
`canvas_id` | `null,` `string` | ID BSON del Canvas al que pertenece este evento
`canvas_name` | `null,` `string` | Nombre del Canvas
`canvas_step_name` | `null,` `string` | Nombre del paso en Canvas
`canvas_variation_name` | `null,` `string` | Nombre de la variación de Canvas que recibió este usuario
`device_id` | `null,` `string` | ID del dispositivo en el que se ha producido el evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`error` | `null,` `string` | Nombre del error
`from_rcs_sender` | `null,` `string` | El ID del remitente RCS o el nombre del agente utilizado para enviar el mensaje
`is_sms_fallback` | `null, boolean` | Indica si se intentó una alternativa SMS para este mensaje RCS rechazado. Está vinculado/emparejado al evento Entrega SMS
`message_variation_name` | `null,` `string` | Nombre de la variación del mensaje
`provider_error_code` | `null,` `string` | Código de error del proveedor
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`subscription_group_api_id` | `string` | ID API del grupo de suscripción
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`to_phone_number` | `null,` `string` | [PII] Número de teléfono del usuario que recibe el mensaje en formato e.164 (por ejemplo +14155552671)
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_SEND_SHARED {#USERS_MESSAGES_RCS_SEND_SHARED}

Campo | Tipo | Descripción
------|------|------------
`app_group_api_id` | `null,` `string` | API ID del grupo de aplicaciones al que pertenece este usuario
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`id` | `string` | ID global único para este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el suceso
`user_id` | `string` | Braze ID de usuario del usuario que realizó este evento
`campaign_name` | `null,` `string` | Nombre de la campaña
`canvas_id` | `null,` `string` | ID BSON del Canvas al que pertenece este evento
`canvas_name` | `null,` `string` | Nombre del Canvas
`canvas_step_name` | `null,` `string` | Nombre del paso en Canvas
`canvas_variation_name` | `null,` `string` | Nombre de la variación de Canvas que recibió este usuario
`category` | `null,` `string` | Nombre de la categoría de palabras clave, sólo rellenado para mensajes de respuesta automática: "adhesión voluntaria", "exclusión voluntaria", "ayuda" o valor personalizado.
`device_id` | `null,` `string` | ID del dispositivo en el que se ha producido el evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`from_rcs_sender` | `null,` `string` | El ID del remitente RCS o el nombre del agente utilizado para enviar el mensaje
`message_extras` | `null,` `string` | Una cadena JSON de los pares clave-valor etiquetados durante la renderización de Liquid
`message_variation_name` | `null,` `string` | Nombre de la variación del mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`subscription_group_api_id` | `string` | ID API del grupo de suscripción
`to_phone_number` | `null,` `string` | [PII] Número de teléfono del usuario que recibe el mensaje en formato e.164 (por ejemplo +14155552671)
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_ABORT_SHARED {#USERS_MESSAGES_SMS_ABORT_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`subscription_group_api_id` | `null,` `string` | ID externo del grupo de suscripción
`abort_type` | `null,` `string` | Tipo de aborto, uno de ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] Mensaje de registro que describe los detalles de la interrupción (máximo de 2.000 caracteres)
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_CARRIERSEND_SHARED {#USERS_MESSAGES_SMS_CARRIERSEND_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`device_id` | `null,` `string` | `device_id` que está vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`to_phone_number` | `null,` `string` | [PII] número de teléfono del destinatario
`from_phone_number` | `null,` `string` | número de teléfono desde el que se envió el mensaje SMS
`subscription_group_api_id` | `null,` `string` | ID externo del grupo de suscripción
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_DELIVERY_SHARED {#USERS_MESSAGES_SMS_DELIVERY_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`device_id` | `null,` `string` | `device_id` que está vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`to_phone_number` | `null,` `string` | [PII] número de teléfono del destinatario
`from_phone_number` | `null,` `string` | Número de teléfono desde el que se envió el mensaje SMS
`subscription_group_api_id` | `null,` `string` | ID externo del grupo de suscripción
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`is_sms_fallback` | `null, boolean` | Indica si se intentó una alternativa SMS para este mensaje RCS rechazado. Está vinculado/emparejado al evento Entrega SMS
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED {#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`device_id` | `null,` `string` | `device_id` que está vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`to_phone_number` | `null,` `string` | [PII] número de teléfono del destinatario
`subscription_group_api_id` | `null,` `string` | ID externo del grupo de suscripción
`error` | `null,` `string` | nombre del error
`provider_error_code` | `null,` `string` | código de error del proveedor de servicios SMS
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`is_sms_fallback` | `null, boolean` | Indica si se intentó una alternativa SMS para este mensaje RCS rechazado. Está vinculado/emparejado al evento Entrega SMS
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `null,` `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`app_group_api_id` | `null,` `string` | ID de API del espacio de trabajo asociado al número de teléfono de entrada
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`user_phone_number` | `string` | [PII] el número de teléfono del usuario desde el que se recibió el mensaje
`subscription_group_id` | `null,` `string` | ID del grupo de suscripción al que va dirigido este mensaje SMS
`subscription_group_api_id` | `null,` `string` | ID de API del grupo de suscripción al que va dirigido este mensaje SMS
`inbound_phone_number` | `string` | Número de entrada al que se envió el mensaje
`action` | `string` | Acción tomada en respuesta a este mensaje. Por ejemplo, `Subscribed`, `Unsubscribed`, o `None`.
`message_body` | `string` | Respuesta del usuario
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | URL multimedia del usuario
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje a la que pertenece este evento
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas al que pertenece este evento
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_REJECTION_SHARED {#USERS_MESSAGES_SMS_REJECTION_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`device_id` | `null,` `string` | `device_id` que está vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`to_phone_number` | `null,` `string` | [PII] número de teléfono del destinatario
`from_phone_number` | `null,` `string` | número de teléfono desde el que se envió el mensaje SMS
`subscription_group_api_id` | `null,` `string` | ID externo del grupo de suscripción
`error` | `null,` `string` | nombre del error
`provider_error_code` | `null,` `string` | código de error del proveedor de servicios SMS
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`is_sms_fallback` | `null, boolean` | Indica si se intentó una alternativa SMS para este mensaje RCS rechazado. Está vinculado/emparejado al evento Entrega SMS
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_SEND_SHARED {#USERS_MESSAGES_SMS_SEND_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`device_id` | `null,` `string` | `device_id` que está vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`to_phone_number` | `null,` `string` | [PII] número de teléfono del destinatario
`subscription_group_api_id` | `null,` `string` | ID externo del grupo de suscripción
`category` | `null,` `string` | Nombre de la categoría de palabras clave, sólo se rellena para los mensajes de respuesta automática: Opt-in", "Opt-out", "Ayuda" o valor personalizado
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`message_extras` | `null,` `string` | [PII] Una cadena JSON de los pares clave-valor etiquetados durante la renderización de Liquid.
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED {#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `null,` `string` | ID de Braze del usuario al que se dirige short_url, nulo si short_url no utilizó el seguimiento de clics del usuario
`external_user_id` | `null,` `string` | [PII] ID externo del usuario al que se dirige short_url si existe, nulo si short_url no utilizó el seguimiento de clics del usuario.
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo utilizado para generar short_url
`time` | `int` | Marca de tiempo Unix en la que se hizo clic en short_url 
`timezone` | `null,` `string` | Zona horaria del usuario
`campaign_id` | `null,` `string` | Braze ID de la campaña para la que se generó short_url, null si no es de una campaña
`campaign_api_id` | `null,` `string` | API ID de la campaña para la que se generó short_url, null si no es de una campaña
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje para la que se generó short_url, null si no es de una campaña
`canvas_id` | `null,` `string` | Braze ID del Canvas para el que se generó short_url, null si no es de un Canvas
`canvas_api_id` | `null,` `string` | API ID del Canvas para el que se generó short_url, null si no es de un Canvas
`canvas_variation_api_id` | `null,` `string` | API ID de la variación del Canvas para la que se generó short_url, null si no es de un Canvas
`canvas_step_api_id` | `null,` `string` | API ID del paso en Canvas para el que se generó short_url, null si no es de un Canvas
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso en Canvas para el que se generó short_url, null si no es de un Canvas
`url` | `string` | URL original contenida en el mensaje al que se redirige mediante short_url
`short_url` | `string` | URL acortada en la que se ha hecho clic
`user_agent` | `null,` `string` | agente usuario solicitante short_url
`user_phone_number` | `string` | [PII] número de teléfono del usuario
`device_id` | `null,` `string` | ID del dispositivo en el que se ha producido el evento
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`is_suspected_bot_click` | `null, boolean` | Si este evento se procesó como un evento bot
`suspected_bot_click_reason` | `null, object` | Por qué este evento fue clasificado como bot
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_ABORT_SHARED {#USERS_MESSAGES_WEBHOOK_ABORT_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`device_id` | `null,` `string` | `device_id` que está vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`abort_type` | `null,` `string` | Tipo de aborto, uno de ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] Mensaje de registro que describe los detalles de la interrupción (máximo de 2.000 caracteres)
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_WEBHOOK_FAILURE_SHARED {#USERS_MESSAGES_WEBHOOK_FAILURE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`http_status_code` | `null, int` | Código de estado HTTP de la respuesta
`endpoint_url` | `null,` `string` | La url del punto final que se solicita
`app_group_api_id` | `null,` `string` | API ID del grupo de aplicaciones al que pertenece este usuario
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`campaign_id` | `null,` `string` | ID BSON de la campaña a la que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_id` | `null,` `string` | ID BSON del Canvas al que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`content_length` | `null, int` | Longitud del contenido de la respuesta
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`host` | `null,` `string` | El host de la petición
`id` | `string` | ID global único para este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`raw_response` | `null,` `string` | Respuesta bruta truncada del punto final
`retry_count` | `null, int` | El número de reintentos intentados
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el suceso
`url_path` | `null,` `string` | La ruta de la url solicitada
`user_id` | `string` | Braze ID de usuario del usuario que realizó este evento
`webhook_duration` | `null, int` | Duración total de esta petición en milisegundos
`webhook_failure_source` | `null,` `string` | Para saber si un error ha sido creado por Braze o por el propio punto final. El campo de origen podría ser Punto final externo, No tratar código de estado a host inalcanzable
`is_terminal` | `null, boolean` | Si este suceso fue el intento terminal en un envío
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_SEND_SHARED {#USERS_MESSAGES_WEBHOOK_SEND_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`device_id` | `null,` `string` | `device_id` que está vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`gender` | `null,` `string` | [PII] Sexo del usuario
`country` | `null,` `string` | [PII] País del usuario
`timezone` | `null,` `string` | Zona horaria del usuario
`language` | `null,` `string` | [PII] Idioma del usuario
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`message_extras` | `null,` `string` | [PII] Una cadena JSON de los pares clave-valor etiquetados durante la renderización de Liquid.
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_ABORT_SHARED {#USERS_MESSAGES_WHATSAPP_ABORT_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`to_phone_number` | 	`null,` `string` | [PII] número de teléfono del destinatario
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`device_id` | `null,` `string` | `device_id` que está vinculado a este usuario si el usuario es anónimo
`timezone` | `null,` `string` | Zona horaria del usuario
`app_group_id` | `null,` `string` | ID del espacio de trabajo al que pertenece este usuario
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`subscription_group_api_id` | `string` | ID API del grupo de suscripción
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`abort_type` | `null,` `string` | Tipo de aborto, uno de ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] Mensaje de registro que describe los detalles de la interrupción (máximo de 2.000 caracteres)
`sf_created_at` | `timestamp`, `null` | Cuando este evento fue recogido por el Snowpipe      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_WHATSAPP_CLICK_SHARED {#USERS_MESSAGES_WHATSAPP_CLICK_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`user_id` | `string` | Braze ID de usuario del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`device_id` | `null,` `string` | ID del dispositivo en el que se ha producido el evento
`app_group_id` | `null,` `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`app_group_api_id` | `null,` `string` | API ID del grupo de aplicaciones al que pertenece este usuario
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el suceso
`timezone` | `null,` `string` | Zona horaria del usuario
`campaign_id` | `null,` `string` | ID BSON de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID BSON del Canvas al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`url` | `null,` `string` | URL en la que ha hecho clic el usuario
`short_url` | `null,` `string` | URL acortada en la que se ha hecho clic
`user_agent` | `null,` `string` | Agente de usuario en el que se produjo el informe de spam
`user_phone_number` | `null,` `string` | [PII] Número de teléfono del usuario desde el que se recibió el mensaje
`sf_created_at` | `timestamp`, `null` | cuando este acontecimiento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED {#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`to_phone_number` | `null,` `string` | [PII] número de teléfono del destinatario
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`device_id` | `null,` `string` | `device_id` que está vinculado a este usuario si el usuario es anónimo
`timezone` | `null,` `string` | Zona horaria del usuario
`from_phone_number` | `null,` `string` | Número de teléfono desde el que se envió el mensaje de WhatsApp
`app_group_id` | `null,` `string` | ID del espacio de trabajo al que pertenece este usuario
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`subscription_group_api_id` | `string` | ID API del grupo de suscripción
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`sf_created_at` | `timestamp`, `null` | Cuando este evento fue recogido por el Snowpipe      
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`flow_id` | `null,` `string` | El ID único del Flujo en el administrador de WhatsApp. Presente si el usuario está respondiendo a un Flujo de WhatsApp.
`template_name` | `null,` `string` | [PII] Nombre de la plantilla en el administrador de WhatsApp. Presentar si se envía una plantilla de mensaje
`message_id` | `null,` `string` | El ID único generado por Meta para este mensaje
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_FAILURE_SHARED {#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`to_phone_number` | `null,` `string` | [PII] número de teléfono del destinatario
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`device_id` | `null,` `string` | `device_id` que está vinculado a este usuario si el usuario es anónimo
`timezone` | `null,` `string` | Zona horaria del usuario
`from_phone_number` | `null,` `string` | Número de teléfono desde el que se envió el mensaje de WhatsApp
`app_group_id` | `null,` `string` | ID del espacio de trabajo al que pertenece este usuario
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`subscription_group_api_id` | `string` | ID API del grupo de suscripción
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`provider_error_code` | `null,` `string` | Código de error de WhatsApp
`provider_error_title` | `null, ` `string` | Título de error de WhatsApp
`sf_created_at` | `timestamp`, `null` | Cuando este evento fue recogido por el Snowpipe      
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`message_id` | `null,` `string` | El ID único generado por Meta para este mensaje
`template_name` | `null,` `string` | [PII] Nombre de la plantilla en el administrador de WhatsApp. Presentar si se envía una plantilla de mensaje
`flow_id` | `null,` `string` | El ID único del Flujo en el administrador de WhatsApp. Presente si el usuario está respondiendo a un Flujo de WhatsApp.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`user_phone_number` | `string` | [PII] el número de teléfono del usuario desde el que se recibió el mensaje
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`inbound_phone_number` | `string` | Número de entrada al que se envió el mensaje
`device_id` | `null,` `string` | `device_id` que está vinculado a este usuario si el usuario es anónimo
`timezone` | `null,` `string` | Zona horaria del usuario
`app_group_id` | `null,` `string` | ID del espacio de trabajo al que pertenece este usuario
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`subscription_group_api_id` | `string` | ID API del grupo de suscripción
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`message_body` | `string` | Respuesta del usuario
`quick_reply_text` | `string` | Texto del botón pulsado por el usuario
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | URL multimedia del usuario
`action` | `string` | Acción tomada en respuesta a este mensaje. Por ejemplo, `Subscribed`, `Unsubscribed`, o `None`.
`sf_created_at` | `timestamp`, `null` | Cuando este evento fue recogido por el Snowpipe      
`catalog_id` | `null,` `string` | ID de catálogo de un producto si se hace referencia a un producto en el mensaje de entrada. Si no, vacío.
`product_id` | `null,` `string` | ID del producto adquirido
`flow_id` | `null,` `string` | El ID único del Flujo en el administrador de WhatsApp. Presente si el usuario está respondiendo a un Flujo de WhatsApp.
`flow_response_json` | `null,` `string` | [PII] Los valores del formulario con los que respondió el usuario. Presente si el usuario está respondiendo a un Flujo de WhatsApp.
`message_id` | `null,` `string` | El ID único generado por Meta para este mensaje
`in_reply_to` | `null,` `string` | La dirección message_id del mensaje al que respondía este mensaje
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_READ_SHARED {#USERS_MESSAGES_WHATSAPP_READ_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`to_phone_number` | `null,` `string` | [PII] número de teléfono del destinatario
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`device_id` | `null,` `string` | `device_id` que está vinculado a este usuario si el usuario es anónimo
`timezone` | `null,` `string` | Zona horaria del usuario
`from_phone_number` | `null,` `string` | Número de teléfono desde el que se envió el mensaje de WhatsApp
`app_group_id` | `null,` `string` | ID del espacio de trabajo al que pertenece este usuario
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`subscription_group_api_id` | `string` | ID API del grupo de suscripción
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`sf_created_at` | `timestamp`, `null` | Cuando este evento fue recogido por el Snowpipe      
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`template_name` | `null,` `string` | [PII] Nombre de la plantilla en el administrador de WhatsApp. Presentar si se envía una plantilla de mensaje
`message_id` | `null,` `string` | El ID único generado por Meta para este mensaje
`flow_id` | `null,` `string` | El ID único del Flujo en el administrador de WhatsApp. Presente si el usuario está respondiendo a un Flujo de WhatsApp.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_SEND_SHARED {#USERS_MESSAGES_WHATSAPP_SEND_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID global único para este evento
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`to_phone_number` | `null,` `string`	| [PII] número de teléfono del destinatario
`user_id` | `string` | Braze ID del usuario que realizó este evento
`external_user_id` | `null,` `string` | [PII] ID externo del usuario
`device_id` | `null,` `string` | `device_id` que está vinculado a este usuario si el usuario es anónimo
`timezone` | `null,` `string` | Zona horaria del usuario
`from_phone_number` | `null,` `string` | número de teléfono desde el que se envió el mensaje de WhatsApp
`app_group_id` | `null,` `string` | ID del espacio de trabajo al que pertenece este usuario
`app_group_api_id` | `null,` `string` | API ID del espacio de trabajo al que pertenece este usuario
`subscription_group_api_id` | `string` | ID API del grupo de suscripción
`campaign_id` | `null,` `string` | ID Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,` `string` | API ID de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,` `string` | API ID de la variación de mensaje que recibió este usuario
`canvas_id` | `null,` `string` | ID Braze de uso interno del lienzo al que pertenece este evento
`canvas_api_id` | `null,` `string` | API ID del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,` `string` | API ID de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,` `string` | API ID del paso Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de la variación del mensaje del paso Canvas que recibió este usuario
`dispatch_id` | `null,` `string` | ID del envío al que pertenece este mensaje
`message_extras` | `null,` `string` | [PII] Una cadena JSON de los pares clave-valor etiquetados durante la renderización de Liquid.
`sf_created_at` | `timestamp`, `null` | Cuando este evento fue recogido por el Snowpipe      
`send_id` | `null,` `string` | ID de envío del mensaje al que pertenece este mensaje
`flow_id` | `null,` `string` | El ID único del Flujo en el administrador de WhatsApp. Presente si el usuario está respondiendo a un Flujo de WhatsApp.
`template_name` | `null,` `string` | [PII] Nombre de la plantilla en el administrador de WhatsApp. Presentar si se envía una plantilla de mensaje
`message_id` | `null,` `string` | El ID único generado por Meta para este mensaje
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Usuarios

### USERS_RANDOMBUCKETNUMBERUPDATE_SHARED {#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED}

| Campo                       | Tipo                     | Descripción                                        |
| --------------------------- | ------------------------ | -------------------------------------------------- |
| `id`                        | `string`, `null`    | ID global único para este evento                  |
| `app_group_id`              | `string`, `null`    | Braze ID del espacio de trabajo al que pertenece este usuario      |
| `app_group_api_id`          | `string`, `null`    | API ID del espacio de trabajo al que pertenece este usuario       |
| `user_id`                   | `string`, `null`    | Braze ID del usuario que realizó este evento      |
| `external_user_id`          | `string`, `null`    | [PII] ID externo del usuario                 |
| `time`                      | `int`, `null`       | Marca de tiempo Unix en la que ocurrió el evento         |
| `random_bucket_number`      | `int`, `null`       | Número de cubo aleatorio actual asignado al usuario  |
| `prev_random_bucket_number` | `int`, `null`       | Número de cubo aleatorio anterior asignado al usuario |
| `sf_created_at`             | `timestamp`, `null` | Cuando este evento fue recogido por el Snowpipe      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_USERDELETEREQUEST_SHARED {#USERS_USERDELETEREQUEST_SHARED}

| Campo              | Tipo                     | Descripción                                                   |
| ------------------ | ------------------------ | ------------------------------------------------------------- |
| `id`               | `string`, `null`    | ID global único para este evento                             |
| `user_id`          | `string`, `null`    | Braze ID del usuario que fue eliminado                          |
| `app_group_id`     | `string`, `null`    | Braze ID del espacio de trabajo al que pertenece este usuario                 |
| `app_group_api_id` | `string`, `null`    | API ID del espacio de trabajo al que pertenece este usuario                  |
| `time`             | `int`, `null`       | Marca de tiempo Unix en la que se procesó la solicitud de eliminación de usuario |
| `sf_created_at`    | `timestamp`, `null` | Cuando este evento fue recogido por el Snowpipe                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_USERORPHAN_SHARED {#USERS_USERORPHAN_SHARED}

| Campo              | Tipo                     | Descripción                                                                   |
| ------------------ | ------------------------ | ----------------------------------------------------------------------------- |
| `id`               | `string`, `null`    | ID global único para este evento                                             |
| `user_id`          | `string`, `null`    | Braze ID del usuario que quedó huérfano                                         |
| `external_user_id` | `string`, `null`    | [PII] ID externo del usuario                                            |
| `device_id`        | `string`, `null`    | ID del dispositivo que está vinculado a este usuario, si el usuario es anónimo          |
| `app_group_id`     | `string`, `null`    | Braze ID del espacio de trabajo al que pertenece este usuario                                 |
| `app_group_api_id` | `string`, `null`    | API ID del espacio de trabajo al que pertenece este usuario                                  |
| `app_api_id`       | `string`, `null`    | API ID de la aplicación a la que pertenecía el usuario huérfano                               |
| `time`             | `int`, `null`       | Marca de tiempo Unix en la que el usuario quedó huérfano                                 |
| `orphaned_by_id`   | `string`, `null`    | Braze ID del usuario cuyo perfil se fusionó con el perfil del usuario huérfano |
| `sf_created_at`    | `timestamp`, `null` | Cuando este evento fue recogido por el Snowpipe                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
