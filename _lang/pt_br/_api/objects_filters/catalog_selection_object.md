---
nav_title: "Objeto de seleção de catálogo"
article_title: Objeto de Seleção de Catálogo da API
page_order: 12
page_type: reference
description: "Este artigo de referência explica os diferentes componentes do objeto de seleção de catálogo."
tool: Catalogs

---

# Objeto de seleção de catálogo

> Ao criar uma seleção de catálogo, você pode fornecer um objeto de seleção para definir os critérios de filtragem, ordenação e limitação para os itens retornados do seu catálogo.

O objeto `selection` permite que você especifique quais itens do seu catálogo devem ser incluídos na seleção com base em filtros, como eles devem ser ordenados e quantos resultados retornar. Use este objeto ao criar seleções de catálogo através da API.

## Corpo do objeto

```json
{
  "selection": {
    "name": "Sale",
    "description": "Sales Collection",
    "external_id": "12345678",
    "source": "Shopify",
    "filters": [
      {
        "field": "collection",
        "operator": "includes value",
        "value": "Best Seller"
      },
      {
        "field": "collection",
        "operator": "does not include value",
        "value": "Sale"
      }
    ],
    "results_limit": 5,
    "sort_field": "id",
    "sort_order": "asc"
  }
}
```

## Detalhes do objeto

| Chave | Obrigatória | Tipo de dados | Descrição |
| --- | -------- | --------- | ----------- |
| `name` | Obrigatória | String | O nome da seleção de catálogo. |
| `description` | Opcional | String | Uma descrição da seleção de catálogo. |
| `external_id` | Obrigatória | String | Um identificador único para a seleção. |
| `source` | Obrigatória | String | A fonte dos dados do catálogo. Para catálogos Shopify, defina isso como `"Shopify"`. Para catálogos não Shopify, use uma string descritiva como `"custom"` ou o nome da sua integração. |
| `filters` | Opcional | Vetor de objetos | Um array de objetos de filtro a serem aplicados aos itens do catálogo. Você pode especificar até quatro filtros por solicitação. Se nenhum filtro for fornecido, todos os itens do catálogo são incluídos. |
| `results_limit` | Opcional | Inteiro | O número máximo de resultados a serem retornados. Deve ser um número entre 1 e 50. |
| `sort_field` | Opcional | String | O campo para ordenar os resultados. Isso deve ser emparelhado com `sort_order`. Se tanto `sort_field` quanto `sort_order` não estiverem presentes, os resultados são retornados em ordem aleatória. |
| `sort_order` | Opcional | String | A ordem para classificar os resultados. Os valores aceitos são `"asc"` (crescente) ou `"desc"` (decrescente). Isso deve ser emparelhado com `sort_field`. Se tanto `sort_field` quanto `sort_order` não estiverem presentes, os resultados são retornados em ordem aleatória. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Objeto de filtro

Cada objeto de filtro no array `filters` contém os campos descritos na tabela a seguir.

| Chave | Obrigatória | Tipo de dados                                   | Descrição |
| --- | -------- | ------------------------------------------- | ----------- |
| `field`    | Obrigatória | String                                      | O campo do catálogo a ser filtrado. |
| `operator` | Obrigatória | String                                      | O operador de comparação a ser usado para filtragem. Exemplos incluem `"includes value"` e `"does not include value"`. |
| `value`    | Obrigatória | Varia (string, número, booleano, tempo)     | O valor a ser comparado. Isso deve corresponder ao tipo de dado do campo do catálogo subjacente (por exemplo, string, número, booleano, tempo). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
A API suporta um máximo de quatro filtros por solicitação de seleção. No dashboard do Braze, você pode adicionar até 10 filtros por seleção. Os filtros são aplicados na ordem em que aparecem no array.
{% endalert %}
