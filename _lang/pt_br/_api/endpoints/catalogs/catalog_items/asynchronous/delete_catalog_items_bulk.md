---
nav_title: "DELETE: Excluir vários itens do catálogo"
article_title: "DELETE: Excluir vários itens do catálogo"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Excluir vários itens do catálogo\"."

---
{% api %}
# exclui vários itens do catálogo
{% apimethod delete %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> Use esse ponto de extremidade para excluir vários itens em seu catálogo.

Cada solicitação pode suportar até 50 itens. Esse ponto de extremidade é assíncrono.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#647c82e8-8b38-4df2-bde2-b1d8e19fd332 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `catalogs.delete_items`.

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
| `items` | Obrigatória | Vetor | Um vetor que contém objetos de item. Os objetos de item devem conter um `id` referenciando os itens que a Braze deve excluir. São permitidos até 50 objetos de item por solicitação. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Exemplo de solicitação

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {"id": "restaurant1"},
    {"id": "restaurant2"},
    {"id": "restaurant3"}
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
      "id": "items-missing-ids",
      "message": "There are 1 item(s) that do not have ids",
      "parameters": [],
      "parameter_values": []
    }
  ],
  "message": "Invalid Request",
}
```

## Solução de problemas

A tabela a seguir lista os possíveis erros retornados e as etapas de solução de problemas associadas.

| Erro | Solução de problemas |
| --- | --- |
| `catalog-not-found` | Verifique se o nome do catálogo é válido. |
| `ids-too-large` | Os IDs de item não podem ter mais de 250 caracteres. |
| `ids-not-unique` | Verifique se os IDs do item são exclusivos na solicitação. |
| `ids-not-strings` | As IDs de item devem ser do tipo string. |
| `items-missing-ids` | Alguns itens não têm IDs de item. Verifique se cada item tem um ID de item. |
| `invalid-ids` | Os IDs de itens só podem conter letras, números, hifens e underscores. |
| `request-includes-too-many-items` | Sua solicitação tem muitos itens. O limite de itens por solicitação é de 50. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
