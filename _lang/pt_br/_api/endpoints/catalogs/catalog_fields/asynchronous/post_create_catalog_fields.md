---
nav_title: "POST: Criar campos de catálogo"
article_title: "POST: Criar campos do catálogo"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o o endpoint da Braze \"Criar campos do catálogo\"."

---
{% api %}
# Criar campos de catálogo
{% apimethod post %}
/catalogs/{catalog_name}/fields
{% endapimethod %}

> Use esse ponto de extremidade para criar vários campos em seu catálogo.

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `catalogs.create_fields`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog fields' %}

## Parâmetros da jornada

| Parâmetro      | Obrigatória | Tipo de dados | Descrição          |
| -------------- | -------- | --------- | -------------------- |
| `catalog_name` | Obrigatória | String    | Nome do catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição                                                                                                  |
| --------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------ |
| `fields`  | Obrigatória | Vetor     | Um vetor que contém objetos de campo. Os objetos de campos devem conter o nome e o tipo dos novos campos. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Exemplo de solicitação

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/fields' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "fields": [
    {
      "name": "Name",
      "type": "string"
    },
    {
      "name": "Ratings",
      "type": "number"
    },
    {
      "name": "Loyalty_Program",
      "type": "boolean"
    },
    {
      "name": "Created_At",
      "type": "time"
    }
  ]
}'
```

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

| Erro                                | Solução de problemas                                                                                        |
|--------------------------------------|--------------------------------------------------------------------------------------------------------|
| `arbitrary-error`                    | Ocorreu um erro arbitrário. Tente novamente ou entre em contato com [o suporte]({{site.baseurl}}/support_contact/). |
| `catalog-not-found`                  | Verifique se o nome do catálogo é válido.                                                                  |
| `company-size-limit-already-reached` | O limite de tamanho do armazenamento do catálogo foi atingido.                                                             |
| `request-includes-too-many-fields`   | Cada solicitação pode suportar até 50 novos campos.                                                          |
| `catalog-exceeds-fields-limit`       | O catálogo não pode ter mais de 500 campos.                                                              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
