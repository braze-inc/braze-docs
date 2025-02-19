---
nav_title: "POST: Geplante Nachrichten erstellen"
article_title: "POST: Geplante Nachrichten erstellen"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel enthält Details zum Braze-Endpunkt Geplante Nachrichten erstellen."

---
{% api %}
# Geplante Nachrichten erstellen
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/messages/schedule/create
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Kampagne, ein Canvas oder eine andere Nachricht zu planen, die zu einem bestimmten Zeitpunkt versendet werden soll, und geben Sie einen Identifikator an, mit dem Sie diese Nachricht bei Aktualisierungen referenzieren können.

Wenn Sie ein Segment anvisieren, wird ein Datensatz Ihrer Anfrage in der [Entwicklerkonsole](https://dashboard.braze.com/app_settings/developer_console/activitylog/) gespeichert, nachdem alle geplanten Nachrichten versendet wurden.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#25272fb8-bc39-41df-9a41-07ecfd76cb1d {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `messages.schedule.create`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='default' category='message endpoints' %}

## Körper der Anfrage

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
  "segment_id": (optional, string) see segment identifier,
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

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
| --------- | ---------| --------- | ----------- |
|`broadcast`| Optional | Boolesche | Sie müssen `broadcast` auf true setzen, wenn Sie eine Nachricht an ein ganzes Segment senden, auf das eine Kampagne oder ein Canvas abzielt. Dieser Parameter ist standardmäßig auf false eingestellt (Stand: 31\. August 2017). <br><br> Wenn `broadcast` auf true gesetzt ist, kann eine `recipients` Liste nicht aufgenommen werden. Seien Sie jedoch vorsichtig, wenn Sie `broadcast: true` setzen, da das unbeabsichtigte Setzen dieser Markierung dazu führen kann, dass Sie Ihre Nachricht an ein größeres Publikum als erwartet senden. |
| `external_user_ids` | Optional | Array von Zeichenketten | Siehe [externe Benutzerkennungen]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields). |
| `user_aliases` | Optional | Array von Benutzer-Alias-Objekten | Siehe [Benutzer-Alias-Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
| `audience` | Optional | Verbundenes Publikumsobjekt | Siehe [angeschlossenes Publikum]({{site.baseurl}}/api/objects_filters/connected_audience/). |
| `segment_id` | Optional | String | Siehe [Segmentbezeichner]({{site.baseurl}}/api/identifier_types/). |
| `campaign_id`|Optional|String| Siehe [Kennung der Kampagne]({{site.baseurl}}/api/identifier_types/). |
| `recipients` | Optional | Array von Empfängerobjekten | Siehe [Empfängerobjekt]({{site.baseurl}}/api/objects_filters/recipient_object/). |
| `send_id` | Optional | String | Siehe [Kennung senden]({{site.baseurl}}/api/identifier_types/). |
| `override_messaging_limits` | Optional | Boolesche | Globale Ratenbeschränkungen für Kampagnen ignorieren, Standardwert ist false |
|`recipient_subscription_state`| Optional | String | Verwenden Sie diese Option, um Nachrichten nur an Benutzer zu senden, die sich angemeldet haben (`opted_in`), nur an Benutzer, die sich angemeldet haben oder angemeldet sind (`subscribed`) oder an alle Benutzer, einschließlich nicht angemeldeter Benutzer (`all`). <br><br>Die Verwendung von `all` ist nützlich für transaktionale E-Mail-Nachrichten. Die Standardeinstellung ist `subscribed`. |
| `schedule` | Erforderlich | Objekt terminieren | Siehe [Objekt Zeitplan]({{site.baseurl}}/api/objects_filters/schedule_object/) |
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
