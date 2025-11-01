---
nav_title: "OBTER: Listar o status do grupo de assinatura dos usuários"
article_title: "OBTER: Listar Status do Grupo de Inscrições do Usuário"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o status do grupo de inscrições do usuário da lista no endpoint Braze."

---
{% api %}
# Listar status do grupo de inscrições do usuário
{% apimethod get %}
/subscription/status/get
{% endapimethod %}

> Use este endpoint para obter o estado de inscrição de um usuário em um grupo de inscrições.

Estes grupos estarão disponíveis na página do **grupo de inscrições**. A resposta deste endpoint incluirá o ID externo e "subscribed", "unsubscribed" ou "unknown" para o grupo de inscrições específico solicitado na chamada da API. Isso pode ser usado para atualizar o estado do grupo de inscrições em chamadas subsequentes da API ou para ser exibido em uma página da web hospedada.

Se você quiser ver exemplos ou testar este endpoint para **Grupos de Inscrição de E-mail**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#488c8923-fa44-4124-9245-036d13c615f2 {% endapiref %}

Se você quiser ver exemplos ou testar este endpoint para **Grupos de Inscrição de SMS**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

Se você quiser ver exemplos ou testar este endpoint para **Grupos do WhatsApp**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `subscription.status.get`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types/?tab=subscription%20group%20ids)  | Obrigatória | String | O `id` do seu grupo de inscrições. |
| `external_id`  |  Obrigatório* | String | O `external_id` do usuário (deve incluir pelo menos um e no máximo 50 `external_ids`). <br><br>Quando ambos um `external_id` e `email`/`phone` são enviados, apenas os `external_id` fornecidos serão aplicado à consulta de resultado. |
| `email` | Obrigatório* | String | O endereço de e-mail do usuário. Pode ser passado como um vetor de strings com um máximo de 50.<br><br> Enviar tanto um endereço de e-mail quanto um número de telefone (sem `external_id`) resultará em um erro. |
| `phone` | Obrigatório* | string no [E.164](https://en.wikipedia.org/wiki/E.164) formato | O número de telefone do usuário. Se o e-mail não estiver incluído, você precisa incluir pelo menos um número de telefone (com um máximo de 50).<br><br> Enviar tanto um endereço de e-mail quanto um número de telefone (sem `external_id`) resultará em um erro. |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Um de `external_id` ou `email` ou `phone` é necessário para cada usuário.

- Para grupos de inscrição de SMS e WhatsApp, é necessário `external_id` ou `phone`.  Quando ambos são enviados, apenas o `external_id` é usado para consulta e o número de telefone é aplicado a esse usuário.
- Para grupos de inscrição de e-mail, é necessário `external_id` ou `email`.  Quando ambos são enviados, apenas a `external_id` é usada para a consulta e o endereço de e-mail é aplicado a esse usuário.

## Exemplo de solicitação 

{% tabs %}
{% tab Multiple Users %}
{% raw %}
```
https://rest.iad-03.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&external_id[]=1&external_id[]=2
```
{% endraw %}
{% endtab %}
{% tab SMS and WhatsApp %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&phone=+11112223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% tab Email %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&email=example@braze.com' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Resposta

Todas as respostas bem-sucedidas retornarão `Subscribed`, `Unsubscribed` ou `Unknown` dependendo do status e do histórico do usuário com o grupo de inscrições.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "status": {
    "1": "Unsubscribed",
    "2": "Subscribed"
  },
  "message": "success"
}
```

{% endapi %}
