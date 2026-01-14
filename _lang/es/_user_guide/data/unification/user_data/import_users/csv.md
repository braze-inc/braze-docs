---
nav_title: Utilizar un CSV
article_title: "Importación CSV"
description: "Aprende a registrar y actualizar atributos de usuario y eventos personalizados mediante la importación de CSV."
page_order: 1.2
---

# Importación CSV

> Aprende a registrar y actualizar atributos de usuario y eventos personalizados mediante la importación de CSV.

## Acerca de la importación CSV

Puedes utilizar la importación en CSV para registrar y actualizar los siguientes atributos de usuario y eventos personalizados.

|Tipo|Definición|Ejemplo|Tamaño máximo del archivo|
|---|---|---|---|
|Atributos predeterminados|Atributos de usuario reservados reconocidos por Braze.|`first_name`, `email`|500 MB|
|Atributos personalizados|Atributos de usuario únicos para tu empresa.|`last_destination_searched`|500 MB|
|Eventos personalizados|Eventos únicos de tu empresa que representan acciones de los usuarios.|`trip_booked`|50 MB|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

## Utilizar la importación CSV

### Paso 1: Descargar una plantilla CSV

Para abrir la importación en CSV, ve a **Audiencias** > Importar usuarios. Aquí encontrarás una tabla con detalles sobre las importaciones más recientes, como la fecha de carga, el nombre del cargador, el nombre del archivo, la disponibilidad de destino, el número de filas importadas y el estado de la importación.

Para empezar con tu CSV, descarga una plantilla para atributos o eventos.

Página "Importar usuarios" del panel de Braze.]({% image_buster /assets/img/csv_import/import_users_page.png %})

### Paso 2: Elige un identificador {#choose-an-identifier}

El CSV que importes necesitará un identificador específico. Puedes elegir entre lo siguiente:

{% tabs local %}
<!-- TAB -->
{% tab external id %}
Al importar tus datos de clientes, puedes utilizar un `external_id` para que sirva como identificador único de cada cliente. Cuando proporciones un `external_id` en tu importación, Braze actualizará cualquier usuario existente con el mismo `external_id` o creará un nuevo usuario identificado con ese `external_id` establecido si no se encuentra ninguno.

- Descárgatelo: [Plantilla de importación de atributos CSV: ID externo]({{site.baseurl}}/assets/download_file/braze-user-import-template-csv.xlsx?3aafd0c03634ac03f248b3055fbc3126)
- Descárgatelo: [Plantilla de importación de eventos CSV: ID externo](https://braze.com/unlisted_docs/assets/download_file/braze-csv-events-import-template.csv?3b64ea284baa9a21cfe0a7ab4b46fce4)

{% alert note %}
Si estás subiendo una mezcla de usuarios con un `external_id` y usuarios sin él, tienes que crear un CSV para cada importación. Un CSV no puede contener tanto `external_ids` como alias de usuario.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab user alias %}
Para dirigirte a usuarios que no tienen un `external_id`, puedes importar una lista de usuarios con alias de usuario. Un alias sirve como identificador de usuario único alternativo, y puede ser útil si estás intentando comercializar con usuarios anónimos que no se han registrado o creado una cuenta en tu aplicación.

Si estás cargando o actualizando perfiles de usuario que son sólo alias, debes tener las dos columnas siguientes en tu CSV:

- `user_alias_name`: Un identificador único de usuario; una alternativa al `external_id`  
- `user_alias_label`: Una etiqueta común para agrupar los alias de usuario

| `user_alias_name` | `user_alias_label` | `last_name` | `email` | sample_attribute |
| :---- | :---- | :---- | :---- | :---- |
| 182736485 | my_alt_identifier | Smith | smith@user.com | VERDADERO |
| 182736486 | my_alt_identifier | Nguyen | nguyen@user.com | FALSO |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation"}

Cuando proporciones tanto un `user_alias_name` como un `user_alias_label` en tu importación, Braze actualizará cualquier usuario existente con el mismo `user_alias_name` y `user_alias_label`. Si no se encuentra un usuario, Braze creará un usuario recién identificado con esa configuración `user_alias_name`.

{% alert important %}
No puedes utilizar una importación en CSV para actualizar un usuario existente con un `user_alias_name` si ya tiene un `external_id`. En su lugar, se creará un nuevo perfil de usuario con la dirección `user_alias_name` asociada. Para asociar un usuario de sólo alias a un `external_id`, utiliza el [punto final Identificar usuarios]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/).
{% endalert %}

Descárgatelo: [Plantilla de importación de atributos CSV: Alias de usuario]({{site.baseurl}}/assets/download_file/braze-user-import-alias-template-csv.xlsx?c0ce6c0aa1e901395161d87c5ba17747)
{% endtab %}

<!-- TAB -->
{% tab braze id %}
Para actualizar perfiles de usuario existentes en Braze utilizando un valor interno de ID de Braze en lugar de un valor de `external_id` o `user_alias_name` y `user_alias_label`, especifica `braze_id` como cabecera de columna.

Esto puede ser útil si has exportado datos de usuario desde Braze a través de nuestra opción de exportación CSV dentro de la segmentación y quieres añadir un nuevo atributo personalizado a esos usuarios existentes.

{% alert important %}
No puedes utilizar una importación en CSV para crear un nuevo usuario utilizando `braze_id`. Este método sólo puede utilizarse para actualizar usuarios preexistentes dentro de la plataforma Braze.  
{% endalert %}

{% alert tip %}
El valor `braze_id` podría etiquetarse como `Appboy ID` en las exportaciones CSV desde el panel de Braze. Este ID será el mismo que el de `braze_id` para un usuario, así que puedes cambiar el nombre de esta columna a `braze_id` cuando vuelvas a importar el CSV.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab email address and phone numbers %}
Puedes omitir un ID externo o un alias de usuario y utilizar una dirección de correo electrónico o un número de teléfono para importar usuarios. Antes de importar un archivo CSV con direcciones de correo electrónico o números de teléfono, comprueba lo siguiente:

- Comprueba que no tienes ID externos ni alias de usuario para estos perfiles en tu archivo CSV. Si lo haces, Braze dará prioridad al uso del ID externo o alias de usuario antes que a la dirección de correo electrónico para identificar perfiles.  
- Confirma que tu archivo CSV tiene el formato adecuado.  

{% alert note %}
Si incluyes tanto direcciones de correo electrónico como números de teléfono en tu archivo CSV, la dirección de correo electrónico tendrá prioridad sobre el número de teléfono a la hora de buscar perfiles.
{% endalert %}

Si un perfil existente tiene esa dirección de correo electrónico o número de teléfono, ese perfil se actualizará, y Braze no creará un perfil nuevo. Si hay varios perfiles con esa misma dirección de correo electrónico, Braze utilizará la misma lógica que el [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), donde se actualizará el perfil actualizado más recientemente.

Si no existe un perfil con esa dirección de correo electrónico o número de teléfono, Braze creará un nuevo perfil con ese identificador. Puedes utilizar el [punto final`/users/identify` ]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) para identificar este perfil más adelante. Para eliminar un perfil de usuario, también puedes utilizar el punto final [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) punto final.
{% endtab %}
{% endtabs %}

### Paso 3: Crea tu archivo CSV

Puedes cargar cualquiera de los siguientes tipos de datos como un único archivo CSV. Para subir más de un tipo de datos, sube varios archivos CSV.

- **Atributos del usuario:** Esto incluye atributos de usuario predeterminados y personalizados. Los atributos predeterminados de usuario son claves reservadas en Braze (como `first_name` o `email`) y los atributos personalizados son atributos de usuario únicos para tu empresa (como `last_destination_searched`).  
- **Eventos personalizados:** Son únicos para tu empresa y reflejan las acciones que ha realizado un usuario, como `trip_booked` para una aplicación de reserva de viajes.

Cuando estés listo para empezar a crear tu archivo CSV, consulta la siguiente información:

{% tabs local %}
<!-- TAB -->
{% tab user attributes %}
#### Identificadores obligatorios {#required-identifiers-attributes}

Aunque `external_id` no es obligatorio, **debes** incluir **uno** de los siguientes identificadores como cabecera en tu archivo CSV. Para más detalles sobre cada uno de ellos, revisa [Elige un identificador](#choose-an-identifier).

- `external_id`
- `braze_id`
- `user_alias_name` **y** `user_alias_label`
- `email`
- `phone`

#### Atributos personalizados

Los siguientes tipos de datos pueden utilizarse como atributos personalizados para la importación de CSV. Los encabezados de columna que no coincidan exactamente con un [atributo predeterminado](#default-attributes) recibirán un atributo personalizado en Braze.

| Tipo de datos | Descripción |
|---|---|
| Fecha y hora | Debe almacenarse en formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601). |
| Booleano | Acepta `true` o `false`. |
| Número | Debe ser un número entero o flotante sin espacios ni comas. Los flotantes deben utilizar un punto (`.`) como separador decimal. |
| Cadena | Puede contener comas si el valor va entre comillas dobles (`""`). |
| En blanco | Los valores en blanco no sobrescribirán los valores existentes en el perfil de usuario, y no es necesario que incluyas todos los atributos de usuario existentes en tu archivo CSV. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
Las matrices, los tokens de notificaciones push y los tipos de datos de eventos personalizados no son compatibles con la importación de usuarios, ya que las comas de tu archivo CSV se interpretarán como un separador de columnas y provocarán errores al analizar tu archivo.<br><br>Para cargar este tipo de valores, utiliza en su lugar el [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) o [la Ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/cloud_ingestion/).
{% endalert %} 

#### Atributos predeterminados

{% alert important %}
Al importar atributos predeterminados, las cabeceras de columna que utilices deben coincidir exactamente con la ortografía y las mayúsculas de los atributos predeterminados de usuario. De lo contrario, Braze los detectará como [atributos personalizados](#custom-attributes).
{% endalert %}

| Campo Perfil de usuario | Tipo de datos | Descripción | ¿Es necesario? |
| :---- | :---- | :---- | :---- |
| `external_id` | Cadena | Un identificador de usuario único para tu cliente. | Condicionalmente. Ver [Identificadores obligatorios](#required-identifiers-attributes). |
| `user_alias_name` | Cadena | Un identificador único de usuario para usuarios anónimos que es una alternativa a `external_id`. Debe utilizarse con `user_alias_label`. | Condicionalmente. Ver [Identificadores obligatorios](#required-identifiers-attributes). |
| `user_alias_label` | Cadena | Una etiqueta común para agrupar los alias de usuario. Debe utilizarse con `user_alias_name`. | Condicionalmente. Ver [Identificadores obligatorios](#required-identifiers-attributes). |
| `first_name` | Cadena | El nombre de pila de tus usuarios tal y como ellos lo han indicado (por ejemplo, `Jane`). | No |
| `last_name` | Cadena | El apellido de tus usuarios tal y como ellos lo han indicado (por ejemplo, `Doe`). | No |
| `email` | Cadena | El correo electrónico de tus usuarios tal y como ellos lo han indicado (por ejemplo, `jane.doe@braze.com`). | No |
| `country` | Cadena | Los códigos de país deben pasarse a Braze en la norma ISO-3166-1 alfa-2 (por ejemplo, `GB`). | No |
| `dob` | Cadena | Debe pasarse en el formato "AAAA-MM-DD" (por ejemplo, `1980-12-21`). Esto importará la fecha de nacimiento de tu usuario y te habilitará para dirigirte a usuarios cuya fecha de cumpleaños sea "hoy". | No |
| `gender` | Cadena | "M", "F", "O" (otro), "N" (no aplicable), "P" (prefiero no decirlo) o nulo (desconocido). | No |
| `home_city` | Cadena | La ciudad de residencia de tus usuarios tal y como ellos la han indicado (por ejemplo, `London`). | No |
| `language` | Cadena | El idioma debe pasarse a Braze en la norma ISO-639-1 (por ejemplo, `en`). Consulta nuestra [lista de lenguas aceptadas]({{site.baseurl}}/user_guide/data/user_data_collection/language_codes/). | No |
| `phone` | Cadena | Un número de teléfono indicado por tus usuarios, en formato `E.164` (por ejemplo, `+442071838750`). Consulta [Números de teléfono de usuario]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/) para ver cómo formatearlos. | No |
| `email_open_tracking_disabled` | Booleano | verdadero o falso aceptado. Establécelo como verdadero para desactivar que el píxel de seguimiento de apertura se añada a todos los futuros correos electrónicos enviados a este usuario. Disponible sólo para SparkPost y SendGrid. | No |
| `email_click_tracking_disabled` | Booleano | verdadero o falso aceptado. Establécelo como verdadero para desactivar el seguimiento de clics de todos los enlaces dentro de un futuro correo electrónico, enviado a este usuario. Disponible sólo para SparkPost y SendGrid. | No |
| `email_subscribe` | Cadena | Los valores disponibles son `opted_in` (se ha registrado explícitamente para recibir mensajes de correo electrónico), `unsubscribed` (se ha excluido explícitamente de recibir mensajes de correo electrónico) y `subscribed` (ni se ha registrado ni se ha excluido). | No |
| `push_subscribe` | Cadena | Los valores disponibles son `opted_in` (se ha registrado explícitamente para recibir mensajes push), `unsubscribed` (se ha excluido explícitamente de los mensajes push) y `subscribed` (ni se ha aceptado ni se ha excluido). | No |
| `time_zone` | Cadena | La zona horaria debe pasarse a Braze en el mismo formato que la base de datos de zonas horarias de IANA (por ejemplo, `America/New_York` o `Eastern Time (US & Canada)`). | No |
| `date_of_first_session`  `date_of_last_session` | Cadena | Puede pasarse en uno de los siguientes formatos ISO 8601: "AAAA-MM-DD" "AAAA-MM-DDTHH:MM:SS+00:00" "AAAA-MM-DDTHH:MM:SSZ" "AAAA-MM-DDTHH:MM:SS" (por ejemplo, 2019-11-20T18:38:57) | No |
| `subscription_group_id` | Cadena | La dirección `id` de tu grupo de suscripción. Este identificador se encuentra en la página del grupo de suscripción de tu panel. | No |
| `subscription_state` | Cadena | El estado de suscripción para el grupo de suscripción especificado por `subscription_group_id`. Los valores permitidos son `unsubscribed` (no en el grupo de suscripción) o `subscribed` (en el grupo de suscripción). | No, pero se recomienda encarecidamente si se utiliza `subscription_group_id`  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

#### Actualización del estado del grupo de suscripción (opcional)

Además, puedes añadir usuarios a grupos de suscripción por correo electrónico o SMS mediante la importación de usuarios. Esto es especialmente útil para los SMS, porque un usuario debe estar inscrito en un grupo de suscripción SMS para recibir mensajes con el canal SMS. Para más información, consulta [Grupos de suscripción SMS](https://www.braze.com/docs/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement).

Si estás actualizando estados del grupo de suscripción, debes tener las dos columnas siguientes en tu CSV:

- `subscription_group_id`: La dirección `id` del [grupo de suscripción](https://www.braze.com/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups).  
- `subscription_state`: Los valores disponibles son `unsubscribed` (no está en el grupo de suscripción) o `subscribed` (está en el grupo de suscripción).

| external_id | first_name | subscription_group_id | subscription_state |
| :---- | :---- | :---- | :---- |
| A8i3mkd99 | Colby | 6ff593d7-cf69-448b-aca9-abf7d7b8c273 | suscrito |
| k2LNhj8Ks | Tom | aea02307-a91e-4bc0-abad-1c0bee817dfa | suscrito |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

{% alert note %}
Sólo se puede configurar un único `subscription_group_id` por fila en la importación de usuarios. Diferentes filas pueden tener diferentes valores `subscription_group_id`. Sin embargo, si necesitas inscribir a los mismos usuarios en varios grupos de suscripción, tendrás que hacer varias importaciones.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab custom events %}
#### Identificadores obligatorios {#required-identifiers-custom-events}

Aunque `external_id` no es obligatorio, **debes** incluir **uno** de los siguientes identificadores como cabecera en tu archivo CSV. Para más detalles sobre cada uno de ellos, revisa [Elige un identificador](#choose-an-identifier).

- `external_id`
- `braze_id`
- `user_alias_name` **y** `user_alias_label`
- `email`
- `phone`

#### Campos de evento personalizados

Además de lo siguiente, tu CSV también puede contener cabeceras de columna adicionales para las propiedades del evento. Estas propiedades deben tener una cabecera de columna de `<event_name>.properties.<property name>.`

Por ejemplo, el evento personalizado `trip_booked` puede tener las propiedades `destination` y `duration`. Se pueden importar con las cabeceras de columna `trip_booked.properties.destination` y `trip_booked.properties.duration`.

| Campo Perfil de usuario | Tipo de datos | Información | ¿Es necesario? |
| :---- | :---- | :---- | :---- |
| `external_id` | Cadena | Un identificador único para tu usuario. | Condicionalmente. Ver [Identificadores obligatorios](#required-identifiers-custom-events). |
| `braze_id` | Cadena | Un identificador Braze asignado a tu usuario. | Condicionalmente. Ver [Identificadores obligatorios](#required-identifiers-custom-events). |
| `user_alias_name` | Cadena | Un identificador único de usuario para usuarios anónimos, que es una alternativa a `external_id`. Debe utilizarse con `user_alias_label`. | Condicionalmente. Ver [Identificadores obligatorios](#required-identifiers-custom-events). |
| `user_alias_label` | Cadena | Una etiqueta común para agrupar los alias de usuario. Debe utilizarse con `user_alias_name`. | Condicionalmente. Ver [Identificadores obligatorios](#required-identifiers-custom-events). |
| `email` | Cadena | El correo electrónico de tus usuarios tal y como ellos lo han indicado (por ejemplo, `jane.doe@braze.com`). | No, y sólo puede utilizarse en ausencia de otros identificadores. Véase la nota siguiente. |
| `phone` | Cadena | Un número de teléfono indicado por tus usuarios, en formato `E.164` (por ejemplo, `+442071838750`). Consulta [Números de teléfono de usuario]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/) para ver cómo formatearlos. | No, y sólo puede utilizarse en ausencia de otros identificadores. Véase la nota siguiente. |
| `name` | Cadena | Un evento personalizado de tus usuarios. | Sí |
| `time` | Cadena | La hora del acontecimiento. Puede pasarse en uno de los siguientes formatos ISO-8601: "AAAA-MM-DD" "AAAA-MM-DDTHH:MM:SS+00:00" "AAAA-MM-DDTHH:MM:SSZ" "AAAA-MM-DDTHH:MM:SS" (por ejemplo, 2019-11-20T18:38:57) | Sí |
| `<event name>.properties.<property name>` | Múltiple | Una propiedad de evento asociada a un evento personalizado. Un ejemplo es `trip_booked.properties.destination` | No |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}
{% endtab %}
{% endtabs %}

### Paso 4: Carga y vista previa de tus datos

Antes de que Braze procese tu CSV, generará una vista previa de las primeras filas para que puedas comprobar si hay algún problema. Para generar tu vista previa, elige **Atributos** o **Eventos**, luego selecciona **Examinar archivos** y carga tu CSV. 

<!-- old image -->
Se ha completado la carga de CSV con errores relacionados con tipos de datos mixtos en una sola columna]({% image_buster /assets/img/csv_import/upload_csv.png %}){: style="max-width:70%"}

{% alert important %}
La vista previa de importación de usuarios no escanea todas las filas del archivo de entrada. Es posible que no se detecten los errores después de las primeras filas, así que considera la posibilidad de examinar el archivo CSV en su totalidad.
{% endalert %}

### Paso 5: Elige las preferencias de segmentación

También puedes elegir entre las siguientes preferencias de orientación. Si no necesitas crear un nuevo filtro de segmentación o segmento a partir de tu importación, selecciona **No hacer que esta lista esté disponible como filtro de segmentación**.

| Opción | Descripción |
|---|---|
| Filtro de selección | Para convertir tu archivo CSV en una opción de reorientación al crear segmentos de usuarios, elige tu archivo en el desplegable **Actualizado/Importado de CSV** y, a continuación, selecciona **Crear filtro de reorientación**. |
| Nuevos segmentos | Para crear también un nuevo segmento a partir de tu nuevo filtro **de segment** ación, selecciona **Crear filtro de segmentación y añadir a nuevo segmento**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Un grupo de filtros con el filtro "Actualizado/Importado de CSV" que incluye un archivo CSV titulado "Diversión en la temporada de Halloween".]({% image_buster /assets/img/csv_import/add_filter_group.png %}){: style="max-width:85%;"}

### Paso 6: Inicia tu importación CSV

Cuando estés listo, selecciona **Iniciar importación**. Puedes seguir el progreso actual en la página de **Importación de usuarios**, que se actualiza automáticamente cada cinco segundos.

Si no hay problemas, el estado se actualizará a **Completo** y se mostrará el número de filas procesadas. Todos los datos de las filas procesadas se añadirán a los perfiles existentes o a los perfiles de nueva creación.

{% alert note %}
Puedes importar más de un CSV al mismo tiempo. Las importaciones de CSV se ejecutan simultáneamente, por lo que no se garantiza que el orden de las actualizaciones sea en serie. Si necesitas que las importaciones de CSV se ejecuten una tras otra, espera a que haya finalizado una importación de CSV antes de cargar una segunda.
{% endalert %}

## Consideraciones sobre el punto de datos

Cada dato de clientes importado de un archivo CSV sobrescribirá el valor existente en los perfiles de usuario y registrará un punto de datos, excepto los ID externos y los valores en blanco. Si tienes alguna pregunta sobre los matices de los puntos de datos Braze, tu administrador de cuentas Braze puede responderte.

| Consideración | Detalles |
|---|---|
| ID externos | Cargar un CSV con sólo `external_id` no registrará puntos de datos. Esto te permite segmentar a los usuarios existentes de Braze sin afectar a los límites de datos. Sin embargo, incluir campos como `email` o `phone` sobrescribirá los datos de usuario existentes **y** registrará puntos de datos. <br><br>Las importaciones de CSV utilizadas sólo para la segmentación no registran puntos de datos, como los que sólo contienen `external_id`, `braze_id` o `user_alias_name`. |
| Valores en blanco | Los valores en blanco de tu CSV no sobrescribirán los datos de perfil de usuario existentes. No es necesario que incluyas todos los atributos de usuario o eventos personalizados al importar. |
| Estados de suscripción | La actualización de `email_subscribe`, `push_subscribe`, `subscription_group_id`, o `subscription_state` **no** cuenta para el uso de punto de datos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
Configurar `language` o `country` en un usuario a través de la importación en CSV o API impedirá que Braze capture automáticamente esta información a través del SDK.
{% endalert %}

## Solución de problemas

Revisa estos problemas comunes si tienes problemas con la importación de CSV. ¿Aún necesitas ayuda? Ponte en contacto con [support@braze.com](mailto:support@braze.com).

### Problemas de formato de los archivos

#### Fila malformada

Si la carga se completó con errores, es posible que haya una fila mal formada en tu archivo CSV. 

Para importar datos correctamente, debe haber una fila de encabezamiento. Cada fila debe tener el mismo número de celdas que la fila de cabecera. Las filas con una longitud de más o menos valores que la fila de cabecera se excluirán de la importación. Las comas en un valor se interpretarán como un separador y pueden provocar este error. Además, todos los datos deben estar codificados en UTF-8.

Si tu archivo CSV tiene filas en blanco e importa menos filas que el total de líneas del archivo CSV, puede que esto no indique un problema con la importación, ya que no sería necesario importar las filas en blanco. Comprueba el número de líneas que se importaron correctamente y asegúrate de que coincide con el número de usuarios que intentas importar.

#### Fila que falta

Hay algunas razones por las que el número de usuarios importados puede no coincidir con el total de filas de tu archivo CSV:

| Edición | Resolución |
|---|---|
| Duplicar ID externos, alias de usuario, ID Braze, direcciones de correo electrónico o números de teléfono. | Si hay columnas ID externas duplicadas, esto puede provocar filas mal formadas o no importadas, aunque las filas estén formateadas correctamente. En algunos casos, esto puede no informar de un error específico. Comprueba si hay duplicados y elimínalos antes de volver a subirlos. |
| Caracteres acentuados | Tu CSV puede incluir nombres o atributos con acentos. Asegúrate de que el archivo está codificado en UTF-8 para evitar problemas de importación. |
| El ID de Braze pertenece a un usuario huérfano | Si un usuario se fusionó con otro y Braze no puede asociar el ID de Braze con el perfil restante, la fila no se importará. |
| Fila vacía | Las filas en blanco en el CSV pueden provocar errores de datos malformados. Compruébalo utilizando un editor de texto plano, no Excel ni Sheets. |
| Incluyendo las comillas dobles (`"` ) | Este carácter no es válido y provocará una fila malformada. Utiliza en su lugar comillas simples (`'`). |
| Saltos de línea incoherentes | Los saltos de línea mixtos (e.g., `\n` y `\r\n`) pueden hacer que la primera fila de datos se trate como parte de la cabecera. Utiliza un editor hexadecimal o de texto avanzado para inspeccionar y arreglar. |
| Archivo codificado incorrectamente | Aunque se permitan los acentos, el archivo debe estar codificado en UTF-8. Otras codificaciones pueden funcionar parcialmente, pero no son totalmente compatibles. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Cita de cadena

Los valores entre comillas simples (`''`) o dobles (`""`) se leerán como cadenas en la importación.

#### Fechas con formato incorrecto

Las fechas que no estén en formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) no se leerán como `datetimes` en la importación.

### Cuestiones de estructura de datos

#### Direcciones de correo electrónico no válidas

Si tu carga se completó con errores, es posible que haya una o más direcciones de correo electrónico codificadas no válidas. Confirma que todas las direcciones de correo electrónico están codificadas correctamente antes de importarlas a Braze.

- **Al [actualizar o importar direcciones de correo electrónico]({{site.baseurl}}/user_guide/analytics/field_level_encryption/#step-3-import-and-update-users)** en Braze, utiliza el valor de correo electrónico cifrado siempre que se incluya un correo electrónico. Estos valores hash de correo electrónico los proporciona tu equipo interno. 
- **Al crear un nuevo usuario**, debes añadir `email_encrypted` con el valor de correo electrónico encriptado del usuario. De lo contrario, no se creará el usuario. Del mismo modo, si vas a añadir una dirección de correo electrónico a un usuario existente que no tiene correo electrónico, debes añadir `email_encrypted`. De lo contrario, el usuario no se actualizará.

#### Datos importados como atributo personalizado

Si un dato de usuario predeterminado (como `email` o `first_name`) se importa como atributo personalizado, comprueba las mayúsculas y minúsculas y el espaciado de tu archivo CSV. Por ejemplo, `First_name` se importaría como un atributo personalizado, mientras que `first_name` se importaría correctamente en el campo "nombre" del perfil de un usuario.

#### Múltiples tipos de datos

Braze espera que cada valor de una columna sea del mismo tipo de datos. Los valores que no coincidan con el tipo de datos de su atributo provocarán errores en la segmentación.

Además, empezar un atributo numérico por cero causará problemas, porque los números que empiezan por ceros se consideran cadenas. Cuando Braze convierta esa cadena, podrá tratarla como un valor octal (que utiliza dígitos del cero al siete), lo que significa que se convertirá a su valor decimal correspondiente. Por ejemplo, si el valor del archivo CSV es 0130, el perfil Braze mostrará 88. Para evitar este problema, utiliza atributos con tipos de datos de cadena. Sin embargo, este tipo de datos no está disponible en la comparación de números de segmentación.

#### Tipos de atributos predeterminados

Algunos atributos predeterminados sólo aceptan determinados valores como válidos para las actualizaciones de los usuarios. Para orientarte, consulta [Construir tu CSV]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/#constructing-your-csv).

Los espacios al final y las diferencias de mayúsculas pueden hacer que un valor se interprete como no válido. Por ejemplo, en el siguiente archivo CSV, sólo se actualizarán correctamente los estados de correo electrónico y push del usuario de la primera fila (`brazetest1`) porque los valores aceptados son `unsubscribed`, `subscribed` y `opted_in`. 

```plaintext
external_id,email,email_subscribe,push_subscribe
brazetest1,test1@braze.com,unsubscribed,unsubscribed
brazetest2,test2@braze.com,Unsubscribed,Unsubscribed
```

### "Seleccionar archivo CSV" no funciona

Hay varias razones por las que el botón **Seleccionar archivo CSV** puede no funcionar:

| Edición | Resolución |
|---|---|
| Bloqueador de ventanas emergentes | Esto puede impedir que se muestre la página. Confirma que tu navegador permite ventanas emergentes en el sitio web del panel de Braze. |
| Navegador anticuado | Asegúrate de que tu navegador está actualizado; si no lo está, actualízalo a la última versión. |
| Procesos de fondo | Cierra todas las instancias del navegador y reinicia tu computadora. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
