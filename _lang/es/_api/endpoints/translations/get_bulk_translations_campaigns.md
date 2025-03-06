---
nav_title: "GET: Ver las traducciones de una campaña"
article_title: "GET: Ver las traducciones de una campaña"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Ver las traducciones de una campaña."
---

{% api %}
# Ver las traducciones de una campaña
{% apimethod get %}
/campaigns/translations
{% endapimethod %}

> Utiliza este punto final para ver todas las traducciones de cada variante de mensaje de una campaña.

{% alert important %}
La visualización de las traducciones de los mensajes de campaña a través de la API se encuentra actualmente en acceso temprano. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en el acceso anticipado.
{% endalert %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `campaigns.translations.get`.

## Límite de velocidad

Este punto final tiene un límite de velocidad de 250 000 solicitudes por hora.

## Parámetros de la ruta

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
|`campaign_id`| Necesario para traducir una campaña | Cadena | El ID de su campaña. |
| `message_variation_id` | Obligatoria | Cadena | El ID de tu mensaje. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Ten en cuenta que todos los ID de traducción se consideran identificadores únicos universales (UUID), que se pueden encontrar en la configuración **del soporte multilingüe** o en la respuesta a la solicitud.

## Ejemplo de solicitud

```
curl --location --request GET 'https://rest.iad-03.braze.com/campaign/translations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Respuesta

Hay cuatro respuestas de código de estado para este punto final: `200`, `400`, `404` y `429`.

## Ejemplo de respuesta positiva

El código de estado `200` podría devolver la siguiente cabecera y cuerpo de respuesta.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
	"translations": [
		{
			"locale": {
 				"name": "zh-HK",
 				"country": "Hong Kong",
 				"language": "Chinese (Traditional)",
			},
			"translation_map": {
				"id_0": "Hello",
				"id_1": "My name is Jacky",
				"id_2": "Where is the library?"
			}
		}
	]
}
```

## Ejemplo de respuesta de error

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
| `MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE` | Solo se pueden traducir las campañas de correo electrónico o los mensajes de Canvas con correos electrónicos.             |
| `UNSUPPORTED_CHANNEL`                   | Solo se pueden traducir los mensajes de las campañas de correo electrónico o los mensajes de Canvas con correos electrónicos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
