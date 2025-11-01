---
nav_title: "PUBLICAR: Exportar perfil de usuario por identificador"
article_title: "PUBLICAR: Exportar perfil de usuario por identificador"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Exportar usuarios por identificador de Braze."

---
{% api %}
# Exportar perfil de usuario por identificador
{% apimethod post %}
/users/export/ids
{% endapimethod %}

> Utiliza este punto final para exportar datos de cualquier perfil de usuario especificando un identificador de usuario.

Se pueden incluir hasta 50 `external_ids` o `user_aliases` en una sola solicitud. Si quieres especificar `device_id`, `email_address`, o `phone`, sólo se puede incluir uno de estos identificadores por solicitud.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b9750447-9d94-4263-967f-f816f0c76577 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `users.export.ids`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='users export ids' %}

## Cuerpo de la solicitud

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_ids": (optional, array of strings) External identifiers for users you wish to export,
  "user_aliases": (optional, array of user alias objects) user aliases for users to export,
  "device_id": (optional, string) Device identifier as returned by various SDK methods such as `getDeviceId`,
  "braze_id": (optional, string) Braze identifier for a particular user,
  "email_address": (optional, string) Email address of user,
  "phone": (optional, string) Phone number of user,
  "fields_to_export": (optional, array of strings) Name of user data fields to export
}
```

{% alert note %}
Para los clientes que se hayan incorporado a Braze a partir del 22 de agosto de 2024, se requiere el parámetro de solicitud `fields_to_export`.
{% endalert %}

## Parámetros de la solicitud

| Parámetro          | Obligatoria | Tipo de datos                                                     | Descripción                                                                                  |
| ------------------ | -------- | ------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `external_ids`     | Opcional | Matriz de cadenas                                              | Identificadores externos de los usuarios que deseas exportar.                                              |
| `user_aliases`     | Opcional | Matriz de objeto alias de usuario                                    | [Alias]({{site.baseurl}}/api/objects_filters/user_alias_object/) de usuario para exportar usuarios. |
| `device_id`        | Opcional | Cadena                                                        | Identificador del dispositivo, devuelto por varios métodos del SDK como `getDeviceId`.                 |
| `braze_id`         | Opcional | Cadena                                                        | Identificador Braze de un usuario concreto.                                                      |
| `email_address`    | Opcional | Cadena                                                        | Dirección de correo electrónico del usuario.                                                                       |
| `phone`            | Opcional | Cadena en [E.164](https://en.wikipedia.org/wiki/E.164) formato | Número de teléfono del usuario.                                                                        |
| `fields_to_export` | Opcional\*. | Matriz de cadenas                                              | Nombre de los campos de datos de usuario a exportar.<br><br>\*Este campo es necesario para utilizar el límite de velocidad de 40 peticiones por segundo. Si se omite, se utilizará en su lugar el límite de velocidad predeterminado de 250 peticiones por minuto. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

\*Requerido para clientes que se hayan incorporado a Braze a partir del 22 de agosto de 2024.

## Ejemplo de solicitud
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/export/ids' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_ids": ["user_identifier1", "user_identifier2"],
  "user_aliases": [
    {
      "alias_name": "example_alias",
      "alias_label": "example_label"
    }
  ],
  "device_id": "1234567",
  "braze_id": "braze_identifier",
  "email_address": "example@braze.com",
  "phone": "11112223333",
  "fields_to_export": ["first_name", "email", "purchases"]
}'
```

## Campos a exportar

La siguiente es una lista de elementos `fields_to_export` válidos. El uso de `fields_to_export` para minimizar los datos devueltos puede mejorar el tiempo de respuesta de este punto final de la API:

| Campo a exportar       | Tipo de datos       | Descripción                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `apps`                | Matriz           | Aplicaciones para las que este usuario ha iniciado sesión, que incluye los campos:<br><br>- `name`: nombre de la aplicación<br>- `platform`: plataforma de la aplicación, como iOS, Android o Web<br>- `version`: número o nombre de la versión de la aplicación <br>- `sessions`: número total de sesiones de esta aplicación<br>- `first_used`: fecha de la primera sesión<br>- `last_used`: fecha de la última sesión<br><br>Todos los campos son cadenas.                                                                                                                                                                                                                                                                                       |
| `attributed_campaign` | Cadena          | Datos de [las integraciones de atribución]({{site.baseurl}}/partners/message_orchestration/), si están configuradas. Identificador de una campaña publicitaria concreta.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `attributed_source`   | Cadena          | Datos de [las integraciones de atribución]({{site.baseurl}}/partners/message_orchestration/), si están configuradas. Identificador de la plataforma en la que estaba el anuncio.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `attributed_adgroup`  | Cadena          | Datos de [las integraciones de atribución]({{site.baseurl}}/partners/message_orchestration/), si están configuradas. Identificador de una subagrupación opcional debajo de campaña.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `attributed_ad`       | Cadena          | Datos de [las integraciones de atribución]({{site.baseurl}}/partners/message_orchestration/), si están configuradas. Identificador de un subgrupo opcional por debajo de la campaña y del grupo de anuncios.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `push_subscribe`      | Cadena          | Estado de la suscripción push del usuario.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `email_subscribe`     | Cadena          | Estado de la suscripción por correo electrónico del usuario.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `braze_id`            | Cadena          | Identificador único de usuario específico del dispositivo establecido por Braze para este usuario.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `country`             | Cadena          | País del usuario utilizando la norma [ISO 3166-1 alfa-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `created_at`          | Cadena          | Fecha y hora de creación del perfil de usuario, en formato ISO 8601.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `custom_attributes`   | Objeto          | Pares clave-valor de atributos personalizados para este usuario.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `custom_events`       | Matriz           | Eventos personalizados atribuidos a este usuario en los últimos 90 días.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `devices`             | Matriz           | Información sobre el dispositivo del usuario, que podría incluir lo siguiente dependiendo de la plataforma:<br><br>- `model`: Nombre del modelo del dispositivo<br>- `os`: Sistema operativo del dispositivo<br>- `carrier`: Operador de servicio del dispositivo, si está disponible<br>- `idfv`: identificador del dispositivo Braze (iOS), el identificador de Apple para el proveedor, si existe<br>- `idfa`: (iOS) Identificador de Publicidad, si existe<br>- `device_id`: (Android) Identificador de dispositivo Braze<br>- `google_ad_id`: (Android) Identificador de publicidad de Google Play, si existe<br>- `roku_ad_id`: (Roku) Identificador de publicidad de Roku<br>- `ad_tracking_enabled`: Si el seguimiento de anuncios está habilitado en el dispositivo, puede ser verdadero o falso |
| `dob`                 | Cadena          | Fecha de nacimiento del usuario en el formato `YYYY-MM-DD`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `email`               | Cadena          | Dirección de correo electrónico del usuario.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `external_id`         | Cadena          | Identificador único de usuario para usuarios identificados.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `first_name`          | Cadena          | Nombre del usuario.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `gender`              | Cadena          | Sexo del usuario. Los valores posibles son:<br><br>- `M`: masculino<br>- `F`: mujer<br>- `O`: otros<br>- `N`: no aplicable<br>- `P`: prefiero no decirlo<br>- `nil`: desconocido                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `home_city`           | Cadena          | Ciudad de residencia del usuario.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `language`            | Cadena          | Idioma del usuario en la norma ISO-639-1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `last_coordinates`    | Matriz de flotantes | Ubicación más reciente del dispositivo del usuario, formateada como `[longitude, latitude]`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `last_name`           | Cadena          | Apellido del usuario.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `phone`               | Cadena          | Número de teléfono del usuario en formato E.164.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `purchases`           | Matriz           | Compras que este usuario ha realizado en los últimos 90 días.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `push_tokens`         | Matriz           | Identificador anónimo único que especifica dónde enviar las notificaciones de una aplicación.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `random_bucket`       | Entero         | [Número de contenedor aleatorio]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events#random-bucket-number-event) del usuario, utilizado para crear segmentos uniformemente distribuidos de usuarios aleatorios.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `time_zone`           | Cadena          | Zona horaria del usuario en el mismo formato que la base de datos de zonas horarias de IANA.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `total_revenue`       | Flotante           | Total de ingresos atribuidos a este usuario. Los ingresos totales se calculan en función de las compras que el usuario realizó durante las ventanas de conversión de las campañas y Lienzos que recibió.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `uninstalled_at`      | Marca de tiempo       | Fecha y hora en que el usuario desinstala la aplicación. Se omite si no se ha desinstalado la aplicación.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `user_aliases`        | Objeto          | [Objeto alias de usuario]({{site.baseurl}}/api/objects_filters/user_alias_object#user-alias-object-specification) que contiene `alias_name` y `alias_label`, si existe.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Tenga en cuenta que el punto final `/users/export/ids` reunirá todo el perfil de usuario de este usuario, incluyendo datos como todas las campañas y Canvases recibidos, todos los eventos personalizados realizados, todas las compras realizadas y todos los atributos personalizados. Como resultado, este punto final es más lento que otros puntos finales de la API REST.

Dependiendo de los datos solicitados, este punto final de la API puede no ser suficiente para satisfacer tus necesidades debido al límite de velocidad de 250 solicitudes por minuto. Si prevés utilizar este punto final regularmente para exportar usuarios, considera en su lugar la exportación de usuarios por segmento, que es asíncrona y está más optimizada para grandes extracciones de datos.

## Respuesta

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "users" : (array of object) the data for each of the exported users, may be empty if no users are found,
    "invalid_user_ids" : (optional, array of string) each of the identifiers provided in the request that did not correspond to a known user
}
```

Para ver un ejemplo de los datos accesibles a través de este punto final, consulta el siguiente ejemplo.

### Ejemplo de archivo de exportación de usuario

Objeto de exportación del usuario (incluiremos los menos datos posibles; si falta un campo en el objeto, debe considerarse nulo o vacío):

{% tabs %}
{% tab All fields %}

```json
{
    "created_at": (string),
    "external_id" : (string),
    "user_aliases" : [
      {
        "alias_name" : (string),
        "alias_label" : (string)
      }
    ],
    "braze_id": (string),
    "first_name" : (string),
    "last_name" : (string),
    "email" : (string),
    "dob" : (string) date for the user's date of birth,
    "home_city" : (string),
    "country" : (string) ISO-3166-1 alpha-2 standard,
    "phone" : (string),
    "language" : (string) ISO-639-1 standard,
    "time_zone" : (string),
    "last_coordinates" : (array of float) [lon, lat],
    "gender" : (string) "M" | "F",
    "total_revenue" : (float),
    "attributed_campaign" : (string),
    "attributed_source" : (string),
    "attributed_adgroup" : (string),
    "attributed_ad" : (string),
    "push_subscribe" : (string) "opted_in" | "subscribed" | "unsubscribed",
    "email_subscribe" : (string) "opted_in" | "subscribed" | "unsubscribed",
    "custom_attributes" : (object) custom attribute key-value pairs,
    "custom_events" : [
      {
        "name" : (string),
        "first" : (string) date,
        "last" : (string) date,
        "count" : (int)
      },
      ...
    ],
    "purchases" : [
      {
        "name" : (string),
        "first" : (string) date,
        "last" : (string) date,
        "count" : (int)
      },
      ...
    ],
    "devices" : [
      {
        "model" : (string),
        "os" : (string),
        "carrier" : (string),
        "idfv" : (string) only included for iOS devices when IDFV collection is enabled,
        "idfa" : (string) only included for iOS devices when IDFA collection is enabled,
        "google_ad_id" : (string) only included for Android devices when Google Play Advertising Identifier collection is enabled,
        "roku_ad_id" : (string) only included for Roku devices,
        "ad_tracking_enabled" : (boolean)
      },
      ...
    ],
    "push_tokens" : [
      {
        "app" : (string) app name,
        "platform" : (string),
        "token" : (string),
        "device_id": (string),
        "notifications_enabled": (boolean) whether the user's push notifications are turned on or turned off
      },
      ...
    ],
    "apps" : [
      {
        "name" : (string),
        "platform" : (string),
        "version" : (string),
        "sessions" : (integer),
        "first_used" : (string) date,
        "last_used" : (string) date
      },
      ...
    ],
    "campaigns_received" : [
      {
        "name" : (string),
        "last_received" : (string) date,
        "engaged" :
         {
           "opened_email" : (boolean),
           "opened_push" : (boolean),
           "clicked_email" : (boolean),
           "clicked_triggered_in_app_message" : (boolean)
          },
          "converted" : (boolean),
          "api_campaign_id" : (string),
          "variation_name" : (optional, string) exists only if it is a multivariate campaign,
          "variation_api_id" : (optional, string) exists only if it is a multivariate campaign,
          "in_control" : (optional, boolean) exists only if it is a multivariate campaign
        },
      ...
    ],
    "canvases_received": [
      {
        "name": (string),
        "api_canvas_id": (string),
        "last_received_message": (string) date,
        "last_entered": (string) date,
        "variation_name": (string),
        "in_control": (boolean),
        "last_exited": (string) date,
        "steps_received": [
          {
            "name": (string),
            "api_canvas_step_id": (string),
            "last_received": (string) date
          },
          {
            "name": (string),
            "api_canvas_step_id": (string),
            "last_received": (string) date
          },
          {
            "name": (string),
            "api_canvas_step_id": (string),
            "last_received": (string) date
          }
        ]
      },
      ...
    ],
    "cards_clicked" : [
      {
        "name" : (string)
      },
      ...
    ]
}
```

{% endtab %}
{% tab Sample output %}

```json
{
    "created_at" : "2020-07-10 15:00:00.000 UTC",
    "external_id" : "A8i3mkd99",
    "user_aliases" : [
      {
        "alias_name" : "user_123",
        "alias_label" : "amplitude_id"
      }
    ],
    "braze_id": "5fbd99bac125ca40511f2cb1",
    "random_bucket" : 2365,
    "first_name" : "Jane",
    "last_name" : "Doe",
    "email" : "example@braze.com",
    "dob" : "1980-12-21",
    "home_city" : "Chicago",
    "country" : "US",
    "phone" : "+442071838750",
    "language" : "en",
    "time_zone" : "Eastern Time (US & Canada)",
    "last_coordinates" : [41.84157636433568, -87.83520818508256],
    "gender" : "F",
    "total_revenue" : 65,
    "attributed_campaign" : "braze_test_campaign_072219",
    "attributed_source" : "braze_test_source_072219",
    "attributed_adgroup" : "braze_test_adgroup_072219",
    "attributed_ad" : "braze_test_ad_072219",
    "push_subscribe" : "opted_in",
    "push_opted_in_at": "2020-01-26T22:45:53.953Z",
    "email_subscribe" : "subscribed",
    "custom_attributes":
    {
      "loyaltyId": "37c98b9d-9a7f-4b2f-a125-d873c5152856",
      "loyaltyPoints": "321",
       "loyaltyPointsNumber": 107
    },
    "custom_events": [
      {
        "name": "Loyalty Acknowledgement",
        "first": "2021-06-28T17:02:43.032Z",
        "last": "2021-06-28T17:02:43.032Z",
        "count": 1
      },
      ...
    ],
    "purchases": [
      {
        "name": "item_40834",
        "first": "2021-09-05T03:45:50.540Z",
        "last": "2022-06-03T17:30:41.201Z",
        "count": 10
      },
      ...
    ],
    "devices": [
      {
        "model": "Pixel XL",
        "os": "Android (Q)",
        "carrier": null,
        "device_id": "312ef2c1-83db-4789-967-554545a1bf7a",
        "ad_tracking_enabled": true
      },
      ...
    ],
    "push_tokens": [
      {
        "app": "MovieCanon",
        "platform": "Android",
        "token": "12345abcd",
        "device_id": "312ef2c1-83db-4789-967-554545a1bf7a",
        "notifications_enabled": true
      },
      ...
    ],
    "apps": [
      {
        "name": "MovieCannon",
        "platform": "Android",
        "version": "3.29.0",
        "sessions": 1129,
        "first_used": "2020-02-02T19:56:19.142Z",
        "last_used": "2021-11-11T00:25:19.201Z"
      },
      ...
    ],
    "campaigns_received": [
      {
        "name": "Email Unsubscribe",
        "api_campaign_id": "d72fdc84-ddda-44f1-a0d5-0e79f47ef942",
        "last_received": "2022-06-02T03:07:38.105Z",
        "engaged":
        {
           "opened_email": true
        },
        "converted": true,
        "multiple_converted":
        {
          "Primary Conversion Event - A": true
        },
        "in_control": false,
        "variation_name": "Variant 1",
        "variation_api_id": "1bddc73a-a134-4784-9134-5b5574a9e0b8"
      },
      ...
    ],
    "canvases_received": [
      {
        "name": "Non Global  Holdout Group 4/21/21",
        "api_canvas_id": "46972a9d-dc81-473f-aa03-e3473b4ed781",
        "last_received_message": "2021-07-07T20:46:24.136Z",
        "last_entered": "2021-07-07T20:45:24.000+00:00",
        "variation_name": "Variant 1",
        "in_control": false,
        "last_entered_control_at": null,
        "last_exited": "2021-07-07T20:46:24.136Z",
        "steps_received": [
          {
            "name": "Step",
            "api_canvas_step_id": "43d1a349-c3c8-4be1-9fbe-ce708e4d1c39",
            "last_received": "2021-07-07T20:46:24.136Z"
          },
          ...
        ]
      }
      ...
    ],    
    "cards_clicked" : [
      {
        "name" : "Loyalty Promo"
      },
      ...
    ]
}
```

{% endtab %}
{% endtabs %}

{% alert tip %}
Para obtener ayuda con las exportaciones CSV y API, visita [Solución de problemas de exportación]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
