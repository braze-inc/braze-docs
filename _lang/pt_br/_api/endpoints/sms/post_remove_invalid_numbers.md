---
nav_title: "POST: Remover números de telefone inválidos"
article_title: "POST: Remover números de telefone inválidos"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Remover números de telefone inválidos da Braze."

---
{% api %}
# Remover números de telefone inválidos
{% apimethod post %}
/sms/invalid_phone_numbers/remove
{% endapimethod %}

> Use esse endpoint para remover números de telefone "inválidos" da nossa lista de inválidos.

Isso pode ser usado para revalidar números de telefone depois de terem sido marcados como inválidos.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#76495aac-8c2d-4e1a-8cac-12e3856ab1d3 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `sms.invalid_phone_numbers.remove`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corpo da solicitação

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "phone_numbers": (required, array of string in e.164 format)
}
```

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| ----------|-----------| ---------|------ |
| `phone_number` | Obrigatória | Matriz de strings no formato e.164  | Uma matriz de até 50 números telefônicos para modificar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação

```
curl --location --request POST 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "phone_numbers" : ["12183095514","14255551212"]
}'
```

{% endapi %}
