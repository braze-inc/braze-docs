---
nav_title: Actos de interacción con mensajes
layout: message_engagement_events_glossary
alias: /message_events_glossary/
page_order: 5
excerpt_separator: ""
page_type: glossary
description: "Este glosario enumera los distintos Eventos de interacción de mensajes que Braze puede seguir y enviar a los Almacenes de datos elegidos mediante Currents."
tool: Currents
search_rank: 6
---

Los esquemas de almacenamiento se aplican a los datos de eventos de archivo plano que enviamos a los socios de almacenamiento de almacén de datos (Google Cloud Storage, Amazon S3 y Microsoft Azure Blob Storage). Para los esquemas que se aplican a los demás socios, consulta nuestra lista de [socios disponibles]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) y comprueba sus respectivas páginas.

Ponte en contacto con tu director de cuentas o abre un [ticket de soporte]({{site.baseurl}}/braze_support/) si necesitas acceder a derechos de eventos adicionales. Si no encuentras lo que necesitas en este artículo, consulta nuestra [Biblioteca de eventos de comportamiento del cliente]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) o nuestros [ejemplos de datos de muestra de Currents](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explanation of message engagement event structure and platform values %}

### Estructura del acontecimiento

Este desglose de eventos muestra qué tipo de información se incluye generalmente en un evento de interacción de mensajes. Con una sólida comprensión de sus componentes, tus desarrolladores y el equipo de estrategia de inteligencia empresarial pueden utilizar los datos de eventos Currents entrantes para elaborar informes y gráficos basados en datos, y aprovechar otras valiosas métricas de datos.

\![Desglose de un evento de interacción de mensajes que muestra un evento de cancelar suscripción por correo electrónico con las propiedades de la lista agrupadas por propiedades específicas del usuario, propiedades de seguimiento de campaña o Canvas y propiedades específicas del evento]({% image_buster /assets/img/message_engagement_event.png %})

Los eventos de interacción de mensajes se componen de propiedades **específicas de usuario**, propiedades de **seguimiento de campaña/lienzo** y propiedades **específicas de evento**.

### Esquema de ID de usuario

Nota las convenciones de nomenclatura para los ID de usuario.

| Esquema Braze | Esquema Currents | Descripción |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | El identificador único que asigna automáticamente Braze. |
| `external_id` | `"EXTERNAL_USER_ID"` | El identificador único del perfil de un usuario configurado por el cliente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Valores de la plataforma

Algunos eventos devuelven un valor `platform` que especifica la plataforma del dispositivo del usuario.
<br>La siguiente tabla detalla los posibles valores devueltos:

| Dispositivo del usuario | Valor de la plataforma |
| --- | --- |
| iOS | `ios` |
| Android | `android` |
| FireTV | `kindle` |
| Kindle | `kindle` |
| Web | `web` |
| tvOS | `tvos` |
| Roku | `roku` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% enddetails %}

{% alert important %}
Currents eliminará los eventos con cargas útiles excesivamente grandes, superiores a 900 KB.
{% endalert %}

{% alert note %}
Los objetos relacionados con el Flujo del Canvas tienen ID que pueden utilizarse para agruparlos y traducirse a nombres legibles por humanos mediante el [punto final Exportar detalles del Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/).
{% endalert %}

{% alert note %}
Algunos campos pueden tardar más en mostrar su estado más reciente después de actualizar una campaña o Canvas. Estos campos son:
<ul>
  <li>"campaign_name"</li>
  <li>"canvas_name"</li>
  <li>"canvas_step_name"</li>
  <li>"conversion_behavior"</li>
  <li>"canvas_variation_name"</li>
  <li>"experiment_split_name"</li>
  <li>"message_variation_name"</li>
</ul>
Si se requiere una coherencia total, te recomendamos que esperes una hora desde la última actualización de estos campos antes de enviar la mensajería a tus usuarios.
{% endalert %}

{% api %}
## Desinstalar eventos {#uninstall-events}

{% apitags %}
Desinstala
{% endapitags %}

Este evento se produce cuando un usuario desinstala una aplicación. Utiliza estos datos para hacer un seguimiento de cuándo los usuarios desinstalan una aplicación. Aunque actualmente se trata de un evento de interacción de mensajes, en el futuro se cambiará a un evento de comportamiento del usuario.

{% alert important %}
Este evento no se dispara cuando el usuario desinstala realmente la aplicación, ya que es imposible hacer un seguimiento exacto. Braze envía un push silencioso diario para determinar si la aplicación sigue existiendo en el dispositivo de tu usuario, y si obtenemos un error en ese push silencioso, se asume que la aplicación se ha desinstalado.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Uninstall (users.behaviors.Uninstall)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Uninstall (users.behaviors.Uninstall)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Application Uninstalls (users.behaviors.Uninstall)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Application Uninstalled (users.behaviors.Uninstall)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.behaviors.Uninstall

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de cambio de estado de suscripción global {#global-subscription-state-change-events}

{% apitags %}
Suscripción
{% endapitags %}

Este evento se produce cuando Braze recibe una solicitud para actualizar el estado de suscripción global del usuario, aunque la solicitud no altere el estado de suscripción actual del usuario.

{% tabs %}
{% tab Amplitude %}
```json
// Global Subscription State Change (users.behaviors.subscription.GlobalStateChange)

{
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "channel" : "(optional, string) Channel this event belongs to",
    "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
    "email_address" : "(optional, string) [PII] Email address of the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
    "subscription_status" : "(required, string) Subscription status: 'Subscribed', 'Unsubscribed' or 'Opted In'",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Global Subscription State Change (users.behaviors.subscription.GlobalStateChange)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "channel" : "(optional, string) Channel this event belongs to",
    "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(optional, string) [PII] Email address of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
    "subscription_status" : "(required, string) Subscription status: 'Subscribed', 'Unsubscribed' or 'Opted In'",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Global Subscription State Changes (users.behaviors.subscription.GlobalStateChange)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "channel" : "(optional, string) Channel this event belongs to",
          "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
          "subscription_status" : "(required, string) Subscription status: 'Subscribed', 'Unsubscribed' or 'Opted In'"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(optional, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Global Subscription State Changed (users.behaviors.subscription.GlobalStateChange)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "email" : "(optional, string) [PII] Email address of the user"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "channel" : "(optional, string) Channel this event belongs to",
    "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
    "subscription_status" : "(required, string) Subscription status: 'Subscribed', 'Unsubscribed' or 'Opted In'"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.behaviors.subscription.GlobalStateChange

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "channel" : "(optional, string) Channel this event belongs to",
  "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
  "email_address" : "(optional, string) [PII] Email address of the user",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
  "subscription_status" : "(required, string) Subscription status: 'Subscribed', 'Unsubscribed' or 'Opted In'",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalles de la propiedad

- `state_change_source` devolverá una cadena con el nombre completo de la fuente. Por ejemplo, la importación del CSV de origen devolverá la cadena `CSV Import`. A continuación se enumeran las fuentes disponibles:

| Fuente | Descripción |
| --- | --- |
| SDK | Puntos finales SDK |
| Panel de control | Cuando se actualiza el estado de suscripción de un usuario desde la página **Perfil de usuario** del panel de control |
| Página de suscripción | Cuando un usuario se da de baja a través de un enlace de correo electrónico que no es el centro de preferencias |
| API REST | Puntos finales de la API REST |
| Importación CSV | Importación de usuarios en CSV |
| Centro de preferencias | Cuando se actualiza un usuario desde el centro de preferencias |
| Mensaje de entrada | Cuando un usuario se actualiza mediante mensajes entrantes de usuarios finales a través de canales, como SMS |
| Migración | Cuando un usuario se actualiza mediante migraciones internas o scripts de mantenimiento |
| Fusión de usuarios | Cuando se actualiza un usuario mediante el proceso de fusión de usuarios |
| Paso en Canvas para actualizar usuarios | Cuando un usuario se actualiza mediante el paso en Canvas Actualizar usuario |
| Registro de token de notificaciones push | Cuando un usuario se actualiza mediante el proceso de registro de token |
| Lista- Cancelar suscripción | Cuando un usuario se da de baja a través del mailto de Braze o de la cabecera de cancelar suscripción con un solo clic |
| Otros | Incluye cualquier otra fuente, como trabajos de sincronización de demostraciones o proveedores, o devoluciones de llamada de eventos de SMS y Whatsapp. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endapi %}

{% api %}
## Eventos de cambio de estado del grupo de suscripción {#subscription-group-state-change-events}

{% apitags %}
Suscripción
{% endapitags %}

Este evento se produce cuando cambia el estado de suscripción de un usuario en un grupo de suscripción.

{% alert important %}
Por el momento, los grupos de suscripción sólo están disponibles para los canales de correo electrónico, SMS y WhatsApp.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Subscription Group State Change (users.behaviors.subscriptiongroup.StateChange)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "channel" : "(optional, string) Channel this event belongs to",
    "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(optional, string) [PII] Email address of the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
    "subscription_group_id" : "(required, string) Subscription group API ID",
    "subscription_status" : "(required, string) Subscription status: 'Subscribed' or 'Unsubscribed'",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Subscription Group State Change (users.behaviors.subscriptiongroup.StateChange)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "channel" : "(optional, string) Channel this event belongs to",
    "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(optional, string) [PII] Email address of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
    "subscription_group_id" : "(required, string) Subscription group API ID",
    "subscription_status" : "(required, string) Subscription status: 'Subscribed' or 'Unsubscribed'",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Subscription Group State Changes (users.behaviors.subscriptiongroup.StateChange)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "channel" : "(optional, string) Channel this event belongs to",
          "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
          "subscription_group_id" : "(required, string) Subscription group API ID",
          "subscription_status" : "(required, string) Subscription status: 'Subscribed' or 'Unsubscribed'"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(optional, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Subscription Group State Changed (users.behaviors.subscriptiongroup.StateChange)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "email" : "(optional, string) [PII] Email address of the user"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "channel" : "(optional, string) Channel this event belongs to",
    "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
    "subscription_group_id" : "(required, string) Subscription group API ID",
    "subscription_status" : "(required, string) Subscription status: 'Subscribed' or 'Unsubscribed'"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.behaviors.subscriptiongroup.StateChange

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "channel" : "(optional, string) Channel this event belongs to",
  "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(optional, string) [PII] Email address of the user",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "phone_number" : "(optional, string) [PII] Phone number of the user in e.164 format (for example +14155552671)",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
  "subscription_group_id" : "(required, string) Subscription group API ID",
  "subscription_status" : "(required, string) Subscription status: 'Subscribed' or 'Unsubscribed'",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalles de la propiedad

- `state_change_source` devolverá una cadena con el nombre completo de la fuente. Por ejemplo, la importación del CSV de origen devolverá la cadena `CSV Import`. A continuación se enumeran las fuentes disponibles:

| Fuente | Descripción |
| --- | --- |
| SDK | Puntos finales SDK |
| Panel de control | Cuando se actualiza el estado de suscripción de un usuario desde la página Perfil de usuario del Panel de control |
| Página de suscripción | Cuando un usuario se da de baja a través de un enlace de correo electrónico que no es el centro de preferencias |
| API REST | Puntos finales de la API REST |
| Importación CSV | Importación de usuarios en CSV |
| Centro de preferencias | Cuando se actualiza un usuario desde el centro de preferencias |
| Mensaje de entrada | Cuando un usuario se actualiza mediante mensajes entrantes de usuarios finales a través de canales como SMS |
| Migración | Cuando un usuario se actualiza mediante migraciones internas o scripts de mantenimiento |
| Fusión de usuarios | Cuando un usuario es actualizado por el proceso de fusión de usuarios |
| Paso en Canvas para actualizar usuarios | Cuando un usuario es actualizado por el paso de actualización de usuarios de Canvas |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endapi %}

{% api %}
## Campaña Eventos de conversión {#campaign-conversion-events}

{% apitags %}
Campaña, conversión
{% endapitags %}

Este evento se produce cuando un usuario realiza una acción que se ha configurado como evento de conversión en una campaña.

{% alert note %}
`dispatch_id` está obsoleto y se eliminará en la próxima versión de Currents.
{% endalert %}

{% alert important %}
Ten en cuenta que el evento de conversión se codifica en el campo `conversion_behavior`, que incluye el tipo de evento de conversión, la ventana (marco temporal) e información adicional según el tipo de evento de conversión. El campo `conversion_behavior_index` representa qué evento de conversión, como 0 = A, 1 = B, 2 = C, 3 = D.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Campaign Conversion (users.campaigns.Conversion)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Campaign Conversion (users.campaigns.Conversion)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Campaign Conversions (users.campaigns.Conversion)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
          "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Campaign Converted (users.campaigns.Conversion)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.campaigns.Conversion

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "campaign_id" : "(required, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
  "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Campaña Grupo de control Actos de inscripción {#campaign-control-group-enrollment-events}

{% apitags %}
Campaña, Entrada
{% endapitags %}

Este evento se produce cuando un usuario se inscribe en una variante de control establecida en una campaña multivariante. Este evento se genera porque no habrá ningún evento de envío de canal para este usuario.

{% alert note %}
`dispatch_id` está obsoleto y se eliminará en la próxima versión de Currents.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Campaign Control Group Enrollment (users.campaigns.EnrollInControl)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Campaign Control Group Enrollment (users.campaigns.EnrollInControl)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Campaign Control Group Enrollments (users.campaigns.EnrollInControl)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Campaign Control Group Entered (users.campaigns.EnrollInControl)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.campaigns.EnrollInControl

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "campaign_id" : "(required, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de conversión en Canvas {#canvas-conversion-events}

{% apitags %}
Canvas, Conversión
{% endapitags %}

Este evento se produce cuando un usuario realiza una acción que se ha configurado como evento de conversión en Canvas.

{% alert important %}
Ten en cuenta que el evento de conversión se codifica en el campo `conversion_behavior`, que incluye el tipo de evento de conversión, la ventana (marco temporal) e información adicional según el tipo de evento de conversión. El campo `conversion_behavior_index` representa qué evento de conversión, como 0 = A, 1 = B, 2 = C, 3 = D.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Canvas Conversion (users.canvas.Conversion)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Canvas Conversion (users.canvas.Conversion)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Canvas Conversions (users.canvas.Conversion)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
          "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Canvas Converted (users.canvas.Conversion)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "device_id" : "(optional, string) ID of the device on which the event occurred"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.canvas.Conversion

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "canvas_id" : "(required, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(required, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
  "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de entrada en Canvas {#canvas-entry-events}

{% apitags %}
Canvas, Entrada
{% endapitags %}

Este evento se produce cuando un usuario entra en el Canvas. Este evento te indica en qué variante ha entrado el usuario.

{% tabs %}
{% tab Amplitude %}
```json
// Canvas Entry (users.canvas.Entry)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Canvas Entry (users.canvas.Entry)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Canvas Entries (users.canvas.Entry)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Canvas Entered (users.canvas.Entry)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.canvas.Entry

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "canvas_id" : "(required, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(required, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Partida de salida Actos de la audiencia {#exit-match-audience-events}

{% apitags %}
Salida, Canvas
{% endapitags %}

Este evento se produce cuando un usuario ha salido de un Canvas al coincidir con una audiencia.

{% tabs %}
{% tab Amplitude %}
```json
// Exit Match Audience (users.canvas.exit.MatchedAudience)

{
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Exit Match Audience (users.canvas.exit.MatchedAudience)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Exit Matched Audiences (users.canvas.exit.MatchedAudience)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Exit Matched Audience (users.canvas.exit.MatchedAudience)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.canvas.exit.MatchedAudience

{
  "app_group_api_id" : "(optional, string) [DEPRECATED]",
  "app_group_id" : "(required, string) API ID of the app group this user belongs to",
  "canvas_api_id" : "(optional, string) [DEPRECATED]",
  "canvas_id" : "(required, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_api_id" : "(optional, string) [DEPRECATED]",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_api_id" : "(optional, string) [DEPRECATED]",
  "canvas_variation_id" : "(required, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Salir Rendimiento Eventos del evento {#exit-perform-event-events}

{% apitags %}
Salida, Canvas
{% endapitags %}

Este evento se produce cuando un usuario ha salido de un Canvas realizando un evento.

{% tabs %}
{% tab Amplitude %}
```json
// Exit Perform Event (users.canvas.exit.PerformedEvent)

{
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Exit Perform Event (users.canvas.exit.PerformedEvent)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Exit Performed Events (users.canvas.exit.PerformedEvent)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Exit Performed Event (users.canvas.exit.PerformedEvent)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.canvas.exit.PerformedEvent

{
  "app_group_api_id" : "(optional, string) [DEPRECATED]",
  "app_group_id" : "(required, string) API ID of the app group this user belongs to",
  "canvas_api_id" : "(optional, string) [DEPRECATED]",
  "canvas_id" : "(required, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_api_id" : "(optional, string) [DEPRECATED]",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_api_id" : "(optional, string) [DEPRECATED]",
  "canvas_variation_id" : "(required, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Paso del experimento Eventos de conversión {#experiment-step-conversion-events}

{% apitags %}
Canvas
{% endapitags %}

Este evento se produce cuando un usuario convierte para un paso de experimento en Canvas.

{% tabs %}
{% tab Amplitude %}
```json
// Experiment Step Conversion (users.canvas.experimentstep.Conversion)

{
  "event_properties" : {
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
    "experiment_split_name" : "(optional, string) Name of the experiment split",
    "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Experiment Step Conversion (users.canvas.experimentstep.Conversion)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
    "experiment_split_name" : "(optional, string) Name of the experiment split",
    "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Experiment Step Conversions (users.canvas.experimentstep.Conversion)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
          "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
          "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
          "experiment_split_name" : "(optional, string) Name of the experiment split",
          "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Experiment Step Converted (users.canvas.experimentstep.Conversion)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
    "experiment_split_name" : "(optional, string) Name of the experiment split",
    "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.canvas.experimentstep.Conversion

{
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
  "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
  "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
  "experiment_split_name" : "(optional, string) Name of the experiment split",
  "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Experimento Eventos de entrada dividida {#experiment-split-entry-events}

{% apitags %}
Canvas
{% endapitags %}

Este evento se produce cuando un usuario entra en una ruta de experimentos en Canvas.

{% tabs %}
{% tab Amplitude %}
```json
// Experiment Split Entry (users.canvas.experimentstep.SplitEntry)

{
  "event_properties" : {
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
    "experiment_split_name" : "(optional, string) Name of the experiment split",
    "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
    "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Experiment Split Entry (users.canvas.experimentstep.SplitEntry)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
    "experiment_split_name" : "(optional, string) Name of the experiment split",
    "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
    "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Experiment Split Entries (users.canvas.experimentstep.SplitEntry)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
          "experiment_split_name" : "(optional, string) Name of the experiment split",
          "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
          "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Experiment Split Entered (users.canvas.experimentstep.SplitEntry)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
    "experiment_split_name" : "(optional, string) Name of the experiment split",
    "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
    "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.canvas.experimentstep.SplitEntry

{
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
  "experiment_split_name" : "(optional, string) Name of the experiment split",
  "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de progresión de pasos en Canvas {#canvas-step-progression-events}

{% apitags %}
Canvas, Progresión
{% endapitags %}

Este evento se produce cuando un usuario avanza por un paso en Canvas con algún resultado. Nota que este evento no se produce al entrar o salir de los pasos. Actualmente, sólo los pasos divididos (rutas de audiencia, división de decisiones, rutas de acción, experimento) y los resultados de avance generan eventos de progresión de pasos.

{% tabs %}
{% tab Amplitude %}
```json
// Canvas Step Progression (users.canvasstep.Progression)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_entry_id" : "(required, string) Unique identifier for this instance of a user in a canvas",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "exit_reason" : "(optional, string) If this is an exit, the reason a user exited the canvas during the step",
    "is_canvas_entry" : "(optional, boolean) Whether this is entry into a first step in a canvas",
    "next_step_id" : "(optional, string) API ID of the next step in the canvas",
    "progression_type" : "(required, string) What type of step progression event this is"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Canvas Step Progression (users.canvasstep.Progression)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_entry_id" : "(required, string) Unique identifier for this instance of a user in a canvas",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "exit_reason" : "(optional, string) If this is an exit, the reason a user exited the canvas during the step",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "is_canvas_entry" : "(optional, boolean) Whether this is entry into a first step in a canvas",
    "next_step_id" : "(optional, string) API ID of the next step in the canvas",
    "progression_type" : "(required, string) What type of step progression event this is",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Canvas Step Progressions (users.canvasstep.Progression)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "canvas_entry_id" : "(required, string) Unique identifier for this instance of a user in a canvas",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "exit_reason" : "(optional, string) If this is an exit, the reason a user exited the canvas during the step",
          "is_canvas_entry" : "(optional, boolean) Whether this is entry into a first step in a canvas",
          "next_step_id" : "(optional, string) API ID of the next step in the canvas",
          "progression_type" : "(required, string) What type of step progression event this is",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Canvas Step Progression (users.canvasstep.Progression)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_entry_id" : "(required, string) Unique identifier for this instance of a user in a canvas",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "exit_reason" : "(optional, string) If this is an exit, the reason a user exited the canvas during the step",
    "is_canvas_entry" : "(optional, boolean) Whether this is entry into a first step in a canvas",
    "next_step_id" : "(optional, string) API ID of the next step in the canvas",
    "progression_type" : "(required, string) What type of step progression event this is"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.canvasstep.Progression

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "canvas_entry_id" : "(required, string) Unique identifier for this instance of a user in a canvas",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "exit_reason" : "(optional, string) If this is an exit, the reason a user exited the canvas during the step",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "is_canvas_entry" : "(optional, boolean) Whether this is entry into a first step in a canvas",
  "next_step_id" : "(optional, string) API ID of the next step in the canvas",
  "progression_type" : "(required, string) What type of step progression event this is",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Banner Abortar eventos {#banner-abort-events}

{% apitags %}
Banner, Abortar
{% endapitags %}

Este evento se produce cuando un mensaje de banner programado originalmente fue abortado por alguna razón.

{% tabs %}
{% tab Amplitude %}
```json
// Banner Abort (users.messages.banner.Abort)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "device_model" : "(optional, string) Model of the device",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Banner Abort (users.messages.banner.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Banner Aborts (users.messages.banner.Abort)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
          "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Banner Aborted (users.messages.banner.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.banner.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
  "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "carrier" : "(optional, string) Carrier of the device",
  "country" : "(optional, string) [PII] Country of the user",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "gender" : "(optional, string) [PII] Gender of the user, one of ['M', 'F', 'O', 'N', 'P']",
  "id" : "(required, string) Globally unique ID for this event",
  "language" : "(optional, string) [PII] Language of the user",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "resolution" : "(optional, string) Resolution of the device",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Banner Eventos de clic {#banner-click-events}

{% apitags %}
Banner, Clics
{% endapitags %}

Este evento se produce cuando un usuario hace clic en un banner.

{% tabs %}
{% tab Amplitude %}
```json
// Banner Click (users.messages.banner.Click)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "device_model" : "(optional, string) Model of the device",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Banner Click (users.messages.banner.Click)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Banner Clicks (users.messages.banner.Click)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
          "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
          "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Banner Clicked (users.messages.banner.Click)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.banner.Click

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
  "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
  "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "carrier" : "(optional, string) Carrier of the device",
  "country" : "(optional, string) [PII] Country of the user",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "gender" : "(optional, string) [PII] Gender of the user, one of ['M', 'F', 'O', 'N', 'P']",
  "id" : "(required, string) Globally unique ID for this event",
  "language" : "(optional, string) [PII] Language of the user",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "resolution" : "(optional, string) Resolution of the device",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de impresión de banners {#banner-impression-events}

{% apitags %}
Banner, Impresiones
{% endapitags %}

Este evento se produce cuando un usuario ve un banner.

{% tabs %}
{% tab Amplitude %}
```json
// Banner Impression (users.messages.banner.Impression)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "device_model" : "(optional, string) Model of the device",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Banner Impression (users.messages.banner.Impression)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Banner Impressions (users.messages.banner.Impression)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
          "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Banner Viewed (users.messages.banner.Impression)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.banner.Impression

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
  "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "carrier" : "(optional, string) Carrier of the device",
  "country" : "(optional, string) [PII] Country of the user",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "gender" : "(optional, string) [PII] Gender of the user, one of ['M', 'F', 'O', 'N', 'P']",
  "id" : "(required, string) Globally unique ID for this event",
  "language" : "(optional, string) [PII] Language of the user",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "resolution" : "(optional, string) Resolution of the device",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de abortar tarjeta de contenido {#content-card-abort-events}

{% apitags %}
Abortar, Tarjetas de contenido
{% endapitags %}

Este evento se produce si se ha abortado un mensaje de la tarjeta de contenido en función de los abortos de Liquid, etc.

{% tabs %}
{% tab Amplitude %}
```json
// Content Card Abort (users.messages.contentcard.Abort)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Content Card Abort (users.messages.contentcard.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Content Card Aborts (users.messages.contentcard.Abort)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Content Card Aborted (users.messages.contentcard.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.contentcard.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de clic en la tarjeta de contenido {#content-card-click-events}

{% apitags %}
Tarjetas de contenido, Clics
{% endapitags %}

Este evento se produce cuando un usuario hace clic en una tarjeta de contenido.

{% alert note %}
`dispatch_id` está obsoleto y se eliminará en la próxima versión de Currents.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Content Card Click (users.messages.contentcard.Click)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "device_model" : "(optional, string) Model of the device",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Content Card Click (users.messages.contentcard.Click)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Content Card Clicks (users.messages.contentcard.Click)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "card_id" : "(required, string) ID of the card that generated this event",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Content Card Clicked (users.messages.contentcard.Click)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.contentcard.Click

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "content_card_id" : "(required, string) ID of the card that generated this event",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalles de la propiedad

- Para `ad_id`, `ad_id_type`, y `ad_tracking_enabled`, necesitas recopilar explícitamente el IDFA de publicidad de iOS y el ID de publicidad de Google de Android a través de los SDK nativos. Más información sobre esta configuración para [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift) y [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).
- Si utilizas Kafka para la ingesta de datos [de Currents]({{site.baseurl}}/user_guide/data/braze_currents/), ponte en contacto con tu administrador del éxito del cliente para habilitar el envío de `ad_id`.
{% endapi %}

{% api %}
## Tarjeta de contenido Descartar eventos {#content-card-dismiss-events}

{% apitags %}
Tarjetas de contenido, despido
{% endapitags %}

Este evento se produce cuando un usuario descarta una tarjeta de contenido.

{% alert note %}
`dispatch_id` está obsoleto y se eliminará en la próxima versión de Currents.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Content Card Dismiss (users.messages.contentcard.Dismiss)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "device_model" : "(optional, string) Model of the device",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Content Card Dismiss (users.messages.contentcard.Dismiss)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Content Card Dismisses (users.messages.contentcard.Dismiss)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "card_id" : "(required, string) ID of the card that generated this event",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Content Card Dismissed (users.messages.contentcard.Dismiss)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.contentcard.Dismiss

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "content_card_id" : "(required, string) ID of the card that generated this event",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalles de la propiedad

- Para `ad_id`, `ad_id_type`, y `ad_tracking_enabled`, necesitas recopilar explícitamente el IDFA de publicidad de iOS y el ID de publicidad de Google de Android a través de los SDK nativos. Más información sobre esta configuración para [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift) y [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).
- Si utilizas Kafka para la ingesta de datos [de Currents]({{site.baseurl}}/user_guide/data/braze_currents/), ponte en contacto con tu administrador del éxito del cliente para habilitar el envío de `ad_id`.
{% endapi %}

{% api %}
## Eventos de impresión de tarjetas de contenido {#content-card-impression-events}

{% apitags %}
Tarjetas de contenido, impresiones
{% endapitags %}

Este evento se produce cuando un usuario ve una tarjeta de contenido.

{% alert note %}
`dispatch_id` está obsoleto y se eliminará en la próxima versión de Currents.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Content Card Impression (users.messages.contentcard.Impression)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "device_model" : "(optional, string) Model of the device",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Content Card Impression (users.messages.contentcard.Impression)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Content Card Impressions (users.messages.contentcard.Impression)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "card_id" : "(required, string) ID of the card that generated this event",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Content Card Viewed (users.messages.contentcard.Impression)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.contentcard.Impression

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "content_card_id" : "(required, string) ID of the card that generated this event",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalles de la propiedad

- Para `ad_id`, `ad_id_type`, y `ad_tracking_enabled`, necesitas recopilar explícitamente el IDFA de publicidad de iOS y el ID de publicidad de Google de Android a través de los SDK nativos. Más información sobre esta configuración para [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift) y [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).
- Si utilizas Kafka para la ingesta de datos [de Currents]({{site.baseurl}}/user_guide/data/braze_currents/), ponte en contacto con tu administrador del éxito del cliente para habilitar el envío de `ad_id`.
{% endapi %}

{% api %}
## Tarjeta de contenido Enviar eventos {#content-card-send-events}

{% apitags %}
Tarjetas de contenido, Envía
{% endapitags %}

Este evento se produce cuando se envía una tarjeta de contenido a un usuario.

{% alert note %}
`dispatch_id` está obsoleto y se eliminará en la próxima versión de Currents.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Content Card Send (users.messages.contentcard.Send)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Content Card Send (users.messages.contentcard.Send)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Content Card Sends (users.messages.contentcard.Send)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "card_id" : "(required, string) ID of the card that generated this event",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Content Card Sent (users.messages.contentcard.Send)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.contentcard.Send

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "content_card_id" : "(required, string) ID of the card that generated this event",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalles de la propiedad

- `message_extras` te permiten anotar tus eventos de envío con datos dinámicos del Contenido conectado, atributos personalizados (como el idioma o el país) y propiedades de entrada del Canvas. Consulta [Extras de mensajes]({{site.baseurl}}/message_extras_tag/) para obtener más información.
{% endapi %}

{% api %}
## Correo electrónico Abortar eventos {#email-abort-events}

{% apitags %}
Cancelar, correo electrónico
{% endapitags %}

Este evento se produce si se ha abortado un mensaje de correo electrónico debido a que Liquid lo ha abortado, etc.

{% tabs %}
{% tab Amplitude %}
```json
// Email Abort (users.messages.email.Abort)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Abort (users.messages.email.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Aborts (users.messages.email.Abort)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Aborted (users.messages.email.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.email.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de rebotes de correo electrónico {#email-bounce-events}

{% apitags %}
Correo electrónico, rebotar
{% endapitags %}

Este evento se produce cuando un proveedor de servicios de Internet devuelve un rebote duro. Un rebote duro significa un fallo permanente en la capacidad de entrega.

{% tabs %}
{% tab Amplitude %}
```json
// Email Bounce (users.messages.email.Bounce)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_drop" : "(optional, boolean) Indicates that this event counts as a drop event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Bounce (users.messages.email.Bounce)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_drop" : "(optional, boolean) Indicates that this event counts as a drop event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Bounces (users.messages.email.Bounce)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "is_drop" : "(optional, boolean) Indicates that this event counts as a drop event",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Bounced (users.messages.email.Bounce)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_drop" : "(optional, boolean) Indicates that this event counts as a drop event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.email.Bounce

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "is_drop" : "(optional, boolean) Indicates that this event counts as a drop event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "sending_ip" : "(optional, string) IP address from which the email send was made",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalles de la propiedad

- El comportamiento para `dispatch_id` difiere entre Canvas y las campañas porque Braze trata los pasos en Canvas (excepto los pasos de entrada, que pueden programarse) como eventos desencadenados, incluso cuando están programados. Más información sobre [el comportamiento del ID de envío]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}
## Correo electrónico Eventos de clic {#email-click-events}

{% apitags %}
Correo electrónico, Clics
{% endapitags %}

Este evento se produce cuando un usuario hace clic en un correo electrónico. Se pueden generar varios eventos para la misma campaña si un usuario hace clic varias veces o hace clic en diferentes enlaces dentro del correo electrónico.

{% tabs %}
{% tab Amplitude %}
```json
// Email Click (users.messages.email.Click)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
    "device_model" : "(optional, string) Model of the device",
    "device_os" : "(optional, string) Device operating system extracted from user_agent",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
    "is_suspected_bot_click" : "(optional, boolean) Indicates that this is a suspected bot click. Will only populate when Bot Filtering setting is enabled",
    "link_alias" : "(optional, string) Alias associated with this link ID",
    "link_id" : "(optional, string) Unique ID for the link which was clicked, as created by Braze",
    "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "suspected_bot_click_reason" : "(optional, array of string) Reason(s) why this is a suspected bot click. Will always populate even if Bot Filtering setting is disabled.",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Click (users.messages.email.Click)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "$device" : "(optional, string) Model of the device",
    "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "device_os" : "(optional, string) Device operating system extracted from user_agent",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
    "is_suspected_bot_click" : "(optional, boolean) Indicates that this is a suspected bot click. Will only populate when Bot Filtering setting is enabled",
    "link_alias" : "(optional, string) Alias associated with this link ID",
    "link_id" : "(optional, string) Unique ID for the link which was clicked, as created by Braze",
    "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "suspected_bot_click_reason" : "(optional, array of string) Reason(s) why this is a suspected bot click. Will always populate even if Bot Filtering setting is disabled.",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Clicks (users.messages.email.Click)

{
  "device_info" : {
    "device_model" : "(optional, string) Model of the device",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "device_os" : "(optional, string) Device operating system extracted from user_agent",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
          "is_suspected_bot_click" : "(optional, boolean) Indicates that this is a suspected bot click. Will only populate when Bot Filtering setting is enabled",
          "link_alias" : "(optional, string) Alias associated with this link ID",
          "link_id" : "(optional, string) Unique ID for the link which was clicked, as created by Braze",
          "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "url" : "(optional, string) URL that the user clicked on",
          "user_agent" : "(optional, string) User agent on which the spam report occurred"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Link Clicked (users.messages.email.Click)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device"
    },
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "device_os" : "(optional, string) Device operating system extracted from user_agent",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
    "is_suspected_bot_click" : "(optional, boolean) Indicates that this is a suspected bot click. Will only populate when Bot Filtering setting is enabled",
    "link_alias" : "(optional, string) Alias associated with this link ID",
    "link_id" : "(optional, string) Unique ID for the link which was clicked, as created by Braze",
    "link_url" : "(optional, string) URL that the user clicked on",
    "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "suspected_bot_click_reason" : "(optional, array of string) Reason(s) why this is a suspected bot click. Will always populate even if Bot Filtering setting is disabled.",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.email.Click

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
  "device_model" : "(optional, string) Model of the device",
  "device_os" : "(optional, string) Device operating system extracted from user_agent",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
  "is_suspected_bot_click" : "(optional, boolean) Indicates that this is a suspected bot click. Will only populate when Bot Filtering setting is enabled",
  "link_alias" : "(optional, string) Alias associated with this link ID",
  "link_id" : "(optional, string) Unique ID for the link which was clicked, as created by Braze",
  "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "suspected_bot_click_reason" : "(optional, array of string) Reason(s) why this is a suspected bot click. Will always populate even if Bot Filtering setting is disabled.",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "url" : "(optional, string) URL that the user clicked on",
  "user_agent" : "(optional, string) User agent on which the spam report occurred",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalles de la propiedad

- El comportamiento para `dispatch_id` difiere entre Canvas y las campañas porque Braze trata los pasos en Canvas (excepto los pasos de entrada, que pueden programarse) como eventos desencadenados, incluso cuando están programados. Más información sobre [el comportamiento del ID de envío]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}
## Eventos de aplazamiento por correo electrónico {#email-deferral-events}

{% apitags %}
Correo electrónico, Aplazamiento
{% endapitags %}

Este evento se produce cuando un proveedor de servicios de Internet no entrega inmediatamente el envío por correo electrónico a una dirección de correo electrónico que no ha rebotado duro y Braze reintenta el envío durante un máximo de 72 horas. Las razones típicas de los aplazamientos incluyen la limitación de la tasa de volumen de correo electrónico basada en la reputación por parte del proveedor de buzón de entrada, problemas temporales de conectividad, el buzón del destinatario está lleno o errores de DNS.

{% tabs %}
{% tab Amplitude %}
```json
// Email Deferral (users.messages.email.Deferral)

{
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "attempt_count" : "(optional, int) Number of attempts made to send the message",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "deferral_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this deferral event",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "recipient_domain" : "(optional, string) Receipient's email domain",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Deferral (users.messages.email.Deferral)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "attempt_count" : "(optional, int) Number of attempts made to send the message",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "deferral_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this deferral event",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "recipient_domain" : "(optional, string) Receipient's email domain",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Deferrals (users.messages.email.Deferral)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "attempt_count" : "(optional, int) Number of attempts made to send the message",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "deferral_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this deferral event",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "recipient_domain" : "(optional, string) Receipient's email domain",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Deferred (users.messages.email.Deferral)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "attempt_count" : "(optional, int) Number of attempts made to send the message",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "deferral_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this deferral event",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "recipient_domain" : "(optional, string) Receipient's email domain",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.email.Deferral

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "attempt_count" : "(optional, int) Number of attempts made to send the message",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "deferral_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this deferral event",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "recipient_domain" : "(optional, string) Receipient's email domain",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "sending_ip" : "(optional, string) IP address from which the email send was made",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalles de la propiedad

- El comportamiento para `dispatch_id` difiere entre Canvas y las campañas porque Braze trata los pasos en Canvas (excepto los pasos de entrada, que pueden programarse) como eventos desencadenados, incluso cuando están programados. Más información sobre [el comportamiento del ID de envío]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}
## Eventos de entrega de correo electrónico {#email-delivery-events}

{% apitags %}
Correo electrónico, entrega
{% endapitags %}

Este evento se produce cuando un correo electrónico enviado llega correctamente al buzón de entrada del usuario final.

{% tabs %}
{% tab Amplitude %}
```json
// Email Delivery (users.messages.email.Delivery)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Delivery (users.messages.email.Delivery)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Deliveries (users.messages.email.Delivery)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Delivered (users.messages.email.Delivery)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.email.Delivery

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "sending_ip" : "(optional, string) IP address from which the email send was made",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalles de la propiedad

- El comportamiento para `dispatch_id` difiere entre Canvas y las campañas porque Braze trata los pasos en Canvas (excepto los pasos de entrada, que pueden programarse) como eventos desencadenados, incluso cuando están programados. Más información sobre [el comportamiento del ID de envío]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}
## Eventos de Marcar como Spam por correo electrónico {#email-mark-as-spam-events}

{% apitags %}
Correo electrónico, Spam
{% endapitags %}

Este evento se produce cuando el usuario final pulsa el botón "spam" del correo electrónico. Ten en cuenta que esto no representa el hecho de que el correo electrónico haya ido a parar a la carpeta de correo no deseado, ya que Braze no hace un seguimiento de ello.

{% tabs %}
{% tab Amplitude %}
```json
// Email Mark As Spam (users.messages.email.MarkAsSpam)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Mark As Spam (users.messages.email.MarkAsSpam)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Marks As Spam (users.messages.email.MarkAsSpam)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "user_agent" : "(optional, string) User agent on which the spam report occurred"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Marked as Spam (users.messages.email.MarkAsSpam)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.email.MarkAsSpam

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_agent" : "(optional, string) User agent on which the spam report occurred",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalles de la propiedad

- El comportamiento para `dispatch_id` difiere entre Canvas y las campañas porque Braze trata los pasos en Canvas (excepto los pasos de entrada, que pueden programarse) como eventos desencadenados, incluso cuando están programados. Más información sobre [el comportamiento del ID de envío]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}
## Correo electrónico Eventos abiertos {#email-open-events}

{% apitags %}
Correo electrónico, aperturas
{% endapitags %}

Este evento se produce cuando un usuario abre un correo electrónico. Se pueden generar varios eventos para la misma campaña si un usuario abre el correo electrónico varias veces.

{% alert important %}
Es un comportamiento conocido que los campos de evento de apertura de correo electrónico `device_model` y `mailbox_provider` están vacíos. Puedes ignorarlos por ahora.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Email Open (users.messages.email.Open)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
    "device_model" : "(optional, string) Model of the device",
    "device_os" : "(optional, string) Device operating system extracted from user_agent",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
    "machine_open" : "(optional, string) Populated to 'true' if the open event is triggered without user engagement, for example by an Apple device with Mail Privacy Protection enabled. Value may change over time to provide more granularity.",
    "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Open (users.messages.email.Open)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "$device" : "(optional, string) Model of the device",
    "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "device_os" : "(optional, string) Device operating system extracted from user_agent",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
    "machine_open" : "(optional, string) Populated to 'true' if the open event is triggered without user engagement, for example by an Apple device with Mail Privacy Protection enabled. Value may change over time to provide more granularity.",
    "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Opens (users.messages.email.Open)

{
  "device_info" : {
    "device_model" : "(optional, string) Model of the device",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "device_os" : "(optional, string) Device operating system extracted from user_agent",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
          "machine_open" : "(optional, string) Populated to 'true' if the open event is triggered without user engagement, for example by an Apple device with Mail Privacy Protection enabled. Value may change over time to provide more granularity.",
          "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "user_agent" : "(optional, string) User agent on which the spam report occurred"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Opened (users.messages.email.Open)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device"
    },
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "device_os" : "(optional, string) Device operating system extracted from user_agent",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
    "machine_open" : "(optional, string) Populated to 'true' if the open event is triggered without user engagement, for example by an Apple device with Mail Privacy Protection enabled. Value may change over time to provide more granularity.",
    "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.email.Open

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
  "device_model" : "(optional, string) Model of the device",
  "device_os" : "(optional, string) Device operating system extracted from user_agent",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
  "machine_open" : "(optional, string) Populated to 'true' if the open event is triggered without user engagement, for example by an Apple device with Mail Privacy Protection enabled. Value may change over time to provide more granularity.",
  "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_agent" : "(optional, string) User agent on which the spam report occurred",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalles de la propiedad

- El comportamiento para `dispatch_id` difiere entre Canvas y las campañas porque Braze trata los pasos en Canvas (excepto los pasos de entrada, que pueden programarse) como eventos desencadenados, incluso cuando están programados. Más información sobre [el comportamiento del ID de envío]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}
## Enviar eventos por correo electrónico {#email-send-events}

{% apitags %}
Correo electrónico, Envíos
{% endapitags %}

Este evento se produce cuando una solicitud de envío de correo electrónico se ha comunicado correctamente entre Braze y SendGrid. Sin embargo, esto no significa que el correo electrónico se haya recibido en el buzón de entrada del usuario.

{% tabs %}
{% tab Amplitude %}
```json
// Email Send (users.messages.email.Send)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Send (users.messages.email.Send)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Sends (users.messages.email.Send)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Sent (users.messages.email.Send)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.email.Send

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalles de la propiedad

- El comportamiento para `dispatch_id` difiere entre Canvas y las campañas porque Braze trata los pasos en Canvas (excepto los pasos de entrada, que pueden programarse) como eventos desencadenados, incluso cuando están programados. Más información sobre [el comportamiento del ID de envío]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
- `message_extras` te permiten anotar tus eventos de envío con datos dinámicos de Contenido conectado, atributos personalizados (como idioma, país) y propiedades de entrada en Canvas. Consulta [Extras de mensajes]({{site.baseurl}}/message_extras_tag/) para obtener más información.
{% endapi %}

{% api %}
## Eventos de correo electrónico de rebote blando {#email-soft-bounce-events}

{% apitags %}
Correo electrónico, rebotar
{% endapitags %}

Este evento se produce cuando un proveedor de servicios de Internet devuelve un rebote blando. Un rebote blando significa que no se ha podido entregar un correo electrónico debido a un fallo temporal de capacidad de entrega.

{% tabs %}
{% tab Amplitude %}
```json
// Email Soft Bounce (users.messages.email.SoftBounce)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Soft Bounce (users.messages.email.SoftBounce)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Soft Bounces (users.messages.email.SoftBounce)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Soft Bounced (users.messages.email.SoftBounce)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.email.SoftBounce

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "sending_ip" : "(optional, string) IP address from which the email send was made",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalles de la propiedad

- El comportamiento para `dispatch_id` difiere entre Canvas y las campañas porque Braze trata los pasos en Canvas (excepto los pasos de entrada, que pueden programarse) como eventos desencadenados, incluso cuando están programados. Más información sobre [el comportamiento del ID de envío]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}
## Cancelar suscripción a eventos por correo electrónico {#email-unsubscribe-events}

{% apitags %}
Correo electrónico, suscripción
{% endapitags %}

Este evento se produce cuando el usuario final ha hecho clic en "cancelar suscripción" del correo electrónico.

{% alert important %}
El evento `Unsubscribe` es en realidad un evento de clic especializado que se dispara cuando tu usuario hace clic en el enlace de cancelar suscripción del correo electrónico (ya sea un enlace normal de cancelar suscripción dentro del cuerpo del correo electrónico o del pie de página, o utilizando la [cabecera lista-desuscripción]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/email_settings#include-a-list-unsubscribe-header)), no cuando el usuario cambia el estado a desuscrito. Si el cambio de estado de suscripción se envía a través de la API, o a través de un enlace de cancelación de suscripción personalizado (no de Braze), no desencadenará un evento en Currents.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Email Unsubscribe (users.messages.email.Unsubscribe)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Unsubscribe (users.messages.email.Unsubscribe)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Unsubscribes (users.messages.email.Unsubscribe)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Unsubscribed (users.messages.email.Unsubscribe)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.email.Unsubscribe

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalles de la propiedad

- El comportamiento para `dispatch_id` difiere entre Canvas y las campañas porque Braze trata los pasos en Canvas (excepto los pasos de entrada, que pueden programarse) como eventos desencadenados, incluso cuando están programados. Más información sobre [el comportamiento del ID de envío]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}
## Característica Bandera Experimento Eventos de impresión {#feature-flag-experiment-impression-events}

{% apitags %}
Banderas de características, impresiones
{% endapitags %}

Este evento se produce siempre que un usuario ha tenido la oportunidad de interactuar con tu característica, o cuando podría haber interactuado si la característica está desactivada (en el caso de un grupo de control en una prueba A/B).

Las impresiones de la bandera de características sólo se registran una vez por sesión.


{% tabs %}
{% tab Amplitude %}
```json
// Feature Flag Experiment Impression (users.messages.featureflag.Impression)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_model" : "(optional, string) Model of the device",
    "feature_flag_id_name" : "(optional, string) The Feature Flag Rollout identifier",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Feature Flag Experiment Impression (users.messages.featureflag.Impression)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "feature_flag_id_name" : "(optional, string) The Feature Flag Rollout identifier",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Feature Flag Experiment Impressions (users.messages.featureflag.Impression)

{
  "device_info" : {
    "device_model" : "(optional, string) Model of the device",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "platform" : "(optional, string) Platform of the device"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "feature_flag_id_name" : "(optional, string) The Feature Flag Rollout identifier",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Feature Flag Experiment Impressed (users.messages.featureflag.Impression)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "feature_flag_id_name" : "(optional, string) The Feature Flag Rollout identifier",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.featureflag.Impression

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "carrier" : "(optional, string) Carrier of the device",
  "country" : "(optional, string) [PII] Country of the user",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "feature_flag_id_name" : "(optional, string) The Feature Flag Rollout identifier",
  "gender" : "(optional, string) [PII] Gender of the user, one of ['M', 'F', 'O', 'N', 'P']",
  "id" : "(required, string) Globally unique ID for this event",
  "language" : "(optional, string) [PII] Language of the user",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "resolution" : "(optional, string) Resolution of the device",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de cancelación de mensajes dentro de la aplicación {#in-app-message-abort-events}

{% apitags %}
Mensajes dentro de la aplicación, Cancelar
{% endapitags %}

Este evento se produce cuando se cancela un mensaje dentro de la aplicación programado originalmente.

{% tabs %}
{% tab Amplitude %}
```json
// In-App Message Abort (users.messages.inappmessage.Abort)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_model" : "(optional, string) Model of the device",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// In-App Message Abort (users.messages.inappmessage.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(optional, string) API ID of the card",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// In-App Message Aborts (users.messages.inappmessage.Abort)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// In-App Message Aborted (users.messages.inappmessage.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(optional, string) API ID of the card",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.inappmessage.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "card_id" : "(optional, string) API ID of the card",
  "carrier" : "(optional, string) Carrier of the device",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "resolution" : "(optional, string) Resolution of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event",
  "version" : "(required, string) Which version of in-app message, legacy or triggered"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de clic en mensajes dentro de la aplicación {#in-app-message-click-events}

{% apitags %}
Mensajes dentro de la aplicación, clics
{% endapitags %}

Este evento se produce cuando un usuario hace clic en un mensaje dentro de la aplicación.

{% alert note %}
`dispatch_id` está obsoleto y se eliminará en la próxima versión de Currents.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// In-App Message Click (users.messages.inappmessage.Click)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(optional, string) API ID of the card",
    "device_model" : "(optional, string) Model of the device",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// In-App Message Click (users.messages.inappmessage.Click)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(optional, string) API ID of the card",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// In-App Message Clicks (users.messages.inappmessage.Click)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "card_id" : "(optional, string) API ID of the card",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// In-App Message Clicked (users.messages.inappmessage.Click)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(optional, string) API ID of the card",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.inappmessage.Click

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "card_id" : "(optional, string) API ID of the card",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalles de la propiedad

- Para `ad_id`, `ad_id_type`, y `ad_tracking_enabled`, necesitas recopilar explícitamente el IDFA de publicidad de iOS y el ID de publicidad de Google de Android a través de los SDK nativos. Más información sobre esta configuración para [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift) y [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).
- Si utilizas Kafka para la ingesta de datos [de Currents]({{site.baseurl}}/user_guide/data/braze_currents/), ponte en contacto con tu administrador del éxito del cliente para habilitar el envío de `ad_id`.
{% endapi %}

{% api %}
## Eventos de impresión de mensajes dentro de la aplicación {#in-app-message-impression-events}

{% apitags %}
Mensajes dentro de la aplicación, impresiones
{% endapitags %}

Este evento se produce cuando un usuario ve un mensaje dentro de la aplicación.

{% alert note %}
`dispatch_id` está obsoleto y se eliminará en la próxima versión de Currents.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// In-App Message Impression (users.messages.inappmessage.Impression)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(optional, string) API ID of the card",
    "device_model" : "(optional, string) Model of the device",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// In-App Message Impression (users.messages.inappmessage.Impression)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(optional, string) API ID of the card",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// In-App Message Impressions (users.messages.inappmessage.Impression)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "card_id" : "(optional, string) API ID of the card",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
          "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// In-App Message Viewed (users.messages.inappmessage.Impression)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(optional, string) API ID of the card",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.inappmessage.Impression

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "card_id" : "(optional, string) API ID of the card",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
  "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalles de la propiedad

- Para `ad_id`, `ad_id_type`, y `ad_tracking_enabled`, necesitas recopilar explícitamente el IDFA de publicidad de iOS y el ID de publicidad de Google de Android a través de los SDK nativos. Más información sobre esta configuración para [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift) y [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).
- Si utilizas Kafka para la ingesta de datos [de Currents]({{site.baseurl}}/user_guide/data/braze_currents/), ponte en contacto con tu administrador del éxito del cliente para habilitar el envío de `ad_id`.
{% endapi %}

{% api %}
## Abortar eventos {#abort-events}

{% apitags %}
LÍNEA, Abortar
{% endapitags %}

Este evento se produce cuando no se puede entregar un mensaje programado de LINE, antes de enviarlo a LINE.

{% tabs %}
{% tab Amplitude %}
```json
// Abort (users.messages.line.Abort)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
    "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Abort (users.messages.line.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
    "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Aborts (users.messages.line.Abort)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
          "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Aborted (users.messages.line.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
    "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.line.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
  "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de clic {#click-events}

{% apitags %}
LÍNEA, Clics
{% endapitags %}

Este evento se produce cuando un usuario hace clic en un enlace de un mensaje de LINE en el que el dominio del enlace coincide con el dominio de seguimiento de clics.

{% tabs %}
{% tab Amplitude %}
```json
// Click (users.messages.line.Click)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
    "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
    "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "short_url" : "(required, string) Shortened url that was clicked",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "timezone" : "(optional, string) Time zone of the user",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Click (users.messages.line.Click)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
    "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
    "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "short_url" : "(required, string) Shortened url that was clicked",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Clicks (users.messages.line.Click)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
          "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
          "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "short_url" : "(required, string) Shortened url that was clicked",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID",
          "url" : "(optional, string) URL that the user clicked on",
          "user_agent" : "(optional, string) User agent on which the spam report occurred"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Clicked (users.messages.line.Click)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
    "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
    "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "short_url" : "(required, string) Shortened url that was clicked",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.line.Click

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
  "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
  "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "short_url" : "(required, string) Shortened url that was clicked",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "url" : "(required, string) URL that the user clicked on",
  "user_agent" : "(optional, string) User agent on which the spam report occurred",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## LÍNEA Recibir eventos {#line-inbound-receive-events}

{% apitags %}
LÍNEA, Entrada Recibida
{% endapitags %}

Este evento se produce cuando se recibe un mensaje LINE de un usuario.

{% tabs %}
{% tab Amplitude %}
```json
// LINE Inbound Receive (users.messages.line.InboundReceive)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
    "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
    "media_id" : "(optional, string) The LINE-generated ID which can be used to retrieve inbound media from LINE",
    "message_body" : "(optional, string) Typed response from the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// LINE Inbound Receive (users.messages.line.InboundReceive)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
    "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
    "media_id" : "(optional, string) The LINE-generated ID which can be used to retrieve inbound media from LINE",
    "message_body" : "(optional, string) Typed response from the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// LINE Inbound Receives (users.messages.line.InboundReceive)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
          "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
          "media_id" : "(optional, string) The LINE-generated ID which can be used to retrieve inbound media from LINE",
          "message_body" : "(optional, string) Typed response from the user",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// LINE Inbound Received (users.messages.line.InboundReceive)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
    "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
    "media_id" : "(optional, string) The LINE-generated ID which can be used to retrieve inbound media from LINE",
    "message_body" : "(optional, string) Typed response from the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.line.InboundReceive

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
  "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
  "media_id" : "(optional, string) The LINE-generated ID which can be used to retrieve inbound media from LINE",
  "message_body" : "(optional, string) Typed response from the user",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Enviar eventos {#send-events}

{% apitags %}
LÍNEA, Envía
{% endapitags %}

Este evento se produce cuando se envía un mensaje LINE a LINE.

{% tabs %}
{% tab Amplitude %}
```json
// Send (users.messages.line.Send)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
    "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Send (users.messages.line.Send)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
    "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Sends (users.messages.line.Send)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
          "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
          "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Sent (users.messages.line.Send)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
    "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.line.Send

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
  "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
  "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Actividad en vivo Eventos de resultados {#live-activity-outcome-events}

{% apitags %}
Actividad en vivo, Resultado
{% endapitags %}

Este evento se produce cuando Braze recibe una respuesta de un proveedor externo (e.g. APN) tras el envío de la Actividad en vivo

{% tabs %}
{% tab Amplitude %}
```json
// Live Activity Outcome (users.messages.liveactivity.Outcome)

{
  "event_properties" : {
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "live_activity_event_outcome" : "(optional, string) Outcome of Live Activity event",
    "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "update_token" : "(optional, string) Live Activity update token"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Live Activity Outcome (users.messages.liveactivity.Outcome)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "live_activity_event_outcome" : "(optional, string) Outcome of Live Activity event",
    "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "update_token" : "(optional, string) Live Activity update token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Live Activity Outcomes (users.messages.liveactivity.Outcome)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "activity_attributes_type" : "(optional, string) Live Activity attribute type",
          "activity_id" : "(optional, string) Live Activity identifier",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "live_activity_event_outcome" : "(optional, string) Outcome of Live Activity event",
          "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
          "push_to_start_token" : "(optional, string) Live Activity push to start token",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "update_token" : "(optional, string) Live Activity update token"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Live Activity Outcome (users.messages.liveactivity.Outcome)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "live_activity_event_outcome" : "(optional, string) Outcome of Live Activity event",
    "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "update_token" : "(optional, string) Live Activity update token"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.liveactivity.Outcome

{
  "activity_attributes_type" : "(optional, string) Live Activity attribute type",
  "activity_id" : "(optional, string) Live Activity identifier",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "live_activity_event_outcome" : "(optional, string) Outcome of Live Activity event",
  "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
  "push_to_start_token" : "(optional, string) Live Activity push to start token",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "update_token" : "(optional, string) Live Activity update token",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Actividad en vivo Enviar eventos {#live-activity-send-events}

{% apitags %}
Actividad en vivo, Envía
{% endapitags %}

Este evento se produce cuando el backend Braze realiza una solicitud a su proveedor en relación con la Actividad en vivo

{% tabs %}
{% tab Amplitude %}
```json
// Live Activity Send (users.messages.liveactivity.Send)

{
  "event_properties" : {
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "update_token" : "(optional, string) Live Activity update token"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Live Activity Send (users.messages.liveactivity.Send)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "update_token" : "(optional, string) Live Activity update token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Live Activity Sends (users.messages.liveactivity.Send)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "activity_attributes_type" : "(optional, string) Live Activity attribute type",
          "activity_id" : "(optional, string) Live Activity identifier",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
          "push_to_start_token" : "(optional, string) Live Activity push to start token",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "update_token" : "(optional, string) Live Activity update token"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Live Activity Sent (users.messages.liveactivity.Send)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "update_token" : "(optional, string) Live Activity update token"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.liveactivity.Send

{
  "activity_attributes_type" : "(optional, string) Live Activity attribute type",
  "activity_id" : "(optional, string) Live Activity identifier",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
  "push_to_start_token" : "(optional, string) Live Activity push to start token",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "update_token" : "(optional, string) Live Activity update token",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de cancelación de notificación push {#push-notification-abort-events}

{% apitags %}
Abortar, Push
{% endapitags %}

Este evento se produce si se ha abortado un mensaje de notificación push en función de las interrupciones de Liquid, etc.

{% tabs %}
{% tab Amplitude %}
```json
// Push Notification Abort (users.messages.pushnotification.Abort)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Push Notification Abort (users.messages.pushnotification.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Push Notification Aborts (users.messages.pushnotification.Abort)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "platform" : "(optional, string) Platform of the device"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Push Notification Aborted (users.messages.pushnotification.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(required, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.pushnotification.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "platform" : "(required, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de rebote de notificaciones push {#push-notification-bounce-events}

{% apitags %}
Push, Envía, Rebota
{% endapitags %}

Este evento se produce cuando se recibe un error del servicio de notificaciones push de Apple o de Fire Cloud Messaging. Esto significa que el mensaje push fue rebotado y, por tanto, no se entregó al dispositivo del usuario.

{% tabs %}
{% tab Amplitude %}
```json
// Push Notification Bounce (users.messages.pushnotification.Bounce)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Push Notification Bounce (users.messages.pushnotification.Bounce)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Push Notification Bounces (users.messages.pushnotification.Bounce)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Push Notification Bounced (users.messages.pushnotification.Bounce)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.pushnotification.Bounce

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalles de la propiedad

- Si utilizas Kafka para la ingesta de datos [de Currents]({{site.baseurl}}/user_guide/data/braze_currents/), ponte en contacto con tu director del éxito del cliente o tu administrador de cuentas para habilitar la función para el envío de `ad_id`.
{% endapi %}

{% api %}
## Notificación push Eventos de apertura en primer plano de iOS {#push-notification-ios-foreground-open-events}

{% apitags %}
Push, iOS, Envía
{% endapitags %}

Este evento no es compatible con nuestro [SDK Swift](https://github.com/braze-inc/braze-swift-sdk) y ahora está obsoleto en nuestro [SDK Obj-C](https://github.com/Appboy/appboy-ios-sdk).

{% tabs %}
{% tab Amplitude %}
```json
// Push Notification iOS Foreground Open (users.messages.pushnotification.IosForeground)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_model" : "(optional, string) Model of the device",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Push Notification iOS Foreground Open (users.messages.pushnotification.IosForeground)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Ios Foreground Push Opened (users.messages.pushnotification.IosForeground)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.pushnotification.IosForeground

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "platform" : "(required, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalles de la propiedad

- Para `ad_id`, `ad_id_type`, y `ad_tracking_enabled`, necesitas recopilar explícitamente el IDFA de publicidad de iOS y el ID de publicidad de Google de Android a través de los SDK nativos. Más información sobre esta configuración para [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift) y [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).
- Si utilizas Kafka para la ingesta de datos [de Currents]({{site.baseurl}}/user_guide/data/braze_currents/), ponte en contacto con tu administrador del éxito del cliente para habilitar el envío de `ad_id`.
{% endapi %}

{% api %}
## Notificación push Eventos abiertos {#push-notification-open-events}

{% apitags %}
Empuja, Abre
{% endapitags %}

Este evento se produce cuando un usuario hace clic directamente en la notificación push para abrir la aplicación. Actualmente, los Eventos de Apertura Push se refieren específicamente a "Direct Opens" y no a "Total Opens". Esto no incluye las estadísticas mostradas a nivel de campaña de "influenced opens", ya que éstas no se atribuyen a nivel de usuario.

{% alert note %}
En raras ocasiones, un push abierto puede aparecer antes que el correspondiente evento push enviado en los datos de Currents debido a lo siguiente:
- Tu SDK tiene un reloj incorrecto.
- Alta latencia de escritura por lotes. La hora de envío registrada puede ir por detrás de las primeras entregas, por lo que es posible que se registren aperturas muy rápidas antes de que se escriba la marca de hora de envío final del lote. Los grandes envíos se despachan y registran por lotes.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Push Notification Open (users.messages.pushnotification.Open)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_model" : "(optional, string) Model of the device",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Push Notification Open (users.messages.pushnotification.Open)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Push Notification Opens (users.messages.pushnotification.Open)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Push Notification Tapped (users.messages.pushnotification.Open)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.pushnotification.Open

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "button_action_type" : "(optional, string) Action type of the push notification button, null if not from a button click. One of ['uri', 'deep_link', 'none', 'close']",
  "button_string" : "(optional, string) Identifier (button_string) of the push notification button clicked. null if not from a button click",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalles de la propiedad

- Para `ad_id`, `ad_id_type`, y `ad_tracking_enabled`, necesitas recopilar explícitamente el IDFA de publicidad de iOS y el ID de publicidad de Google de Android a través de los SDK nativos. Más información sobre esta configuración para [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift) y [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).
- Si utilizas Kafka para la ingesta de datos [de Currents]({{site.baseurl}}/user_guide/data/braze_currents/), ponte en contacto con tu administrador del éxito del cliente para habilitar el envío de `ad_id`.
{% endapi %}

{% api %}
## Notificación push Enviar eventos {#push-notification-send-events}

{% apitags %}
Push, Envía
{% endapitags %}

Este evento se produce cuando Braze procesa un mensaje push para un usuario, comunicándolo al servicio de notificaciones push de Apple o a Fire Cloud Messaging. Esto no significa que se haya entregado el push al dispositivo, sólo que se ha enviado un mensaje.

{% tabs %}
{% tab Amplitude %}
```json
// Push Notification Send (users.messages.pushnotification.Send)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Push Notification Send (users.messages.pushnotification.Send)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Push Notification Sends (users.messages.pushnotification.Send)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
          "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Push Notification Sent (users.messages.pushnotification.Send)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(required, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.pushnotification.Send

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
  "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "platform" : "(required, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalles de la propiedad

- Para `ad_id`, `ad_id_type`, y `ad_tracking_enabled`, necesitas recopilar explícitamente el IDFA de publicidad de iOS y el ID de publicidad de Google de Android a través de los SDK nativos. Más información sobre esta configuración para [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift) y [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).
- Si utilizas Kafka para la ingesta de datos [de Currents]({{site.baseurl}}/user_guide/data/braze_currents/), ponte en contacto con tu administrador del éxito del cliente para habilitar el envío de `ad_id`.
- `message_extras` te permiten anotar tus eventos de envío con datos dinámicos de Contenido conectado, atributos personalizados (como idioma, país) y propiedades de entrada en Canvas. Consulta [Extras de mensajes]({{site.baseurl}}/message_extras_tag/) para obtener más información.
{% endapi %}

{% api %}
## Abortar eventos {#abort--events}

{% apitags %}
RCS, Abortar
{% endapitags %}

Este evento se crea cuando un envío RCS se interrumpe debido a un error detectado en Braze, y el mensaje se abandona.

{% tabs %}
{% tab Amplitude %}
```json
// Abort  (users.messages.rcs.Abort)

{
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) The type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Abort  (users.messages.rcs.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) The type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Aborts (users.messages.rcs.Abort)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) The type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Aborted (users.messages.rcs.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) The type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.rcs.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) The type of abort",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de clic {#click-events}

{% apitags %}
RCS, Clics
{% endapitags %}

Evento que se crea cuando el usuario interactúa con un mensaje RCS de una forma que implica tocar o hacer clic en un elemento de la interfaz de usuario.

{% tabs %}
{% tab Amplitude %}
```json
// Click (users.messages.rcs.Click)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "element_label" : "(optional, string) Optional details about the clicked element, such as the text of a suggested reply or button. \nExample: Button or chip text (will be reply message body for reply chips and buttons)",
    "element_type" : "(optional, string) Specifies if an interaction_type that is common across suggestions and buttons came from a suggestion or button. Examples: Suggestion, Button",
    "interaction_type" : "(required, string) The type of interaction that generated the click. Example string values: Text URL, Reply, OpenURL",
    "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "short_url" : "(optional, string) The shortened URL that a user clicks on",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "suspected_bot_click_reason" : "(optional, array of string) Reasons why this event was classified as a bot",
    "url" : "(optional, string) The full URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the click occurred",
    "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Click (users.messages.rcs.Click)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "element_label" : "(optional, string) Optional details about the clicked element, such as the text of a suggested reply or button. \nExample: Button or chip text (will be reply message body for reply chips and buttons)",
    "element_type" : "(optional, string) Specifies if an interaction_type that is common across suggestions and buttons came from a suggestion or button. Examples: Suggestion, Button",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "interaction_type" : "(required, string) The type of interaction that generated the click. Example string values: Text URL, Reply, OpenURL",
    "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "short_url" : "(optional, string) The shortened URL that a user clicks on",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "suspected_bot_click_reason" : "(optional, array of string) Reasons why this event was classified as a bot",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "url" : "(optional, string) The full URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the click occurred",
    "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Clicks (users.messages.rcs.Click)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "element_label" : "(optional, string) Optional details about the clicked element, such as the text of a suggested reply or button. \nExample: Button or chip text (will be reply message body for reply chips and buttons)",
          "element_type" : "(optional, string) Specifies if an interaction_type that is common across suggestions and buttons came from a suggestion or button. Examples: Suggestion, Button",
          "interaction_type" : "(required, string) The type of interaction that generated the click. Example string values: Text URL, Reply, OpenURL",
          "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "short_url" : "(optional, string) The shortened URL that a user clicks on",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID",
          "url" : "(optional, string) The full URL that the user clicked on",
          "user_agent" : "(optional, string) User agent on which the click occurred"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] The user's phone number from which the message was received"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Clicked (users.messages.rcs.Click)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(required, string) [PII] The user's phone number from which the message was received"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "element_label" : "(optional, string) Optional details about the clicked element, such as the text of a suggested reply or button. \nExample: Button or chip text (will be reply message body for reply chips and buttons)",
    "element_type" : "(optional, string) Specifies if an interaction_type that is common across suggestions and buttons came from a suggestion or button. Examples: Suggestion, Button",
    "interaction_type" : "(required, string) The type of interaction that generated the click. Example string values: Text URL, Reply, OpenURL",
    "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "short_url" : "(optional, string) The shortened URL that a user clicks on",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "suspected_bot_click_reason" : "(optional, array of string) Reasons why this event was classified as a bot",
    "user_agent" : "(optional, string) User agent on which the click occurred"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.rcs.Click

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "element_label" : "(optional, string) Optional details about the clicked element, such as the text of a suggested reply or button. \nExample: Button or chip text (will be reply message body for reply chips and buttons)",
  "element_type" : "(optional, string) Specifies if an interaction_type that is common across suggestions and buttons came from a suggestion or button. Examples: Suggestion, Button",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "interaction_type" : "(required, string) The type of interaction that generated the click. Example string values: Text URL, Reply, OpenURL",
  "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "short_url" : "(optional, string) The shortened URL that a user clicks on",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "suspected_bot_click_reason" : "(optional, array of string) Reasons why this event was classified as a bot",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "url" : "(optional, string) The full URL that the user clicked on",
  "user_agent" : "(optional, string) User agent on which the click occurred",
  "user_id" : "(required, string) Braze user ID of the user who performed this event",
  "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Actos de entrega {#delivery-events}

{% apitags %}
RCS, Entrega
{% endapitags %}

Este evento se crea cuando se entrega correctamente un mensaje RCS al dispositivo móvil de un usuario.

{% tabs %}
{% tab Amplitude %}
```json
// Delivery (users.messages.rcs.Delivery)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_rcs_sender" : "(optional, string) The RCS sender ID or agent name used to send the message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Delivery (users.messages.rcs.Delivery)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "from_rcs_sender" : "(optional, string) The RCS sender ID or agent name used to send the message",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "to_phone_number" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Deliveries (users.messages.rcs.Delivery)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "from_rcs_sender" : "(optional, string) The RCS sender ID or agent name used to send the message",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Delivered (users.messages.rcs.Delivery)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_rcs_sender" : "(optional, string) The RCS sender ID or agent name used to send the message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.rcs.Delivery

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_rcs_sender" : "(optional, string) The RCS sender ID or agent name used to send the message",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "to_phone_number" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Recepción de eventos {#inbound-receive-events}

{% apitags %}
RCS, Entrada Recibida
{% endapitags %}

Este evento se crea cuando Braze recibe un mensaje RCS originado por el usuario.

{% tabs %}
{% tab Amplitude %}
```json
// Inbound Receive (users.messages.rcs.InboundReceive)

{
  "event_properties" : {
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "message_body" : "(optional, string) Typed response from the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_rcs_sender" : "(required, string) The inbound RCS sender that the message was sent to",
    "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Inbound Receive (users.messages.rcs.InboundReceive)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "message_body" : "(optional, string) Typed response from the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "to_rcs_sender" : "(required, string) The inbound RCS sender that the message was sent to",
    "token" : "(required, string) The Mixpanel API token",
    "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Inbound Receives (users.messages.rcs.InboundReceive)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "message_body" : "(optional, string) Typed response from the user",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID",
          "to_rcs_sender" : "(required, string) The inbound RCS sender that the message was sent to"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] The user's phone number from which the message was received"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Inbound Received (users.messages.rcs.InboundReceive)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(required, string) [PII] The user's phone number from which the message was received"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "message_body" : "(optional, string) Typed response from the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_rcs_sender" : "(required, string) The inbound RCS sender that the message was sent to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.rcs.InboundReceive

{
  "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "media_urls" : "(optional, array of string) Media URLs from the user",
  "message_body" : "(required, string) Typed response from the user",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "to_rcs_sender" : "(required, string) The inbound RCS sender that the message was sent to",
  "user_id" : "(required, string) Braze user ID of the user who performed this event",
  "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Leer acontecimientos {#read-events}

{% apitags %}
RCS, Leer
{% endapitags %}

Este evento se crea cuando un usuario abre un mensaje RCS en su dispositivo, indicando que ha visto o leído el contenido del mensaje.

{% tabs %}
{% tab Amplitude %}
```json
// Read (users.messages.rcs.Read)

{
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "to_phone_number" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Read (users.messages.rcs.Read)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "to_phone_number" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Reads (users.messages.rcs.Read)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Read (users.messages.rcs.Read)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.rcs.Read

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "to_phone_number" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de rechazo {#rejection-events}

{% apitags %}
RCS, Rechazo
{% endapitags %}

Evento que se crea cuando un mensaje RCS no se entrega al dispositivo móvil de un usuario debido a la intervención del operador.

{% tabs %}
{% tab Amplitude %}
```json
// Rejection (users.messages.rcs.Rejection)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "error" : "(optional, string) Error name",
    "from_rcs_sender" : "(optional, string) The RCS sender ID or agent name used to send the message",
    "is_sms_fallback" : "(optional, boolean) Indicates if SMS fallback was attempted for this rejected RCS message. It is linked/paired to the SMS Delivery event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(optional, string) The error code from the provider",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Rejection (users.messages.rcs.Rejection)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "error" : "(optional, string) Error name",
    "from_rcs_sender" : "(optional, string) The RCS sender ID or agent name used to send the message",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "is_sms_fallback" : "(optional, boolean) Indicates if SMS fallback was attempted for this rejected RCS message. It is linked/paired to the SMS Delivery event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(optional, string) The error code from the provider",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "to_phone_number" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Rejections (users.messages.rcs.Rejection)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "error" : "(optional, string) Error name",
          "from_rcs_sender" : "(optional, string) The RCS sender ID or agent name used to send the message",
          "is_sms_fallback" : "(optional, boolean) Indicates if SMS fallback was attempted for this rejected RCS message. It is linked/paired to the SMS Delivery event",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "provider_error_code" : "(optional, string) The error code from the provider",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Rejected (users.messages.rcs.Rejection)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "error" : "(optional, string) Error name",
    "from_rcs_sender" : "(optional, string) The RCS sender ID or agent name used to send the message",
    "is_sms_fallback" : "(optional, boolean) Indicates if SMS fallback was attempted for this rejected RCS message. It is linked/paired to the SMS Delivery event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(optional, string) The error code from the provider",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.rcs.Rejection

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "error" : "(optional, string) Error name",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_rcs_sender" : "(optional, string) The RCS sender ID or agent name used to send the message",
  "id" : "(required, string) Globally unique ID for this event",
  "is_sms_fallback" : "(optional, boolean) Indicates if SMS fallback was attempted for this rejected RCS message. It is linked/paired to the SMS Delivery event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "provider_error_code" : "(optional, string) The error code from the provider",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "to_phone_number" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Enviar eventos {#send-events}

{% apitags %}
RCS, Envía
{% endapitags %}

Este evento se crea cuando se envía un mensaje RCS desde Braze a nuestros socios de entrega de última milla.

{% tabs %}
{% tab Amplitude %}
```json
// Send (users.messages.rcs.Send)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_rcs_sender" : "(optional, string) The RCS sender ID or agent name used to send the message",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Send (users.messages.rcs.Send)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "from_rcs_sender" : "(optional, string) The RCS sender ID or agent name used to send the message",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "to_phone_number" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Sends (users.messages.rcs.Send)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "from_rcs_sender" : "(optional, string) The RCS sender ID or agent name used to send the message",
          "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Sent (users.messages.rcs.Send)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_rcs_sender" : "(optional, string) The RCS sender ID or agent name used to send the message",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.rcs.Send

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_rcs_sender" : "(optional, string) The RCS sender ID or agent name used to send the message",
  "id" : "(required, string) Globally unique ID for this event",
  "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "to_phone_number" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## SMS Abortar eventos {#sms-abort-events}

{% apitags %}
Abortar, SMS
{% endapitags %}

Este evento se produce si se ha abortado un mensaje SMS debido a que Liquid lo ha abortado, etc.

{% tabs %}
{% tab Amplitude %}
```json
// SMS Abort (users.messages.sms.Abort)

{
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Abort (users.messages.sms.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Aborts (users.messages.sms.Abort)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// SMS Aborted (users.messages.sms.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.sms.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## SMS Operador Enviar eventos {#sms-carrier-send-events}

{% apitags %}
SMS, Envíos
{% endapitags %}

Este evento se produce cuando se envía un SMS al operador.

{% alert important %}
`CarrierSend` sólo se admite para usuarios de infraestructuras heredadas.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// SMS Carrier Send (users.messages.sms.CarrierSend)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Carrier Send (users.messages.sms.CarrierSend)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Carrier Sends (users.messages.sms.CarrierSend)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// SMS Sent to Carrier (users.messages.sms.CarrierSend)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.sms.CarrierSend

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de entrega de SMS {#sms-delivery-events}

{% apitags %}
SMS, Entrega
{% endapitags %}

Este evento se produce cuando se ha entregado correctamente un SMS al teléfono móvil del usuario.

{% tabs %}
{% tab Amplitude %}
```json
// SMS Delivery (users.messages.sms.Delivery)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "is_sms_fallback" : "(optional, boolean) Indicates that a SMS fallback message was sent due to a rejected RCS message. The message could result in delivery, delivery failure, or rejection. It can be linked to the RCS Rejection event via a send ID and dispatch ID",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Delivery (users.messages.sms.Delivery)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "is_sms_fallback" : "(optional, boolean) Indicates that a SMS fallback message was sent due to a rejected RCS message. The message could result in delivery, delivery failure, or rejection. It can be linked to the RCS Rejection event via a send ID and dispatch ID",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Deliveries (users.messages.sms.Delivery)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
          "is_sms_fallback" : "(optional, boolean) Indicates that a SMS fallback message was sent due to a rejected RCS message. The message could result in delivery, delivery failure, or rejection. It can be linked to the RCS Rejection event via a send ID and dispatch ID",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// SMS Delivered (users.messages.sms.Delivery)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "is_sms_fallback" : "(optional, boolean) Indicates that a SMS fallback message was sent due to a rejected RCS message. The message could result in delivery, delivery failure, or rejection. It can be linked to the RCS Rejection event via a send ID and dispatch ID",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.sms.Delivery

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "is_sms_fallback" : "(optional, boolean) Indicates that a SMS fallback message was sent due to a rejected RCS message. The message could result in delivery, delivery failure, or rejection. It can be linked to the RCS Rejection event via a send ID and dispatch ID",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de fallo en la entrega de SMS {#sms-delivery-failure-events}

{% apitags %}
SMS, Entrega
{% endapitags %}

Este evento se produce cuando un SMS experimenta un fallo en la entrega. Utiliza este evento y los códigos de error proporcionados para ayudar a solucionar problemas con la entrega de SMS.

{% tabs %}
{% tab Amplitude %}
```json
// SMS Delivery Failure (users.messages.sms.DeliveryFailure)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "error" : "(optional, string) Error name",
    "is_sms_fallback" : "(optional, boolean) Indicates that a SMS fallback message was sent due to a rejected RCS message. The message could result in delivery, delivery failure, or rejection. It can be linked to the RCS Rejection event via a send ID and dispatch ID",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(optional, string) Error code from the SMS provider",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Delivery Failure (users.messages.sms.DeliveryFailure)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "error" : "(optional, string) Error name",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "is_sms_fallback" : "(optional, boolean) Indicates that a SMS fallback message was sent due to a rejected RCS message. The message could result in delivery, delivery failure, or rejection. It can be linked to the RCS Rejection event via a send ID and dispatch ID",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(optional, string) Error code from the SMS provider",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Delivery Failures (users.messages.sms.DeliveryFailure)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "error" : "(optional, string) Error name",
          "is_sms_fallback" : "(optional, boolean) Indicates that a SMS fallback message was sent due to a rejected RCS message. The message could result in delivery, delivery failure, or rejection. It can be linked to the RCS Rejection event via a send ID and dispatch ID",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "provider_error_code" : "(optional, string) Error code from the SMS provider",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// SMS Delivery Failed (users.messages.sms.DeliveryFailure)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "error" : "(optional, string) Error name",
    "is_sms_fallback" : "(optional, boolean) Indicates that a SMS fallback message was sent due to a rejected RCS message. The message could result in delivery, delivery failure, or rejection. It can be linked to the RCS Rejection event via a send ID and dispatch ID",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(optional, string) Error code from the SMS provider",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.sms.DeliveryFailure

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "error" : "(optional, string) Error name",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "is_sms_fallback" : "(optional, boolean) Indicates that a SMS fallback message was sent due to a rejected RCS message. The message could result in delivery, delivery failure, or rejection. It can be linked to the RCS Rejection event via a send ID and dispatch ID",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "provider_error_code" : "(optional, string) Error code from the SMS provider",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de recepción de SMS {#sms-inbound-received-events}

{% apitags %}
SMS, Recibidos
{% endapitags %}

Este evento se produce cuando uno de tus usuarios envía un SMS a un número de teléfono de uno de tus grupos de suscripción a Braze SMS.

Cuando Braze recibe un SMS entrante, atribuimos ese mensaje entrante a cualquier usuario que comparta ese número de teléfono. Como resultado, puedes recibir varios eventos por mensaje entrante si varios usuarios de tu instancia de Braze comparten el mismo número de teléfono. Si necesitas la atribución de ID de usuario específicos en función de mensajes anteriores enviados a ese usuario, puedes utilizar el evento SMS entregado para atribuir eventos de recepción de entrada al ID de usuario que haya recibido más recientemente un mensaje de tu número Braze.

Si detectamos que este mensaje entrante es una respuesta a una campaña saliente o a un componente Canvas enviado desde Braze, también incluiremos los metadatos de la campaña o Canvas con el evento. Braze define una respuesta como un mensaje entrante que llega en las cuatro horas siguientes a un mensaje saliente. Sin embargo, hay una caché de un minuto para la información de la campaña atribuida del último SMS saliente recibido.


{% tabs %}
{% tab Amplitude %}
```json
// SMS Inbound Received (users.messages.sms.InboundReceive)

{
  "event_properties" : {
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "message_body" : "(optional, string) Typed response from the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Inbound Received (users.messages.sms.InboundReceive)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "message_body" : "(optional, string) Typed response from the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Inbound Received (users.messages.sms.InboundReceive)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
          "message_body" : "(optional, string) Typed response from the user",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] The user's phone number from which the message was received"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// SMS Inbound Received (users.messages.sms.InboundReceive)

{
  "anonymousId" : "(optional, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(required, string) [PII] The user's phone number from which the message was received"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "message_body" : "(optional, string) Typed response from the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.sms.InboundReceive

{
  "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
  "app_group_id" : "(required, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
  "media_urls" : "(optional, array of string) Media URLs from the user",
  "message_body" : "(required, string) Typed response from the user",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) Braze user ID of the user who performed this event",
  "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Sucesos de rechazo de SMS {#sms-rejection-events}

{% apitags %}
SMS, Rechazo
{% endapitags %}

Este evento se produce cuando un envío de SMS es rechazado por el operador, esto puede ocurrir por varias razones. Utiliza este evento y los códigos de error proporcionados para ayudar a solucionar problemas con la entrega de SMS.

{% tabs %}
{% tab Amplitude %}
```json
// SMS Rejection (users.messages.sms.Rejection)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "error" : "(optional, string) Error name",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "is_sms_fallback" : "(optional, boolean) Indicates that a SMS fallback message was sent due to a rejected RCS message. The message could result in delivery, delivery failure, or rejection. It can be linked to the RCS Rejection event via a send ID and dispatch ID\nIt can be linked to the RCS Rejection event via a send ID and dispatch ID. (Event property)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(optional, string) Error code from the SMS provider",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Rejection (users.messages.sms.Rejection)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "error" : "(optional, string) Error name",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "is_sms_fallback" : "(optional, boolean) Indicates that a SMS fallback message was sent due to a rejected RCS message. The message could result in delivery, delivery failure, or rejection. It can be linked to the RCS Rejection event via a send ID and dispatch ID\nIt can be linked to the RCS Rejection event via a send ID and dispatch ID. (Event property)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(optional, string) Error code from the SMS provider",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Rejections (users.messages.sms.Rejection)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "error" : "(optional, string) Error name",
          "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
          "is_sms_fallback" : "(optional, boolean) Indicates that a SMS fallback message was sent due to a rejected RCS message. The message could result in delivery, delivery failure, or rejection. It can be linked to the RCS Rejection event via a send ID and dispatch ID\nIt can be linked to the RCS Rejection event via a send ID and dispatch ID. (Event property)",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "provider_error_code" : "(optional, string) Error code from the SMS provider",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// SMS Rejected (users.messages.sms.Rejection)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "error" : "(optional, string) Error name",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "is_sms_fallback" : "(optional, boolean) Indicates that a SMS fallback message was sent due to a rejected RCS message. The message could result in delivery, delivery failure, or rejection. It can be linked to the RCS Rejection event via a send ID and dispatch ID\nIt can be linked to the RCS Rejection event via a send ID and dispatch ID. (Event property)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(optional, string) Error code from the SMS provider",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.sms.Rejection

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "error" : "(optional, string) Error name",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "is_sms_fallback" : "(optional, boolean) Indicates that a SMS fallback message was sent due to a rejected RCS message. The message could result in delivery, delivery failure, or rejection. It can be linked to the RCS Rejection event via a send ID and dispatch ID\nIt can be linked to the RCS Rejection event via a send ID and dispatch ID. (Event property)",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "provider_error_code" : "(optional, string) Error code from the SMS provider",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de envío de SMS {#sms-send-events}

{% apitags %}
SMS, Envíos
{% endapitags %}

Este evento se produce cuando un usuario envía un SMS.

{% tabs %}
{% tab Amplitude %}
```json
// SMS Send (users.messages.sms.Send)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Send (users.messages.sms.Send)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Sends (users.messages.sms.Send)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// SMS Sent (users.messages.sms.Send)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.sms.Send

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalles de la propiedad

- `message_extras` te permiten anotar tus eventos de envío con datos dinámicos de Contenido conectado, atributos personalizados (como idioma, país) y propiedades de entrada en Canvas. Consulta [Extras de mensajes]({{site.baseurl}}/message_extras_tag/) para obtener más información.
{% endapi %}

{% api %}
## Enlace corto SMS Eventos de clic {#sms-short-link-click-events}

{% apitags %}
SMS, Clics
{% endapitags %}

Este evento se produce cuando un usuario hace clic en un enlace corto de SMS.

{% tabs %}
{% tab Amplitude %}
```json
// SMS Short Link Click (users.messages.sms.ShortLinkClick)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "short_url" : "(required, string) Shortened url that was clicked",
    "suspected_bot_click_reason" : "(optional, array of string) Why this event was classified as a bot",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred",
    "user_phone_number" : "(optional, string) [PII] The user's phone number from which the message was received"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Short Link Click (users.messages.sms.ShortLinkClick)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "short_url" : "(required, string) Shortened url that was clicked",
    "suspected_bot_click_reason" : "(optional, array of string) Why this event was classified as a bot",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred",
    "user_phone_number" : "(optional, string) [PII] The user's phone number from which the message was received"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Short Link Clicks (users.messages.sms.ShortLinkClick)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "short_url" : "(required, string) Shortened url that was clicked",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "url" : "(optional, string) URL that the user clicked on",
          "user_agent" : "(optional, string) User agent on which the spam report occurred"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] The user's phone number from which the message was received"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// SMS Short Link Clicked (users.messages.sms.ShortLinkClick)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(optional, string) [PII] The user's phone number from which the message was received"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "short_url" : "(required, string) Shortened url that was clicked",
    "suspected_bot_click_reason" : "(optional, array of string) Why this event was classified as a bot",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.sms.ShortLinkClick

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "short_url" : "(required, string) Shortened url that was clicked",
  "suspected_bot_click_reason" : "(optional, array of string) Why this event was classified as a bot",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "url" : "(required, string) URL that the user clicked on",
  "user_agent" : "(optional, string) User agent on which the spam report occurred",
  "user_id" : "(required, string) Braze user ID of the user who performed this event",
  "user_phone_number" : "(optional, string) [PII] The user's phone number from which the message was received"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de abortar webhook {#webhook-abort-events}

{% apitags %}
Abortar, Webhooks
{% endapitags %}

Este evento se produce si se ha abortado un mensaje de webhook en función de los abortos de Liquid, etc.

{% tabs %}
{% tab Amplitude %}
```json
// Webhook Abort (users.messages.webhook.Abort)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Webhook Abort (users.messages.webhook.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Webhook Aborts (users.messages.webhook.Abort)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Webhook Aborted (users.messages.webhook.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.webhook.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de fallo del webhook {#webhook-failure-events}

{% apitags %}
Fallo, Webhooks
{% endapitags %}

Este evento se produce si se entregó un mensaje de webhook pero falló con una respuesta de error del punto final.

{% tabs %}
{% tab Amplitude %}
```json
// Webhook Failure (users.messages.webhook.Failure)

{
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "content_length" : "(optional, int) Content length of the response",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "endpoint_url" : "(optional, string) The endpoint URL of the failed webhook",
    "host" : "(optional, string) The host of the webhook URL that returned a failure response",
    "http_status_code" : "(optional, int) HTTP status code of the response",
    "is_terminal" : "(optional, boolean) Whether this event was the terminal attempt in a send",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "raw_response" : "(optional, string) Truncated raw response from endpoint",
    "retry_count" : "(optional, int) Number of webhook sends attempted before giving up",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "url_path" : "(optional, string) The path of the webhook URL that returned a failure response",
    "webhook_duration" : "(optional, int) Total duration of this request in milliseconds",
    "webhook_failure_source" : "(optional, string) To tell whether an error was created by Braze or by the endpoint itself. The source field could be External Endpoint, Treat no status code to host unreachable"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Webhook Failure (users.messages.webhook.Failure)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "content_length" : "(optional, int) Content length of the response",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "endpoint_url" : "(optional, string) The endpoint URL of the failed webhook",
    "host" : "(optional, string) The host of the webhook URL that returned a failure response",
    "http_status_code" : "(optional, int) HTTP status code of the response",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "is_terminal" : "(optional, boolean) Whether this event was the terminal attempt in a send",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "raw_response" : "(optional, string) Truncated raw response from endpoint",
    "retry_count" : "(optional, int) Number of webhook sends attempted before giving up",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "url_path" : "(optional, string) The path of the webhook URL that returned a failure response",
    "webhook_duration" : "(optional, int) Total duration of this request in milliseconds",
    "webhook_failure_source" : "(optional, string) To tell whether an error was created by Braze or by the endpoint itself. The source field could be External Endpoint, Treat no status code to host unreachable"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Webhook Failures (users.messages.webhook.Failure)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "content_length" : "(optional, int) Content length of the response",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "endpoint_url" : "(optional, string) The endpoint URL of the failed webhook",
          "host" : "(optional, string) The host of the webhook URL that returned a failure response",
          "http_status_code" : "(optional, int) HTTP status code of the response",
          "is_terminal" : "(optional, boolean) Whether this event was the terminal attempt in a send",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "raw_response" : "(optional, string) Truncated raw response from endpoint",
          "retry_count" : "(optional, int) Number of webhook sends attempted before giving up",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "url_path" : "(optional, string) The path of the webhook URL that returned a failure response",
          "webhook_duration" : "(optional, int) Total duration of this request in milliseconds",
          "webhook_failure_source" : "(optional, string) To tell whether an error was created by Braze or by the endpoint itself. The source field could be External Endpoint, Treat no status code to host unreachable"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Webhook Failed (users.messages.webhook.Failure)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "content_length" : "(optional, int) Content length of the response",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "endpoint_url" : "(optional, string) The endpoint URL of the failed webhook",
    "host" : "(optional, string) The host of the webhook URL that returned a failure response",
    "http_status_code" : "(optional, int) HTTP status code of the response",
    "is_terminal" : "(optional, boolean) Whether this event was the terminal attempt in a send",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "raw_response" : "(optional, string) Truncated raw response from endpoint",
    "retry_count" : "(optional, int) Number of webhook sends attempted before giving up",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "url_path" : "(optional, string) The path of the webhook URL that returned a failure response",
    "webhook_duration" : "(optional, int) Total duration of this request in milliseconds",
    "webhook_failure_source" : "(optional, string) To tell whether an error was created by Braze or by the endpoint itself. The source field could be External Endpoint, Treat no status code to host unreachable"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.webhook.Failure

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "content_length" : "(optional, int) Content length of the response",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "endpoint_url" : "(optional, string) The endpoint URL of the failed webhook",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "host" : "(optional, string) The host of the webhook URL that returned a failure response",
  "http_status_code" : "(optional, int) HTTP status code of the response",
  "id" : "(required, string) Globally unique ID for this event",
  "is_terminal" : "(optional, boolean) Whether this event was the terminal attempt in a send",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "raw_response" : "(optional, string) Truncated raw response from endpoint",
  "retry_count" : "(optional, int) Number of webhook sends attempted before giving up",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "url_path" : "(optional, string) The path of the webhook URL that returned a failure response",
  "user_id" : "(required, string) Braze user ID of the user who performed this event",
  "webhook_duration" : "(optional, int) Total duration of this request in milliseconds",
  "webhook_failure_source" : "(optional, string) To tell whether an error was created by Braze or by the endpoint itself. The source field could be External Endpoint, Treat no status code to host unreachable"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Webhook Enviar eventos {#webhook-send-events}

{% apitags %}
Webhooks, Envíos
{% endapitags %}

Este evento se produce cuando un webhook ha sido procesado y enviado al tercero especificado en ese webhook. Ten en cuenta que esto no significa que se haya recibido o no la solicitud.

{% tabs %}
{% tab Amplitude %}
```json
// Webhook Send (users.messages.webhook.Send)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Webhook Send (users.messages.webhook.Send)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Webhook Sends (users.messages.webhook.Send)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Webhook Sent (users.messages.webhook.Send)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.webhook.Send

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalles de la propiedad

- `message_extras` te permiten anotar tus eventos de envío con datos dinámicos del Contenido conectado, atributos personalizados (como el idioma o el país) y propiedades de entrada del Canvas. Consulta [Extras de mensajes]({{site.baseurl}}/message_extras_tag/) para obtener más información.
{% endapi %}

{% api %}
## Eventos de WhatsApp Abortar {#whatsapp-abort-events}

{% apitags %}
WhatsApp, Cancelar
{% endapitags %}

Este evento se produce si se ha abortado un mensaje de WhatsApp debido a que Liquid lo ha abortado, etc.

{% tabs %}
{% tab Amplitude %}
```json
// WhatsApp Abort (users.messages.whatsapp.Abort)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// WhatsApp Abort (users.messages.whatsapp.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, long) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// WhatsApp Aborts (users.messages.whatsapp.Abort)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, long) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// WhatsApp Aborted (users.messages.whatsapp.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, long) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.whatsapp.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Seguimiento de enlaces de WhatsApp Eventos de clic {#whatsapp-tracked-link-click-events}

{% apitags %}
WhatsApp, Clics
{% endapitags %}

Este evento se produce cuando un usuario hace clic en un enlace o botón de un mensaje de WhatsApp en el que el dominio del enlace coincide con el dominio de seguimiento de clics.

{% tabs %}
{% tab Amplitude %}
```json
// WhatsApp Tracked Link Click (users.messages.whatsapp.Click)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "short_url" : "(required, string) Shortened url that was clicked",
    "timezone" : "(optional, string) Time zone of the user",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred",
    "user_phone_number" : "(optional, string) [PII] The user's phone number from which the message was received"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// WhatsApp Tracked Link Click (users.messages.whatsapp.Click)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "short_url" : "(required, string) Shortened url that was clicked",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred",
    "user_phone_number" : "(optional, string) [PII] The user's phone number from which the message was received"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// WhatsApp Tracked Link Clicks (users.messages.whatsapp.Click)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "short_url" : "(required, string) Shortened url that was clicked",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "url" : "(optional, string) URL that the user clicked on",
          "user_agent" : "(optional, string) User agent on which the spam report occurred"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] The user's phone number from which the message was received"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// WhatsApp Tracked Link Clicked (users.messages.whatsapp.Click)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(optional, string) [PII] The user's phone number from which the message was received"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "short_url" : "(required, string) Shortened url that was clicked",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.whatsapp.Click

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "short_url" : "(required, string) Shortened url that was clicked",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "url" : "(required, string) URL that the user clicked on",
  "user_agent" : "(optional, string) User agent on which the spam report occurred",
  "user_id" : "(required, string) Braze user ID of the user who performed this event",
  "user_phone_number" : "(optional, string) [PII] The user's phone number from which the message was received"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Actos de entrega de WhatsApp {#whatsapp-delivery-events}

{% apitags %}
WhatsApp, Entrega
{% endapitags %}

Este evento se produce cuando un mensaje de WhatsApp enviado llega correctamente al dispositivo del usuario.

{% tabs %}
{% tab Amplitude %}
```json
// WhatsApp Delivery (users.messages.whatsapp.Delivery)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_id" : "(optional, string) The unique ID generated by Meta for this message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// WhatsApp Delivery (users.messages.whatsapp.Delivery)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_id" : "(optional, string) The unique ID generated by Meta for this message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message",
    "time" : "(required, long) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// WhatsApp Deliveries (users.messages.whatsapp.Delivery)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
          "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
          "message_id" : "(optional, string) The unique ID generated by Meta for this message",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID",
          "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, long) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// WhatsApp Delivered (users.messages.whatsapp.Delivery)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_id" : "(optional, string) The unique ID generated by Meta for this message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message"
  },
  "timestamp" : "(required, long) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.whatsapp.Delivery

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
  "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "message_id" : "(optional, string) The unique ID generated by Meta for this message",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de fallo de WhatsApp {#whatsapp-failure-events}

{% apitags %}
WhatsApp, Fracaso
{% endapitags %}

Este evento se produce cuando WhatsApp no puede entregar el mensaje al usuario. Un rebote duro significa un fallo permanente en la capacidad de entrega.

{% tabs %}
{% tab Amplitude %}
```json
// WhatsApp Failure (users.messages.whatsapp.Failure)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_id" : "(optional, string) The unique ID generated by Meta for this message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(required, string) Error code from WhatsApp",
    "provider_error_title" : "(required, string) Description of error from WhatsApp",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// WhatsApp Failure (users.messages.whatsapp.Failure)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_id" : "(optional, string) The unique ID generated by Meta for this message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(required, string) Error code from WhatsApp",
    "provider_error_title" : "(required, string) Description of error from WhatsApp",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message",
    "time" : "(required, long) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// WhatsApp Failures (users.messages.whatsapp.Failure)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
          "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
          "message_id" : "(optional, string) The unique ID generated by Meta for this message",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "provider_error_code" : "(required, string) Error code from WhatsApp",
          "provider_error_title" : "(required, string) Description of error from WhatsApp",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID",
          "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, long) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// WhatsApp Failed (users.messages.whatsapp.Failure)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_id" : "(optional, string) The unique ID generated by Meta for this message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(required, string) Error code from WhatsApp",
    "provider_error_title" : "(required, string) Description of error from WhatsApp",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message"
  },
  "timestamp" : "(required, long) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.whatsapp.Failure

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
  "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "message_id" : "(optional, string) The unique ID generated by Meta for this message",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "provider_error_code" : "(required, string) Error code from WhatsApp",
  "provider_error_title" : "(required, string) Description of error from WhatsApp",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos recibidos de WhatsApp {#whatsapp-inbound-received-events}

{% apitags %}
WhatsApp, Recepción
{% endapitags %}

Este evento se produce cuando uno de tus usuarios envía un mensaje de WhatsApp a un número de teléfono de uno de tus grupos de suscripción a Braze WhatsApp.

{% tabs %}
{% tab Amplitude %}
```json
// WhatsApp Inbound Received (users.messages.whatsapp.InboundReceive)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "catalog_id" : "(optional, string) Catalog ID of a product if a product is referenced in the inbound message. Otherwise, empty.",
    "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the user is responding to a WhatsApp Flow.",
    "flow_response_json" : "(optional, string) [PII] The form values the user responded with. Present if the user is responding to a WhatsApp Flow.",
    "in_reply_to" : "(optional, string) The message_id of the message this message was replying to",
    "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "message_body" : "(optional, string) Typed response from the user",
    "message_id" : "(optional, string) The unique ID generated by Meta for this message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "quick_reply_text" : "(optional, string) Text of button pressed by the user",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "productId" : "(optional, string) Product SKU if a product is referenced in the inbound message. Otherwise, empty.",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// WhatsApp Inbound Received (users.messages.whatsapp.InboundReceive)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "catalog_id" : "(optional, string) Catalog ID of a product if a product is referenced in the inbound message. Otherwise, empty.",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the user is responding to a WhatsApp Flow.",
    "flow_response_json" : "(optional, string) [PII] The form values the user responded with. Present if the user is responding to a WhatsApp Flow.",
    "in_reply_to" : "(optional, string) The message_id of the message this message was replying to",
    "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "message_body" : "(optional, string) Typed response from the user",
    "message_id" : "(optional, string) The unique ID generated by Meta for this message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "product_id" : "(optional, string) Product SKU if a product is referenced in the inbound message. Otherwise, empty.",
    "quick_reply_text" : "(optional, string) Text of button pressed by the user",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, long) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// WhatsApp Inbound Received (users.messages.whatsapp.InboundReceive)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "catalog_id" : "(optional, string) Catalog ID of a product if a product is referenced in the inbound message. Otherwise, empty.",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the user is responding to a WhatsApp Flow.",
          "flow_response_json" : "(optional, string) [PII] The form values the user responded with. Present if the user is responding to a WhatsApp Flow.",
          "in_reply_to" : "(optional, string) The message_id of the message this message was replying to",
          "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
          "message_body" : "(optional, string) Typed response from the user",
          "message_id" : "(optional, string) The unique ID generated by Meta for this message",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "product_id" : "(optional, string) Product SKU if a product is referenced in the inbound message. Otherwise, empty.",
          "quick_reply_text" : "(optional, string) Text of button pressed by the user",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, long) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] The user's phone number from which the message was received"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// WhatsApp Inbound Received (users.messages.whatsapp.InboundReceive)

{
  "anonymousId" : "(optional, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(required, string) [PII] The user's phone number from which the message was received"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "catalog_id" : "(optional, string) Catalog ID of a product if a product is referenced in the inbound message. Otherwise, empty.",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the user is responding to a WhatsApp Flow.",
    "flow_response_json" : "(optional, string) [PII] The form values the user responded with. Present if the user is responding to a WhatsApp Flow.",
    "in_reply_to" : "(optional, string) The message_id of the message this message was replying to",
    "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "message_body" : "(optional, string) Typed response from the user",
    "message_id" : "(optional, string) The unique ID generated by Meta for this message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "product_id" : "(optional, string) Product SKU if a product is referenced in the inbound message. Otherwise, empty.",
    "quick_reply_text" : "(optional, string) Text of button pressed by the user",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, long) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.whatsapp.InboundReceive

{
  "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "catalog_id" : "(optional, string) Catalog ID of a product if a product is referenced in the inbound message. Otherwise, empty.",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the user is responding to a WhatsApp Flow.",
  "flow_response_json" : "(optional, string) [PII] The form values the user responded with. Present if the user is responding to a WhatsApp Flow.",
  "id" : "(required, string) Globally unique ID for this event",
  "in_reply_to" : "(optional, string) The message_id of the message this message was replying to",
  "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
  "media_urls" : "(optional, array of string) Media URLs from the user",
  "message_body" : "(optional, string) Typed response from the user",
  "message_id" : "(optional, string) The unique ID generated by Meta for this message",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "product_id" : "(optional, string) Product SKU if a product is referenced in the inbound message. Otherwise, empty.",
  "quick_reply_text" : "(optional, string) Text of button pressed by the user",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(optional, string) Braze user ID of the user who performed this event",
  "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## WhatsApp Leer eventos {#whatsapp-read-events}

{% apitags %}
WhatsApp, Leer
{% endapitags %}

Este evento se produce cuando el usuario lee un mensaje de WhatsApp.

{% tabs %}
{% tab Amplitude %}
```json
// WhatsApp Read (users.messages.whatsapp.Read)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_id" : "(optional, string) The unique ID generated by Meta for this message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// WhatsApp Read (users.messages.whatsapp.Read)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_id" : "(optional, string) The unique ID generated by Meta for this message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message",
    "time" : "(required, long) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// WhatsApp Reads (users.messages.whatsapp.Read)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
          "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
          "message_id" : "(optional, string) The unique ID generated by Meta for this message",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID",
          "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, long) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// WhatsApp Read (users.messages.whatsapp.Read)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_id" : "(optional, string) The unique ID generated by Meta for this message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message"
  },
  "timestamp" : "(required, long) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.whatsapp.Read

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
  "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "message_id" : "(optional, string) The unique ID generated by Meta for this message",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Enviar eventos de WhatsApp {#whatsapp-send-events}

{% apitags %}
WhatsApp, Envía
{% endapitags %}

Este evento se produce cuando una solicitud de envío se ha comunicado correctamente entre Braze y WhatsApp. Sin embargo, esto no significa que el usuario haya recibido el mensaje.

{% tabs %}
{% tab Amplitude %}
```json
// WhatsApp Send (users.messages.whatsapp.Send)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_id" : "(optional, string) The unique ID generated by Meta for this message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp Manager. Present if sending a Template Message",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// WhatsApp Send (users.messages.whatsapp.Send)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_id" : "(optional, string) The unique ID generated by Meta for this message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp Manager. Present if sending a Template Message",
    "time" : "(required, long) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// WhatsApp Sends (users.messages.whatsapp.Send)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
          "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
          "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
          "message_id" : "(optional, string) The unique ID generated by Meta for this message",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID",
          "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp Manager. Present if sending a Template Message"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, long) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// WhatsApp Sent (users.messages.whatsapp.Send)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_id" : "(optional, string) The unique ID generated by Meta for this message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp Manager. Present if sending a Template Message"
  },
  "timestamp" : "(required, long) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.whatsapp.Send

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
  "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
  "message_id" : "(optional, string) The unique ID generated by Meta for this message",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp Manager. Present if sending a Template Message",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}