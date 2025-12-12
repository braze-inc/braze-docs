---
nav_title: "POST: Excluir telas programadas disparadas pela API"
article_title: "POST: Excluir telas programadas disparadas pela API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Excluir telas programadas disparadas pela API da Braze."

---
{% api %}
# Excluir telas programadas disparadas pela API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/trigger/schedule/delete
{% endapimethod %}

> O ponto de extremidade de exclusão de agendamento permite cancelar uma mensagem que você agendou anteriormente por meio de Canvas disparados pela API antes que ela seja enviada.

As mensagens programadas ou os disparos que forem excluídos muito perto ou durante o horário em que deveriam ser enviados serão atualizados com os melhores esforços, de modo que as exclusões de último segundo poderão ser aplicadas a todos, alguns ou nenhum dos usuários direcionados.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7d34037f-4bf2-4fab-bc9c-c972988051a7 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `canvas.trigger.schedule.delete`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corpo da solicitação

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) the Canvas identifier,
  "schedule_id": (required, string) the `schedule_id` to delete (obtained from the response to create schedule)
}
```

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `canvas_id`| Obrigatória | String | Consulte [Identificador do Canva]({{site.baseurl}}/api/identifier_types/). |
| `schedule_id` | Obrigatória | String | O endereço `schedule_id` a ser excluído (obtido da resposta à programação de criação). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


## Exemplo de solicitação
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "schedule_id": "schedule_identifier"
}'
```

{% endapi %}
