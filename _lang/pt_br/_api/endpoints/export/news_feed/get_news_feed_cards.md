---
nav_title: "OBTER: Exportar lista de cartões do feed de notícias"
article_title: "OBTER: Exportar lista de cartões do feed de notícias"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Exportar lista de cartões do feed de notícias\"."

---
{% api %}
# Exportar lista de cartões do feed de notícias
{% apimethod get %}
/feed/list
{% endapimethod %}

> Use esse endpoint para exportar uma lista de cartões do Feed de notícias, cada um dos quais incluirá seu nome e o identificador da API do cartão.

Os cartões são retornados em grupos de 100 classificados por hora de criação (do mais antigo para o mais recente, por padrão).

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9fa7a3bc-4a02-4de2-bc4c-8f111750665e {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `feed.list`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | -------- | --------- | ----------- |
| `page` | Opcional | Inteiro   | A página de cartões a ser retornada, o padrão é 0 (retorna o primeiro conjunto de até 100). |
| `include_archived` | Opcional | Booleano   | Se deve ou não incluir cartões arquivados; o padrão é false. |
| `sort_direction` | Opcional | String | \- Classifique o tempo de criação do mais novo para o mais antigo: passe o valor `desc`.<br> \- Classifique o tempo de criação do mais antigo para o mais recente: passe o valor `asc`. <br><br>Se `sort_direction` não estiver incluído, a ordem padrão será da mais antiga para a mais recente. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação
```
curl --location --request GET 'https://rest.iad-01.braze.com/feed/list?page=1&include_archived=true&sort_direction=desc' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Resposta

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "cards" : [
        {
            "id" : (string) the card API identifier,
            "type" : (string) type of the card - NewsItem (classic cards), CaptionedImage, Banner
            "title" : (string) the title of the card,
            "tags" : (array) the tag names associated with the card
        },
        ...
    ]
}
```

{% alert tip %}
Para obter ajuda com exportações de CSV e API, acesse [Resolução de problemas de exportação]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
