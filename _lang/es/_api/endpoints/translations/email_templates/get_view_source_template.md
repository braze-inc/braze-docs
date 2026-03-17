---
nav_title: "GET: Ver traducciones originales para la plantilla de correo electrónico"
article_title: "GET: Ver traducciones de la fuente para la plantilla de correo electrónico"
search_tag: Punto de conexión
page_order: 1

layout: api_page
page_type: reference
description: "Este artículo describe los detalles sobre el extremo Ver traducciones de origen para una plantilla de correo electrónico."
---

{% api %}
# Ver las traducciones originales de una plantilla de correo electrónico
{% apimethod get %}
/plantillas/correo electrónico/traducciones/fuente
{% endapimethod %}

> Utiliza este punto final para ver las traducciones originales de una [plantilla de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates). Consulta [Locales en los mensajes]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/) para obtener más información sobre las características de traducción.

{% multi_lang_include early_access_beta_alert.md feature='This endpoint' %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `templates.email.info`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parámetros de consulta

| Parámetro     | Obligatoria | Tipo de datos | Descripción                     |
|---------------|----------|-----------|---------------------------------|
| `template_id` | Obligatoria | Cadena    | El ID de tu plantilla de correo electrónico. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud

```
curl --location --request GET 'https://rest.iad-03.braze.com/templates/email/translations/source?template_id={template_id}'
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
--Request Body
---template_id: "6ad1507f-ca10-44c4-95bf-aj39fm10fm1ps"
```

## Respuesta

Hay cuatro respuestas de código de estado para este punto final: `200`, `400`, `404` y `429`.

### Ejemplo de respuesta positiva

El código de estado `200` podría devolver la siguiente cabecera y cuerpo de respuesta.

```json
{
    "translations": {
        "translation_map": {
            "id_0": "Here's a limited time offer for your membership tier!",
            "id_1": "Welcome to a new fashion-forward season!"
        }
    },
    "message": "success"
}
```

### Ejemplo de respuesta de error

El código de estado `400` podría devolver el siguiente cuerpo de respuesta. Consulte la sección [Solución de problemas](#troubleshooting) para obtener más información sobre los errores que puede encontrar.

```json
{
    "errors": [
        {
            "message": "The provided locale code does not exist."
        }
    ]
}
```

{% endapi %}
