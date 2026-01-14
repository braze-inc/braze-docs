---
nav_title: "GET: Detalles del segmento de exportación"
article_title: "GET: Detalles del segmento de exportación"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Exportar detalles del segmento de Braze."

---
{% api %}
# Detalles del segmento de exportación
{% apimethod get %}
/segments/details
{% endapimethod %}

> Utiliza este punto final para recuperar información relevante sobre un segmento, que puede identificarse mediante la dirección `segment_id`.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aab56ed9-0a28-476a-8b57-b79786dbb9c1 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `segments.details`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parámetros de la solicitud

| Parámetro    | Obligatoria | Tipo de datos | Descripción            |
| ------------ | -------- | --------- | ---------------------- |
| `segment_id` | Obligatoria | Cadena | Ver [Identificador API de segmento]({{site.baseurl}}/api/identifier_types/).<br><br> La dirección `segment_id` para un segmento determinado se puede encontrar en la página [Claves de API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) dentro de su cuenta Braze o puede utilizar el [punto final Exportar lista de segmentos]({{site.baseurl}}/api/endpoints/export/segments/get_segment/).  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/segments/details?segment_id={{segment_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Respuesta

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
      "message": (required, string) the status of the export, returns 'success' when completed without errors,
      "created_at" : (string) the date created as ISO 8601 date,
      "updated_at" : (string) the date last updated as ISO 8601 date,
      "name" : (string) the segment name,
      "description" : (string) a human-readable description of filters,
      "text_description" : (string) the segment description,
      "tags" : (array) the tag names associated with the segment formatted as strings,
      "teams" : (array) the names of the Teams associated with the campaign
}
```

{% alert tip %}
Para obtener ayuda con las exportaciones CSV y API, visita [Solución de problemas de exportación]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
