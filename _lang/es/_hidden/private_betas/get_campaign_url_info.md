---
nav_title: "GET: Alias de enlace de lista para campañas"
layout: api_page
page_type: reference
hidden: true
permalink: /get_campaign_link_alias/

platform: API
channel:
  - Email
tool:
  - Canvas
  - Campaigns

description: "En este artículo se describen los detalles del punto final Listar alias de enlaces de Braze."
---
{% api %}
# Lista de alias de enlaces para la campaña
{% apimethod get %}
/campaigns/url_info/details
{% endapimethod %}

> Utiliza este punto final para listar el alias de enlace establecido en una variante de mensaje de campaña específica.

{% apiref postman %}  {% endapiref %}

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `campaign_id`  | Obligatoria | Cadena | Ver [identificador API de campaña]({{site.baseurl}}/api/identifier_types/#campaign-api-identifier).|
| `message_variation_id `  |  Obligatoria | Cadena | Identificador API de la variante del mensaje. Puedes encontrarlo en la página de detalles de campaña de una campaña, en la sección **Identificador de API**. |
| `includes_link_id` | Opcional | Cadena | Un identificador de enlace específico (asignado por Braze) o `null`. Sirve para filtrar los resultados por un `link_id` concreto. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud
```
curl --location --request GET 'https://rest.iad-01.braze.com/campaigns/url_info/details?campaign_id=4615a404-b2c2-421e-9a04-2233bb3ec4f9&message_variation_id=0ea708fe-36b4-43f7-9f5c-a0650ea2a7a0&includes_link_id=014tk4e0kg97' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Respuesta

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "channel": "email",
  "name": "Variant 1",
  "link_data": [
    {
      "link_URL": "https://www.braze.com?lid=014tk4e0kg97",
      "link_id": "014tk4e0kg97",
      "content_block_path_info": [],
      "link_alias": "link5"
    }
  ],
  "message": "success"
}
```

### Solución de problemas

La siguiente tabla enumera los posibles errores devueltos y sus pasos asociados para la solución de problemas.

| Error | Solución de problemas |
| --- | --- |
| `Missing/Invalid Campaign ID` | El ID de API de la campaña debe ser un identificador de API. Puedes encontrarlo utilizando el [punto final Exportar lista de campañas]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) o accediendo al panel. |
| `Missing/Invalid Message Variant ID` | El ID de API de la variante del mensaje debe ser un identificador de API. Puedes encontrarlo utilizando el [punto final Exportar detalles de campaña]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) o accediendo al panel. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


{% endapi %}
