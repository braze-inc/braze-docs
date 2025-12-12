---
nav_title: "OBTER: Listar grupos de assinatura de usuários"
article_title: "OBTER: Listar os grupos de inscrições do usuário"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Braze dos grupos de inscrições de usuários da lista."

---
{% api %}
# Listar os grupos de inscrições do usuário
{% apimethod get %}
/subscription/user/status
{% endapimethod %}

> Use esse ponto de extremidade para listar e obter os grupos de assinatura com o histórico de um determinado usuário.

Se você quiser ver exemplos ou testar este endpoint para **Grupos de Inscrição de E-mail**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d1c3b617-22f1-47bf-9ee8-499526824470 {% endapiref %}

Se você quiser ver exemplos ou testar este endpoint para **Grupos de Inscrição de SMS**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

Se você quiser ver exemplos ou testar este endpoint para **Grupos do WhatsApp**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `subscription.groups.get`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `external_id`  | Obrigatória | String | O `external_id` do usuário (deve incluir no mínimo um e no máximo 50 `external_ids`). |
| `email`  |  Obrigatório* | String | O endereço de e-mail do usuário pode ser passado como uma matriz de strings. Deve incluir pelo menos um endereço de e-mail (com um máximo de 50). |
| `phone` | Obrigatório* | string no [E.164](https://en.wikipedia.org/wiki/E.164) formato | O número de telefone do usuário. Deve incluir pelo menos um número de telefone (com um máximo de 50). |
| `limit` | Opcional | Inteiro | O limite do número máximo de resultados retornados. O `limit` padrão (e máximo) é 100. |
| `offset`  |  Opcional | Inteiro | Número de modelos a serem ignorados antes de retornar o restante dos modelos que atendem aos critérios de pesquisa. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert tip %}
Se houver vários usuários (vários `external_ids`) que compartilham o mesmo endereço de e-mail, todos os usuários serão retornados como um usuário separado (mesmo que tenham o mesmo endereço de e-mail ou grupo de inscrições).
{% endalert %}

## Exemplo de solicitação 

{% tabs %}
{% tab Multiple Users %}
{% raw %}
`https://rest.iad-03.braze.com/subscription/user/status?external_id[]=1&external_id[]=2`
{% endraw %}
{% endtab %}
{% tab SMS and WhatsApp %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/user/status?external_id={{external_id}}&limit=100&offset=1&phone=+11112223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% tab Email %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/user/status?external_id={{external_id}}&email=example@braze.com&limit=100&offset=0' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Exemplo de resposta

Somente os grupos de assinatura que tiveram uma atualização de status de assinatura no histórico de um usuário serão incluídos em uma resposta bem-sucedida. Isso significa que os grupos de assinatura recém-criados não serão listados.

```json
{
  "success": true,
  "subscription_groups": [
    {
      "subscription_group_id": "group_id_1",
      "subscription_status": "subscribed"
    },
    {
      "subscription_group_id": "group_id_2",
      "subscription_status": "unsubscribed"
    }
  ]
}
```

{% endapi %}
