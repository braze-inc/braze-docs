---
nav_title: "POST: Nachrichten sofort nur über die API senden"
article_title: "POST: Nachrichten sofort nur über die API senden"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts „Nachrichten sofort nur über die API senden"."

---
{% api %}
# Nachrichten sofort nur über die API senden
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/messages/send
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um über die Braze API sofortige Nachrichten an bestimmte Nutzer:innen zu senden.

Wenn Sie ein Segment als Zielgruppe verwenden, wird ein Datensatz Ihrer Anfrage in der [Entwicklungskonsole](https://dashboard.braze.com/app_settings/developer_console/activitylog/) gespeichert.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#946cb701-96e3-48d7-868c-f079785b6d24 {% endapiref %}

{% multi_lang_include api/payload_size_alert.md %}

{% alert important %}
Bei der Verwendung dieses Endpunkts für API-Kampagnen muss die Empfängerin bzw. der Empfänger bereits in Braze vorhanden sein, damit die Anfrage erfolgreich ist. Dies gilt bei der Angabe von Nutzer:innen in den Parametern `external_user_ids` oder `user_aliases`.
{% endalert %}

### Neue Nutzer:innen mit API-Sends erstellen

Wenn Sie im Rahmen eines API-Sends eine Nutzer:in erstellen müssen, stehen Ihnen zwei Optionen zur Verfügung:

#### Option 1: `/users/track` verwenden und anschließend senden

Erstellen Sie zunächst die Nutzer:in über den [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)-Endpunkt und warten Sie anschließend, bis die Daten übertragen wurden (in der Regel werden einige Minuten empfohlen), bevor Sie den API-only-Sendvorgang starten. Beachten Sie, dass Braze keine Garantie für die Datenverarbeitungszeiten bei `/users/track` übernimmt. Daher kann es zu [Race-Conditions]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions) kommen, wenn zwischen diesen Aufrufen nicht genügend Zeit eingeplant wird.

#### Option 2: Eine API-getriggerte Kampagne oder einen Canvas verwenden

Verwenden Sie eine [API-getriggerte Kampagne]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) oder einen [Canvas]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)-Workflow. Hiermit können Sie eine Empfänger:in anlegen, falls noch keine vorhanden ist. Diese Option vereinfacht Ihre Backend-Prozesse, erfordert jedoch die Konfiguration einer Kampagne oder eines Canvas im Braze-Dashboard.


## Voraussetzungen

Um diesen Endpunkt zu verwenden, müssen Sie einen API-Schlüssel mit der Berechtigung `messages.send` generieren.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='message send endpoint' %}

## Anfragetext

{% alert tip %}
Achten Sie darauf, [Messaging-Objekte]({{site.baseurl}}/api/objects_filters/#messaging-objects) in Ihren Anfragetext aufzunehmen, um Ihre Anfragen zu vervollständigen.
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

## Anfrageparameter

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
|`broadcast`| Optional | Boolescher Wert | Sie müssen `broadcast` auf true setzen, wenn Sie eine Nachricht an ein ganzes Segment senden, auf das eine Kampagne oder ein Canvas abzielt. Dieser Parameter ist standardmäßig auf false eingestellt (Stand: 31. August 2017). <br><br> Wenn `broadcast` auf true gesetzt ist, kann keine `recipients`-Liste angegeben werden. Seien Sie jedoch vorsichtig beim Setzen von `broadcast: true`, da ein unbeabsichtigtes Setzen dieses Flags dazu führen kann, dass Ihre Nachricht an eine größere Zielgruppe als erwartet gesendet wird. |
|`external_user_ids` | Optional | String-Array | Siehe [externe Nutzer-ID]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields). |
|`user_aliases`| Optional | Array von Nutzer-Alias-Objekten | Siehe [Nutzer-Alias-Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
|`segment_id `| Optional | String | Siehe [Segment-Bezeichner]({{site.baseurl}}/api/identifier_types/#segment-identifier). |
|`audience`| Optional | Verbundenes Zielgruppen-Objekt | Siehe [verbundene Zielgruppe]({{site.baseurl}}/api/objects_filters/connected_audience/). |
|`campaign_id`| Optional* | String | Siehe [Kampagnen-Bezeichner]({{site.baseurl}}/api/identifier_types/#campaign-identifier/) für weitere Informationen. <br><br>*Erforderlich, wenn Sie Kampagnen-Metriken (wie _Sendungen_, _Klicks_ oder _Absprünge_) im Braze-Dashboard verfolgen möchten oder wenn Sie Ereignisse zu dieser Nachricht im Tab [Nachrichtenverlauf]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#messaging-history-tab) des Nutzerprofils sehen möchten. |
|`send_id`| Optional | String | Siehe [Send-Bezeichner]({{site.baseurl}}/api/identifier_types/#send-identifier). |
|`override_frequency_capping`| Optional | Boolescher Wert | `frequency_capping` für Kampagnen ignorieren, standardmäßig `false`. |
|`recipient_subscription_state`| Optional | String | Verwenden Sie diesen Parameter, um Nachrichten nur an Nutzer:innen zu senden, die sich angemeldet haben (`opted_in`), nur an Nutzer:innen, die abonniert oder angemeldet sind (`subscribed`), oder an alle Nutzer:innen, einschließlich abgemeldeter Nutzer:innen (`all`). <br><br>Die Verwendung von `all` ist nützlich für Transaktions-E-Mails. Standardmäßig ist `subscribed` eingestellt. |
|`messages`| Optional | Messaging-Objekte | Siehe [verfügbare Messaging-Objekte]({{site.baseurl}}/api/objects_filters/#messaging-objects). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispielanfrage
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

## Antwortdetails

Die Antworten des Endpunkts zum Nachrichtenversand enthalten die `dispatch_id` als Referenz auf den Versand der Nachricht. Die `dispatch_id` ist die ID des Nachrichtenversands, also die eindeutige ID für jede von Braze gesendete „Übertragung". Weitere Informationen finden Sie unter [Verhalten der Dispatch-ID]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

{% endapi %}