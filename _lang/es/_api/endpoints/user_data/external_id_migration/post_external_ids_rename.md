---
nav_title: "POST: Renombrar ID externo"
article_title: "POST: Renombrar ID externo"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Renombrar ID externos."

---
{% api %}
# Renombrar ID externo
{% apimethod post %}
/users/external_ids/rename
{% endapimethod %}

> Utiliza este punto final para renombrar los ID externos de tus usuarios. 

Puedes enviar hasta 50 objetos de renombramiento por solicitud. 

Con este punto final se establece un nuevo (principal) `external_id` para el usuario y se elimina su `external_id` existente. Esto significa que el usuario puede ser identificado por cualquiera de los dos `external_id` hasta que se elimine el obsoleto. Tener varios ID externos permite un periodo de migración para que no se rompan las versiones anteriores de tus aplicaciones que utilicen el esquema de nomenclatura ID externo anterior. 

Cuando ya no utilices tu antiguo esquema de nombres, te recomendamos encarecidamente que elimines los ID externos obsoletos utilizando el [punto final`/users/external_ids/remove` ]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove).

{% alert warning %}
Asegúrate de eliminar los ID externos obsoletos con el punto final `/users/external_ids/remove` en lugar de `/users/delete`. Enviar una solicitud a `/users/delete` con el ID externo obsoleto elimina el perfil de usuario por completo y no se puede deshacer.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#17682d2b-1546-4a3c-9703-aa5a12861d7c {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/api_key/) con el permiso `users.external_ids.rename`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='external id migration' %}

## Cuerpo de la solicitud

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_id_renames" : (required, array of external ID rename objects)
}
```

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `external_id_renames` | Obligatoria | Matriz de identificadores externos renombrar objetos | Consulta el ejemplo de solicitud y las limitaciones siguientes para conocer la estructura del objeto renombrar identificador externo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Toma nota de lo siguiente:

- El `current_external_id` debe ser el ID principal del usuario, y no puede ser un ID obsoleto.
- El `new_external_id` no debe estar ya en uso ni como ID principal ni como ID obsoleto.
- El `current_external_id` y el `new_external_id` no pueden ser iguales.

## Ejemplo de solicitud
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/external_ids/rename' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_id_renames" :[
    {
      "current_external_id": "existing_external_id",
      "new_external_id" : "new_external_id"
    }
  ]
}'
```

## Respuesta

La respuesta confirmará todos los renombramientos realizados con éxito, así como los renombramientos fallidos con los errores asociados. Los mensajes de error en el campo `rename_errors` harán referencia al índice del objeto en la matriz de la solicitud original.

```
{
  "message" : (string) status message,
  "external_ids" : (array of strings) successful rename operations,
  "rename_errors": (array of arrays) <minor error message>
}
```

El campo `message` devolverá `success` para cualquier solicitud válida. Los errores más específicos se recogen en la matriz `rename_errors`. El campo `message` devuelve un error en caso de:

- Clave de API no válida
- Matriz vacía `external_id_renames` 
- `external_id_renames` matriz con más de 50 objetos
- Alcanzado el límite de velocidad (más de 1.000 solicitudes por minuto)

## Preguntas más frecuentes

### ¿Influye esto en los MAU?
No, ya que el número de usuarios seguirá siendo el mismo, sólo tendrán un nuevo `external_id`.

### ¿Cambia históricamente el comportamiento de los usuarios?
No, ya que el usuario sigue siendo el mismo, y todo su comportamiento histórico sigue vinculado a él.

### ¿Puede ejecutarse en espacios de trabajo de desarrollador o de puesta en escena?
Sí. De hecho, recomendamos encarecidamente realizar una migración de prueba en un espacio de trabajo de ensayo o de desarrollador, y asegurarse de que todo ha ido bien antes de ejecutarla en los datos de producción.

### ¿Consume puntos de datos?
Esta característica no cuesta puntos de datos.

### ¿Cuál es el periodo de amortización recomendado?
No tenemos un límite estricto sobre el tiempo que puedes mantener ID externos obsoletos, pero recomendamos encarecidamente eliminarlos cuando ya no sea necesario hacer referencia a los usuarios por el ID obsoleto.

{% endapi %}
