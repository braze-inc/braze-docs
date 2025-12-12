---
nav_title: "OBTER: Dados de receita de exportação"
article_title: "OBTER: Dados de receita de exportação"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Exportar dados de receita\"."

---
{% api %}
# Exportar dados de receita por tempo
{% apimethod get %}
/purchases/revenue_series
{% endapimethod %}

> Use esse endpoint para retornar o total de dinheiro gasto em seu app em um intervalo de tempo.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f6e05f9a-13c0-4d66-8caa-4a376d25749f{% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `purchases.revenue_series`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='purchases product list' %}

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `ending_at` | Opcional | Datetime ([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | Data em que a exportação de dados deve terminar. Padrões para o momento da solicitação. |
| `length` | Obrigatória | Inteiro | Número máximo de dias antes de `ending_at` para incluir na série retornada. Deve estar entre 1 e 100 (inclusive). |
| `unit` | Opcional | String | Unidade de tempo entre os pontos de dados. Pode ser dia ou hora; o padrão é dia. |
| `app_id` | Opcional | String | Identificador da API do app recuperado da página [Chaves de API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/). Se excluído, serão retornados os resultados de todos os apps em um espaço de trabalho. |
| `product` | Opcional | String | Nome do produto para filtrar a resposta por. Se excluído, os resultados de todos os apps serão retornados. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação

```
curl --location --request GET 'https://rest.iad-01.braze.com/purchases/revenue_series?length=100' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Resposta

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "message": (required, string) the status of the export, returns 'success' when completed without errors,
  "data" : [
    {
      "time" : (string) the date as ISO 8601 date,
      "revenue" : (int) amount of revenue for the time period
      },
    ...
  ]
}
```

{% endapi %}

{% alert tip %}
Para obter ajuda com exportações de CSV e API, acesse [Resolução de problemas de exportação]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}
