---
nav_title: "POST: Atualizar o status do grupo de inscrições dos usuários v2"
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

> Use esse endpoint para atualizar em lote o estado da inscrição de até 50 usuários no dashboard do Braze.

É possível acessar o site `subscription_group_id` de um grupo de inscrições navegando até a página **Grupo de inscrições**.

Para ver exemplos ou testar este endpoint para **Grupos de Inscrição por E-mail**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b1b9a0e0-6329-4df2-a465-53347f410662 {% endapiref %}

Para ver exemplos ou testar este endpoint para **Grupos de Inscrição por SMS**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409 {% endapiref %}

Para ver exemplos ou testar este endpoint para **Grupos de WhatsApp**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409 {% endapiref %}

## Pré-requisitos

Para usar este endpoint, você precisa de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `subscription.status.set`.

{% alert note %}
Se você estiver interessado em usar este endpoint com [grupos de inscrições do LINE]({{site.baseurl}}/user_guide/message_building_by_channel/line/line_users/subscription_groups/), entre em contato com seu gerente de sucesso do cliente.
{% endalert %}

## Diferenças em relação ao V1

O endpoint V2 difere do [endpoint V1]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) das seguintes maneiras:

- **Vários grupos de inscrições**: O V2 permite que você atualize vários grupos de inscrições em uma única solicitação de API, enquanto o V1 suporta apenas um grupo de inscrições por solicitação.
- **Atualizar tanto e-mail quanto SMS em uma chamada**: Ao usar `external_ids`, você pode atualizar tanto os grupos de inscrições por e-mail quanto por SMS para os mesmos usuários em uma única chamada de API. Com o V1, você deve fazer chamadas de API separadas para grupos de inscrições por e-mail e SMS.
- **Usando identificadores de e-mail ou telefone**: Se você usar `emails` ou `phones` em vez de `external_ids`, não poderá atualizar tanto os grupos de inscrições por e-mail quanto por SMS na mesma solicitação. Você deve fazer chamadas de API separadas—uma para grupos de inscrições por e-mail e uma para grupos de inscrições por SMS.

{% alert important %}
**Formato do número de telefone**: Os números de telefone devem estar no formato [E.164 (por exemplo, `+12223334444`). Números de telefone que não estão no formato E.164 são rejeitados.
{% endalert %}

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
| `phones` | Obrigatório* | string no [E.164](https://en.wikipedia.org/wiki/E.164) formato | Você pode passar os números de telefone dos usuários como um array de strings. Deve incluir pelo menos um número de telefone (até 50). Os números de telefone devem estar no formato E.164 (por exemplo, `+12223334444`). <br><br>Se vários usuários (`external_id`) no mesmo espaço de trabalho compartilharem o mesmo número de telefone, todos os usuários que compartilham o número de telefone são atualizados com as mesmas alterações do grupo de inscrições.|
| `use_double_opt_in_logic` | Opcional | Booleano | Se este parâmetro for omitido ou definido como `false`, os usuários não são inseridos no fluxo de trabalho de aceitação dupla de SMS. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert important %}
**Seleção de identificador**: 
- Para atualizar tanto os grupos de inscrições de e-mail quanto os de SMS em uma única chamada de API, use `external_ids`. Você não pode incluir tanto `emails` quanto `phones` na mesma solicitação.
- Se você usar `emails` ou `phones` em vez de `external_ids`, faça chamadas de API separadas—uma para grupos de inscrições de e-mail e outra para grupos de inscrições de SMS.
- Você pode enviar `emails`, `phones` ou `external_ids` individualmente.
{% endalert %}

### Exemplos de solicitações

O seguinte exemplo usa `external_ids` para atualizar tanto os grupos de inscrições de e-mail quanto os de SMS em uma única chamada de API. Isso só é possível ao usar `external_ids`—você não pode atualizar tanto os grupos de inscrições de e-mail quanto os de SMS em uma chamada ao usar `emails` ou `phones`.

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
