---
nav_title: "GET: Ver los valores predeterminados de las fuentes para las etiquetas de traducción de campañas."
article_title: "GET: Ver los valores predeterminados de las fuentes para las etiquetas de traducción de campañas."
search_tag: Punto de conexión
page_order: 3

layout: api_page
page_type: reference
description: "Este artículo describe los detalles sobre el punto final de origen de la traducción de la campaña."
---

{% api %}
# Ver los valores predeterminados de las etiquetas de traducción de una campaña
{% apimethod get %}
/campañas/traducciones/fuente
{% endapimethod %}

> Utiliza este punto final para ver todas las fuentes de traducción predeterminadas para las etiquetas de traducción de una campaña. Estos son los valores dentro del {% raw %}`{% translation id %} source {% endtranslation %}`{% endraw %}. Consulta [Locales en los mensajes]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/) para obtener más información sobre las características de la localización.

{% multi_lang_include early_access_beta_alert.md feature='This endpoint' %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `campaigns.translations.get`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parámetros de consulta

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
|`campaign_id`| Obligatoria | Cadena | El ID de su campaña. |
|`message_variation_id`| Obligatoria | Cadena | El ID de tu variación de mensaje. |
|`locale_id`| Opcional | Cadena | Un UUID local para filtrar las respuestas. |
|`post_launch_draft_version`| Opcional | Booleano | Cuando`true`  devuelve la última versión preliminar en lugar de la última versión publicada en vivo. Predeterminado,`false`devuelve la última versión en vivo.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Todos los ID de traducción se consideran identificadores únicos universales (UUID), que se pueden encontrar en la respuesta del punto final GET.
{% endalert %}

## Ejemplo de solicitud

```
curl --location --request GET 'https://rest.iad-03.braze.com/campaigns/translations/source?campaign_id={campaign_id}&message_variation_id={message_variation_id}&locale_id={locale_uuid}&post_launch_draft_version=true' \
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
