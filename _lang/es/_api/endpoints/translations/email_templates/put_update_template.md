---
nav_title: "COLOCAR: Actualizar las traducciones de una plantilla de correo electrónico"
article_title: "COLOCAR: Actualizar las traducciones de una plantilla de correo electrónico"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "Este artículo describe los detalles sobre las traducciones de actualización para un punto final de plantilla de correo electrónico."
---

{% api %}
# Actualizar las traducciones de una plantilla de correo electrónico
{% apimethod put %}
/plantillas/correo electrónico/traducciones/
{% endapimethod %}

> Utiliza este punto final para actualizar las traducciones de una [plantilla de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates). Consulta [Locales en los mensajes]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/) para obtener más información sobre las características de traducción.

{% alert important %}
Este punto final se encuentra actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en el acceso anticipado.
{% endalert %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `templates.translations.update`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parámetros de la ruta

No hay parámetros de ruta para este punto final.

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `template_id` | Obligatoria | Cadena | El ID de tu plantilla de correo electrónico. |
| `locale_id` | Obligatoria | Cadena | El ID de la configuración regional. |
| `translations_map` | Obligatoria | Cadena | El mapeado de las traducciones para tu plantilla de correo electrónico. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Todos los ID de traducción se consideran identificadores únicos universales (UUID), que pueden encontrarse en la respuesta del punto final GET.
{% endalert %}

## Ejemplo de solicitud

```json
{
    "template_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
    "locale_id": "h94404b3-3626-4de0-bdec-06935f3aa0ad",
    "translation_map": {
        "id_0": "¡Hola!",
        "id_1": "Me llamo Jacky",
        "id_2": "¿Dónde está la biblioteca?"
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
			"id": "1234567-abc-123-012345678",
			"message": "The provided translations yielded errors when parsing. Please contact Braze for more information."
		}
	]
}
```

{% endapi %}
