---
nav_title: "POST: Excluir usuários"
article_title: "POST: Excluir usuários"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o o endpoint da Braze \"Excluir usuários\"."

---
{% api %}
# Excluir usuários
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/delete
{% endapimethod %}

> Use esse endpoint para excluir qualquer perfil de usuário, especificando um identificador de usuário conhecido.

Até 50 `external_ids`, `user_aliases`, ou `braze_ids` podem ser incluídos em uma única solicitação. Apenas uma das opções `external_ids`, `user_aliases` ou `braze_ids` pode ser incluída em uma única solicitação.

{% alert warning %}
A exclusão de perfis de usuário não pode ser desfeita. Ele removerá permanentemente os usuários que possam causar discrepâncias nos seus dados. Saiba mais sobre o que acontece quando você [exclui um perfil de usuário via API]({{site.baseurl}}/help/help_articles/api/delete_user/) em nossa documentação de Ajuda.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#22e91d00-d178-4b4f-a3df-0073ecfcc992 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/api_key/) com a permissão `users.delete`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='users delete' %}

## Corpo da solicitação

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "external_ids" : (optional, array of string) External ids for the users to delete,
  "user_aliases" : (optional, array of user alias objects) User aliases for the users to delete,
  "braze_ids" : (optional, array of string) Braze user identifiers for the users to delete
}
```
### Parâmetros de solicitação

| Parâmetro      | Obrigatória | Tipo de dados                  | Descrição                                                                                      |
| -------------- | -------- | -------------------------- | ------------------------------------------------------------------------------------------------ |
| `external_ids` | Opcional | Matriz de strings           | Identificadores externos para os usuários a serem excluídos.                                                    |
| `user_aliases` | Opcional | Vetor de objeto de alias de usuário | [Aliases de usuário]({{site.baseurl}}/api/objects_filters/user_alias_object/) para os usuários a serem excluídos. |
| `braze_ids`    | Opcional | Matriz de strings           | Identificadores de usuário Braze para os usuários a serem excluídos.                                                  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Exclusão de usuários por e-mail
Se um `email` for especificado como um identificador, um valor `prioritization` adicional será necessário no identificador. O `prioritization` é uma matriz ordenada e deve especificar qual usuário deve ser excluído se forem encontrados vários usuários. Isso significa que a exclusão de usuários não ocorrerá se mais de um usuário corresponder a uma priorização.

Os valores permitidos para o vetor são: `identified`, `unidentified`, `most_recently_updated`. `most_recently_updated` refere-se à priorização do usuário atualizado mais recentemente.

Somente uma das opções a seguir pode existir na matriz de priorização por vez:
- `identified` refere-se à priorização de um usuário com uma `external_id`
- `unidentified` refere-se à priorização de um usuário sem um `external_id`

## Exemplo de solicitação
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "external_ids": ["external_identifier1", "external_identifier2"],
  "braze_ids": ["braze_identifier1", "braze_identifier2"],
  "user_aliases": [
    {
      "alias_name": "user_alias1", "alias_label": "alias_label1"
    },
    {
      "alias_name": "user_alias2", "alias_label": "alias_label2"
    }
  ],
  "email_addresses": [
    {
      "email": "john.smith@braze.com",
      "prioritization": ["unidentified", "most_recently_updated"]
    }
  ]
}'
```

## Resposta

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "deleted" : (required, integer) number of user ids queued for deletion
}
```
{% endapi %}


