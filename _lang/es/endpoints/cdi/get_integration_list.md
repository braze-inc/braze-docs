---
nav_title: "GET: Lista de integraciones"
article_title: "GET: Lista de integraciones"
search_tag: Endpoint
page_order: 1
alias: /api/cdi/get_integration_list/
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Enumerar integraciones de Braze."

---
{% api %}
# Lista de integraciones
{% apimethod get %}
/cdi/integrations
{% endapimethod %}

> Utiliza este punto final para obtener una lista de las integraciones existentes.


{% alert note %}
Para utilizar este punto final, deberás generar una clave de API con el permiso .
{% endalert %}

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='cdi list integrations' %}

## Parámetros de consulta

Cada llamada a este punto final devolverá 10 elementos. Para una lista con más de 10 integraciones, utiliza la cabecera `Link` para recuperar los datos en la página siguiente, como se muestra en el ejemplo de respuesta.

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `cursor` | Opcional | Cadena | Determina la paginación de la lista de integración. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud

### Sin cursor

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### Con cursor

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Respuesta

### Ejemplo de respuesta satisfactoria

El código de estado `200` podría devolver el siguiente cuerpo de respuesta.

{% alert note %}
La cabecera `Link` no existirá si hay menos o igual a 10 integraciones en total. En las llamadas sin cursor, `prev` no se mostrará. Al consultar la última página de elementos, `next` no se mostrará.
{% endalert %}

```
Link: </cdi/integrations?cursor=c2tpcDow>; rel="prev",</cdi/integrations?cursor=c2tpcDoxMDA=>; rel="next"
```

```json
{
  "results": [
    {
      "integration_id": (string) integration ID,
      "app_group_id": (string) app group ID,
      "integration_name": (string) integration name,
      "integration_type": (string) integration type,
      "integration_status": (string) integration status,
      "contact_emails": (string) contact email(s),
      "last_updated_at": (string) last timestamp that was synced in ISO 8601,
      "warehouse_type": (string) data warehouse type,
      "last_job_start_time": (string) timestamp of the last sync run in ISO 8601,
      "last_job_status": (string) status of the last sync run,
      "next_scheduled_run": (string) timestamp of the next scheduled sync in ISO 8601,
    },
  ],
  "message": "success"
}
```

## Solución de problemas

La siguiente tabla enumera los posibles errores devueltos y sus pasos asociados para la solución de problemas.

| Error | Solución de problemas |
| --- | --- |
| `400 Invalid cursor` | Compruebe que su `cursor` es válido. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para obtener más códigos de estado y mensajes de error asociados, consulta [Errores fatales & respuestas]({{site.baseurl}}/api/errors/#fatal-errors).

{% endapi %}
