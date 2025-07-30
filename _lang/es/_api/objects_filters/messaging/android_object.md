---
nav_title: "Objetos Android"
article_title: Objeto de mensajería de Android
page_order: 0
page_type: reference
channel: push
platform: Android
description: "Este artículo de referencia enumera y explica los diferentes objetos Android utilizados en Braze."

---
# Objeto Android

> El objeto `android_push` le permite definir o solicitar información relacionada con el contenido de Android Push y Android Push Alert a través de nuestros [puntos finales de mensajería]({{site.baseurl}}/api/endpoints/messaging).

## Objeto push de Android

Debes incluir un objeto push de Android en `messages` si quieres que los usuarios a los que te has dirigido reciban un push en sus dispositivos Android. El número total de bytes de tu cadena `alert` y del objeto `extra` no debe superar los 4.000. La API de mensajería devolverá un error si superas el tamaño de mensaje permitido por Google.

```json
{
   "alert": (required, string) the notification message,
   "title": (required, string) the title that appears in the notification drawer,
   "extra": (optional, object) additional keys and values to be sent in the push,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be an Android Push Message),
   "notification_channel_id": (optional, string) the channel ID the notification will be sent with,
   "priority": (optional, integer) the notification priority value,
   "android_priority": (optional, string) the FCM sender priority,
   "send_to_sync": (optional, if set to true we will throw an error if "alert" or "title" is set),
   "collapse_key": (optional, string) the collapse key for this message,
   // Specifying "default" in the sound field will play the standard notification sound
   "sound": (optional, string) the location of a custom notification sound within the app,
   "custom_uri": (optional, string) a web URL, or Deep Link URI,
   "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to false,
   "summary_text": (optional, string),
   "time_to_live": (optional, integer (maximum of 2,419,200 seconds)),
   "notification_id": (optional, integer),
   "push_icon_image_url": (optional, string) an image URL for the large icon,
   "accent_color": (optional, integer) accent color to be applied by the standard Style templates when presenting this notification, an RGB integer value,
   "send_to_most_recent_device_only": (optional, boolean) defaults to false, if set to true, Braze will only send this push to a user's most recently used Android device, rather than all eligible Android devices,
   "buttons" : (optional, array of Android push action button objects) push action buttons to display
   "conversation_data" : (optional, Android Conversation Push Object) the data to be displayed through Conversation Push
}
```

Puedes enviar notificaciones "Big Picture" especificando la clave `appboy_image_url` en el objeto `extra`. El valor de `appboy_image_url` debe ser una URL que enlace a donde esté alojada tu imagen. Las imágenes deben recortarse a una relación de aspecto de 2:1 y deben tener al menos 600 x 300 px.

### Detalles adicionales de los parámetros

| Parámetro | Detalles |
| --------- | ------- |
| `priority` | Este parámetro aceptará valores de `-2` a `2`, donde `-2` representa la prioridad "MIN" y `2` representa la prioridad "MAX". `0` es el valor "DEFAULT". <br> <br> Cualquier valor enviado fuera de ese rango será predeterminado a 0. Para más información sobre qué nivel de prioridad utilizar, consulta [Prioridad de notificación en Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings#notification-priority). |
| `android_priority` | Este parámetro aceptará los valores `normal` o `high` para especificar la prioridad del remitente FCM. Por defecto, los mensajes se envían con la prioridad predeterminada del FCM configurada en la página [Configuración push]({{site.baseurl}}/user_guide/administrative/app_settings/push_settings/#default-fcm-priority-for-android-campaigns).<br><br> Para más información sobre cómo afectan los distintos valores a la entrega, consulta [Prioridad de mensajes en Android](https://firebase.google.com/docs/cloud-messaging/android/message-priority). |
| `collapse_key` | FCM solo puede almacenar simultáneamente hasta cuatro claves de colapso por dispositivo. Si utilizas más de cuatro claves de colapso, FCM no garantiza cuáles se conservarán. Braze utiliza una de ellas de forma predeterminada para las campañas, así que asegúrate de especificar sólo hasta tres claves de colapso adicionales para los mensajes de Android. |
| `push_icon_image_url` | El valor del parámetro icono grande debe ser una URL que enlace a donde esté alojada tu imagen. <br> <br> Las imágenes deben recortarse a una relación de aspecto 1:1 y deben tener un tamaño mínimo de 40x40. |
| `notification_channel` | Si no se especifica, Braze intentará enviar la carga útil de la notificación con el ID del canal [alternativo del panel]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/#dashboard-fallback-channel). Para más información, consulta [Canales de notificación]({{site.baseurl}}/user_guide/message_building_by_channel/push/notification_channels/) y consulta los pasos para [definir canales de notificación]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-5-define-notification-channels) durante la integración. |
| `send_to_sync` | Para más información sobre los mensajes de `send_to_sync`, consulta las [notificaciones silenciosas de Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications/#silent-push-notifications). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Objeto botón de acción push de Android

```json
{
  "text": (required, string) the button's text,
  "action": (optional, string) one of "OPEN_APP", "URI", "DEEP_LINK", or "CLOSE", defaults to "OPEN_APP",
  "uri": (optional, string) a web URL or Deep Link URI,
  "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to true
}
```

## Conversación Android objeto push {#android-conversation-push-object}

{% sdk_min_versions android:15.0.0 %}

Los conceptos de este mensaje corresponden a los de la documentación sobre [Android People y Conversaciones](https://developer.android.com/guide/topics/ui/conversations) push.

```json
{
  "shortcut_id" : (required, string) the sharing shortcut identifier,
  "reply_person_id" : (required, string) the identifier of the Person this push is replying to,
  "messages" : (required, array of Android Conversation Push Message Object),
  "persons" : (required, array of Android Conversation Push Person Object)
}
```

### Objeto de mensaje push de conversación Android

```json
{
  "text" : (required, string) the text of this message,
  "timestamp" : (required, integer) the unix timestamp of when this message was sent,
  "person_id" : (required, string) the Person identifier of this message's sender,
}
```

### Objeto de persona push de conversación de Android

```json
{
  "id" : (required, string) the identifier of this Person,
  "name" : (required, string) the display name of this Person
}
```

