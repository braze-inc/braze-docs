---
nav_title: "POST: Nutzer:innen tracken (synchron)"
article_title: "POST: Nutzer:innen verfolgen (Synchron)"
alias: /post_user_track_synchronous/
layout: api_page
page_order: 4.5
page_type: reference
description: "Dieser Artikel beschreibt Details zum synchronen Tracking von Nutzer:innen in Braze."

---
{% api %}
# Nutzer:innen tracken (synchron)
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/benutzer/track/sync
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um angepasste Events und Käufe aufzuzeichnen und die Attribute des Nutzerprofils synchron zu aktualisieren. Dieser Endpunkt funktioniert ähnlich wie der [Endpunkt `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), der die Nutzerprofile asynchron aktualisiert.

{% alert important %}
Dieser Endpunkt befindet sich derzeit in der Beta-Phase. Kontaktieren Sie Ihren Braze-Konto Manager:in, wenn Sie an dieser Beta teilnehmen möchten.
{% endalert %}

## Synchrone und asynchrone API-Aufrufe

Bei einem asynchronen Aufruf gibt die API den Status Code `201` zurück, der anzeigt, dass Ihre Anfrage erfolgreich empfangen, verstanden und akzeptiert wurde. Dies bedeutet jedoch nicht, dass Ihre Anfrage vollständig bearbeitet wurde.

Bei einem synchronen Aufruf gibt die API einen Status Code `201` zurück, der anzeigt, dass Ihre Anfrage erfolgreich empfangen, verstanden, akzeptiert und abgeschlossen wurde. In der Antwort auf den Anruf werden ausgewählte Felder des Nutzerprofils als Ergebnis des Vorgangs angezeigt.

Dieser Endpunkt hat ein niedrigeres Rate-Limit als der Endpunkt `/users/track` (siehe [Rate-Limit](#rate-limit) unten). Jede Anfrage von `/users/track/sync` kann nur ein Ereignisobjekt, ein Attribut-Objekt **oder** ein Kauf-Objekt enthalten. Dieser Endpunkt sollte für Updates von Nutzerprofilen reserviert sein, wenn ein synchroner Aufruf erforderlich ist. Für eine gesunde Implementierung empfehlen wir `/users/track/sync` und `/users/track` zusammen zu verwenden.

Wenn Sie beispielsweise innerhalb eines kurzen Zeitraums aufeinanderfolgende Anfragen für denselben Nutzer:innen senden, sind Race-Conditions mit dem asynchronen Endpunkt `/users/track` möglich. Mit dem Endpunkt `/users/track/sync` können Sie diese Anfragen jedoch nacheinander senden, jeweils nach Erhalt einer Antwort von `2XX`.

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit der Berechtigung `users.track.sync`.

Kund:innen, die die API für Server-zu-Server-Aufrufe verwenden, müssen möglicherweise die Liste `rest.iad-01.braze.com` zulassen, wenn sie sich hinter einer Firewall befinden.

## Rate-Limit

Für diesen Endpunkt gilt für alle Kund:in ein Basisgeschwindigkeitslimit von 500 Anfragen pro Minute. Jede Anfrage von `/users/track/sync` kann bis zu einem Ereignisobjekt, einem Attribut-Objekt oder einem Kauf-Objekt enthalten. Jedes Objekt (Ereignis-, Attribut- und Kauf-Arrays) kann jeweils eine:n Nutzer:in aktualisieren.

## Anfragetext

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, one attributes object),
  "events": (optional, one event object),
  "purchases": (optional, one purchase object),
}
```

### Parameter der Anfrage

{% alert important %}
Für jede in der folgenden Tabelle aufgeführte Komponente einer Anfrage ist eine der folgenden Angaben erforderlich: `external_id`, `user_alias`, `braze_id`, `email` oder `phone`.
{% endalert %}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `attributes` | Optional | Ein Attribute Objekt | Siehe [Nutzer:innen Attribute Objekt]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Optional | Ein Ereignisobjekt | Siehe [Objekt Ereignisse]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Optional | Ein Kauf-Objekt | Siehe [Kauf-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Antworten

Wenn Sie die [Anfrageparameter](#request-parameters) dieses Endpunkts verwenden, sollten Sie eine der folgenden Antworten erhalten: eine erfolgreiche Nachricht oder eine Nachricht mit schwerwiegenden Fehlern.

### Erfolgreiche Nachricht

Erfolgreiche Nachrichten liefern die folgende Antwort, die Informationen über die aktualisierten Nutzerprofildaten enthält.

```json
{
    "users": (optional, object), the identifier of the user in the request. May be empty if no users are found and _update_existing_only key is set to true,
        "custom_attributes": (optional, object), the custom attributes as a result of the request. Only custom attributes from the request will be listed,
        "custom_events": (optional, object), the custom events as a result of the request. Only custom events from the request will be listed,
        "purchase_events": (optional, object), the purchase events as a result of the request. Only purchase events from the request will be listed,
    },
    "message": "success"
```

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

## Beispielanfragen und -antworten

### Update eines angepassten Attributs nach externer ID

#### Anfrage

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "external_id": "xyz123",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ]
}'
```

#### Antwort

```
{
    "users": [
        {
            "external_id": "xyz123",
            "custom_attributes": {
                "string_attribute": "fruit",
                "boolean_attribute_1": true,
                "integer_attribute": 25,
                "array_attribute": [
                    "banana",
                    "apple",
                ]
            }
        }
    ],
    "message": "success"
} 
```

### Ein angepasstes Event per E-Mail aktualisieren

#### Anfrage

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
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
        }
    ]
}'
```

#### Antwort

```
{
    "users": [
        {
            "email": "test@braze.com",
            "custom_events": [
                {
                "name": "rented_movie",
                "first": "2022-01-001T00:00:00.000Z",
                "last": "2022-12-06T18:20:45.000Z",
                "count": 10
                }
            ]
        }
    ],
    "message": "success"
} 
```

### Update eines Kauf-Events durch Nutzer:in-Alias

#### Anfrage

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "purchases" : [
    {
      "user_alias" : { 
          "alias_name" : "device123", 
          "alias_label" : "my_device_identifier"
      }
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "Completed Order",
      "currency" : "USD",
      "price" : 219.98,
      "time" : "2022-12-06T19:20:45+01:00",
      "properties" : {
          "products" : [ 
            {
              "name": "Monitor",
              "category": "Gaming",
              "product_amount": 19.99
            },
            { 
              "name": "Gaming Keyboard",
              "category": "Gaming ",
              "product_amount": 199.99
            }
          ]
      }
   }
  ]
}'
```

#### Antwort

```
{
    "users": [
        {
          "user_alias" : { 
            "alias_name" : "device123", 
            "alias_label" : "my_device_identifier"
          },
          "purchase_events": [
                {
                "product_id": "Completed Order",
                "first": "2013-07-16T19:20:30+01:00",
                "last": "2022-12-06T18:20:45.000Z",
                "count": 3
                }
            ]
        }
    ],
    "message": "success"
} 
```

## Häufig gestellte Fragen

### Soll ich den asynchronen oder den synchronen Endpunkt verwenden?

Für die meisten Updates von Profilen eignet sich der Endpunkt `/users/track` am besten, da er ein höheres Rate-Limit hat und Sie Anfragen in Stapeln bearbeiten können. Der Endpunkt `/users/track/sync` ist jedoch nützlich, wenn Sie Race-Conditions aufgrund von schnellen, aufeinanderfolgenden Anfragen für denselben Nutzer:innen erleben.

### Weicht die Antwortzeit vom Endpunkt `/users/track` ab?

Bei einem synchronen Aufruf wartet die API, bis die Anfrage abgeschlossen ist, um eine Antwort zurückzugeben. Daher dauern synchrone Anfragen im Durchschnitt länger als asynchrone Anfragen an `/users/track`. Für die meisten Anfragen können Sie innerhalb von Sekunden eine Antwort erwarten.

### Kann ich mehrere Anfragen gleichzeitig senden?

Ja, solange die Anfragen für verschiedene Nutzer:innen sind oder jede Anfrage verschiedene Attribute, Ereignisse, Käufe für einen Nutzer:innen aktualisiert.

Wenn Sie mehrere Anfragen für einen Nutzer:innen für dasselbe Attribut, Ereignis oder Kauf senden, empfiehlt Braze, zwischen den einzelnen Anfragen auf eine erfolgreiche Antwort zu warten, um Race-Conditions zu vermeiden.

### Warum stimmt der Antwortwert nicht mit dem in meiner ursprünglichen Anfrage überein?

Obwohl Ihre Anfrage abgeschlossen ist, ist es möglich, dass der Wert Ihres angepassten Attributs nicht aktualisiert wurde. Dies kann passieren, wenn Ihr angepasstes Attribut Update die maximale Anzahl von Zeichen überschreitet, die Array-Grenzen überschreitet oder wenn der Nutzer:in nicht in Braze existiert und Sie `_update_existing_only = true` haben.

In diesen Fällen sollten Sie die Antwort als Hinweis darauf betrachten, dass Ihre Anfrage zwar abgeschlossen, das gewünschte Update jedoch nicht durchgeführt wurde. Beheben Sie die Fehlerbehebung anhand der oben genannten Gründe, die dazu führen können.

{% endapi %}
