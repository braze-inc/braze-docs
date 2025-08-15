---
nav_title: "POST: Crear una nueva cuenta de usuario en el panel"
article_title: "POST: Crear una nueva cuenta de usuario en el panel"
alias: /post_create_user_account/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles sobre el punto final Crear nueva cuenta de usuario del panel de Braze."

---

{% api %}
# Crear una nueva cuenta de usuario en el panel
{% apimethod post %}
/scim/v2/Users
{% endapimethod %}

> Utiliza este punto final para crear una nueva cuenta de usuario del panel especificando correo electrónico, nombres y apellidos, permisos (para establecer permisos a nivel de empresa, espacio de trabajo y equipo).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#768a3c9d-ce1d-44fc-a0e4-d556b09f7aa3 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás un token SCIM. Utilizarás el origen de tu servicio como cabecera de `X-Request-Origin`. Para más información, consulta [Aprovisionamiento automatizado de usuarios]({{site.baseurl}}/scim/automated_user_provisioning/).

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='create dashboard user' %}

## Cuerpo de la solicitud
```
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-SCIM-TOKEN-KEY
```
```
{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "userName": "user@test.com",
    "name": {
        "givenName": "Test",
        "familyName": "User"
    },
    "department": "finance",
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "roles": [
            {
                "roleName": "Test Role"
            },
            {
                "roleId": "2519dafcdba238ae7"
            }
        ],
        "appGroup": [
            {
                "appGroupName": "Test Workspace",
                "appGroupPermissions": ["basic_access","send_campaigns_canvases"],
                "team": [
                    {
                         "teamName": "Test Team",                  
                         "teamPermissions": ["basic_access","export_user_data"]
                    }
                ]
            },
            {
                "appGroupName": "Other Test Workspace",
                "appGroupPermissionSets": [
                    {
                        "appGroupPermissionSetName":  "Test Permission Set"
                    }
                ]
            }
        ]
    }
}
```

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | -------- | --------- | ----------- |
| `schemas` | Obligatoria | Matriz de cadenas | Nombre del esquema SCIM 2.0 esperado para el objeto usuario. |
| `userName` | Obligatoria | Cadena | La dirección de correo electrónico del usuario. |
| `name` | Obligatoria | Objeto JSON | Este objeto contiene el nombre y los apellidos del usuario. |
| `department` | Obligatoria | Cadena | Cadena [de]({{site.baseurl}}/scim_api_appendix/#department-strings) departamento válida de la [documentación de cadenas de departamento]({{site.baseurl}}/scim_api_appendix/#department-strings). |
| `permissions` | Opcional | Objeto JSON | Objeto [de permisos]({{site.baseurl}}/scim_api_appendix/#permissions-object) tal y como se describe en [la documentación del objeto de permisos]({{site.baseurl}}/scim_api_appendix/#permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud
```json
curl --location --request POST 'https://rest.iad-01.braze.com/scim/v2/Users' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM–TOKEN-HERE' \
--data raw '{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "userName": "user@test.com",
    "name": {
        "givenName": "Test",
        "familyName": "User"
    },
    "department": "finance",
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "roles": [
            {
                "roleName": "Test Role"
            },
            {
                "roleId": "2519dafcdba238ae7"
            }
        ],
        "appGroup": [
            {
                "appGroupName": "Test Workspace",
                "appGroupPermissions": ["basic_access","send_campaigns_canvases"],
                "team": [
                    {
                         "teamName": "Test Team",                  
                         "teamPermissions": ["basic_access","export_user_data"]
                    }
                ]
            } 
        ]
    }
}'
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
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "roles": [
            {
                "roleName": "Test Role",
                "roleId": "519dafcdba23dfaae7,
                "appGroup": [
                    {
                        "appGroupId": "241adcd25789fabcded",
                        "appGroupName": "Some Workspace",
                        "appGroupPermissions": ["basic_access", "publish_cards"],
                        "team": [
                            {
                                "teamId": "2519dafcdba238ae7",
                                "teamName": "Some Team",                  
                                "teamPermissions": ["export_user_data"]
                            }
                        ]
                    } 
                ]
            },
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
                         "teamId": "2519dafcdba238ae7",
                         "teamName": "Test Team",                  
                         "teamPermissions": ["basic_access","export_user_data"]
                    }
                ]
            },
            {
                "appGroupName": "Other Test Workspace",
                "appGroupPermissionSets": [
                    {
                        "appGroupPermissionSetName":  "Test Permission Set"
                    }
                ]
            } 
        ]
    }
}
```

## Parámetros de respuesta

| Parámetro | Tipo de datos | Descripción |
| --------- | --------- | ----------- |
| `schemas` | Matriz de cadenas | Nombre del esquema SCIM 2.0 esperado para el objeto usuario. |
| `userName` | Cadena | La dirección de correo electrónico del usuario. |
| `name` | Objeto JSON | Este objeto contiene el nombre y apellidos del usuario. |
| `department` | Cadena | Cadena [de]({{site.baseurl}}/scim_api_appendix/#department-strings) departamento válida de la [documentación de cadenas de departamento]({{site.baseurl}}/scim_api_appendix/#department-strings). |
| `permissions` | Objeto JSON | Objeto [de permisos]({{site.baseurl}}/scim_api_appendix/#permissions-object) tal y como se describe en [la documentación del objeto de permisos]({{site.baseurl}}/scim_api_appendix/#permissions-object). |
| `id` | Cadena | ID generado por Braze que se utiliza para buscar y administrar cuentas de usuario. |
| `lastSignInAt` | Cadena | Fecha del último inicio de sesión con éxito en hora UTC. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Estados de error

Si ya existe en Braze un usuario con este `userName` o dirección de correo electrónico, el punto final responderá con:

```json
HTTP/1.1 409 Conflict
Date: Tue, 10 Sep 2019 02:22:30 GMT
Content-Type: text/json;charset=UTF-8

{
  "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
  "detail": "User already exists in the database.",
  "status": 409
}
```

{% endapi %}
