---
nav_title: "OBTER: Listar detalhes do item do catálogo"
article_title: "OBTER: Lista Detalhes do item do catálogo"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint da Braze Listar informações do item do catálogo"

---
{% api %}
# Listar detalhes do item do catálogo
{% apimethod get %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> Use esse ponto de extremidade para retornar um item de catálogo e seu conteúdo.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#52c6631c-7366-48e5-9e0e-16de7b6285cc {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `catalogs.get_item`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## Parâmetros da jornada

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `catalog_name` | Obrigatória | String | Nome do catálogo. |
| `item_id` | Obrigatória | String | A ID do item do catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Parâmetros de solicitação

Não há corpo de solicitação para esse endpoint.

## Exemplo de solicitação

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Resposta

Existem dois códigos de status para este endpoint: `200` e `404`.

### Exemplo de resposta bem-sucedida

O código de status `200` poderia retornar o seguinte corpo de resposta.

```json
{
  "items": [
    {
      "id": "restaurant3",
      "Name": "Restaurant1",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": true,
      "Open_Time": "2022-11-01T09:03:19.967Z"
    }
  ],
  "message": "success"
}
```

### Exemplo de resposta de erro

O código de status `404` poderia retornar a seguinte resposta. Consulte [Solução de problemas](#troubleshooting) para obter mais informações sobre os erros que você pode encontrar.

```json
{
  "errors": [
    {
      "id": "item-not-found",
      "message": "Could not find item",
      "parameters": [
        "item_id"
      ],
      "parameter_values": [
        "restaurant34"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## Solução de problemas

A tabela a seguir lista os possíveis erros retornados e as etapas de solução de problemas associadas, se aplicável.

| Erro | Solução de problemas |
| --- | --- |
| `catalog-not-found` | Verifique se o nome do catálogo é válido. |
| `item-not-found` | Verifique se o item está no catálogo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
