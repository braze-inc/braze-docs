---
nav_title: "PUBLICAR: Lienzos duplicados"
article_title: "PUBLICAR: Lienzos duplicados"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Lienzos duplicados."
---

{% api %}
# Duplicar lienzos utilizando la API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/duplicate
{% endapimethod %}

> Utiliza este punto final para duplicar Lienzos. Este punto final de la API es similar a [duplicar Lienzos en el panel de Braze][1].

{% alert important %}
Este punto final se encuentra actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en el acceso anticipado.
{% endalert %}

## Requisitos previos

Para utilizar este punto final, deberás generar una clave de API con el permiso `canvas.duplicate`.

## Límite de velocidad

Este punto final está limitado a 100 llamadas API por minuto.

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
|`tag_names` | Opcional | Cadena | Las etiquetas para el Canvas resultante. Deben ser etiquetas existentes. Si añades nuevas etiquetas en la solicitud, éstas sobrescribirán cualquier etiqueta que hubiera en el Canvas original. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Respuesta

Este punto final devolverá un código de estado `202`, y la creación del Canvas se producirá de forma asíncrona. Puedes utilizar la [descarga de eventos de Seguridad][2] para ver los registros de cuándo se duplicaron los Lienzos y mediante qué clave de API.

[1]: {{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/duplicating
[2]: {{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings

{% endapi %}
