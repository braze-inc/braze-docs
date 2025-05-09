---
nav_title: "Objeto Apple"
article_title: Objeto de mensajería de Apple
page_order: 1
page_type: reference
channel: push
platform: iOS
description: "Este artículo de referencia enumera y explica los diferentes objetos Apple utilizados en Braze."

---

# Objeto push de Apple

> El objeto `apple_push` le permite definir o solicitar información relacionada con el contenido de Apple Push y Apple Push Alert a través de nuestros [puntos finales de mensajería]({{site.baseurl}}/api/endpoints/messaging).

## Objeto push de Apple

```json
{
   "badge": (optional, int) the badge count after this message,
   "alert": (required unless content-available is true, string or Apple Push Alert Object) the notification message,
   // Specifying "default" in the sound field will play the standard notification sound
   "sound": (optional, string) the location of a custom notification sound within the app,
   "extra": (optional, object) additional keys and values to be sent,
   "content-available": (optional, boolean) if set, Braze will add the "content-available" flag to the push payload,
   "interruption_level": (optional, string: "passive", "active", "time-sensitive", or "critical") specifies the interruption level passed (iOS 15+),
   "relevance_score": (optional, float) specifies the relevance score between 0.0 and 1.0 used for grouping notification summaries (iOS 15+),
   "expiry": (optional, ISO 8601 date string) if set, push messages will expire at the specified datetime,
   "custom_uri": (optional, string) a web URL, or Deep Link URI,
   "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to true,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be an iOS Push Message),
   "notification_group_thread_id": (optional, string) the notification group thread ID the notification will be sent with,
   "asset_url": (optional, string) content URL for rich notifications for devices using iOS 10 or higher,
   "asset_file_type": (required if asset_url is present, string) file type of the asset - one of "aif", "gif", "jpg", "m4a", "mp3", "mp4", "png", or "wav",
   "collapse_id": (optional, string) To update a notification on the user's device after you've issued it, send another notification with the same collapse ID you used previously
   "mutable_content": (optional, boolean) if true, Braze will add the mutable-content flag to the payload and set it to 1. The mutable-content flag is automatically set to 1 when sending a rich notification, regardless of the value of this parameter.
   "send_to_most_recent_device_only": (optional, boolean) defaults to false, if set to true, Braze will only send this push to a user's most recently used iOS device, rather than all eligible iOS devices,
   "category": (optional, string) the iOS notification category identifier for displaying push action buttons,
   "buttons" : (optional, array of Apple push action button objects) push action buttons to display
}
```

Debe incluir un objeto push de Apple en `messages` si desea que los usuarios a los que se ha dirigido reciban un push en sus dispositivos iOS. El número total de bytes de la cadena `alert`, el objeto `extra` y otros parámetros opcionales no debe exceder de 1912. La API de mensajería devolverá un error si supera el tamaño de mensaje permitido por Apple. Los mensajes que incluyan las claves `ab` o `aps` en el objeto `extra` serán rechazados.

{% alert note %}
Si envía el objeto Apple Push como parte de una carga útil de actividades en directo, asegúrese de incluir la cadena `sound` en el objeto `alert`.
{% endalert %}

### Objeto de alerta push de Apple

En la mayoría de los casos, `alert` puede especificarse como una cadena en un objeto `apple_push`.

```json
{
   "body": (required unless content-available is true in the Apple Push Object, string) the text of the alert message,
   "title": (optional, string) a short string describing the purpose of the notification, displayed as part of the Apple Watch notification interface,
   "title_loc_key": (optional, string) the key to a title string in the `Localizable.strings` file for the current localization,
   "title_loc_args": (optional, array of strings) variable string values to appear in place of the format specifiers in title_loc_key,
   "action_loc_key": (optional, string) if a string is specified, the system displays an alert that includes the Close and View buttons, the string is used as a key to get a localized string in the current localization to use for the right button's title instead of "View",
   "loc_key": (optional, string) a key to an alert-message string in a Localizable.strings file for the current localization,
   "loc_args": (optional, array of strings) variable string values to appear in place of the format specifiers in loc_key,
   "sound": (optional, string) the location of a custom notification sound within the app (live activities only),
}
```

#### Ejemplo

```json
{
  "broadcast": false,
  "external_user_ids": ["PushTest12"],
  "campaign_id": "9c2fefcd-9115-3932-f771-c7f43d18d6b6",
  "override_frequency_capping": "false",
  "recipient_subscription_state": "all",
  "messages": {
    "apple_push": {
      "alert": {
        "title": "Hello!",
        "body": "Message here"
      },
      "message_variation_id": "iosPush-640"
    }
  }
}
```

## Objeto de botón de acción para notificación push de Apple

Debe incluir el campo `category` en el objeto push de Apple para utilizar los botones de acción push de iOS. Si incluye el campo `category`, se mostrarán todos los botones de acción de pulsación asociados; sólo incluya el campo `buttons` si desea definir adicionalmente las acciones de pulsación individuales de los botones. El SDK de Braze proporciona un conjunto de botones de acción para notificación push predeterminados que se muestran en la tabla siguiente. También puede utilizar sus propios botones si se han registrado en su aplicación.

### Objeto de botón de acción de Apple para los botones predeterminados de Braze

| Identificador de categoría   | Texto del botón | Identificador de la acción del botón | Acciones permitidas         |
|-----------------------|-------------|--------------------------|-------------------------|
| `ab_cat_accept_decline` | Aceptar      | `ab_pb_accept`             | OPEN_APP, URI o DEEP_LINK |
| `ab_cat_accept_decline` | Rechazar     | `ab_pb_decline`            | CERRAR                   |
| `ab_cat_yes_no`         | Sí         | `ab_pb_yes`                | OPEN_APP, URI o DEEP_LINK |
| `ab_cat_yes_no`         | No          | `ab_pb_no`                 | CERRAR                   |
| `ab_cat_confirm_cancel` | Confirmar     | `ab_pb_confirm`            | OPEN_APP, URI o DEEP_LINK |
| `ab_cat_confirm_cancel` | Cancelar      | `ab_pb_cancel`             | CERRAR                   |
| `ab_cat_more`           | Más        | `ab_pb_more`               | OPEN_APP, URI o DEEP_LINK |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

```json
{
  "action_id": (required, string) the button's action identifier,
  "action": (optional, string) one of "OPEN_APP", "URI", "DEEP_LINK", or "CLOSE". Defaults to either "OPEN_APP" or "CLOSE" depending on the button,
  "uri": (optional, string) a web URL or Deep Link URI,
  "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to true
}
```

### Objeto botón de acción de Apple para las categorías definidas por su aplicación

```json
{
  "action_id": (required, string) the button's action identifier,
  "action": (required, string) one of "URI" or "DEEP_LINK",
  "uri": (required, string) a web URL or Deep Link URI,
  "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to true
}
```
