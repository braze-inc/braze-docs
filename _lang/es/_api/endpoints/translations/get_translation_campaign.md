---
nav_title: "GET: Ver la traducción de una campaña"
article_title: "GET: Ver la traducción de una campaña"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Ver la traducción de una campaña."
---

{% api %}
# Ver la traducción de una campaña
{% apimethod get %}
/campaign/translations/?locale_id={locale_id}
{% endapimethod %}

> Utilice este punto final para visualizar un mensaje de campaña traducido y ver qué aspecto tiene este mensaje para un usuario.

{% alert important %}
La opción de ver un mensaje de campaña traducido a través de la API se encuentra actualmente en acceso anticipado. Póngase en contacto con su gestor de cuenta Braze si está interesado en participar en el acceso anticipado.
{% endalert %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `campaigns.translations.get`.

## Límite de velocidad

Este punto final tiene un límite de velocidad de 250 000 solicitudes por hora.

## Parámetros de la ruta

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
|`campaign_id`| Obligatoria | Cadena | El ID de su campaña. |
|`message_variation_id`| Obligatoria | Cadena | El ID de su variación de mensaje. |
|`locale_id`| Obligatoria | Cadena | El ID de la configuración regional. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Ten en cuenta que todos los ID de traducción se consideran identificadores únicos universales (UUID), que se pueden encontrar en la configuración **del soporte multilingüe** o en la respuesta a la solicitud.

## Ejemplo de solicitud

```
curl --location --request GET 'https://rest.iad-03.braze.com/campaign/translations/?locale_id={locale_id}' \
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
 				"name": "es-MX",
 				"country": "Mexico",
 				"language": "Spanish",
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

### Ejemplo de respuesta de error

El código de estado `400` podría devolver el siguiente cuerpo de respuesta. Consulte la sección [Solución de problemas](#troubleshooting) para obtener más información sobre los errores que puede encontrar.

```json
{
	"errors": [
		{
			"message": "Invalid locale ID"
		}
	]
}
```

## Solución de problemas

La siguiente tabla enumera los posibles errores devueltos y los pasos asociados para solucionarlos.

| Mensaje de error                           | Solución de problemas                                                                    |
|-----------------------------------------|------------------------------------------------------------------------------------|
| `INVALID_CAMPAIGN_ID`                   | Confirma que el ID de la campaña coincide con la campaña que estás traduciendo.                   |
| `INVALID_LOCALE_ID`                     | Confirma que tu ID de configuración regional existe en la traducción de tu mensaje.                         |
| `INVALID_MESSAGE_VARIATION_ID`          | Confirma que el ID de tu mensaje es correcto.                                                |
| `MESSAGE_NOT_FOUND`                     | Comprueba el mensaje para traducir.                                           |
| `LOCALE_NOT_FOUND`                      | Confirma que la configuración regional existe en tu configuración multilingüe.                         |
| `MULTI_LANGUAGE_NOT_ENABLED`            | La configuración multilingüe no está activada para tu espacio de trabajo.                       |
| `MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE` | Solo se pueden traducir las campañas de correo electrónico o los mensajes de Canvas con correos electrónicos.             |
| `UNSUPPORTED_CHANNEL`                   | Solo se pueden traducir los mensajes de las campañas de correo electrónico o los mensajes de Canvas con correos electrónicos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
