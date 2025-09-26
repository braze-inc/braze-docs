---
nav_title: "GET: Details zur Kampagne exportieren"
article_title: "GET: Details zur Kampagne exportieren"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Export von Kampagnendetails Braze."

---
{% api %}
# Details zur Kampagne exportieren
{% apimethod get %}
/kampagnen/details
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um relevante Informationen zu einer bestimmten Kampagne abzurufen, die durch den Bezeichner `campaign_id` identifiziert werden kann.

Wenn Sie Canvas-Daten abrufen möchten, referenzieren Sie auf den Endpunkt [Canvas-Details exportieren]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aad2a811-7237-43b1-9d64-32042eabecd9 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `campaigns.details`.

## Rate-Limits

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | -------- | --------- | ----------- |
| `campaign_id` | Erforderlich | String | Siehe [API-Bezeichner der Kampagne]({{site.baseurl}}/api/identifier_types/).<br><br> Die `campaign_id` für API-Kampagnen finden Sie auf der Seite [API-Schlüssel]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) und auf der Seite **Kampagnendetails** in Ihrem Dashboard; oder Sie können den [Endpunkt Liste der Kampagnen exportieren](#campaign-list-endpoint) verwenden. |
| `post_launch_draft_version` | Optional | Boolesch | Bei Nachrichten, die einen Entwurf nach dem Start haben, zeigt die Einstellung `true` alle verfügbaren Entwürfe an. Standardmäßig ist `false` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/campaigns/details?campaign_id={{campaign_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Antworten

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "created_at" : (string) the date created as ISO 8601 date,
    "updated_at" : (string) the date last updated as ISO 8601 date,
    "archived": (boolean) whether this campaign is archived,
    "draft": (boolean) whether this campaign is a draft,
    "enabled": (boolean) whether this campaign is active or not,
    "has_post_launch_draft": (boolean) whether this campaign has a post-launch draft,
    "name" : (string) the campaign name,
    "description" : (string) the campaign description,
    "schedule_type" : (string) the type of scheduling action,
    "channels" : (array) the list of channels to send via,
    "first_sent" : (string) the date and hour of first sent as ISO 8601 date,
    "last_sent" : (string) the date and hour of last sent as ISO 8601 date,
    "tags" : (array) the tag names associated with the campaign,
    "teams" : (array) the names of the Teams associated with the campaign,
    "messages": {
        "message_variation_id": (string) { // <=This is the actual id
            "channel": (string) the channel type of the message, must be either email, ios_push, webhook, content_card, in-app_message, or sms,
            "name": (string) the name of the message in the dashboard (eg., "Variation 1")
            ... channel-specific fields for this message, see the following messages section ...
        }
    },
    "conversion_behaviors": (array) the conversion event behaviors assigned to the campaign, see the following conversions behavior section.
}
```

### Nachrichten nach Kanal

Die Antwort `messages` enthält Informationen zu jeder Nachricht. Im Folgenden finden Sie Beispielantworten auf Nachrichten für die einzelnen Kanäle:

#### Push

```json
{
    "channel": (string) the description of the channel, such as "ios_push" or "android_push",
    "name": (string) the name of the variant,
    "alert": (string) the alert body text,
    "extras": (hash) any key-value pairs provided,
    "title": (string) the alert title text,
    "action": (string) action link from click
}
```

#### E-Mail

```json
{
    "channel": "email",
    "name": (string) the name of the variant,
    "extras": (array) the email extras,
    "subject": (string) the subject,
    "body": (string) the HTML body,
    "from": (string) the from address and display name,
    "reply_to": (string) the reply-to for message, if different than "from" address,
    "title": (string) the name of the email,
    "amp_body": (string) the AMP HTML body,
    "preheader": (string) the preheader,
    "custom_plain_text": (string) the custom plain text,
    "should_inline_css": (boolean) whether there should be inline CSS,
    "should_whitespace_header": (boolean) whether there should be a whitespace header,
    "email_headers": (array) list of email headers
}
```

#### In-App-Nachrichten

```json
{
    "type": (string) the description of in-app message type, such as "survey",
    "data": {
        "pages": [
            {
                "header":
                    {
                         "text":(string) the display text for the header of the survey,
                    }
                "choices": [
                    {
                       "choice_id": (string) the choice identifier,
                       "text": (string) the display text,
                       "custom_attribute_key": (string) the custom attribute key,
                       "custom_attribute_value": (sting) the custom attribute value,
                       "deleted": (boolean) deleted from live campaign,
                    },
                    ...
                ]
            }
        ]
    }
}
```

#### Content-Cards

```json
{
    "channel": "content_cards",
    "name": (string) the name of variant,
    "extras": (hash) any key-value pairs provided; only present if at least one key-value pair has been set
}
```

#### Webhook

```json
{
    "channel": "webhook",
    "url": (string) the URL for webhook,
    "body": (string) the payload body,
    "type": (string) the body content type,
    "headers": (hash) the specified request headers,
    "method": (string) the HTTP method, either POST or GET
}
```

#### SMS

```json
{
  "channel": "sms",
  "body": (string) the payload body,
  "from": (string) the list of numbers associated with the subscription group,
  "subscription_group_id": (string) the API id of the subscription group targeted in the SMS message
}
```

#### WhatsApp

##### Template Nachrichten

```json
{
  "channel": "whats_app",
  "subscription_group_id": (string) the API ID of the subscription group selected in the WhatsApp message
  "from": (array) the list of strings of the numbers associated with the subscription group,
  "template_name": (string) the name of the WhatsApp template being sent,
  "template_language_code": (string) the language code of the WhatsApp template being sent,
  "header_variables": (array) the list of strings, if present, of Liquid variables being inserted into header of WhatsApp template being sent,
  "body_variables": (array) the list of strings, if present, of Liquid variables being inserted into body of WhatsApp template being sent,
  "button_variables": (array) the list of strings, if present, of Liquid variables being inserted into buttons of WhatsApp template being sent
}
```

##### Responsive Nachrichten

```json
{
  "channel": "whats_app",
  "subscription_group_id": (string) the API ID of the subscription group selected in the WhatsApp message,
  "from": (array) list of strings of the numbers associated with the subscription group,
  "layout": (string) the name of the WhatsApp template being sent (text or media or quick-reply),
  "header_text": (string, optional) the text, if present, of the header of the message being sent,
  "body_text": (string, optional) the text, if present, of the body of the message being sent,
  "footer_text": (string, optional) the text, if present, of the footer of the message being sent,
  "buttons": (array) list of button objects in the message being sent ({"text": (string) the text of the button})
}
```

#### Nachrichten kontrollieren

```json
{
    "channel": (string) the description of the channel that the control is for,
    "type": "control"
}
```

### Verhalten bei Konversion

Das Array `conversion_behaviors` enthält Informationen über jedes Konversions-Event-Verhalten, das für die Kampagne festgelegt wurde. Diese Verhaltensweisen sind in der von der Kampagne vorgegebenen Reihenfolge. Zum Beispiel wird Konversions-Event A der erste Artikel im Array sein, Konversions-Event B der zweite usw. Im Folgenden finden Sie Beispiele für das Verhalten bei Konversions-Events:

#### Klicks auf E-Mail

```json
{
    "type": "Clicks Email",
    "window": (integer) the number of seconds during which the user can convert on this event, such as 86400, which is 24 hours
}
```

#### Öffnet eine E-Mail

```json
{
    "type": "Opens Email",
    "window": (integer) the number of seconds during which the user can convert on this event, such as 86400, which is 24 hours
}
```

#### Tätigt einen Kauf (egal welchen)

```json
{
    "type": "Makes Any Purchase",
    "window": (integer) the number of seconds during which the user can convert on this event, such as 86400, which is 24 hours
}
```

#### Tätigt einen Kauf (bestimmtes Produkt)

```json
{
    "type": "Makes Specific Purchase",
    "window": (integer) the number of seconds during which the user can convert on this event, such as 86400, which is 24 hours,
    "product": (string) the name of the product, such as "Feline Body Armor"
}
```

#### Führt angepasste Events durch

```json
{
    "type": "Performs Custom Event",
    "window": (integer) the number of seconds during which the user can convert on this event, such as 86400, which is 24 hours,
    "custom_event_name": (string) the name of the event, such as "Used Feline Body Armor"
}
```

#### Upgraden Sie die App

```json
{
    "type": "Upgrades App",
    "window": (integer) the number of seconds during which the user can convert on this event, such as 86400, which is 24 hours,
    "app_ids": (array or null) array of app ids, such as ["12345", "67890"], or `null` if "Track sessions for any app" is selected in the UI
}
```

#### Nutzt die App

```json
{
    "type": "Starts Session",
    "window": (integer) the number of seconds during which the user can convert on this event, such as 86400, which is 24 hours,
    "app_ids": (array or null) array of app ids, such as ["12345", "67890"], or `null` if "Track sessions for any app" is selected in the UI
}
```

{% alert tip %}
Hilfe zu CSV- und API-Exporten finden Sie unter [Fehlerbehebung bei Exporten]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
