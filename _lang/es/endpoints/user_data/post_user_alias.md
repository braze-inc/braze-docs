---
nav_title: "PUBLICAR: Crear nuevo alias de usuario"
article_title: "PUBLICAR: Crear nuevo alias de usuario"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Crear nuevo alias de usuario de Braze."

---
{% api %}
# Crear nuevo alias de usuario
{% apimethod post %}
/users/alias/new
{% endapimethod %}

> Utiliza este punto final para añadir nuevos alias de usuario para usuarios identificados existentes, o para crear nuevos usuarios no identificados.

Se pueden especificar hasta 50 alias de usuario por solicitud.

**Añadir un alias de usuario para un usuario existente** requiere incluir un `external_id` en el nuevo objeto alias de usuario. Si el `external_id` está presente en el objeto pero no hay ningún usuario con ese `external_id`, el alias no se añadirá a ningún usuario. Si `external_id` no está presente, se creará un usuario, pero será necesario identificarlo más tarde. Puedes hacerlo utilizando el punto final "Identificación de usuarios" y el punto final `users/identify`.

La **creación de un nuevo usuario solo de alias** requiere que se omita `external_id` en el nuevo objeto alias de usuario. Una vez creado el usuario, utilice el punto final `/users/track` para asociar el usuario de solo alias con atributos, eventos y compras, y el punto final `/users/identify` para identificar al usuario con un `external_id`.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5cf18e64-fd02-452f-8c90-9a0f7c4d0487 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/api_key/) con el permiso `users.alias.new`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='users alias new' %}

## Cuerpo de la solicitud

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "user_aliases" : (required, array of new user alias object)
}
```

### Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `user_aliases` | Obligatoria | Matriz de nuevos objetos alias de usuario | Ver [objeto alias de usuario]({{site.baseurl}}/api/objects_filters/user_alias_object/).<br><br> Para más información sobre `alias_name` y `alias_label`, consulta nuestra documentación [sobre alias de usuario]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases).|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Cuerpo de la solicitud del punto final con la especificación del nuevo objeto alias de usuario

```json
{
  "external_id" : (optional, string),
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```

## Ejemplo de solicitud
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/alias/new' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "user_aliases" :[
    {
      "external_id": "external_identifier",
      "alias_name" : "example_name",
      "alias_label" : "example_label"
    }
  ]
}'
```

## Respuesta

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
    "aliases_processed": 1,
    "message": "success"
}
```


{% endapi %}

