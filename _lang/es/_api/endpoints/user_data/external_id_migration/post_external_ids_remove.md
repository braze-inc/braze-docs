---
nav_title: "POST: Eliminar ID externo"
article_title: "POST: Eliminar ID externo"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Eliminar ID externos."

---
{% api %}
# Eliminar ID externo
{% apimethod post %}
/users/external_ids/remove
{% endapimethod %}

> Utiliza este punto final para eliminar los antiguos ID externos obsoletos de tus usuarios. 

Puedes enviar hasta 50 ID externos por solicitud. 

{% alert warning %}
Este punto final elimina completamente el ID obsoleto y no puede deshacerse. Si utilizas este punto final para eliminar la dirección `external_ids` obsoleta que todavía está asociada a usuarios de tu sistema, puedes impedir permanentemente que encuentres los datos de esos usuarios.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e16b5340-5f44-42b6-9033-2398faf8908e {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/api_key/) con el permiso `users.external_ids.remove`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='external id migration' %}

## Cuerpo de la solicitud

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_ids" : (required, array of external identifiers to remove)
}
```

### Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `external_ids` | Obligatoria | Matriz de cadenas | Identificadores externos para que los usuarios los eliminen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/external_ids/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_ids" :[
    "existing_deprecated_external_id_string",
    ...
  ]
}'
```

{% alert important %}
Solo se pueden eliminar los ID obsoletos; si se intenta eliminar un ID externo primario se producirá un error.
{% endalert %}

## Respuesta

La respuesta confirmará todas las retiradas realizadas con éxito, así como las retiradas fallidas con los errores asociados. Los mensajes de error del campo `removal_errors` harán referencia al índice de la matriz de la solicitud original.

```
{
  "message" : (string) status message,
  "removed_ids" : (array of strings) successful remove operations,
  "removal_errors": (array of arrays) <minor error message>
}
```

El campo `message` devolverá `success` para cualquier solicitud válida. Los errores más específicos se recogen en la matriz `removal_errors`. El campo `message` devuelve un error en caso de:
- Clave de API no válida
- Matriz vacía `external_ids` 
- `external_ids` matriz con más de 50 elementos
- Alcanzado el límite de velocidad (más de 1.000 solicitudes/minuto)

{% endapi %}
