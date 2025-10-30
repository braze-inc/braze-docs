---
nav_title: "OBTER: Listar vários detalhes de itens do catálogo"
article_title: "OBTER: Listar vários detalhes de itens de catálogo"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "Este artigo traz informações sobre sobre o endpoint da Braze \"Listar vários detalhes de itens de catálogo\"."

---
{% api %}
# Listar vários detalhes de itens do catálogo
{% apimethod get %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> Use esse ponto de extremidade para retornar vários itens de catálogo e seu conteúdo.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#63a19dd5-10e0-4649-bdf0-097216748bbb {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `catalogs.get_items`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## Parâmetros da jornada

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `catalog_name` | Obrigatória | String | Nome do catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Parâmetros de consulta

Observe que cada chamada a esse endpoint retornará 50 itens. Para um catálogo com mais de 50 itens, use o cabeçalho `Link` para recuperar os dados na próxima página, conforme mostrado no exemplo de resposta a seguir.

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `cursor` | Opcional | String | Determina a paginação dos itens do catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Parâmetros de solicitação

Não há corpo de solicitação para esse endpoint.

## Exemplos de solicitações

### Sem cursor

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### Com cursor

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Resposta

Há três respostas de código de status para esse endpoint: `200`, `400` e `404`.

### Exemplo de resposta bem-sucedida

O código de status `200` poderia retornar o seguinte cabeçalho e corpo de resposta.

{% alert note %}
O cabeçalho `Link` não existirá se o catálogo tiver até 50 itens. Nas chamadas sem cursor, o endereço `prev` não será exibido. Ao olhar a última página de itens, `next` não será exibido.
{% endalert %}

```
Link: </catalogs/all_restaurants/items?cursor=c2tpcDow>; rel="prev",</catalogs/all_restaurants/items?cursor=c2tpcDoxMDA=>; rel="next"
```

```json
{
  "items": [
    {
      "id": "restaurant1",
      "Name": "Restaurant1",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": true,
      "Open_Time": "2022-11-02T09:03:19.967Z"
    },
    {
      "id": "restaurant2",
      "Name": "Restaurant2",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 10,
      "Loyalty_Program": true,
      "Open_Time": "2022-11-02T09:03:19.967Z"
    },
    {
      "id": "restaurant3",
      "Name": "Restaurant3",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": false,
      "Open_Time": "2022-11-02T09:03:19.967Z"
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
      "id": "invalid-cursor",
      "message": "'cursor' is not valid",
      "parameters": [
        "cursor"
      ],
      "parameter_values": [
        "bad-cursor"
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
| `invalid-cursor` | Verifique se o site `cursor` é válido. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
