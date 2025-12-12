---
nav_title: "GET: Siehe Informationen zur E-Mail-Vorlage"
article_title: "GET: Siehe E-Mail Template Informationen"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts E-Mail Template Braze sehen."

---
{% api %}
# Siehe Informationen zur E-Mail-Vorlage
{% apimethod get %}
/templates/email/info
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um Informationen über Ihre E-Mail Templates zu erhalten.

{% alert important %}
Templates, die mit dem Drag-and-Drop-Editor für E-Mails erstellt wurden, werden nicht akzeptiert.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e98d2d5b-62fe-4358-b391-9fe9e460d0ac {% endapiref %}

## Voraussetzungen
Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit der Berechtigung `templates.email.info`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `email_template_id`  | Erforderlich | String | Siehe [E-Mail Template API Bezeichner]({{site.baseurl}}/api/identifier_types/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/templates/email/info?email_template_id={{email_template_id}}' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```
{% endraw %}

## Antwort 

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "email_template_id": (string) Your email template's API Identifier,
  "template_name": (string) The name of your email template,
  "description": (string) The email template description,
  "subject": (string) The email template subject line,
  "preheader": (optional, string) The email preheader used to generate previews in some clients),
  "body": (optional, string) The email template body that may include HTML,
  "plaintext_body": (optional, string) A plaintext version of the email template body,
  "should_inline_css": (optional, boolean) Whether there is inline CSS in the body of the template - defaults to the css inlining value for the workspace,
  "tags": (string) Tag names,
  "created_at": (string) The time the email was created at in ISO 8601,
  "updated_at": (string) The time the email was updated in ISO 8601
}
```

Die Bilder in dieser Antwort werden in der Variable `body` als HTML angezeigt.

{% endapi %}
