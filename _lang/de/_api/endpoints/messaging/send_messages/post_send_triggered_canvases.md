---
nav_title: "POST: Senden von Canvas Nachrichten mit API-getriggerter Zustellung"
article_title: "POST: Senden von Canvas Nachrichten mit API-getriggerter Zustellung"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Canvase mit API-getriggerter Zustellung von Braze senden."

---
{% api %}
# Senden Sie Canvas Nachrichten mit API-getriggerter Zustellung
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/trigger/send
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um Canvas Nachrichten mit API-getriggerter Zustellung zu versenden.

Die API-getriggerte Zustellung ermöglicht es Ihnen, den Inhalt von Nachrichten im Braze-Dashboard zu speichern und gleichzeitig über Ihre API zu bestimmen, wann und an wen eine Nachricht gesendet wird.

Bevor Sie mit diesem Endpunkt Nachrichten versenden können, müssen Sie über eine [Canvas ID]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier) verfügen (die beim Erstellen eines Canvas erstellt wird).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c9a8a5fe-a101-4755-99f2-73aa8fc146fe {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, müssen Sie einen API-Schlüssel mit der Berechtigung `canvas.trigger.send` erstellen.

## Rate-Limits

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='message endpoints' %}

## Körper der Anfrage

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) see Canvas identifier,
  "canvas_entry_properties": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if `recipients` is omitted,
  "segment_id": (optional, string) see segment identifier,
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message will send to the entire segment targeted by the Canvas)
    [{
      // Either "external_user_id" or "user_alias" or "email" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "email": (optional, string) email address of user to receive message,
      "prioritization": (optional, array) prioritization array; required when using email,
      "canvas_entry_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent `canvas_entry_properties`)
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases
      "attributes": (optional, object) fields in the attributes object will create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values will be overwritten
    }],
    ...
}
```

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
|`canvas_id`| Erforderlich | String | Siehe [Canvas Bezeichner]({{site.baseurl}}/api/identifier_types/). |
|`canvas_entry_properties`| Optional | Objekt | Dazu gehören auch die [Eigenschaften von Canvas-Eingängen]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/). Die Schlüssel-Wert-Paare für die Personalisierung gelten für alle Nutzer:innen in dieser Anfrage. Das Objekt Canvas Eingang-Eigenschaften hat eine maximale Größe von 50 KB. <br><br>**Hinweis:** Wenn Sie am [Canvas-Kontext-Frühzugang]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/) teilnehmen, lautet dieser Parameter `context` und enthält die Eigenschaften des Canvas-Eingangs. |
|`broadcast`| Optional | Boolesch | Sie müssen `broadcast` auf true setzen, wenn Sie eine Nachricht an ein ganzes Segment senden, auf das eine Kampagne oder ein Canvas abzielt. Dieser Parameter ist standardmäßig auf false eingestellt (Stand: 31\. August 2017). <br><br> Wenn `broadcast` auf true gesetzt ist, kann eine `recipients` Liste nicht aufgenommen werden. Seien Sie jedoch vorsichtig, wenn Sie `broadcast: true` setzen, denn wenn Sie dieses Flag unbeabsichtigt setzen, kann dies dazu führen, dass Sie Ihre Nachricht an eine größere Zielgruppe als erwartet senden. |
|`segment_id `| Optional | String | Siehe [Bezeichner für Segmente]({{site.baseurl}}/api/identifier_types/). |
|`audience`| Optional| Verbundenes Objekt der Zielgruppe | Siehe [Verbundenes Publikum]({{site.baseurl}}/api/objects_filters/connected_audience/). |
|`recipients`| Optional | Array | Siehe [Objekt Empfänger:innen]({{site.baseurl}}/api/objects_filters/recipient_object/). <br><br>Falls nicht angegeben und `broadcast` auf true gesetzt ist, wird die Nachricht an das gesamte Segment, auf das das Canvas abzielt, gesendet.<br><br> Das Array `recipients` kann bis zu 50 Objekte enthalten, wobei jedes Objekt einen einzelnen String `external_user_id` und ein Objekt `canvas_entry_properties` enthält. Dieser Aufruf erfordert eine `external_user_id`, `user_alias` oder `email`. In der Anfrage darf nur eine Angabe gemacht werden. <br><br>Wenn `email` der Bezeichner ist, müssen Sie [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email) in das Empfänger:innen-Objekt aufnehmen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
Für den Parameter `recipients` gilt: Wenn `send_to_existing_only` `true` ist, sendet Braze die Nachricht nur an bestehende Nutzer:innen. Dieses Flag kann jedoch nicht mit Nutzer:innen verwendet werden. <br><br>Wenn `send_to_existing_only` `false` ist, muss ein Attribut-Objekt enthalten sein. Wenn `send_to_existing_only` `false` ist **und** ein Nutzer:innen mit der angegebenen `id` nicht existiert, erstellt Braze einen Nutzer:innen mit dieser ID und den Attributen, bevor die Nachricht gesendet wird.
{% endalert %}

Kund:innen, die die API für Server-zu-Server-Aufrufe verwenden, müssen möglicherweise die entsprechende API-URL zulassen, wenn sie sich hinter einer Firewall befinden.

{% alert note %}
Wenn Sie sowohl bestimmte Nutzer:innen in Ihrem API-Aufruf als auch ein Zielsegment im Dashboard angeben, wird die Nachricht speziell an die Nutzerprofile gesendet, die sowohl im API-Aufruf enthalten sind als auch für die Segmentierung in Frage kommen.
{% endalert %}

## Beispiel Anfrage
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "canvas_entry_properties": {"product_name" : "shoes", "product_price" : 79.99},
  "broadcast": false,
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
  "recipients": [
    {
      "user_alias": {
        "alias_name" : "example_name",
        "alias_label" : "example_label"
      },
      "external_user_id": "user_identifier",
      "send_to_existing_only": true,
      "attributes": {
          "first_name" : "Alex"
      }
    }
  ]
}'
```

## Details zur Antwort

Die Antworten des Endpunkts, der die Nachricht versendet, enthalten die `dispatch_id`, um auf den Versand der Nachricht zu referenzieren. Die `dispatch_id` ist die ID des Nachrichtenversands (eindeutige ID für jede von der Braze-Plattform gesendete "Übertragung"). Weitere Informationen finden Sie unter [Verhalten der Dispatch ID]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

### Beispiel für eine erfolgreiche Antwort

Der Status Code `201` könnte den folgenden Antwortkörper zurückgeben. Wenn das Canvas archiviert, angehalten oder pausiert wird, wird das Canvas nicht über diesen Endpunkt gesendet.

```
{
  "notice": "The Canvas is paused. Resume the Canvas to ensure trigger requests will take effect.",
  "dispatch_id": "example_dispatch_id",
  "message": "success"
}
```

Wenn Ihr Canvas archiviert ist, sehen Sie diese Nachricht `notice`: "Der Canvas ist archiviert. Heben Sie die Archivierung des Canvas auf, um sicherzustellen, dass die Anfragen zum Auslösen wirksam werden." Wenn Ihr Canvas nicht aktiv ist, sehen Sie diese Nachricht `notice`: "Der Canvas ist angehalten. Setzen Sie den Canvas fort, um sicherzustellen, dass die Anfragen zum Auslösen wirksam werden."

Wenn Ihre Anfrage auf einen schwerwiegenden Fehler stößt, finden Sie unter [Fehler und Antworten]({{site.baseurl}}/api/errors/#fatal-errors) den Fehlercode und die Beschreibung.

## Attribute Objekt für Canvas

Verwenden Sie das Messaging-Objekt `attributes`, um Attribute und Werte für einen Nutzer hinzuzufügen, zu erstellen oder zu aktualisieren, bevor Sie ihm über den Endpunkt `canvas/trigger/send` ein API-getriggertes Canvas senden. Dieser API-Aufruf verarbeitet das Objekt mit den Nutzer:in-Attributen, bevor es das Canvas verarbeitet und sendet. Dadurch wird das Risiko von Problemen, die durch [Race-Conditions]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/) verursacht werden, minimiert. Standardmäßig können Abo-Gruppen jedoch nicht auf diese Weise aktualisiert werden.

{% alert note %}
Sie suchen die Kampagnenversion dieses Endpunkts? Informieren Sie sich über den [Versand von Messaging-Kampagnen Nachrichten mit API-getriggerter Zustellung]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/).
{% endalert %}

{% endapi %}
