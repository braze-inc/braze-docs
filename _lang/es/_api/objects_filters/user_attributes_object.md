---
nav_title: "Objeto de atributos del usuario"
article_title: Objeto API de atributos de usuario
page_order: 11
page_type: reference
description: "Este artículo de referencia explica los distintos componentes del objeto atributos de usuario."

---

# Objeto de atributos del usuario

> Una petición a la API con cualquier campo del objeto atributos creará o actualizará un atributo de ese nombre con el valor dado en el perfil de usuario especificado. 

Utiliza los nombres de campo de perfil de usuario de Braze (enumerados a continuación o cualquiera de los enumerados en la sección de [campos de perfil de usuario de Braze][27]) para actualizar esos valores especiales en el perfil de usuario en el panel o añade tus propios datos de atributos personalizados al usuario.

## Cuerpo del objeto

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required
  "external_id" : (optional, string) see external user ID,
  "user_alias" : (optional, User alias object),
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  // Setting this flag to true will put the API in "Update Only" mode.
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

- [ID usuario externo]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)
- [Alias de usuario]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)

Para eliminar un atributo de perfil, ponlo en `null`. Algunos campos, como `external_id` y `user_alias` no se pueden eliminar después de añadirlos al perfil de usuario.

#### Actualizar solo los perfiles existentes

Si deseas actualizar solo los perfiles de usuario existentes en Braze, debes pasar la clave `_update_existing_only` con el valor `true` en el cuerpo de la solicitud. Si se omite este valor, Braze creará un nuevo perfil de usuario si `external_id` no existe ya.

{% alert note %}
Si está creando un perfil de usuario de solo alias a través del punto final `/users/track`, `_update_existing_only` debe establecerse en `false`. Si se omite este valor, no se creará el perfil de solo alias.
{% endalert %}

#### Importación de tokens de notificaciones push

Antes de importar tokens de notificaciones push a Braze, comprueba si es necesario. Cuando los SDK de Braze se ponen en marcha, gestionan los tokens de notificaciones push automáticamente sin necesidad de cargarlos a través de la API.

Si necesitas subirlos a través de la API, puedes hacerlo para usuarios identificados o para usuarios anónimos. Esto significa que, o bien se debe presentar un `external_id`, o bien los usuarios anónimos deben tener la bandera `push_token_import` establecida en `true`. 

{% alert note %}
Al importar tokens de notificaciones push de otros sistemas, no siempre se dispone de una dirección `external_id`. Para mantener la comunicación con estos usuarios durante tu transición a Braze, puedes importar los tokens heredados para usuarios anónimos sin proporcionar `external_id` especificando `push_token_import` como `true`.
{% endalert %}

Al especificar `push_token_import` como `true`:

* `external_id` y `braze_id` **no** deben especificarse
* El objeto atributo **debe** contener un token de notificaciones push
* Si el token ya existe en Braze, se ignora la solicitud; de lo contrario, Braze creará un perfil de usuario anónimo temporal para cada token para habilitarte a seguir enviando mensajes a estas personas.

Tras la importación, cuando cada usuario inicie la versión habilitada para Braze de tu aplicación, Braze moverá automáticamente su token de notificaciones push importado a su perfil de usuario Braze y limpiará el perfil temporal.

Braze comprobará una vez al mes si hay algún perfil anónimo con la bandera `push_token_import` que no tenga un token de notificaciones push. Si el perfil anónimo ya no tiene un token de notificaciones push, eliminaremos el perfil. Sin embargo, si el perfil anónimo aún tiene un token de notificaciones push, lo que sugiere que el usuario real aún no ha iniciado sesión en el dispositivo con dicho token, no haremos nada.

Para más información, consulta [Migración de tokens de notificaciones push][3].

#### Tipos de datos de atributos personalizados

Los siguientes tipos de datos pueden almacenarse como un atributo personalizado:

| Tipo de datos | Notas |
| --- | --- |
| Matrices | Se admiten matrices de atributos personalizadas. Añadir un elemento a una matriz de atributos personalizada añade el elemento al final de la matriz, a menos que ya esté presente, en cuyo caso se mueve desde su posición actual al final de la matriz.<br><br>Por ejemplo, si se importara una matriz `['hotdog','hotdog','hotdog','pizza']`, se mostraría en el atributo de matriz como `['hotdog', 'pizza']` porque sólo se admiten valores únicos.<br><br>Además de establecer los valores de una matriz diciendo algo como `"my_array_custom_attribute":[ "Value1", "Value2" ]`, puedes añadir a matrices existentes haciendo algo como `"my_array_custom_attribute" : { "add" : ["Value3"] },` o eliminar valores de una matriz haciendo algo como `"my_array_custom_attribute" : { "remove" : [ "Value1" ]}`<br><br>El número máximo de elementos en las matrices de atributos personalizadas es, por defecto, 25, pero puede aumentarse hasta 100 para una matriz individual. Para más información, ver [Matrices][6]. |
| Matriz de objetos | La matriz de objetos te permite definir una lista de objetos en la que cada objeto contiene un conjunto de atributos. Esto puede ser útil si necesitas almacenar varios conjuntos de datos relacionados de un usuario, como estancias en hoteles, historial de compras o preferencias. <br><br> Por ejemplo, puedes definir un atributo personalizado en un perfil de usuario llamado `hotel_stays`. Este atributo personalizado puede definirse como una matriz en la que cada objeto representa una estancia independiente, con atributos como `hotel_name`, `check_in_date`, `nights_stayed`. Para más detalles, consulta [este ejemplo](#array-of-objects-example). |
| Booleanos | `true` o `false` |
| Fechas | Debe almacenarse en el formato [ISO 8601][19] o en cualquiera de los siguientes formatos: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` <br><br>Ten en cuenta que la "T" es un indicador de tiempo, no un marcador de posición, y no debe cambiarse ni eliminarse. <br><br>Los atributos de tiempo sin zona horaria serán predeterminados a Medianoche UTC (y se formatearán en el panel como el equivalente a Medianoche UTC en la zona horaria de la empresa). <br><br> Los eventos con marcas de tiempo en el futuro serán predeterminados a la hora actual. <br><br> Para los atributos personalizados normales, si el año es menor que 0 o mayor que 3000, Braze almacena estos valores como cadenas en el usuario. |
| Flotantes | Los atributos personalizados flotantes son números positivos o negativos con un punto decimal. Por ejemplo, puedes utilizar flotadores para almacenar saldos de cuentas o tasas de usuarios de productos o servicios. |
| Enteros | Los atributos personalizados enteros pueden incrementarse con enteros positivos o negativos asignándoles un objeto con el campo "inc" y el valor por el que quieras incrementarlos. <br><br>Ejemplo: `"my_custom_attribute_2" : {"inc" : int_value},`|
| Atributos personalizados anidados | Los atributos personalizados anidados definen un conjunto de atributos como propiedad de otro atributo. Cuando defines un objeto atributo personalizado, defines un conjunto de atributos adicionales para ese objeto. Para más información, consulta [Atributos personalizados anidados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support). |
| Cadenas | Los atributos personalizados de cadena son secuencias de caracteres que se utilizan para almacenar datos de texto. Por ejemplo, puedes utilizar cadenas para almacenar nombres y apellidos, direcciones de correo electrónico o preferencias. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Para obtener información sobre cuándo debes utilizar un evento personalizado frente a un atributo personalizado, consulta nuestra documentación respectiva sobre [eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) y [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/).
{% endalert %}

##### Ejemplo de matriz de objetos 

Esta matriz de objetos te permite crear segmentos basados en criterios específicos dentro de las estancias, y personalizar tus mensajes utilizando los datos de cada estancia con plantillas Liquid.

```json
"hotel_stays": [
  { "hotel_name": "Ocean View Resort", "check_in_date": "2023-06-15", "nights_stayed": 5 },
  { "hotel_name": "Mountain Lodge", "check_in_date": "2023-09-10", "nights_stayed": 3 }
  ]
```

#### Braze campos de perfil de usuario {#braze-user-profile-fields}

{% alert important %}
Los siguientes campos del perfil de usuario distinguen entre mayúsculas y minúsculas, así que asegúrate de hacer referencia a ellos en minúsculas.
{% endalert %}

| Campo Perfil de usuario | Especificación del tipo de datos |
| ---| --- |
| alias_nombre | (cadena) |
| alias_label | (cadena) |
| braze_id | (cadena, opcional) Cuando el SDK reconoce un perfil de usuario, se crea un perfil de usuario anónimo con un `braze_id` asociado. La dirección `braze_id` la asigna Braze automáticamente, no se puede editar y es específica de cada dispositivo. | 
| country | (cadena) Requerimos que los códigos de país se pasen a Braze en la [norma ISO-3166-1 alfa-2][17]. Nuestra API hará todo lo posible por mapear los países recibidos en diferentes formatos. Por ejemplo, "Australia" puede mapearse como "AU". Sin embargo, si la entrada no coincide con un determinado [estándar ISO-3166-1 alfa-2][17], el valor del país se establecerá en `NULL`. <br><br>Configurar `country` en un usuario mediante importación en CSV o API impedirá que Braze capture automáticamente esta información a través del SDK. |
| current_location | (objeto) De la forma {"longitude": -73.991443, "latitude": 40.753824} |
| fecha_de_primera_sesión | (fecha en la que el usuario utilizó la aplicación por primera vez) Cadena en formato ISO 8601 o en cualquiera de los siguientes formatos: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| fecha_de_última_sesión | (fecha en la que el usuario utilizó la aplicación por última vez) Cadena en formato ISO 8601 o en cualquiera de los siguientes formatos: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY`  |
| dob | (fecha de nacimiento) Cadena en formato "AAAA-MM-DD", por ejemplo, 1980-12-21. |
| correo electrónico | (cadena) |
| email_subscribe | (cadena) Los valores disponibles son "opted_in" (registrado explícitamente para recibir mensajes de correo electrónico), "unsubscribed" (excluido explícitamente de los mensajes de correo electrónico) y "subscribed" (ni opted in ni out).  |
| email_open_tracking_disabled |(booleano) `true` o `false` aceptados. Establécelo en `true` para desactivar que el píxel de seguimiento de apertura se añada a todos los futuros correos electrónicos enviados a este usuario.|
| email_click_tracking_disabled |(booleano) `true` o `false` aceptados. Establécelo en `true` para desactivar el seguimiento de clics para todos los enlaces dentro de un futuro correo electrónico, enviado a este usuario.|
| external_id | (cadena) Un identificador único para un perfil de usuario. Una vez asignado un `external_id`, el perfil de usuario se identifica a través de los dispositivos de un usuario. En la primera instancia en que se asigne un identificador externo a un perfil de usuario desconocido, todos los datos existentes del perfil de usuario se migrarán al nuevo perfil de usuario. |
| Facebook | hash que contiene cualquiera de `id` (cadena), `likes` (matriz de cadenas), `num_friends` (entero). |
| first_name | (cadena) |
| gender | (cadena) "M", "F", "O" (otro), "N" (no procede), "P" (prefiere no decirlo) o nil (desconocido). |
| home_city | (cadena) |
| language | (cadena) requerimos que el lenguaje se pase a Braze en el [estándar ISO-639-1][24]. Para conocer los idiomas admitidos, consulta nuestra [lista de idiomas aceptados][2].<br><br>Configurar `language` en un usuario mediante importación en CSV o API impedirá que Braze capture automáticamente esta información a través del SDK. |
| last_name | (cadena) |
| marked_email_as_spam_at | (cadena) Fecha en la que el correo electrónico del usuario fue marcado como correo no deseado. Aparece en formato ISO 8601 o en cualquiera de los siguientes formatos: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| teléfono | (cadena) Recomendamos proporcionar los números de teléfono en el formato [E.164](https://en.wikipedia.org/wiki/E.164) formato. Para más detalles, consulta [Números de teléfono de usuario]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#formatting).|
| push_subscribe | (cadena) Los valores disponibles son "opted_in" (registrado explícitamente para recibir mensajes push), "unsubscribed" (excluido explícitamente de los mensajes push) y "subscribed" (ni opted in ni opted out).  |
| push_tokens | Matriz de objetos con `app_id` y cadena `token`. Opcionalmente, puedes proporcionar un `device_id` para el dispositivo al que está asociado este token, por ejemplo, `[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`. Si no se proporciona un `device_id`, se generará uno aleatoriamente. |
| subscription_groups| Matriz de objetos con una cadena `subscription_group_id` y `subscription_state`, por ejemplo, `[{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]`. Los valores disponibles para `subscription_state` son "subscribed" y "unsubscribed".|
| zona_horaria | (cadena) Del nombre de la zona horaria de [la base de datos de zonas horarias de IANA][26] (por ejemplo, "America/New_York" o "Eastern Time (US & Canada)"). Sólo se establecerán los valores de zona horaria válidos. |
| twitter | Hash que contiene `id` (entero), `screen_name` (cadena, X (antes Twitter) handle), `followers_count` (entero), `friends_count` (entero), `statuses_count` (entero). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Los valores de idioma que se establezcan explícitamente a través de esta API tendrán prioridad sobre la información de localización que Braze reciba automáticamente del dispositivo.

####  Ejemplo de solicitud de atributo de usuario

Este ejemplo contiene dos objetos de atributo de usuario con las 75 solicitudes permitidas por llamada a la API.

```json
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

[2]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/
[3]: {{site.baseurl}}/help/help_articles/push/push_token_migration/
[6]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays
[15]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/
[17]: http://en.wikipedia.org/wiki/ISO_3166-1 "Códigos ISO-3166-1"
[19]: http://en.wikipedia.org/wiki/ISO_8601 "Wiki de código de horario ISO 8601"
[24]: http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes "Códigos ISO-639-1"
[26]: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
[27]: #braze-user-profile-fields
