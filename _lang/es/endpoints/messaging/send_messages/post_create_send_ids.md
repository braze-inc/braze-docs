---
nav_title: "PUBLICAR: Crear ID de envío"
article_title: "PUBLICAR: Crear ID de envío"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Crear ID de envío de Braze."

---
{% api %}
# Crear ID de envío
{% apimethod post %}
/sends/id/create
{% endapimethod %}

> Utiliza este punto final para crear ID de envío que puedan utilizarse para enviar mensajes y hacer un seguimiento del rendimiento de los mensajes mediante programación, sin necesidad de crear campañas para cada envío.

Utilizar el identificador de envío para el seguimiento y envío de mensajes es útil si piensas generar y enviar contenido mediante programación.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#74a04e53-659f-4473-abc5-0f6f735550ff {% endapiref %}

## Requisitos previos

Para utilizar este punto final, deberás generar una clave de API con el permiso `sends.id.create`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='sends id create' %}

## Cuerpo de la solicitud

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "send_id": (optional, string) see send identifier
}
```

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Obligatoria | Cadena | Ver [identificador de campaña]({{site.baseurl}}/api/identifier_types/). |
|`send_id`| Opcional | Cadena | Ver [identificador de envío]({{site.baseurl}}/api/identifier_types/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud
```
curl --location --request POST 'https://rest.iad-01.braze.com/sends/id/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier"
}'
```

## Respuesta

### Ejemplo de respuesta satisfactoria

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "message": "success",
  "send_id" : (string) the send identifier
}
```

{% endapi %}
