---
nav_title: "PUBLICAR: Iniciar actividad en vivo"
article_title: "PUBLICAR: Iniciar actividad en vivo"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Iniciar actividad en vivo."

---
{% api %}
# Iniciar actividad en vivo
{% apimethod post %}
/messages/live_activity/start
{% endapimethod %}

> Utiliza este endpoint para iniciar remotamente [Actividades en vivo]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift) mostradas en tu aplicación iOS. Este punto final requiere una configuración adicional.

Después de crear una Actividad en vivo, puedes hacer una petición POST para iniciar remotamente tu actividad para cualquier segmento dado. Para más información sobre las Actividades en vivo de Apple, consulta [Iniciar y actualizar Actividades en vivo con notificaciones push de ActivityKit](https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications).

Si `content-available` no está configurado, la prioridad predeterminada del servicio de notificaciones push de Apple (APN) es 10. Si `content-available` está configurado, esta prioridad es 5. Consulta el [objeto push de Apple]({{site.baseurl}}/api/objects_filters/messaging/apple_object) para más detalles. 

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#2300226e-f26a-4154-9bcc-5883f1f294cd {% endapiref %}

## Requisitos previos

Para utilizar este punto final, tendrás que completar lo siguiente:

- Genera una clave de API con el permiso `messages.live_activity.start`.
- [Crear una actividad en vivo]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?tab=local&sdktab=swift#swift_create-an-activity) utilizando el SDK Swift de Braze.

{% multi_lang_include api/payload_size_alert.md %}

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Cuerpo de la solicitud

```json
{
  "app_id": "(required, string) App API identifier retrieved from the Developer Console.",
  "activity_id": "(required, string) Define a custom string as your `activity_id`. You will use this ID when you wish to send update or end events to your Live Activity.",
  "activity_attributes_type": "(required, string) The activity attributes type you define within `liveActivities.registerPushToStart` in your app",
  "activity_attributes": "(required, object) The static attribute values for the activity type (such as the sports team names, which don't change)",
  "content_state": "(required, object) You define the ContentState parameters when you create your Live Activity. Pass the updated values for your ContentState using this object. The format of this request must match the shape you initially defined.",
  "dismissal_date": "(optional, datetime in ISO-8601 format) The time to remove the Live Activity from the user’s UI. If this time is in the past, the Live Activity will be removed immediately.",
  "stale_date": "(optional, datetime in ISO-8601 format) The time the Live Activity content is marked as outdated in the user’s UI.",
  "notification": "(required, object) Include an `apple_push` object to define a push notification that creates an alert for the user, displayed on paired watchOS devices. Should include `notification.alert.title` and `notification.alert.body`",
  // One of the following:
  "external_user_ids": "(optional, array of strings) see external user identifier, maximum 50",
  "custom_audience": "(optional, connected audience object) see connected audience",
  "segment_id": "(optional, string) see segment identifier"
}
```

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos| Descripción  |
|-----------|----------|----------|--------------|
| `app_id` | Obligatoria | Cadena | [Identificador de la API de]({{site.baseurl}}/api/identifier_types/#the-app-identifier) la aplicación recuperado de la página [Claves de API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/).  |
| `activity_id` | Obligatoria | Cadena  | Define una cadena personalizada como tu `activity_id`. Utilizarás este ID cuando desees enviar eventos de actualización o finalización a tu Actividad en vivo.  |
| `activity_attributes_type`  | Obligatoria | Cadena | El tipo de atributos de actividad que defines en `liveActivities.registerPushToStart` en tu aplicación.  |
| `activity_attributes` | Obligatoria | Objeto  | Los valores estáticos de los atributos de la clase de actividad (como los nombres de los equipos deportivos, que no cambian). |
| `content_state` | Obligatoria | Objeto  | Los parámetros de `ContentState` se definen al crear la Live Activity. Pase los valores actualizados para su `ContentState` utilizando este objeto.<br><br>El formato de esta solicitud debe coincidir con la forma que definió inicialmente. |
| `dismissal_date` | Opcional | Fecha y hora <br>(cadena [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Este parámetro define el tiempo para eliminar la Actividad en vivo de la IU del usuario. |
| `stale_date` | Opcional | Fecha y hora <br>(cadena [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Este parámetro indica al sistema cuándo el contenido de la Actividad en Directo se marca como obsoleto en la interfaz de usuario. |
| `notification` | Obligatoria | Objeto | Incluya un objeto [`apple_push`]({{site.baseurl}}/api/objects_filters/messaging/apple_object/) para definir una notificación push. El comportamiento de esta notificación push depende de si el usuario está activo o si está utilizando un dispositivo proxy. {::nomarkdown}<ul><li>Si se incluye una <code>notificación</code> y el usuario está activo en su iPhone cuando se entrega la actualización, la IU de Actividad en vivo actualizada se deslizará hacia abajo y se mostrará como una notificación push.</li><li>Si se incluye una <code>notificación</code> y el usuario no está activo en su iPhone, su pantalla se iluminará para mostrar la IU de Actividad en vivo actualizada en su pantalla de bloqueo.</li><li>La <code>alerta de notificación</code> no se mostrará como una notificación push estándar. Además, si un usuario tiene un dispositivo proxy, como un Apple Watch, la <code>alerta</code> se mostrará allí.</li></ul>{:/} |
| `external_user_ids` | Opcional si se proporciona `segment_id` o `audience`  | Matriz de cadenas | Ver [ID de usuario externo]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields). Máximo 50 ID externos de usuario.  |
| `segment_id `  | Opcional si se proporciona `external_user_ids` o `audience`  | Cadena    | Ver [identificador de segmento]({{site.baseurl}}/api/identifier_types/). |
| `custom_audience` | Opcional si se proporciona `external_user_ids` o `segment_id`  | Objeto de audiencia conectado  | Ver [audiencia conectada]({{site.baseurl}}/api/objects_filters/connected_audience/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud

```json
curl --location --request POST 'https://rest.iad-01.braze.com/messages/live_activity/start' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {YOUR-REST-API-KEY}' \
--data-raw '{
    "app_id": "{YOUR-APP-API-IDENTIFIER}",
    "activity_id": "football-chiefs-bills-2024-01-21",
    "content_state": {
        "teamOneScore": 0,
        "teamTwoScore": 0
    },
    "activity_attributes_type": "FootballActivity",
    "activity_attributes": {
        "team1Name": "Chiefs",
        "team2Name": "Bills"
    },
    "dismissal_date": "2024-01-22T00:00:00+0000",
    "stale_date": "2024-01-22T16:55:49+0000",
    "notification": {
        "alert": {
            "body": "The game is starting! Tune in soon!",
            "title": "Chiefs v. Bills"
        }
    },
    // One of the following required:
    "segment_id": "{YOUR-SEGMENT-API-IDENTIFIER}", // Optional
    "custom_audience": {...}, // Optional
    "external_user_ids": ["user-id1", "user-id2"], // Optional
}'
```

## Respuesta

Hay dos respuestas de código de estado para este punto final: `201` y `4XX`.

### Ejemplo de respuesta positiva

Se devuelve un código de estado `201` si la solicitud se ha formateado correctamente y la hemos recibido. El código de estado `201` podría devolver el siguiente cuerpo de respuesta.

```json
{
  "message": "success"
}
```

### Ejemplo de respuesta de error

La clase de código de estado `4XX` indica un error del cliente. Consulte el [artículo Errores y respuestas de la API]({{site.baseurl}}/api/errors/) para obtener más información sobre los errores que puede encontrar.

El código de estado `400` podría devolver el siguiente cuerpo de respuesta. 

```json
{
    "error": "\nProblem:\n  message body does not match declared format\nResolution:\n  when specifying application/json as content-type, you must pass valid application/json in the request's 'body' "
}
```

{% endapi %}
