---
nav_title: Directrices de documentación de puntos de conexión de API
article_title: Directrices de documentación de puntos de conexión de API
description: "Directrices para documentar los puntos de conexión de la API de Braze."
page_order: 3
noindex: true
---

# Directrices de documentación de puntos de conexión de API

<style>
.style-guide-table td {
  overflow-wrap: break-word;
  word-break: break-word;
  min-width: 0;
}
</style>

> En general, la documentación de los puntos de conexión de API debe seguir las directrices indicadas en las [Directrices generales]({{site.baseurl}}/contributing/style_guide/writing_style_guide/#general-guidelines). Sin embargo, hay temas específicos que pueden requerir directrices de contenido diferentes, las cuales se enumeran en este documento.

Braze admite los siguientes métodos de API REST:

* GET  
* DELETE  
* PATCH  
* POST  
* PUT

## Crear un nuevo artículo de punto de conexión

Al crear un nuevo artículo de punto de conexión, asegúrate de añadir también este punto de conexión en la [guía de la API de Braze]({{site.baseurl}}/api/home) para que sea localizable mediante búsqueda. Navega a la carpeta **`_docs`** **`> _api`** y al archivo **`> home.md`** para añadir el punto de conexión con su ruta y una descripción de una frase.

## Hacer referencia a puntos de conexión

En general, no existe una convención clara para referirse a los puntos de conexión en la documentación. Cuando hagas referencia a puntos de conexión de Braze, usa tu mejor criterio para determinar cómo referirte a un punto de conexión según tu caso de uso.

Puedes referirte a un punto de conexión por su ruta (por ejemplo, `/users/track`) o por el nombre del punto de conexión seguido de la palabra "endpoint" (por ejemplo, el endpoint track user). Si la ruta es especialmente larga, usa el nombre del punto de conexión en su lugar.

Usa estilo de oración cuando te refieras al punto de conexión por su nombre. Usa texto de código cuando te refieras al punto de conexión por su ruta.

No pongas en mayúsculas la palabra "endpoint" a menos que te refieras directamente al nombre de una sección. No incluyas la palabra "API" cuando hagas referencia directa a un punto de conexión.

Hay casos en los que un punto de conexión se denomina API. Por ejemplo, esta es una afirmación correcta: "Braze usa una API REST con muchos puntos de conexión" cuando se habla en general sobre los puntos de conexión de Braze.

No pongas comillas alrededor del nombre del punto de conexión. No uses texto sin formato cuando te refieras a la ruta.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Usa el endpoint Generate preference center URL para completar los siguientes pasos.</td><td style="width: 50%;">Usa <code>/preference_center/v1/{preferenceCenterExternalId}/url/{userId}</code> para completar los siguientes pasos.</td></tr>
<tr><td style="width: 50%;">Usa el endpoint <code>/users/track</code>.</td><td style="width: 50%;">Usa el endpoint de API "Users Track".</td></tr>
</tbody>
</table>
{:/}

### Enlazar a artículos de puntos de conexión

Cuando hagas referencia a artículos de puntos de conexión, asegúrate de usar [texto de enlace significativo]({{site.baseurl}}/contributing/style_guide/writing_style_guide/#writing-links) que tenga sentido fuera de contexto. Si usas la ruta del punto de conexión como enlace, asegúrate de proporcionar detalles en el texto circundante, ya que la ruta puede no comunicar claramente la función del punto de conexión.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Elimina perfiles de usuario usando el <a href="{{site.baseurl}}/api/endpoints/user_data/post_user_delete/">endpoint Delete user</a> de Braze.</td><td style="width: 50%;">Elimina perfiles de usuario usando el endpoint <a href="{{site.baseurl}}/api/endpoints/user_data/post_user_delete/">Delete user</a> de Braze.</td></tr>
<tr><td style="width: 50%;"><a href="{{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/">endpoint <code>/users/export/id</code></a></td><td style="width: 50%;"><a href="{{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/"><code>/users/export/id</code></a> endpoint</td></tr>
</tbody>
</table>
{:/}

## Encabezados

La introducción de un artículo de punto de conexión debe incluir la siguiente información:

* Tipo de solicitud y URL de la ruta del punto de conexión  
* Una breve descripción del punto de conexión, comenzando con "Usa este endpoint para…"  
* Enlace "See me in Postman"  
* Una alerta de nota con el permiso de clave de API REST requerido

Usa esta lista de verificación para asegurarte de que los encabezados (y el contenido) adecuados estén incluidos en cada artículo de punto de conexión y en el orden indicado. Ten en cuenta que puede haber subencabezados únicos para un punto de conexión, como diferentes tipos de solicitudes de ejemplo.

* Límite de velocidad  
* Parámetros de ruta  
* Cuerpo de la solicitud  
* Parámetros de solicitud  
* Solicitud de ejemplo  
* Parámetros de respuesta  
* Respuesta de ejemplo  
* Solución de problemas (si aplica)

Consulta [Encabezados y títulos]({{site.baseurl}}/contributing/style_guide/writing_style_guide/#headings-and-titles) para las directrices de formato.

### Parámetros de ruta

Si hay parámetros de ruta para el punto de conexión, incluye un encabezado de parámetros de ruta y una tabla (similar a la tabla de parámetros de solicitud).

Si no hay parámetros de ruta para el punto de conexión, incluye un encabezado de parámetros de ruta y el siguiente aviso: "There are no path parameters for this endpoint."

Si no hay parámetros de ruta ni de solicitud para el punto de conexión, combina la aclaración en la misma sección como se muestra a continuación.

{% raw %}
{::nomarkdown}
<div style="margin-left: 2em;">
<code>
## Path and request parameters <br>
There are no path or request parameters for this endpoint.
</code>
</div>
{:/}
{% endraw %}

## Convenciones de nomenclatura

Comienza cada nombre de punto de conexión con un verbo activo después de su método. Esto permite a los usuarios conocer la función del punto de conexión de inmediato.

No uses el método de API como verbo inicial para el nombre del punto de conexión.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">POST: Create new user alias</td><td style="width: 50%;">POST: New user alias</td></tr>
<tr><td style="width: 50%;">GET: Look up an existing dashboard user account</td><td style="width: 50%;">GET: Existing dashboard user account</td></tr>
</tbody>
</table>
{:/}

Las excepciones a esta convención de nomenclatura son los puntos de conexión en la [sección Export]({{site.baseurl}}/api/endpoints/export), ya que el nombre de la sección es un verbo que indica que la información listada puede exportarse.

## Permisos de clave de API

Los permisos de clave de API son permisos que puedes asignar a un usuario o grupo para limitar su acceso a ciertas llamadas de API. Para cada documentación de punto de conexión, incluye el siguiente aviso después del enlace de documentación de Postman:

> Para usar este endpoint, debes generar una clave de API con el permiso `permission_name_here`.

Para encontrar la lista completa de permisos de clave de API, ve a **Configuración > Claves de API** en **Configuración y pruebas** en el panel de Braze. Selecciona una clave de API con acceso completo (el nombre de la clave generalmente incluye la frase "full access"). Cada nombre de permiso debe coincidir generalmente con el nombre del punto de conexión.

Ten en cuenta que los puntos de conexión SCIM no tienen permisos de clave de API listados, ya que son específicos de la integración SCIM que ocurre fuera de la consola para desarrolladores.

## Límites de velocidad

En general, tu límite de velocidad debe especificar el número de solicitudes y el tiempo asignado.

Ten en cuenta los puntos de conexión que comparten un límite de velocidad total. Por ejemplo, todos los puntos de conexión asíncronos de elementos de Catálogo comparten un límite de velocidad total, por lo que es importante indicarlo en los artículos respectivos.

### Cómo actualizar el archivo de límites de velocidad

Si la documentación de tu punto de conexión requiere actualizar o listar un nuevo límite de velocidad, ve a **_docs > _api > api_limits.md** para realizar las ediciones del límite de velocidad.

## Parámetros

Define tanto los parámetros de solicitud como los de respuesta en dos tablas separadas. Estas tablas deben contener las siguientes columnas:

* **Parámetro**  
* **Obligatoria**  
* **Tipo de datos**  
* **Descripción**

Cuando te refieras directamente a los parámetros de un punto de conexión y al listar los valores en la columna **Parámetro**, usa texto de código. Al listar los valores en las columnas **Obligatoria**, **Tipo de datos** y **Descripción**, usa mayúscula inicial.

### Texto de marcador de posición

Para el texto de marcador de posición, usa llaves con una breve descripción de lo que el usuario debe incluir.

Para los marcadores de posición de clave de API, usa `YOUR_REST_API_KEY`, no `YOUR-REST-API-KEY`.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><code>/preference_center/v1/{preferenceCenterExternalId}/url/{userId}</code></td><td style="width: 50%;"><code>/preference_center/v1/[preferenceCenterExternalId]</code></td></tr>
<tr><td style="width: 50%;"><code>/scim/v2/Users/{userId}</code></td><td style="width: 50%;"><code>/url/[userId]/scim/v2/Users/userID</code></td></tr>
</tbody>
</table>
{:/}

Para los marcadores de posición de clave de API, usa `YOUR_REST_API_KEY` (con guiones bajos), no `YOUR-REST-API-KEY` (con guiones).

## Solicitudes y respuestas

Una solicitud de API incluye el encabezado y los parámetros de solicitud. Los parámetros de solicitud deben formatearse así:

```bash
parameter": (required/optional, data type) A brief description
```

Aquí tienes un ejemplo de cuerpo de solicitud para el [endpoint Create new user alias]({{site.baseurl}}/api/endpoints/user_data/post_user_alias/):

```bash
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "user_aliases": (required, array of new user alias object)
}
```

Usa comillas dobles rectas (" ") para identificar parámetros que son cadenas o arrays en una solicitud de ejemplo. Asegúrate de que todos los corchetes y paréntesis abiertos estén cerrados.

Una respuesta de API incluye el cuerpo de la respuesta, los encabezados y el código de estado HTTP. Incluye siempre una respuesta de ejemplo. Este ejemplo debe incluir un ejemplo de texto simple que describa el parámetro. Aquí tienes una respuesta de ejemplo para el [endpoint Update user alias]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/#example-request).

```bash
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

### Códigos de estado y error

Los códigos de estado indican si la solicitud específica de un usuario se ha completado correctamente. Puede ser útil incluir los códigos de estado para que los usuarios sepan qué se considera un éxito. Por ejemplo, 400 y 404 pueden ser indicadores de una respuesta de error para el punto de conexión.

Si la documentación de tu punto de conexión requiere listar códigos de error, enlaza al artículo [Errores y respuestas de API]({{site.baseurl}}/api/errors/) en la carpeta **_docs** **> _api** y el archivo **> errors.md**.

## Código de ejemplo

El código de ejemplo, como las solicitudes y respuestas de ejemplo, debe poder copiarse y usarse con un trabajo mínimo. Con la excepción del texto de marcador de posición (por ejemplo, la clave de API en el encabezado), las solicitudes de ejemplo deben funcionar tal cual. Usa Postman para asegurarte de que tu solicitud tenga el formato correcto.

### Código embellecido versus minificado

Si la solicitud del punto de conexión contiene un cuerpo, embellece el ejemplo en Postman. Esto facilita que los desarrolladores que están aprendiendo las convenciones de Braze comprendan cada parte de la solicitud.

Si el cuerpo de la solicitud del punto de conexión es muy corto o no contiene un cuerpo, minifica la solicitud para eliminar los espacios en blanco innecesarios. Usa una herramienta como [JSON Minifier](https://codebeautify.org/jsonminifier) para esto.

### Comentarios en línea

Usa dos barras diagonales (//) para indicar comentarios de una sola línea en el código de ejemplo.

Los comentarios en línea son herramientas valiosas para llamar la atención del usuario sobre una sección específica del código, explicar la función de un bloque de código o proporcionar contexto adicional.

Usa comentarios en línea para mostrar rápidamente dónde se colocaría la capa lógica del usuario y cómo haría referencia al código del SDK. Usa ejemplos simples pero realistas. Por ejemplo, un atributo de ejemplo como "favorite_movie" es más fuerte que "example_attribute". Aunque el negocio del usuario no rastree ni se preocupe por la película favorita de un usuario final, este ejemplo muestra los *tipos* de casos de uso que podrían rastrearse a través de este atributo. Los ejemplos genéricos no logran generar la misma comprensión intuitiva.

Evita los comentarios en línea que simplemente repitan código legible o nombres de métodos. En su lugar, usa una variedad de sinónimos para los métodos y parámetros específicos de Braze para proporcionar un andamiaje para hablantes no nativos de inglés.

En general, sigue las convenciones estándar del inglés al proporcionar comentarios en línea. Por ejemplo, comienza las oraciones con mayúscula, escribe las palabras completas, etc.

## Recursos adicionales

- [Guía de estilo de documentación para desarrolladores de Google](https://developers.google.com/style)  
  - [Código de referencia de API y comentarios](https://developers.google.com/style/api-reference-comments)