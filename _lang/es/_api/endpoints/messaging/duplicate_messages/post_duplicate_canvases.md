---
nav_title: "POST: Duplicar Canvas"
article_title: "POST: Duplicar Canvas"
search_tag: Punto de conexión
page_order: 5
layout: api_page
page_type: reference
description: "Este artículo describe los detalles sobre el punto de conexión Duplicar Canvas."
---

{% api %}
# Duplicar Canvas utilizando la API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/duplicate
{% endapimethod %}

> Utiliza este punto de conexión para duplicar Canvas. Este punto de conexión de la API es similar a [duplicar Canvas en el panel de Braze][1].

## Requisitos previos

Para utilizar este punto de conexión, deberás generar una clave de API con el permiso `canvas.duplicate`.

## Límite de velocidad

Este punto de conexión está limitado a 100 llamadas a la API por minuto.

## Cuerpo de la solicitud

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) The Canvas identifier,
  "name": (required, string) The name of the resulting Canvas,
  "description": (optional, string) The description of the resulting Canvas,
  "tag_names": (optional, string) The tags of the resulting Canvas,
}
```

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
|`canvas_id`| Obligatoria | Cadena | Ver [identificador de Canvas](https://www.braze.com/docs/api/identifier_types/). |
|`name`| Obligatoria | Cadena | El nombre del Canvas resultante. |
|`description`| Opcional | Cadena | El campo de descripción del Canvas resultante. |
|`tag_names` | Opcional | Cadena | Las etiquetas del Canvas resultante. Deben ser etiquetas existentes. Si añades nuevas etiquetas en la solicitud, sobrescribirán cualquier etiqueta que hubiera en el Canvas original. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Respuesta

Este punto de conexión devolverá un código de estado `202`, y la creación del Canvas se producirá de forma asíncrona. Puedes utilizar la [descarga de eventos de seguridad][2] para ver los registros de cuándo se duplicaron los Canvas y mediante qué clave de API.

[1]: {{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/duplicating
[2]: {{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings

{% endapi %}