---
nav_title: "PUBLICAR: Sincronización del desencadenador"
article_title: "PUBLICAR: Sincronización de desencadenante"
search_tag: Endpoint
page_order: 2
alias: /api/cdi/post_trigger_sync/
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Desencadenar sincronización de Braze."

---
{% api %}
# Desencadenar una sincronización
{% apimethod post %}
/cdi/integrations/{integration_id}/sync
{% endapimethod %}

> Utiliza este punto final para desencadenar una sincronización para una integración determinada.

{% alert note %}
Para utilizar este punto final, deberás generar una clave de API con el permiso .
{% endalert %}

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='cdi job sync' %}

## Parámetros de la ruta

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `integration_id` | Obligatoria | Cadena | ID de integración. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud

```
curl --location --request POST 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Respuesta

### Ejemplo de respuesta satisfactoria

El código de estado `202` podría devolver el siguiente cuerpo de respuesta:

```json
{
  "message": "success"
}
```

## Solución de problemas

La siguiente tabla enumera los posibles errores devueltos y sus pasos asociados para la solución de problemas.

| Error | Solución de problemas |
| --- | --- |
| `400 Invalid integration ID` | Compruebe que su `integration_id` es válido. |
| `404 Integration not found` | No existe ninguna integración para el ID de integración dado. Asegúrate de que tu ID de integración es válido. |
| `429 Another job is in progress` | Actualmente se está ejecutando una sincronización para esta integración. Inténtalo de nuevo cuando se haya completado la sincronización. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para obtener más códigos de estado y mensajes de error asociados, consulta [Errores fatales & respuestas]({{site.baseurl}}/api/errors/#fatal-errors).

{% endapi %}
