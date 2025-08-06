---
nav_title: "POST: Senden Sie Nachrichten sofort und nur über die API"
article_title: "POST: Senden Sie Nachrichten sofort und nur über die API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Nachrichten sofort senden nur über API Braze."

---
{% api %}
# Senden Sie Nachrichten sofort nur über die API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/nachrichten/senden
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um über die Braze API sofortige Nachrichten an bestimmte Nutzer:innen zu senden.

Wenn Sie ein Segment Targeting betreiben, wird ein Datensatz Ihrer Anfrage in der [Entwickler:in-Konsole](https://dashboard.braze.com/app_settings/developer_console/activitylog/) gespeichert.

{% multi_lang_include api/payload_size_alert.md %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#946cb701-96e3-48d7-868c-f079785b6d24 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, müssen Sie einen API-Schlüssel mit der Berechtigung `messages.send` erstellen.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='message send endpoint' %}

## Anfragetext

{% alert tip %}
Achten Sie darauf, dass Sie [Messaging-Objekte]({{site.baseurl}}/api/objects_filters/#messaging-objects) in Ihren Textkörper aufnehmen, um Ihre Anfragen zu vervollständigen.
{% endalert %}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   // You will need to include at least one of 'segment_id', 'external_user_ids', and 'audience'
   // Including 'segment_id' will send to members of that segment
   // Including 'external_user_ids' and/or 'user_aliases' will send to those users
   // Including both will send to the provided users if they are in the segment
   "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if no external_user_ids or aliases are provided,
   "external_user_ids": (optional, array of strings) see external user identifier,
   "user_aliases": (optional, array of user alias object) see user alias,
   "segment_id": (optional, string) see segment identifier,
   "audience": (optional, connected audience object) see connected audience,
   "campaign_id": (optional*, string) *required if you wish to track campaign stats (for example, sends, clicks, bounces, etc). see campaign identifier,
   "send_id": (optional, string) see send identifier,
   "override_frequency_capping": (optional, bool) ignore frequency_capping for campaigns, defaults to false,
   "recipient_subscription_state": (optional, string) use this to send messages to only users who have opted in ('opted_in'), only users who have subscribed or are opted in ('subscribed') or to all users, including unsubscribed users ('all'), the latter being useful for transactional email messaging. Defaults to 'subscribed',
   "messages": {
     "android_push": (optional, android push object),
     "apple_push": (optional, apple push object),
     "content_card": (optional, content card object),
     "email": (optional, email object),
     "kindle_push": (optional, kindle/fireOS push object),
     "web_push": (optional, web push object),
     "webhook": (optional, webhook object),
     "whats_app": (optional, WhatsApp object),
     "sms": (optional, SMS object)
   }
 }
```

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
|`broadcast`| Optional | Boolesch | Sie müssen `broadcast` auf true setzen, wenn Sie eine Nachricht an ein ganzes Segment senden, auf das eine Kampagne oder ein Canvas abzielt. Dieser Parameter ist standardmäßig auf false eingestellt (Stand: 31\. August 2017). <br><br> Wenn `broadcast` auf true gesetzt ist, kann eine `recipients` Liste nicht aufgenommen werden. Seien Sie jedoch vorsichtig, wenn Sie `broadcast: true` setzen, denn wenn Sie dieses Flag unbeabsichtigt setzen, kann dies dazu führen, dass Sie Ihre Nachricht an eine größere Zielgruppe als erwartet senden. |
|`external_user_ids` | Optional | String-Array | Siehe [externe Nutzer:in ID]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields). |
|`user_aliases`| Optional | Array von Nutzer:innen-Alias-Objekten| Siehe [Nutzer-Alias Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
|`segment_id `| Optional | String | Siehe [Bezeichner für Segmente]({{site.baseurl}}/api/identifier_types/). |
|`audience`| Optional | Verbundenes Objekt der Zielgruppe | Siehe [verbundene Zielgruppe]({{site.baseurl}}/api/objects_filters/connected_audience/). |
|`campaign_id`| Fakultativ* | String | Siehe [Bezeichner der Kampagne]({{site.baseurl}}/api/identifier_types/) für weitere Informationen. <br><br>\*Erforderlich, wenn Sie Statistiken zu Kampagnen (z.B. Sendungen, Klicks, Bounces usw.) auf dem Braze-Dashboard verfolgen möchten. |
|`send_id`| Optional | String | Siehe [Bezeichner senden]({{site.baseurl}}/api/identifier_types/) |
|`override_frequency_capping`| Optional | Boolesch | Ignorieren Sie `frequency_capping` für Kampagnen, standardmäßig ist `false` eingestellt. |
|`recipient_subscription_state`| Optional | String | Verwenden Sie diese Option, um Nachrichten nur an Nutzer:in (`opted_in`), nur an Nutzer:in (`subscribed`) oder an alle Nutzer:in zu senden, auch an abgemeldete Nutzer (`all`), die sich angemeldet haben. <br><br>Die Verwendung von `all` Nutzer:innen ist nützlich für Transaktions-E-Mails Messaging. Standardmäßig ist `subscribed` eingestellt. |
|`messages`| Optional | Messaging Objekte | Siehe [verfügbare Messaging-Objekte]({{site.baseurl}}/api/objects_filters/#messaging-objects). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/send' \
--data-raw '{
  "broadcast": "false",
  "external_user_ids": "external_user_identifiers",
  "user_aliases": {
    "alias_name": "example_name",
    "alias_label": "example_label"
  },
  "segment_id": "segment_identifier",
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
  "override_frequency_capping": "false",
  "recipient_subscription_state": "all",
  "messages": {
    "android_push": "(optional, Android Push Object)",
    "apple_push": "(optional, Apple Push Object)",
    "content_card": "(optional, Content Card Object)",
    "email": "(optional, Email Object)",
    "kindle_push": "(optional, Kindle/FireOS Push Object)",
    "web_push": "(optional, Web Push Object)"
  }
}'
```

## Details zur Antwort

Die Antworten des Endpunkts, der die Nachricht versendet, enthalten die `dispatch_id`, um auf den Versand der Nachricht zu referenzieren. Die `dispatch_id` ist die ID des Nachrichtenversands, d.h. die eindeutige ID für jede von Braze gesendete "Übertragung". Weitere Informationen finden Sie unter [Verhalten der Dispatch ID]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

{% endapi %}
