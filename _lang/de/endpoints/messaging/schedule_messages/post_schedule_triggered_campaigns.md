---
nav_title: "POST: Zeitplan für API-getriggerte Kampagnen"
article_title: "POST: Zeitplan für API-getriggerte Kampagnen"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Endpunkt Zeitplan API-getriggerte Kampagnen Braze."

---
{% api %}
# Zeitplan für API-getriggerte Kampagnen
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/kampagnen/triggern/zeitplan/erstellen
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um vom Dashboard erstellte Kampagnen-Nachrichten über eine API-getriggerte Zustellung zu versenden. Dabei ist es zulässig, dass Sie entscheiden, welche Aktion den Versand der Nachricht auslösen soll.

Sie können `trigger_properties` übergeben, das als Template in die Nachricht selbst eingefügt wird.

Beachten Sie, dass Sie zum Versenden von Nachrichten mit diesem Endpunkt eine [ID für die Kampagne]({{site.baseurl}}/api/identifier_types/) benötigen, die Sie beim Erstellen einer [API-getriggerten Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) erstellt haben.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b7e61de7-f2c2-49c9-9e46-b85a0aa01bba {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `campaigns.trigger.schedule.create`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' category='send messages endpoints' %}

## Anfragetext

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "send_id": (optional, string) see send identifier,
  // Including 'recipients' will send only to the provided user ids if they are in the campaign's segment
  "recipients": (optional, array of recipients object),
  // for any keys that conflict between these trigger properties and those in a Recipients Object, the value from the Recipients Object will be used
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' will only send to users in the audience
  // If 'recipients' and 'audience' are not provided and broadcast is not set to 'false',
  // the message will send to entire segment targeted by the campaign
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" object is omitted,
  "trigger_properties": (optional, object) personalization key-value pairs for all users in this send; see trigger properties,
  "schedule": {
    "time": (required, datetime as ISO 8601 string) time to send the message,
    "in_local_time": (optional, bool),
    "at_optimal_time": (optional, bool),
  }
}
```
## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
|`campaign_id`|Erforderlich|String| Siehe [Bezeichner der Kampagne]({{site.baseurl}}/api/identifier_types/)|
| `send_id` | Optional | String | Siehe [Bezeichner senden]({{site.baseurl}}/api/identifier_types/). |
| `recipients` | Optional | Array von Empfänger:innen-Objekten | Siehe [Empfänger:innen Objekt]({{site.baseurl}}/api/objects_filters/recipient_object/). |
| `audience` | Optional | Verbundenes Objekt der Zielgruppe | Siehe [verbundene Zielgruppe]({{site.baseurl}}/api/objects_filters/connected_audience/). |
|`broadcast`| Optional | Boolesch | Sie müssen `broadcast` auf true setzen, wenn Sie eine Nachricht an ein ganzes Segment senden, auf das eine Kampagne oder ein Canvas abzielt. Dieser Parameter ist standardmäßig auf false eingestellt (Stand: 31\. August 2017). <br><br> Wenn `broadcast` auf true gesetzt ist, kann eine `recipients` Liste nicht aufgenommen werden. Seien Sie jedoch vorsichtig, wenn Sie `broadcast: true` setzen, denn wenn Sie dieses Flag unbeabsichtigt setzen, kann dies dazu führen, dass Sie Ihre Nachricht an eine größere Zielgruppe als erwartet senden. |
| `trigger_properties` | Optional | Objekt | Schlüssel-Wert-Paare zur Personalisierung für alle Nutzer:innen in dieser Sendung. Siehe [Eigenschaften des Auslösers]({{site.baseurl}}/api/objects_filters/trigger_properties_object/). |
| `schedule` | Erforderlich | Objekt Zeitplan | Siehe [Zeitplan-Objekt]({{site.baseurl}}/api/objects_filters/schedule_object/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "recipients": [
    {
      "user_alias": "example_alias",
      "external_user_id": "external_user_identifier",
      "trigger_properties": {}
    }
  ],
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "eye_color",
          "comparison": "equals",
          "value": "blue"
        }
      },
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_foods",
          "comparison": "includes_value",
          "value": "pizza"
        }
      },
      {
        "OR": [
          {
            "custom_attribute": {
              "custom_attribute_name": "last_purchase_time",
              "comparison": "less_than_x_days_ago",
              "value": 2
            }
          },
          {
            "push_subscription_status": {
              "comparison": "is",
              "value": "opted_in"
            }
          }
        ]
      },
      {
        "email_subscription_status": {
          "comparison": "is_not",
          "value": "subscribed"
        }
      },
      {
        "last_used_app": {
          "comparison": "after",
          "value": "2019-07-22T13:17:55+0000"
        }
      }
    ]
  },
  "broadcast": false,
  "trigger_properties": {},
  "schedule": {
    "time": "",
    "in_local_time": false,
    "at_optimal_time": false
  }
}'
```

## Antwort

### Beispiel für eine erfolgreiche Antwort

```json
Content-Type: application/json
Authorization: Bearer YOUR-API-KEY-HERE
{
{
    "dispatch_id": "dispatch_identifier",
    "schedule_id": "schedule_identifier",
    "message": "success"
}
```

{% endapi %}
