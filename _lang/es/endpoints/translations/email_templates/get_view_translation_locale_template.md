---
nav_title: "GET: Ver traducción y localización específicas para plantilla de correo electrónico"
article_title: "GET: Ver traducción específica y localización para plantilla de correo electrónico"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "En este artículo se describen los detalles sobre la traducción específica de la Vista y la configuración regional para el punto final de la plantilla de correo electrónico."
---

{% api %}
# Ver una traducción y localización específicas para el punto final de la plantilla de correo electrónico
{% apimethod get %}
/templates/translations/email?locale_id={locale_uuid}&template_id={template_id}
{% endapimethod %}

> Utiliza este punto final para ver una traducción y localización específicas de una [plantilla de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates).

{% alert important %}
Este punto final se encuentra actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en el acceso anticipado.
{% endalert %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `templates.translations.get`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parámetros de consulta

| Parámetro     | Obligatoria | Tipo de datos | Descripción                     |
|---------------|----------|-----------|---------------------------------|
| `template_id` | Obligatoria | Cadena    | El ID de tu plantilla de correo electrónico. |
| `locale_id`   | Obligatoria | Cadena    | El ID de la configuración regional.           |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Ten en cuenta que todos los ID de traducción se consideran identificadores únicos universales (UUID), que se pueden encontrar en la configuración **del soporte multilingüe** o en la respuesta a la solicitud.

## Ejemplo de solicitud

```
curl --location --request GET 'https://rest.iad-03.braze.com/templates/translations/email?locale_id={locale_uuid}&template_id={template_id}/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Respuesta

Hay cuatro respuestas de código de estado para este punto final: `200`, `400`, `404` y `429`.

### Ejemplo de respuesta positiva

El código de estado `200` podría devolver la siguiente cabecera y cuerpo de respuesta.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
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

## Solución de problemas

La siguiente tabla enumera los posibles errores devueltos y los pasos asociados para solucionarlos.

| Mensaje de error                           | Solución de problemas                                                                    |
|-----------------------------------------|------------------------------------------------------------------------------------|
| `INVALID_LOCALE_ID`                     | Confirma que tu ID de configuración regional existe en la traducción de tu mensaje.                         |
| `LOCALE_NOT_FOUND`                      | Confirma que la configuración regional existe en tu configuración multilingüe.                         |
| `MULTI_LANGUAGE_NOT_ENABLED`            | La configuración multilingüe no está activada para tu espacio de trabajo.                       |
| `MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE` | Sólo se pueden traducir las plantillas de correo electrónico y las campañas de mensajería por correo electrónico, push y dentro de la aplicación, o los mensajes de Canvas con correos electrónicos.             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
