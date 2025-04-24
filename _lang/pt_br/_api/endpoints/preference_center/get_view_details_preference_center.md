---
nav_title: "OBTER: Exibir detalhes da Central de Preferências"
article_title: "OBTER: Exibir detalhes da Central de Preferências"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint \"Exibir detalhes da Central de Preferências\" da Braze."

---
{% api %}
# Exibir detalhes da Central de Preferências
{% apimethod get %}
/preference_center/v1/{preferenceCenterExternalID}
{% endapimethod %}

> Use esse endpoint para visualizar os detalhes de suas Centrais de Preferências, inclusive quando foram criadas e atualizadas.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6a47fd7c-2997-4832-aedb-d101a2dd03a5 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `preference_center.get`.

## Limite de taxa

Esse endpoint tem um limite de frequência de 1.000 solicitações por minuto, por espaço de trabalho.

## Parâmetros da jornada

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
|`preferenceCenterExternalID`| Obrigatória | String | A ID de sua central de preferências. |
{: role="presentation" }

## Parâmetros de solicitação

Não há parâmetros de solicitação para esse endpoint.

## Exemplo de solicitação

```
curl --location -g --request GET https://rest.iad-01.braze.com/preference_center/v1/preference_center_external_id \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Resposta
```json
{
  "name": "My Preference Center",
  "preference_center_api_id": "preference_center_api_id",
  "created_at": "example_time_created",
  "updated_at": "example_time_updated",
  "preference_center_title": "Example preference center title",
  "preference_center_page_html": "HTML for preference center here",
  "confirmation_page_html": "HTML for confirmation page here",
  "redirect_page_html": null,
  "preference_center_options": {
    "meta-viewport-content": "width=device-width, initial-scale=2"
  },
  "state": "active"
}
```

{% endapi %}
