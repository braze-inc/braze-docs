---
nav_title: "Objeto de atributos del usuario"
article_title: Objeto API de atributos de usuario
page_order: 11
page_type: reference
description: "Este artículo de referencia explica los distintos componentes del objeto atributos de usuario."

---

# Objeto de atributos del usuario

> Una solicitud API con cualquier campo del objeto de atributos crea o actualiza un atributo con ese nombre y el valor indicado en el perfil de usuario especificado.

Utiliza los nombres de campo de perfil de usuario de Braze (enumerados a continuación o cualquiera de los enumerados en la sección de [campos de perfil de usuario de Braze](#braze-user-profile-fields)) para actualizar esos valores especiales en el perfil de usuario en el dashboard o añade tus propios datos de atributos personalizados al usuario.

## Cuerpo del objeto

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required
  "external_id" : (optional, string) see external user ID,
  "user_alias" : (optional, User alias object),
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  // Setting this flag to true puts the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" defaults to true.
  "_update_existing_only" : (optional, boolean),
  // See note regarding anonymous push token imports
  "push_token_import" : (optional, boolean),
  // Braze User Profile Fields
  "first_name" : "Jon",
  "email" : "bob@example.com",
  // Custom Attributes
  "my_custom_attribute" : value,
  "my_custom_attribute_2" : {"inc" : int_value},
  "my_array_custom_attribute":[ "Value1", "Value2" ],
  // Adding a new value to an array custom attribute
  "my_array_custom_attribute" : { "add" : ["Value3"] },
  // Removing a value from an array custom attribute
  "my_array_custom_attribute" : { "remove" : [ "Value1" ]},
}
```

- [ID externo de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)
- [Alias de usuario]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)

Para eliminar un atributo de perfil, ponlo en `null`. Algunos campos, como `external_id` y `user_alias`, no se pueden eliminar después de añadirlos al perfil de usuario.

#### Resolución de identificadores

A menos que estés realizando una [importación anónima de tokens de notificaciones push](#push-token-import), cada objeto de atributos de usuario debe incluir al menos un identificador: `external_id`, `user_alias`, `braze_id`, `email` o `phone`. Siempre que sea posible, incluye solo un identificador por objeto para evitar ambigüedades sobre qué perfil de usuario se está actualizando o creando.

Ten en cuenta lo siguiente al utilizar identificadores:

- **`external_id` y `user_alias` son mutuamente excluyentes.** Incluir ambos en el mismo objeto de atributos de usuario devuelve un error. Para añadir un alias a un usuario que ya tiene un `external_id`, utiliza el [punto de conexión `/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias/).
- **`email` tiene prioridad sobre `phone`.** Si tanto `email` como `phone` están incluidos en el mismo objeto, Braze utiliza `email` como identificador. Esto significa que los atributos se aplican al perfil de usuario asociado a esa dirección de correo electrónico, incluso si el número de teléfono pertenece a un perfil diferente.

{% alert important %}
Para evitar comportamientos inesperados, utiliza un único identificador por objeto de atributos de usuario. Proporcionar múltiples identificadores que hacen referencia a diferentes perfiles de usuario puede dar lugar a que los atributos se apliquen al perfil incorrecto.
{% endalert %}

#### Actualizar solo los perfiles existentes

Si deseas actualizar solo los perfiles de usuario existentes en Braze, debes pasar la clave `_update_existing_only` con el valor `true` en el cuerpo de la solicitud. Si se omite este valor, Braze crea un nuevo perfil de usuario si el `external_id` aún no existe.

{% alert note %}
Si estás creando un perfil de usuario solo con alias a través del punto de conexión `/users/track`, debes establecer `_update_existing_only` en `false`. Si omites este valor, Braze no creará el perfil solo con alias.
{% endalert %}

#### Importación de tokens de notificaciones push

Antes de importar tokens de notificaciones push a Braze, comprueba si es necesario. Cuando los SDK de Braze están implementados, gestionan los tokens de notificaciones push automáticamente sin necesidad de cargarlos a través de la API.

Si necesitas subirlos a través de la API, puedes hacerlo para usuarios identificados o para usuarios anónimos. Esto significa que, o bien debe estar presente un `external_id`, o bien los usuarios anónimos deben tener la marca `push_token_import` establecida en `true`.

{% alert note %}
Al importar tokens de notificaciones push de otros sistemas, no siempre se dispone de un `external_id`. Para mantener la comunicación con estos usuarios durante tu transición a Braze, puedes importar los tokens heredados para usuarios anónimos sin proporcionar `external_id` especificando `push_token_import` como `true`.
{% endalert %}

Al especificar `push_token_import` como `true`:

* `external_id` y `braze_id` **no** deben especificarse
* El objeto de atributos **debe** contener un token de notificaciones push
* Si el token ya existe en Braze, la solicitud se ignora; de lo contrario, Braze crea un perfil de usuario temporal y anónimo para cada token, lo que te permite seguir enviando mensajes a estas personas.

Después de la importación, cada vez que un usuario inicia la versión de tu aplicación habilitada para Braze, Braze traslada automáticamente su token de notificaciones push importado a su perfil de usuario de Braze y limpia el perfil temporal.

Braze comprueba una vez al mes si hay algún perfil anónimo con la marca `push_token_import` que no tenga un token de notificaciones push. Si el perfil anónimo ya no tiene un token de notificaciones push, Braze elimina el perfil. Sin embargo, si el perfil anónimo todavía tiene un token de notificaciones push, lo que sugiere que el usuario real aún no ha iniciado sesión en el dispositivo con dicho token de notificaciones push, Braze no hace nada.

Para más información, consulta [Migración de tokens de notificaciones push](#migrating-push-tokens).

#### Tipos de datos de atributos personalizados

Los siguientes tipos de datos pueden almacenarse como un atributo personalizado:

| Tipo de datos | Notas |
| --- | --- |
| Matrices | Se admiten matrices de atributos personalizados. Cuando añades un elemento, se añade al final de la matriz. Si el elemento ya existe, se mueve desde su posición actual hasta el final.<br><br>Solo se almacenan valores únicos. Por ejemplo, importar `['hotdog','hotdog','hotdog','pizza']` da como resultado `['hotdog', 'pizza']`.<br><br>Puedes establecer una matriz directamente (por ejemplo, `"my_array_custom_attribute":[ "Value1", "Value2" ]`), añadir a una matriz existente con `"my_array_custom_attribute" : { "add" : ["Value3"] }`, o eliminar valores con `"my_array_custom_attribute" : { "remove" : [ "Value1" ]}`.<br><br>La cantidad máxima de elementos predeterminada en una matriz es 500. Puedes actualizar la cantidad máxima de matrices en el panel de Braze, en **Configuración de datos** > **Atributos personalizados**. Para más información, consulta [Matrices]({{site.baseurl}}/developer_guide/analytics/#arrays). |
| Conjunto de objetos | Utiliza una matriz de objetos para definir una lista de objetos en la que cada objeto contenga un conjunto de atributos. Utiliza este tipo para almacenar varios conjuntos de datos relacionados con un usuario, como estancias en hoteles, historial de compras o preferencias. <br><br>Por ejemplo, define un atributo personalizado llamado `hotel_stays` en un perfil de usuario como una matriz en la que cada objeto representa una estancia independiente, con atributos como `hotel_name`, `check_in_date` y `nights_stayed`. Para obtener más información, consulta [el ejemplo de matriz de objetos](#array-of-objects-example). |
| Booleanos | `true` o `false` |
| Fechas | Deben almacenarse en formato [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) o en cualquiera de los siguientes formatos: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` <br><br>Ten en cuenta que la "T" es un indicador de tiempo, no un marcador de posición, y no debe cambiarse ni eliminarse. <br><br>Los atributos de tiempo sin zona horaria se establecen de forma predeterminada a medianoche UTC (y se formatean en el dashboard como el equivalente a medianoche UTC en la zona horaria de la empresa). Para especificar una zona horaria, añade un desplazamiento UTC a la marca de tiempo (por ejemplo, `2024-11-10T18:00:00-05:00` para EST). Si el desplazamiento de zona horaria falta o tiene un formato incorrecto, el valor se establece de forma predeterminada en UTC. <br><br>Las horas se muestran en el dashboard en la zona horaria de tu empresa. Por ejemplo, `2024-11-10T18:00:00-05:00` (6:00 PM EST) aparecería como la hora equivalente en la zona horaria configurada de tu empresa. <br><br>Los eventos con marcas de tiempo en el futuro se establecen de forma predeterminada en la hora actual. <br><br>Para los atributos personalizados habituales, si el año es inferior a 0 o superior a 3000, Braze almacena el valor como una cadena en el perfil de usuario. |
| Flotantes | Los atributos personalizados flotantes son números positivos o negativos con un punto decimal. Por ejemplo, puedes utilizar flotantes para almacenar saldos de cuentas o valoraciones de usuarios de productos o servicios. |
| Enteros | Puedes incrementar los atributos personalizados enteros asignando un objeto con el campo "inc" y la cantidad que deseas añadir. <br><br>Ejemplo: `"my_custom_attribute_2" : {"inc" : int_value},`|
| Atributos personalizados anidados | Los atributos personalizados anidados definen un conjunto de atributos como propiedad de otro atributo. Cuando defines un objeto de atributo personalizado, añades un conjunto de atributos a ese objeto. Para más información, consulta [Atributos personalizados anidados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/). |
| Cadenas | Los atributos personalizados de cadena son secuencias de caracteres que se utilizan para almacenar datos de texto. Por ejemplo, puedes utilizar cadenas para almacenar nombres y apellidos, direcciones de correo electrónico o preferencias. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Para obtener orientación sobre cuándo utilizar un evento personalizado frente a un atributo personalizado, consulta [Eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) y [Atributos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/).
{% endalert %}

##### Ejemplo de matriz de objetos

Esta matriz de objetos te permite crear segmentos basados en criterios específicos dentro de las estancias y personalizar tus mensajes utilizando los datos de cada estancia con plantillas Liquid.

```json
{"hotel_stays": [
  { "hotel_name": "Ocean View Resort", "check_in_date": "2023-06-15", "nights_stayed": 5 },
  { "hotel_name": "Mountain Lodge", "check_in_date": "2023-09-10", "nights_stayed": 3 }
]}
```

#### Campos de perfil de usuario de Braze {#braze-user-profile-fields}

{% alert important %}
Los siguientes campos del perfil de usuario distinguen entre mayúsculas y minúsculas, así que asegúrate de hacer referencia a ellos en minúsculas.
{% endalert %}

| Campo de perfil de usuario | Especificación del tipo de datos |
| ---| --- |
| alias_name | (cadena) |
| alias_label | (cadena) |
| braze_id | (cadena, opcional) Cuando el SDK reconoce un perfil de usuario, se crea un perfil de usuario anónimo con un `braze_id` asociado. El `braze_id` lo asigna Braze automáticamente, no se puede editar y es específico de cada dispositivo. |
| country | (cadena) Requerimos que los códigos de país se pasen a Braze en la [norma ISO-3166-1 alfa-2](http://en.wikipedia.org/wiki/ISO_3166-1). Nuestra API hace todo lo posible por mapear los países recibidos en diferentes formatos. Por ejemplo, "Australia" puede mapearse como "AU". Sin embargo, si la entrada no coincide con un [estándar ISO-3166-1 alfa-2](http://en.wikipedia.org/wiki/ISO_3166-1) determinado, el valor del país se establece en `NULL`. <br><br>La configuración de `country` en un usuario mediante la importación de CSV o la API impide que Braze capture automáticamente esta información a través del SDK. |
| current_location | (objeto) Con el formato {"longitude": -73.991443, "latitude": 40.753824} |
| date_of_first_session | (fecha en la que el usuario utilizó la aplicación por primera vez) Cadena en formato ISO 8601 o en cualquiera de los siguientes formatos: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| date_of_last_session | (fecha en la que el usuario utilizó la aplicación por última vez) Cadena en formato ISO 8601 o en cualquiera de los siguientes formatos: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY`  |
| dob | (fecha de nacimiento) Cadena en formato "AAAA-MM-DD", por ejemplo, 1980-12-21. |
| email | (cadena) |
| email_subscribe | (cadena) Los valores disponibles son "opted_in" (registrado explícitamente para recibir mensajes de correo electrónico), "unsubscribed" (excluido explícitamente de los mensajes de correo electrónico) y "subscribed" (ni incluido ni excluido).  |
| email_open_tracking_disabled |(booleano) `true` o `false` aceptados. Establécelo en `true` para desactivar que el píxel de seguimiento de apertura se añada a todos los futuros correos electrónicos enviados a este usuario. Disponible solo para SparkPost y SendGrid.|
| email_click_tracking_disabled |(booleano) `true` o `false` aceptados. Establécelo en `true` para desactivar el seguimiento de clics para todos los enlaces dentro de un futuro correo electrónico enviado a este usuario. Disponible solo para SparkPost y SendGrid.|
| external_id | (cadena) Un identificador único para un perfil de usuario. Después de asignar un `external_id`, Braze identifica el perfil de usuario en todos los dispositivos del usuario. La primera vez que se asigna un external_id a un perfil de usuario desconocido, Braze realiza la migración de todos los datos del perfil de usuario existentes al nuevo perfil de usuario. |
| facebook | hash que contiene cualquiera de `id` (cadena), `likes` (matriz de cadenas), `num_friends` (entero). |
| first_name | (cadena) |
| gender | (cadena) "M", "F", "O" (otro), "N" (no procede), "P" (prefiere no decirlo) o nil (desconocido). |
| home_city | (cadena) |
| language | (cadena) Requerimos que el idioma se pase a Braze en el [estándar ISO-639-1](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). Para conocer los idiomas admitidos, consulta nuestra [lista de idiomas aceptados]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/).<br><br>La configuración de `language` en un usuario mediante la importación de CSV o la API impide que Braze capture automáticamente esta información a través del SDK. |
| last_name | (cadena) |
| marked_email_as_spam_at | (cadena) Fecha en la que el correo electrónico del usuario fue marcado como correo no deseado. Aparece en formato ISO 8601 o en cualquiera de los siguientes formatos: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| phone | (cadena) Recomendamos proporcionar los números de teléfono en el formato [E.164](https://en.wikipedia.org/wiki/E.164). Para más detalles, consulta [Números de teléfono de usuario]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#formatting).|
| push_subscribe | (cadena) Los valores disponibles son "opted_in" (registrado explícitamente para recibir mensajes push), "unsubscribed" (excluido explícitamente de los mensajes push) y "subscribed" (ni incluido ni excluido).  |
| push_tokens | Matriz de objetos con `app_id` y cadena `token`. Opcionalmente, puedes proporcionar un `device_id` para el dispositivo al que está asociado este token, por ejemplo, `[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`. Si no se proporciona un `device_id`, se genera uno aleatoriamente. |
| subscription_groups| Matriz de objetos con una cadena `subscription_group_id` y `subscription_state`, por ejemplo, `[{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]`. Los valores disponibles para `subscription_state` son "subscribed" y "unsubscribed".|
| time_zone | (cadena) Nombre de la zona horaria de la [base de datos de zonas horarias de la IANA](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (por ejemplo, "America/New_York" o "Eastern Time (US & Canada)"). Solo se establecen valores de zona horaria válidos. |
| twitter | Hash que contiene cualquiera de `id` (entero), `screen_name` (cadena, identificador de X (antes Twitter)), `followers_count` (entero), `friends_count` (entero), `statuses_count` (entero). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Los valores de idioma que se establecen explícitamente a través de esta API tienen prioridad sobre la información de configuración regional que Braze recibe automáticamente del dispositivo.

####  Ejemplo de solicitud de atributo de usuario

Este ejemplo contiene cuatro objetos de atributos de usuario, de un total de 75 objetos de atributos permitidos por llamada a la API.

```http
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes" : [
    {
      "external_id" : "user1",
      "first_name" : "Jon",
      "has_profile_picture" : true,
      "dob": "1988-02-14",
      "music_videos_favorited" : { "add" : [ "calvinharris-summer" ], "remove" : ["nickiminaj-anaconda"] }
    },
    {
      "external_id" : "user2",
      "first_name" : "Jill",
      "has_profile_picture" : false,
      "push_tokens": [{"app_id": "Your App Identifier", "token": "abcd", "device_id": "optional_field_value"}]

    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "first_name" : "Alice",
      "has_profile_picture" : false
    },
    {
      "external_id": "user3",
      "subscription_groups" : [{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]
    }
  ]
}
```

## Migración de tokens de notificaciones push

Si enviabas notificaciones push antes de integrar Braze, por tu cuenta o a través de otro proveedor, la migración de tokens de notificaciones push te permite seguir enviando notificaciones push a tus usuarios con tokens de notificaciones push registrados.

### Migración automática a través del SDK

Después de [integrar el SDK de Braze]({{site.baseurl}}/developer_guide/sdk_integration/), los tokens de notificaciones push de los usuarios que hayan realizado la adhesión voluntaria se migran automáticamente la próxima vez que abran tu aplicación. Hasta entonces, no podrás enviar notificaciones push a esos usuarios a través de Braze.

Como alternativa, puedes [migrar tus tokens de notificaciones push manualmente](#manual-migration-via-api), lo que te permitirá reactivar la interacción con tus usuarios más rápidamente.

#### Consideraciones sobre los tokens web

Debido a la naturaleza de los tokens de notificaciones push web, asegúrate de tener en cuenta lo siguiente al implementar notificaciones push para web:

|Consideración|Detalles|
|----------------------|------------|
| **Prestadores de servicios**  | De forma predeterminada, el SDK Web busca un prestador de servicios en `./service-worker` a menos que se especifique otra opción, como `manageServiceWorkerExternally` o `serviceWorkerLocation`. Si tu prestador de servicios no está configurado correctamente, puede provocar que los tokens de notificaciones push de tus usuarios caduquen. |
| **Tokens caducados**   | Si un usuario no ha iniciado una sesión web en un plazo de 60 días, su token de notificaciones push caduca. Dado que Braze no puede migrar los tokens de notificaciones push caducados, debes enviar un [push primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages) para reactivar la interacción. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Migración manual a través de API

La migración manual de tokens de notificaciones push es el proceso de importar estas claves creadas previamente a tu plataforma Braze a través de la API.

Migra programáticamente los tokens de iOS (APN) y Android (FCM) a tu plataforma utilizando el [punto de conexión `users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Puedes migrar tanto usuarios identificados (usuarios con un ID externo asociado) como usuarios anónimos (usuarios sin ID externo).

Especifica el `app_id` de tu aplicación durante la migración del token de notificaciones push para asociar el token de notificaciones push adecuado con la aplicación apropiada. Cada aplicación (iOS, Android, etc.) tiene su propio `app_id`, que puedes encontrar en la sección **Identificación** de la página [Claves de API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/). Asegúrate de utilizar el `app_id` de la plataforma correcta.

{% alert important %}
No es posible migrar tokens de notificaciones push web a través de la API. Esto se debe a que los tokens de notificaciones push web no se ajustan al mismo esquema que otras plataformas.

<br>Si estás intentando migrar tokens de notificaciones push web mediante programación, es posible que aparezca un error como el siguiente: `Received '400: Invalid subscription auth' sending to 'https://fcm.googleapis.com/fcm/send`

<br>
Como alternativa a la migración de API, te recomendamos que integres el SDK y permitas que tu base de tokens se repoble de forma natural.
{% endalert %}

{% tabs local %}
{% tab External ID present %}
Para usuarios identificados, establece el indicador `push_token_import` en `false` (u omite el parámetro) y especifica los valores `external_id`, `app_id` y `token` en el objeto de usuario `attributes`.

Por ejemplo:

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes" : [
    {
      "push_token_import" : false,
      "external_id": "example_external_id",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING"}
      ]
    }
  ]
}'
```
{% endtab %}

{% tab External ID missing %}
Al importar tokens de notificaciones push de otros sistemas, no siempre se dispone de un `external_id`. En este caso, configura tu indicador `push_token_import` como `true` y especifica los valores `app_id` y `token`. Braze crea un perfil de usuario temporal y anónimo para cada token, lo que te permite seguir enviando mensajes a estas personas. Si el token ya existe en Braze, se ignora la solicitud.

Por ejemplo:

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes": [
    {
      "push_token_import" : true,
      "email": "braze.test1@testbraze.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}
      ]
    },

    {
      "push_token_import" : true,
      "email": "braze.test2@testbraze.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE_1": "YOUR_VALUE",
      "YOUR_CUSTOM_ATTRIBUTE_2": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}
      ]
    }
  ]
}'
```

Después de la importación, cuando el usuario anónimo inicia la versión de tu aplicación habilitada para Braze, Braze traslada automáticamente su token de notificaciones push importado a su perfil de usuario de Braze y limpia el perfil temporal.

Braze comprueba una vez al mes si hay algún perfil anónimo con la marca `push_token_import` que no tenga un token de notificaciones push. Si el perfil anónimo ya no tiene un token de notificaciones push, Braze elimina el perfil. Sin embargo, si el perfil anónimo sigue teniendo un token de notificaciones push, lo que sugiere que el usuario real aún no ha iniciado sesión en el dispositivo con dicho token de notificaciones push, Braze no hace nada.
{% endtab %}
{% endtabs %}

### Importar tokens de notificaciones push de Android

{% alert important %}
La siguiente consideración solo se aplica a las aplicaciones Android. Las aplicaciones iOS no requieren estos pasos porque esa plataforma solo tiene un marco para mostrar notificaciones push, y estas se muestran inmediatamente siempre que Braze tenga los tokens de notificaciones push y certificados necesarios.
{% endalert %}

Si debes enviar notificaciones push de Android a tus usuarios antes de que se complete la integración del SDK de Braze, utiliza pares clave-valor para validar las notificaciones push.

Debes tener un receptor para gestionar y mostrar cargas útiles push. Para notificar al receptor la carga útil push, añade los pares clave-valor necesarios a la campaña push. Los valores de estos pares dependen del socio de push específico que hayas utilizado antes de Braze.

{% alert note %}
Para algunos proveedores de notificaciones push, Braze necesita aplanar los pares clave-valor para que puedan interpretarse correctamente. Para aplanar los pares clave-valor de una aplicación Android específica, ponte en contacto con tu administrador del éxito del cliente.
{% endalert %}