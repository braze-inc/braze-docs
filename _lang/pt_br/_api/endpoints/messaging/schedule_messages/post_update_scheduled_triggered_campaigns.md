---
nav_title: "POST: Atualizar campanhas programadas disparadas pela API"
article_title: "POST: Atualizar campanhas agendadas disparadas por API"
search_tag: Endpoint
page_order: 4
layout: api_page
description: "Este artigo descreve os detalhes sobre o endpoint da Braze \"Atualizar campanhas agendadas disparadas por API\""

---
{% api %}
# Atualizar campanhas programadas disparadas pela API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/trigger/schedule/update
{% endapimethod %}

> Use esse endpoint para atualizar campanhas programadas acionadas por API criadas no dashboard, permitindo que você decida qual ação deve disparar a mensagem a ser enviada.

Você pode passar `trigger_properties` que os templates do Braze para a mensagem em si.

Observe que, para enviar mensagens com esse ponto de extremidade, você deve ter um ID de campanha, criado ao criar uma [campanha disparada por API]({{site.baseurl}}/api/api_campaigns/).

Qualquer programação sobrescreve completamente a que você forneceu na solicitação de criação de programação ou nas solicitações de atualização de programação anteriores. Por exemplo, se você originalmente definiu a programação para `"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}` e depois a atualiza para `"schedule" : {"time" : "2015-02-20T14:14:47"}`, o Braze envia a mensagem no horário especificado em UTC, não no horário local do usuário.

Os gatilhos programados que são atualizados perto ou durante o horário em que deveriam ser enviados são atualizados com o melhor esforço para que o Braze possa aplicar mudanças de última hora a todos, alguns ou nenhum dos seus usuários-alvo. As atualizações não são aplicadas se a programação original usou o horário local e o horário original já passou em qualquer fuso horário.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6d2a6e66-9d6f-4ae1-965a-79fa52b86b1d {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `campaigns.trigger.schedule.update`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corpo da solicitação

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "schedule_id": (required, string) the `schedule_id` to update (obtained from the response to create schedule),
  "schedule": {
    // required, see create schedule documentation
  }
}
```

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
|`campaign_id`|Obrigatória|String| Ver [identificador de campanha]({{site.baseurl}}/api/identifier_types/)|
| `schedule_id` | Obrigatória | String | O endereço `schedule_id` a ser atualizado (obtido da resposta para criar uma agenda). |
|`schedule` | Obrigatória | Objeto | Consulte [objeto de agendamento]({{site.baseurl}}/api/objects_filters/schedule_object/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "schedule_id": "schedule_identifier",
  "schedule": {
    "time": "2017-05-24T21:30:00Z",
    "in_local_time": true
  }
}'
```

{% endapi %}
