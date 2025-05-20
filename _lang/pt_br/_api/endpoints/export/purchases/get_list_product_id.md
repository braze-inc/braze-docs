---
nav_title: "OBTER: Exportar IDs de produtos"
article_title: "OBTER: Exportar IDs de produtos"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre sobre o endpoint da Braze \"Exportar IDs de produtos\"."

---
{% api %}
# Exportar IDs de produtos
{% apimethod get %}
/purchases/product_list
{% endapimethod %}

> Use esse ponto de extremidade para retornar uma lista paginada de IDs de produtos.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#dff4ed40-81f5-451d-9d44-accc0e932285{% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `purchases.product_list`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='purchases product list' %}

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `page` | Opcional | String | A página da lista de produtos que você deseja visualizar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação

{% raw %}
```
https://rest.iad-01.braze.com/purchases/product_list?page=1
```
{% endraw %}

## Resposta

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "products": [
    "product_name" (string), the name of the product
  ],
  "message": "success"
}
```

{% endapi %}

{% alert tip %}
Para obter ajuda com exportações de CSV e API, acesse [Resolução de problemas de exportação]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}
