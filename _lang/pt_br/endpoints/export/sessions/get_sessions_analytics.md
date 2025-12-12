---
nav_title: "OBTER: Exportar sessões de aplicativos por horário"
article_title: "Obter: Exportar sessões de app por tempo"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Exportar sessões de app por tempo\""

---
{% api %}
# Exportar sessão do app por hora
{% apimethod get %}
/sessions/data_series
{% endapimethod %}

> Use esse endpoint para recuperar uma série do número de sessões do seu app em um período de tempo designado.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#79efb6a9-62ec-4b8a-bf4a-e96313aa4be1 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `sessions.data_series`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação

| Parâmetro| Obrigatória | Tipo de dados | Descrição |
| -------- | -------- | --------- | ----------- |
| `length` | Obrigatória | Inteiro | Número máximo de unidades (dias ou horas) antes de `ending_at` para incluir na série retornada. Deve estar entre 1 e 100 (inclusive). |
| `unit` | Opcional | String | Unidade de tempo entre os pontos de dados. Pode ser `day` ou `hour`, o padrão é `day`.  |
| `ending_at` | Opcional | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | Data em que a série de dados deve terminar. O padrão é a hora da solicitação. |
| `app_id` | Opcional | String | Identificador da API do aplicativo recuperado da página [Chaves de API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) para limitar a análise de dados a um aplicativo específico. |
| `segment_id` | Opcional | String | Consulte [Identificador da API de segmento]({{site.baseurl}}/api/identifier_types/). ID do segmento que indica o segmento com análise de dados ativada para o qual as sessões devem ser retornadas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/sessions/data_series?length=14&unit=day&ending_at=2018-06-28T23:59:59-5:00&app_id={{app_identifier}}&segment_id={{segment_identifier}}' \
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
            "time" : (string) point in time - as ISO 8601 extended when unit is "hour" and as ISO 8601 date when unit is "day",
            "sessions" : (int)
        },
        ...
    ]
}
```

{% alert tip %}
Para obter ajuda com exportações de CSV e API, acesse [Resolução de problemas de exportação]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
