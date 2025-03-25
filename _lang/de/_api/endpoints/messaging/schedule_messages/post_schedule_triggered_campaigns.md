---
nav_title: "POST: Planen von API-gesteuerten Kampagnen"
article_title: "POST: Planen von API-gesteuerten Kampagnen"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "In diesem Artikel finden Sie Einzelheiten zum API-gesteuerten Kampagnen-Endpunkt Braze."

---
{% api %}
# Planen Sie API-ausgelöste Kampagnen
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/trigger/schedule/create
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um vom Dashboard erstellte Kampagnennachrichten über eine API-ausgelöste Zustellung zu versenden. Dabei können Sie entscheiden, welche Aktion den Versand der Nachricht auslösen soll.

Sie können `trigger_properties` übergeben, das als Vorlage in die Nachricht selbst eingefügt wird.

Beachten Sie, dass Sie zum Senden von Nachrichten über diesen Endpunkt eine [Kampagnen-ID]({{site.baseurl}}/api/identifier_types/) benötigen, die Sie bei der Erstellung einer [API-ausgelösten Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) erstellt haben.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b7e61de7-f2c2-49c9-9e46-b85a0aa01bba {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `campaigns.trigger.schedule.create`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='default' category='Nachrichtenendpunkte' %}

## Körper der Anfrage

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
## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
| --------- | ---------| --------- | ----------- |
|`campaign_id`|Erforderlich|String| Siehe [Kennung der Kampagne]({{site.baseurl}}/api/identifier_types/)|
| `send_id` | Optional | String | Siehe [Kennung senden]({{site.baseurl}}/api/identifier_types/). |
| `recipients` | Optional | Array von Empfängerobjekten | Siehe [Empfängerobjekt]({{site.baseurl}}/api/objects_filters/recipient_object/). |
| `audience` | Optional | Verbundenes Publikumsobjekt | Siehe [angeschlossenes Publikum]({{site.baseurl}}/api/objects_filters/connected_audience/). |
|`broadcast`| Optional | Boolesche | Sie müssen `broadcast` auf true setzen, wenn Sie eine Nachricht an ein ganzes Segment senden, auf das eine Kampagne oder ein Canvas abzielt. Dieser Parameter ist standardmäßig auf false eingestellt (Stand: 31\. August 2017). <br><br> Wenn `broadcast` auf true gesetzt ist, kann eine `recipients` Liste nicht aufgenommen werden. Seien Sie jedoch vorsichtig, wenn Sie `broadcast: true` setzen, da das unbeabsichtigte Setzen dieser Markierung dazu führen kann, dass Sie Ihre Nachricht an ein größeres Publikum als erwartet senden. |
| `trigger_properties` | Optional | Objekt | Personalisierungs-Schlüsselwertpaare für alle Benutzer in dieser Sendung. Siehe [Auslösereigenschaften]({{site.baseurl}}/api/objects_filters/trigger_properties_object/). |
| `schedule` | Erforderlich | Objekt terminieren | Siehe [Schedule-Objekt]({{site.baseurl}}/api/objects_filters/schedule_object/). |
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
