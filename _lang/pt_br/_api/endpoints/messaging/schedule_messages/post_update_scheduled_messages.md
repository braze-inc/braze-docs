---
nav_title: "POST: Atualizar envios de mensagens programadas"
article_title: "POST: Atualizar envios de mensagens programadas"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint da Braze para atualização de mensagens agendadas."

---
{% api %}
# Atualizar envios de mensagens programadas
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/messages/schedule/update
{% endapimethod %}

> Use esse endpoint para atualizar os envios de mensagens programadas.

Esse endpoint aceita atualizações do parâmetro `schedule` ou `messages` ou de ambos. Sua solicitação deve conter pelo menos uma dessas duas chaves.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f61edf74-4467-4551-b9c4-a4b8d188cd7a {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `messages.schedule.update`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corpo da solicitação

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "schedule_id": (required, string) the `schedule_id` to update (obtained from the response to create schedule),
  "schedule": {
    // optional, see create schedule documentation
  },
  "messages": {
    // optional, see available messaging objects documentation
  }
}
```
## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `schedule_id` | Obrigatória | String | O endereço `schedule_id` a ser atualizado (obtido da resposta para criar cronograma). |
|`schedule` | Opcional | Objeto | Consulte [objeto de agendamento]({{site.baseurl}}/api/objects_filters/schedule_object/). |
|`messages` | Opcional | Objeto | Consulte os [objetos de envio de mensagens disponíveis]({{site.baseurl}}/api/objects_filters/#messaging-objects). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "schedule_id": "schedule_identifier",
  "schedule": {
    "time": "2017-05-24T20:30:36Z"
   },
  "messages": {
    "apple_push": {
      "alert": "Updated Message!",
      "badge": 1
    },
    "android_push": {
      "title": "Updated title!",
      "alert": "Updated message!"
    },
    "sms": {  
      "subscription_group_id": "subscription_group_identifier",
      "message_variation_id": "message_variation_identifier",
      "body": "This is my SMS body.",
      "app_id": "app_identifier"
    }
  }
}'
```

{% endapi %}
