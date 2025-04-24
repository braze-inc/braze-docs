---
nav_title: "OBTER: Exportar Detalhes do Cartão do Feed de Notícias"
article_title: "OBTER: Exportar Detalhes do Cartão do Feed de Notícias"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o o endpoint da Braze \"Exportar Detalhes do Cartão do Feed de Notícias\"."

---
{% api %}
# Exportar detalhes do cartão do feed de notícias
{% apimethod get %}
/feed/details
{% endapimethod %}

> Use este endpoint para recuperar informações relevantes sobre um cartão, que pode ser identificado pelo `card_id`.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5b1401a6-f12c-4827-82c9-8dc604f1671e {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `feed.details`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição            |
| --------- | -------- | --------- | ---------------------- |
| `card_id` | Obrigatória | String | Consulte [Identificador da API do cartão]({{site.baseurl}}/api/identifier_types/). <br><br> O [endereço]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_cards/) `card_id` para um determinado cartão pode ser encontrado na página [Chaves de API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) e na página de detalhes do cartão em seu dashboard, ou você pode usar o [endpoint Exportar lista de cartões do feed de notícias]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_cards/).|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/feed/details?card_id={{card_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Resposta

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) The status of the export, returns 'success' when completed without errors,
    "created_at" : (string) the ate created as ISO 8601 date,
    "updated_at" : (string) the ate last updated as ISO 8601 date,
    "name" : (string) the card name,
    "publish_at" : (string) the date the card was published as ISO 8601 date,
    "end_at" : (string) the date the card will stop displaying for users as ISO 8601 date,
    "tags" : (array) the tag names associated with the card,
    "title" : (string) the title of the card,
    "image_url" : (string) the image URL used by this card,
    "extras" : (dictionary) a dictionary containing key-value pair data attached to this card,
    "description" : (string) the description text used by this card,
    "archived": (boolean) whether this Card is archived,
    "draft": (boolean) whether this Card is a draft,
}
```

{% alert tip %}
Para obter ajuda com exportações de CSV e API, acesse [Resolução de problemas de exportação]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
