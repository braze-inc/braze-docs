---
nav_title: "POST: Nutzer:innen tracken"
article_title: "POST: Nutzer:innen tracken"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Tracking Nutzer:innen Endpunkts."

---
{% api %}
# Nutzer:innen tracken
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/benutzer:innen/track
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um angepasste Events und Käufe aufzuzeichnen und die Attribute des Nutzerprofils zu aktualisieren.

{% alert note %}
Braze verarbeitet die über die API übergebenen Daten zum Nennwert, und Kunden sollten nur Deltas (sich ändernde Daten) übergeben, um den Verbrauch unnötiger Datenpunkte zu minimieren. Um mehr zu erfahren, referenzieren Sie auf [Datenpunkte]({{site.baseurl}}/user_guide/data/data_points/).
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4cf57ea9-9b37-4e99-a02e-4373c9a4ee59 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit der Berechtigung `users.track`.

Kund:innen, die die API für Server-zu-Server-Aufrufe verwenden, müssen möglicherweise die Liste `rest.iad-01.braze.com` zulassen, wenn sie sich hinter einer Firewall befinden.

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

### Parameter der Anfrage

{% alert important %}
Für jede in der folgenden Tabelle aufgeführte Komponente einer Anfrage ist eine der folgenden Angaben erforderlich: `external_id`, `user_alias`, `braze_id`, `email` oder `phone`.
{% endalert %}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `attributes` | Optional | Array der Attribute Objekte | Siehe [Nutzer:innen Attribute Objekt]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Optional | Array von Ereignisobjekten | Siehe [Objekt Ereignisse]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Optional | Array von Kauf-Objekten | Siehe [Kauf-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel-Anfragen

### Update eines Nutzerprofils über eine E-Mail Adresse

Über den Endpunkt `/users/track` können Sie ein Nutzerprofil per E-Mail aktualisieren. 

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

### Update eines Nutzerprofils nach Rufnummer

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

Dieses Beispiel zeigt, wie Sie einen Nutzer:innen anlegen und seine Abo-Gruppe im Objekt Benutzerattribute festlegen. 

Das Aktualisieren des Abo-Status mit diesem Endpunkt aktualisiert den durch seine `external_id` angegebenen Nutzer (z.B. User1) und aktualisiert den Abo-Status aller Nutzer:innen mit der gleichen E-Mail wie dieser Nutzer (User1).

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
          "subscription_state": "subscribed"
        }
      ]
    }
  ]
}'
```

### Beispiel für eine Anfrage zur Erstellung eines Nutzers:in, der nur einen Alias hat

Sie können den Endpunkt `/users/track` verwenden, um einen neuen Nutzer:innen mit einem Alias zu erstellen, indem Sie den Schlüssel `_update_existing_only` mit dem Wert `false` im Textkörper der Anfrage angeben. Wenn dieser Wert weggelassen wird, wird das Nutzerprofil, das nur einen Alias enthält, nicht erstellt. Die Verwendung eines Nutzers:innen mit Alias garantiert, dass nur ein Profil mit diesem Alias existiert. Dies ist besonders hilfreich, wenn Sie eine neue Integration erstellen, da es die Erstellung doppelter Nutzer:innen-Profile verhindert.

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

Wenn Sie eine der oben genannten API-Anfragen verwenden, sollten Sie eine der folgenden drei allgemeinen Antworten erhalten: eine [erfolgreiche Nachricht](#successful-message), eine [erfolgreiche Nachricht mit nicht schwerwiegenden Fehlern](#successful-message-with-non-fatal-errors) oder eine [Nachricht mit schwerwiegenden Fehlern](#message-with-fatal-errors).

### Erfolgreiche Nachricht

Erfolgreiche Nachrichten werden mit der folgenden Antwort beantwortet:

```json
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this will return an integer of the number of external_ids with attributes that were queued to be processed,
  "events_processed": (optional, integer), if events are included in the request, this will return an integer of the number of events that were queued to be processed,
  "purchases_processed": (optional, integer), if purchases are included in the request, this will return an integer of the number of purchases that were queued to be processed,
}
```

### Erfolgreiche Nachricht mit nicht schwerwiegenden Fehlern

Wenn Ihre Nachricht erfolgreich ist, aber nicht-schwerwiegende Fehler aufweist, wie z.B. ein ungültiges Ereignisobjekt aus einer langen Liste von Ereignissen, dann erhalten Sie die folgende Antwort:

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

Bei Erfolgsnachrichten werden alle Daten, die nicht von einem Fehler im Array `errors` betroffen sind, weiterhin verarbeitet. 

### Nachricht mit schwerwiegenden Fehlern

Wenn Ihre Nachricht einen schwerwiegenden Fehler enthält, erhalten Sie die folgende Antwort:

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

### Schwerwiegende Fehler Antwortcodes

Für Statuscodes und zugehörige Nachrichten, die zurückgegeben werden, wenn Ihre Anfrage auf einen schwerwiegenden Fehler stößt, referenzieren Sie [Schwerwiegende Fehler & Antworten.]({{site.baseurl}}/api/errors/#fatal-errors)

Wenn Sie die Fehlermeldung "provided external_id is blacklisted and disallowed" erhalten, hat Ihre Anfrage möglicherweise eine "Nutzer:innen-Attrappe" enthalten. Weitere Informationen finden Sie unter [Spam-Blockierung]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking). 

## Häufig gestellte Fragen

{% multi_lang_include email-via-sms-warning.md %}

### Was passiert, wenn mehrere Profile mit derselben E-Mail Adresse gefunden werden?
Wenn die `external_id` existiert, wird das zuletzt aktualisierte Profil mit einer externen ID bei Updates bevorzugt behandelt. Wenn das `external_id` nicht existiert, wird das zuletzt aktualisierte Profil für Updates bevorzugt.

### Was passiert, wenn kein Profil mit der E-Mail Adresse existiert?
Es wird ein neues Profil erstellt und ein Nutzer:in, der nur per E-Mail erreichbar ist. Ein Alias wird nicht erstellt. Das Feld E-Mail wird auf test@braze.com gesetzt, wie in der Beispielanfrage zum Update eines Nutzerprofils über die E-Mail-Adresse angegeben.

### Wie verwenden Sie `/users/track`, um alte Nutzer:innen-Daten zu importieren?
Sie können über die Braze API Daten für einen Nutzer:innen übermitteln, der Ihre mobile App noch nicht verwendet hat, um ein Nutzerprofil zu erstellen. Wenn der Nutzer:innen die Anwendung später nutzt, werden alle Informationen, die auf seine Identifizierung mit dem SDK folgen, mit dem bestehenden Nutzerprofil zusammengeführt, das Sie mit dem API-Aufruf erstellt haben. Jegliches Nutzerverhalten, das vom SDK vor der Identifizierung anonym aufgezeichnet wurde, geht bei der Zusammenführung mit dem bestehenden, von der API generierten Nutzerprofil verloren.

Das Segmentierungs-Tool berücksichtigt diese Nutzer:innen unabhängig davon, ob sie sich mit der App beschäftigt haben. Wenn Sie Nutzer:innen ausschließen möchten, die über die User API hochgeladen wurden und sich noch nicht mit der App beschäftigt haben, fügen Sie den Filter `Session Count > 0` hinzu.

### Wie behandelt `/users/track` doppelte Ereignisse?

Jedes Event-Objekt im Event-Array repräsentiert ein einzelnes Vorkommen eines angepassten Events durch einen Nutzer:in zu einem bestimmten Zeitpunkt. Das bedeutet, dass jedes Ereignis, das in Braze aufgenommen wird, seine eigene ID hat, so dass "doppelte" Ereignisse als separate, eindeutige Ereignisse behandelt werden.

### Wie geht `/users/track` mit ungültigen, verschachtelten angepassten Attributen um?

Wenn ein verschachteltes angepasstes Attribut ungültige Werte enthält (z.B. ungültige Zeitformate oder Nullwerte), werden alle verschachtelten angepassten Attribute in der Anfrage nicht verarbeitet. Dies gilt für alle verschachtelten Strukturen innerhalb dieses spezifischen Attributs. Um eine erfolgreiche Verarbeitung zu gewährleisten, überprüfen Sie vor dem Senden, ob alle Werte innerhalb der verschachtelten angepassten Attribute gültig sind.

## Monatlich aktive Nutzer:innen CY 24-25
Für Kunden, die Monatlich aktive:r Nutzer:innen - CY 24-25 erworben haben, verwaltet Braze verschiedene Rate-Limits auf seinem Endpunkt `/users/track`:
- Die stündlichen Rate-Limits richten sich nach der erwarteten Aktivität der Datenaufnahme auf Ihrem Konto, die von der Anzahl der monatlich aktiven Nutzer:innen, der Branche, der Saisonalität oder anderen Faktoren abhängen kann.
- Zusätzlich zum stündlichen Limit setzt Braze ein Burst-Limit für die Anzahl der Anfragen durch, die alle drei Sekunden gesendet werden können.
- Jede Anfrage kann bis zu 50 Updates für Attribute, Ereignisse oder Kauf-Objekte zusammenfassen.

Aktuelle Grenzwerte auf der Grundlage der erwarteten Ingestion finden Sie im Dashboard unter **Einstellungen** > **APIs und Bezeichner** > **API-Nutzungs-Dashboard**. Wir können Rate-Limits ändern, um die Systemstabilität zu schützen oder einen höheren Datendurchsatz auf Ihrem Konto zu ermöglichen. Wenden Sie sich bitte an den Braze Support oder Ihren Customer-Success-Manager:in, wenn Sie Fragen oder Bedenken bezüglich der stündlichen oder sekündlichen Begrenzung von Anfragen und den Anforderungen Ihres Unternehmens haben.



{% endapi %}
