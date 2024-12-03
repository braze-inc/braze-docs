---
nav_title: "GET: Ver información sobre los bloques de contenido"
article_title: "GET: Ver información sobre los bloques de contenido"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Ver información de los bloques de contenido de Braze."
---

{% api %}
# Ver información del bloque de contenido
{% apimethod get %}
/content_blocks/info
{% endapimethod %}

> Utiliza este punto final para llamar a la información de tus [Bloques de contenido]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) existentes.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#589adda3-0def-4369-9ddc-eae71923c0ee {% endapiref %}

## Requisitos previos
Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/api_key/) con el permiso `content_blocks.info`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `content_block_id`  | Obligatoria | Cadena | El identificador del bloque de contenido. <br><br>Puedes encontrarlo listando la información del Bloque de Contenido a través de una llamada a la API o yendo a la página [Claves de la API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/), y desplazándote hasta el final y buscando tu identificador de la API del Bloque de Contenido.|
| `include_inclusion_data`  | Opcional | Booleano | Cuando se establece en `true`, la API devuelve el identificador de la API de variación de mensajes de las campañas y lienzos en los que se incluye este bloque de contenido, para utilizarlo en llamadas posteriores.  Los resultados excluyen campañas o Lienzos archivados o eliminados. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/content_blocks/info?content_block_id={{content_block_id}}&include_inclusion_data=false' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Respuesta

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "content_block_id": (string) the Content Block identifier,
  "name": (string) the name of the Content Block,
  "content": (string) the content in the Content Block,
  "description": (string) the Content Block description,
  "content_type": (string) the content type, html or text,
  "tags": (array) An array of tags formatted as strings,
  "created_at": (string) The time the Content Block was created in ISO 8601,
  "last_edited": (string) The time the Content Block was last edited in ISO 8601,
  "inclusion_count" : (integer) the inclusion count,
  "inclusion_data": (array) the inclusion data,
  "message": "success",
}
```

## Solución de problemas

La siguiente tabla enumera los posibles errores devueltos y sus pasos asociados para la solución de problemas.

| Error | Solución de problemas |
| --- | --- |
| `Content Block ID cannot be blank` | Asegúrate de que en tu petición aparece un bloque de contenido y de que está encapsulado entre comillas (`""`). |
| `Content Block ID is invalid for this workspace` | Este bloque de contenido no existe o está en una cuenta de empresa o espacio de trabajo diferente. |
| `Content Block has been deleted—content not available` | Este bloque de contenido, aunque puede haber existido antes, ha sido eliminado. |
| `Include Inclusion Data—error` | Este parámetro solo acepta valores booleanos (verdadero o falso). Asegúrate de que el valor de `include_inclusion_data` no está encapsulado entre comillas (`""`), lo que hace que el valor se envíe como una cadena. Consulta los [parámetros de la solicitud](#request-parameters) para más detalles. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


{% endapi %}
