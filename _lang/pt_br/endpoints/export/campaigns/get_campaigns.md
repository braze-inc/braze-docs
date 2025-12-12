---
nav_title: "OBTER: Exportar lista de campanhas"
article_title: "OBTER: Exportar lista de campanhas"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Exportar lista de campanhas\"."

---
{% api %}
# Exportar lista de campanhas
{% apimethod get %}
/campaigns/list
{% endapimethod %}

> Use esse ponto de extremidade para exportar uma lista de campanhas, cada uma das quais incluirá seu nome, o identificador da API da campanha, se é uma campanha da API e as tags associadas à campanha.

As campanhas são retornadas em grupos de 100, classificadas por hora de criação (da mais antiga para a mais recente, por padrão).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f3b0b3ef-04fb-4a31-8570-e6ad88dacb18 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `campaigns.list`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | -------- | --------- | ----------- |
| `page` | Opcional | Inteiro | A página de campanhas a ser retornada; o padrão é 0 (retorna o primeiro conjunto de até 100). |
| `include_archived` | Opcional | Booleano | Se deve ou não incluir campanhas arquivadas; o padrão é false. |
| `sort_direction` | Opcional | String | \- Classifique o tempo de criação do mais novo para o mais antigo: passe o valor `desc`.<br> \- Classifique o tempo de criação do mais antigo para o mais recente: passe o valor `asc`. <br><br>Se `sort_direction` não estiver incluído, a ordem padrão será da mais antiga para a mais recente. |
| `last_edit.time[gt]` | Opcional | Horário | Filtra os resultados e retorna apenas as campanhas que foram editadas mais do que o tempo fornecido até o momento. O formato é `yyyy-MM-DDTHH:mm:ss`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação

```
curl --location -g --request GET 'https://rest.iad-01.braze.com/campaigns/list?page=0&include_archived=false&sort_direction=desc&last_edit.time[gt]=2020-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Resposta

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "campaigns" : [
        {
            "id" : (string) the Campaign API identifier,
            "last_edited": (ISO 8601 string) the last edited time for the message
            "name" : (string) the campaign name,
            "is_api_campaign" : (boolean) whether the campaign is an API campaign,
            "tags" : (array) the tag names associated with the campaign formatted as strings
        },
        ...
    ]
}
```

{% alert tip %}
Para obter ajuda com exportações de CSV e API, acesse [Resolução de problemas de exportação]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
