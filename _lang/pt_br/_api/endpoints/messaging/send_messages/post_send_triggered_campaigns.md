---
nav_title: "POST: Envie campanhas usando entrega acionada por API"
article_title: "POST: Enviar campanhas usando a entrega disparada por API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint do Braze Enviar campanhas usando entrega disparada por API."

---
{% api %}
# Envie mensagens de campanha usando a entrega disparada por API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/trigger/send
{% endapimethod %}

> Use esse endpoint para enviar mensagens únicas e imediatas a usuários designados usando a entrega disparada pela API.

O envio disparado pela API permite que você abrigue o conteúdo da mensagem dentro do dashboard do Braze e, ao mesmo tempo, determine quando a mensagem será enviada e para quem, usando sua API.

Se você estiver direcionando um segmento, um registro de sua solicitação é armazenado no [console de desenvolvedor](https://dashboard.braze.com/app_settings/developer_console/activitylog/). Para enviar mensagens com esse endpoint, você deve ter um [ID de campanha](https://www.braze.com/docs/api/identifier_types/) criado ao criar uma [campanha disparada por API]({{site.baseurl}}/api/api_campaigns/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aef185ae-f591-452a-93a9-61d4bc023b05 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará gerar uma chave de API com a permissão `campaigns.trigger.send`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='send messages endpoints' %}

## Corpo da solicitação

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "send_id": (optional, string) see send identifier,
  "trigger_properties": (optional, object) personalization key-value pairs that apply to all users in this request,
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' sends to only users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to `false`, message sends to the entire segment targeted by the campaign)
    [
      {
      // Either "external_user_id" or "user_alias" or "email" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "email": (optional, string) email address of user to receive message,
      "prioritization": (optional, array) prioritization array; required when using email,
      "trigger_properties": (optional, object) personalization key-value pairs that apply to this user (these key-value pairs override any keys that conflict with the parent trigger_properties),
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases; if set to `false`, an attributes object must also be included,
      "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
    }
  ],
  "attachments": (optional, array) array of JSON objects that define the files you need attached, defined by "file_name" and "url",
    [
      {
       "file_name": (required, string) the name of the file you want to attach to your email, excluding the extension (for example, ".pdf"). Attach files up to 2 MB. This is required if you use "attachments",
       "url": (required, string) the corresponding URL of the file you want to attach to your email. The file name's extension is detected automatically from the URL defined, which should return the appropriate "Content-Type" as a response header. This is required if you use "attachments",
      }
    ]
}
```

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
|`campaign_id`|Obrigatória|String|Consulte [identificador de campanha]({{site.baseurl}}/api/identifier_types/). |
|`send_id`| Opcional | String | Consulte [enviar identificador]({{site.baseurl}}/api/identifier_types/). |
|`trigger_properties`| Opcional | Objeto | Consulte [propriedades do disparador]({{site.baseurl}}/api/objects_filters/trigger_properties_object/). Pares de chave-valor de personalização se aplicam a todos os usuários nesta solicitação. |
|`broadcast`| Opcional | Booleano | Você deve definir `broadcast` como verdadeiro ao enviar uma mensagem para um segmento inteiro que uma campanha ou canva segmenta. O padrão desse parâmetro é false (a partir de 31 de agosto de 2017). <br><br> Se `broadcast` estiver definido como true, uma lista `recipients` não poderá ser incluída. No entanto, tenha cuidado ao definir `broadcast: true`, pois definir essa flag inadvertidamente pode fazer com que você envie sua mensagem para um público maior do que o esperado. |
|`audience`| Opcional | Objeto de público conectado| Veja [público conectado]({{site.baseurl}}/api/objects_filters/connected_audience/). |
|`recipients`| Opcional | Vetor | Consulte [objeto de destinatários]({{site.baseurl}}/api/objects_filters/recipient_object/).<br><br>Se `send_to_existing_only` for `false`, um objeto de atribuição deverá ser incluído.<br><br>Se `recipients` não for fornecido e `broadcast` estiver definido como verdadeiro, a mensagem é enviada para todo o segmento direcionado pela campanha. <br><br> Se `email` for o identificador, você deve incluir [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email) no objeto de destinatários. |
|`attachments`| Opcional | Vetor | Se `broadcast` estiver definido como true, a lista `attachments` não poderá ser incluída. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

- O vetor de objetos pode conter até 50 objetos, sendo que cada objeto contém uma única string `external_user_id` e um objeto `trigger_properties`.
- Quando `send_to_existing_only` é `true` (o padrão), Braze envia a mensagem apenas para usuários existentes. Quando definido como `false` e um objeto de atributos é fornecido, Braze cria um novo usuário se um não existir. Observe que definir `send_to_existing_only` como `false` não é suportado para aliases de usuário—novos usuários apenas com alias não podem ser criados através deste endpoint. Para enviar para um usuário apenas com alias, o usuário deve já existir no Braze.

O status do grupo de inscrições de um usuário pode ser atualizado com a inclusão de um parâmetro `subscription_groups` no objeto `attributes`. Para obter mais informações, consulte [Objeto de atribuições do usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object).

## Exemplo de solicitação
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "trigger_properties": "",
  "broadcast": false,
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
  "recipients": [
    {
      "user_alias": {
        "alias_name" : "example_name",
        "alias_label" : "example_label"
      },
      "external_user_id": "external_user_identifier",
      "trigger_properties": "",
      "send_to_existing_only": true,
      "attributes": {
        "first_name" : "Alex"
      }
    }
  ],
  "attachments": [
    {
      "file_name" : "YourFileName",
      "url" : "https://exampleurl.com/YourFileName.pdf"
    }
  ]
}'
```

## Detalhes da resposta

As respostas do endpoint de envio de mensagens incluem o `dispatch_id` da mensagem para referência de volta ao envio da mensagem. O endereço `dispatch_id` é o ID do envio de mensagens, um ID exclusivo para cada transmissão enviada pela Braze. Ao usar esse endpoint, você recebe um único `dispatch_id` para um conjunto inteiro de usuários em lote. Para saber mais sobre o site `dispatch_id`, consulte nossa documentação sobre o [comportamento do Dispatch ID]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

Se sua solicitação encontrar um erro fatal, consulte [Erros e respostas]({{site.baseurl}}/api/errors/#fatal-errors) para obter o código e a descrição do erro.

## Objeto de atribuições para campanhas

Braze tem um objeto de envio de mensagens chamado `attributes` que permite adicionar, criar ou atualizar atributos e valores para um usuário antes de enviar uma campanha acionada por API. Usando o endpoint `campaign/trigger/send` enquanto esta chamada de API processa o objeto de atributos do usuário antes de processar e enviar a campanha. Isso ajuda a minimizar o risco de problemas causados por [condições de corrida]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/).

{% alert tip %}
Está procurando a versão do Canva desse endpoint? Dê uma olhada em [Envio de mensagens do Canva usando entrega disparada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#create-send-endpoint).
{% endalert %}

{% endapi %}
