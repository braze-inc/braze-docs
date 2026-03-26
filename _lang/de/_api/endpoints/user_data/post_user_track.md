---
nav_title: "POST: Nutzer:innen erstellen und aktualisieren"
article_title: "POST: Nutzer:innen erstellen und aktualisieren"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts „Nutzer:innen tracken"."
toc_headers: h2
---
{% api %}
# Nutzer:innen erstellen und aktualisieren
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/track
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um angepasste Events und Käufe aufzuzeichnen und die Attribute des Nutzerprofils zu aktualisieren.

{% alert note %}
Braze verarbeitet die über die API übergebenen Daten zum Nennwert. Kund:innen sollten nur Deltas (sich ändernde Daten) übergeben, um die unnötige Protokollierung von Datenpunkten zu minimieren. Weitere Informationen finden Sie unter [Datenpunkte]({{site.baseurl}}/user_guide/data/data_points/).
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4cf57ea9-9b37-4e99-a02e-4373c9a4ee59 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit der Berechtigung `users.track`.

Kund:innen, die die API für Server-zu-Server-Aufrufe verwenden, müssen möglicherweise `rest.iad-01.braze.com` auf die Zulassungsliste setzen, wenn sie sich hinter einer Firewall befinden.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='users track' %}

## Anfragetext

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, array of attributes object),
  "events": (optional, array of event object),
  "purchases": (optional, array of purchase object),
}
```

### Anfrageparameter

{% alert important %}
Für jede in der folgenden Tabelle aufgeführte Anfragekomponente müssen Sie eines der folgenden Felder angeben: `external_id`, `user_alias`, `braze_id`, `email` oder `phone`.
{% endalert %}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `attributes` | Optional | Array von Attribut-Objekten | Siehe [Nutzer:innen-Attribut-Objekt]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Optional | Array von Event-Objekten | Siehe [Event-Objekt]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Optional | Array von Kauf-Objekten | Siehe [Kauf-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Bezeichner-Auflösung

Jedes Anfrageobjekt muss mindestens einen Bezeichner enthalten. Die folgende Tabelle beschreibt, wie Braze bestimmt, welcher Bezeichner für die Suche nach dem Nutzerprofil verwendet wird.

| Bezeichnertyp | Bezeichner | Verhalten |
| --------------- | ----------- | -------- |
| Primär | `external_id`, `user_alias`, `braze_id` | Wird für die Suche nach dem Nutzerprofil verwendet. Pro Anfrageobjekt ist nur ein primärer Bezeichner zulässig – die Angabe von mehr als einem führt dazu, dass das Objekt abgelehnt wird. |
| Sekundär | `email`, `phone` | Wird für die Suche nach dem Nutzerprofil **nur** verwendet, wenn kein primärer Bezeichner vorhanden ist. Wenn sowohl `email` als auch `phone` ohne primären Bezeichner angegeben werden, hat `email` Vorrang. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Wenn ein primärer Bezeichner vorhanden ist, werden alle `email`- oder `phone`-Werte im selben Anfrageobjekt als Profilattribute behandelt – nicht als Bezeichner für die Nutzersuche. Wenn eine Anfrage beispielsweise sowohl eine `external_id` als auch eine `email` enthält:

- Braze sucht das Nutzerprofil anhand der `external_id`.
- Der `email`-Wert wird als Attribut im aufgelösten Profil gesetzt (oder aktualisiert).

{% alert important %}
Die Angabe eines primären Bezeichners, der keinem bestehenden Profil entspricht, kann ein doppeltes Profil erzeugen – selbst wenn `email` oder `phone` in derselben Anfrage mit einem bestehenden Profil übereinstimmen. Weitere Informationen finden Sie unter [Wie vermeide ich die Erstellung doppelter Nutzerprofile?](#how-do-i-avoid-creating-duplicate-user-profiles).
{% endalert %}

## Beispiel-Anfragen

### Ein Nutzerprofil über die E-Mail-Adresse aktualisieren

Über den Endpunkt `/users/track` können Sie ein Nutzerprofil per E-Mail-Adresse aktualisieren.

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "email": "test@braze.com",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 26,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ],
    "events": [
        {
            "email": "test@braze.com",
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2022-12-06T19:20:45+01:00",
            "properties": {
                "release": {
                    "studio": "FilmStudio",
                    "year": "2022"
                },
                "cast": [
                    {
                        "name": "Actor1"
                    },
                    {
                        "name": "Actor2"
                    }
                ]
            }
        },
        {
            "user_alias": {
                "alias_name": "device123",
                "alias_label": "my_device_identifier"
            },
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2013-07-16T19:20:50+01:00"
        }
    ],
    "purchases": [
        {
            "email": "test@braze.com",
            "app_id": "your_app_identifier",
            "product_id": "product_name",
            "currency": "USD",
            "price": 12.12,
            "quantity": 6,
            "time": "2017-05-12T18:47:12Z",
            "properties": {
                "color": "red",
                "monogram": "ABC",
                "checkout_duration": 180,
                "size": "Large",
                "brand": "Backpack Locker"
            }
        }
    ]
}'
```

### Ein Nutzerprofil nach Telefonnummer aktualisieren

Über den Endpunkt `/users/track` können Sie ein Nutzerprofil nach Telefonnummer aktualisieren. Dieser Endpunkt funktioniert nur, wenn Sie eine gültige Telefonnummer angeben.

{% alert important %}
Wenn Sie eine Anfrage sowohl mit `email` als auch mit `phone` stellen, verwendet Braze die E-Mail als Bezeichner.
{% endalert %}

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "phone": "+15043277269",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ],
}'
```
### Abo-Gruppen festlegen

Dieses Beispiel zeigt, wie Sie eine:n Nutzer:in anlegen und die Abo-Gruppe im Nutzer:innen-Attribut-Objekt festlegen.

Das Aktualisieren des Abo-Status mit diesem Endpunkt aktualisiert die durch ihre `external_id` angegebene Person (z. B. User1) und aktualisiert den Abo-Status aller Nutzer:innen mit derselben E-Mail wie diese Person (User1).

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
  {
    "external_id": "user_identifier",
    "email": "example@email.com",
    "email_subscribe": "subscribed",
    "subscription_groups": [{
      "subscription_group_id": "subscription_group_identifier_1",
      "subscription_state": "unsubscribed"
      },
      {
        "subscription_group_id": "subscription_group_identifier_2",
        "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_3",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}'
```

{% alert note %}
Wenn Sie bei SMS-Abo-Gruppen den `subscription_state` einer Gruppe auf `subscribed` setzen, können Sie den optionalen Parameter `use_double_opt_in_logic` innerhalb dieses Abo-Gruppen-Objekts auf `true` setzen, um die Person in den [SMS-Double-Opt-in]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/)-Workflow aufzunehmen. Wenn dieser Parameter weggelassen oder auf `false` gesetzt wird, während `subscription_state` den Wert `subscribed` hat, wird die Person ohne den Double-Opt-in-Workflow abonniert. Dieser Parameter wird nicht angewendet, wenn `subscription_state` auf andere Werte wie `unsubscribed` gesetzt ist.
{% endalert %}

### Beispiel-Anfrage zur Erstellung einer/eines Nur-Alias-Nutzer:in

Sie können den Endpunkt `/users/track` verwenden, um eine:n Nur-Alias-Nutzer:in zu erstellen, indem Sie den Schlüssel `_update_existing_only` mit dem Wert `false` im Anfragetext angeben. Wenn Sie diesen Wert weglassen, erstellt Braze kein Nur-Alias-Nutzerprofil. Die Verwendung einer/eines Nur-Alias-Nutzer:in stellt sicher, dass genau ein Profil mit diesem Alias existiert. Dies ist besonders hilfreich beim Aufbau einer Integration, da Braze so keine doppelten Nutzerprofile erstellt.

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
    "attributes": [
        {
            "_update_existing_only": false,
            "user_alias": {
                "alias_name": "example_name",
                "alias_label": "example_label"
            },
            "email": "email@example.com"
        }
    ],
}'
```


## Antworten

Bei Verwendung einer der oben genannten API-Anfragen sollten Sie eine der folgenden drei allgemeinen Antworten erhalten: eine [erfolgreiche Nachricht](#successful-message), eine [erfolgreiche Nachricht mit nicht schwerwiegenden Fehlern](#successful-message-with-non-fatal-errors) oder eine [Nachricht mit schwerwiegenden Fehlern](#message-with-fatal-errors).

### Erfolgreiche Nachricht

Erfolgreiche Nachrichten werden mit der folgenden Antwort zurückgegeben:

```json
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this returns an integer of the number of external_ids with attributes that Braze queued for processing,
  "events_processed": (optional, integer), if events are included in the request, this returns an integer of the number of events that Braze queued for processing,
  "purchases_processed": (optional, integer), if purchases are included in the request, this returns an integer of the number of purchases that Braze queued for processing,
}
```

### Erfolgreiche Nachricht mit nicht schwerwiegenden Fehlern

Wenn Ihre Nachricht erfolgreich ist, aber nicht schwerwiegende Fehler aufweist – z. B. ein ungültiges Event-Objekt in einer langen Liste von Events –, erhalten Sie die folgende Antwort:

```json
{
  "message": "success",
  "errors": [
    {
      <minor error message>
    }
  ]
}
```

Bei Erfolgsmeldungen verarbeitet Braze weiterhin alle Daten, die nicht von einem Fehler im Array `errors` betroffen sind.

### Nachricht mit schwerwiegenden Fehlern

Wenn Ihre Nachricht einen schwerwiegenden Fehler aufweist, erhalten Sie die folgende Antwort:

```json
{
  "message": <fatal error message>,
  "errors": [
    {
      <fatal error message>
    }
  ]
}
```

### Antwortcodes für schwerwiegende Fehler

Informationen zu Statuscodes und zugehörigen Fehlermeldungen, die Braze zurückgibt, wenn Ihre Anfrage auf einen schwerwiegenden Fehler stößt, finden Sie unter [Schwerwiegende Fehler und Antworten]({{site.baseurl}}/api/errors/#fatal-errors).

Wenn Sie die Fehlermeldung „provided external_id is blacklisted and disallowed" erhalten, hat Ihre Anfrage möglicherweise einen „Dummy-Nutzer" enthalten. Weitere Informationen finden Sie unter [Spam-Blockierung]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking).

### Endpunktspezifische Fehler

Die folgenden Fehler sind spezifisch für den Endpunkt `/users/track` und werden im Array `errors` der Antwort zurückgegeben. Verwenden Sie diese zur Fehlerbehebung bei einzelnen Objekten in einer Anfrage.

| Fehler | Beschreibung |
|---|---|
| `BAD_DEVICE_ID` | Die `device_id` für einen Token-Import muss zwischen 8 und 255 Bytes lang sein. |
| `BAD_EMAIL_SUBSCRIPTION_STATE` | `email_subscribe` muss `subscribed`, `unsubscribed` oder `opted_in` sein. |
| `BAD_LOCATION_UPDATE` | `current_location` muss ein Objekt sein, das `longitude` und `latitude` enthält. |
| `BAD_PUSH_SUBSCRIPTION_STATE` | `push_subscribe` muss `subscribed`, `unsubscribed` oder `opted_in` sein. |
| `BAD_PUSH_TOKEN_APP_ID` | Die `app_id` in einem Token-Import muss ein gültiger App-Bezeichner aus dem aktuellen Workspace sein. |
| `BAD_PUSH_TOKEN_IMPORT` | Token-Importe müssen Token enthalten und `external_id` sowie `braze_id` ausschließen. |
| `BAD_PUSH_TOKEN_STRING` | Der `token`-Wert in einem Token-Import muss ein String sein. |
| `BAD_PUSH_TOKEN_VALUE` | `push_tokens` muss ein Array von Objekten sein. |
| `BAD_SUBSCRIPTION_GROUP_ARRAY` | `subscription_groups` muss ein Array sein. |
| `BAD_SUBSCRIPTION_GROUP_HASH` | Jedes Element im Array `subscription_groups` muss ein JSON-Objekt mit den Schlüsseln `subscription_group_id` und `subscription_state` sein. |
| `BAD_SUBSCRIPTION_GROUP_ID` | `subscription_group_id` muss eine gültige UUID einer Abo-Gruppe sein. |
| `BAD_SUBSCRIPTION_GROUP_STATE` | `subscription_state` für eine Abo-Gruppe muss `subscribed` oder `unsubscribed` sein. |
| `BLACKLISTED_EXTERNAL_USER_ID` | Die angegebene `external_id` ist blockiert und nicht zulässig. |
| `EMAIL_BAD_FORMAT` | Der für `email` angegebene Wert ist keine gültige E-Mail-Adresse. |
| `EXTERNAL_USER_ID_TOO_LARGE` | Die `external_id` überschreitet die maximal zulässige Länge von 987 Bytes. |
| `INVALID_ATTRIBUTE_EMAIL_SUBSCRIPTION_INFO` | `email_subscription_info` ist kein gültiges Attribut. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Häufig gestellte Fragen

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

### Was passiert, wenn mehrere Profile mit derselben E-Mail-Adresse gefunden werden?
Wenn die `external_id` existiert, priorisiert Braze das zuletzt aktualisierte Profil mit einer externen ID für Updates. Wenn die `external_id` nicht existiert, priorisiert Braze das zuletzt aktualisierte Profil für Updates.

### Was passiert, wenn kein Profil mit der E-Mail-Adresse existiert?
Braze erstellt ein Profil und eine:n Nur-E-Mail-Nutzer:in und setzt das E-Mail-Feld auf test@braze.com, wie in der Beispiel-Anfrage für das Update eines Nutzerprofils über eine E-Mail-Adresse angegeben. Braze erstellt keinen Alias.

### Wie verwenden Sie `/users/track`, um alte Nutzerdaten zu importieren?
Sie können über die Braze API Daten für eine:n Nutzer:in übermitteln, die/der Ihre mobile App noch nicht verwendet hat, um ein Nutzerprofil zu erstellen. Wenn die/der Nutzer:in die Anwendung anschließend nutzt, werden alle Informationen nach der Identifizierung über das SDK mit dem bestehenden Nutzerprofil zusammengeführt, das Sie über den API-Aufruf erstellt haben. Jegliches Nutzerverhalten, das vom SDK vor der Identifizierung anonym aufgezeichnet wurde, geht beim Zusammenführen mit dem bestehenden, über die API generierten Nutzerprofil verloren.

Das Segmentierungs-Tool berücksichtigt diese Nutzer:innen unabhängig davon, ob sie mit der App interagiert haben. Wenn Sie Nutzer:innen ausschließen möchten, die über die User API hochgeladen wurden und noch nicht mit der App interagiert haben, fügen Sie den Filter `Session Count > 0` hinzu.

### Wie vermeide ich die Erstellung doppelter Nutzerprofile?

Doppelte Profile können entstehen, wenn eine Anfrage einen primären Bezeichner (wie `external_id`) enthält, der keinem bestehenden Profil entspricht, zusammen mit einem `email`- oder `phone`-Wert, der mit einem bestehenden Profil übereinstimmt. Da primäre Bezeichner für die Nutzersuche verwendet werden, erstellt Braze ein neues Profil für die unbekannte `external_id`, anstatt das bestehende Nur-E-Mail- oder Nur-Telefon-Profil zu aktualisieren.

So vermeiden Sie Duplikate:

- Wenn Sie Nutzer:innen von Nur-E-Mail- oder Nur-Telefon-Profilen zu identifizierten Profilen überführen, verwenden Sie den [`/users/identify`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/), um dem bestehenden Profil eine `external_id` zuzuweisen, anstatt beides an `/users/track` zu senden.
- Wenn bereits Duplikate vorhanden sind, führen Sie diese mit dem [`/users/merge`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) zusammen.

### Wie behandelt `/users/track` doppelte Events?

Jedes Event-Objekt im Events-Array repräsentiert ein einzelnes Vorkommen eines angepassten Events durch eine:n Nutzer:in zu einem bestimmten Zeitpunkt. Das bedeutet, dass jedes in Braze aufgenommene Event seine eigene Event-ID hat, sodass „doppelte" Events als separate, eindeutige Events behandelt werden.

### Wie geht `/users/track` mit ungültigen verschachtelten angepassten Attributen um?

Wenn ein verschachteltes angepasstes Attribut ungültige Werte enthält (z. B. ungültige Zeitformate oder Null-Werte), verwirft Braze alle Updates verschachtelter angepasster Attribute in der Anfrage. Dies gilt für alle verschachtelten Strukturen innerhalb dieses spezifischen Attributs. Um eine erfolgreiche Verarbeitung sicherzustellen, überprüfen Sie vor dem Senden, ob alle Werte innerhalb der verschachtelten angepassten Attribute gültig sind.

## Monatlich aktive Nutzer:innen CY 24-25, Universal MAU, Web MAU und Mobile MAU

Für Kund:innen mit neuen Preismodellen werden Rate-Limits auf Unternehmensebene durchgesetzt. Kund:innen können Workspace-Rate-Limits für stündliche Limits festlegen, aber Burst-Limits werden weiterhin von allen Workspaces gemeinsam genutzt.

Für Kund:innen, die monatlich aktive Nutzer:innen CY 24-25, Universal MAU, Web MAU oder Mobile MAU erworben haben, verwaltet Braze verschiedene Rate-Limits auf dem Endpunkt `/users/track`:
- Die stündlichen Rate-Limits richten sich nach der erwarteten Datenaufnahme-Aktivität auf Ihrem Konto, die von der Anzahl der erworbenen monatlich aktiven Nutzer:innen, der Branche, der Saisonalität oder anderen Faktoren abhängen kann.
- Zusätzlich zum stündlichen Limit setzt Braze ein Burst-Limit für die Anzahl der Anfragen durch, die alle drei Sekunden gesendet werden können.
- Jede Anfrage kann bis zu 75 Updates kombiniert über Attribut-, Event- oder Kauf-Objekte zusammenfassen.

Aktuelle Limits basierend auf der erwarteten Datenaufnahme finden Sie im Dashboard unter **Einstellungen** > **APIs und Bezeichner** > **API-Nutzungs-Dashboard**. Wir können Rate-Limits ändern, um die Systemstabilität zu schützen oder einen höheren Datendurchsatz auf Ihrem Konto zu ermöglichen. Bitte wenden Sie sich an den Braze Support oder Ihren Customer-Success-Manager, wenn Sie Fragen oder Bedenken bezüglich des stündlichen oder sekündlichen Anfragelimits und der Anforderungen Ihres Unternehmens haben.

### Rate-Limit-Header für monatlich aktive Nutzer:innen CY 24-25, Universal MAU, Web MAU und Mobile MAU

Alle Antworten ohne Rate-Limit (z. B. nicht `429`) enthalten die folgenden HTTP-Antwort-Header, die dem Client den Status des stündlichen Rate-Limit-Fensters anzeigen. Verwenden Sie diese Header, um Ihre Anfragerate zu verwalten:

| Header-Name             | Beschreibung                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| `X-RateLimit-Limit`     | Die Anzahl der zulässigen Anfragen pro Zeitraum                                              |
| `X-RateLimit-Remaining` | Die ungefähre Anzahl der verbleibenden Anfragen innerhalb eines Fensters                                |
| `X-RateLimit-Reset`     | Die Anzahl der verbleibenden Sekunden, bevor das aktuelle Fenster zurückgesetzt wird                                    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Beachten Sie, dass die Header `RateLimit-Limit`, `RateLimit-Remaining` und `RateLimit-Reset` nicht zurückgegeben werden, wenn ein HTTP-`429`-Fehler auftritt. In diesem Fall werden diese Header durch einen `X-Ratelimit-Retry-After`-Header ersetzt, der eine Ganzzahl zurückgibt, die die Anzahl der Sekunden angibt, bevor Sie wieder Anfragen stellen können.

{% endapi %}