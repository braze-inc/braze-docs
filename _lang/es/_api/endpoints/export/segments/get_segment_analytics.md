---
nav_title: "GET: Análisis de segmentos de exportación"
article_title: "GET: Análisis de segmentos de exportación"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Exportar análisis de segmentos de Braze."

---
{% api %}
# Análisis de segmentos de exportación
{% apimethod get %}
/segments/data_series
{% endapimethod %}

> Utilice este punto final para recuperar una serie diaria del tamaño estimado de un segmento a lo largo del tiempo.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#62d9d142-cdec-4aea-a287-c13efea7415e {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `segments.data_series`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | -------- | --------- | ----------- |
| `segment_id` | Obligatoria | Cadena | Ver [Identificador API de segmento]({{site.baseurl}}/api/identifier_types/).<br><br> La dirección `segment_id` para un segmento determinado se puede encontrar en la página [Claves de API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) dentro de su cuenta Braze o puede utilizar el [punto final Exportar lista de segmentos]({{site.baseurl}}/api/endpoints/export/segments/get_segment/).  |
| `length` | Obligatoria | Entero | Número máximo de días antes de `ending_at` a incluir en la serie devuelta. Debe estar comprendido entre 1 y 100 (ambos inclusive). |
| `ending_at` | Opcional | Fecha y hora <br>(cadena [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Fecha en la que debe finalizar la serie de datos. De forma predeterminada, la hora de la solicitud. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/segments/data_series?segment_id={{segment_identifier}}&length=14&ending_at=2018-06-27T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Respuesta

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) the date as ISO 8601 date,
            "size" : (int) the size of the segment on that date
        },
        ...
    ]
}
```

{% alert tip %}
Para obtener ayuda con las exportaciones CSV y API, visita [Solución de problemas de exportación]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
