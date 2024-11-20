---
nav_title: "POST: Identificar usuarios"
article_title: "POST: Identificar usuarios"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
alias: /users_identify_merge/
description: "En este artículo se describen los detalles del punto final Identificar usuarios de Braze."

---
{% api %}
# Identificar usuarios
{% apimethod post %}
/users/identify
{% endapimethod %}

> Utiliza este punto final para identificar a un usuario no identificado (sólo alias). 

{% alert important %}
A partir del 7 de agosto de 2023, este punto final fusionará los datos de todas las llamadas. Esto significa que [`merge_behavior`](#merge) se establecerá en `merge` para todas las llamadas.
{% endalert %}

La llamada a `/users/identify` combina el perfil de sólo alias con el perfil identificado y elimina el perfil de sólo alias.

Para identificar a un usuario es necesario incluir un `external_id` en el objeto `aliases_to_identify`. Si no hay ningún usuario con ese `external_id`, el `external_id` se añadirá al registro del usuario aliaseado, y éste se considerará identificado. Puedes añadir hasta 50 alias de usuario por solicitud.

Posteriormente, puedes asociar varios alias de usuario adicionales a un único `external_id`. 
- Cuando estas asociaciones posteriores se realizan con el campo `merge_behavior` configurado como `none`, sólo se conservan los tokens de notificaciones push y el historial de mensajes asociados al alias de usuario; cualquier atributo, evento o compra quedará "huérfano" y no estará disponible para el usuario identificado. Una solución consiste en exportar los datos del usuario alias antes de la identificación mediante el [punto final`/users/export/ids` ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/), y luego volver a asociar los atributos, eventos y compras con el usuario identificado.
- Cuando se realizan asociaciones con el campo `merge_behavior` configurado como `merge`, este punto final fusionará [campos específicos](#merge) encontrados en el usuario anónimo con el usuario identificado.

{% alert tip %}
Para evitar la pérdida inesperada de datos al identificar a los usuarios, te recomendamos encarecidamente que primero consultes [las mejores prácticas de recopilación de datos]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/#capturing-user-data-when-alias-only-user-info-is-already-present) para saber cómo capturar datos de usuario cuando ya existe información de usuario sólo con alias.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f74e0f7-0620-4c7b-b0a2-f5f38fdbff58 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/api_key/) con el permiso `users.identify`.

## Límite de velocidad 
Se aplica un límite de velocidad a las solicitudes realizadas a este punto final para los clientes que se incorporaron a Braze a partir del 16 de septiembre de 2021. Para más información, consulta [Límites de la API]({{site.baseurl}}/api/basics/#api-limits).

## Cuerpo de la solicitud

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
   "aliases_to_identify" : (required, array of alias to identify objects), 
   "merge_behavior": (optional, string) one of 'none' or 'merge' is expected
}
```

### Parámetros de la solicitud

| Parámetro             | Obligatoria | Tipo de datos                           | Descripción                                                                                                                                                                 |
| --------------------- | -------- | ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `aliases_to_identify` | Obligatoria | Conjunto de alias para identificar objetos | Ver [alias para identificar objeto]({{site.baseurl}}/api/objects_filters/aliases_to_identify/) y [alias de usuario objeto]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
| `merge_behavior`      | Opcional | Cadena                              | Se espera una de `merge` o .                                                                                                                                       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

#### Campo Comportamiento_fusión {#merge}

Si se define el campo `merge_behavior` como `merge`, el punto final fusionará cualquiera de los siguientes campos que se encuentren **exclusivamente** en el usuario anónimo con el usuario identificado. 
- Nombre
- Apellido
- Correo electrónico
- Género
- Fecha de nacimiento
- Número de teléfono
- Zona horaria
- Ciudad de origen
- País
- Idioma
- Recuento de sesiones (la suma de las sesiones de ambos perfiles)
- Fecha de la primera sesión (Braze elegirá la fecha más temprana de las dos)
- Fecha de la última sesión (Braze elegirá la fecha más tardía de las dos)
- Atributos personalizados
- Datos personalizados de eventos y compras
- Propiedades del evento personalizado y del evento de compra para la segmentación "X veces en Y días" (donde X<=50 e Y<=30)
- Resumen segmentable de eventos personalizados
  - Recuento de eventos (la suma de ambos perfiles)
  - Fecha en que ocurrió el suceso (Braze elegirá la fecha más temprana de las dos)
  - Última vez que ocurrió el suceso (Braze elegirá la fecha más tardía de las dos)
- Total de compras dentro de la aplicación en céntimos (la suma de ambos perfiles)
- Número total de compras (la suma de ambos perfiles)
- Fecha de la primera compra (Braze elegirá la fecha anterior de las dos)
- Fecha de la última compra (Braze elegirá la fecha más tardía de las dos)
- Resúmenes de la aplicación
- Campos Last_X_at (Braze actualizará los campos si los campos huérfanos del perfil son más recientes)
- Resúmenes de campaña (Braze elegirá los campos de fecha más recientes)
- Resúmenes del flujo de trabajo (Braze elegirá los campos de fecha más recientes)
- Historial de interacción de mensajes y mensajería

Cualquiera de los siguientes campos del usuario anónimo al usuario identificado:
- Evento personalizado y recuento de eventos de compra y marcas de tiempo de primera fecha y última fecha 
  - Estos campos fusionados actualizarán los filtros "para X eventos en Y días". Para los eventos de compra, estos filtros incluyen "número de compras en Y días" y "dinero gastado en los últimos Y días".

Los datos de la sesión solo se fusionarán si la aplicación existe en ambos perfiles de usuario. Por ejemplo, si nuestro usuario de destino no tiene un resumen de aplicación para "ABCApp" pero nuestro usuario original sí, el usuario de destino tendrá el resumen de aplicación "ABCApp" en su perfil después de la fusión. 

Si configuras el campo como `none`, no se fusionará ningún dato de usuario con el perfil de usuario identificado.

### Identificador de usuarios por correo electrónico
Si se especifica un `email` como identificador, se requiere un valor `prioritization` adicional en el identificador. `prioritization` debe ser una matriz que especifique qué usuario fusionar si se encuentran varios usuarios. `prioritization` es una matriz ordenada, lo que significa que si más de un usuario coincide a partir de una priorización, no se producirá la fusión.

Los valores permitidos para la matriz son: `identified`, `unidentified`, `most_recently_updated`. `most_recently_updated` se refiere a dar prioridad al usuario actualizado más recientemente.

En la matriz de priorización solo puede existir una de las siguientes opciones a la vez:
- `identified` se refiere a dar prioridad a un usuario con un `external_id`
- `unidentified` se refiere a dar prioridad a un usuario sin un `external_id`

## Ejemplo de solicitud
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/identify' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "aliases_to_identify": [
    {
      "external_id": "external_identifier",
      "user_alias": {
          "alias_name": "example_alias",
          "alias_label": "example_label"
      }
    }
  ],
  "emails_to_identify": [
    {
      "external_id": "external_identifier_2",
      "email": "john.smith@braze.com",
      "prioritization": ["unidentified", "most_recently_updated"]
    }
  ]
  "merge_behavior": "merge"
}'
```

{% alert tip %}
Para más información sobre `alias_name` y `alias_label`, consulta nuestra documentación [sobre alias de usuario]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases).
{% endalert %}

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
