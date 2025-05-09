---
nav_title: "OBTER: Exportar eventos personalizados"
article_title: "OBTER: Exportar eventos personalizados"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint da Braze \"Exportar eventos personalizados\"."

---
{% api %}
# Exportar eventos personalizados
{% apimethod get %}
/eventos
{% endapimethod %}

> Use esse endpoint para exportar uma lista de eventos personalizados registrados para o seu aplicativo. Os eventos são retornados em grupos de 50, classificados em ordem alfabética.

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `events.get`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='events' %}

## Parâmetros de consulta

Observe que cada chamada a esse endpoint retornará 50 eventos. Para mais de 50 eventos, use o cabeçalho `Link` para recuperar os dados na próxima página, conforme mostrado no exemplo de resposta a seguir.

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `cursor` | Opcional | String | Determina a paginação dos eventos personalizados. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Exemplos de solicitações

### Sem cursor

```
curl --location --request GET 'https://rest.iad-01.braze.com/events' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### Com cursor

```
curl --location --request GET 'https://rest.iad-03.braze.com/events?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Resposta

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "events" : [
        {
            "name": "The event name", (string) the event name,
            "description": "The event description", (string) the event description,
            "included_in_analytics_report": false, (boolean) the analytics report inclusion,
            "status": "Active", (string) the event status,
            "tag_names": ["Tag One", "Tag Two"] (array) the tag names associated with the event formatted as strings,
        },
        ...
    ]
}
```

### Códigos de resposta a erros fatais {#fatal-export}

Para obter os códigos de status e as mensagens de erro associadas que serão retornadas se sua solicitação encontrar um erro fatal, consulte [Erros fatais]({{site.baseurl}}/api/errors/#fatal-errors).

{% alert tip %}
Para obter ajuda com exportações de CSV e API, acesse [Resolução de problemas de exportação]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
