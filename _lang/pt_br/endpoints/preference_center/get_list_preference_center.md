---
nav_title: "OBTER: Listar centros de preferência"
article_title: "OBTER: Listar Centros de Preferência"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Listar centrais de preferência\"."

---
{% api %}
# Listar centros de preferência
{% apimethod get %}
/preference_center/v1/list
{% endapimethod %}

> Use este endpoint para listar seus centros de preferência disponíveis.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#dd8f6667-5eba-4e19-a29e-ba74644c0b8e {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `preference_center.list`.

## Limite de taxa

Este endpoint tem um limite de frequência de 1.000 solicitações por minuto, por espaço de trabalho.

## jornada e parâmetros de solicitação

Não há parâmetros de jornada ou solicitação para esse endpoint.

## Exemplo de solicitação

```
curl --location -g --request GET https://rest.iad-01.braze.com/preference_center/v1/list \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Resposta

```json
{
  "preference_centers": [
    {
      "name": "My Preference Center 1",
      "preference_center_api_id": "preference_center_api_id",
      "created_at": "2022-08-17T15:46:10Z",
      "updated_at": "2022-08-17T15:46:10Z"
    },
    {
      "name": "My Preference Center 2",
      "preference_center_api_id": "preference_center_api_id",
      "created_at": "2022-08-19T11:13:06Z",
      "updated_at": "2022-08-19T11:13:06Z"
    },
    {
      "name": "My Preference Center 3",
      "preference_center_api_id": "preference_center_api_id",
      "created_at": "2022-08-19T11:30:50Z",
      "updated_at": "2022-08-19T11:30:50Z"
    },
    {
      "name": "My Preference Center 4",
      "preference_center_api_id": "preference_center_api_id",
      "created_at": "2022-09-13T20:41:34Z",
      "updated_at": "2022-09-13T20:41:34Z"
    }
  ]
}
```

{% endapi %}
