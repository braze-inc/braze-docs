---
nav_title: "POST: Criar novo alias de usuário"
article_title: "POST: Criar novo alias de usuário"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Create new user alias Braze."

---
{% api %}
# Criar novo alias de usuário
{% apimethod post %}
/users/alias/new
{% endapimethod %}

> Use esse endpoint para adicionar novos aliases de usuário para usuários identificados existentes ou para criar novos usuários não identificados.

Podem ser especificados até 50 aliases de usuário por solicitação.

**A adição de um alias de usuário para um usuário existente** requer que um `external_id` seja incluído no novo objeto de alias de usuário. Se o `external_id` estiver presente no objeto, mas não houver nenhum usuário com esse `external_id`, o alias não será adicionado a nenhum usuário. Se um `external_id` não estiver presente, um usuário ainda será criado, mas precisará ser identificado posteriormente. Você pode fazer isso usando o endpoint "Identificação de usuários" e `users/identify`.

**A criação de um novo usuário somente de alias** exige que o endereço `external_id` seja omitido no novo objeto de alias de usuário. Depois que o usuário for criado, use o endpoint `/users/track` para associar o usuário somente de alias a atribuições, eventos e compras, e o endpoint `/users/identify` para identificar o usuário com um `external_id`.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5cf18e64-fd02-452f-8c90-9a0f7c4d0487 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/api_key/) com a permissão `users.alias.new`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='users alias new' %}

## Corpo da solicitação

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "user_aliases" : (required, array of new user alias object)
}
```

### Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `user_aliases` | Obrigatória | Vetor de objetos de novos alias de usuário | Consulte o [objeto de alias de usuário]({{site.baseurl}}/api/objects_filters/user_alias_object/).<br><br> Para saber mais sobre `alias_name` e `alias_label`, consulte nossa documentação sobre [aliases de usuário]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases).|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Corpo da solicitação do endpoint com a nova especificação de objeto de alias de usuário

```json
{
  "external_id" : (optional, string),
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```

## Exemplo de solicitação
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/alias/new' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "user_aliases" :[
    {
      "external_id": "external_identifier",
      "alias_name" : "example_name",
      "alias_label" : "example_label"
    }
  ]
}'
```

## Resposta

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
    "aliases_processed": 1,
    "message": "success"
}
```


{% endapi %}

