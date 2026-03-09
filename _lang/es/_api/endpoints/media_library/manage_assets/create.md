---
nav_title: "PUBLICAR: Subir un activo a la biblioteca multimedia"
article_title: "PUBLICAR: Subir un activo a la biblioteca multimedia"
search_tag: Punto de conexión
page_order: 1

layout: api_page
page_type: reference
description: "Este artículo describe los detalles sobre el punto final `POST /media_library/create`."
---

{% api %}
# Subir un activo a la biblioteca multimedia
{% apimethod post %}
/media_library/create
{% endapimethod %}

> Utiliza este punto final para añadir un activo a la [biblioteca multimedia de Braze](https://www.braze.com/docs/user_guide/engagement_tools/templates_and_media/media_library) utilizando una URL alojada externamente (`asset_url`) o datos de archivos binarios enviados en el cuerpo de la solicitud (`asset_file`). Este punto final admite imágenes y archivos ZIP que contienen imágenes.

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `media_library.create`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Cuerpo de la solicitud

Cuando incluyes `asset_url`, el punto final descarga el archivo desde la URL. Cuando incluyes `asset_file`, el punto final utiliza los datos binarios del cuerpo de la solicitud.

Ejemplo de cuerpo de solicitud para`asset_url`:

```json
{
  "asset_url": "https://cdn.example.com/assets/cat.jpg",
  "name": "Cat Graphic"
}
```

Ejemplo de cuerpo de solicitud para`asset_file`:

```json
{
  "asset_file": <BINARY FILE DATA>,
  "name": "Cat Graphic"
}
```

El cuerpo de la solicitud incluye los siguientes parámetros:

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | -------- | --------- | ----------- |
| `asset_url` | Opcional | Cadena | Una URL de acceso público para el activo que se va a cargar en Braze. |
| `asset_file` | Opcional | Binario | Datos de archivo binario. |
| `name` | Opcional | Cadena | Nombre que aparecerá en la biblioteca multimedia para este activo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert important %}
`asset_url` y`asset_file`  son mutuamente excluyentes, solo debes incluir uno de ellos en tu solicitud API.
{% endalert %}

### Nombres de los archivos subidos

En esta sección se explica cómo el punto final asigna nombres a los archivos cargados en función de si se incluye el`name`parámetro .

#### Subidas de archivos individuales

| Escenario | Resultado |
| --- | --- |
| `name` proporcionado | El`name`valor se utiliza como nombre del activo en la biblioteca multimedia. |
| `name` excluido | Se utiliza el nombre de archivo original de la URL o del archivo cargado. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" style="table-layout: fixed; width: 100%;" }

#### Carga de archivos ZIP

| Escenario | Resultado |
| --- | --- |
| `name` proporcionado | El`name`valor se utiliza como prefijo, con un número incremental añadido como sufijo (por ejemplo, «Mi archivo 1», «Mi archivo 2», «Mi archivo 3»). |
| `name` excluido | Cada archivo conserva su nombre original dentro del archivo ZIP. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" style="table-layout: fixed; width: 100%;" }

## Ejemplo de solicitud

Esta sección incluye dos ejemplos`curl`de solicitudes, una para añadir un activo utilizando una URL y otra utilizando datos de archivo binario.

Esta solicitud muestra un ejemplo de cómo añadir un activo a la biblioteca multimedia utilizando un `asset_url`.

```
curl -X POST --location 'https://rest.iad-01.braze.com/media_library/create' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_url": "https://cdn.example.com/assets/cat.jpg", "name": "Cat Graphic"}'
```

Esta solicitud muestra un ejemplo de cómo añadir un activo a la biblioteca multimedia utilizando un `asset_file`.

```
curl -X POST --location 'https://rest.iad-01.braze.com/media_library/create' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_file":<BINARY FILE DATA>, "name":"Cat Graphic"}'
```

### Respuestas de error

En esta sección se enumeran los posibles errores y sus correspondientes mensajes y descripciones. 

#### Errores de validación

Los errores de validación devuelven una estructura como esta:

```json
{
  "message": (String) Human-readable error description
}
```

Esta tabla enumera los posibles errores de validación.

| Estado HTTP | Mensaje | Descripción |
| --- | --- | --- |
| 400 | Se debe proporcionarasset_urlasset_file  o  . | No se ha proporcionado ningún parámetro de activo en la solicitud. |
| 400 | No se pueden asset_fileproporcionar niasset_url  ni . Por favor, proporciona solo uno. | Se proporcionaron ambos parámetros de activos; solo se permite uno. |
| 403 | «Las API públicas de la biblioteca multimedia no están habilitadas para esta empresa». | La característica de biblioteca multimedia no está habilitada para este espacio de trabajo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Errores de procesamiento

Los errores de procesamiento devuelven una respuesta diferente con códigos de error:

```json
{
  "message": (String) Human-readable error description,
  "error_code": (String) error code,
  "meta": { }
}
```

Esta tabla enumera los posibles errores de procesamiento.

| Código de error | Estado HTTP | Descripción |
| --- | --- | --- |
| `UNSUPPORTED_FILE_TYPE` | 400 | El tipo de archivo cargado no es compatible. El`meta`objeto incluye el`file_type`que fue rechazado. |
| `ASSET_SIZE_EXCEEDS_LIMIT` | 400 | El archivo supera el tamaño máximo permitido. Las imágenes tienen un límite de 5 MB. |
| `MEDIA_LIBRARY_LIMIT_REACHED` | 400 | El espacio de trabajo ha alcanzado su número máximo de activos (200 predeterminados para las empresas con versión de prueba gratuita, ilimitado en los demás casos). El`meta`objeto incluye el actual`limit`. |
| `ASSET_UPLOAD_FAILED` | 400 | El activo no se ha podido cargar debido a problemas de procesamiento. |
| `ZIP_UPLOAD_ERROR` | 400 | El archivo ZIP está dañado o no se puede abrir. El`meta`objeto incluye el`original_error`mensaje. |
| `ZIP_FILE_TOO_LARGE` | 400 | El tamaño total sin comprimir del archivo ZIP supera el límite de 5 MB. El`meta`objeto incluye el`zip_file_name`y `zip_file_size`el . |
| `ZIPPED_ENTITY_HAS_NO_NAME` | 400 | Una entrada de archivo dentro del ZIP no tiene nombre. Asegúrate de que el archivo ZIP no esté dañado y añade un nombre a cualquier entrada de archivo sin nombre. |
| `ZIPPED_ENTITY_CANNOT_HAVE_NESTED_DIRECTORY` | 400 | El archivo ZIP contiene directorios anidados, que no son compatibles. Todos los archivos deben estar en la raíz del ZIP. |
| `GENERIC_ERROR` | 500 | Se ha producido un error inesperado durante la carga. El`meta`objeto incluye el`original_error`mensaje para la depuración. Vuelve a intentarlo o ponte en contacto con [el servicio de asistencia]({{site.baseurl}}/support_contact/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


## Respuesta

Hay cinco respuestas de código de estado para este punto final: `200`, `400`,`403` `429`, y `500`.

El siguiente JSON muestra el formato esperado de la respuesta.

```json
{ 
    "new_assets": [
        {
            "name": (String) the name of the asset,
            "size": (Integer) the byte size of the asset,
            "url": (String) the URL to access the asset,
            "ext": (String) the file extension (e.g., "png", "jpg", "gif")
        }
    ],
    "errors": [
        {
            "name": (String) the name of the asset,
            "size": (Integer) the byte size of the asset,
            "ext": (String) the file extension (e.g., "png", "jpg", "gif"),
            "error": (String) the error that occurred
        }
    ],
    "dashboard_url": (String) the URL to view this asset in the Braze dashboard
}
```

{% endapi %}
