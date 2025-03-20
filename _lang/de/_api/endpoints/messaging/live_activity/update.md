---
nav_title: "POST: Live-Aktivität aktualisieren"
article_title: "POST: Live-Aktivität aktualisieren"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Dieser Artikel enthält Einzelheiten zum Endpunkt Live-Aktivität aktualisieren."

---
{% api %}
# Live-Aktivität aktualisieren
{% apimethod post %}
/messages/live_activity/update
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um die von Ihrer iOS-App angezeigten [Live-Aktivitäten]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/live_activities/) zu aktualisieren und zu beenden. Dieser Endpunkt erfordert eine zusätzliche Einrichtung.

Nachdem Sie eine Live-Aktivität registriert haben, können Sie eine JSON-Nutzlast übergeben, um Ihren Apple Push Notification Service (APNs) zu aktualisieren. Weitere Informationen finden Sie in der Apple-Dokumentation zum [Aktualisieren Ihrer Live-Aktivitäten mit Push-Benachrichtigungen](https://developer.apple.com/documentation/activitykit/updating-and-ending-your-live-activity-with-activitykit-push-notifications).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#2300226e-f26a-4154-9bcc-5883f1f294cd {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, müssen Sie Folgendes tun:

- Erzeugen Sie einen API-Schlüssel mit der Berechtigung `messages.live_activity.update`.
- Registrieren Sie eine Live-Aktivität [aus der Ferne]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/live_activities/?tab=remote#step-2-start-the-activity) oder [lokal]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/live_activities/?tab=local#step-2-start-the-activity) mit dem Braze Swift SDK.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='default' %}

## Körper der Anfrage

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

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
|---|---|---|---|
| `app_id` | Erforderlich | String | [App-API-Kennung]({{site.baseurl}}/api/identifier_types/#the-app-identifier), die von der Seite [API-Schlüssel]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) abgerufen wird.  |
| `activity_id` | Erforderlich | String | Wenn Sie Ihre Live-Aktivität mit [`launchActivity`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class)registrieren, verwenden Sie den Parameter `pushTokenTag`, um das Push-Token der Aktivität mit einer benutzerdefinierten Zeichenfolge zu benennen.<br><br>Setzen Sie `activity_id` auf diese benutzerdefinierte Zeichenfolge, um festzulegen, welche Live-Aktivität Sie aktualisieren möchten. |
| `content_state` | Erforderlich | Objekt | Sie definieren die `ContentState` Parameter, wenn Sie Ihre Live-Aktivität erstellen. Übergeben Sie die aktualisierten Werte für Ihr `ContentState` mit diesem Objekt.<br><br>Das Format dieser Anfrage muss der Form entsprechen, die Sie ursprünglich definiert haben. |
| `end_activity` | Optional | Boolesche | Wenn `true`, beendet diese Anfrage die Live-Aktivität. |
| `dismissal_date` | Optional | Datetime <br>[(ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) Zeichenfolge) | Dieser Parameter legt die Zeit fest, nach der die Live-Aktivität aus der Benutzeroberfläche entfernt wird. Wenn dieser Zeitpunkt in der Vergangenheit liegt und `end_activity` `true` ist, wird die Live-Aktivität sofort entfernt.<br><br> Wenn `end_activity` `false` ist oder weggelassen wird, aktualisiert dieser Parameter nur die Live-Aktivität.|
| `stale_date` | Optional | Datetime <br>[(ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) Zeichenfolge) | Dieser Parameter teilt dem System mit, wann der Inhalt der Live-Aktivität in der Benutzeroberfläche als veraltet markiert wird. |
| `notification` | Optional | Objekt | Fügen Sie ein [`apple_push`]({{site.baseurl}}/api/objects_filters/messaging/apple_object/) Objekt, um eine Push-Benachrichtigung zu definieren. Das Verhalten dieser Push-Benachrichtigung hängt davon ab, ob der Benutzer aktiv ist oder ob er ein Proxy-Gerät verwendet. {::nomarkdown}<ul><li>Wenn ein <code>notification</code> enthalten ist und der Benutzer zum Zeitpunkt der Aktualisierung auf seinem iPhone aktiv ist, wird die aktualisierte Live-Aktivitäts-Benutzeroberfläche nach unten geschoben und wie eine Push-Benachrichtigung angezeigt.</li><li>Wenn ein <code>notification</code> enthalten ist und der Benutzer auf seinem iPhone nicht aktiv ist, leuchtet sein Bildschirm auf und zeigt die aktualisierte Live Activity UI auf dem Sperrbildschirm an.</li><li>Die <code>notification alert</code> wird nicht als Standard-Push-Benachrichtigung angezeigt. Wenn ein Benutzer über ein Proxy-Gerät wie eine Apple Watch verfügt, kann die <code>alert</code> wird dort angezeigt.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Beispiel Anfrage

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

## Antwort

Es gibt zwei Statuscode-Antworten für diesen Endpunkt: `201` und `4XX`.

### Beispiel für eine erfolgreiche Antwort

Ein `201` Statuscode wird zurückgegeben, wenn die Anfrage korrekt formatiert wurde und wir die Anfrage erhalten haben. Der Statuscode `201` könnte den folgenden Antwortkörper zurückgeben.

```json
{
  "message": "success"
}
```

### Beispiel einer Fehlerantwort

Die Klasse `4XX` des Statuscodes weist auf einen Client-Fehler hin. Weitere Informationen zu Fehlern, die auftreten können, finden Sie im [Artikel API-Fehler und Antworten]({{site.baseurl}}/api/errors/).

Der Statuscode `400` könnte den folgenden Antwortkörper zurückgeben. 

```json
{
    "error": "\nProblem:\n  message body does not match declared format\nResolution:\n  when specifying application/json as content-type, you must pass valid application/json in the request's 'body' "
}
```

{% endapi %}
