---
nav_title: "PATCH: Editar vários itens do catálogo"
article_title: "PATCH: Editar Vários Itens do Catálogo"
alias: /catalogs_items_patch/
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Editar Vários Itens do Catálogo\"."

---
{% api %}
# edita vários itens do catálogo
{% apimethod patch %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> Use este endpoint para editar vários itens existentes em seu catálogo.

Cada solicitação pode suportar até 50 itens. Esse ponto de extremidade é assíncrono.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#03f3548e-4139-4f60-812d-7e1a695a738a {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `catalogs.update_items`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog item' %}

## Parâmetros da jornada

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `catalog_name` | Obrigatória | String | Nome do catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `items` | Obrigatória | Vetor | Uma matriz que contém objetos de item. Os objetos de item devem conter campos que existem no catálogo. Até 50 objetos de item são permitidos por solicitação. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Exemplo de solicitação

```
curl --location --request PATCH 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "id": "restaurant1",
      "Name": "Restaurant",
      "Loyalty_Program": false,
      "Location": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      },
      "Top_Dishes": {
        "$add": [
          "Biscuits",
          "Coleslaw"
        ],
        "$remove": [
          "French Fries"
        ]
      },
      "Open_Time": "2021-09-03T09:03:19.967+00:00"
    },
    {
      "id": "restaurant3",
      "City": "San Francisco",
      "Rating": 2,
      "Top_Dishes": [
        "Buffalo Wings",
        "Philly Cheesesteak"
      ]
    }
  ]
}'
```

{% alert note %}
Os operadores `$add` e `$remove` são aplicáveis somente a campos do tipo matriz e são compatíveis apenas com os pontos de extremidade PATCH.
{% endalert %}

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
| `catalog-not-found` | Verifique se o nome do catálogo é válido. |
| `ids-too-large` | Os IDs de item não podem ter mais de 250 caracteres. |
| `ids-not-strings` | As IDs de item devem ser do tipo string. |
| `ids-not-unique` | As IDs de item devem ser exclusivas na solicitação. |
| `invalid-ids` | Os IDs de itens só podem conter letras, números, hifens e underscores. |
| `invalid-fields` | Confirme se todos os campos que está enviando na solicitação de API já existem no catálogo. Isso não está relacionado ao campo ID mencionado no erro. |
| `invalid-keys-in-value-object` | As chaves de objeto do item não podem incluir `.` ou `$`. |
| `items-missing-ids` | Alguns itens não têm IDs de item. Verifique se cada item tem um ID de item. |
| `item-array-invalid` | `items` deve ser um vetor de objetos. |
| `items-too-large` | Os valores dos itens não podem exceder 5.000 caracteres. |
| `request-includes-too-many-items` | Sua solicitação tem muitos itens. O limite de itens por solicitação é de 50. |
| `too-deep-nesting-in-value-object` | Os objetos de item não podem ter mais de 50 níveis de aninhamento. |
| `unable-to-coerce-value` | Os tipos de itens não podem ser convertidos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
