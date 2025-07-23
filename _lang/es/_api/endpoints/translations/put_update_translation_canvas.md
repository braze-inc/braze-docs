---
nav_title: "COLOCAR: Actualizar la traducción en un lienzo"
article_title: "COLOCAR: Actualizar la traducción en un lienzo"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Actualizar la traducción de un Canvas."
---

{% api %}
# Actualizar la traducción en un lienzo
{% apimethod put %}
/canvas/translations
{% endapimethod %}

> Utilice este punto final para actualizar varias traducciones de un lienzo.

{% alert important %}
La opción de actualizar la traducción para los mensajes de Canvas a través de la API se encuentra actualmente en acceso anticipado. Póngase en contacto con su gestor de cuenta Braze si está interesado en participar en el acceso anticipado.
{% endalert %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `canvas.translations.update`.

## Límite de velocidad

Este punto final tiene un límite de velocidad de 250 000 solicitudes por hora.

## Parámetros de la ruta

No hay parámetros de ruta para este punto final.

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
|`step_id`| Obligatoria | Cadena | El ID de tu paso en Canvas. |
|`message_variation_id`| Obligatoria | Cadena | El ID de tu mensaje. |
|`locale_id`| Obligatoria | Cadena | El ID de la configuración regional. |
|`workflow_id` | Obligatoria | Cadena | ID del Canvas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Ten en cuenta que todos los ID de traducción se consideran identificadores únicos universales (UUID), que puedes encontrar en la configuración **de Soporte multilingüe** o en la respuesta de la solicitud GET.

## Ejemplo de solicitud

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "canvas_id": "9a0ba932-11c0-4c33-b529-e79aafc12409",
    "message_variation_id": "f5896eec-847d-4c0d-a4b6-7695e67520d7",
    "locale_id": "3fa10d31-83ae-4ff4-9631-f52cea9ec8fa",
    "translation_map": {
        "id_4": "¿Dónde está la biblioteca? Me llamo T-Bone, La araña discoteca.",
        "subject_1": "¿Dónde está la biblioteca? Me llamo T-Bone, La araña discoteca.",
        "id_1": "¿Dónde está la biblioteca? Me llamo T-Bone, La araña discoteca.",
        "image": "¿Dónde está la biblioteca? Me llamo T-Bone, La araña discoteca."
    }
}
```

## Ejemplo de respuesta positiva

```json
{
	"message": "success"
}
```

### Ejemplo de respuesta de error

El código de estado `400` podría devolver el siguiente cuerpo de respuesta. Consulte la sección [Solución de problemas](#troubleshooting) para obtener más información sobre los errores que puede encontrar.

```json
{
	"errors": [
		{
			"message": "Something went wrong. Translation IDs are mismatched or translated text exceeds limits."
		}
	]
}
```

## Solución de problemas

La siguiente tabla enumera los posibles errores devueltos y los pasos asociados para solucionarlos.

| Mensaje de error | Solución de problemas |
| --- | --- |
|`INVALID_CAMPAIGN_ID`|Confirma que el ID de la campaña coincide con la campaña que estás traduciendo.|
|`INVALID_LOCALE_ID`|Confirma que tu ID de configuración regional existe en la traducción de tu mensaje.|
|`INVALID_MESSAGE_VARIATION_ID`|Confirma que el ID de tu mensaje es correcto.|
|`INVALID_TRANSLATION_OBJECT`|Los ID de traducción no coinciden o el texto traducido supera los límites.|
|`MESSAGE_NOT_FOUND`|Comprueba el mensaje para traducir.|
|`LOCALE_NOT_FOUND`| Confirma que la configuración regional existe en tu configuración multilingüe. |
|`MISSING_TRANSLATIONS`|Los ID de traducción deben coincidir con el mensaje.|
|`MULTI_LANGUAGE_NOT_ENABLED`|La configuración multilingüe no está activada para tu espacio de trabajo.|
|`MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE`|Solo se pueden traducir las campañas de correo electrónico o los mensajes de Canvas con correos electrónicos.|
|`UNSUPPORTED_CHANNEL`| Solo se pueden traducir los mensajes de las campañas de correo electrónico o los mensajes de Canvas con correos electrónicos.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


          INVALID_CAMPAIGN_ID = "Invalid campaign or step ID"
          INVALID_LOCALE_ID = "Invalid locale ID"
          INVALID_MESSAGE_VARIATION_ID = "Invalid message ID"
          INVALID_TRANSLATION_OBJECT = "Invalid translation object"
          MESSAGE_NOT_FOUND = "Message not found"
          LOCALE_NOT_FOUND = "Locale not found"
          MISSING_TRANSLATIONS = "Missing translations from the request body"
          MULTI_LANGUAGE_NOT_ENABLED = "Multi-language feature is not enabled on this company"
          MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE = "This message does not have multi-language setup"
          UNSUPPORTED_CHANNEL = "This message type does not support multi-language"

{% endapi %}
