---
nav_title: "POST: Envie mensagens do canva usando entrega acionada por API"
article_title: "POST: Enviar Mensagens de Canva Usando Entrega Acionada por API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o envio de canvas usando o API acionado pela entrega do Braze."

---
{% api %}
# Envie mensagens do canva usando entrega acionada por API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/trigger/send
{% endapimethod %}

> Use este endpoint para enviar mensagens de canva com entrega acionada por API.

A entrega acionada por API permite que você armazene o conteúdo da mensagem no dashboard do Braze enquanto determina quando uma mensagem é enviada e para quem usando sua API.

Antes de enviar mensagens com esse endpoint, você deve ter um [ID do Canvas]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier) (que é criado quando você constrói um Canvas).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c9a8a5fe-a101-4755-99f2-73aa8fc146fe {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará gerar uma chave de API com a permissão `canvas.trigger.send`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='send messages endpoints' %}

## Corpo da solicitação

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) see Canvas identifier,
  "canvas_entry_properties": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if `recipients` is omitted,
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message will send to the entire segment targeted by the Canvas)
    [{
      // Either "external_user_id" or "user_alias" or "email" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "email": (optional, string) email address of user to receive message,
      "prioritization": (optional, array) prioritization array; required when using email,
      "canvas_entry_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent `canvas_entry_properties`)
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases
      "attributes": (optional, object) fields in the attributes object will create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values will be overwritten
    }],
    ...
}
```

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
|`canvas_id`| Obrigatória | String | Consulte [Identificador do Canva]({{site.baseurl}}/api/identifier_types/). |
|`canvas_entry_properties`| Opcional | Objeto | Isso inclui [propriedades de entrada do Canvas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/). Os pares de chave-valor de personalização se aplicarão a todos os usuários nesta solicitação. O objeto de propriedades de entrada do canva tem um limite máximo de tamanho de 50 KB. <br><br>**Nota:** Se você estiver participando do [acesso antecipado do Canvas Context]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/), este parâmetro é `context` e inclui propriedades de entrada do Canvas. |
|`broadcast`| Opcional | Booleano | Você deve definir `broadcast` como verdadeiro ao enviar uma mensagem para um segmento inteiro que uma campanha ou canva segmenta. O padrão desse parâmetro é false (a partir de 31 de agosto de 2017). <br><br> Se `broadcast` estiver definido como true, uma lista `recipients` não poderá ser incluída. No entanto, tenha cuidado ao definir `broadcast: true`, pois definir essa flag inadvertidamente pode fazer com que você envie sua mensagem para um público maior do que o esperado. |
|`audience`| Opcional| Objeto do público conectado | Consulte [Público conectado]({{site.baseurl}}/api/objects_filters/connected_audience/). |
|`recipients`| Opcional | Vetor | Consulte o [objeto Recipients]({{site.baseurl}}/api/objects_filters/recipient_object/). <br><br>Se não fornecido e `broadcast` estiver definido como verdadeiro, a mensagem será enviada para todo o segmento alvo do canva.<br><br> O `recipients` array pode conter até 50 objetos, com cada objeto contendo uma única `external_user_id` string e um `canvas_entry_properties` objeto. Esta chamada requer um `external_user_id`, `user_alias` ou `email`. As solicitações devem especificar apenas uma. <br><br>Se `email` for o identificador, você deve incluir [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email) no objeto de destinatários. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
Para o parâmetro `recipients`, quando `send_to_existing_only` for `true`, a Braze enviará a mensagem apenas para os usuários existentes. No entanto, esse sinalizador não pode ser usado com aliases de usuário. <br><br>Se `send_to_existing_only` for `false`, um objeto de atribuição deverá ser incluído. Quando `send_to_existing_only` for `false` **e** não existir um usuário com o `id` fornecido, a Braze criará um usuário com esse ID e atribuições antes de enviar a mensagem.
{% endalert %}

Os clientes que usam a API para chamadas de servidor para servidor talvez precisem listar o URL apropriado da API se estiverem protegidos por um firewall.

{% alert note %}
Se você incluir tanto usuários específicos na sua chamada de API quanto um segmento alvo no dashboard, a mensagem será enviada especificamente para os perfis de usuário que estão tanto na chamada de API quanto qualificam para os filtros de segmento.
{% endalert %}

## Exemplo de solicitação
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "canvas_entry_properties": {"product_name" : "shoes", "product_price" : 79.99},
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
      "external_user_id": "user_identifier",
      "send_to_existing_only": true,
      "attributes": {
          "first_name" : "Alex"
      }
    }
  ]
}'
```

## Detalhes da resposta

As respostas do endpoint de envio de mensagens incluirão o `dispatch_id` da mensagem para referência de volta ao envio da mensagem. O endereço `dispatch_id` é o ID do envio de mensagens (ID exclusivo para cada "transmissão" enviada da plataforma Braze). Para saber mais, consulte [Comportamento do Dispatch ID]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

### Exemplo de resposta bem-sucedida

O código de status `201` pode retornar o seguinte corpo de resposta. Se o canva for arquivado, interrompido ou pausado, ele não será enviado por meio desse endpoint.

```
{
  "notice": "The Canvas is paused. Resume the Canvas to ensure trigger requests will take effect.",
  "dispatch_id": "example_dispatch_id",
  "message": "success"
}
```

Se o seu canva estiver arquivado, você verá a mensagem `notice`: "O Canva está arquivado. Desarquive o Canva para garantir que as solicitações de disparo tenham efeito." Se o canva não estiver ativo, você verá a mensagem `notice`: "O Canva está em pausa. Retome o Canva para garantir que as solicitações de disparo tenham efeito."

Se sua solicitação encontrar um erro fatal, consulte [Erros e respostas]({{site.baseurl}}/api/errors/#fatal-errors) para obter o código e a descrição do erro.

## Objeto de atributos para canva

Use o objeto de envio de mensagens `attributes` para adicionar, criar ou atualizar atributos e valores para um usuário antes de enviar um Canvas acionado por API usando o endpoint `canvas/trigger/send`. Esta chamada de API processa o objeto de atributos do usuário antes de processar e enviar o canva. Isso ajuda a minimizar o risco de problemas causados por [condições de corrida]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/). No entanto, por padrão, os grupos de inscrições não podem ser atualizados dessa forma.

{% alert note %}
Procurando a versão da campanha deste endpoint? Confira [Envio de mensagens de campanha usando entrega acionada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/).
{% endalert %}

{% endapi %}
