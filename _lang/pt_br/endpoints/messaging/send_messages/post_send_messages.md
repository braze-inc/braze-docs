---
nav_title: "POST: Envio imediato de mensagens usando apenas a API"
article_title: "POST: Envio de mensagens imediatamente usando somente a API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Enviar mensagens imediatamente usando somente a API do Braze."

---
{% api %}
# Envio imediato de mensagens usando apenas a API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/messages/send
{% endapimethod %}

> Use esse endpoint para enviar mensagens imediatas a usuários designados usando a API do Braze.

Se estiver direcionando a campanha para um segmento, um registro da sua solicitação será armazenado [Console de desenvolvedor](https://dashboard.braze.com/app_settings/developer_console/activitylog/).

{% multi_lang_include api/payload_size_alert.md %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#946cb701-96e3-48d7-868c-f079785b6d24 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará gerar uma chave de API com a permissão `messages.send`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='message send endpoint' %}

## Corpo da solicitação

{% alert tip %}
Não se esqueça de incluir [objetos de envio de mensagens]({{site.baseurl}}/api/objects_filters/#messaging-objects) em seu corpo para completar suas solicitações.
{% endalert %}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   // You will need to include at least one of 'segment_id', 'external_user_ids', and 'audience'
   // Including 'segment_id' will send to members of that segment
   // Including 'external_user_ids' and/or 'user_aliases' will send to those users
   // Including both will send to the provided users if they are in the segment
   "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if no external_user_ids or aliases are provided,
   "external_user_ids": (optional, array of strings) see external user identifier,
   "user_aliases": (optional, array of user alias object) see user alias,
   "segment_id": (optional, string) see segment identifier,
   "audience": (optional, connected audience object) see connected audience,
   "campaign_id": (optional*, string) *required if you wish to track campaign stats (for example, sends, clicks, bounces, etc). see campaign identifier,
   "send_id": (optional, string) see send identifier,
   "override_frequency_capping": (optional, bool) ignore frequency_capping for campaigns, defaults to false,
   "recipient_subscription_state": (optional, string) use this to send messages to only users who have opted in ('opted_in'), only users who have subscribed or are opted in ('subscribed') or to all users, including unsubscribed users ('all'), the latter being useful for transactional email messaging. Defaults to 'subscribed',
   "messages": {
     "android_push": (optional, android push object),
     "apple_push": (optional, apple push object),
     "content_card": (optional, content card object),
     "email": (optional, email object),
     "kindle_push": (optional, kindle/fireOS push object),
     "web_push": (optional, web push object),
     "webhook": (optional, webhook object),
     "whats_app": (optional, WhatsApp object),
     "sms": (optional, SMS object)
   }
 }
```

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
|`broadcast`| Opcional | Booleano | Você deve definir `broadcast` como verdadeiro ao enviar uma mensagem para um segmento inteiro que uma campanha ou canva segmenta. O padrão desse parâmetro é false (a partir de 31 de agosto de 2017). <br><br> Se `broadcast` estiver definido como true, uma lista `recipients` não poderá ser incluída. No entanto, tenha cuidado ao definir `broadcast: true`, pois definir esta flag de forma não intencional pode fazer com que você envie sua mensagem para um público maior do que o esperado. |
|`external_user_ids` | Opcional | Matriz de strings | Consulte [ID de usuário externo]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields). |
|`user_aliases`| Opcional | Vetor de objetos de alias de usuário| Consulte o [objeto de alias de usuário]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
|`segment_id `| Opcional | String | Consulte [identificador de segmento]({{site.baseurl}}/api/identifier_types/#segment-identifier). |
|`audience`| Opcional | Objeto de público conectado | Veja [público conectado]({{site.baseurl}}/api/objects_filters/connected_audience/). |
|`campaign_id`| Opcional* | String | Para saber mais, consulte o [identificador de campanha]({{site.baseurl}}/api/identifier_types/#campaign-identifier/). <br><br>\*Obrigatório se você deseja rastrear métricas de campanha (como _Envios_, _Cliques_ ou _Retornos_) no painel do Braze. |
|`send_id`| Opcional | String | Consulte [enviar identificador]({{site.baseurl}}/api/identifier_types/#send-identifier). |
|`override_frequency_capping`| Opcional | Booleano | Ignore `frequency_capping` para campanhas, o padrão é `false`. |
|`recipient_subscription_state`| Opcional | String | Use essa opção para enviar mensagens apenas para usuários que tenham aceitado receber mensagens (`opted_in`), apenas para usuários que tenham feito a inscrição ou aceitado receber mensagens (`subscribed`) ou para todos os usuários, inclusive os que cancelaram a inscrição (`all`). <br><br>O uso de usuários do `all` é útil para envio de mensagens por e-mail de transação. O padrão é `subscribed`. |
|`messages`| Opcional | Objetos de envio de mensagens | Consulte os [objetos de envio de mensagens disponíveis]({{site.baseurl}}/api/objects_filters/#messaging-objects). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/send' \
--data-raw '{
  "broadcast": "false",
  "external_user_ids": "external_user_identifiers",
  "user_aliases": {
    "alias_name": "example_name",
    "alias_label": "example_label"
  },
  "segment_id": "segment_identifier",
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
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "override_frequency_capping": "false",
  "recipient_subscription_state": "all",
  "messages": {
    "android_push": "(optional, Android Push Object)",
    "apple_push": "(optional, Apple Push Object)",
    "content_card": "(optional, Content Card Object)",
    "email": "(optional, Email Object)",
    "kindle_push": "(optional, Kindle/FireOS Push Object)",
    "web_push": "(optional, Web Push Object)"
  }
}'
```

## Detalhes da resposta

As respostas do endpoint de envio de mensagens incluirão o endereço `dispatch_id` da mensagem para referência ao envio da mensagem. O endereço `dispatch_id` é o ID do envio de mensagens, ou seja, o ID exclusivo de cada "transmissão" enviada pelo Braze. Para saber mais, consulte [Comportamento do Dispatch ID]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

{% endapi %}
