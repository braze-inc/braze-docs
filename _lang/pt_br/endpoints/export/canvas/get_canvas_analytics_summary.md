---
nav_title: "OBTER: Exportar análises de resumo de dados do Canva"
article_title: "OBTER: Exportar análises de resumo de dados do Canvas"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Exportar análises de resumo de dados do Canvas da Braze."

---
{% api %}
# Exportar análises de resumo de dados do Canva
{% apimethod get %}
/canvas/data_summary
{% endapimethod %}

> O uso desse ponto de extremidade permite exportar rollups de dados de séries temporais para um Canvas, fornecendo um resumo conciso dos resultados do Canvas.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1eb1b760-6b00-4c03-bcfb-12646f2ba6da {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `canvas.data_summary`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | -------- | --------- | ----------- |
| `canvas_id` | Obrigatória | String | Veja [identificador da API canva]({{site.baseurl}}/api/identifier_types/). |
| `ending_at` | Obrigatória | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | Data em que a exportação de dados deve terminar. Padrões para o momento da solicitação. |
| `starting_at` | Opcional* | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | Data em que a exportação de dados deve começar. <br><br>\* Ou `length` ou `starting_at` é necessário. |
| `length` | Opcional* | String | Número máximo de dias antes de `ending_at` para incluir na série retornada. Deve estar entre 1 e 14 (inclusive). <br><br>\* Ou `length` ou `starting_at` é necessário. |
| `include_variant_breakdown` | Opcional | Booleano | Incluir ou não estatísticas variantes (padrão é `false`).  |
| `include_step_breakdown` | Opcional | Booleano | Se deve ou não incluir estatísticas de etapa (padrão é `false`). |
| `include_deleted_step_data` | Opcional | Booleano | Se deve ou não incluir estatísticas de etapa para etapas excluídas (padrão é `false`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_summary?canvas_id={{canvas_id}}&ending_at=2018-05-30T23:59:59-05:00&starting_at=2018-05-28T23:59:59-05:00&length=5&include_variant_breakdown=true&include_step_breakdown=true&include_deleted_step_data=true' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Resposta

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "data": {
    "name": (string) the Canvas name,
    "total_stats": {
      "revenue": (float) the number of dollars of revenue (USD),
      "conversions": (int) the number of conversions,
      "conversions_by_entry_time": (int) the number of conversions for the conversion event by entry time,
      "entries": (int) the number of entries
    },
    "variant_stats": (optional) {
      "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the variant {
        "name": (string) the name of variant,
        "revenue": (float) the number of dollars of revenue (USD),
        "conversions": (int) the number of conversions,
        "entries": (int) the number of entries
      },
      ... (more variants)
    },
    "step_stats": (optional) {
      "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the step {
        "name": (string) the name of step,
        "revenue": (float) the number of dollars of revenue (USD),
        "conversions": (int) the number of conversions,
        "conversions_by_entry_time": (int) the number of conversions for the conversion event by entry time,
        "messages": {
          "android_push": (name of channel) [
            {
              "sent": (int) the number of sends,
              "opens": (int) the number of opens,
              "influenced_opens": (int) the number of influenced opens,
              "bounces": (int) the number of bounces
              ... (more stats for channel)
            }
          ],
          ... (more channels)
        }
      },
      ... (more steps)
    }
  },
  "message": (required, string) the status of the export, returns 'success' when completed without errors
}
```

{% alert tip %}
Para obter ajuda com exportações de CSV e API, acesse [Resolução de problemas de exportação]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
