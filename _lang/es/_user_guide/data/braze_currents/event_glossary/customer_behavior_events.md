---
nav_title: Comportamiento del cliente y eventos de usuario
layout: customer_behavior_events_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "Este glosario enumera los distintos Eventos de comportamiento del cliente y del usuario que Braze puede rastrear y enviar a los Almacenes de datos elegidos mediante Currents."
tool: Currents
search_rank: 7
---

Póngase en contacto con su representante de Braze o abra un [ticket de soporte]({{site.baseurl}}/braze_support/) si necesita acceder a derechos de eventos adicionales. Si no encuentras lo que necesitas en esta página, consulta nuestra [Biblioteca de Eventos de Interacción con Mensajes]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) o nuestros [ejemplos de datos de muestra Currents](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explicación del comportamiento del cliente y de la estructura de eventos del usuario y valores de la plataforma %}

### Estructura del evento

Este desglose del comportamiento del cliente y de los eventos del usuario muestra qué tipo de información se incluye generalmente en un comportamiento del cliente o en un evento del usuario. Con una sólida comprensión de sus componentes, tus desarrolladores y el equipo de estrategia de inteligencia empresarial pueden utilizar los datos de eventos Currents entrantes para elaborar informes y gráficos basados en datos, y aprovechar otras valiosas métricas de datos.

![Desglose de un evento de usuario que muestra un evento de compra con las propiedades enumeradas agrupadas por propiedades específicas del usuario, propiedades específicas del comportamiento y propiedades específicas del dispositivo]({% image_buster /assets/img/customer_engagement_event.png %})

El comportamiento del cliente y los eventos del usuario se componen de propiedades **específicas del usuario**, propiedades **específicas del comportamiento** y propiedades **específicas del dispositivo**.

### Valores de la plataforma

Algunos eventos devuelven un valor `platform` que especifica la plataforma del dispositivo del usuario.
<br>La siguiente tabla detalla los posibles valores devueltos:

| Dispositivo de usuario | Valor de la plataforma |
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
Los esquemas de almacenamiento se aplican a los datos de eventos de archivos planos que enviamos a los socios de almacenamiento de datos (como Google Cloud Storage, Amazon S3 y Microsoft Azure Blob Storage). Algunas combinaciones de eventos y destinos que figuran en esta lista aún no están disponibles de forma general. Para saber qué actos cuentan con el apoyo de distintos socios, consulta nuestra lista de [socios disponibles]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) y consulta sus respectivas páginas.<br><br>Además, ten en cuenta que Currents eliminará los eventos con cargas útiles excesivamente grandes, superiores a 900 KB.
{% endalert %}
{% api %}
## Eventos de actualización del número de contenedor aleatorio

{% apitags %}
Número de contenedor aleatorio
{% endapitags %}

Este evento de usuario se produce cada vez que se crea un nuevo usuario dentro de su área de trabajo. Durante este evento, a cada nuevo usuario se le asigna un número de contenedor aleatorio que puedes utilizar para crear segmentos de usuarios aleatorios distribuidos uniformemente. Utilízalo para agrupar una serie de valores de número de contenedor aleatorios y comparar el rendimiento de tus campañas y variantes de campaña.

{% alert important %}
Este evento de Currents sólo está disponible para clientes que hayan adquirido un "conector para todos los eventos" y sólo está disponible para conectores de eventos de almacenamiento (como Amazon S3, Microsoft Azure y Google Cloud Storage).
<br><br>Para habilitar este evento y programar el relleno de los números de contenedor aleatorios de los usuarios existentes en tu espacio de trabajo, ponte en contacto con tu administrador del éxito del cliente.
{% endalert %}

{% tabs %}
{% tab Almacenamiento en la nube %}
```json
// users.RandomBucketNumberUpdate

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "prev_random_bucket_number" : "(optional, int) Previous random bucket number",
  "random_bucket_number" : "(required, int) New random bucket number",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos personalizados

{% apitags %}
Eventos personalizados
{% endapitags %}

Este evento se produce cuando se activa un evento personalizado específico. Utilícelo para rastrear cuando los usuarios realizan eventos personalizados en su aplicación.

{% tabs %}
{% tab Amplitud %}
```json
// [Braze Custom Event] (users.behaviors.CustomEvent)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device"
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
// [Braze Custom Event] (users.behaviors.CustomEvent)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}


```json
// users.behaviors.CustomEvent

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "name" : "(required, string) Name of the custom event"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Almacenamiento en la nube %}
```json
// users.behaviors.CustomEvent

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "name" : "(required, string) Name of the custom event",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "properties" : "(required, string) Custom properties stored as a JSON encoded string",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalles de la propiedad

- 
- Para `ad_id`, `ad_id_type`, y `ad_tracking_enabled`, necesitas recopilar explícitamente el IDFA del anuncio de iOS y el ID de Google Ads de Android a través de los SDK nativos. Más información aquí: [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).
- Si utilizas Kafka para la ingesta de datos [de Currents]({{site.baseurl}}/user_guide/data/braze_currents/), ponte en contacto con tu director del éxito del cliente o tu administrador de cuentas para habilitar la función para el envío de `ad_id`.
{% endapi %}

{% api %}
## Eventos de atribución de instalación

{% apitags %}
Atribución
{% endapitags %}

Este evento se produce cuando la instalación de una aplicación se atribuye a una fuente. Utilízalo para saber de dónde proceden las instalaciones de tu aplicación.

{% tabs %}
{% tab Amplitud %}
```json
// Install Attribution (users.behaviors.InstallAttribution)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "source" : "(optional, string) The source of the attribution"
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
// Install Attribution (users.behaviors.InstallAttribution)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "source" : "(optional, string) The source of the attribution",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}


```json
// Install Attribution (users.behaviors.InstallAttribution)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "source" : "(required, string) The source of the attribution"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Almacenamiento en la nube %}
```json
// users.behaviors.InstallAttribution

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "source" : "(required, string) The source of the attribution",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de ubicación

{% apitags %}
Ubicaciones
{% endapitags %}

Este evento se activa cuando un usuario visita un lugar determinado. Utilícelo para realizar un seguimiento de los usuarios que activan eventos de ubicación en su aplicación.

{% tabs %}
{% tab Amplitud %}
```json
// Location (users.behaviors.Location)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "alt_accuracy" : "(optional, float) Altitude accuracy of recorded location",
    "altitude" : "(optional, float) [PII] Altitude of recorded location",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "latitude" : "(required, float) [PII] Latitude of recorded location",
    "ll_accuracy" : "(optional, float) Accuracy of the latitude and longitude of recorded location",
    "longitude" : "(required, float) [PII] Longitude of recorded location",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device"
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
// Location (users.behaviors.Location)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "alt_accuracy" : "(optional, float) Altitude accuracy of recorded location",
    "altitude" : "(optional, float) [PII] Altitude of recorded location",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "latitude" : "(required, float) [PII] Latitude of recorded location",
    "ll_accuracy" : "(optional, float) Accuracy of the latitude and longitude of recorded location",
    "longitude" : "(required, float) [PII] Longitude of recorded location",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}


```json
// Location (users.behaviors.Location)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "alt_accuracy" : "(optional, float) Altitude accuracy of recorded location",
    "altitude" : "(optional, float) [PII] Altitude of recorded location",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "latitude" : "(required, float) [PII] Latitude of recorded location",
    "ll_accuracy" : "(optional, float) Accuracy of the latitude and longitude of recorded location",
    "longitude" : "(required, float) [PII] Longitude of recorded location"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Almacenamiento en la nube %}
```json
// users.behaviors.Location

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "alt_accuracy" : "(optional, float) Altitude accuracy of recorded location",
  "altitude" : "(optional, float) [PII] Altitude of recorded location",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "latitude" : "(required, float) [PII] Latitude of recorded location",
  "ll_accuracy" : "(optional, float) Accuracy of the latitude and longitude of recorded location",
  "longitude" : "(required, float) [PII] Longitude of recorded location",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalles de la propiedad

- Para `ad_id`, `ad_id_type`, y `ad_tracking_enabled`, necesitas recopilar explícitamente el IDFA del anuncio de iOS y el ID de Google Ads de Android a través de los SDK nativos. Más información aquí: [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).
- Si utilizas Kafka para la ingesta de datos [de Currents]({{site.baseurl}}/user_guide/data/braze_currents/), ponte en contacto con tu director del éxito del cliente o tu administrador de cuentas para habilitar la función para el envío de `ad_id`.
{% endapi %}

{% api %}
## Eventos de compra

{% apitags %}
Compras
{% endapitags %}

Este evento se produce cuando un usuario realiza una compra. Utilice estos datos para rastrear cuándo los usuarios compran algo en la aplicación.

{% alert tip %}
Las compras son eventos personalizados especiales y vienen con una cadena codificada JSON de propiedades de eventos personalizados de la misma forma que los eventos personalizados.
{% endalert %}

{% tabs %}
{% tab Amplitud %}
```json
// Purchase (users.behaviors.Purchase)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "currency" : "(required, string) Currency of the purchase",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "price" : "(required, float) Price of the purchase",
  "productId" : "(required, string) ID of the product purchased",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Purchase (users.behaviors.Purchase)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "currency" : "(required, string) Currency of the purchase",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "price" : "(required, float) Price of the purchase",
    "product_id" : "(required, string) ID of the product purchased",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}


```json
// Purchased (users.behaviors.Purchase)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "currency" : "(required, string) Currency of the purchase",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "price" : "(required, float) Price of the purchase",
    "product_id" : "(required, string) ID of the product purchased"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Almacenamiento en la nube %}
```json
// users.behaviors.Purchase

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "currency" : "(required, string) Currency of the purchase",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "price" : "(required, float) Price of the purchase",
  "product_id" : "(required, string) ID of the product purchased",
  "properties" : "(required, string) Custom properties stored as a JSON encoded string",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Detalles de la propiedad

- 
- Para `ad_id`, `ad_id_type`, y `ad_tracking_enabled`, necesitas recopilar explícitamente el IDFA del anuncio de iOS y el ID de Google Ads de Android a través de los SDK nativos. Más información aquí: [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).
- Si utilizas Kafka para la ingesta de datos [de Currents]({{site.baseurl}}/user_guide/data/braze_currents/), ponte en contacto con tu director del éxito del cliente o tu administrador de cuentas para habilitar la función para el envío de `ad_id`.
{% endapi %}

{% api %}
## Actos de la Primera Sesión

{% apitags %}
Sesiones
{% endapitags %}

Este evento se produce cuando un usuario inicia su primera sesión en tu aplicación. Utilice estos datos para saber cuándo inician sesión los usuarios.

{% alert tip %}
Cuando un usuario inicia su primera sesión, se disparan los eventos `FirstSession` y `SessionStart`.
{% endalert %}

{% tabs %}
{% tab Amplitud %}
```json
// First Session (users.behaviors.app.FirstSession)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session"
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
// First Session (users.behaviors.app.FirstSession)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}


```json
// First Session (users.behaviors.app.FirstSession)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "session_id" : "(required, string) UUID of the session"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Almacenamiento en la nube %}
```json
// users.behaviors.app.FirstSession

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "country" : "(optional, string) [DEPRECATED]",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "gender" : "(optional, string) [DEPRECATED]",
  "id" : "(required, string) Globally unique ID for this event",
  "language" : "(optional, string) [DEPRECATED]",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "sdk_version" : "(optional, string) [DEPRECATED]",
  "session_id" : "(required, string) UUID of the session",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de fin de sesión

{% apitags %}
Sesiones
{% endapitags %}

Esto ocurre cuando un usuario sale de su aplicación, terminando así su sesión actual. Utilice estos datos para realizar un seguimiento de cuándo finalizan las sesiones y, junto con el evento de inicio de sesión correspondiente, calcular la duración de su tiempo en una sesión.

{% tabs %}
{% tab Amplitud %}
```json
// Session End (users.behaviors.app.SessionEnd)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "duration" : "(optional, float) Duration of the session in seconds",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session"
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
// Session End (users.behaviors.app.SessionEnd)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "duration" : "(optional, float) Duration of the session in seconds",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}


```json
// Session Ended (users.behaviors.app.SessionEnd)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "duration" : "(optional, float) Duration of the session in seconds",
    "session_id" : "(required, string) UUID of the session"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Almacenamiento en la nube %}
```json
// users.behaviors.app.SessionEnd

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "duration" : "(optional, float) Duration of the session in seconds",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "session_id" : "(required, string) UUID of the session",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de inicio de sesión

{% apitags %}
Sesiones
{% endapitags %}

Este evento se produce cuando un usuario inicia una sesión. Utilice estos datos para saber cuándo inician sesión los usuarios.

{% alert tip %}
Cuando un usuario inicia su primera sesión, se disparan los eventos `FirstSession` y `SessionStart`.
{% endalert %}

{% tabs %}
{% tab Amplitud %}
```json
// Session Start (users.behaviors.app.SessionStart)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session"
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
// Session Start (users.behaviors.app.SessionStart)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}


```json
// Session Started (users.behaviors.app.SessionStart)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "session_id" : "(required, string) UUID of the session"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Almacenamiento en la nube %}
```json
// users.behaviors.app.SessionStart

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "session_id" : "(required, string) UUID of the session",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## 

{% apitags %}

{% endapitags %}



{% tabs %}
{% tab Amplitud %}
```json
// Live Activity Push To Start Token Change (users.behaviors.liveactivity.PushToStartTokenChange)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type"
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
// Live Activity Push To Start Token Change (users.behaviors.liveactivity.PushToStartTokenChange)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}


```json
// Live Activity Push To Start Token Changed (users.behaviors.liveactivity.PushToStartTokenChange)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Almacenamiento en la nube %}
```json
// users.behaviors.liveactivity.PushToStartTokenChange

{
  "activity_attributes_type" : "(optional, string) Live Activity attribute type",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
  "push_to_start_token" : "(optional, string) Live Activity push to start token",
  "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## 

{% apitags %}

{% endapitags %}



{% tabs %}
{% tab Amplitud %}
```json
// Live Activity Update Token Change (users.behaviors.liveactivity.UpdateTokenChange)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
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
// Live Activity Update Token Change (users.behaviors.liveactivity.UpdateTokenChange)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "update_token" : "(optional, string) Live Activity update token"
  }
}
```
{% endtab %}


```json
// Live Activity Update Token Changed (users.behaviors.liveactivity.UpdateTokenChange)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "update_token" : "(optional, string) Live Activity update token"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Almacenamiento en la nube %}
```json
// users.behaviors.liveactivity.UpdateTokenChange

{
  "activity_id" : "(optional, string) Live Activity identifier",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
  "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "update_token" : "(optional, string) Live Activity update token",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## 

{% apitags %}

{% endapitags %}

 

{% tabs %}
{% tab Amplitud %}
```json
// Push Notification Token State Change (users.behaviors.pushnotification.TokenStateChange)

{
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "platform" : "(optional, string) Platform of the device",
    "push_token_created_at" : "(optional, int) UNIX timestamp at which the push token was created",
    "push_token_device_id" : "(optional, string) Device id of the push token",
    "push_token_foreground_push_disabled" : "(optional, boolean) Foreground push disabled flag of the push token",
    "push_token_provisionally_opted_in" : "(optional, boolean) Provisionally opted in flag of the push token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "push_token_updated_at" : "(optional, int) UNIX timestamp at which the push token was last updated",
    "web_push_token_public_key" : "(optional, string) Public key of the push token, only applies to web push tokens",
    "web_push_token_user_auth" : "(optional, string) User auth of the push token, only applies to web push tokens",
    "web_push_token_vapid_public_key" : "(optional, string) VAPID public key of the push token, only applies to web push tokens"
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
// Push Notification Token State Change (users.behaviors.pushnotification.TokenStateChange)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "platform" : "(optional, string) Platform of the device",
    "push_token" : "(optional, string) Push token of the event",
    "push_token_created_at" : "(optional, int) UNIX timestamp at which the push token was created",
    "push_token_device_id" : "(optional, string) Device id of the push token",
    "push_token_foreground_push_disabled" : "(optional, boolean) Foreground push disabled flag of the push token",
    "push_token_provisionally_opted_in" : "(optional, boolean) Provisionally opted in flag of the push token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "push_token_updated_at" : "(optional, int) UNIX timestamp at which the push token was last updated",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "web_push_token_public_key" : "(optional, string) Public key of the push token, only applies to web push tokens",
    "web_push_token_user_auth" : "(optional, string) User auth of the push token, only applies to web push tokens",
    "web_push_token_vapid_public_key" : "(optional, string) VAPID public key of the push token, only applies to web push tokens"
  }
}
```
{% endtab %}


```json
// Push Notification Token State Changed (users.behaviors.pushnotification.TokenStateChange)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_token" : "(optional, string) Push token of the event",
    "push_token_created_at" : "(optional, int) UNIX timestamp at which the push token was created",
    "push_token_device_id" : "(optional, string) Device id of the push token",
    "push_token_foreground_push_disabled" : "(optional, boolean) Foreground push disabled flag of the push token",
    "push_token_provisionally_opted_in" : "(optional, boolean) Provisionally opted in flag of the push token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "push_token_updated_at" : "(optional, int) UNIX timestamp at which the push token was last updated",
    "web_push_token_public_key" : "(optional, string) Public key of the push token, only applies to web push tokens",
    "web_push_token_user_auth" : "(optional, string) User auth of the push token, only applies to web push tokens",
    "web_push_token_vapid_public_key" : "(optional, string) VAPID public key of the push token, only applies to web push tokens"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Almacenamiento en la nube %}
```json
// users.behaviors.pushnotification.TokenStateChange

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
  "platform" : "(optional, string) Platform of the device",
  "push_token_created_at" : "(optional, int) UNIX timestamp at which the push token was created",
  "push_token_device_id" : "(optional, string) Device id of the push token",
  "push_token_foreground_push_disabled" : "(optional, boolean) Foreground push disabled flag of the push token",
  "push_token_provisionally_opted_in" : "(optional, boolean) Provisionally opted in flag of the push token",
  "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
  "push_token_updated_at" : "(optional, int) UNIX timestamp at which the push token was last updated",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event",
  "web_push_token_public_key" : "(optional, string) Public key of the push token, only applies to web push tokens",
  "web_push_token_user_auth" : "(optional, string) User auth of the push token, only applies to web push tokens",
  "web_push_token_vapid_public_key" : "(optional, string) VAPID public key of the push token, only applies to web push tokens"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}
