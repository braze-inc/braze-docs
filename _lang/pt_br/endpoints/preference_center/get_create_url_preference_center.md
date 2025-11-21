---
nav_title: "OBTER: Gerar URL da Central de Preferências"
article_title: "OBTER: Gerar URL da Central de Preferências"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint \"Gerar URL da Central de Preferências\"."

---
{% api %}
# Gerar URL da Central de Preferências
{% apimethod get %}
/preference_center/v1/{preferenceCenterExternalID}/url/{userID}
{% endapimethod %}

> Use esse endpoint para gerar um URL para uma Central de Preferências.

Cada URL da Central de Preferências é exclusivo para cada usuário.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0bc750ff-068e-4391-897e-6eddca2561cd {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `preference_center.user.get`.

## Limite de taxa

Esse endpoint tem um limite de frequência de 1.000 solicitações por minuto, por espaço de trabalho.

## Parâmetros da jornada

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
|`preferenceCenterExternalID`| Obrigatória | String | A ID de sua central de preferências. |
|`userID`| Obrigatória | String | A ID do usuário. |
{:  role="presentation" }

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
|`preference_center_api_id`| Obrigatória | String | A ID de sua central de preferências. |
|`external_id`| Obrigatória | String | A ID externa de um usuário. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação

```
curl --location --request GET 'https://rest.iad-01.braze.com/preference_center/v1/$preference_center_external_id/url/$user_external_id' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Resposta

```json
{
  "preference_center_url": "https://www.example.com/preferences"
}
```

{% endapi %}

{% alert note %}
Este endpoint gera apenas URLs para o novo Central de Preferências (como Central de Preferências criadas usando nossa API ou o editor de arrastar e soltar).
{% endalert %}
