---
nav_title: "Android Objekte"
article_title: Android Messaging Objekt
page_order: 0
page_type: reference
channel: push
platform: Android
description: "Dieser referenzierte Artikel listet die verschiedenen Android-Objekte auf, die bei Braze verwendet werden, und erklärt sie."

---
# Android Objekt

> Mit dem Objekt `android_push` können Sie über unsere [Messaging Endpunkte]({{site.baseurl}}/api/endpoints/messaging) Informationen zu Android Push und Android Push Alert Inhalten definieren oder anfragen.

## Android-Push-Objekt

Sie müssen ein Android Push-Objekt in `messages` einbinden, wenn Sie möchten, dass Nutzer:innen auf ihren Android Geräten einen Push erhalten. Die Gesamtzahl der Bytes in Ihrem `alert` String und `extra` Objekt sollte 4.000 nicht überschreiten. Die Messaging API gibt einen Fehler zurück, wenn Sie die von Google zulässige Größe der Nachrichten überschreiten.

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

Sie können "Big Picture"-Benachrichtigungen senden, indem Sie den Schlüssel `appboy_image_url` im Objekt `extra` angeben. Der Wert für `appboy_image_url` sollte eine URL sein, die auf den Ort verweist, an dem Ihr Bild gehostet wird. Die Bilder müssen auf ein Seitenverhältnis von 2:1 zugeschnitten werden und sollten mindestens 600 x 300 px groß sein.

### Zusätzliche Parameterdetails

| Parameter | Details |
| --------- | ------- |
| `priority` | Dieser Parameter akzeptiert Werte von `-2` bis `2`, wobei `-2` für die Priorität "MIN" und `2` für "MAX" steht. `0` ist der "DEFAULT"-Wert. <br> <br> Alle Werte, die außerhalb dieses Bereichs gesendet werden, werden standardmäßig auf 0 gesetzt. Weitere Informationen darüber, welche Prioritätsstufe Sie verwenden sollten, finden Sie unter [Android Benachrichtigungspriorität]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings#notification-priority). |
| `android_priority` | Dieser Parameter akzeptiert entweder die Werte `normal` oder `high`, um die Priorität des FCM Senders anzugeben. Standardmäßig werden Nachrichten mit der auf der Seite [Push-Einstellungen]({{site.baseurl}}/user_guide/administrative/app_settings/push_settings/#default-fcm-priority-for-android-campaigns) konfigurierten Standard-FCM-Priorität gesendet.<br><br> Weitere Informationen darüber, wie sich unterschiedliche Werte auf die Zustellung auswirken, finden Sie unter [Android Nachrichtenpriorität](https://firebase.google.com/docs/cloud-messaging/android/message-priority). |
| `collapse_key` | FCM kann gleichzeitig nur bis zu vier Klappschlüssel pro Gerät speichern. Wenn Sie mehr als vier Collapse Keys verwenden, übernimmt FCM keine Garantie dafür, welche davon erhalten bleiben. Braze verwendet standardmäßig einen dieser Schlüssel für Kampagnen. Stellen Sie daher sicher, dass Sie nur bis zu drei zusätzliche Klappschlüssel für Android-Nachrichten angeben. |
| `push_icon_image_url` | Der Wert für den Parameter "Großes Symbol" sollte eine URL sein, die auf den Ort verweist, an dem Ihr Bild gehostet wird. <br> <br> Die Bilder müssen auf ein Seitenverhältnis von 1:1 beschnitten werden und sollten mindestens 40x40 groß sein. |
| `notification_channel` | Wenn dies nicht angegeben wird, versucht Braze, die Nutzdaten der Benachrichtigung mit der [Fallback-Kanal-ID des Dashboards]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/#dashboard-fallback-channel) zu senden. Weitere Informationen finden Sie unter [Benachrichtigungskanäle]({{site.baseurl}}/user_guide/message_building_by_channel/push/notification_channels/) und in den Schritten zur [Definition von Benachrichtigungskanälen]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-5-define-notification-channels) während der Integration. |
| `send_to_sync` | Weitere Informationen zu `send_to_sync` Nachrichten finden Sie unter [Stille Android-Benachrichtigungen]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications/#silent-push-notifications). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Android Push-Action-Button Objekt

```json
{
  "text": (required, string) the button's text,
  "action": (optional, string) one of "OPEN_APP", "URI", "DEEP_LINK", or "CLOSE", defaults to "OPEN_APP",
  "uri": (optional, string) a web URL or Deep Link URI,
  "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to true
}
```

## Android Konversations-Push-Objekt {#android-conversation-push-object}

{% sdk_min_versions android:15.0.0 %}

Die Konzepte in dieser Nachricht entsprechen denen in der [Android People und Conversations](https://developer.android.com/guide/topics/ui/conversations) Push Dokumentation.

```json
{
  "shortcut_id" : (required, string) the sharing shortcut identifier,
  "reply_person_id" : (required, string) the identifier of the Person this push is replying to,
  "messages" : (required, array of Android Conversation Push Message Object),
  "persons" : (required, array of Android Conversation Push Person Object)
}
```

### Android Konversation Push Nachricht Objekt

```json
{
  "text" : (required, string) the text of this message,
  "timestamp" : (required, integer) the unix timestamp of when this message was sent,
  "person_id" : (required, string) the Person identifier of this message's sender,
}
```

### Android Konversation Push Person Objekt

```json
{
  "id" : (required, string) the identifier of this Person,
  "name" : (required, string) the display name of this Person
}
```

