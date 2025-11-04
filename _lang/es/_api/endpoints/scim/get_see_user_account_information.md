---
nav_title: "GET: Buscar una cuenta de usuario existente en el salpicadero"
article_title: "GET: Buscar una cuenta de usuario existente en el salpicadero"
alias: /get_see_user_account_information/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Braze Buscar un ID de recurso de cuenta de usuario de panel existente."
---

{% api %}
# Buscar una cuenta de usuario existente en el panel por ID de recurso
{% apimethod get %}
/scim/v2/Users/{id}
{% endapimethod %}

> Utiliza este punto final para buscar una cuenta de usuario existente en el panel especificando el recurso `id` devuelto por el método SCIM [`POST`]({{site.baseurl}}/api/endpoints/scim/post_create_user_account/). 

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#3df40764-8f74-4532-aed3-ab8a6cb92122 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás un token SCIM. Utilizarás el origen de tu servicio como cabecera de `X-Request-Origin`. Para más información, consulta [Aprovisionamiento automatizado de usuarios]({{site.baseurl}}/scim/automated_user_provisioning/).

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='look up dashboard user' %}

## Parámetros de la ruta

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `id` | Obligatoria | Cadena | ID del recurso del usuario. Este parámetro lo devuelven los métodos `POST` `/scim/v2/Users/` o `GET`  `/scim/v2/Users?filter=userName eq "user@test.com"`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Cuerpo de la solicitud
```json
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-REST-API-KEY
```

## Ejemplo de solicitud
```json
curl --location --request GET 'https://rest.iad-01.braze.com/scim/v2/Users/dfa245b7-24195aec-887bb3ad-602b3340' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
```

## Respuesta
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
    "createdAt": "Thursday, January 1, 1970 12:00:00 AM",
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "roles": [
            {
                "roleName": "Another Test Role",
                "roleId": "23125dad23dfaae7,
                "appGroup": [
                    {
                        "appGroupId": "241adcd25adfabcded",
                        "appGroupName": "Production Workspace",
                        "appGroupPermissionSets": [
                            {
                                "appGroupPermissionSetName": "A Permission Set",
                                "appGroupPermissionSetId": "dfa385109bc38",
                                "permissions": ["basic_access","publish_cards"]
                            }
                        ]
                    } 
                ]
            }
        ],
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