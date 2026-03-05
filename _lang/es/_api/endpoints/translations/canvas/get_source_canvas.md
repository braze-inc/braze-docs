---
nav_title: "GET: Ver los valores de origen predeterminados para las etiquetas de traducción de Canvas"
article_title: "GET: Ver los valores de origen predeterminados para las etiquetas de traducción de Canvas"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final de la fuente de traducción de Canvas."
---

{% api %}
# Ver los valores de origen predeterminados para las etiquetas de traducción de un Canvas
{% apimethod get %}
/canvas/traducciones/fuente
{% endapimethod %}

> Utiliza este punto final para ver todas las fuentes de traducción predeterminadas para las etiquetas de traducción de un Canvas. Estos son los valores con el {% raw %}`{% translation id %} source {% endtranslation %}`{% endraw %}. Consulta [Locales en los mensajes]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/) para obtener más información sobre las características de traducción.

{% alert important %}
Este punto final se encuentra actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en el acceso anticipado.
{% endalert %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `canvas.translations.get`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parámetros de consulta

| Parámetro              | Obligatoria | Tipo de datos | Descripción                        |
|------------------------|----------|-----------|------------------------------------|
| `workflow_id`          | Obligatoria | Cadena    | ID del Canvas.              |
| `step_id`              | Obligatoria | Cadena    | El ID de tu paso en Canvas.        |
|`message_variation_id`| Obligatoria | Cadena | El ID de la variación de tu mensaje. |
| `locale_id`            | Opcional | Cadena    | El ID (UUID) de la localización.              |
| `post_launch_draft_version`| Opcional | Booleano | Cuando `true` devuelve la última versión borrador en lugar de la última versión publicada en vivo. Predetermina `false` devolviendo la última versión en vivo.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Todos los ID de traducción se consideran identificadores únicos universales (UUID), que pueden encontrarse en la respuesta del punto final GET.
{% endalert %}

## Ejemplo de solicitud

```
curl --location --request GET 'https://rest.iad-03.braze.com/canvas/translations/source?workflow_id={workflow_id}&step_id={step_id}&message_variation_id={message_variation_id}&locale_id={locale_uuid}&post_launch_draft_version=true' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Respuesta

Hay cuatro respuestas de código de estado para este punto final: `200`, `400`, `404` y `429`.

### Ejemplo de respuesta positiva

El código de estado `200` podría devolver la siguiente cabecera y cuerpo de respuesta.

```json
{
   "translations": {
       "translation_map": {
           "id_0": "Here's a Million Dollars",
           "id_1": "Hello World!"
       }
   },
   "message": "success"
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

{% endapi %}
