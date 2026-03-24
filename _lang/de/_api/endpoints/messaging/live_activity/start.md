---
nav_title: "POST: Live-Aktivität starten"
article_title: "POST: Live-Aktivität starten"
search_tag: Endpunkt
page_order: 1

layout: api_page
page_type: reference
description: "Dieser Artikel enthält Einzelheiten zum Endpunkt „Live-Aktivität starten"."

---
{% api %}
# Live-Aktivität starten
{% apimethod post %}
/messages/live_activity/start
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um [Live-Aktivitäten]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift), die in Ihrer iOS-App angezeigt werden, aus der Ferne zu starten. Dieser Endpunkt erfordert eine zusätzliche Einrichtung.

Nachdem Sie eine Live-Aktivität erstellt haben, können Sie eine POST-Anfrage senden, um Ihre Aktivität für ein bestimmtes Segment aus der Ferne zu starten. Weitere Informationen über die Live-Aktivitäten von Apple finden Sie unter [Starten und Aktualisieren von Live-Aktivitäten mit Push-Benachrichtigungen von ActivityKit](https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications).

Wenn `content-available` nicht festgelegt ist, beträgt die Standardpriorität des Apple-Push-Benachrichtigungs-Dienstes (APN) 10. Wenn `content-available` gesetzt ist, beträgt diese Priorität 5. Weitere Details finden Sie unter [Apple-Push-Objekt]({{site.baseurl}}/api/objects_filters/messaging/apple_object).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#2300226e-f26a-4154-9bcc-5883f1f294cd {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, müssen Sie Folgendes tun:

- Generieren Sie einen API-Schlüssel mit der Berechtigung `messages.live_activity.start`.
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
  "external_user_ids": "(optional, array of strings) see external user identifier, maximum 50",
  "custom_audience": "(optional, connected audience object) see connected audience",
  "segment_id": "(optional, string) see segment identifier"
}
```

## Anfrageparameter

| Parameter | Erforderlich | Datentyp | Beschreibung |
|-----------|----------|----------|--------------|
| `app_id` | Erforderlich | String | [API-Bezeichner]({{site.baseurl}}/api/identifier_types/#the-app-identifier) der App, abgerufen von der Seite [API-Schlüssel]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/). |
| `activity_id` | Erforderlich | String | Definieren Sie einen angepassten String als Ihre `activity_id`. Sie verwenden diese ID, wenn Sie Update- oder End-Ereignisse an Ihre Live-Aktivität senden möchten. |
| `activity_attributes_type` | Erforderlich | String | Der Aktivitätsattribut-Typ, den Sie unter `liveActivities.registerPushToStart` in Ihrer App definieren. |
| `activity_attributes` | Erforderlich | Objekt | Die statischen Attributwerte für den Aktivitätstyp (z. B. die Namen der Sportteams, die sich nicht ändern). |
| `content_state` | Erforderlich | Objekt | Sie definieren die `ContentState`-Parameter, wenn Sie Ihre Live-Aktivität erstellen. Übergeben Sie die aktualisierten Werte für Ihren `ContentState` mit diesem Objekt.<br><br>Das Format dieser Anfrage muss mit der Struktur übereinstimmen, die Sie ursprünglich definiert haben. |
| `dismissal_date` | Optional | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)-String) | Dieser Parameter legt den Zeitpunkt fest, zu dem die Live-Aktivität aus der UI der Nutzer:innen entfernt wird.<br><br>Dieses Entfernungsdatum wird nach dem Empfang einer `/messages/live_activity/update`-Anfrage mit `end_activity` als `true` berücksichtigt. |
| `stale_date` | Optional | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)-String) | Dieser Parameter teilt dem System mit, wann der Inhalt der Live-Aktivität in der UI der Nutzer:innen als veraltet markiert wird. |
| `notification` | Erforderlich | Objekt | Fügen Sie ein [`apple_push`]({{site.baseurl}}/api/objects_filters/messaging/apple_object/)-Objekt ein, um eine Push-Benachrichtigung zu definieren. Das Verhalten dieser Push-Benachrichtigung hängt davon ab, ob die Nutzer:innen aktiv sind oder ein Proxy-Gerät verwenden. {::nomarkdown}<ul><li>Wenn eine <code>notification</code> enthalten ist und die Nutzer:innen auf ihrem iPhone aktiv sind, wenn das Update zugestellt wird, wird die aktualisierte Live-Aktivitäts-UI nach unten geschoben und wie eine Push-Benachrichtigung angezeigt.</li><li>Wenn eine <code>notification</code> enthalten ist und die Nutzer:innen auf ihrem iPhone nicht aktiv sind, leuchtet der Bildschirm auf und zeigt die aktualisierte Live-Aktivitäts-UI auf dem Sperrbildschirm an.</li><li>Der <code>notification alert</code> wird nicht als normale Push-Benachrichtigung angezeigt. Wenn Nutzer:innen ein Proxy-Gerät wie eine Apple Watch besitzen, wird der <code>alert</code> dort angezeigt.</li></ul>{:/} |
| `external_user_ids` | Optional, wenn `segment_id` oder `audience` bereitgestellt wird | String-Array | Siehe [externe Nutzer-ID]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields). Maximal 50 externe Nutzer-IDs. |
| `segment_id ` | Optional, wenn `external_user_ids` oder `audience` bereitgestellt wird | String | Siehe [Segment-Bezeichner]({{site.baseurl}}/api/identifier_types/). |
| `custom_audience` | Optional, wenn `external_user_ids` oder `segment_id` bereitgestellt wird | Verbundenes Zielgruppen-Objekt | Siehe [verbundene Zielgruppe]({{site.baseurl}}/api/objects_filters/connected_audience/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Beispielanfrage

```bash
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

Für diesen Endpunkt gibt es zwei Statuscode-Antworten: `201` und `4XX`.

### Beispiel für eine erfolgreiche Antwort

Ein Statuscode `201` wird zurückgegeben, wenn die Anfrage korrekt formatiert war und wir sie erhalten haben. Der Statuscode `201` könnte den folgenden Antworttext zurückgeben.

```json
{
  "message": "success"
}
```

### Beispiel für eine Fehlerantwort

Die Statuscode-Klasse `4XX` weist auf einen Client-Fehler hin. Weitere Informationen zu möglichen Fehlern finden Sie im Artikel [API-Fehler und -Antworten]({{site.baseurl}}/api/errors/).

Der Statuscode `400` könnte den folgenden Antworttext zurückgeben.

```json
{
    "error": "\nProblem:\n  message body does not match declared format\nResolution:\n  when specifying application/json as content-type, you must pass valid application/json in the request's 'body' "
}
```

{% endapi %}