---
nav_title: "DELETE: Excluir campo de catálogo"
article_title: "DELETE: Excluir campo do catálogo"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint da Braze \"Excluir campo do catálogo\"."

---
{% api %}
# Excluir campo de catálogo
{% apimethod delete %}
/catalogs/{catalog_name}/fields/{field_name}
{% endapimethod %}

> Use esse ponto de extremidade para excluir um campo de catálogo.

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `catalogs.delete_fields`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog fields' %}

## Parâmetros da jornada

| Parâmetro      | Obrigatória | Tipo de dados | Descrição                |
| -------------- | -------- | --------- | -------------------------- |
| `catalog_name` | Obrigatória | String    | Nome do catálogo.       |
| `field_name`   | Obrigatória | String    | Nome do campo do catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Exemplo de solicitação

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/fields/ratings' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
```

## Resposta

Existem dois códigos de status para este endpoint: `202` e `404`.

### Exemplo de resposta bem-sucedida

O código de status `202` poderia retornar o seguinte corpo de resposta:

```json
{
  "message": "success"
}
```

### Exemplo de resposta de erro

O código de status `404` poderia retornar o seguinte corpo de resposta. Consulte [Solução de problemas](#troubleshooting) para obter mais informações sobre os erros que você pode encontrar.

```json
{
  "errors": [
    {
      "id": "catalog-not-found",
      "message": "Could not find catalog",
      "parameters": [
        "catalog_name"
      ],
      "parameter_values": [
        "restaurants"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## Solução de problemas

A tabela a seguir lista os possíveis erros retornados e as etapas de solução de problemas associadas.

| Erro                           | Solução de problemas                                                  |
| ------------------------------- | ---------------------------------------------------------------- |
| `catalog-not-found`             | Verifique se o nome do catálogo é válido.                            |
| `field-referenced-by-selection` | Verifique se o campo de catálogo está sendo usado atualmente por uma seleção. |
| `field-is-inventory`            | Verifique se o campo de catálogo é usado como um campo de inventário.      |
| `invalid-field-name`            | Verifique se o nome do campo do catálogo é válido.                      |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
