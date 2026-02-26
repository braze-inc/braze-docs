---
nav_title: "POST: Erstellen Sie geplante Nachrichten"
article_title: "POST: Geplante Nachrichten erstellen"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Endpunkt Zeitplan Nachrichten erstellen von Braze."

---
{% api %}
# Erstellen Sie geplante Nachrichten
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/nachrichten/zeitplan/erstellen
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um einen Zeitplan für eine Kampagne, ein Canvas oder eine andere Nachricht zu erstellen, die zu einem bestimmten Zeitpunkt versendet werden soll, und geben Sie einen Bezeichner an, mit dem Sie diese Nachricht für Updates referenzieren können.

Wenn Sie ein Segment Targeting betreiben, wird eine Aufzeichnung Ihrer Anfrage in der [Entwickler:in-Konsole](https://dashboard.braze.com/app_settings/developer_console/activitylog/) gespeichert, nachdem alle geplanten Nachrichten versendet worden sind.

{% alert tip %}
Wenn Sie daran interessiert sind, Nachrichten sofort an bestimmte Nutzer:innen zu senden, verwenden Sie stattdessen den [Endpunkt`/messages/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages).
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#25272fb8-bc39-41df-9a41-07ecfd76cb1d {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `messages.schedule.create`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' category='send messages endpoints' %}

## Anfragetext

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  // You will need to include at least one of 'segment_id', 'external_user_ids', and 'audience'
  // Including 'segment_id' will send to members of that segment
  // Including 'external_user_ids' and/or 'user_aliases' will send to those users
  // Including both a Segment and users will send to the provided users if they are in the segment
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if users are not specified,
  "external_user_ids": (optional, array of strings) see external user identifier,
  "user_aliases": (optional, array of user alias object) see user alias,
  "audience": (optional, connected audience object) see connected audience,
  "campaign_id": (optional, string) see campaign identifier,
  "send_id": (optional, string) see send identifier,
  "override_messaging_limits": (optional, bool) ignore frequency capping rules, defaults to false,
  "recipient_subscription_state": (optional, string) use this to send messages to only users who have opted in ('opted_in'), only users who have subscribed or are opted in ('subscribed') or to all users, including unsubscribed users ('all'), the latter being useful for transactional email messaging. Defaults to 'subscribed',
  "schedule": {
    "time": (required, datetime as ISO 8601 string) time to send the message in UTC,
    "in_local_time": (optional, bool),
    "at_optimal_time": (optional, bool),
  },
  "messages": {
    "apple_push": (optional, apple push object),
    "android_push": (optional, android push object),
    "kindle_push": (optional, kindle/fireOS push object),
    "web_push": (optional, web push object),
    "email": (optional, email object),
    "webhook": (optional, webhook object),
    "content_card": (optional, content card object),
    "sms": (optional, SMS object)
  }
}
```

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
|`broadcast`| Optional | Boolesch | Sie müssen `broadcast` auf true setzen, wenn Sie eine Nachricht an ein ganzes Segment senden, auf das eine Kampagne oder ein Canvas abzielt. Dieser Parameter ist standardmäßig auf `false` eingestellt. <br><br> Wenn `broadcast` auf `true` eingestellt ist, kann eine Empfänger:innen-Liste nicht aufgenommen werden. Seien Sie jedoch vorsichtig, wenn Sie `broadcast: true` setzen, denn wenn Sie dieses Flag unbeabsichtigt setzen, kann dies dazu führen, dass Sie Ihre Nachricht an eine größere Zielgruppe als erwartet senden. |
| `external_user_ids` | Optional | String-Array | Siehe [externer Bezeichner für Nutzer:innen]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields). |
| `user_aliases` | Optional | Array von Nutzer:innen-Alias-Objekten | Siehe [Nutzer-Alias Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
| `audience` | Optional | Verbundenes Objekt der Zielgruppe | Siehe [verbundene Zielgruppe]({{site.baseurl}}/api/objects_filters/connected_audience/). |
| `segment_id` | Optional | String | Siehe [Bezeichner für Segmente]({{site.baseurl}}/api/identifier_types/). |
| `campaign_id`|Optional|String| Siehe [Bezeichner der Kampagne]({{site.baseurl}}/api/identifier_types/). |
| `send_id` | Optional | String | Siehe [Bezeichner senden]({{site.baseurl}}/api/identifier_types/). |
| `override_messaging_limits` | Optional | Boolesch | Frequency-Capping für Kampagnen ignorieren, Standardwert ist false |
|`recipient_subscription_state`| Optional | String | Verwenden Sie diese Option, um Nachrichten nur an Nutzer:in (`opted_in`), nur an Nutzer:in (`subscribed`) oder an alle Nutzer:in zu senden, auch an abgemeldete Nutzer (`all`), die sich angemeldet haben. <br><br>Die Verwendung von `all` Nutzer:innen ist nützlich für Transaktions-E-Mails Messaging. Standardmäßig ist `subscribed` eingestellt. |
| `schedule` | Erforderlich | Objekt Zeitplan | Siehe [Zeitplan Objekt]({{site.baseurl}}/api/objects_filters/schedule_object/) |
| `messages` | Optional | Messaging Objekt | Siehe [verfügbare Messaging-Objekte]({{site.baseurl}}/api/objects_filters/#messaging-objects). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/schedule/create' \
--data-raw '{
  "broadcast": "false",
  "external_user_ids": "external_user_identifiers",
  "user_aliases": {
    "alias_name" : "example_name",
    "alias_label" : "example_label"
  },
  "segment_id": "segment_identifiers",
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
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "override_messaging_limits": false,
  "recipient_subscription_state": "subscribed",
  "schedule": {
    "time": "",
    "in_local_time": true,
    "at_optimal_time": true
  },
  "messages": {
    "apple_push": (optional, Apple Push Object),
    "android_push": (optional, Android Push Object),
    "kindle_push": (optional, Kindle/FireOS Push Object),
    "web_push": (optional, Web Push Object),
    "email": (optional, Email object)
    "webhook": (optional, Webhook object)
    "content_card": (optional, Content Card Object)
  }
}'
```

## Antwort

### Beispiel für eine erfolgreiche Antwort

```json
{
    "dispatch_id": (string) the dispatch identifier,
    "schedule_id": (string) the schedule identifier,
    "message": "success"
}
```

{% endapi %}
