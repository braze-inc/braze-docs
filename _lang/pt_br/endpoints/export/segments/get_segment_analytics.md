---
nav_title: "OBTER: Análise de dados do segmento de exportação"
article_title: "OBTER: Análise de dados do segmento de exportação"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint de \"Exportar análises do segmento\"."

---
{% api %}
# Análise de dados do segmento de exportação
{% apimethod get %}
/segments/data_series
{% endapimethod %}

> Use esse ponto de extremidade para recuperar uma série diária do tamanho estimado de um segmento ao longo do tempo.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#62d9d142-cdec-4aea-a287-c13efea7415e {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `segments.data_series`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | -------- | --------- | ----------- |
| `segment_id` | Obrigatória | String | Consulte [Identificador da API de segmento]({{site.baseurl}}/api/identifier_types/).<br><br> O [endereço]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) `segment_id` para um determinado segmento pode ser encontrado na página [Chaves de API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) em sua conta Braze ou você pode usar o [endpoint Exportar lista de segmentos]({{site.baseurl}}/api/endpoints/export/segments/get_segment/).  |
| `length` | Obrigatória | Inteiro | Número máximo de dias antes de `ending_at` para incluir na série retornada. Deve estar entre 1 e 100 (inclusive). |
| `ending_at` | Opcional | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | Data em que a série de dados deve terminar. O padrão é a hora da solicitação. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/segments/data_series?segment_id={{segment_identifier}}&length=14&ending_at=2018-06-27T23:59:59-5:00' \
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
            "time" : (string) the date as ISO 8601 date,
            "size" : (int) the size of the segment on that date
        },
        ...
    ]
}
```

{% alert tip %}
Para obter ajuda com exportações de CSV e API, acesse [Resolução de problemas de exportação]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
