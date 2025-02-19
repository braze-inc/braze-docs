---
nav_title: "GET: Verfügbare E-Mail-Vorlagen auflisten"
article_title: "GET: Verfügbare E-Mail-Vorlagen auflisten"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel enthält Details zu den in der Liste verfügbaren E-Mail-Vorlagen des Braze-Endpunkts."

---
{% api %}
# Verfügbare E-Mail-Vorlagen auflisten
{% apimethod get %}
/templates/email/list
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Liste der verfügbaren E-Mail-Vorlagen in Ihrem Braze-Konto zu erhalten.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#eec24bf4-a3f4-47cb-b4d8-bb8f03964cca {% endapiref %}

## Voraussetzungen
Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit der Berechtigung `templates.email.list`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
|---|---|---|---|
| `modified_after`  | Optional | Zeichenkette im [ISO-8601-Format](https://en.wikipedia.org/wiki/ISO_8601)  | Ruft nur Vorlagen ab, die zum oder nach dem angegebenen Zeitpunkt aktualisiert wurden. |
| `modified_before`  |  Optional | Zeichenkette im [ISO-8601-Format](https://en.wikipedia.org/wiki/ISO_8601)  | Rufen Sie nur Vorlagen ab, die zum oder vor dem angegebenen Zeitpunkt aktualisiert wurden. |
| `limit` | Optional | Positive Zahl | Maximale Anzahl der abzurufenden Vorlagen. Standardmäßig 100, wenn nicht angegeben, mit einem maximal zulässigen Wert von 1000. |
| `offset`  |  Optional | Positive Zahl | Anzahl der Vorlagen, die übersprungen werden sollen, bevor der Rest der Vorlagen, die den Suchkriterien entsprechen, zurückgegeben wird. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
```
curl --location --request GET 'https://rest.iad-01.braze.com/templates/email/list?modified_after=2020-01-01T01:01:01.000000&modified_before=2020-02-01T01:01:01.000000&limit=1&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Antwort 

{% alert important %}
Vorlagen, die mit dem Drag-and-Drop-Editor für E-Mails erstellt wurden, sind in dieser Antwort nicht enthalten.
{% endalert %}

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "count": the number of templates returned
  "templates": [template with the following properties]:
    "email_template_id": (string) your email template's API Identifier,
    "template_name": (string) the name of your email template,
    "created_at": (string) the time the email was created at in ISO 8601,
    "updated_at": (string) the time the email was updated in ISO 8601,
    "tags": (array of strings) tags appended to the template
}
```
{% endapi %}



