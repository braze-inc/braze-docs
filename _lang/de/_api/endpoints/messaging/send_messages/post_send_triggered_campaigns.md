---
nav_title: "POST: Kampagnen mit API-gesteuerter Zustellung versenden"
article_title: "POST: Kampagnen mit API-gesteuerter Zustellung versenden"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts Kampagnen senden mit API-gesteuerter Zustellung."

---
{% api %}
# Senden Sie Kampagnennachrichten mit API-gesteuerter Zustellung
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/trigger/send
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um sofortige, einmalige Nachrichten an bestimmte Benutzer zu senden, indem Sie den API-gesteuerten Versand verwenden.

Mit der API-gesteuerten Zustellung können Sie den Inhalt von Nachrichten innerhalb des Braze-Dashboards unterbringen und gleichzeitig über Ihre API bestimmen, wann und an wen eine Nachricht gesendet wird.

Wenn Sie auf ein Segment abzielen, wird ein Datensatz Ihrer Anfrage in der [Entwicklerkonsole](https://dashboard.braze.com/app_settings/developer_console/activitylog/) gespeichert. Um Nachrichten mit diesem Endpunkt zu versenden, müssen Sie eine [Kampagnen-ID](https://www.braze.com/docs/api/identifier_types/) erstellen, wenn Sie eine [API-ausgelöste Kampagne]({{site.baseurl}}/api/api_campaigns/) erstellen.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aef185ae-f591-452a-93a9-61d4bc023b05 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, müssen Sie einen API-Schlüssel mit der Berechtigung `campaigns.trigger.send` erstellen.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='message endpoints' %}

## Körper der Anfrage

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "send_id": (optional, string) see send identifier,
  "trigger_properties": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to `false`, message will send to the entire segment targeted by the campaign)
    [
      {
      // Either "external_user_id" or "user_alias" or "email" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "email": (optional, string) email address of user to receive message,
      "prioritization": (optional, array) prioritization array; required when using email,
      "trigger_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent trigger_properties),
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases; if set to `false`, an attributes object must also be included,
      "attributes": (optional, object) fields in the attributes object will create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values will be overwritten
    }
  ],
  "attachments": (optional, array) array of JSON objects that define the files you need attached, defined by "file_name" and "url",
    [
      {  
       "file_name": (required, string) the name of the file you want to attach to your email, excluding the extension (for example, ".pdf"). Attach files up to 2 MB. This is required if you use "attachments",
       "url": (required, string) the corresponding URL of the file you want to attach to your email. The file name's extension will be detected automatically from the URL defined, which should return the appropriate "Content-Type" as a response header. This is required if you use "attachments",
      }
    ]
}
```

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
| --------- | ---------| --------- | ----------- |
|`campaign_id`|Erforderlich|String|Siehe [Kennung der Kampagne]({{site.baseurl}}/api/identifier_types/). |
|`send_id`| Optional | String | Siehe [Kennung senden]({{site.baseurl}}/api/identifier_types/). |
|`trigger_properties`| Optional | Objekt | Siehe [Auslösereigenschaften]({{site.baseurl}}/api/objects_filters/trigger_properties_object/). Schlüssel-Wert-Paare für die Personalisierung, die für alle Benutzer in dieser Anfrage gelten sollen. |
|`broadcast`| Optional | Boolesche | Sie müssen `broadcast` auf true setzen, wenn Sie eine Nachricht an ein ganzes Segment senden, auf das eine Kampagne oder ein Canvas abzielt. Dieser Parameter ist standardmäßig auf false eingestellt (Stand: 31\. August 2017). <br><br> Wenn `broadcast` auf true gesetzt ist, kann eine `recipients` Liste nicht aufgenommen werden. Seien Sie jedoch vorsichtig, wenn Sie `broadcast: true` setzen, da das unbeabsichtigte Setzen dieser Markierung dazu führen kann, dass Sie Ihre Nachricht an ein größeres Publikum als erwartet senden. |
|`audience`| Optional | Verbundenes Publikumsobjekt| Siehe [angeschlossenes Publikum]({{site.baseurl}}/api/objects_filters/connected_audience/). |
|`recipients`| Optional | Array | Siehe [Empfängerobjekt]({{site.baseurl}}/api/objects_filters/recipient_object/).<br><br>Wenn `send_to_existing_only` `false` ist, muss ein Attributobjekt enthalten sein.<br><br>Wenn `recipients` nicht angegeben wird und `broadcast` auf true gesetzt ist, wird die Nachricht an das gesamte Zielsegment der Kampagne gesendet. |
|`attachments`| Optional | Array | Wenn `broadcast` auf true gesetzt ist, kann die Liste `attachments` nicht einbezogen werden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

- Das Empfänger-Array kann bis zu 50 Objekte enthalten, wobei jedes Objekt einen einzelnen `external_user_id` String und ein `trigger_properties` Objekt enthält.
- Wenn `send_to_existing_only` ist `true`, sendet Braze die Nachricht nur an bestehende Benutzer. Dieses Flag kann jedoch nicht mit Benutzer-Aliasnamen verwendet werden.
- Wenn `send_to_existing_only` `false` ist, muss ein Attribut angegeben werden. Braze erstellt einen Benutzer mit der Adresse `id` und den Attributen, bevor die Nachricht gesendet wird.

{% alert important %}
Die Angabe eines Empfängers über die E-Mail-Adresse ist derzeit in einer frühen Phase. Wenden Sie sich an Ihren Customer Success Manager, wenn Sie an diesem frühen Zugang interessiert sind.
{% endalert %}

Der Status der Abonnementgruppe eines Benutzers kann über den Parameter `subscription_groups` im `attributes` Objekt aktualisiert werden. Weitere Einzelheiten finden Sie unter [Objekt Benutzerattribute]({{site.baseurl}}/api/objects_filters/user_attributes_object).

## Beispiel Anfrage
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "trigger_properties": "",
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
      "external_user_id": "external_user_identifier",
      "trigger_properties": "",
      "send_to_existing_only": true,
      "attributes": {
        "first_name" : "Alex"
      }
    }
  ],
  "attachments": [
    {
      "file_name" : "YourFileName",
      "url" : "https://exampleurl.com/YourFileName.pdf"
    }
  ]
}'
```

## Antwort Details

Die Antworten des Endpunkts, der die Nachricht versendet, enthalten die Adresse `dispatch_id`, die als Referenz für den Versand der Nachricht dient. Die `dispatch_id` ist die ID des Nachrichtenversands, eine eindeutige ID für jede von Braze gesendete Übertragung. Wenn Sie diesen Endpunkt verwenden, erhalten Sie eine einzige `dispatch_id` für eine ganze Gruppe von Benutzern. Weitere Informationen zu `dispatch_id` finden Sie in unserer Dokumentation zum [Verhalten von Dispatch ID]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

Wenn Ihre Anfrage auf einen schwerwiegenden Fehler stößt, finden Sie unter [Fehler und Antworten]({{site.baseurl}}/api/errors/#fatal-errors) den Fehlercode und die Beschreibung.

## Attribute Objekt für Kampagnen

Braze verfügt über ein Messaging-Objekt namens `attributes`, mit dem Sie Attribute und Werte für einen Benutzer hinzufügen, erstellen oder aktualisieren können, bevor Sie ihm eine über die API ausgelöste Kampagne senden. Wenn Sie den Endpunkt `campaign/trigger/send` für diesen API-Aufruf verwenden, wird das Objekt mit den Benutzerattributen verarbeitet, bevor die Kampagne verarbeitet und gesendet wird. Dies hilft, das Risiko von Problemen zu minimieren, die durch [Rennbedingungen]({{site.baseurl}}/help/best_practices/race_conditions/) verursacht werden. Standardmäßig können Abonnementgruppen jedoch nicht auf diese Weise aktualisiert werden.

{% alert important %}
Suchen Sie die Canvas-Version dieses Endpunkts? Sehen Sie sich das [Versenden von Canvas-Nachrichten mit API-gesteuerter Zustellung]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#create-send-endpoint) an.
{% endalert %}

{% endapi %}
