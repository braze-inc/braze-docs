---
nav_title: "POST: Atualizar o status do grupo de assinatura de usuários v2"
alias: /post_update_user_subscription_group_status_v2/
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Braze V2 de atualização do status do grupo de inscrições do usuário."

platform: API
channel:
  - Email
---

{% api %}
# Atualizar o status do grupo de inscrições do usuário (V2)
{% apimethod post %}
/v2/subscription/status/set
{% endapimethod %}

> Use este endpoint para atualizar em lote o estado de inscrição de até 50 usuários no dashboard do Braze. 

Você pode acessar o `subscription_group_id` de um grupo de inscrições navegando até a página **Grupo de Inscrições**.

Se você quiser ver exemplos ou testar este endpoint para **Grupos de Inscrição de E-mail**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b1b9a0e0-6329-4df2-a465-53347f410662 {% endapiref %}

Se você quiser ver exemplos ou testar este endpoint para **Grupos de Inscrição de SMS**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409 {% endapiref %}

Se você quiser ver exemplos ou testar este endpoint para **Grupos do WhatsApp**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `subscription.status.set`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='subscription status set' %}

## Corpo da solicitação

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "subscription_groups":[
    {
      "subscription_group_id": (required, string),
      "subscription_state": (required, string)
      "external_ids": (required*, array of strings),
      "emails": (required*, array of strings),
      "phones": (required*, array of strings in E.164 format),
    }
  ]
}
```
\* Você não pode incluir ambos os parâmetros `emails` e `phones`. Além disso, `emails`, `phones` e `external_ids` podem ser enviados individualmente.

{% alert tip %}
Ao criar novos usuários usando o [endpoint `/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), é possível definir grupos de inscrições no objeto de atribuições do usuário, o que permite criar um usuário e definir o estado do grupo de inscrições em uma única chamada de API.
{% endalert %}

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types/?tab=subscription%20group%20ids) | Obrigatória | String | O `id` do seu grupo de inscrições. |
| `subscription_state` | Obrigatória | String | Os valores disponíveis são `unsubscribed` (não está no grupo de inscrições) ou `subscribed` (está no grupo de inscrições). |
| `external_ids` | Obrigatório* | Array de strings | O `external_id` do usuário ou usuários pode incluir até 50 `id`s. |
| `emails` | Obrigatório* | string ou array de strings | O endereço de e-mail do usuário pode ser passado como um vetor de strings. Deve incluir pelo menos um endereço de e-mail (com um máximo de 50). <br><br>Se vários usuários (`external_id`) no mesmo espaço de trabalho compartilharem o mesmo e-mail, todos os usuários que compartilham o e-mail são atualizados com as mudanças do grupo de inscrições. |
| `phones` | Obrigatório* | string em [E.164](https://en.wikipedia.org/wiki/E.164) formato | Os números de telefone do usuário podem ser passados como um vetor de strings. Deve incluir pelo menos um número de telefone (até 50). <br><br>Se vários usuários (`external_id`) no mesmo espaço de trabalho compartilharem o mesmo número de telefone, todos os usuários que compartilham o número de telefone serão atualizados com as mesmas alterações do grupo de assinatura.|
| `use_double_opt_in_logic` | Opcional | Booleano | Se esse parâmetro for omitido ou definido como `false`, os usuários não serão inseridos no fluxo de trabalho de opt-in duplo de SMS. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
Você não pode incluir ambos os parâmetros `emails` e `phones`. Além disso, `emails`, `phones` e `external_ids` podem ser enviados individualmente.
{% endalert %}

### Exemplos de solicitações

O exemplo a seguir usa `external_id` para fazer uma chamada de API para e-mail e SMS.

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@email.com"]
    },
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@email.com"]
    }
  ]
}
```

## E-mail

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "emails":["example1@email.com","example2@email.com"]
    }
  ]
}
'
```

## SMS e WhatsApp

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "phones":["+12223334444","+15556667777"]
    }
  ]
}
'
```

{% endapi %}
