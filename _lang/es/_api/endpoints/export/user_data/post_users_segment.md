---
nav_title: "POST: Exportar perfil de usuario por segmento"
article_title: "POST: Exportar perfil de usuario por segmento"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Exportar usuarios por segmento de Braze."

---
{% api %}
# Exportar perfil de usuario por segmento
{% apimethod post %}
/users/export/segment
{% endapimethod %}

> Utiliza este punto final para exportar todos los usuarios de un segmento. 

{% alert important %}
Cuando utilices este punto final, ten en cuenta lo siguiente:<br><br>1\. El campo `fields_to_export` de esta solicitud API es **obligatorio**.<br>2\. Los campos de `custom_events`, `purchases`, `campaigns_received` y `canvases_received` solo contienen datos de los últimos 90 días.
{% endalert %}

Los datos de usuario se exportan como varios archivos de objetos JSON de usuario separados por nuevas líneas (como un objeto JSON por línea). Los datos se exportan a una URL generada automáticamente, o a un contenedor de S3 si esta integración ya está configurada.

Ten en cuenta que una empresa puede ejecutar como máximo una exportación por segmento con este punto final en un momento dado. Espera a que se complete la exportación antes de volver a intentarlo. 

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cfa6fa98-632c-4f25-8789-6c3f220b9457 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `users.export.segment`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Detalles de la respuesta basados en credenciales

Si has añadido tus credenciales de [S3][1], [Azure][2] o [Google Cloud Storage][3] a Braze, cada archivo se cargará en tu contenedor como un archivo ZIP con el formato de clave similar a `segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip`. Si utilizas Azure, asegúrate de que tienes marcada la casilla **Hacer de éste el destino predeterminado de exportación de datos** en la página del socio de Azure en Braze. Por lo general, crearemos 1 archivo por cada 5.000 usuarios para optimizar el procesamiento. Exportar segmentos más pequeños dentro de un espacio de trabajo grande puede dar lugar a varios archivos. A continuación, puedes extraer los archivos y concatenar todos los archivos `json` en un único archivo si es necesario. Si especificas un `output_format` de `gzip`, la extensión del archivo será `.gz` en lugar de `.zip`.

{% details Desglose de rutas de exportación para ZIP %}
**Formato ZIP:**
`bucket-name/segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip`

**Ejemplo ZIP:**
`braze.docs.bucket/segment-export/abc56c0c-rd4a-pb0a-870pdf4db07q/2019-04-25/d9696570-dfb7-45ae-baa2-25e302r2da27-1556044807/114f0226319130e1a4770f2602b5639a.zip`

| Propiedad                        | Detalles                                                                              | Se muestra en el ejemplo como                    |
| ------------------------------- | ------------------------------------------------------------------------------------ |
| `bucket-name`                   | Solucionado en función de su nombre de contenedor.                                                     | `braze.docs.bucket`                    |
| `segment-export`                | Solucionado.                                                                               | `segment-export`                       |
| `SEGMENT_ID`                    | Incluido en la solicitud de exportación.                                                      | `abc56c0c-rd4a-pb0a-870pdf4db07q`      |
| `YYYY-MM-dd`                    | La fecha cuando se recibe la devolución de llamada con éxito.                                        | `2019-04-25`                           |
| `RANDOM_UUID`                   | Un UUID aleatorio generado por Braze en el momento de la solicitud.                         | `d9696570-dfb7-45ae-baa2-25e302r2da27` |
| `TIMESTAMP_WHEN_EXPORT_STARTED` | Hora Unix (segundos desde 2017-01-01:00:00:00Z) en que se solicitó la exportación en UTC. | `1556044807`                           |
| `filename`                      | Aleatorio por archivo.                                                                     | `114f0226319130e1a4770f2602b5639a`     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% enddetails %}

Le recomendamos encarecidamente que configure sus propias credenciales de S3 o Azure cuando utilice este punto final para aplicar sus propias políticas de bucket en la exportación. Si no tienes tus credenciales de almacenamiento en la nube, la respuesta a la solicitud proporciona la URL donde se puede descargar un archivo ZIP que contiene todos los archivos del usuario. La URL sólo se convertirá en una ubicación válida cuando la exportación esté lista. 

Ten en cuenta que si no proporcionas tus credenciales de almacenamiento en la nube, existe una limitación en la cantidad de datos que puedes exportar desde este punto final. Dependiendo de los campos que estés exportando y del número de usuarios, la transferencia del archivo puede fallar si es demasiado grande. Una buena práctica es especificar los campos que quieres exportar utilizando `fields_to_export` y especificar sólo los campos que necesitas para que el tamaño de la transferencia sea menor. Si obtienes errores al generar el archivo, considera la posibilidad de dividir tu base de usuarios en más segmentos basándote en un número de contenedor aleatorio (por ejemplo, crea un segmento en el que el número de contenedor aleatorio sea inferior a 1.000 o esté comprendido entre 1.000 y 2.000).

En cualquiera de los dos casos, puedes proporcionar opcionalmente un `callback_endpoint` para que se te notifique cuando la exportación esté lista. Si se facilita la dirección `callback_endpoint`, haremos una petición por correo a la dirección facilitada cuando la descarga esté lista. El cuerpo de la publicación será "success":true. Si no has añadido credenciales de S3 a Braze, el cuerpo de la entrada tendrá además el atributo `url` con la URL de descarga como valor.

Las bases de usuarios más grandes darán lugar a tiempos de exportación más largos. Por ejemplo, una aplicación con 20 millones de usuarios podría tardar una hora o más.

## Cuerpo de la solicitud

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "segment_id" : (required, string) identifier for the segment to be exported,
  "callback_endpoint" : (optional, string) endpoint to post a download URL when the export is available,
  "fields_to_export" : (required, array of string) name of user data fields to export, you may also export custom attributes. New accounts must specify specific fields to export,
  "output_format" : (optional, string) when using your own S3 bucket,  specifies file format as 'zip' or 'gzip'. Defaults to ZIP file format
}
```

## Parámetros de la solicitud

| Parámetro                     | Obligatoria  | Tipo de datos        | Descripción                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------- | --------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `segment_id`                  | Obligatoria  | Cadena           | Identificador del segmento que se va a exportar. Ver [identificador de segmento]({{site.baseurl}}/api/identifier_types/).<br><br>Puedes encontrar la dirección `segment_id` para un segmento determinado en la página [Claves de API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) de tu cuenta Braze o puedes utilizar el [punto final de la lista de segmentos]({{site.baseurl}}/api/endpoints/export/segments/get_segment/). |
| `callback_endpoint`           | Opcional  | Cadena           | Punto final en el que publicar una URL de descarga cuando la exportación esté disponible.                                                                                                                                                                                                                                                                                                                                             |
| `fields_to_export`            | Requerido* | Matriz de cadenas | Nombre de los campos de datos de usuario a exportar. También puedes exportar todos los atributos personalizados incluyendo `custom_attributes` en este parámetro. <br><br>\*A partir de abril de 2021, en las cuentas nuevas, se deben especificar los campos concretos que se exportarán.                                                                                                                                                                                        |
| `custom_attributes_to_export` | Opcional  | Matriz de cadenas | Nombre del atributo personalizado específico que se va a exportar. Se pueden exportar hasta 500 atributos personalizados. Para crear y administrar atributos personalizados en el panel, ve a **Configuración de datos** > **Atributos** personalizados **.**                                                                                                                                                                                                          |
| `output_format`               | Opcional  | Cadena           | El formato de salida de tu archivo. Predetermina el formato de archivo `zip`. Si utilizas tu propio contenedor de S3, puedes especificar `zip` o `gzip`.                                                                                                                                                                                                                                                                         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Si se incluye `custom_attributes` en el parámetro `fields_to_export`, se exportan todos los atributos personalizados independientemente de lo que haya en `custom_attributes_to_export`. Si tu objetivo es exportar atributos específicos, `custom_attributes` no debe incluirse en el parámetro `fields_to_export`. En su lugar, utiliza el parámetro `custom_attributes_to_export`.
{% endalert %}

## Ejemplo de solicitud de exportación de todos los atributos personalizados
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/export/segment' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "segment_id" : "segment_identifier",
  "callback_endpoint" : "example_endpoint",
  "fields_to_export" : ["first_name", "email", "purchases", "custom_attributes"],
  "output_format" : "zip"
}'
```

## Ejemplo de solicitud de exportación de atributos personalizados específicos
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/export/segment' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "segment_id" : "segment_identifier",
  "callback_endpoint" : "example_endpoint",
  "fields_to_export" : ["first_name", "email", "purchases"],
  "custom_attributes_to_export" : ["allergies", "favorite_food"],
  "output_format" : "zip"
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
| `push_tokens`         | Matriz           | Información sobre los tokens de notificaciones push del usuario.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `random_bucket`       | Entero         | [Número de contenedor aleatorio]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events#random-bucket-number-event) del usuario, utilizado para crear segmentos uniformemente distribuidos de usuarios aleatorios.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `time_zone`           | Cadena          | Zona horaria del usuario en el mismo formato que la base de datos de zonas horarias de IANA.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `total_revenue`       | Flotante           | Total de ingresos atribuidos a este usuario. Los ingresos totales se calculan en función de las compras que el usuario realizó durante las ventanas de conversión de las campañas y Lienzos que recibió.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `uninstalled_at`      | Marca de tiempo       | Fecha y hora en que el usuario desinstala la aplicación. Se omite si no se ha desinstalado la aplicación.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `user_aliases`        | Objeto          | [Objeto alias de usuario]({{site.baseurl}}/api/objects_filters/user_alias_object#user-alias-object-specification) que contiene `alias_name` y `alias_label`, si existe.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Recordatorios importantes

- Los campos de `custom_events`, `purchases`, `campaigns_received`, y `canvases_received` sólo contendrán datos de los últimos 90 días.
- Tanto `custom_events` como `purchases` contienen campos para `first` y `count`. Ambos campos reflejarán información de todos los tiempos, y no se limitarán sólo a los datos de los últimos 90 días. Por ejemplo, si un usuario concreto realizó el evento por primera vez hace 90 días, esto se reflejará con exactitud en el campo `first`, y el campo `count` también tendrá en cuenta los eventos ocurridos antes de los últimos 90 días.
- El número de exportaciones de segmentos simultáneas que una empresa puede ejecutar en el nivel de punto final está limitado a 100. Los intentos que superen este límite provocarán un error.
- Si se intenta exportar un segmento por segunda vez mientras se está ejecutando el primer trabajo de exportación, se producirá un error 429.

## Respuesta

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "object_prefix": (required, string) the filename prefix that will be used for the JSON file produced by this export, for example, 'bb8e2a91-c4aa-478b-b3f2-a4ee91731ad1-1464728599',
    "url" : (optional, string) the URL where the segment export data can be downloaded if you do not have your own S3 credentials
}
```

Una vez que la URL esté disponible, solo será válida durante unas horas. Por ello, te recomendamos encarecidamente que añadas tus propias credenciales de S3 a Braze.

## Ejemplo de archivo de exportación de usuario

Objeto de exportación del usuario (incluiremos los menos datos posibles; si falta un campo en el objeto, debe considerarse nulo o vacío):

{% tabs %}
{% tab Todos los campos %}

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
{% tab Muestra de resultados %}

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

[1]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3
[2]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/microsoft_azure_blob_storage_for_currents/
[3]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/google_cloud_storage_for_currents/

{% endapi %}
