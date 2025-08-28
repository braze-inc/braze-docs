---
nav_title: "COLOCAR: Actualizar la traducción en una campaña"
article_title: "COLOCAR: Actualizar la traducción en una campaña"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Actualizar la traducción en una campaña."
---

{% api %}
# Actualizar la traducción en una campaña
{% apimethod put %}
/campaigns/translations
{% endapimethod %}

> Utilice este punto final para actualizar varias traducciones de una campaña.

Si quieres actualizar las traducciones después de lanzar una campaña, primero tendrás que [guardar tu mensaje como borrador]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/).

{% alert important %}
Este punto final se encuentra actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en el acceso anticipado.
{% endalert %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `campaigns.translations.update`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parámetros de la ruta

No hay parámetros de ruta para este punto final.

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Obligatoria | Cadena | El ID de su campaña. |
| `message_variation_id` | Obligatoria | Cadena | El ID de la variación de tu mensaje. |
| `locale_name` | Obligatoria | Cadena | El nombre de la localización. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Ten en cuenta que todos los ID de traducción se consideran identificadores únicos universales (UUID), que puedes encontrar en la configuración **de Soporte multilingüe** o en la respuesta de la solicitud GET.

## Ejemplo de solicitud

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "campaign_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab", // CAMPAIGNS ONLY
    "message_variation_id": "f14404b3-3626-4de0-bdec-06935f3aa0ad",
    "locale_id": "h94404b3-3626-4de0-bdec-06935f3aa0ad",
    "translation_map": {
        "id_3": "Ein Absatz ohne Formatierung"
    }
}
```

## Respuesta

Hay cuatro respuestas de código de estado para este punto final: `200`, `400`, `404` y `429`.

### Ejemplo de respuesta positiva

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
			"message": "The provided locale code does not exist."
		}
	]
}
```


## Solución de problemas

La siguiente tabla enumera los posibles errores devueltos y los pasos asociados para solucionarlos.

| Mensaje de error  | Solución de problemas |
|----|----------|
| `The provided translations yielded errors when parsing. Please contact Braze for more information.` | Ocurre cuando el traductor externo proporciona traducciones con excepciones que generan errores Liquid. Ponte en contacto con el soporte de Braze para obtener más ayuda. |
| `The provided translations are missing 'id_1', 'id_2'` | Los ID de traducción no coinciden o el texto traducido supera los límites. Por ejemplo, esto podría significar que a la forma de la carga útil le faltan campos en el objeto de traducción. Cada mensaje (cuando está habilitado para la multiidioma) debe tener un número determinado de "bloques de traducción" con un ID asociado. Si a la carga útil proporcionada le falta alguno de los ID, se considerará un objeto incompleto y dará lugar a un error. |
| `The provided locale code does not exist.` | La carga útil del traductor externo contiene un código de localización que no existe en Braze. |
| `The provided translations have exceeded the maximum of 20MB.` | La carga útil proporcionada supera el límite de tamaño. |
| `You have exceeded the maximum number of requests. Please try again later.` | Todas las API de Braze tienen un límite de tasa incorporado, y este error se devolverá automáticamente cuando la tasa haya superado la cantidad asignada para este token de autenticación. |
| `This message does not support multi-language.` | Esto puede ocurrir cuando un ID de mensaje aún no admite mensajes en varios idiomas. Sólo se pueden traducir los mensajes de los siguientes canales: push, mensajes dentro de la aplicación y correo electrónico. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
