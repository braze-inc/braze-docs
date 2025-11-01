---
nav_title: "PUBLICAR: Borrar usuarios"
article_title: "PUBLICAR: Eliminar usuarios"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Eliminar usuarios de Braze."

---
{% api %}
# Borrar usuarios
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/delete
{% endapimethod %}

> Utiliza este punto final para eliminar cualquier perfil de usuario especificando un identificador de usuario conocido.

Se pueden incluir hasta 50 `external_ids`, `user_aliases`, `braze_ids`, `email_addresses`, o `phone_numbers` en una sola solicitud. Sólo se puede incluir una de las siguientes opciones en una misma solicitud: `external_ids`, `user_aliases`, `braze_ids`, `email_addresses`, o `phone_numbers`. 

Si tienes un caso de uso que no puede resolverse con la eliminación masiva de usuarios a través de la API, ponte en contacto con el [equipo de soporte de Braze]({{site.baseurl}}/user_guide/administrative/access_braze/support/) para obtener ayuda.

{% alert warning %}
La eliminación de perfiles de usuario no se puede deshacer. Eliminará permanentemente los usuarios que puedan causar discrepancias en sus datos. Obtén más información sobre lo que ocurre cuando [eliminas un perfil de usuario utilizando la API]({{site.baseurl}}/help/help_articles/api/delete_user/) en nuestra documentación de Ayuda.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#22e91d00-d178-4b4f-a3df-0073ecfcc992 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/api_key/) con el permiso `users.delete`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='users delete' %}

## Cuerpo de la solicitud

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "external_ids" : (optional, array of string) External IDs to be deleted,
  "user_aliases" : (optional, array of user alias objects) User aliases to be deleted,
  "braze_ids" : (optional, array of string) Braze user identifiers to be deleted,
  "email_addresses": (optional, array of string) User emails to be deleted,
  "phone_numbers": (optional, array of string) User phone numbers to be deleted
}
```
### Parámetros de la solicitud

| Parámetro         | Obligatoria | Tipo de datos                  | Descripción                                                                                      |
|-------------------|----------|----------------------------|--------------------------------------------------------------------------------------------------|
| `external_ids`    | Opcional | Matriz de cadenas           | Identificadores externos que hay que eliminar.                                                    |
| `user_aliases`    | Opcional | Matriz de objeto alias de usuario | [Alias de usuario]({{site.baseurl}}/api/objects_filters/user_alias_object/) a eliminar. |
| `braze_ids`       | Opcional | Matriz de cadenas           | Identificadores de usuario Braze a eliminar.                                                  |
| `email_addresses` | Opcional | Matriz de cadenas           | Correos electrónicos de usuarios que deben eliminarse. Consulta [Eliminar usuarios por correo](#deleting-users-by-email) electrónico para más información.                                                             |
| `phone_numbers` | Opcional | Matriz de cadenas | Números de teléfono de usuario que hay que borrar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Eliminar usuarios por direcciones de correo electrónico y números de teléfono

Si se especifica una dirección de correo electrónico o un número de teléfono como identificador, se requiere un valor adicional `prioritization` en el identificador. `prioritization` debe ser una matriz ordenada y debe especificar qué usuario eliminar si hay varios usuarios. Esto significa que la eliminación de usuarios no se producirá si más de un usuario coincide con una priorización.

Los valores permitidos para la matriz son:

- `identified`
- `unidentified`
- `most_recently_updated` (se refiere a dar prioridad al usuario actualizado más recientemente)

En la matriz `prioritization` sólo puede existir una de las siguientes opciones a la vez:

- `identified` se refiere a dar prioridad a un usuario con un `external_id`
- `unidentified` se refiere a dar prioridad a un usuario sin un `external_id`

## Ejemplo de solicitud

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "external_ids": ["external_identifier1", "external_identifier2"],
  "braze_ids": ["braze_identifier1", "braze_identifier2"],
  "user_aliases": [
    {
      "alias_name": "user_alias1", "alias_label": "alias_label1"
    },
    {
      "alias_name": "user_alias2", "alias_label": "alias_label2"
    }
  ],
  "email_addresses": [
    {
      "email": "john.smith@braze.com",
      "prioritization": ["unidentified", "most_recently_updated"]
    }
  ]
}'
```

## Respuesta

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "deleted" : (required, integer) number of user IDs queued for deletion
}
```
{% endapi %}


