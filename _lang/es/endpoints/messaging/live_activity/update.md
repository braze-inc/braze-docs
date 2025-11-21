---
nav_title: "PUBLICAR: Actualiza la actividad en vivo"
article_title: "PUBLICAR: Actualizar la actividad en directo"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Actualizar actividad en vivo."

---
{% api %}
# Actualizar la actividad en directo
{% apimethod post %}
/messages/live_activity/update
{% endapimethod %}

> Utilice este punto final para actualizar y finalizar [las Actividades en Directo]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift) mostradas por su aplicación iOS. Este punto final requiere una configuración adicional.

Después de registrar una Live Activity, puede pasar una carga JSON para actualizar su servicio de Notificaciones Push de Apple (APNs). Para más información, consulte la documentación de Apple sobre la [actualización de Live Activity con cargas útiles de notificaciones push](https://developer.apple.com/documentation/activitykit/updating-and-ending-your-live-activity-with-activitykit-push-notifications).

Si `content-available` no está configurado, la prioridad predeterminada del servicio de notificaciones push de Apple (APN) es 10. Si `content-available` está configurado, esta prioridad es 5. Consulta el [objeto push de Apple]({{site.baseurl}}/api/objects_filters/messaging/apple_object) para más detalles. 

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#2300226e-f26a-4154-9bcc-5883f1f294cd {% endapiref %}

## Requisitos previos

Para utilizar este punto final, tendrás que completar lo siguiente:

- Generar una clave API con el permiso `messages.live_activity.update`.
- Registra una actividad en vivo [de forma remota]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?tab=remote&sdktab=swift) o [local]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?tab=local&sdktab=swift) utilizando el SDK Swift de Braze.

{% multi_lang_include api/payload_size_alert.md %}

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Cuerpo de la solicitud

```json
{
   "app_id": "(required, string) App API identifier retrieved from the Developer Console.",
   "activity_id": "(required, string) When you register your Live Activity using launchActivity, you use the pushTokenTag parameter to name the Activity’s push token to a custom string. Set activity_id to this custom string to define which Live Activity you want to update.",
   "content_state": "(required, object) You define the ContentState parameters when you create your Live Activity. Pass the updated values for your ContentState using this object. The format of this request must match the shape you initially defined.",
   "end_activity": "(optional, boolean) If true, this request ends the Live Activity.",
   "dismissal_date": "(optional, datetime in ISO-8601 format) The time to remove the Live Activity from the user’s UI. If this time is in the past, the Live Activity will be removed immediately.",
   "stale_date": "(optional, datetime in ISO-8601 format) The time the Live Activity content is marked as outdated in the user’s UI.",
   "notification": "(optional, object ) Include an `apple_push` object to define a push notification that creates an alert for the user."
 }
 ```

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `app_id` | Obligatoria | Cadena | [Identificador de la API de]({{site.baseurl}}/api/identifier_types/#the-app-identifier) la aplicación recuperado de la página [Claves de API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/).  |
| `activity_id` | Obligatoria | Cadena | Cuando registras tu actividad en vivo utilizando [`launchActivity`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class), se utiliza el parámetro `pushTokenTag` para asignar una cadena personalizada al token de notificaciones push de la actividad.<br><br>Establezca `activity_id` en esta cadena personalizada para definir qué Actividad en vivo desea actualizar. |
| `content_state` | Obligatoria | Objeto | Los parámetros de `ContentState` se definen al crear la Live Activity. Pase los valores actualizados para su `ContentState` utilizando este objeto.<br><br>El formato de esta solicitud debe coincidir con la forma que definió inicialmente. |
| `end_activity` | Opcional | Booleano | Si `true`, esta solicitud finaliza la Actividad en vivo. |
| `dismissal_date` | Opcional | Fecha y hora <br>(cadena [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Este parámetro define el tiempo para eliminar la Actividad en Directo de la interfaz de usuario. Si este tiempo ya ha pasado y `end_activity` es `true`, la Actividad en Directo será eliminada inmediatamente.<br><br> Si `end_activity` es `false` o se omite, este parámetro solo actualiza la Actividad en vivo.|
| `stale_date` | Opcional | Fecha y hora <br>(cadena [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Este parámetro indica al sistema cuándo el contenido de la Actividad en Directo se marca como obsoleto en la interfaz de usuario. |
| `notification` | Opcional | Objeto | Incluya un objeto [`apple_push`]({{site.baseurl}}/api/objects_filters/messaging/apple_object/) para definir una notificación push. El comportamiento de esta notificación push depende de si el usuario está activo o si está utilizando un dispositivo proxy. {::nomarkdown}<ul><li>Si se incluye una <code>notificación</code> y el usuario está activo en su iPhone cuando se entrega la actualización, la IU de Actividad en vivo actualizada se deslizará hacia abajo y se mostrará como una notificación push.</li><li>Si se incluye una <code>notificación</code> y el usuario no está activo en su iPhone, su pantalla se iluminará para mostrar la IU de Actividad en vivo actualizada en su pantalla de bloqueo.</li><li>La <code>alerta de notificación</code> no se mostrará como una notificación push estándar. Además, si un usuario tiene un dispositivo proxy, como un Apple Watch, la <code>alerta</code> se mostrará allí.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud

```json
curl --location --request POST 'https://rest.iad-01.braze.com/messages/live_activity/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {YOUR-REST-API-KEY}' \
--data-raw '{
    "app_id": "{YOUR-APP-API-IDENTIFIER}",
    "activity_id": "live-activity-1",
    "content_state": {
        "teamOneScore": 2,
        "teamTwoScore": 4
    },
    "end_activity": false,
    "dismissal_date": "2023-02-28T00:00:00+0000",
    "stale_date": "2023-02-27T16:55:49+0000",
    "notification": {
        "alert": {
            "body": "It's halftime! Let's look at the scores",
            "title": "Halftime"
        }
    }
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
