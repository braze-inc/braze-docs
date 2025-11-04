---
nav_title: "PUBLICAR: Actualizar alias de usuario"
article_title: "PUBLICAR: Actualizar alias de usuario"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Actualizar alias de usuario de Braze."
---
{% api %}
# Actualizar alias de usuario
{% apimethod post %}
/users/alias/update
{% endapimethod %}

> Utiliza este punto final para actualizar los alias de usuario existentes.

Se pueden especificar hasta 50 alias de usuario por solicitud.

Para actualizar un alias de usuario, es necesario incluir `alias_label`, `old_alias_name` y `new_alias_name` en el objeto de actualizar alias de usuario. Si no hay ningún alias de usuario asociado a `alias_label` y `old_alias_name`, no se actualizará ningún alias. Si se encuentra el `alias_label` y el `old_alias_name` dados, entonces el `old_alias_name` se actualizará al `new_alias_name`.

{% alert note %}
Este punto final no garantiza la secuencia de actualización de los objetos de `alias_updates`.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#a084b843-b3cd-43f0-bfb1-ef7bada839c5 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/api_key/) con el permiso `users.alias.update`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='users alias update' %}

## Cuerpo de la solicitud

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "alias_updates" : (required, array of update user alias object)
}
```

### Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | --------- | --------- | ----------- |
| `alias_updates` | Obligatoria | Matriz de objetos de actualización de alias de usuario | Ver [objeto alias de usuario]({{site.baseurl}}/api/objects_filters/user_alias_object/).<br><br> Para más información sobre `old_alias_name`, `new_alias_name`, y `alias_label`, consulta [Alias de usuario]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Cuerpo de la solicitud de punto final con especificación de objeto de actualizar alias de usuario

```json
{
  "alias_label" : (required, string),
  "old_alias_name" : (required, string),
  "new_alias_name" : (required, string)
}
```

## Ejemplo de solicitud
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/alias/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "alias_updates" :[
    {
      "alias_label": "example_alias_label",
      "old_alias_name" : "example_old_alias_name",
      "new_alias_name" : "example_new_alias_name"
    }
  ]
}'
```

{% endapi %}

