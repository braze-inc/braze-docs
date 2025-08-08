---
nav_title: "GET: Buscar cuenta de usuario existente en el panel por correo electrónico"
article_title: "GET: Buscar cuenta de usuario existente en el panel por correo electrónico"
alias: /get_search_existing_dashboard_user_email/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Buscar una cuenta de usuario existente en el panel por correo electrónico de Braze."
---

{% api %}
# Buscar cuenta de usuario existente en el salpicadero por correo electrónico
{% apimethod get %}
scim/v2/Users?filter=userName%20eq%20"user%40test.com"
{% endapimethod %}

> Utilice este punto final para buscar una cuenta de usuario del cuadro de mandos existente especificando su correo electrónico en el parámetro de consulta del filtro. 

Tenga en cuenta que cuando el parámetro de consulta está codificado en URL se leerá así:

`/scim/v2/Users?filter=userName%20eq%20%22user@test.com%22`

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5037d810-b822-4c54-bb51-f30470a42a95 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás un token SCIM. Utilizarás el origen de tu servicio como cabecera de `X-Request-Origin`. Para más información, consulta [Aprovisionamiento automatizado de usuarios]({{site.baseurl}}/scim/automated_user_provisioning/).

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='look up dashboard user email' %}

## Parámetros de la ruta

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `userName@example.com` | Obligatoria | Cadena | El correo electrónico del usuario. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Parámetros de la solicitud

```json
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-REST-API-KEY
```

## Ejemplo de solicitud
```json
curl --location --request GET \ 'https://rest.iad-01.braze.com/scim/v2/Users?filter=userName%20eq%20%22user@test.com%22' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
```

## Respuesta
```json
{
    "schemas": ["urn:ietf:params:scim:api:messages:2.0:ListResponse"],
    "totalResults": 1,
    "Resources": [
        {
            "userName": "user@test.com",
            "id": "dfa245b7-24195aec-887bb3ad-602b3340",
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
    ]
}
```

{% endapi %}

