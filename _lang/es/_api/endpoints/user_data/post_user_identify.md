---
nav_title: "PUBLICAR: Identificar usuarios"
article_title: "PUBLICAR: Identificar usuarios"
search_tag: Punto de conexión
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

> Utiliza este punto final para identificar a un usuario no identificado (solo alias, solo correo electrónico o solo número de teléfono) utilizando el ID externo proporcionado.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f74e0f7-0620-4c7b-b0a2-f5f38fdbff58 {% endapiref %}

## Cómo funciona

La llamada`/users/identify`combina un perfil de usuario identificado por un alias (perfil solo con alias), una dirección de correo electrónico (perfil solo con correo electrónico) o un número de teléfono (perfil solo con número de teléfono) con un perfil de usuario que tiene un`external_id`identificador (perfil identificado) y, a continuación, elimina el perfil solo con alias.

Para identificar a un usuario es necesario incluir un`external_id`identificador en los siguientes objetos:

- `aliases_to_identify`
- `emails_to_identify`
- `phone_numbers_to_identify`

Si no hay ningún usuario con ese nombre`external_id`, el`external_id`  se añade al registro del usuario con asignación de alias y se considera que el usuario tiene un identificador. Los usuarios solo pueden tener un alias para una etiqueta específica. Si ya existe un usuario con el`external_id`  y tiene un alias existente con la misma etiqueta de alias que el perfil de solo alias, entonces los perfiles de usuario no se combinan.

{% alert tip %}
Para evitar la pérdida inesperada de datos al identificar a los usuarios, te recomendamos encarecidamente que primero consultes [las mejores prácticas de recopilación de datos]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/#capturing-user-data-when-alias-only-user-info-is-already-present) para saber cómo capturar datos de usuario cuando ya existe información de usuario sólo con alias.
{% endalert %}

### Comportamiento de fusión

De forma predeterminada, este punto final fusiona la siguiente lista de campos que se encuentran **exclusivamente** en el usuario anónimo con el usuario con identificador.

{% details List of fields that are merged %}
- Nombre
- Apellido
- Correo electrónico
- Género
- Fecha de nacimiento
- Número de teléfono
- Huso horario
- Ciudad de origen
- País
- Idioma
- Recuento de sesiones (la suma de las sesiones de ambos perfiles)
- Fecha de la primera sesión (Braze elige la fecha más temprana de las dos fechas)
- Fecha de la última sesión (Braze elige la fecha más reciente de las dos).
- Atributos personalizados
- Datos personalizados de eventos y compras
- Propiedades del evento personalizado y propiedades de la compra para la segmentación «X veces en Y días» (dondeX<=50  y Y<=30)
- Resumen segmentable de eventos personalizados
  - Recuento de eventos (la suma de ambos perfiles)
  - Primera vez que ocurrió el evento (Braze elige la fecha más temprana de las dos fechas)
  - Última vez que ocurrió el evento (Braze elige la fecha más reciente de las dos fechas)
- Total de compras dentro de la aplicación en céntimos (la suma de ambos perfiles)
- Número total de compras (la suma de ambos perfiles)
- Fecha de la primera compra (Braze selecciona la fecha más temprana de las dos fechas).
- Fecha de la última compra (Braze elige la fecha más reciente de las dos).
- Resúmenes de la aplicación
- Last_X_at campos (Braze actualiza los campos si los campos del perfil huérfano son más recientes)
- Resúmenes de campañas (Braze selecciona los campos de fecha más recientes)
- Resúmenes del flujo de trabajo (Braze selecciona los campos de fecha más recientes)
- Historial de interacción de mensajes y mensajería
- Evento personalizado y recuento de eventos de compra y marcas de tiempo de primera fecha y última fecha
  - Estos campos combinados actualizan los filtros «para X eventos en Y días». Para los eventos de compra, estos filtros incluyen "número de compras en Y días" y "dinero gastado en los últimos Y días".
- Datos de sesión si la aplicación existe en ambos perfiles de usuario
  - Por ejemplo, si nuestro usuario objetivo no tiene un resumen de la aplicación «ABCApp», pero nuestro usuario original sí, el usuario objetivo tendrá el resumen de la aplicación «ABCApp» en su perfil después de la fusión.
{% enddetails %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/api_key/) con el permiso `users.identify`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='users identify' %}

## Cuerpo de la solicitud

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
   "aliases_to_identify" : (required, array of alias to identify objects),
   "emails_to_identify": (optional, array of alias to identify objects) User emails to identify,
   "phone_numbers_to_identify": (optional, array of alias to identify objects) User phone numbers to identify,
},
```

### Parámetros de la solicitud

Puedes añadir hasta 50 alias de usuario por solicitud. Puedes asociar varios alias de usuario adicionales a un único `external_id`.

{% alert important %}
Se requiere uno de los siguientes elementos: `aliases_to_identify`, `emails_to_identify`, o`phone_numbers_to_identify`  por solicitud. Por ejemplo, puedes utilizar este punto final para identificar a los usuarios por correo electrónico utilizando`emails_to_identify`  en tu solicitud.
{% endalert %}

| Parámetro                   | Obligatoria | Tipo de datos                           | Descripción                                                                                                                                                                 |
|-----------------------------|----------|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `aliases_to_identify`       | Obligatoria | Conjunto de alias para identificar objetos | Ver [alias para identificar objeto]({{site.baseurl}}/api/objects_filters/aliases_to_identify/) y [alias de usuario objeto]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
| `emails_to_identify`        | Obligatoria | Conjunto de alias para identificar objetos | Requerido si`email`  se especifica como identificador. Direcciones de correo electrónico como identificadores de usuarios. Ver [Identificador de usuarios por correo electrónico](#identifying-users-by-email).                                                                                                              |
| `phone_numbers_to_identify` | Obligatoria | Conjunto de alias para identificar objetos | Números de teléfono como identificadores de usuarios.                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Identificación de usuarios mediante direcciones de correo electrónico y números de teléfono

Si se especifica una dirección de correo electrónico o un número de teléfono como identificador, también debes incluir`prioritization`  en el identificador.

Debe ser `prioritization`una matriz que especifique qué usuario fusionar si se encuentran varios usuarios.`prioritization`Es una matriz ordenada, lo que significa que si más de un usuario coincide con una priorización, no se produce la fusión.

Los valores permitidos para la matriz son:

- `identified`
- `unidentified`
- `most_recently_updated` (se refiere a dar prioridad al usuario actualizado más recientemente)
- `least_recently_updated` (se refiere a dar prioridad al usuario que menos recientemente ha actualizado su información)

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
}'
```

{% alert tip %}
Para más información sobre `alias_name` y `alias_label`, consulta nuestra documentación [sobre alias de usuario]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases).
{% endalert %}

## Respuesta

```json
{
    "aliases_processed": 1,
    "message": "success"
}
```

{% endapi %}
