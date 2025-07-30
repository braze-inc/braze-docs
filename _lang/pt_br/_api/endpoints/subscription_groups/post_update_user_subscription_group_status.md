---
nav_title: "POST: Atualizar o status do grupo de inscrições do usuário"
article_title: "POST: Atualizar o status do grupo de inscrições do usuário"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o o endpoint da Braze \"Atualizar o status do grupo de inscrições do usuário\""
---
{% api %}
# Atualizar o status do grupo de inscrições do usuário
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/subscription/status/set
{% endapimethod %}

> Use esse endpoint para atualizar em lote o estado da inscrição de até 50 usuários no dashboard do Braze. 

É possível acessar o site `subscription_group_id` de um grupo de inscrições navegando até a página **Grupo de inscrições**.

Se você quiser ver exemplos ou testar esse endpoint para **grupos de inscrições para e-mail**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8895e87e-6324-47a3-a833-adf29a258bb9 {% endapiref %}

Se você quiser ver exemplos ou testar esse endpoint para **grupos de inscrições SMS e RCS**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#72558b32-7dbe-4cba-bd22-a7ce513076dd {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `subscription.status.set`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='subscription status set' %}

## Corpo da solicitação

{% tabs %}
{% tab SMS e RCS %}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "subscription_group_id": (required, string) the id of your subscription group,
   "subscription_state": (required, string) available values are "unsubscribed" (not in subscription group) or "subscribed" (in subscription group),
   "external_id": (required*, array of strings) the external ID of the user or users, may include up to 50 IDs,
   "phone": (required*, array of strings in E.164 format) The phone number of the user (must include at least one phone number and at most 50 phone numbers),
   // SMS and RCS subscription group - one of external_id or phone is required
 }
```
\* Grupos de inscrições de SMS e RCS: Somente `external_id` ou `phone` são aceitos.

{% endtab %}
{% tab Email %}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "subscription_group_id": (required, string) the id of your subscription group,
   "subscription_state": (required, string) available values are "unsubscribed" (not in subscription group) or "subscribed" (in subscription group),
   "external_id": (required*, array of strings) the external ID of the user or users, may include up to 50 IDs,
   "email": (required*, array of strings) the email address of the user (must include at least one email and at most 50 emails),
   // Email subscription group - one of external_id or email is required
   // Note that sending an email address that is linked to multiple profiles will update all relevant profiles
 }
```
\* Grupos de inscrições para e-mail: É necessário o endereço `email` ou `external_id`.
{% endtab %}
{% endtabs %}

Essa propriedade não deve ser usada para atualizar as informações de perfil de um usuário. Em vez disso, use a propriedade [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

{% alert tip %}
Ao criar novos usuários usando o endpoint [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), é possível definir grupos de inscrições no objeto de atribuições do usuário, o que permite criar um usuário e definir o estado do grupo de inscrições em uma única chamada de API.
{% endalert %}

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types/?tab=subscription%20group%20ids) | Obrigatória | String | O `id` do seu grupo de inscrições. |
| `subscription_state` | Obrigatória | String | Os valores disponíveis são `unsubscribed` (não está no grupo de inscrições) ou `subscribed` (está no grupo de inscrições). |
| `external_id` | Obrigatório* | Matriz de strings | O `external_id` do usuário ou dos usuários pode incluir até 50 `id`s. |
| `email` | Obrigatório* | string ou array de strings | O endereço de e-mail do usuário pode ser passado como um vetor de strings. Deve incluir pelo menos um endereço de e-mail (com um máximo de 50). <br><br>Se vários usuários (`external_id`) no mesmo espaço de trabalho compartilharem o mesmo endereço de e-mail, todos os usuários que compartilham o endereço de e-mail serão atualizados com as alterações do grupo de inscrições. |
| `phone` | Obrigatório* | String em [E.164](https://en.wikipedia.org/wiki/E.164) formato | O número de telefone do usuário pode ser passado como uma matriz de strings. Deve incluir pelo menos um número de telefone (até 50). <br><br>Se vários usuários (`external_id`) no mesmo espaço de trabalho compartilharem o mesmo número de telefone, todos os usuários que compartilham o número de telefone serão atualizados com as mesmas alterações no grupo de inscrições. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplos de solicitações

### E-mail

```
curl --location --request POST 'https://rest.iad-01.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "subscription_group_identifier",
  "subscription_state": "unsubscribed",
  "external_id": "external_identifier",
  "email": ["example1@email.com", "example2@email.com"]
}
'
```

### SMS e RCS

```
curl --location --request POST 'https://rest.iad-01.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "subscription_group_identifier",
  "subscription_state": "unsubscribed",
  "external_id": "external_identifier",
  "phone": ["+12223334444", "+11112223333"]
}
'
```

## Exemplo de resposta bem-sucedida

O código de status `201` poderia retornar o seguinte corpo de resposta.

```json
{
    "message": "success"
}
```

{% alert important %}
O endpoint aceita apenas o valor `email` ou `phone`, não ambos. Se forem fornecidos ambos, você receberá esta resposta: `{"message":"Either an email address or a phone number should be provided, but not both."}`
{% endalert %}

{% endapi %}

