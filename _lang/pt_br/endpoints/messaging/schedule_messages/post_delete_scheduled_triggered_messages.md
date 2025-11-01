---
nav_title: "POST: Excluir campanhas programadas disparadas pela API"
article_title: "POST: Excluir campanhas programadas disparadas pela API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint da Braze \"Excluir campanhas programadas disparadas pela API\"."

---
{% api %}
# Excluir campanhas programadas disparadas pela API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/trigger/schedule/delete
{% endapimethod %}

> Use esse endpoint para cancelar uma mensagem do canva que você programou anteriormente via API - disparada antes de ser enviada.

As mensagens programadas ou os disparos que forem excluídos muito perto ou durante o horário em que deveriam ser enviados serão atualizados com os melhores esforços, de modo que as exclusões de último segundo poderão ser aplicadas a todos, alguns ou nenhum dos usuários direcionados.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7d34037f-4bf2-4fab-bc9c-c972988051a7 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `campaigns.trigger.schedule.delete`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corpo da solicitação

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) the campaign identifier,
  "schedule_id": (required, string) the `schedule_id` to delete (obtained from the response to create schedule)
}
```

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `campaign_id`| Obrigatória | String | Consulte [identificador de campanha]({{site.baseurl}}/api/identifier_types/). |
| `schedule_id` | Obrigatória | String | O endereço `schedule_id` a ser excluído (obtido da resposta à programação de criação). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


## Exemplo de solicitação
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "schedule_id": "schedule_identifier"
}'
```

{% endapi %}
