---
nav_title: "OBTER: Exportar lista de canva"
article_title: "OBTER: Exportar Lista de Canva"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint da Braze \"Exportar lista do canva\""

---
{% api %}
# Exportar lista de canva
{% apimethod get %}
/canvas/list
{% endapimethod %}

> Use este endpoint para exportar uma lista de canvas, incluindo o nome, identificador da API de canva e tags associadas.

Canvas são retornados em grupos de 100 classificados por data de criação (do mais antigo ao mais recente por padrão).

Canvas arquivados não serão incluídos na resposta da API, a menos que o campo `include_archived` seja especificado. Canvas que estão parados, mas não arquivados, no entanto, serão retornados por padrão.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e6c150d7-fceb-4b10-91e2-a9ca4d5806d1 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `canvas.list`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | -------- | --------- | ----------- |
| `page` | Opcional | Número inteiro | A página dos canvas a ser retornada, retornará ao padrão `0` (retorna o primeiro conjunto de até 100) |
| `include_archived` | Opcional | Booleano | Se deve ou não incluir canvas arquivados, o padrão é `false`. |
| `sort_direction` | Opcional | String | \- Classifique o tempo de criação do mais novo para o mais antigo: passe o valor `desc`.<br> \- Classifique o tempo de criação do mais antigo para o mais recente: passe o valor `asc`. <br><br>Se `sort_direction` não estiver incluído, a ordem padrão será da mais antiga para a mais recente. |
| `last_edit.time[gt]` | Opcional | Horário | Filtra os resultados e retorna apenas canvas que foram editados depois do tempo fornecido até agora. O formato é `yyyy-MM-DDTHH:mm:ss`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação

```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/list?page=1&include_archived=false&sort_direction=desc&last_edit.time[gt]=2020-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Resposta

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "canvases" : [
  	{
  		"id" : (string) the Canvas API identifier,
  		"last_edited": (ISO 8601 string) the last edited time for the message,
  		"name" : (string) the Canvas name,
  		"tags" : (array) the tag names associated with the Canvas formatted as strings,
  	},
    ... (more Canvases)
  ],
  "message": (required, string) the status of the export, returns 'success' when completed without errors
}
```

{% alert tip %}
Para obter ajuda com exportações de CSV e API, acesse [Resolução de problemas de exportação]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
