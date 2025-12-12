---
nav_title: "POST: Envio de e-mails para listas de bloqueio"
article_title: "POST: Envio de e-mails para listas de bloqueio"
search_tag: Endpoint
page_order: 8
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o o endpoint da Braze \"Envio de e-mails para listas de bloqueio\"."

---
{% api %}
# Envio de e-mails para listas de bloqueio
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/email/blocklist
{% endapimethod %}

> Use esse endpoint para cancelar a inscrição de um usuário no e-mail e marcá-lo como hard bounce.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d51155a1-a6e8-4dcc-9f2b-88c54ab9e8c6 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `email.blacklist`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corpo da solicitação

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": ["blocklist_email1","blocklist_email2"]
}
```

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| -----------|----------| --------|------- |
| `email` | Obrigatória | String ou matriz | Envio de e-mail em string para a lista de bloqueio ou uma matriz de até 50 endereços de e-mail para a lista de bloqueio. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/blocklist' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": ["blocklist_email1","blocklist_email2"]
}'
```

{% endapi %}
