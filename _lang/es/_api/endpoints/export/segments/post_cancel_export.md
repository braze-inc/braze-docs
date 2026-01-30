---
nav_title: "PUBLICAR: Cancela las exportaciones por segmento"
article_title: "PUBLICAR: Cancela las exportaciones por segmento"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles de Cancelar exportaciones por segmento en el punto final Braze."

---
{% api %}
# Cancela las exportaciones por segmento
{% apimethod post %}
/exportar/segmento/cancelar
{% endapimethod %}

> Utiliza este punto final para cancelar todas las exportaciones en curso con un ID de segmento especificado.

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `segments.list`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Cuerpo de la solicitud

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "segment_id": (required, string) the `segment_id` to locate and cancel its ongoing exports
}
```

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `segment_id` | Obligatoria | Cadena | La `segment_id` para cancelar sus exportaciones en curso. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud
```
curl --location --request POST 'https://rest.iad-01.braze.com/export/segment/cancel' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "segment_id": "segment_identifier"
}'
```

{% endapi %}

