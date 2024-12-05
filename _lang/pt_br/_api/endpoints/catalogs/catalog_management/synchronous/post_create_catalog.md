---
nav_title: "POST: Criar catálogo"
article_title: "POST: Criar catálogo"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Criar catálogo Braze."

---
{% api %}
# Criar catálogo
{% apimethod post %}
/catalogs
{% endapimethod %}

> Use esse ponto de extremidade para criar um catálogo.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#af9f3e2d-b7e7-49e7-aa64-f4652892be6e {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `catalogs.create`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='synchronous catalog' %}

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `catalogs` | Obrigatória | Vetor | Um vetor que contém objetos de catálogo. Somente um objeto de catálogo é permitido para essa solicitação. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Parâmetros do objeto de catálogo

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `name` | Obrigatória | String | O nome do catálogo que você deseja criar. |
| `description` | Obrigatória | String | A descrição do catálogo que você deseja criar. |
| `fields` | Obrigatória | Vetor | Um vetor de objetos em que o objeto contém as chaves `name` e `type`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Exemplo de solicitação
```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "catalogs": [
    {
      "name": "restaurants",
      "description": "My Restaurants",
      "fields": [
        {
          "name": "id",
          "type": "string"
        },
        {
          "name": "Name",
          "type": "string"
        },
        {
          "name": "City",
          "type": "string"
        },
        {
          "name": "Cuisine",
          "type": "string"
        },
        {
          "name": "Rating",
          "type": "number"
        },
        {
          "name": "Loyalty_Program",
          "type": "boolean"
        },
        {
          "name": "Location",
          "type": "object"
        },
        {
          "name": "Top_Dishes",
          "type": "array"
        },
        {
          "name": "Created_At",
          "type": "time"
        }
      ]
    }
  ]
}'
```

## Resposta

Existem dois códigos de status para este endpoint: `201` e `400`.

### Exemplo de resposta bem-sucedida

O código de status `201` poderia retornar o seguinte corpo de resposta.

```json
{
  "catalogs": [
    {
      "description": "My Restaurants",
      "fields": [
        {
          "name": "id",
          "type": "string"
        },
        {
          "name": "Name",
          "type": "string"
        },
        {
          "name": "City",
          "type": "string"
        },
        {
          "name": "Cuisine",
          "type": "string"
        },
        {
          "name": "Rating",
          "type": "number"
        },
        {
          "name": "Loyalty_Program",
          "type": "boolean"
        },
        {
          "name": "Location",
          "type": "object"
        },
        {
          "name": "Top_Dishes",
          "type": "array"
        },
        {
          "name": "Created_At",
          "type": "time"
        }
      ],
      "name": "restaurants",
      "num_items": 0,
      "updated_at": "2022-11-02T20:04:06.879+00:00"
    }
  ],
  "message": "success"
}
```

### Exemplo de resposta de erro

O código de status `400` poderia retornar o seguinte corpo de resposta. Consulte [Solução de problemas](#troubleshooting) para obter mais informações sobre os erros que você pode encontrar.

```json
{
  "errors": [
    {
      "id": "catalog-name-already-exists",
      "message": "A catalog with that name already exists",
      "parameters": [
        "name"
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

| Erro | Solução de problemas |
| --- | --- |
| `catalog-array-invalid` | `catalogs` deve ser um vetor de objetos. |
| `catalog-name-already-exists` | Já existe um catálogo com esse nome. |
| `catalog-name-too-large`  | O limite de caracteres para um nome de catálogo é 250. |
| `description-too-long` | O limite de caracteres para a descrição é de 250. |
| `field-names-not-unique` | O mesmo nome de campo é referenciado duas vezes. |
| `field-names-too-large` | O limite de caracteres para um nome de campo é 250. |
| `id-not-first-column` | O `id` deve ser o primeiro campo da matriz. Verifique se o tipo é uma string. |
| `invalid-catalog-name` | O nome do catálogo só pode incluir letras, números, hífens e sublinhados. |
| `invalid-field-names` | Os campos só podem incluir letras, números, hífens e sublinhados. |
| `invalid-field-types` | Verifique se os tipos de campo são válidos. |
| `invalid-fields` | `fields` não está formatado corretamente. |
| `too-many-catalog-atoms` | Você só pode criar um catálogo por solicitação. |
| `too-many-fields` | O limite de número de campos é 500. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
