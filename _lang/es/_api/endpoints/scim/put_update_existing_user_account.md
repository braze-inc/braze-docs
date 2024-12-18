---
nav_title: "COLOCAR: Actualizar la cuenta de usuario del panel de control"
article_title: "COLOCAR: Actualizar la cuenta de usuario del panel de control"
alias: /post_update_existing_user_account/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Actualizar una cuenta de usuario existente en el panel de Braze."
---

{% api %}
# Actualizar una cuenta de usuario en el panel
{% apimethod put %}
/scim/v2/Users/{id}
{% endapimethod %}

> Utiliza este punto final para actualizar una cuenta de usuario existente en el panel especificando el recurso `id` devuelto por el método SCIM [`POST`]({{site.baseurl}}/scim/post_create_user_account/).

Permite actualizar los nombres y apellidos, los permisos (para establecer permisos a nivel de empresa, espacio de trabajo y equipo) y el departamento.

Por razones de seguridad, `userName` (dirección de correo electrónico) no se puede actualizar a través de este punto final. Si desea cambiar la `userName` (dirección de correo electrónico) de un usuario, póngase en contacto con [el servicio de asistencia]({{site.baseurl}}/support_contact/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f9a1642-988e-4011-8fb8-db4340ea1ac7 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás un token SCIM. Para más información, consulta [Aprovisionamiento automatizado de usuarios]({{site.baseurl}}/scim/automated_user_provisioning/).

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='update dashboard user' %}

## Parámetros de la ruta

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `id` | Obligatoria | Cadena | ID del recurso del usuario. Este parámetro es devuelto por los métodos `POST` `/scim/v2/Users/` o `GET`  `/scim/v2/Users?filter=userName eq "user@test.com"`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Cuerpo de la solicitud
```
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-REST-API-KEY
```
```json
{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "name": {"name": {
        "givenName": "Test",
        "familyName": "User"
    },
    "department": "finance",
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "appGroup": [
            {
                "appGroupName": "Test Workspace",
                "appGroupPermissions": ["basic_access","send_campaigns_canvases"],
                "team": [
                    {
                         "teamName": "Test Team",
                         "teamPermissions": ["admin"]
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
| `schemas` | Obligatoria | Matriz de cadenas | Nombre de esquema SCIM 2.0 esperado para el objeto de usuario. |
| `name` | Obligatoria | Objeto JSON | Este objeto contiene el nombre y los apellidos del usuario. |
| `department` | Obligatoria | Cadena | Cadena [de]({{site.baseurl}}/scim_api_appendix/#department-strings) departamento válida de la [documentación de cadenas de departamento]({{site.baseurl}}/scim_api_appendix/#department-strings). |
| `permissions` | Obligatoria | Objeto JSON | Objeto [de permisos]({{site.baseurl}}/scim_api_appendix/#permissions-object) tal y como se describe en [la documentación del objeto de permisos]({{site.baseurl}}/scim_api_appendix/#permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


## Ejemplo de solicitud
```json
curl --location --request PUT 'https://rest.iad-01.braze.com/scim/v2/Users/dfa245b7-24195aec-887bb3ad-602b3340' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data raw '{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "name": {
        "givenName": "Test",
        "familyName": "User"
    },
    "department": "finance",
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "appGroup": [
            {
                "appGroupName": "Test Workspace",
                "appGroupPermissions": ["basic_access","send_campaign_canvases"],
                "team": [
                    {
                         "teamName": "Test Team",                  
                         "teamPermissions": ["admin"]
                    }
                ]
            }
        ]
    }
}
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
        "appGroup": [
            {
                "appGroupId": "241adcd25789fabcded",
                "appGroupName": "Test Workspace",
                "appGroupPermissions": ["basic_access","send_campaigns_canvases"],
                "team": [
                    {
                         "teamId": "2519dafcdba238ae7",
                         "teamName": "Test Team",                  
                         "teamPermissions": ["admin"]
                    }
                ]
            }
        ]
    }
}
```

### Estados de error
Si un usuario con este ID no existe en Braze, el punto final responderá con:

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
