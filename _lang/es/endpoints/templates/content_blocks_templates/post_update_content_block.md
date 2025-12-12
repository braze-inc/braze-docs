---
nav_title: "PUBLICAR: Actualizar bloque de contenido"
article_title: "PUBLICAR: Actualizar bloque de contenido"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Actualizar bloques de contenido de Braze."

---
{% api %}
# Actualizar bloque de contenido
{% apimethod post %}
/content_blocks/update
{% endapimethod %}

> Utiliza este punto final para actualizar un [Bloque de contenido]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4782239a-cb60-4217-9de0-51411434d57d {% endapiref %}

## Requisitos previos
Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/api_key/) con el permiso `content_blocks.update`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Cuerpo de la solicitud

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "content_block_id" : (required, string) Content Block's API identifier.
  "name": (optional, string) Must be less than 100 characters,
  "description": (optional, string) The description of the Content Block. Must be less than 250 character,
  "content": (optional, string) HTML or text content within Content Block,
  "state": (optional, string) Choose `active` or `draft`. Defaults to `active` if not specified,
  "tags": (optional, array of strings) Tags must already exist
}
```

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `content_block_id`|	Obligatoria |	Cadena | El identificador de la API de tu bloque de contenido.|
| `name` | Opcional | Cadena | Nombre del bloque de contenido. Debe tener menos de 100 caracteres. |
| `description` | Opcional | Cadena | Descripción del bloque de contenido. Debe tener menos de 250 caracteres. |
| `content` | Opcional | Cadena | Contenido HTML o de texto dentro de los bloques de contenido.
| `state` | Opcional | Cadena | Elige `active` o `draft`. Predetermina `active` si no se especifica. |
| `tags` | Opcional | Matriz de cadenas | [Las etiquetas]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) ya deben existir. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud
```json
curl --location --request POST 'https://rest.iad-01.braze.com/content_blocks/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "content_block_id" :"content_block_id",
  "name": "content_block",
  "description": "This is my Content Block",
  "content": "HTML or text content within block",
  "state": "draft",
  "tags": ["marketing"]
}'
```

## Respuesta

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "content_block_id": (string) Your newly generated block id,
  "liquid_tag": (string) The generated block tag from the Content Block name,
  "created_at": (string) The time the Content Block was created in ISO 8601,
  "message": "success"
}
```

## Solución de problemas

La siguiente tabla enumera los posibles errores devueltos y sus pasos asociados para la solución de problemas.

| Error | Solución de problemas |
| --- | --- |
| `Content cannot be blank` |
| `Content must be a string` | Asegúrate de que tu contenido está entre comillas (`""`). |
| `Content must be smaller than 50kb` | El contenido de tu bloque de contenido debe ser inferior a 50 KB en total. |
| `Content contains malformed liquid` | El Liquid proporcionado no es válido ni analizable. Inténtalo de nuevo con un Liquid válido o ponte en contacto con el servicio de asistencia. |
| `Content Block cannot be referenced within itself` |
| `Content Block description cannot be blank` |
| `Content Block description must be a string` | Asegúrate de que la descripción de tu bloque de contenido está entre comillas (`""`). |
| `Content Block description must be shorter than 250 characters` |
| `Content Block name cannot be blank` |
| `Content Block name must be shorter than 100 characters` |
| `Content Block name can only contain alphanumeric characters` | Los nombres de los bloques de contenido pueden incluir cualquiera de los siguientes caracteres: las letras (mayúsculas o minúsculas) `A` a `Z`, los números `0` a `9`, guiones `-` y guiones bajos `_`. No puede contener caracteres no alfanuméricos como emojis, `!`, `@`, `~`, `&` y otros caracteres "especiales". |
| `Content Block with this name already exists` | Prueba con otro nombre. |
| `Content Block name cannot be updated for active Content Blocks` |
| `Content Block state must be either active or draft` |
| `Active Content Block can not be updated to Draft. Create a new Content Block.` |
| `Tags must be an array` | Las etiquetas deben formatearse como una matriz de cadenas, por ejemplo `["marketing", "promotional", "transactional"]`. |
| `All tags must be strings` | Asegúrate de que tus etiquetas estén entre comillas (`""`). |
| `Some tags could not be found` | Para añadir una etiqueta al crear un Bloque de contenido, la etiqueta debe existir ya en Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


{% endapi %}
