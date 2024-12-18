---
nav_title: "POST: Envio de mensagens de canva via entrega disparada por API"
article_title: "POST: Envio de mensagens de canva via entrega disparada por API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint da Braze Envio de mensagens de canva via entrega disparada por API"

---
{% api %}
# Enviar mensagens do Canva por meio de entrega disparada pela API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/trigger/send
{% endapimethod %}

> Use esse endpoint para enviar mensagens do canva por meio de entrega disparada pela API.

A entrega disparada por API permite que você armazene o conteúdo da mensagem no dashboard do Braze e, ao mesmo tempo, determine quando a mensagem será enviada e para quem por meio de sua API.

Antes de enviar mensagens com esse endpoint, você deve ter um [ID do Canvas]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier) (que é criado quando você constrói um Canvas).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c9a8a5fe-a101-4755-99f2-73aa8fc146fe {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará gerar uma chave de API com a permissão `canvas.trigger.send`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='message endpoints' %}

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
|`canvas_entry_properties`| Opcional | Objeto | Consulte [Propriedades de entrada do Canva]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/). Pares de valores-chave de personalização que serão aplicados a todos os usuários nessa solicitação. O objeto de propriedades de entrada do canva tem um limite máximo de tamanho de 50 KB. |
|`broadcast`| Opcional | Booleano | Você deve definir `broadcast` como true ao enviar uma mensagem para um segmento inteiro que uma campanha ou Canva direciona. O padrão desse parâmetro é false (a partir de 31 de agosto de 2017). <br><br> Se `broadcast` estiver definido como true, uma lista `recipients` não poderá ser incluída. No entanto, tenha cuidado ao definir `broadcast: true`, pois a definição não intencional desse sinalizador pode fazer com que sua mensagem seja enviada a um público maior do que o esperado. |
|`audience`| Opcional| Objeto do público conectado | Consulte [Público conectado]({{site.baseurl}}/api/objects_filters/connected_audience/). |
|`recipients`| Opcional | Vetor | Consulte o [objeto Recipients]({{site.baseurl}}/api/objects_filters/recipient_object/). Se não for fornecido e `broadcast` for definido como true, a mensagem será enviada para todo o segmento de mensagem direcionado pelo Canva.<br><br> O vetor `recipients` pode conter até 50 objetos, sendo que cada objeto contém uma única string `external_user_id` e um objeto `canvas_entry_properties`. Os endereços `external_user_id` ou `user_alias` são necessários para essa chamada. As solicitações devem especificar apenas uma. <br><br> Quando `send_to_existing_only` for `true`, a Braze enviará a mensagem apenas para os usuários existentes - no entanto, esse sinalizador não pode ser usado com aliases de usuários. Quando `send_to_existing_only` for `false` e não existir um usuário com o `id` fornecido, o Braze criará um usuário com esse ID e atribuições antes de enviar a mensagem.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Os clientes que usam a API para chamadas de servidor para servidor talvez precisem listar o URL apropriado da API se estiverem protegidos por um firewall.

{% alert important %}
A especificação de um destinatário por endereço de e-mail está atualmente em acesso antecipado. Entre em contato com seu gerente de sucesso do cliente se tiver interesse em participar desse acesso antecipado.
{% endalert %}

{% alert note %}
Se você incluir usuários específicos na sua chamada de API e um segmento de mensagem no dashboard, a mensagem será enviada especificamente para os perfis de usuário que estão na chamada de API e se qualificam para os filtros de segmento.
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

As respostas do endpoint de envio de mensagens incluirão o endereço `dispatch_id` da mensagem para referência ao envio da mensagem. O endereço `dispatch_id` é o ID do envio de mensagens (ID exclusivo para cada "transmissão" enviada da plataforma Braze). Para saber mais, consulte [Comportamento do Dispatch ID]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

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

## Objeto de atribuições para o Canva

Use o objeto de envio de mensagens `attributes` para adicionar, criar ou atualizar atribuições e valores para um usuário antes de enviar a ele um Canva disparado pela API usando o ponto de extremidade `canvas/trigger/send`. Essa chamada da API processa o objeto de atribuições do usuário antes de processar e enviar a tela. Isso ajuda a minimizar o risco de problemas causados por [condições de corrida]({{site.baseurl}}/help/best_practices/race_conditions/).

{% alert note %}
Procurando a versão de campanhas desse endpoint? Confira o [Envio de mensagens de campanha por meio de entrega disparada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/).
{% endalert %}

{% endapi %}
