---
nav_title: "POST: Excluir envios de mensagens agendadas"
article_title: "POST: Excluir envios de mensagens programadas"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o o endpoint da Braze \"Excluir envios de mensagens programadas\"."

---
{% api %}
# Excluir envios de mensagens agendadas
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/messages/schedule/delete
{% endapimethod %}

> Use esse endpoint para cancelar uma mensagem que você programou anteriormente antes de ela ser enviada.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5e89355c-0a5d-4d8b-8d89-2fd99bac36b0 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `messages.schedule.delete`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corpo da solicitação

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "schedule_id": (required, string) the `schedule_id` to delete (obtained from the response to create schedule)
}
```

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `schedule_id` | Obrigatória | String | O endereço `schedule_id` a ser excluído (obtido da resposta à programação de criação). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "schedule_id": "schedule_identifier"
}'
```

{% endapi %}
