---
nav_title: "GET: Exportar KPI para desinstalaciones diarias de aplicaciones por fecha"
article_title: "GET: Exportar KPI para desinstalaciones diarias de aplicaciones por fecha"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artículo describe los detalles sobre la Exportación diaria de desinstalaciones de aplicaciones por fecha del punto final Braze."

---
{% api %}
# Exportar KPI para desinstalaciones diarias de aplicaciones por fecha
{% apimethod get %}
/kpi/uninstalls/data_series
{% endapimethod %}

> Utilice este punto final para recuperar una serie diaria del número total de desinstalaciones en cada fecha.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#59c4d592-3e77-42f8-8ff1-d5d250acbeae {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `kpi.uninstalls.data_series`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parámetros de la solicitud

| Parámetro| Obligatoria | Tipo de datos | Descripción |
| -------- | -------- | --------- | ----------- |
| `length` | Obligatoria | Entero | Número máximo de días antes de `ending_at` a incluir en la serie devuelta. Debe estar comprendido entre 1 y 100 (ambos inclusive). |
| `ending_at` | Opcional | Fecha y hora <br>(cadena [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Fecha en la que debe finalizar la serie de datos. De forma predeterminada, la hora de la solicitud. |
| `app_id` | Opcional | Cadena | Identificador de la API de la aplicación recuperado de la página [Claves de API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/). Si se excluye, se mostrarán los resultados de todas las aplicaciones del espacio de trabajo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/kpi/uninstalls/data_series?length=14&ending_at=2018-06-28T23:59:59-5:00&app_id={{app_identifier}}' \
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
            "uninstalls" : (int) the number of uninstalls
        },
        ...
    ]
}
```

{% alert tip %}
Para obtener ayuda con las exportaciones CSV y API, visita [Solución de problemas de exportación]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
