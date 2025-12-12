---
nav_title: "PUT: Substituir item de catálogo"
article_title: "PUT: Substituir item de catálogo"
search_tag: Endpoint
page_order: 6

layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint do Braze do item de catálogo Replace."

---
{% api %}
# Substituir item de catálogo
{% apimethod put %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> Use esse ponto de extremidade para substituir um item em seu catálogo.

Se o `item_id` não for encontrado, este endpoint criará o item em seu catálogo. Este endpoint é síncrono.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b2871ed7-734e-4a37-b8f1-e11584e569f5 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `catalogs.replace_item`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## Parâmetros da jornada

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `catalog_name` | Obrigatória | String | Nome do catálogo. |
| `item_id` | Obrigatória | String | A ID do item do catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `items` | Obrigatória | Vetor | Um vetor que contém objetos de item. Os objetos de item devem conter campos que existem no catálogo, exceto o campo `id`. Somente um objeto de item é permitido por solicitação. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Exemplo de solicitação

```
curl --location --request PUT 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "Name": "Restaurant",
      "Loyalty_Program": false,
      "Location": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      },
      "Top_Dishes": [
        "Hamburger",
        "Deluxe Cheeseburger"
      ],
      "Open_Time": "2021-09-03T09:03:19.967+00:00"
    }
  ]
}'
```

## Resposta

Há três respostas de código de status para esse endpoint: `200`, `400` e `404`.

### Exemplo de resposta bem-sucedida

O código de status `200` poderia retornar o seguinte corpo de resposta.

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
      "id": "invalid-fields",
      "message": "Some of the fields given do not exist in the catalog",
      "parameters": [
        "id"
      ],
      "parameter_values": [
        "restaurant1"
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
| `arbitrary-error` | Ocorreu um erro arbitrário. Tente novamente ou entre em contato com [o suporte]({{site.baseurl}}/support_contact/). |
| `catalog-not-found` | Verifique se o nome do catálogo é válido. |
| `filtered-set-field-too-long` | O valor do campo está sendo usado em um conjunto filtrado que excede o limite de caracteres de um item. |
| `id-in-body` | Remova quaisquer IDs de item no corpo da solicitação. |
| `ids-too-large` | O limite de caracteres para cada ID de item é de 250 caracteres. |
| `invalid-ids` | Os caracteres compatíveis com os nomes de ID de item são letras, números, hífens e sublinhados. |
| `invalid-fields` | Confirme se todos os campos que está enviando na solicitação de API já existem no catálogo. Isso não está relacionado ao campo ID mencionado no erro. |
| `invalid-keys-in-value-object` | As chaves de objeto do item não podem incluir `.` ou `$`. |
| `item-already-exists` | O item já existe no catálogo. |
| `item-array-invalid` | `items` deve ser um vetor de objetos. |
| `items-too-large` | O limite de caracteres para cada item é de 5.000 caracteres. |
| `request-includes-too-many-items` | Você só pode criar um item de catálogo por solicitação. |
| `too-deep-nesting-in-value-object` | Os objetos de item não podem ter mais de 50 níveis de aninhamento. |
| `unable-to-coerce-value` | Os tipos de itens não podem ser convertidos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
