---
nav_title: "POST: [Nome do endpoint]"
article_title: "Exemplo de layout: POST: Rastreamento do usuário"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
excerpt_separator: ""

description: "Este artigo detalha o uso desse endpoint POST [nome do endpoint] da Braze."

noindex: true
#ATTENTION: remove noindex and this alert from template
---
{% api %}
# [Nome do endpoint]

{% apimethod post %}
/sms/invalid_phone_numbers/remove
{% endapimethod %}

<!--
This is the description of the endpoint. API descriptions usually start with "Use this endpoint to..."-->
Use esse endpoint para remover números telefônicos "inválidos" da lista de inválidos no Braze. Isso pode ser usado para revalidar números de telefone depois de terem sido marcados como inválidos.

<!-- Your postman link. Once you have published the endpoint to postman, you will be able get a direct link to the information in the postman docs to share here-->
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

## Limite de taxa

<!-- The rate limit of the endpoint. This pulls from /includes/rate_limits/ and displays specific endpoint limits based on the endpoint provided -->
{% multi_lang_include rate_limits.md endpoint='default' %}

## Corpo da solicitação

<!--This is where you can give more information about your endpoint request body. -->

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "phone_numbers": (required, array of string in e.164 format)
}
```

### Parâmetros de solicitação

<!--This is a place for you to describe additional details for the parameters in the request body.-->

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| ----------|-----------| ---------|------ |
| `phone_number` | Obrigatória | Matriz de strings no formato e.164  | Uma matriz de até 50 números telefônicos para modificar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação

<!--The following example demonstrates a request that will remove specific SMS numbers from Braze's invalid phone number list via the API:-->

```
curl --location --request POST 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "phone_numbers" : ["12183095514","14255551212"]
}'
```
{% endapi %}
