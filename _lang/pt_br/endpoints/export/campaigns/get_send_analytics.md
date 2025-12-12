---
nav_title: "OBTER: Exportar análises de envio"
article_title: "OBTER: Exportação Enviar análises de dados"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o o endpoint da Braze \"Exportar análises de envio\"."

---
{% api %}
# Exportar análises de envio
{% apimethod get %}
/sends/data_series
{% endapimethod %}

> Use esse endpoint para recuperar uma série diária de várias estatísticas de um rastreamento `send_id` para campanhas da API.

A Braze armazena análises de dados de envio por 14 dias após o envio. As conversões da campanha serão atribuídas ao `send_id` mais recente que um determinado usuário recebeu da campanha.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#76f822a8-a13b-4bfb-b20e-72b5013dfe86 {% endapiref %}

## Pré-requisitos

Esse endpoint é apenas para campanhas de API. Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `sends.data_series`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | -------- | --------- |------------ |
| `campaign_id` | Obrigatória | String | Consulte o [identificador da API da campanha]({{site.baseurl}}/api/identifier_types/). |
| `send_id` | Obrigatória | String | Consulte [Enviar identificador da API]({{site.baseurl}}/api/identifier_types/). |
| `length` | Obrigatória | Inteiro | Número máximo de dias antes de `ending_at` para incluir na série retornada. Deve estar entre 1 e 100 (inclusive). |
| `ending_at` | Opcional | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | Data em que a série de dados deve terminar. O padrão é a hora da solicitação. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação

{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/sends/data_series?campaign_id={{campaign_identifier}}&send_id={{send_identifier}}&length=30&ending_at=2014-12-10T23:59:59-05:00' \
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
            "time": (string) the date as ISO 8601 date,
            "messages": {
                "ios_push" : [
                    {
                      "variation_name": (string) variation name,
                      "sent": (int) the number of sends,
                      "delivered": (int) the number of messages successfully delivered,
                      "undelivered": (int) the number of undelivered,
                      "delivery_failed": (int) the number of rejected,
                      "direct_opens": (int) the number of direct opens,
                      "total_opens": (int) the number of total opens,
                      "bounces": (int) the number of bounces,
                      "body_clicks": (int) the number of body clicks,
                      "revenue": (float) the number of dollars of revenue (USD),
                      "unique_recipients": (int) the number of unique recipients at the campaign-level,
                      "conversions": (int) the number of conversions,
                      "conversions_by_send_time": (int) the number of conversions attributed to the date the campaign was sent,
                      "conversions1": (optional, int) the number of conversions for the second conversion event,
                      "conversions1_by_send_time": (optional, int) the number of conversions for the second conversion event attributed to the date the campaign was sent,
                      "conversions2": (optional, int) the number of conversions for the third conversion event,
                      "conversions2_by_send_time": (optional, int) the number of conversions for the third conversion event attributed to the date the campaign was sent,
                      "conversions3": (optional, int) the number of conversions for the fourth conversion event,
                      "conversions3_by_send_time": (optional, int) the number of conversions for the fourth, conversion event attributed to the date the campaign was sent
                      }
                  ]
            },
        "conversions_by_send_time": (optional, int),
        "conversions1_by_send_time": (optional, int),
        "conversions2_by_send_time": (optional, int),
        "conversions3_by_send_time": (optional, int),
        "conversions": (int),
        "conversions1": (optional, int),
        "conversions2": (optional, int),
        "conversions3": (optional, int),
        "unique_recipients": (int),
        "revenue": (optional, float)
      }
    ],
  "message": "success"
}
```

{% alert tip %}
Para obter ajuda com exportações de CSV e API, acesse [Resolução de problemas de exportação]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
