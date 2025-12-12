---
nav_title: "POST: Atualizar telas programadas disparadas pela API"
article_title: "POST: Atualizar telas programadas disparadas pela API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint da Braze \"Atualizar canvas programados disparados pela API\""

---
{% api %}
# Atualizar telas programadas disparadas pela API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canva/trigger/schedule/update
{% endapimethod %}

> Use esse endpoint para atualizar as telas programadas disparadas pela API que foram criadas no dashboard.

Isso permite que você decida qual ação deve disparar a mensagem a ser enviada. Você pode passar o endereço `trigger_properties` que será modelado na própria mensagem.

Note que, para enviar mensagens com esse ponto de extremidade, você deve ter um ID do Canvas, criado quando você constrói um [Canvas]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier).

Qualquer programação substituirá completamente a que você forneceu na solicitação de criação de programação ou em solicitações anteriores de atualização de programação.
  - Por exemplo, se você originalmente forneceu `"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}` e, em sua atualização, forneceu `"schedule" : {"time" : "2015-02-20T14:14:47"}`, sua mensagem será enviada no horário fornecido em UTC, e não no fuso local do usuário.
  - Os disparos programados que forem atualizados muito perto ou durante o horário em que deveriam ser enviados serão atualizados com os melhores esforços, de modo que as alterações de último segundo poderão ser aplicadas a todos, alguns ou nenhum dos usuários direcionados.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8fdf158b-ce20-41d8-80e4-a9300a6706d4 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `canvas.trigger.schedule.update`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corpo da solicitação

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) see Canvas identifier,
  "schedule_id": (required, string) the `schedule_id` to update (obtained from the response to create schedule),
  "schedule": {
    // required, see create schedule documentation
  }
}
```

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
|`canvas_id`|Obrigatória|String| Consulte [Identificador do Canva]({{site.baseurl}}/api/identifier_types/). |
| `schedule_id` | Opcional | String | O endereço `schedule_id` a ser atualizado (obtido da resposta para criar cronograma). |
|`schedule` | Obrigatória | Objeto | Consulte [objeto de agendamento]({{site.baseurl}}/api/objects_filters/schedule_object/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "schedule_id": "schedule_identifier",
  "schedule": {
    "time": "2017-05-24T21:30:00Z",
    "in_local_time": true
  }
}'
```

{% endapi %}
