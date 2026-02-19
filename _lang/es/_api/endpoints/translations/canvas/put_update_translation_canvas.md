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

> Utilice este punto final para actualizar varias traducciones de un lienzo. Consulta [Locales en los mensajes]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/) para obtener más información sobre las características de traducción.

Si quieres actualizar las traducciones después de haber lanzado un Canvas, tendrás que [guardar]({{site.baseurl}}/post-launch_edits/) primero [tu mensaje como borrador]({{site.baseurl}}/post-launch_edits/).

{% alert important %}
Este punto final se encuentra actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en el acceso anticipado.
{% endalert %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `canvas.translations.update`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parámetros de la ruta

No hay parámetros de ruta para este punto final.

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
|`workflow_id` | Obligatoria | Cadena | ID del Canvas. |
|`step_id`| Obligatoria | Cadena | El ID de tu paso en Canvas. |
|`message_variation_id`| Obligatoria | Cadena | El ID de la variación de tu mensaje. |
|`locale_id`| Obligatoria | Cadena | El ID (UUID) de la localización. |
|`translation_map` | Obligatoria | Objeto | Objeto que contiene las nuevas traducciones. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Todos los ID de traducción se consideran identificadores únicos universales (UUID), que pueden encontrarse en la respuesta del punto final GET.
{% endalert %}

## Ejemplo de solicitud

```json
{
    "workflow_id": "a74404b3-3626-4de0-bdec-06935f3aa0ad",
    "step_id": "a74404b3-3626-4de0-bdec-06935f3aa0ac",
    "message_variation_id": "a74404b3-3626-4de0-bdec-06935f3aa0ac",
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

{% endapi %}
