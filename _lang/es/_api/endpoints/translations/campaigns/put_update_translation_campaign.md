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

> Utilice este punto final para actualizar varias traducciones de una campaña. Consulta [Locales en los mensajes]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/) para obtener más información sobre las características de traducción.

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
| `locale_id`| Obligatoria | Cadena | El ID (UUID) de la localización. |
| `translation_map` | Obligatoria | Objeto | Objeto que contiene las nuevas traducciones. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Todos los ID de traducción se consideran identificadores únicos universales (UUID), que pueden encontrarse en la respuesta del punto final GET.
{% endalert %}

## Ejemplo de solicitud

```json
{
    "campaign_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
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

{% endapi %}
