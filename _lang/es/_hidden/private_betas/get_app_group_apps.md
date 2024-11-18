---
nav_title: "GET: Listar aplicaciones del espacio de trabajo"
layout: api_page
page_type: reference
hidden: true
permalink: /get_app_group_apps/

platform: API
description: "En este artículo se describen los detalles del punto final Listar aplicaciones del espacio de trabajo de Braze."
---
{% api %}
# Lista de aplicaciones del espacio de trabajo
{% apimethod get %}
/app_group/apps
{% endapimethod %}

> Utiliza este punto final para listar el nombre y el identificador único (`api_key`) de las aplicaciones de un espacio de trabajo. 

Al pulsar este punto final se obtiene una matriz de objetos llamada `apps`. Cada objeto de `apps` contiene el nombre y el identificador único de la aplicación. 

{% apiref postman %}  {% endapiref %}

## Límite de velocidad

Este punto final tiene un límite de velocidad de 100 solicitudes al día (24 horas).

## Parámetros de la solicitud

Esta petición no acepta parámetros.

## Ejemplo de solicitud

```
curl --location --request GET 'https://rest.iad-01.braze.com/app_group/apps' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Respuesta

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "apps": [
        {
          "name": "App Name",
          "api_key": 00000000-0000-0000-0000-000000000000
        }
    ],
    "message": "success"
}
```

### Solución de problemas

La siguiente tabla enumera los posibles errores devueltos y sus pasos asociados para la solución de problemas.

| Error | Solución de problemas |
| --- | --- |
| `401: Unauthorized` | La clave de API no tiene los permisos necesarios. Asegúrate de que tu clave de API tiene permisos `apps.get`. |
| `403: Forbidden` | La aleta de características no está activada para esta empresa. Ponte en contacto con tu administrador del éxito del cliente para obtener ayuda. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
