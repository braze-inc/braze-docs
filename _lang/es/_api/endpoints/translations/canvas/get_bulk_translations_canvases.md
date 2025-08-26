---
nav_title: "GET: Ver todas las traducciones de un Canvas"
article_title: "GET: Ver todas las traducciones de un Canvas"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "En este artículo se describen los detalles de la función Ver todas las traducciones de un punto final de Canvas."
---

{% api %}
# Ver todas las traducciones de un Canvas
{% apimethod get %}
/canvas/translations
{% endapimethod %}

> Utiliza este punto final para ver todas las traducciones de un Canvas.

{% alert important %}
Este punto final se encuentra actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en el acceso anticipado.
{% endalert %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `canvas.translations.get`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parámetros de consulta

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
|`workflow_id` | Obligatoria | Cadena | ID del Canvas. |
|`step_id`| Obligatoria | Cadena | El ID de tu paso en Canvas. |
|`message_variation_id`| Obligatoria | Cadena | El ID de la variación de tu mensaje. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Ten en cuenta que todos los ID de traducción se consideran identificadores únicos universales (UUID), que se pueden encontrar en la configuración **del soporte multilingüe** o en la respuesta a la solicitud.

## Ejemplo de solicitud

```
curl --location --request GET 'https://rest.iad-03.braze.com/canvas/translations' \
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
            "translation_map": {
                "id_0": "¡Hola!",
                "id_1": "Me llamo Jacky",
                "id_2": "¿Dónde está la biblioteca?"
            },
            "locale": {
                "uuid": "c7c12345-te35-1234-5678-abcdefa99r3f",
                "name": "es-MX",
                "country": "MX",
                "language": "es",
                "locale_key": "es-mx"
            }
        },
        {
            "translation_map": {
                "id_0": "你好",
                "id_1": "我的名字是 Jacky",
                "id_2": "圖書館在哪裡?"
            },
            "locale": {
                "uuid": "a1b12345-cd35-1234-5678-abcdefa99r3f",
                "name": "zh-HK",
                "country": "HK",
                "language": "zh",
                "locale_key": "zh-hk"
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
			"message": "This message does not support multi-language."
		}
	]
}
```

## Solución de problemas

La siguiente tabla enumera los posibles errores devueltos y los pasos asociados para solucionarlos.

| Mensaje de error                           | Solución de problemas                                                                    |
|-----------------------------------------|------------------------------------------------------------------------------------|
| `INVALID_CAMPAIGN_ID`                   | Confirma que el ID de la campaña coincide con la campaña que estás traduciendo.                   |
| `INVALID_MESSAGE_VARIATION_ID`          | Confirma que el ID de tu mensaje es correcto.                                                |
| `MESSAGE_NOT_FOUND`                     | Comprueba el mensaje para traducir.                                           |
| `MULTI_LANGUAGE_NOT_ENABLED`            | La configuración multilingüe no está activada para tu espacio de trabajo.                       |
| `MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE` | Sólo se pueden traducir las campañas de correo electrónico, push y mensajes dentro de la aplicación o los mensajes de Canvas con correos electrónicos.             |
| `UNSUPPORTED_CHANNEL`                   | Sólo se pueden traducir las campañas por correo electrónico, push o mensajes dentro de la aplicación, o los mensajes de Canvas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
