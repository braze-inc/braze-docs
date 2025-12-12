---
nav_title: "GET: Exportar lista de Canvas"
article_title: "GET: Exportar lista de Canvas"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Braze Exportar lista de Canvas."

---
{% api %}
# Exportar lista de Canvas
{% apimethod get %}
/canvas/list
{% endapimethod %}

> Utiliza este punto final para exportar una lista de Canvas, incluyendo el nombre, el identificador de la API de Canvas y las etiquetas asociadas.

Los lienzos se devuelven en grupos de 100 ordenados por fecha de creación (de más antiguo a más reciente por predeterminado).

Los lienzos archivados no se incluirán en la respuesta de la API a menos que se especifique el campo `include_archived`. Sin embargo, los lienzos parados pero no archivados se devolverán predeterminadamente.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e6c150d7-fceb-4b10-91e2-a9ca4d5806d1 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `canvas.list`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | -------- | --------- | ----------- |
| `page` | Opcional | Entero | La página de Lienzos a devolver, predeterminada a `0` (devuelve el primer conjunto de hasta 100) |
| `include_archived` | Opcional | Booleano | Incluir o no los Canvas archivados, de manera predeterminada, `false`. |
| `sort_direction` | Opcional | Cadena | \- Ordenar la hora de creación de más reciente a más antigua: introduce el valor `desc`.<br> \- Ordenar la hora de creación de más antiguo a más reciente: introduce el valor `asc`. <br><br>Si no se incluye `sort_direction`, el orden predeterminado es del más antiguo al más reciente. |
| `last_edit.time[gt]` | Opcional | Tiempo | Filtra los resultados y sólo devuelve los lienzos que se hayan editado más del tiempo indicado hasta ahora. El formato es `yyyy-MM-DDTHH:mm:ss`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud

```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/list?page=1&include_archived=false&sort_direction=desc&last_edit.time[gt]=2020-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Respuesta

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "canvases" : [
  	{
  		"id" : (string) the Canvas API identifier,
  		"last_edited": (ISO 8601 string) the last edited time for the message,
  		"name" : (string) the Canvas name,
  		"tags" : (array) the tag names associated with the Canvas formatted as strings,
  	},
    ... (more Canvases)
  ],
  "message": (required, string) the status of the export, returns 'success' when completed without errors
}
```

{% alert tip %}
Para obtener ayuda con las exportaciones CSV y API, visita [Solución de problemas de exportación]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
