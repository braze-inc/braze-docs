---
nav_title: "POST: Atualizar o alias do usuário"
article_title: "POST: Atualizar alias de usuário"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint \" Atualizar alias de usuário\"."
---
{% api %}
# Atualizar o alias do usuário
{% apimethod post %}
/users/alias/update
{% endapimethod %}

> Use esse endpoint para atualizar os aliases de usuário existentes.

Podem ser especificados até 50 aliases de usuário por solicitação.

A atualização de um alias de usuário exige que `alias_label`, `old_alias_name` e `new_alias_name` sejam incluídos no objeto de atualização de alias do usuário. Se não houver um alias de usuário associado a `alias_label` e `old_alias_name`, nenhum alias será atualizado. Se o `alias_label` e o `old_alias_name` fornecidos forem encontrados, o `old_alias_name` será atualizado para o `new_alias_name`.

{% alert note %}
Esse endpoint não garante a sequência de objetos `alias_updates` que estão sendo atualizados.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#a084b843-b3cd-43f0-bfb1-ef7bada839c5 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/api_key/) com a permissão `users.alias.update`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='users alias update' %}

## Corpo da solicitação

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "alias_updates" : (required, array of update user alias object)
}
```

### Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | --------- | --------- | ----------- |
| `alias_updates` | Obrigatória | Vetor de objetos de alias de usuário de atualização | Consulte o [objeto de alias de usuário]({{site.baseurl}}/api/objects_filters/user_alias_object/).<br><br> Para saber mais sobre `old_alias_name`, `new_alias_name` e `alias_label`, consulte [Aliases de usuário]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Corpo da solicitação de endpoint com especificação de objeto de alias de usuário atualizado

```json
{
  "alias_label" : (required, string),
  "old_alias_name" : (required, string),
  "new_alias_name" : (required, string)
}
```

## Exemplo de solicitação
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/alias/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "alias_updates" :[
    {
      "alias_label": "example_alias_label",
      "old_alias_name" : "example_old_alias_name",
      "new_alias_name" : "example_new_alias_name"
    }
  ]
}'
```

{% endapi %}

