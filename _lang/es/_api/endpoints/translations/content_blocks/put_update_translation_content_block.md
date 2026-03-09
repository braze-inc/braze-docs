---
nav_title: "COLOCAR: Actualizar la traducción en un bloque de contenido"
article_title: "COLOCAR: Actualizar la traducción en un bloque de contenido"
search_tag: Punto de conexión
page_order: 2

layout: api_page
page_type: reference
description: "Este artículo describe los detalles sobre la actualización de la traducción en un punto final del bloque de contenido."
---

{% api %}
# Actualizar la traducción en un bloque de contenido
{% apimethod put %}
/content_blocks/translations
{% endapimethod %}

> Utiliza este punto final para actualizar varias traducciones de un [bloque de contenido]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/). Consulta [Locales en los mensajes]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/) para obtener más información sobre las características de traducción.

{% include early_access_beta_alert.md feature='This endpoint' %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `content_blocks.translations.update`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parámetros de la ruta

No hay parámetros de ruta para este punto final.

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `content_block_id` | Obligatoria | Cadena | El ID de tu bloque de contenido. |
| `locale_id`| Obligatoria | Cadena | El ID (UUID) de la configuración regional. |
| `translation_map` | Obligatoria | Objeto | Objeto que contiene las nuevas traducciones. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Todos los ID de traducción se consideran identificadores únicos universales (UUID), que se pueden encontrar en la respuesta del punto final GET.
{% endalert %}

## Ejemplo de solicitud

```json
{
    "content_block_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
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
