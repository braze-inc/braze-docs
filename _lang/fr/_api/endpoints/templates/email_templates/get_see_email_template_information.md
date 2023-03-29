---
nav_title: "GET : Voir les informations sur les modèles d’e-mail"
article_title: "GET : Voir les informations sur les modèles d’e-mail"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Afficher les modèles d’e-mail."

---
{% api %}
# Voir les informations sur les modèles d’e-mail
{% apimethod get %}
/templates/email/info
{% endapimethod %}

Utilisez cet endpoint pour obtenir des informations sur vos modèles d’e-mail.

{% alert important %}
Les modèles construits à l’aide de l’éditeur Drag & Drop ne sont pas acceptés
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e98d2d5b-62fe-4358-b391-9fe9e460d0ac {% endapiref %}

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `email_template_id`  | Requis | String | Voir [Identifiant API modèle e-mail]({{site.baseurl}}/api/identifier_types/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/templates/email/info?email_template_id={{email_template_id}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponse 

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "email_template_id": (string) your email template's API Identifier,
  "template_name": (string) the name of your email template,
  "description": (string) the email template description,
  "subject": (string) the email template subject line,
  "preheader": (optional, string) the email preheader used to generate previews in some clients),
  "body": (optional, string) the email template body that may include HTML,
  "plaintext_body": (optional, string) a plaintext version of the email template body,
  "should_inline_css": (optional, boolean) whether there is inline CSS in the body of the template - defaults to the css inlining value for the App Group,
  "tags": (string) tag names,
  "created_at": (string) the time the email was created at in ISO 8601,
  "updated_at": (string) the time the email was updated in ISO 8601
}
```

Les images de cette réponse apparaîtront dans la variable `body` sous forme HTML.

{% endapi %}
