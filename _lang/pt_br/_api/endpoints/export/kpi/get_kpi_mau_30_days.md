---
nav_title: "OBTER: Exportar usuários ativos mensais dos últimos 30 dias"
article_title: "OBTER: Exportar usuários ativos mensais dos últimos 30 dias"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint \"Exportar usuários ativos mensais dos últimos 30 dias\"."

---
{% api %}
# Exportar usuários ativos mensais dos últimos 30 dias
{% apimethod get %}
/kpi/mau/data_series
{% endapimethod %}

> Use esse ponto de extremidade para recuperar uma série diária do número total de usuários ativos únicos em uma janela contínua de 30 dias.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#68f45461-3bf1-425c-b918-f0bbf3f87149 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `kpi.mau.data_series`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação

| Parâmetro| Obrigatória | Tipo de dados | Descrição |
| -------- | -------- | --------- | ----------- |
| `length` | Obrigatória | Inteiro | Número máximo de dias antes de `ending_at` para incluir na série retornada. Deve estar entre 1 e 100 (inclusive). |
| `ending_at` | Opcional | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | Data em que a série de dados deve terminar. O padrão é a hora da solicitação. |
| `app_id` | Opcional | String | Identificador da API do app recuperado da página [Chaves de API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/). Se excluído, serão retornados os resultados de todos os apps no espaço de trabalho. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/kpi/mau/data_series?length=7&ending_at=2018-06-28T23:59:59-05:00&app_id={{app_identifier}}' \
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
            "mau" : (int) the number of monthly active users
        },
        ...
    ]
}
```

{% alert tip %}
Para obter ajuda com exportações de CSV e API, acesse [Resolução de problemas de exportação]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
