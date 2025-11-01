---
nav_title: "POST: Alterar o status da inscrição de e-mail"
article_title: "POST: Alterar o status da inscrição de e-mail"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Alterar o status da inscrição de e-mail do usuário\"."

---
{% api %}
# Alterar o status da inscrição de e-mail
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/email/status
{% endapimethod %}

> Use esse endpoint para definir o estado da inscrição de e-mail para seus usuários.

Os usuários podem ser `opted_in`, `unsubscribed`, ou `subscribed` (sem aceitação ou exclusão específica).

É possível definir o estado da inscrição de e-mail para um endereço de e-mail que ainda não esteja associado a nenhum de seus usuários no Braze. Quando esse endereço de e-mail for posteriormente associado a um usuário, o estado de inscrição de e-mail que você enviou ficará automaticamente definido.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#be852462-0cda-4a48-b68b-85bd8a9f2147 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `email.status`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corpo da solicitação

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@braze.com",
  "subscription_state": "subscribed"
}
```

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `email` | Obrigatória | String ou matriz | Envio de e-mail em string para modificar ou uma matriz de até 50 endereços de e-mail para modificar. |
| `subscription_state` | Obrigatória | String | Ou "subscribed" (inscrito), "unsubscribed" (cancelado inscrição) ou "opted_in". |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/status' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": "example@braze.com",
  "subscription_state": "subscribed"
}'
```


{% endapi %}
