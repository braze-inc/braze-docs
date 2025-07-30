---
nav_title: "DELETE: Remover conta de usuário do dashboard"
article_title: "DELETE: Remover conta de usuário do dashboard"
alias: /delete_existing_dashboard_user/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Remover conta de usuário do dashboard\"."
---

{% api %}
# Remova a conta de usuário do dashboard
{% apimethod delete %}
/scim/v2/Users/{id}
{% endapimethod %}

> Use esse endpoint para excluir permanentemente um usuário do dashboard existente, especificando o recurso `id` retornado pelo método SCIM [`POST`]({{site.baseurl}}/api/endpoints/scim/post_create_user_account/). 

Isso é semelhante à exclusão de um usuário na seção **Company Users (Usuários da empresa** ) do dashboard do Braze.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9c7c71ea-afd6-414a-99d1-4eb1fe274f16 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de um token SCIM. Você usará a origem de seu serviço como o cabeçalho `X-Request-Origin`. Para saber mais, consulte [Provisionamento automatizado de usuários]({{site.baseurl}}/scim/automated_user_provisioning/).

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='delete dashboard user' %}

## Parâmetros da jornada

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `id` | Obrigatória | String | A ID do recurso do usuário. Este parâmetro é retornado pelos métodos `POST` `/scim/v2/Users/` ou `GET` `/scim/v2/Users?filter=userName eq "user@test.com"`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Corpo da solicitação

```json
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-REST-API-KEY
```

## Exemplo de solicitação
```json
curl --location --request DELETE 'https://rest.iad-01.braze.com/scim/v2/Users/dfa245b7-24195aec-887bb3ad-602b3340' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \
```

## Resposta

### Exemplo de resposta de erro

```json
HTTP/1.1 204 Not Found
Content-Type: text/html; charset=UTF-8
```

Se um desenvolvedor com essa ID não existir na Braze, o endpoint responderá com:
```json
HTTP/1.1 404 Not Found
Content-Type: text/html; charset=UTF-8

{
    "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
    "detail": "User not found",
    "status": 404
}
```
{% endapi %}
