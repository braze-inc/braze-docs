---
nav_title: "POST: Live-Aktivität starten"
article_title: "POST: Live-Aktivität starten"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Dieser Artikel enthält Einzelheiten zum Endpunkt Live-Aktivität starten."

---
{% api %}
# Live-Aktivität starten
{% apimethod post %}
/messages/live_activity/start
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um [Live-Aktivitäten]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift), die in Ihrer iOS App angezeigt werden, aus der Ferne zu starten. Dieser Endpunkt erfordert eine zusätzliche Einrichtung.

Nachdem Sie eine Live-Aktivität erstellt haben, können Sie eine POST-Anfrage stellen, um Ihre Aktivität für ein bestimmtes Segment aus der Ferne zu starten. Weitere Informationen über die Live-Aktivitäten von Apple finden Sie unter [Starten und Aktualisieren von Live-Aktivitäten mit Push-Benachrichtigungen von ActivityKit](https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#2300226e-f26a-4154-9bcc-5883f1f294cd {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, müssen Sie Folgendes tun:

- Erzeugen Sie einen API-Schlüssel mit der Berechtigung `messages.live_activity.start`.
- [Erstellen Sie eine Live-Aktivität]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?tab=local&sdktab=swift#swift_create-an-activity) mit dem Braze Swift SDK.

{% multi_lang_include api/payload_size_alert.md %}

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Anfragetext

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
  "external_user_ids": "(optional, array of strings) see external user identifier",
  "custom_audience": "(optional, connected audience object) see connected audience",
  "segment_id": "(optional, string) see segment identifier"
}
```

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp| Beschreibung  |
|-----------|----------|----------|--------------|
| `app_id` | Erforderlich | String | [API-Bezeichner]({{site.baseurl}}/api/identifier_types/#the-app-identifier) der App, der von der Seite [API-Schlüssel]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) abgerufen wird.  |
| `activity_id` | Erforderlich | String  | Definieren Sie einen angepassten String als Ihren `activity_id`. Sie verwenden diese ID, wenn Sie Update- oder End-Ereignisse an Ihre Live-Aktivität senden möchten.  |
| `activity_attributes_type`  | Erforderlich | String | Die Art der Attribute, die Sie unter `liveActivities.registerPushToStart` in Ihrer App definieren.  |
| `activity_attributes` | Erforderlich | Objekt  | Die statischen Attributwerte für die Aktivitätsart (z.B. die Namen der Sportteams, die sich nicht ändern). |
| `content_state` | Erforderlich | Objekt  | Sie definieren die `ContentState` Parameter, wenn Sie Ihre Live-Aktivität erstellen. Übergeben Sie die aktualisierten Werte für Ihr `ContentState` mit diesem Objekt.<br><br>Das Format dieser Anfrage muss mit der Form übereinstimmen, die Sie ursprünglich definiert haben. |
| `dismissal_date` | Optional | Datetime <br>[(ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) String) | Dieser Parameter legt die Zeit fest, nach der die Live-Aktivität aus dem UI des Nutzers:innen entfernt wird. |
| `stale_date` | Optional | Datetime <br>[(ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) String) | Dieser Parameter teilt dem System mit, wenn der Inhalt der Live-Aktivität in der UI des Nutzers:in als veraltet markiert wird. |
| `notification` | Erforderlich | Objekt | Fügen Sie ein [`apple_push`]({{site.baseurl}}/api/objects_filters/messaging/apple_object/) Objekt ein, um eine Push-Benachrichtigung zu definieren. Das Verhalten dieser Push-Benachrichtigung hängt davon ab, ob der Nutzer:innen aktiv ist oder ob er ein Proxy-Gerät verwendet. {::nomarkdown}<ul><li>Wenn ein <code>notification</code> enthalten ist und der Nutzer:innen auf seinem iPhone aktiv ist, wenn das Update zugestellt wird, wird die aktualisierte Live Activity UI nach unten geschoben und wie eine Push-Benachrichtigung angezeigt.</li><li>Wenn ein <code>notification</code> enthalten ist und der Nutzer:innen auf seinem iPhone nicht aktiv ist, leuchtet sein Bildschirm auf und zeigt das aktualisierte Live Activity UI auf seinem Sperrbildschirm an.</li><li>Die <code>notification alert</code> wird nicht als normale Push-Benachrichtigung angezeigt. Wenn ein Nutzer:innen ein Proxy-Gerät, wie eine Apple Watch, besitzt, kann die <code>alert</code> wird dort angezeigt.</li></ul>{:/} |
| `external_user_ids` | Optional, wenn `segment_id` oder `audience` bereitgestellt wird. | String-Array | Siehe [externe Nutzer:in ID]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields).  |
| `segment_id `  | Optional, wenn `external_user_ids` oder `audience` bereitgestellt wird. | String    | Siehe [Bezeichner für Segmente]({{site.baseurl}}/api/identifier_types/). |
| `custom_audience` | Optional, wenn `external_user_ids` oder `segment_id` bereitgestellt wird. | Verbundenes Objekt der Zielgruppe  | Siehe [verbundene Zielgruppe]({{site.baseurl}}/api/objects_filters/connected_audience/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Beispiel Anfrage

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

## Antwort

Für diesen Endpunkt gibt es zwei Status Code Antworten: `201` und `4XX`.

### Beispiel für eine erfolgreiche Antwort

Ein `201` Status Code wird zurückgegeben, wenn die Anfrage korrekt formatiert wurde und wir die Anfrage erhalten haben. Der Status Code `201` könnte den folgenden Antwortkörper zurückgeben.

```json
{
  "message": "success"
}
```

### Beispiel einer Fehlerantwort

Die Klasse `4XX` des Status Codes zeigt einen Client-Fehler an. Weitere Informationen zu Fehlern, die auftreten können, finden Sie im [Artikel API-Fehler und Antworten]({{site.baseurl}}/api/errors/).

Der Status Code `400` könnte den folgenden Antwortkörper zurückgeben. 

```json
{
    "error": "\nProblem:\n  message body does not match declared format\nResolution:\n  when specifying application/json as content-type, you must pass valid application/json in the request's 'body' "
}
```

{% endapi %}
