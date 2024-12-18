---
nav_title: "OBTER: Procurar uma Conta de Usuário de Dashboard Existente"
article_title: "OBTER: Procurar uma Conta de Usuário de Dashboard Existente"
alias: /get_see_user_account_information/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Procurar uma conta de usuário no dashboard\"."
---

{% api %}
# Procure uma conta de usuário de dashboard existente
{% apimethod get %}
/scim/v2/Users/{id}
{% endapimethod %}

> Use este endpoint para procurar uma conta de usuário do dashboard existente especificando o recurso `id` retornado pelo método SCIM [`POST`]({{site.baseurl}}/scim/post_create_user_account/). 

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#3df40764-8f74-4532-aed3-ab8a6cb92122 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de um token SCIM. Para saber mais, consulte [Provisionamento automatizado de usuários]({{site.baseurl}}/scim/automated_user_provisioning/).

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='look up dashboard user' %}

## Parâmetros da jornada

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `id` | Obrigatória | String | O ID do recurso do usuário. Este parâmetro é retornado pelos métodos `POST` `/scim/v2/Users/` ou `GET` `/scim/v2/Users?filter=userName eq "user@test.com"`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Corpo da solicitação
```json
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-REST-API-KEY
```

## Exemplo de solicitação
```json
curl --location --request GET 'https://rest.iad-01.braze.com/scim/v2/Users/dfa245b7-24195aec-887bb3ad-602b3340' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
```

## Resposta
```json
{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "id": "dfa245b7-24195aec-887bb3ad-602b3340",
    "userName": "user@test.com",
    "name": {
        "givenName": "Test",
        "familyName": "User"
    },
    "department": "finance",
    "lastSignInAt": "Thursday, January 1, 1970 12:00:00 AM",
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "appGroup": [
            {
                "appGroupId": "241adcd25789fabcded",
                "appGroupName": "Test Workspace",
                "appGroupPermissions": ["basic_access","send_campaigns_canvases"],
                "team": [
                    {
                         "teamId": "241adcd25789fabcded",
                         "teamName": "Test Team",                  
                         "teamPermissions": ["admin"]
                    }
                ]
            } 
        ]
    }
}
```

{% endapi %}