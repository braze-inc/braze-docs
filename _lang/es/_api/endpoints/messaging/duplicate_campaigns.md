---
nav_title: "POST: Campañas duplicadas"
article_title: "POST: Campañas duplicadas"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Duplicar campañas."

---
{% api %}
# Duplicar campañas a través de la API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/duplicate
{% endapimethod %}

> Utilice este punto final para duplicar campañas. Este punto final de la API es similar a la [duplicación de campañas en el panel de control de Braze][1].

{% alert important %}
Duplicar una campaña a través de la API se encuentra actualmente en acceso temprano. Póngase en contacto con su gestor de cuenta Braze si está interesado en participar en el acceso anticipado.
{% endalert %}

## Requisitos previos

Para utilizar este punto final, deberás generar una clave de API con el permiso `campaigns.duplicate`.

## Límite de velocidad

Este punto final está limitado a 100 llamadas API por minuto.

## Cuerpo de la solicitud

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) The campaign identifier,
  "name": (required, string) The name of the resulting campaign,
  "description": (optional, string) The description of the resulting campaign,
}
```

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
|`campaign_id`| Obligatoria | Cadena | Ver [identificador de campaña]({{site.baseurl}}/api/identifier_types/). |
|`name`| Obligatoria | Cadena | El nombre de la campaña resultante. |
|`description`| Opcional | Cadena | El campo de descripción de la campaña resultante. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


## Respuesta

Este punto final devolverá un código de estado `202`, y la creación de la campaña se producirá de forma asíncrona. Puede utilizar la [descarga de eventos de seguridad][2] para ver los registros de cuándo se duplicaron las campañas y mediante qué clave API.



[1]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns#duplicating-segments-campaigns-and-canvases
[2]: {{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/?redirected=true#security-event-download

{% endapi %}
