---
nav_title: "OBTER: Veja as informações do modelo de e-mail"
article_title: "OBTER: Ver Informações do Modelo de E-mail"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Ver Informações do Modelo de E-mail\"."

---
{% api %}
# Veja as informações do modelo de e-mail
{% apimethod get %}
/templates/email/info
{% endapimethod %}

> Use este endpoint para obter informações sobre seus templates de e-mail.

{% alert important %}
Os modelos criados usando o editor de arrastar e soltar para e-mail não são aceitos.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e98d2d5b-62fe-4358-b391-9fe9e460d0ac {% endapiref %}

## Pré-requisitos
Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/api_key/) com a permissão `templates.email.info`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `email_template_id`  | Obrigatória | String | Veja [identificador de API de modelo de e-mail]({{site.baseurl}}/api/identifier_types/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/templates/email/info?email_template_id={{email_template_id}}' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```
{% endraw %}

## Resposta 

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

Imagens nesta resposta aparecerão na variável `body` como HTML.

{% endapi %}
