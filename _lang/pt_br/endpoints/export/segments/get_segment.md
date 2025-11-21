---
nav_title: "OBTER: Exportar lista de segmentos"
article_title: "OBTER: Exportar lista de segmentos"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Exportar lista de segmentos\"."

---
{% api %}
# Exportar lista de segmentos
{% apimethod get %}
/segments/list
{% endapimethod %}

> Use esse endpoint para exportar uma lista de segmentos, cada um dos quais incluirá seu nome, o identificador da API de segmentos e se tem a análise de dados ativada.

Os segmentos são retornados em grupos de 100 classificados por hora de criação (do mais antigo ao mais recente, por padrão). Os segmentos arquivados não estão incluídos.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1349e6f4-3ce7-4e60-b3e9-951c99c0993f {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `segments.list`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação

| Parâmetro| Obrigatória | Tipo de dados | Descrição |
| -------- | -------- | --------- | ----------- |
| `page` | Opcional | Inteiro | A página de segmentos a ser retornada; o padrão é 0 (retorna o primeiro conjunto de até 100). |
| `sort_direction` | Opcional | String | \- Classifique o tempo de criação do mais novo para o mais antigo: passe o valor `desc`.<br> \- Classifique o tempo de criação do mais antigo para o mais recente: passe o valor `asc`. <br><br>Se `sort_direction` não estiver incluído, a ordem padrão será da mais antiga para a mais recente. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação
```
curl --location --request GET 'https://rest.iad-01.braze.com/segments/list?page=1&sort_direction=desc' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Resposta

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "segments" : [
        {
            "id" : (string) the Segment API identifier,
            "name" : (string) segment name,
            "analytics_tracking_enabled" : (boolean) whether the segment has analytics tracking enabled,
            "tags" : (array) the tag names associated with the segment formatted as strings
        },
        ...
    ]
}
```

{% alert tip %}
Para obter ajuda com exportações de CSV e API, acesse [Resolução de problemas de exportação]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
