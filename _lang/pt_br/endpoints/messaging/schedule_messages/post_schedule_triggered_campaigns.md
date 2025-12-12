---
nav_title: "POST: Agende campanhas disparadas pela API"
article_title: "POST: Agendar campanhas disparadas por API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze para campanhas disparadas pela API \"Agendar campanhas disparadas por API\"."

---
{% api %}
# Agende campanhas disparadas pela API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/trigger/schedule/create
{% endapimethod %}

> Use esse endpoint para enviar mensagens de campanha criadas no painel por meio de entrega acionada pela API, permitindo que você decida qual ação deve disparar o envio da mensagem.

Você pode passar`trigger_properties`, que se tornará um modelo na própria mensagem.

Observe que, para enviar mensagens com esse endpoint, é necessário ter um [ID de campanha]({{site.baseurl}}/api/identifier_types/), criado quando você cria uma [campanha disparada pela API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b7e61de7-f2c2-49c9-9e46-b85a0aa01bba {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `campaigns.trigger.schedule.create`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' category='send messages endpoints' %}

## Corpo da solicitação

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "send_id": (optional, string) see send identifier,
  // Including 'recipients' will send only to the provided user ids if they are in the campaign's segment
  "recipients": (optional, array of recipients object),
  // for any keys that conflict between these trigger properties and those in a Recipients Object, the value from the Recipients Object will be used
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' will only send to users in the audience
  // If 'recipients' and 'audience' are not provided and broadcast is not set to 'false',
  // the message will send to entire segment targeted by the campaign
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" object is omitted,
  "trigger_properties": (optional, object) personalization key-value pairs for all users in this send; see trigger properties,
  "schedule": {
    "time": (required, datetime as ISO 8601 string) time to send the message,
    "in_local_time": (optional, bool),
    "at_optimal_time": (optional, bool),
  }
}
```
## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
|`campaign_id`|Obrigatória|String| Ver [identificador de campanha]({{site.baseurl}}/api/identifier_types/)|
| `send_id` | Opcional | String | Consulte [enviar identificador]({{site.baseurl}}/api/identifier_types/). |
| `recipients` | Opcional | Matriz de objetos de destinatários | Veja [objetos de destinatários]({{site.baseurl}}/api/objects_filters/recipient_object/). |
| `audience` | Opcional | Objeto de público conectado | Veja [público conectado]({{site.baseurl}}/api/objects_filters/connected_audience/). |
|`broadcast`| Opcional | Booleano | Você deve definir `broadcast` como verdadeiro ao enviar uma mensagem para um segmento inteiro que uma campanha ou canva segmenta. O padrão desse parâmetro é false (a partir de 31 de agosto de 2017). <br><br> Se `broadcast` estiver definido como true, uma lista `recipients` não poderá ser incluída. No entanto, tenha cuidado ao definir `broadcast: true`, pois definir esta flag de forma não intencional pode fazer com que você envie sua mensagem para um público maior do que o esperado. |
| `trigger_properties` | Opcional | Objeto | Pares de valores-chave de personalização para todos os usuários nesse envio. Consulte [propriedades de gatilho]({{site.baseurl}}/api/objects_filters/trigger_properties_object/). |
| `schedule` | Obrigatória | Objeto de agendamento | Veja [objeto de agendamento]({{site.baseurl}}/api/objects_filters/schedule_object/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "recipients": [
    {
      "user_alias": "example_alias",
      "external_user_id": "external_user_identifier",
      "trigger_properties": {}
    }
  ],
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "eye_color",
          "comparison": "equals",
          "value": "blue"
        }
      },
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_foods",
          "comparison": "includes_value",
          "value": "pizza"
        }
      },
      {
        "OR": [
          {
            "custom_attribute": {
              "custom_attribute_name": "last_purchase_time",
              "comparison": "less_than_x_days_ago",
              "value": 2
            }
          },
          {
            "push_subscription_status": {
              "comparison": "is",
              "value": "opted_in"
            }
          }
        ]
      },
      {
        "email_subscription_status": {
          "comparison": "is_not",
          "value": "subscribed"
        }
      },
      {
        "last_used_app": {
          "comparison": "after",
          "value": "2019-07-22T13:17:55+0000"
        }
      }
    ]
  },
  "broadcast": false,
  "trigger_properties": {},
  "schedule": {
    "time": "",
    "in_local_time": false,
    "at_optimal_time": false
  }
}'
```

## Resposta

### Exemplo de resposta bem-sucedida

```json
Content-Type: application/json
Authorization: Bearer YOUR-API-KEY-HERE
{
{
    "dispatch_id": "dispatch_identifier",
    "schedule_id": "schedule_identifier",
    "message": "success"
}
```

{% endapi %}
