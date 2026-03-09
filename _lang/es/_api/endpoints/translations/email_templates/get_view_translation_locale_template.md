---
nav_title: "GET: Ver la traducción y la configuración regional específicas para la plantilla de correo electrónico."
article_title: "GET: Ver traducción específica y configuración regional para la plantilla de correo electrónico"
search_tag: Punto de conexión
page_order: 2

layout: api_page
page_type: reference
description: "Este artículo describe los detalles sobre el extremo de plantilla de correo electrónico para ver la traducción y la configuración de localización específicas."
---

{% api %}
# Ver una traducción y configuración regional específicas para el punto final de la plantilla de correo electrónico.
{% apimethod get %}
/plantillas/traducciones/correo electrónico
{% endapimethod %}

> Utiliza este punto final para ver una traducción y una configuración regional específicas para una [plantilla de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates). Consulta [Locales en los mensajes]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/) para obtener más información sobre las características de traducción.

{% multi_lang_include early_access_beta_alert.md feature='This endpoint' %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `templates.translations.get`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parámetros de consulta

| Parámetro     | Obligatoria | Tipo de datos | Descripción                     |
|---------------|----------|-----------|---------------------------------|
| `template_id` | Obligatoria | Cadena    | El ID de tu plantilla de correo electrónico. |
| `locale_id`   | Opcional | Cadena    | El ID (UUID) de la configuración regional.           |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Todos los ID de traducción se consideran identificadores únicos universales (UUID), que se pueden encontrar en la respuesta del punto final GET.
{% endalert %}

## Ejemplo de solicitud

```
curl --location --request GET 'https://rest.iad-03.braze.com/templates/translations/email?locale_id={locale_uuid}&template_id={template_id}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Respuesta

Hay cuatro respuestas de código de estado para este punto final: `200`, `400`, `404` y `429`.

### Ejemplo de respuesta positiva

El código de estado `200` podría devolver la siguiente cabecera y cuerpo de respuesta.

```json
{
    "translations": [
        {
            "locale": {
                "uuid": "c7c12345-te35-1234-5678-abcdefa99r3f",
                "name": "es-MX",
                "country": "MX",
                "language": "es",
                "locale_key": "es-mx"
            },
            "translation_map": {
                "id_0": "¡Hola!",
                "id_1": "Me llamo Jacky",
                "id_2": "¿Dónde está la biblioteca?"
            }
        }
    ]
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
