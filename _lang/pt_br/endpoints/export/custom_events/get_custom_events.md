---
nav_title: "OBTER: Exportar lista de eventos personalizados"
article_title: "OBTER: Exportar lista de eventos personalizados"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Exportar lista de eventos personalizados\"."

---
{% api %}
# Exportar lista de eventos personalizados
{% apimethod get %}
/events/list
{% endapimethod %}

> Use esse endpoint para exportar uma lista de eventos personalizados que foram registrados para o seu app. Os nomes dos eventos são retornados em grupos de 250, classificados em ordem alfabética.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#93ecd8a5-305d-4b72-ae33-2d74983255c1 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `events.list`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='events list' %}

## Parâmetros de solicitação

| Parâmetro| Obrigatória | Tipo de dados | Descrição |
| -------- | -------- | --------- | ----------- |
| `page` | Opcional | Inteiro | A página de nomes de eventos a ser retornada; o padrão é 0 (retorna o primeiro conjunto de até 250). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação
```
curl --location --request GET 'https://rest.iad-01.braze.com/events/list?page=3' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Resposta

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "events" : [
        "Event A", (string) the event name,
        "Event B", (string) the event name,
        "Event C", (string) the event name,
        ...
    ]
}
```

### Códigos de resposta a erros fatais {#fatal-export}

Para obter os códigos de status e as mensagens de erro associadas que serão retornadas se sua solicitação encontrar um erro fatal, consulte [Erros fatais & respostas]({{site.baseurl}}/api/errors/#fatal-errors).

{% alert tip %}
Para obter ajuda com exportações de CSV e API, acesse [Resolução de problemas de exportação]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
