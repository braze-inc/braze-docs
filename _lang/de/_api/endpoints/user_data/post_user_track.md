---
nav_title: "POST: Benutzer verfolgen"
article_title: "POST: Benutzer verfolgen"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel enthält Details zum Tracking-Endpunkt von Braze."

---
{% api %}
# Benutzer verfolgen
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/track
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um benutzerdefinierte Ereignisse und Käufe zu erfassen und Benutzerprofilattribute zu aktualisieren.

{% alert note %}
Braze verarbeitet die über die API übermittelten Daten zum Nennwert. Kunden sollten nur Deltas (sich ändernde Daten) übermitteln, um den Verbrauch unnötiger Datenpunkte zu minimieren. Weitere Informationen finden Sie unter [Datenpunkte]({{site.baseurl}}/user_guide/data_and_analytics/data_points/).
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4cf57ea9-9b37-4e99-a02e-4373c9a4ee59 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit der Berechtigung `users.track`.

Kunden, die die API für Server-zu-Server-Aufrufe verwenden, müssen möglicherweise die Liste `rest.iad-01.braze.com` zulassen, wenn sie sich hinter einer Firewall befinden.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='users track' %}

## Körper der Anfrage

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

### Parameter anfordern

{% alert important %}
Für jede in der folgenden Tabelle aufgeführte Anforderungskomponente ist eine der folgenden Angaben erforderlich: `external_id`, `user_alias`, `braze_id`, `email`, oder `phone`.
{% endalert %}

| Parameter | Erforderlich | Daten Typ | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `attributes` | Optional | Array von Attributobjekten | Siehe [Objekt Benutzerattribute]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Optional | Array von Ereignisobjekten | Siehe [Objekt Ereignisse]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Optional | Array von Kaufobjekten | Siehe [Einkäufe Objekt]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfragen

### Ein Benutzerprofil nach E-Mail-Adresse aktualisieren

Über den Endpunkt `/users/track` können Sie ein Benutzerprofil nach E-Mail-Adresse aktualisieren. 

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

### Ein Benutzerprofil nach Telefonnummer aktualisieren

Über den Endpunkt `/users/track` können Sie ein Benutzerprofil nach Telefonnummer aktualisieren. Dieser Endpunkt funktioniert nur, wenn Sie eine gültige Telefonnummer angeben.

{% alert important %}
Wenn Sie eine Anfrage sowohl mit `email` als auch mit `phone` stellen, verwendet Braze die E-Mail als Identifikator.
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
### Abonnementgruppen festlegen

Dieses Beispiel zeigt, wie Sie einen Benutzer erstellen und seine Abonnementgruppe im Objekt Benutzerattribute festlegen. 

Wenn Sie den Abonnementstatus mit diesem Endpunkt aktualisieren, wird der durch seine `external_id` angegebene Benutzer (z.B. User1) aktualisiert und der Abonnementstatus aller Benutzer mit der gleichen E-Mail wie dieser Benutzer (User1) aktualisiert.

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

### Beispielanfrage zur Erstellung eines Alias-Benutzers

Sie können den Endpunkt `/users/track` verwenden, um einen neuen Nur-Alias-Benutzer zu erstellen, indem Sie den Schlüssel `_update_existing_only` mit dem Wert `false` im Text der Anfrage angeben. Wenn dieser Wert weggelassen wird, wird das Alias-Benutzerprofil nicht erstellt. Die Verwendung eines reinen Alias-Benutzers garantiert, dass ein Profil mit diesem Alias existiert. Dies ist besonders hilfreich, wenn Sie eine neue Integration erstellen, da es die Erstellung von doppelten Benutzerprofilen verhindert.

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

Wenn Sie eine der oben genannten API-Anfragen verwenden, sollten Sie eine der folgenden drei allgemeinen Antworten erhalten: eine [erfolgreiche Nachricht](#successful-message), eine [erfolgreiche Nachricht mit nicht fatalen Fehlern](#successful-message-with-non-fatal-errors) oder eine [Nachricht mit fatalen Fehlern](#message-with-fatal-errors).

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

### Erfolgreiche Nachricht mit nicht-tödlichen Fehlern

Wenn Ihre Nachricht erfolgreich ist, aber nicht schwerwiegende Fehler aufweist, wie z.B. ein ungültiges Ereignisobjekt aus einer langen Liste von Ereignissen, dann erhalten Sie die folgende Antwort:

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

Bei Erfolgsmeldungen werden alle Daten, die nicht von einem Fehler im Array `errors` betroffen sind, weiterhin verarbeitet. 

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

### Antwortcodes für schwerwiegende Fehler

Statuscodes und zugehörige Fehlermeldungen, die zurückgegeben werden, wenn Ihre Anfrage auf einen schwerwiegenden Fehler stößt, finden Sie unter [Schwerwiegende Fehler und Antworten]({{site.baseurl}}/api/errors/#fatal-errors).

Wenn Sie die Fehlermeldung "provided external_id is blacklisted and disallowed" erhalten, hat Ihre Anfrage möglicherweise einen "Dummy-Benutzer" enthalten. Weitere Informationen finden Sie unter [Spam-Blockierung]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking). 

## Häufig gestellte Fragen

{% multi_lang_include email-via-sms-warning.md %}

### Was passiert, wenn mehrere Profile mit der gleichen E-Mail-Adresse gefunden werden?
Wenn die `external_id` existiert, wird das zuletzt aktualisierte Profil mit einer externen ID bei Aktualisierungen bevorzugt. Wenn das `external_id` nicht existiert, wird das zuletzt aktualisierte Profil bei der Aktualisierung bevorzugt.

### Was passiert, wenn derzeit kein Profil mit der E-Mail-Adresse existiert?
Ein neues Profil wird erstellt und ein Benutzer, der nur per E-Mail erreichbar ist, wird angelegt. Ein Alias wird nicht erstellt. Das E-Mail-Feld wird auf test@braze.com gesetzt, wie in der Beispielanfrage für die Aktualisierung eines Benutzerprofils nach E-Mail-Adresse angegeben.

### Wie verwenden Sie `/users/track`, um alte Benutzerdaten zu importieren?
Sie können über die Braze API Daten für einen Benutzer übermitteln, der Ihre mobile App noch nicht verwendet hat, um ein Benutzerprofil zu erstellen. Wenn der Benutzer anschließend die Anwendung nutzt, werden alle Informationen, die auf seine Identifizierung mit dem SDK folgen, mit dem bestehenden Benutzerprofil zusammengeführt, das Sie mit dem API-Aufruf erstellt haben. Jegliches Benutzerverhalten, das vom SDK vor der Identifizierung anonym aufgezeichnet wurde, geht bei der Zusammenführung mit dem bestehenden, von der API generierten Benutzerprofil verloren.

Das Segmentierungstool berücksichtigt diese Nutzer unabhängig davon, ob sie die App genutzt haben oder nicht. Wenn Sie Benutzer ausschließen möchten, die mit der Benutzer-API hochgeladen wurden und noch nicht mit der App gearbeitet haben, fügen Sie den Filter `Session Count > 0` hinzu.

### Wie geht `/users/track` mit doppelten Ereignissen um?

Jedes Ereignisobjekt im Ereignis-Array steht für ein einzelnes Auftreten eines benutzerdefinierten Ereignisses durch einen Benutzer zu einem bestimmten Zeitpunkt. Das bedeutet, dass jedes Ereignis, das in Braze aufgenommen wird, seine eigene Ereignis-ID hat, so dass "doppelte" Ereignisse als separate, einzigartige Ereignisse behandelt werden.

## Monatlich aktive Nutzer CY 24-25
Für Kunden, die Monthly Active Users - CY 24-25 erworben haben, verwaltet Braze auf seinem Endpunkt `/users/track` verschiedene Tarifgrenzen:
- Die stündlichen Ratenlimits werden entsprechend der erwarteten Datenübernahmeaktivität auf Ihrem Konto festgelegt, die der Anzahl der monatlich aktiven Nutzer, die Sie erworben haben, der Branche, der Saisonalität oder anderen Faktoren entsprechen kann.
- Zusätzlich zur Begrenzung der Anfragen pro Stunde legt Braze auch ein Burst-Limit für die Anzahl der pro Sekunde zulässigen Anfragen fest.
- Jede Anfrage kann bis zu 50 Aktualisierungen für Attribut-, Ereignis- oder Kaufobjekte enthalten.

Die aktuellen Grenzwerte, die auf der erwarteten Ingestion basieren, finden Sie im Dashboard unter **Einstellungen** > **APIs und Identifikatoren** > **API-Grenzwerte**. Wir können Ratenbeschränkungen ändern, um die Systemstabilität zu schützen oder einen höheren Datendurchsatz auf Ihrem Konto zu ermöglichen. Wenden Sie sich bitte an den Braze-Support oder Ihren Customer Success Manager, wenn Sie Fragen oder Bedenken bezüglich der stündlichen oder sekündlichen Anfragebegrenzung und den Anforderungen Ihres Unternehmens haben.



{% endapi %}
