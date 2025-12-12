---
nav_title: "OBTER: Lista de modelos de e-mail disponíveis"
article_title: "OBTER: Lista de modelos de e-mail disponíveis"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre a lista de modelos de e-mail disponíveis no endpoint da Braze."

---
{% api %}
# Lista de modelos de e-mail disponíveis
{% apimethod get %}
/templates/email/list
{% endapimethod %}

> Use esse endpoint para obter uma lista de modelos de e-mail disponíveis em sua conta Braze.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#eec24bf4-a3f4-47cb-b4d8-bb8f03964cca {% endapiref %}

## Pré-requisitos
Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/api_key/) com a permissão `templates.email.list`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `modified_after`  | Opcional | String no formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)  | Recupera apenas modelos atualizados no momento ou após o momento determinado. |
| `modified_before`  |  Opcional | String no formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)  | Recupera apenas modelos atualizados no momento ou antes do momento determinado. |
| `limit` | Opcional | Número positivo | Número máximo de modelos a serem recuperados. O padrão é 100 se não for fornecido, com um valor máximo aceitável de 1000. |
| `offset`  |  Opcional | Número positivo | Número de modelos a serem ignorados antes de retornar o restante dos modelos que atendem aos critérios de pesquisa. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação
```
curl --location --request GET 'https://rest.iad-01.braze.com/templates/email/list?modified_after=2020-01-01T01:01:01.000000&modified_before=2020-02-01T01:01:01.000000&limit=1&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Resposta 

{% alert important %}
Os modelos criados usando o editor de arrastar e soltar para e-mail não são fornecidos nesta resposta.
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



