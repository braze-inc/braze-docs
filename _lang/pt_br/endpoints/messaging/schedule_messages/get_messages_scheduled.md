---
nav_title: "OBTER: Liste as próximas campanhas e telas programadas"
article_title: "OBTER: Listar as próximas campanhas e telas programadas"
search_tag: Endpoint
page_order: 0
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Listar as próximas campanhas e canvas programados da Braze"

---
{% api %}
# Liste as próximas campanhas e telas programadas
{% apimethod get %}
/messages/scheduled_broadcasts
{% endapimethod %}

> Use esse ponto de extremidade para retornar uma lista JSON de informações sobre campanhas agendadas e canvas de entrada entre agora e um `end_time` designado especificado na solicitação.

As mensagens diárias e recorrentes aparecerão apenas uma vez em sua próxima ocorrência. Os resultados retornados nesse endpoint incluem campanhas e Canvas criados e programados no dashboard do Braze.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6f623cc3-383b-4bf7-b14d-7c56fc5562f5 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `messages.schedule_broadcasts`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | -------- | --------- | ----------- |
| `end_time` | Obrigatória | String no formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)  | Data de ponta a ponta do intervalo para recuperar as próximas campanhas e telas programadas. Isso é tratado como meia-noite no horário UTC pela API. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação
```
curl --location --request GET 'https://rest.iad-01.braze.com/messages/scheduled_broadcasts?end_time=2018-09-01T00:00:00-04:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Resposta

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "scheduled_broadcasts": [
    {
      "name": (string) the name of the scheduled broadcast,
      "id": (stings) the Canvas or campaign identifier,
      "type": (string) the broadcast type either Canvas or Campaign,
      "tags": (array) an array of tag names formatted as strings,
      "next_send_time": (string) The next send time formatted in ISO 8601, may also include time zone if not local/intelligent delivery,
      "schedule_type": (string) The schedule type, either local_time_zones, intelligent_delivery or the name of your company's time zone,
    },
  ]
}
```

{% endapi %}
