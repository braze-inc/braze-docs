---
nav_title: "POST: Fusionar usuarios"
article_title: "POST: Fusionar usuarios"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Fusionar usuarios de Braze."

---
{% api %}
# Fusionar usuarios
{% apimethod post %}
/users/merge
{% endapimethod %}

> Utiliza este punto final para fusionar un usuario con otro usuario. 

Se pueden especificar hasta 50 fusiones por solicitud. Este punto final es asíncrono.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d262b86d-cf84-46e2-b9d0-f882bb7078de {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/api_key/) con el permiso `users.merge`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='users merge' %}

## Cuerpo de la solicitud

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "merge_updates" : (required, array of objects)
}
```

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `merge_updates` | Obligatoria | Matriz | Una matriz de objetos. Cada objeto debe contener un objeto `identifier_to_merge` y un objeto `identifier_to_keep`, cada uno de los cuales debe hacer referencia a un usuario mediante `external_id`, `user_alias`, `phone` o `email`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Comportamiento de la fusión

El comportamiento que se documenta a continuación es válido para todas las características de Braze que *no* funcionan con Snowflake. Las fusiones de usuarios no se reflejarán en la pestaña **Historial de mensajería**, Extensiones de segmento, Generador de consultas y Currents.

{% alert important %}
El punto final no garantiza la secuencia de actualización de los objetos de `merge_updates`.
{% endalert %}

Este punto final fusionará los siguientes campos si no se encuentran en el usuario de destino.

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
- Información del dispositivo
- Recuento de sesiones (la suma de las sesiones de ambos perfiles)
- Fecha de la primera sesión (Braze elegirá la fecha más temprana de las dos)
- Fecha de la última sesión (Braze elegirá la fecha más tardía de las dos)
- Atributos personalizados (los atributos personalizados existentes en el perfil de destino se conservan e incluirán atributos personalizados que no existían en el perfil de destino)
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
- Datos de interacción de la campaña (Braze elegirá los campos de fecha más recientes)
- Resúmenes del flujo de trabajo (Braze elegirá los campos de fecha más recientes)
- Historial de interacción de mensajes y mensajería
- Los datos de la sesión solo se fusionarán si la aplicación existe en ambos perfiles de usuario.

{% alert note %}
Al fusionar usuarios, el uso del punto final `/users/merge` funciona del mismo modo que el [método `changeUser()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser).
{% endalert %}

#### Comportamiento personalizado de la fecha del evento y de la fecha del evento de compra

Estos campos fusionados actualizarán los filtros "para X eventos en Y días". Para los eventos de compra, estos filtros incluyen "número de compras en Y días" y "dinero gastado en los últimos Y días".

### Fusionar usuarios por correo electrónico o número de teléfono

Si se especifica un `email` o `phone` como identificador, se requiere un valor `prioritization` adicional en el identificador. `prioritization` debe ser una matriz que especifique qué usuario fusionar si se encuentran varios usuarios. `prioritization` es una matriz ordenada, lo que significa que si más de un usuario coincide a partir de una priorización, no se producirá la fusión.

Los valores permitidos para la matriz son:

- `identified`
- `unidentified`
- `most_recently_updated` (se refiere a dar prioridad al usuario actualizado más recientemente)
- `least_recently_updated` (se refiere a dar prioridad al usuario que se haya actualizado menos recientemente)

En la matriz de priorización solo puede existir una de las siguientes opciones a la vez:

- `identified` se refiere a dar prioridad a un usuario con un `external_id`
- `unidentified` se refiere a dar prioridad a un usuario sin un `external_id`

## Ejemplos de solicitudes

### Petición básica

Se trata de un cuerpo de petición básico para mostrar el patrón de la petición.

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "external_id": "old-user1"
      },
      "identifier_to_keep": {
        "external_id": "current-user1"
      }
    },
    {
      "identifier_to_merge": {
        "email": "user1@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep":  {
        "email": "user2@braze.com",
        "prioritization": ["identified", "most_recently_updated"]
      }
    },
    {
      "identifier_to_merge": {
        "user_alias": {
          "alias_name": "old-user2@example.com",
          "alias_label": "email"
        }
      },
      "identifier_to_keep": {
        "user_alias": {
          "alias_name": "current-user2@example.com",
          "alias_label": "email"
        }
      }
    }
  ]
}'
```

### Fusionar usuario no identificado

La siguiente solicitud fusionaría el usuario no identificado actualizado más recientemente con dirección de correo electrónico "john.smith@braze.com" en el usuario con `external_id` "john". Si utilizas `most_recently_updated` o `least_recently_updated`, filtrarás la consulta a un solo usuario no identificado. Así, si hubiera dos usuarios no identificados con esta dirección de correo electrónico, solo uno se fusionaría en el usuario con `external_id` "john".

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep": {
        "external_id": "john"
      }
    }
  ]
}'
```

### Fusionar usuario no identificado en usuario identificado

El siguiente ejemplo fusiona el usuario no identificado actualizado más recientemente con la dirección de correo electrónico "john.smith@braze.com" en el usuario identificado actualizado más recientemente con la dirección de correo electrónico "john.smith@braze.com". Utilizar `most_recently_updated` o `least_recently_updated` filtra las consultas a un solo usuario (un usuario no identificado para `identifier_to_merge`, y un usuario identificado para `identifier_to_keep`).

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified", "most_recently_updated", "least_recently_updated"]
      },
      "identifier_to_keep": {
        "email": "john.smith@braze.com",
        "prioritization": ["identified", "most_recently_updated", "least_recently_updated"]
      }
    }
  ]
}'
```

### Fusionar un usuario no identificado sin incluir la priorización más_recientemente_actualizada

Si hay dos usuarios no identificados con la dirección de correo electrónico "john.smith@braze.com", este ejemplo de solicitud no fusiona a ningún usuario, ya que hay dos usuarios no identificados con esa dirección de correo electrónico. Esta solicitud solo funciona si solo hay un usuario no identificado con la dirección de correo electrónico "john.smith@braze.com".

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified"]
      },
      "identifier_to_keep": {
        "external_id": "john"
      }
    }
  ]
}'
```

## Respuesta

Hay dos respuestas de código de estado para este punto final: `202` y `400`.

### Ejemplo de respuesta satisfactoria

El código de estado `202` podría devolver el siguiente cuerpo de respuesta.

```json
{
  "message": "success"
}
```

### Ejemplo de respuesta de error

El código de estado `400` podría devolver el siguiente cuerpo de respuesta. Consulte la sección [Solución de problemas](#troubleshooting) para obtener más información sobre los errores que puede encontrar.

```json
{
  "message": "'merge_updates' must be an array of objects"
}
```

## Solución de problemas

En la tabla siguiente se enumeran los posibles mensajes de error que pueden aparecer.

| Error | Solución de problemas |
| --- |
| `'merge_updates' must be an array of objects` | Comprueba que `merge_updates` es una matriz de objetos. |
| `a single request may not contain more than 50 merge updates` | Solo puede especificar hasta 50 actualizaciones de fusión en una única solicitud. |
| `identifiers must be objects with an 'external_id' property that is a string, 'user_alias' property that is an object, 'email' property that is a string, or 'phone' property that is a string` | Comprueba los identificadores de tu solicitud. |
| `'merge_updates' must only have 'identifier_to_merge' and 'identifier_to_keep'` | Compruebe que `merge_updates` solo contiene los dos objetos `identifier_to_merge` y `identifier_to_keep`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
