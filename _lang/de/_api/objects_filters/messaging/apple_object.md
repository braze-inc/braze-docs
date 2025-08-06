---
nav_title: "Apfel Objekt"
article_title: Apple Messaging Objekt
page_order: 1
page_type: reference
channel: push
platform: iOS
description: "Dieser Artikel referenziert und erklärt die verschiedenen Apple Objekte, die bei Braze verwendet werden."

---

# Apple Push-Objekt

> Das Objekt `apple_push` ermöglicht es Ihnen, über unsere [Messaging Endpunkte]({{site.baseurl}}/api/endpoints/messaging) Informationen zu Apple Push und Apple Push Alert Inhalten zu definieren oder anzufragen.

## Apple Push-Objekt

```json
{
   "badge": (optional, integer) the badge count after this message,
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
   "buttons" : (optional, array of Apple push action button objects) push action buttons to display,
   "apns_priority": (optional, integer) override the default apns_priority value using an integer between 1 and 10; use 10 for immediate delivery, 5 for power-aware delivery, and 1 to minimize power impact and avoid waking the device,
}
```

Sie müssen ein Apple Push-Objekt in `messages` einbinden, wenn Sie möchten, dass Nutzer:innen auf ihren iOS Geräten einen Push erhalten. Die Gesamtzahl der Bytes in Ihrem `alert` String, `extra` Objekt und anderen optionalen Parametern sollte 1912 nicht überschreiten. Die Messaging API gibt einen Fehler zurück, wenn Sie die von Apple zulässige Größe der Nachrichten überschreiten. Nachrichten, die die Schlüssel `ab` oder `aps` im Objekt `extra` enthalten, werden abgelehnt.

{% alert note %}
Wenn Sie das Apple Push-Objekt als Teil einer Live-Aktivitäten-Nutzlast senden, stellen Sie sicher, dass Sie Ihren `sound` String in das `alert` Objekt aufnehmen.
{% endalert %}

### Apple Push-Benachrichtigungsobjekt

In den meisten Fällen kann `alert` als String in einem `apple_push` Objekt angegeben werden.

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

#### Beispiel

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

## Apple Push-Action-Button Objekt

Sie müssen das Feld `category` in das Apple Push-Objekt aufnehmen, um Push-Action-Buttons von iOS zu verwenden. Wenn Sie das Feld `category` einschließen, werden alle zugehörigen Push-Action-Buttons angezeigt. Schließen Sie das Feld `buttons` nur ein, wenn Sie zusätzlich die einzelnen Klick-Aktionen der Buttons definieren möchten. Das Braze SDK stellt Ihnen eine Reihe von Standard Push-Action-Buttons zur Verfügung, die Sie in der folgenden Tabelle finden. Sie können auch Ihre eigenen Buttons verwenden, wenn diese in Ihrer App registriert wurden.

### Apple Push-Action-Button Objekt für Braze Standard-Buttons

| Kategorie Bezeichner   | Button-Text | Button Aktions-Bezeichner | Erlaubte Aktionen         |
|-----------------------|-------------|--------------------------|-------------------------|
| `ab_cat_accept_decline` | Zustimmen      | `ab_pb_accept`             | OPEN_APP, URI, oder DEEP_LINK |
| `ab_cat_accept_decline` | Ablehnen     | `ab_pb_decline`            | SCHLIESSEN                   |
| `ab_cat_yes_no`         | Ja         | `ab_pb_yes`                | OPEN_APP, URI, oder DEEP_LINK |
| `ab_cat_yes_no`         | Kein:e          | `ab_pb_no`                 | SCHLIESSEN                   |
| `ab_cat_confirm_cancel` | Bestätigen     | `ab_pb_confirm`            | OPEN_APP, URI, oder DEEP_LINK |
| `ab_cat_confirm_cancel` | Abbrechen      | `ab_pb_cancel`             | SCHLIESSEN                   |
| `ab_cat_more`           | Mehr        | `ab_pb_more`               | OPEN_APP, URI, oder DEEP_LINK |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

```json
{
  "action_id": (required, string) the button's action identifier,
  "action": (optional, string) one of "OPEN_APP", "URI", "DEEP_LINK", or "CLOSE". Defaults to either "OPEN_APP" or "CLOSE" depending on the button,
  "uri": (optional, string) a web URL or Deep Link URI,
  "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to true
}
```

### Apple Push-Action-Button Objekt für von Ihrer App definierte Kategorien

```json
{
  "action_id": (required, string) the button's action identifier,
  "action": (required, string) one of "URI" or "DEEP_LINK",
  "uri": (required, string) a web URL or Deep Link URI,
  "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to true
}
```
