---
nav_title: "POST: Criar Seleção de Catálogo"
article_title: "POST: Criar Seleção de Catálogo"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Criar seleção de catálogo\""

---
{% api %}
# Criar seleção de catálogo
{% apimethod post %}
/catalogs/{catalog_name}/selections
{% endapimethod %}

> Use este endpoint para criar uma seleção em seu catálogo.

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `catalogs.create_selection`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog selections' %}

## Parâmetros da jornada

| Parâmetro      | Obrigatória | Tipo de dados | Descrição          |
| -------------- | -------- | --------- | -------------------- |
| `catalog_name` | Obrigatória | String    | Nome do catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Parâmetros de solicitação

| Parâmetro   | Obrigatória | Tipo de dados | Descrição                                                                                                                                                        |
| ----------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `selection` | Obrigatória | Objeto    | Um objeto que contém critérios de seleção. Os objetos de seleção podem conter `name`, `description`, `filters`, `results_limit`, `sort_field` e `sort_order`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Exemplo de Solicitação

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/selections' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "selection": {
    "name": "favorite-restaurants",
    "description": "Favorite restaurants in NYC",
    "filters": [
      {
        "field": "City",
        "operator": "equals",
        "value": "NYC"
      },
      {
        "field": "Rating",
        "operator": "greater than",
        "value": 7
      }
    ]
  }
}'
```

### Operadores de filtro

| Tipo de campo | Operadores suportados                                     |
| ---------- | ------------------------------------------------------- |
| `string`   | `equals`, `does not equal`                              |
| `number`   | `equals`, `does not equal`, `greater than`, `less than` |
| `boolean`  | `is`                                                    |
| `time`     | `before`, `after`                                       |
| `array`    | `includes value`, `does not include value`              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Resposta

Há três respostas de código de status para esse endpoint: `202`, `400` e `404`.

### Exemplo de resposta bem-sucedida

O código de status `202` poderia retornar o seguinte corpo de resposta.

```json
{
  "message": "success"
}
```

### Exemplo de resposta de erro

O código de status `400` poderia retornar o seguinte corpo de resposta. Consulte [Solução de problemas](#troubleshooting) para obter mais informações sobre os erros que você pode encontrar.

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

| Erro                                | Solução de problemas                                                                               |
|--------------------------------------|-----------------------------------------------------------------------------------------------|
| `catalog-not-found`                  | Verifique se o nome do catálogo é válido.                                                         |
| `company-size-limit-already-reached` | O limite de tamanho do armazenamento do catálogo foi atingido.                                                    |
| `selection-limit-reached`            | O limite de seleções do catálogo foi atingido.                                                      |
| `invalid-selection`                  | Verifique se a seleção é válida.                                                            |
| `too-many-filters`                   | Verifique se a seleção tem muitos filtros.                                                  |
| `selection-name-already-exists`      | Verifique se o nome da seleção já existe no catálogo.                                    |
| `selection-has-invalid-filter`       | Verifique se o filtro de seleção é válido.                                                       |
| `selection-invalid-results-limit`    | Verifique se o limite de resultados da seleção é válido.                                                |
| `invalid-sorting`                    | Verifique se a ordenação da seleção é válida.                                                      |
| `invalid-sort-field`                 | Verifique se o campo de ordenação por seleção é válido.                                                   |
| `invalid-sort-order`                 | Verifique se a ordem de seleção está correta.                                                   |
| `selection-contains-too-many-arrays` | Verifique se a seleção contém mais de um campo com o tipo `array`. Apenas um é suportado. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
