---
nav_title: "OBTER: Exportar análise de dados do cartão do feed de notícias"
article_title: "OBTER: Exportar análise de dados do cartão do feed de notícias"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Exportar análise de dados do cartão do feed de notícias\"."

---
{% api %}
# Exportar análise de dados de cartões do feed de notícias
{% apimethod get %}
/feed/data_series
{% endapimethod %}

> Use esse ponto de extremidade para recuperar uma série diária de estatísticas de engajamento de um cartão ao longo do tempo.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9cdc3b1e-641e-4d62-b9e8-42d04ee9d4d8 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `feed.data_series`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação

| Parâmetro   | Obrigatória | Tipo de dados | Descrição |
| ----------- | -------- | --------- | ----------- |
| `card_id` | Obrigatória | String | Consulte [Identificador da API do cartão]({{site.baseurl}}/api/identifier_types/). <br><br> O [endereço]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_cards/) `card_id` para um determinado cartão pode ser encontrado na página [Chaves de API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) e na página de detalhes do cartão em seu dashboard, ou você pode usar o [endpoint Exportar lista de cartões do feed de notícias]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_cards/).|
| `length` | Obrigatória | Inteiro | Número máximo de unidades (dias ou horas) antes de `ending_at` para incluir na série retornada. Deve estar entre 1 e 100 (inclusive). |
| `unit` | Opcional | String | Unidade de tempo entre os pontos de dados. Pode ser `day` ou `hour`, o padrão é `day`.  |
| `ending_at` | Opcional | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | Data em que a série de dados deve terminar. O padrão é a hora da solicitação. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/feed/data_series?card_id={{card_identifier}}&length=14&unit=day&ending_at=2018-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Resposta

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) the point in time - as ISO 8601 extended when unit is "hour" and as ISO 8601 date when unit is "day",
            "clicks" : (int) the number of clicks,
            "impressions" : (int) the number of impressions,
            "unique_clicks" : (int) the number of unique clicks,
            "unique_impressions" : (int) the number of unique impressions
        },
        ...
    ]
}
```

{% alert tip %}
Para obter ajuda com exportações de CSV e API, acesse [Resolução de problemas de exportação]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
