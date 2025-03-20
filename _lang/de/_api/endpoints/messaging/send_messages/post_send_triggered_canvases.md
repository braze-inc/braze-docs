---
nav_title: "POST: Senden von Canvas-Nachrichten mit API-gesteuerter Zustellung"
article_title: "POST: Senden von Canvas-Nachrichten mit API-gesteuerter Zustellung"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts Canvases senden mit API-gesteuerter Zustellung."

---
{% api %}
# Senden Sie Canvas-Nachrichten mit API-gesteuerter Zustellung
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/trigger/send
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um Canvas-Nachrichten mit API-gesteuerter Zustellung zu versenden.

Mit der API-gesteuerten Zustellung können Sie den Inhalt von Nachrichten im Braze-Dashboard speichern und über Ihre API bestimmen, wann und an wen eine Nachricht gesendet wird.

Bevor Sie mit diesem Endpunkt Nachrichten senden können, müssen Sie eine [Canvas-ID]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier) haben (die erstellt wird, wenn Sie ein Canvas erstellen).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c9a8a5fe-a101-4755-99f2-73aa8fc146fe {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, müssen Sie einen API-Schlüssel mit der Berechtigung `canvas.trigger.send` erstellen.

## Preisgrenze

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

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
| --------- | ---------| --------- | ----------- |
|`canvas_id`| Erforderlich | String | Siehe [Canvas-Kennung]({{site.baseurl}}/api/identifier_types/). |
|`canvas_entry_properties`| Optional | Objekt | Siehe [Eigenschaften von Canvas-Einträgen]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/). Die Schlüssel-Wert-Paare für die Personalisierung gelten für alle Benutzer in dieser Anfrage. Das Objekt Canvas entry properties hat eine maximale Größe von 50 KB. |
|`broadcast`| Optional | Boolesche | Sie müssen `broadcast` auf true setzen, wenn Sie eine Nachricht an ein ganzes Segment senden, auf das eine Kampagne oder ein Canvas abzielt. Dieser Parameter ist standardmäßig auf false eingestellt (Stand: 31\. August 2017). <br><br> Wenn `broadcast` auf true gesetzt ist, kann eine `recipients` Liste nicht aufgenommen werden. Seien Sie jedoch vorsichtig, wenn Sie `broadcast: true` setzen, da das unbeabsichtigte Setzen dieser Markierung dazu führen kann, dass Sie Ihre Nachricht an ein größeres Publikum als erwartet senden. |
|`audience`| Optional| Verbundenes Publikumsobjekt | Siehe [Vernetztes Publikum]({{site.baseurl}}/api/objects_filters/connected_audience/). |
|`recipients`| Optional | Array | Siehe [Objekt Recipients]({{site.baseurl}}/api/objects_filters/recipient_object/). Wenn keine Angaben gemacht werden und `broadcast` auf true gesetzt ist, wird die Nachricht an das gesamte Segment gesendet, auf das der Canvas abzielt.<br><br> Das Array `recipients` kann bis zu 50 Objekte enthalten, wobei jedes Objekt einen einzelnen String `external_user_id` und ein Objekt `canvas_entry_properties` enthält. Entweder `external_user_id` oder `user_alias` ist für diesen Anruf erforderlich. In der Anfrage darf nur eine Option angegeben werden. <br><br> Wenn `send_to_existing_only` auf `true` gesetzt ist, sendet Braze die Nachricht nur an bestehende Benutzer - dieses Flag kann jedoch nicht mit Benutzer-Alias verwendet werden. Wenn `send_to_existing_only` `false` ist und ein Benutzer mit der angegebenen `id` nicht existiert, erstellt Braze einen Benutzer mit dieser ID und den entsprechenden Attributen, bevor die Nachricht gesendet wird.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Kunden, die die API für Server-zu-Server-Aufrufe verwenden, müssen möglicherweise die entsprechende API-URL zulassen, wenn sie sich hinter einer Firewall befinden.

{% alert important %}
Die Angabe eines Empfängers über die E-Mail-Adresse ist derzeit in einer frühen Phase. Wenden Sie sich an Ihren Customer Success Manager, wenn Sie an diesem frühen Zugang interessiert sind.
{% endalert %}

{% alert note %}
Wenn Sie sowohl bestimmte Benutzer in Ihrem API-Aufruf als auch ein Zielsegment im Dashboard angeben, wird die Nachricht speziell an die Benutzerprofile gesendet, die sowohl im API-Aufruf enthalten sind als auch für die Segmentfilter in Frage kommen.
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

## Antwort Details

Die Antworten des Endpunkts, der die Nachricht versendet, enthalten die Adresse `dispatch_id`, die als Referenz für den Versand der Nachricht dient. Die `dispatch_id` ist die ID des Nachrichtenversands (eindeutige ID für jede "Übertragung", die von der Braze-Plattform gesendet wird). Weitere Informationen finden Sie unter [Dispatch ID Verhalten]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

### Beispiel für eine erfolgreiche Antwort

Der Statuscode `201` könnte den folgenden Antwortkörper zurückgeben. Wenn das Canvas archiviert, angehalten oder pausiert wird, wird das Canvas nicht über diesen Endpunkt gesendet.

```
{
  "notice": "The Canvas is paused. Resume the Canvas to ensure trigger requests will take effect.",
  "dispatch_id": "example_dispatch_id",
  "message": "success"
}
```

Wenn Ihr Canvas archiviert ist, sehen Sie diese Meldung `notice`: "Der Canvas ist archiviert. Heben Sie die Archivierung des Canvas auf, um sicherzustellen, dass die Auslöseranforderungen wirksam werden." Wenn Ihr Canvas nicht aktiv ist, sehen Sie diese Meldung `notice`: "Der Canvas ist angehalten. Setzen Sie den Canvas fort, um sicherzustellen, dass die Auslöseranfragen wirksam werden."

Wenn Ihre Anfrage auf einen schwerwiegenden Fehler stößt, finden Sie unter [Fehler und Antworten]({{site.baseurl}}/api/errors/#fatal-errors) den Fehlercode und die Beschreibung.

## Attribute Objekt für Canvas

Verwenden Sie das Messaging-Objekt `attributes`, um Attribute und Werte für einen Benutzer hinzuzufügen, zu erstellen oder zu aktualisieren, bevor Sie ihm über den Endpunkt `canvas/trigger/send` ein durch die API ausgelöstes Canvas senden. Dieser API-Aufruf verarbeitet das Objekt mit den Benutzerattributen, bevor es die Leinwand verarbeitet und sendet. Dies hilft, das Risiko von Problemen zu minimieren, die durch [Race Conditions]({{site.baseurl}}/help/best_practices/race_conditions/) verursacht werden. Standardmäßig können Abonnementgruppen jedoch nicht auf diese Weise aktualisiert werden.

{% alert note %}
Sie suchen die Kampagnenversion dieses Endpunkts? Sehen Sie sich das [Versenden von Kampagnennachrichten mit API-gesteuerter Zustellung]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) an.
{% endalert %}

{% endapi %}
