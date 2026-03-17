---
nav_title: Importación CSV
article_title: "Importación CSV"
description: "Aprende a registrar y actualizar atributos de usuario y eventos personalizados mediante la importación de CSV."
page_order: 1.2
---

# Importación CSV

> Aprende a registrar y actualizar atributos de usuario y eventos personalizados mediante la importación de CSV.

## Acerca de la importación de CSV

Puedes utilizar la importación CSV para registrar y actualizar los siguientes atributos de usuario y eventos personalizados.

|Tipo|Definición|Ejemplo|Tamaño máximo del archivo|
|---|---|---|---|
|Atributos predeterminados|Atributos de usuario reservados reconocidos por Braze.|`first_name`, `email`|500 MB|
|Atributos personalizados|Atributos de usuario únicos de tu empresa.|`last_destination_searched`|500 MB|
|Eventos personalizados|Eventos únicos de tu negocio que representan acciones de los usuarios.|`trip_booked`|50 MB|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

## Usar la importación CSV

### Paso 1: Descargar una plantilla CSV

Para abrir la importación de usuarios en CSV, ve a **Audiencias** > **Importar usuarios**. Aquí encontrarás una tabla con información detallada sobre las importaciones más recientes, como la fecha de carga, el nombre del usuario que la ha subido, el nombre del archivo, la disponibilidad de segmentación, el número de filas importadas y el estado de la importación.

Para empezar a utilizar tu CSV, descarga una plantilla para atributos o eventos.

![La página "Importar usuarios" del panel de Braze.]({% image_buster /assets/img/csv_import/import_users_page.png %})

### Paso 2: Elige un identificador {#choose-an-identifier}

El archivo CSV que importes necesitará un identificador específico. Puedes elegir entre las siguientes opciones:

{% tabs local %}
<!-- TAB -->
{% tab external id %}
Al importar los datos de clientes, puedes utilizar un`external_id`  como identificador único de cada cliente. Cuando proporcionas un`external_id`  en tu importación, Braze actualiza cualquier usuario existente con el mismo`external_id`  o crea un usuario con un identificador nuevo con ese`external_id`  establecido si no se encuentra ninguno.

- Descargar: [Plantilla de importación de atributos CSV: ID externo]({{site.baseurl}}/assets/download_file/braze-user-import-template-csv.xlsx?3aafd0c03634ac03f248b3055fbc3126)
- Descargar: [Plantilla de importación de eventos CSV: ID externo](https://braze.com/unlisted_docs/assets/download_file/braze-csv-events-import-template.csv?3b64ea284baa9a21cfe0a7ab4b46fce4)

{% alert note %}
Si vas a cargar una mezcla de usuarios con  `external_id`y usuarios sin , debes crear un CSV para cada importación. Un CSV no puede contener tanto`external_ids`  como alias de usuario.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab user alias %}
Para dirigirte a usuarios que no tienen una cuenta`external_id`, puedes importar una lista de usuarios con alias de usuario. Un alias sirve como identificador único alternativo del usuario y puede resultar útil si intentas dirigirte a usuarios anónimos que no se han registrado ni han creado una cuenta en tu aplicación.

Si está cargando o actualizando perfiles de usuario que son sólo alias, debe tener las dos columnas siguientes en su CSV:

- `user_alias_name`: Un identificador único de usuario; una alternativa al `external_id`  
- `user_alias_label`: Una etiqueta común para agrupar los alias de usuario

| `user_alias_name` | `user_alias_label` | `last_name` | `email` | sample_attribute |
| :---- | :---- | :---- | :---- | :---- |
| 182736485 | my_alt_identifier | Smith | smith@user.com | TRUE |
| 182736486 | my_alt_identifier | Nguyen | nguyen@user.com | FALSO |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation"}

Cuando proporcionas tanto un`user_alias_name`  como un`user_alias_label`  en tu importación, Braze actualiza cualquier usuario existente con el mismo`user_alias_name`  y `user_alias_label`. Si no se encuentra un usuario, Braze crea un usuario con un identificador nuevo con ese`user_alias_name`conjunto.

{% alert important %}
No puedes utilizar una importación en CSV para actualizar un usuario existente con un`user_alias_name`  si ya tiene un `external_id`. En su lugar, esto crea un nuevo perfil de usuario con el asociado `user_alias_name`. Para asociar un usuario de solo alias con un `external_id`, utiliza el [punto final Identificar usuarios]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/).
{% endalert %}

Descargar: [Plantilla de importación de atributos CSV: Alias de usuario]({{site.baseurl}}/assets/download_file/braze-user-import-alias-template-csv.xlsx?c0ce6c0aa1e901395161d87c5ba17747)
{% endtab %}

<!-- TAB -->
{% tab braze id %}
Para actualizar perfiles de usuario existentes en Braze utilizando un valor interno de ID de Braze en lugar de un valor de `external_id` o `user_alias_name` y `user_alias_label`, especifica `braze_id` como cabecera de columna.

Esto puede ser útil si has exportado datos de usuario desde Braze a través de nuestra opción de exportación CSV dentro de la segmentación y quieres añadir un nuevo atributo personalizado a esos usuarios existentes.

{% alert important %}
No puedes utilizar la importación CSV para crear un nuevo usuario utilizando `braze_id`. Este método sólo puede utilizarse para actualizar usuarios preexistentes en la plataforma Braze.  
{% endalert %}

{% alert tip %}
El valor `braze_id` puede aparecer etiquetado como `Appboy ID` en las exportaciones CSV del cuadro de mandos Braze. Este ID será el mismo que el de `braze_id` para un usuario, por lo que puede cambiar el nombre de esta columna a `braze_id` cuando vuelva a importar el CSV.
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

Si un perfil existente tiene esa dirección de correo electrónico o número de teléfono, ese perfil se actualiza y Braze no crea un nuevo perfil. Si hay varios perfiles con esa misma dirección de correo electrónico, Braze utilizará la misma lógica que el [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), donde se actualizará el perfil actualizado más recientemente.

Si no existe ningún perfil con esa dirección de correo electrónico o número de teléfono, Braze crea un nuevo perfil con ese identificador. Puedes utilizar el [punto final`/users/identify` ]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) para identificar este perfil más adelante. Para eliminar un perfil de usuario, también puedes utilizar el punto final [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/).
{% endtab %}
{% endtabs %}

### Paso 3: Crea tu archivo CSV

Puedes cargar cualquiera de los siguientes tipos de datos en un único archivo CSV. Para cargar más de un tipo de datos, carga varios archivos CSV.

- **Atributos del usuario:** Esto incluye tanto los atributos predeterminados como los personalizados del usuario. Los atributos de usuario predeterminados son claves reservadas en Braze (como`first_name`  o `email`) y los atributos personalizados son atributos de usuario únicos para tu empresa (como `last_destination_searched`).  
- **Eventos personalizados:** Son únicos para tu negocio y reflejan las acciones que ha realizado un usuario, como`trip_booked`  en el caso de una aplicación de reservas de viajes.

Cuando estés listo para empezar a crear tu archivo CSV, consulta la siguiente información:

{% tabs local %}
<!-- TAB -->
{% tab user attributes %}
#### Identificadores necesarios {#required-identifiers-attributes}

Aunque  no`external_id` es obligatorio, **debes** incluir **uno** de los siguientes identificadores como encabezado en tu archivo CSV. Para obtener más información sobre cada uno de ellos, consulta [Elegir un identificador](#choose-an-identifier).

- `external_id`
- `braze_id`
- `user_alias_name` **y** `user_alias_label`
- `email`
- `phone`

#### Atributos personalizados

Los siguientes tipos de datos se pueden utilizar como atributos personalizados para la importación de CSV. Los encabezados de columna que no coinciden exactamente con un [atributo predeterminado](#default-attributes) se importan como atributos personalizados en Braze.

| Tipo de datos | Descripción |
|---|---|
| Fecha y hora | Debe almacenarse en formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601). |
| Booleano | Acepta `true` o `false`. |
| Número | Debe ser un número entero o flotante sin espacios ni comas. Los flotantes deben utilizar un punto (`.`.) como separador decimal. |
| Cadena | Puede contener comas si el valor está entre comillas dobles (`""`). |
| En blanco | Los valores en blanco no sobrescribirán los valores existentes en el perfil de usuario, y no es necesario que incluyas todos los atributos de usuario existentes en tu archivo CSV. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
Las matrices, los tokens de notificaciones push y los tipos de datos de eventos personalizados no son compatibles con la importación de usuarios, ya que las comas del archivo CSV se interpretarán como separadores de columnas y provocarán errores al analizar el archivo.<br><br>Para cargar este tipo de valores, utiliza el[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)[punto final]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) o [la ingesta de datos]({{site.baseurl}}/user_guide/data/cloud_ingestion/).
{% endalert %} 

#### Atributos predeterminados

{% alert important %}
Al importar atributos predeterminados, los encabezados de columna que utilices deben coincidir exactamente con la ortografía y el uso de mayúsculas de los atributos de usuario predeterminados. De lo contrario, Braze los detecta como [atributos personalizados](#custom-attributes).
{% endalert %}

Los siguientes atributos predeterminados están disponibles para la importación de usuarios.

| Campo Perfil de usuario | Tipo de datos | Descripción | ¿Es necesario? |
| :---- | :---- | :---- | :---- |
| `external_id` | Cadena | Un identificador de usuario único para su cliente. | Condicionalmente. Consulta [Identificadores obligatorios](#required-identifiers-attributes). |
| `user_alias_name` | Cadena | Un identificador único de usuario para usuarios anónimos que es una alternativa a `external_id`. Debe utilizarse con `user_alias_label`. | Condicionalmente. Consulta [Identificadores obligatorios](#required-identifiers-attributes). |
| `user_alias_label` | Cadena | Una etiqueta común para agrupar los alias de usuario. Debe utilizarse con `user_alias_name`. | Condicionalmente. Consulta [Identificadores obligatorios](#required-identifiers-attributes). |
| `first_name` | Cadena | El nombre de pila de sus usuarios tal y como lo han indicado (por ejemplo, `Jane`). | No |
| `last_name` | Cadena | El apellido de sus usuarios tal y como lo han indicado (por ejemplo, `Doe`). | No |
| `email` | Cadena | El correo electrónico de sus usuarios tal y como lo han indicado (por ejemplo, `jane.doe@braze.com`). | No |
| `country` | Cadena | Los códigos de país deben pasarse a Braze en la norma ISO-3166-1 alfa-2 (por ejemplo, `GB`). | No |
| `dob` | Cadena | Debe introducirse en el formato «AAAA-MM-DD» (por ejemplo, `1980-12-21`). Esto importa la fecha de nacimiento de tus usuarios y te habilita para dirigirte a aquellos cuyo cumpleaños sea «hoy». | No |
| `gender` | Cadena | «M», «F», «O» (otro), «N» (no aplicable), «P» (prefieres no decirlo) o nulo (desconocido). | No |
| `home_city` | Cadena | La ciudad de residencia de sus usuarios tal y como la han indicado (por ejemplo, `London`). | No |
| `language` | Cadena | El idioma debe pasarse a Braze en la norma ISO-639-1 (por ejemplo, `en`). Consulta nuestra [lista de idiomas aceptados]({{site.baseurl}}/user_guide/data/user_data_collection/language_codes/). | No |
| `phone` | Cadena | Un número de teléfono indicado por sus usuarios, en formato `E.164` (por ejemplo, `+442071838750`). Consulte [Números de teléfono de usuario]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/) para obtener orientación sobre el formato. | No |
| `email_open_tracking_disabled` | Booleano | verdadero o falso aceptado. Establézcalo en true para desactivar que el píxel de seguimiento de apertura se añada a todos los futuros correos electrónicos enviados a este usuario. Disponible solo para SparkPost y SendGrid. | No |
| `email_click_tracking_disabled` | Booleano | verdadero o falso aceptado. Establecer en true para desactivar el seguimiento de clics para todos los enlaces dentro de un futuro correo electrónico, enviado a este usuario. Disponible solo para SparkPost y SendGrid. | No |
| `email_subscribe` | Cadena | Los valores disponibles son `opted_in` (inscrito explícitamente para recibir mensajes de correo electrónico), `unsubscribed` (excluido explícitamente de recibir mensajes de correo electrónico) y `subscribed` (ni inscrito ni excluido). | No |
| `push_subscribe` | Cadena | Los valores disponibles son `opted_in` (se ha registrado explícitamente para recibir mensajes push), `unsubscribed` (se ha excluido explícitamente de los mensajes push) y `subscribed` (ni se registró ni se excluyó). | No |
| `time_zone` | Cadena | La zona horaria debe pasarse a Braze en el mismo formato que la base de datos de zonas horarias de IANA (por ejemplo, `America/New_York` o `Eastern Time (US & Canada)`). | No |
| `date_of_first_session`  `date_of_last_session` | Cadena | Puede transmitirse en uno de los siguientes formatos ISO 8601: «AAAA-MM-DD» «AAAA-MM-DDTHH:MM:SS+00:00» «AAAA-MM-DDTHH:MM:SSZ» «AAAA-MM-DDTHH:MM:SS» (por ejemplo, 2019-11-20T18:38:57) | No |
| `subscription_group_id` | Cadena | La dirección `id` de su grupo de suscripción. Este identificador se encuentra en la página del grupo de suscripción de su panel de control. | No |
| `subscription_state` | Cadena | El estado de suscripción para el grupo de suscripción especificado por `subscription_group_id`. Los valores permitidos son `unsubscribed` (no en el grupo de suscripción) o `subscribed` (en el grupo de suscripción). | No, pero se recomienda encarecidamente si se utiliza `subscription_group_id`  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

#### Actualización del estado del grupo de suscripción (opcional)

Además, puedes añadir usuarios a grupos de suscripción por correo electrónico o SMS mediante la importación de usuarios. Esto es especialmente útil para los SMS, ya que un usuario debe estar inscrito en un grupo de suscripción SMS para recibir mensajes con el canal SMS. Para más información, consulta [Grupos de suscripción por SMS](https://www.braze.com/docs/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement).

Si estás actualizando estados del grupo de suscripción, debes tener las dos columnas siguientes en tu CSV:

- `subscription_group_id`: La dirección `id` del [grupo de suscripción](https://www.braze.com/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups).  
- `subscription_state`: Los valores disponibles son `unsubscribed` (no está en el grupo de suscripción) o `subscribed` (está en el grupo de suscripción).

| external_id | first_name | subscription_group_id | subscription_state |
| :---- | :---- | :---- | :---- |
| A8i3mkd99 | Colby | 6ff593d7-cf69-448b-aca9-abf7d7b8c273 | suscrito |
| k2LNhj8Ks | Tom | aea02307-a91e-4bc0-abad-1c0bee817dfa | suscrito |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

{% alert note %}
Sólo se puede establecer un único `subscription_group_id` por fila en la importación de usuarios. Diferentes filas pueden tener diferentes valores `subscription_group_id`. Sin embargo, si necesitas inscribir a los mismos usuarios en varios grupos de suscripción, tendrás que realizar varias importaciones.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab custom events %}
#### Identificadores necesarios {#required-identifiers-custom-events}

Aunque  no`external_id` es obligatorio, **debes** incluir **uno** de los siguientes identificadores como encabezado en tu archivo CSV. Para obtener más información sobre cada uno de ellos, consulta [Elegir un identificador](#choose-an-identifier).

- `external_id`
- `braze_id`
- `user_alias_name` **y** `user_alias_label`
- `email`
- `phone`

#### Campos de eventos personalizados

Además de lo siguiente, tu CSV también puede contener encabezados de columna adicionales para las propiedades del evento. Estas propiedades deben tener un encabezado de columna de `<event_name>.properties.<property name>.`

Por ejemplo, el evento personalizado`trip_booked` puede tener las propiedades`destination`y `duration`. Estos pueden importarse utilizando los encabezados de columna`trip_booked.properties.destination`  y `trip_booked.properties.duration`.

| Campo Perfil de usuario | Tipo de datos | Información | ¿Es necesario? |
| :---- | :---- | :---- | :---- |
| `external_id` | Cadena | Un identificador único para tu usuario. | Condicionalmente. Consulta [Identificadores obligatorios](#required-identifiers-custom-events). |
| `braze_id` | Cadena | Un identificador Braze asignado a tu usuario. | Condicionalmente. Consulta [Identificadores obligatorios](#required-identifiers-custom-events). |
| `user_alias_name` | Cadena | Un identificador único para usuarios anónimos, que es una alternativa a `external_id`. Debe utilizarse con `user_alias_label`. | Condicionalmente. Consulta [Identificadores obligatorios](#required-identifiers-custom-events). |
| `user_alias_label` | Cadena | Una etiqueta común para agrupar los alias de usuario. Debe utilizarse con `user_alias_name`. | Condicionalmente. Consulta [Identificadores obligatorios](#required-identifiers-custom-events). |
| `email` | Cadena | El correo electrónico de sus usuarios tal y como lo han indicado (por ejemplo, `jane.doe@braze.com`). | No, y solo se puede utilizar en ausencia de otros identificadores. Véase la siguiente nota. |
| `phone` | Cadena | Un número de teléfono indicado por sus usuarios, en formato `E.164` (por ejemplo, `+442071838750`). Consulte [Números de teléfono de usuario]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/) para obtener orientación sobre el formato. | No, y solo se puede utilizar en ausencia de otros identificadores. Véase la siguiente nota. |
| `name` | Cadena | Un evento personalizado de tus usuarios. | Sí |
| `time` | Cadena | La hora del evento. Se puede transmitir en uno de los siguientes formatos ISO-8601: «AAAA-MM-DD» «AAAA-MM-DDTHH:MM:SS+00:00» «AAAA-MM-DDTHH:MM:SSZ» «AAAA-MM-DDTHH:MM:SS» (por ejemplo, 2019-11-20T18:38:57) | Sí |
| `<event name>.properties.<property name>` | Múltiples | Una propiedad de evento asociada a un evento personalizado. Un ejemplo es `trip_booked.properties.destination` | No |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}
{% endtab %}
{% endtabs %}

### Paso 4: Sube tu archivo

Para cargar tu archivo, selecciona **Atributos** o **Eventos**, haz clic en **Examinar archivos** y carga tu CSV. Braze muestra una vista previa de las primeras filas y un resumen de los campos detectados.

![El modal de carga completada muestra una vista previa del archivo, el campo de nombre de importación, las preferencias de segmentación y la casilla de verificación de validación del archivo.]({% image_buster /assets/img/csv_import/upload_completed.png %})

En el campo **Nombre de la importación**, puedes cambiar el nombre de la importación. De forma predeterminada, se utiliza el nombre del archivo.

{% alert note %}
La vista previa del archivo solo muestra las primeras filas del archivo. Para comprobar cada fila antes de importarla, utiliza [la validación de archivos](#file-validation).
{% endalert %}

### Paso 5: Valida tu archivo (opcional) {#file-validation}

Antes de iniciar la importación, puedes ejecutar la validación de archivos para comprobar si hay errores y advertencias en cada fila. Para validar tu archivo, selecciona **Validar archivo antes de importar** y, a continuación, haz clic en **Iniciar importación**.

La validación puede tardar hasta 2 minutos para los archivos con el tamaño máximo permitido. Mientras se ejecuta la validación, puedes seleccionar **Omitir validación** para saltártela y continuar inmediatamente.

#### Resultados de la validación

Cuando finaliza la validación, aparece uno de los siguientes resultados.

| Resultado | Qué significa | Siguiente paso |
|---|---|---|
| **Validación completada** | No se han encontrado problemas. | Selecciona **Importar datos**. |
| **Problemas detectados** | Algunas filas contienen errores o advertencias. | Descarga el informe de errores para revisarlos y, a continuación, selecciona **Importar de todos modos** para continuar o **Cancelar** para corregir primero el archivo. |
| **Se ha agotado el tiempo de espera de la validación** | Se agotó el tiempo de validación. Las filas que se revisaron no tenían ningún problema. | Selecciona **Importar datos**. En unos minutos estará disponible un informe completo. |
| **Se agotó el tiempo de espera de la validación con problemas** | La validación se agotó y encontró errores en algunas de las filas que comprobó. | Descarga el informe parcial para revisar lo que se ha encontrado y, a continuación, selecciona **Importar de todos modos** o **Cancelar**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

![El cuadro de diálogo «Problemas encontrados» muestra el recuento de filas con errores y advertencias, con opciones para cancelar, descargar el informe de errores o importar de todos modos.]({% image_buster /assets/img/csv_import/validation_issues.png %})

#### Comprender el informe de errores

El informe de errores es un archivo CSV que contiene todas las filas marcadas junto con sus datos originales y una descripción del problema.

| Tipo de problema | Descripción |
|---|---|
| **Error** | La fila se omitirá por completo durante la importación. |
| **Advertencia** | La fila se importará, pero algunos valores se omitirán. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Después de revisar el informe, puedes corregir los problemas en tu archivo original y volver a subirlo, o continuar con la importación y aceptar los resultados parciales.

### Paso 6: Elige tus preferencias de segmentación

También puedes elegir entre las siguientes preferencias de segmentación. Si no necesitas crear un nuevo filtro de segmentación o segmento a partir de tu importación, selecciona **No hacer que esta lista esté disponible como filtro de segmentación**.

| Opción | Descripción |
|---|---|
| Filtro de segmentación | Para convertir tu archivo CSV en una opción de retargeting al crear segmentos de usuarios, selecciona tu archivo en el menú desplegable **Actualizado/Importado desde CSV** y, a continuación, selecciona **Crear filtro de segmentación**. |
| Nuevos segmentos de segmentación | Para crear también un nuevo segmento a partir de tu nuevo filtro de segmentación, selecciona **Crear filtro de segmentación y añadir al nuevo segmento** . |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

![Un grupo de filtros con el filtro «Actualizado/Importado desde CSV» que incluye un archivo CSV titulado «Diversión en Halloween».]({% image_buster /assets/img/csv_import/add_filter_group.png %}){: style="max-width:85%;"}

### Paso 7: Inicia la importación de CSV

Cuando estés listo, haz clic en **Iniciar importación**. Puedes realizar el seguimiento del progreso actual en la página **Importar usuarios**, que se actualiza automáticamente cada 5 segundos.

{% alert note %}
Puede importar más de un CSV al mismo tiempo. Las importaciones de CSV se ejecutan simultáneamente, por lo que no se garantiza que el orden de las actualizaciones sea en serie. Si necesita que las importaciones CSV se ejecuten una tras otra, espere a que una importación CSV haya finalizado antes de cargar una segunda.
{% endalert %}

#### Estados de importación

Una vez iniciada la importación de usuarios, puedes comprobar su estado en la página **Importar usuarios**.

| Estado | Descripción |
|---|---|
| **Completado** | Todas las filas se han importado correctamente. |
| **Éxito parcial** | Algunas filas han fallado. Selecciona el menú de tres puntos situado junto a la importación para descargar un informe de errores o el archivo CSV original cargado. |
| **En curso** | La importación se está realizando actualmente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

![La página Importar usuarios muestra un estado de éxito parcial con el menú contextual abierto, en el que aparecen las opciones Descargar informe de errores y Descargar CSV cargado.]({% image_buster /assets/img/csv_import/partial_success_menu.png %})

El informe de errores posterior a la importación incluye filas que han fallado por motivos que la validación no cubre, como cuando un usuario no existe en Braze.

## Consideraciones sobre los puntos de datos

Cada dato de cliente importado desde un archivo CSV sobrescribe el valor existente en los perfiles de usuario y registra un punto de datos, excepto en el caso de los ID externos y los valores en blanco. Si tienes alguna pregunta sobre los matices de los puntos de datos de Braze, tu director de cuentas de Braze puede responderla.

| Consideración | Detalles |
|---|---|
| ID externo | Al cargar un archivo CSV que solo `external_id`contiene  no se registran los puntos de datos. Esto te permite segmentar a los usuarios actuales de Braze sin afectar los límites de datos. Sin embargo, incluir campos como`email`  o`phone`  sobrescribe los datos de usuario existentes y registra puntos de datos. <br><br>Las importaciones CSV utilizadas únicamente para la segmentación no registran puntos de datos, como los que solo contienen`external_id` , `braze_id`, o `user_alias_name`. |
| Valores en blanco | Los valores en blanco en tu CSV no sobrescribirán los datos existentes del perfil de usuario. No es necesario incluir todos los atributos de usuario ni todos los eventos personalizados al importar. |
| Estados de suscripción | La actualización `email_subscribe`de , `push_subscribe`, `subscription_group_id`, o`subscription_state`  **no** cuenta para el uso de puntos de datos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
La configuración`language`o`country`el usuario en CSV o a través de la API impiden que Braze capture automáticamente esta información a través del SDK.
{% endalert %}

## Solución de problemas

Si utilizaste [la validación de archivos](#file-validation), comienza por el informe de errores, que incluye el problema específico de cada fila marcada y una descripción de cómo solucionarlo. Para las filas que fallaron durante la importación en lugar de la validación, descarga el informe de errores desde el menú de tres puntos en la página **Importar usuarios**.

Si tienes problemas con la importación de CSV, revisa estos problemas comunes a continuación. ¿Aún necesitas ayuda? Ponte en contacto con [support@braze.com](mailto:support@braze.com).

### Problemas con el formato de los archivos

#### Fila malformada

Si la carga se ha completado con errores, es posible que haya una fila mal formada en tu archivo CSV. 

Para importar datos correctamente, debe haber una fila de encabezado. Cada fila debe tener el mismo número de celdas que la fila de cabecera. Las filas con una longitud superior o inferior a la fila de cabecera se excluirán de la importación. Las comas en un valor se interpretarán como un separador y pueden provocar este error. Además, todos los datos deben estar codificados en UTF-8.

Si tu archivo CSV tiene filas en blanco e importas menos filas que el total de líneas del archivo CSV, esto puede no indicar un problema con la importación, ya que las filas en blanco no necesitarían importarse. Compruebe el número de líneas que se han importado correctamente y asegúrese de que coincide con el número de usuarios que está intentando importar.

#### Falta una fila

Existen varias razones por las que el número de usuarios importados puede no coincidir con el total de filas de su archivo CSV:

| Problema | Resolución |
|---|---|
| ID externos duplicados, alias de usuario, ID de Braze, direcciones de correo electrónico o números de teléfono. | Si hay columnas ID externas duplicadas, esto puede provocar filas mal formadas o no importadas, aunque las filas estén formateadas correctamente. En algunos casos, es posible que no se informe de ningún error específico. Comprueba si hay duplicados y elimínalos antes de volver a subirlos. |
| Caracteres acentuados | Tu CSV puede incluir nombres o atributos con acentos. Asegúrate de que el archivo esté codificado en UTF-8 para evitar problemas de importación. |
| Braze ID pertenece a un usuario huérfano. | Si un usuario se ha fusionado con otro y Braze no puede asociar el ID de Braze con el perfil restante, la fila no se importará. |
| Fila vacía | Las filas en blanco en el CSV pueden provocar errores de datos malformados. Compruébalos con un editor de texto sin formato, no con Excel ni Sheets. |
| Comillas dobles sin escapar o desequilibradas (`"`) | Las comillas dobles enmarcan los valores de cadena que contienen comas. Si un valor contiene comillas dobles, escápalo duplicándolo (`""`). Las comillas dobles sin escapar o desequilibradas provocan una fila malformada. |
| Saltos de línea inconsistentes | Los saltos de línea mixtos (e.g.,`\n`  y `\r\n`) pueden hacer que la primera fila de datos se trate como parte del encabezado. Utiliza un editor hexadecimal o un editor de texto avanzado para inspeccionar y corregir. |
| Archivo codificado incorrectamente | Aunque se permitan los acentos, el archivo debe estar codificado en UTF-8. Otras codificaciones pueden funcionar parcialmente, pero no son totalmente compatibles. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Cita de cadena

Los valores entre comillas simples (`''`) o dobles (`""`) se leerán como cadenas en la importación.

#### Fechas con formato incorrecto

Las fechas que no estén en formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) no se leerán como `datetimes` en la importación.

### Problemas con la estructura de datos

#### Direcciones de correo electrónico no válidas

Si la carga se ha completado con errores, es posible que haya una o varias direcciones de correo electrónico cifradas no válidas. Confirma que todas las direcciones de correo electrónico estén cifradas correctamente antes de importarlas a Braze.

- **Al [actualizar o importar direcciones de correo electrónico]({{site.baseurl}}/user_guide/analytics/field_level_encryption/#step-3-import-and-update-users)** en Braze, utiliza el valor hash del correo electrónico siempre que se incluya un correo electrónico. Estos valores hash de correo electrónico son proporcionados por tu equipo interno. 
- **Al crear un nuevo usuario**, debes añadir`email_encrypted`  con el valor cifrado del correo electrónico del usuario. De lo contrario, Braze no creará el usuario. Del mismo modo, si añades una dirección de correo electrónico a un usuario existente que no tiene correo electrónico, debes añadir `email_encrypted`. De lo contrario, Braze no actualizará al usuario.

#### Datos importados como atributo personalizado

Si un dato de usuario predeterminado (como `email` o `first_name`) se importa como atributo personalizado, comprueba las mayúsculas y minúsculas y el espaciado de tu archivo CSV. Por ejemplo,`First_name`  se importa como un atributo personalizado, mientras que`first_name`  se importa correctamente en el campo «nombre» del perfil de usuario.

#### Múltiples tipos de datos

Braze espera que cada valor de una columna sea del mismo tipo de datos. Los valores que no coinciden con el tipo de datos de su atributo provocan errores en la segmentación.

Además, comenzar un atributo numérico con cero causará problemas, ya que los números que comienzan con cero se consideran cadenas. Cuando Braze convierte esa cadena, puede tratarla como un valor octal (que utiliza dígitos del cero al siete), lo que significa que se convierte a su valor decimal correspondiente. Por ejemplo, si el valor del archivo CSV es 0130, el perfil de Braze muestra 88. Para evitar este problema, utiliza atributos con tipos de datos de cadena. Sin embargo, este tipo de datos no está disponible en la comparación de números de segmentación.

#### Tipos de atributos predeterminados

Algunos atributos predeterminados solo pueden aceptar determinados valores como válidos para las actualizaciones de los usuarios. Para obtener orientación, consulta [Creación]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/#constructing-your-csv) de [tu CSV]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/#constructing-your-csv).

Los espacios al final y las diferencias en el uso de mayúsculas pueden hacer que un valor se interprete como no válido. Por ejemplo, en el siguiente archivo CSV, solo el usuario de la primera fila (`brazetest1`) tiene el correo electrónico y los estados push actualizados correctamente, ya que los valores aceptados son `unsubscribed`,`subscribed` y `opted_in`. 

```plaintext
external_id,email,email_subscribe,push_subscribe
brazetest1,test1@braze.com,unsubscribed,unsubscribed
brazetest2,test2@braze.com,Unsubscribed,Unsubscribed
```

### «Seleccionar archivo CSV» no funciona.

Hay varias razones por las que el botón **Seleccionar archivo CSV** puede no funcionar:

| Problema | Resolución |
|---|---|
| Bloqueador de ventanas emergentes | Esto puede impedir que se muestre la página. Confirma que tu navegador permite las ventanas emergentes en el sitio web del panel de Braze. |
| Navegador obsoleto | Asegúrate de que tu navegador esté actualizado; si no es así, actualízalo a la última versión. |
| Procesos en segundo plano | Cierra todas las instancias del navegador y reinicia la computadora. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
