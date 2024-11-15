---
nav_title: Importar datos de usuarios y eventos CSV
article_title: Importar datos de usuarios y eventos CSV
permalink: "/csv_events/"
description: "Este artículo de referencia explica cómo importar datos de usuario y cómo importar eventos personalizados utilizando archivos CSV."
page_type: reference
---

# Importar datos de usuario (eventos CSV de acceso anticipado)

> Braze ofrece varias formas de importar datos de usuarios a la plataforma: SDK, API, ingesta de datos en la nube, integraciones de socios tecnológicos y archivos CSV. Este artículo proporciona instrucciones detalladas sobre cómo importar datos de usuario, incluyendo cómo [importar eventos personalizados mediante archivos CSV (acceso anticipado)](#importing-custom-events).

{% multi_lang_include email-via-sms-warning.md %}

Antes de continuar, nota que Braze no sanea (valida o formatea correctamente) los datos HTML durante la importación. Esto significa que las etiquetas de script deben eliminarse de todos los datos de importación destinados a la personalización Web.

## API REST

Puedes utilizar el [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para registrar eventos personalizados, atributos de usuario y compras de usuarios.

## Importación CSV

Puedes subir y actualizar perfiles de usuario mediante archivos CSV desde **Audiencia** > Importar **usuarios.**

La importación de datos de usuario mediante archivos CSV permite registrar y actualizar atributos de usuario como el nombre y el correo electrónico, además de atributos personalizados como la talla de calzado. Puedes importar un CSV especificando uno de los dos identificadores únicos de usuario: un `external_id` o un alias de usuario.

{% alert important %}
La importación de usuarios también permite grabar y actualizar eventos personalizados de usuario. De forma similar a los atributos de usuario, puedes importar con un `external_id`, `braze_id` o con `user_alias_name` con `user_alias_label`. Para más detalles, consulta [Importar eventos personalizados](#importing-custom-events).
{% endalert %}

{% alert note %}
Si estás subiendo una mezcla de usuarios con un `external_id` y usuarios sin él, tienes que crear un archivo CSV para cada importación. Un archivo CSV no puede contener tanto `external_ids` como alias de usuario.
{% endalert %}

### Importar con ID externo

Al importar tus datos de clientes, tendrás que especificar el identificador único de cada cliente, también conocido como `external_id`. Antes de iniciar la importación en CSV, es importante que tu equipo de ingeniería sepa cómo se identificarán los usuarios en Braze. Normalmente es un ID interno de la base de datos. Debe coincidir con el modo en que el SDK de Braze identificará a los usuarios en el móvil y en la Web, y está diseñado para que cada cliente tenga un único perfil de usuario en Braze en todos sus dispositivos. Más información sobre el [ciclo de vida del perfil de usuario][13] de Braze.

Cuando proporciones un `external_id` en tu importación, Braze actualizará cualquier usuario existente con el mismo `external_id` o creará un nuevo usuario identificado con ese `external_id` establecido si no se encuentra ninguno.

- **Descargar:** [Plantilla de importación de atributos CSV][import_template]
- **Descargar:** [Plantilla CSV de importación de eventos][events_template]

### Importar con alias de usuario

Para dirigirte a usuarios que no tienen un `external_id`, puedes importar una lista de usuarios con alias de usuario. Un alias sirve como identificador de usuario único alternativo, y puede ser útil si estás intentando comercializar con usuarios anónimos que no se han registrado o creado una cuenta en tu aplicación.

Si estás cargando o actualizando perfiles de usuario que son sólo alias, debes tener las dos columnas siguientes en tu CSV:

- `user_alias_name`: Un identificador único de usuario; una alternativa al `external_id`
- `user_alias_label`: Una etiqueta común para agrupar los alias de usuario

| user_alias_name | user_alias_label | last_name | correo electrónico | sample_attribute |
| --- | --- | --- | --- | --- |
| 182736485 | my_alt_identifier | Smith | smith@user.com | TRUE |
| 182736486 | my_alt_identifier | Nguyen | nguyen@user.com | FALSO |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Cuando proporciones tanto un `user_alias_name` como un `user_alias_label` en tu importación, Braze actualizará cualquier usuario existente con el mismo `user_alias_name` y `user_alias_label`. Si no se encuentra un usuario, Braze creará un usuario recién identificado con esa configuración `user_alias_name`.

{% alert important %}
No puedes utilizar una importación en CSV para actualizar un usuario existente con un `user_alias_name` si ya tiene un `external_id`. En su lugar, se creará un nuevo perfil de usuario con la dirección `user_alias_name` asociada. Para asociar un usuario de solo alias con un `external_id`, utiliza el [punto final Identificar usuarios]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/).
{% endalert %}

- **Descargar:** [Plantilla de importación de atributos de alias CSV][template_alias_attributes]
- **Descargar:** [Plantilla de importación de eventos de alias CSV][template_alias_events]

### Importar con Braze ID

Para actualizar perfiles de usuario existentes en Braze utilizando un valor interno de ID de Braze en lugar de un valor de `external_id` o `user_alias_name` y `user_alias_label`, especifica `braze_id` como cabecera de columna.

Esto puede ser útil si has exportado datos de usuario desde Braze a través de nuestra opción de exportación CSV dentro de la segmentación y quieres añadir un nuevo atributo personalizado a esos usuarios existentes.

{% alert important %}
No puedes utilizar una importación en CSV para crear un nuevo usuario utilizando `braze_id`. Este método sólo puede utilizarse para actualizar usuarios preexistentes dentro de la plataforma Braze.
{% endalert %}

{% alert tip %}
El valor `braze_id` podría etiquetarse como `Appboy ID` en las exportaciones CSV desde el panel de Braze. Este ID será el mismo que el de `braze_id` para un usuario, así que puedes cambiar el nombre de esta columna a `braze_id` cuando vuelvas a importar el CSV.
{% endalert %}

### Importar atributos predeterminados

Para importar atributos predeterminados para los usuarios, ve a **Importar usuarios** > **Atributos**. Los atributos predeterminados de usuario son claves reservadas en Braze. Por ejemplo, `first_name` o `email`. Los atributos personalizados se adaptan a tu empresa. Por ejemplo, una aplicación de reserva de viajes puede tener un atributo personalizado llamado `last_destination_searched`.

{% alert important %}
Al importar datos de clientes como atributos, las cabeceras de columna que utilices deben coincidir exactamente con la ortografía y las mayúsculas de los atributos de usuario predeterminados. De lo contrario, Braze creará automáticamente un atributo personalizado en el perfil de ese usuario.
{% endalert %}

#### Encabezados de columna de datos de usuario predeterminados

| CAMPO DE PERFIL DE USUARIO | TIPO DE DATOS | INFORMACIÓN | REQUIRED |
|---|---|---|---|
| `external_id` | Cadena | Un identificador de usuario único para tu cliente. | Sí, consulta la [nota siguiente](#about-external-ids). |
| `user_alias_name` | Cadena | Un identificador de usuario único para usuarios anónimos. Una alternativa a la `external_id`. | No, consulta la [nota siguiente](#about-external-ids). |
| `user_alias_label` | Cadena | Una etiqueta común para agrupar los alias de usuario. | Sí, si se utiliza `user_alias_name`. |
| `first_name` | Cadena | El nombre de pila de tus usuarios tal y como ellos lo han indicado (por ejemplo, `Jane`). | No |
| `last_name` | Cadena | El apellido de tus usuarios tal y como ellos lo han indicado (por ejemplo, `Doe`). | No |
| `email` | Cadena | El correo electrónico de tus usuarios tal y como ellos lo han indicado (por ejemplo, `jane.doe@braze.com`). | No |
| `country` | Cadena | Los códigos de país deben pasarse a Braze en la norma ISO-3166-1 alfa-2 (por ejemplo, `GB`). | No |
| `dob` | Cadena | Debe pasarse en el formato "AAAA-MM-DD" (por ejemplo, `1980-12-21`). Esto importará la fecha de nacimiento de tu usuario y te habilitará para dirigirte a usuarios cuya fecha de cumpleaños sea "hoy". | No |
| `gender` | Cadena | "M", "F", "O" (otro), "N" (no aplicable), "P" (prefiero no decirlo) o nulo (desconocido). | No |
| `home_city` | Cadena | La ciudad de residencia de tus usuarios tal y como ellos la han indicado (por ejemplo, `London`). | No |
| `language` | Cadena | El idioma debe pasarse a Braze en la norma ISO-639-1 (por ejemplo, `en`). <br>Consulta nuestra [lista de idiomas aceptados][1]. | No |
| `phone` | Cadena | Un número de teléfono indicado por tus usuarios, en formato `E.164` (por ejemplo, `+442071838750`). <br> Consulta [Números de teléfono de usuario][2] para obtener orientación sobre el formato. | No |
| `email_open_tracking_disabled` | Booleano | verdadero o falso aceptado.  Establécelo como verdadero para desactivar que el píxel de seguimiento de apertura se añada a todos los futuros correos electrónicos enviados a este usuario.   | No |
| `email_click_tracking_disabled` | Booleano | verdadero o falso aceptado.  Establécelo como verdadero para desactivar el seguimiento de clics de todos los enlaces de un futuro correo electrónico enviado a este usuario. | No |
| `email_subscribe` | Cadena | Los valores disponibles son `opted_in` (se ha registrado explícitamente para recibir mensajes de correo electrónico), `unsubscribed` (se ha excluido explícitamente de recibir mensajes de correo electrónico) y `subscribed` (ni se ha registrado ni se ha excluido). | No |
| `push_subscribe` | Cadena | Los valores disponibles son `opted_in` (se ha registrado explícitamente para recibir mensajes push), `unsubscribed` (se ha excluido explícitamente de los mensajes push) y `subscribed` (ni se ha aceptado ni se ha excluido). | No |
| `time_zone` | Cadena | La zona horaria debe pasarse a Braze en el mismo formato que la base de datos de zonas horarias de IANA (por ejemplo, `America/New_York` o `Eastern Time (US & Canada)`).  | No |
| `date_of_first_session` <br><br> `date_of_last_session`| Cadena | Puede pasarse en uno de los siguientes formatos ISO-8601: {::nomarkdown} <ul> <li> "AAAA-MM-DD" </li> <li> "YYYY-MM-DDTHH:MM:SS+00:00" </li> <li> "AAAA-MM-DDTHH:MM:SSZ" </li> <li> "AAAA-MM-DDTHH:MM:SS" (por ejemplo, 2019-11-20T18:38:57) </li> </ul> {:/} | No |
| `subscription_group_id` | Cadena | La dirección `id` de tu grupo de suscripción. Este identificador se encuentra en la página del grupo de suscripción de tu panel. | No |
| `subscription_state` | Cadena | El estado de suscripción para el grupo de suscripción especificado por `subscription_group_id`. Los valores permitidos son `unsubscribed` (no en el grupo de suscripción) o `subscribed` (en el grupo de suscripción). | No, pero se recomienda encarecidamente si se utiliza `subscription_group_id`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

##### Acerca de los ID externos

Aunque `external_id` no es obligatorio, **debes** incluir uno de estos campos: 
- `external_id`: Un identificador de usuario único para tu cliente, **o**
- `braze_id`: Un identificador de usuario único extraído para los usuarios existentes de Braze, **o bien**
- `user_alias_name` y `user_alias_label`: Un identificador único de usuario para un usuario anónimo

### Importar atributos personalizados

Puedes importar atributos personalizados para los usuarios yendo a **Importar usuarios** > **Atributos**. Cualquier encabezado que no coincida exactamente con los atributos predeterminados crea un atributo personalizado dentro de Braze.

En la importación de usuarios se aceptan los siguientes tipos de datos:

| Tipo de datos | Descripción |
|-----------|-------------|
| Fecha y hora | Debe almacenarse en formato ISO-8601 |
| Booleano | VERDADERO o FALSO |
| Número | Entero o flotante sin espacios ni comas, los flotantes deben usar un punto (.) como separador decimal |
| Cadena | Puede contener comas siempre que haya comillas dobles alrededor del valor de la columna |
| En blanco | Los valores en blanco no sobrescribirán los valores existentes en el perfil de usuario, y no es necesario que incluyas todos los atributos de usuario existentes en tu archivo CSV |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Las matrices y los tokens de notificaciones push no son compatibles con la importación de usuarios. Especialmente en el caso de las matrices, las comas de tu archivo CSV se interpretarán como un separador de columnas, por lo que cualquier coma en los valores provocará errores al analizar el archivo. <br>Para cargar este tipo de valores, utiliza el [punto final `/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) o [la Ingesta de datos en la nube]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/).
{% endalert %}

### Actualización del estado del grupo de suscripción

Puedes añadir usuarios a grupos de suscripción por correo electrónico o SMS mediante la importación de usuarios. Esto es especialmente útil para los SMS, porque un usuario debe estar inscrito en un grupo de suscripción SMS para recibir mensajes con el canal SMS. Para más información, consulta [Grupos de suscripción por SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement).

Si estás actualizando el estado del grupo de suscripción, debes tener las dos columnas siguientes en tu CSV:

- `subscription_group_id`: La dirección `id` del [grupo de suscripción]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups).
- `subscription_state`: Los valores disponibles son `unsubscribed` (no en el grupo de suscripción) o `subscribed` (en el grupo de suscripción).

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">external_id</th>
    <th class="tg-0pky">first_name</th>
    <th class="tg-0pky">subscription_group_id</th>
    <th class="tg-0pky">subscription_state</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">A8i3mkd99</td>
    <td class="tg-0pky">Colby</td>
    <td class="tg-0pky">6ff593d7-cf69-448b-aca9-abf7d7b8c273</td>
    <td class="tg-0pky">suscrito</td>
  </tr>
  <tr>
    <td class="tg-0pky">k2LNhj8Ks</td>
    <td class="tg-0pky">Tom</td>
    <td class="tg-0pky">aea02307-a91e-4bc0-abad-1c0bee817dfa</td>
    <td class="tg-0pky">suscrito</td>
  </tr>
</tbody>
</table>

{% alert important %}
Sólo se puede configurar un único `subscription_group_id` por fila en la importación de usuarios. Diferentes filas pueden tener diferentes valores `subscription_group_id`. Sin embargo, si necesitas inscribir a los mismos usuarios en varios grupos de suscripción, tendrás que hacer varias importaciones.
{% endalert %}

### Importar eventos personalizados (acceso anticipado) {#importing-custom-events}

{% alert important %}
La importación de eventos personalizados está actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en el acceso anticipado.
{% endalert %}

Para importar eventos personalizados para tus usuarios, ve a **Importar usuarios** > Eventos **.**

Los eventos personalizados se adaptan a tu negocio. Por ejemplo, una aplicación de streaming puede tener un evento personalizado llamado película_alquilada. Tu CSV debe tener cabeceras de columna para:

- Una de las siguientes:
  - `external_id`**o**
  - `braze_id`**o** 
  - `user_alias_name` y `user_alias_label`
- Nombre
- Tiempo

Los eventos personalizados pueden tener propiedades del evento. Por ejemplo, el evento personalizado película_alquilada puede tener las propiedades título y género. Estas propiedades del evento deben tener una cabecera de columna `<event_name>.properties.<property name>`. Un ejemplo es `rented_movie.properties.title`.

| CAMPO DE PERFIL DE USUARIO                      | TIPO DE DATOS | INFORMACIÓN                                                                                                                                                                                                             | REQUIRED                                                                                        |
|-----------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| `external_id`                           | Cadena    | Un identificador único para tu usuario.                                                                                                                                                                                 | Sí, se requiere uno de `external_id`, `braze_id`, o `user_alias_name` y `user_alias_label`. |
| `braze_id`                              | Cadena    | Un identificador Braze asignado a tu usuario.                                                                                                                                                                              | Sí, se requiere uno de `external_id`, `braze_id`, o `user_alias_name` y `user_alias_label`. |
| `user_alias_name`                       | Cadena    | Un identificador de usuario único para usuarios anónimos. Una alternativa al external_id.                                                                                                                                        | Sí, se requiere uno de `external_id`, `braze_id`, o `user_alias_name` y `user_alias_label`. |
| `user_alias_label`                      | Cadena    | Una etiqueta común para agrupar los alias de usuario.                                                                                                                                                                          | Sí, se requiere uno de `external_id`, `braze_id`, o `user_alias_name` y `user_alias_label`. |
| `name`                                  | Cadena    | Un evento personalizado de tus usuarios.                                                                                                                                                                                           | Sí                                                                                             |
| `time`                                  | Cadena    | La hora del evento. Puede pasarse en uno de los siguientes formatos ISO-8601: {::nomarkdown} <ul> <li> "AAAA-MM-DD" </li> <li> "YYYY-MM-DDTHH:MM:SS+00:00" </li> <li> "AAAA-MM-DDTHH:MM:SSZ" </li> <li> "AAAA-MM-DDTHH:MM:SS" (por ejemplo, 2019-11-20T18:38:57) </li> </ul> {:/} | Sí                                                                                             |
| `<event name>.properties.<property name>` | Múltiples  | Una propiedad de evento asociada a un evento personalizado. Un ejemplo es `rented_movie.properties.title`                                                                                                                        | No                                                                                              |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Aunque external_id en sí no es obligatorio, debes incluir uno de los siguientes campos: <br>- `external_id`: Un identificador de usuario único para tu cliente <br>- `braze_id`: Un identificador de usuario único extraído para los usuarios existentes de Braze <br>- `user_alias_name`: Un identificador único de usuario para un usuario anónimo
{% endalert %}

#### Tamaño del CSV

Braze acepta datos de usuario en formato CSV estándar de archivos de hasta 500 MB de tamaño. Para descargar una de nuestras plantillas de archivos CSV, consulta [Importar con ID externo](#importing-with-external-id) o [Importar con alias de usuario](#importing-with-user-alias).

#### Consideraciones sobre el punto de datos

Cada dato de clientes importado mediante CSV sobrescribirá el valor existente en los perfiles de usuario y contará como un punto de datos, excepto los ID externos y los valores en blanco.

- Los ID externos cargados mediante importación CSV no consumirán puntos de datos. Si estás cargando un archivo CSV para segmentar a los usuarios existentes de Braze cargando sólo ID externos, esto puede hacerse sin consumir puntos de datos. Si añadieras datos adicionales como el correo electrónico o el número de teléfono de un usuario en tu importación, eso sobrescribiría los datos de usuario existentes y consumiría tus puntos de datos.
    - Las importaciones CSV con fines de segmentación (importaciones realizadas con `external_id`, `braze_id`, o `user_alias_name` como único campo) no consumirán puntos de datos.
- Los valores en blanco no sobrescribirán los valores existentes en el perfil de usuario, y no es necesario que incluyas todos los atributos de usuario o eventos personalizados existentes en tu archivo CSV.
- La actualización de `email_subscribe`, `push_subscribe`, `subscription_group_id` o `subscription_state` no contará para el consumo de puntos de datos.

{% alert important %}
Configurar el idioma o el país de un usuario mediante la importación en CSV o la API impedirá que Braze capture automáticamente esta información a través del SDK.
{% endalert %}

## Importar un CSV

Para importar tu archivo CSV:
1. Ve a **Audiencia** > **Importar usuarios**. 
2. Selecciona **Examinar archivos** y selecciona el archivo que te interese, luego selecciona **Iniciar importación**. Braze cargará tu archivo y comprobará las cabeceras de las columnas, así como los tipos de datos de cada columna.

{% alert important %}
Las importaciones CSV distinguen entre mayúsculas y minúsculas. Esto significa que las mayúsculas en las importaciones de CSV escribirán el campo como un atributo personalizado en lugar de uno estándar. Por ejemplo, "correo electrónico" es correcto, pero "Correo electrónico" se escribiría como un atributo personalizado.
{% endalert %}

![Se selecciona la opción "Eventos" como tipo de información de usuario a importar.][5]

Una vez finalizada la carga, puedes ver una vista previa del contenido de tu archivo. La información de la tabla se basa en los valores de las filas superiores de tu archivo CSV.

Puedes hacer un seguimiento del progreso en la página **Importar usuarios**, que se actualiza cada cinco segundos, o cuando seleccionas **Actualizar tabla**. Puedes seguir utilizando el resto del panel Braze durante la importación, y recibirás notificaciones cuando comience y termine la importación.

También puedes ver tus importaciones más recientes, sus nombres de archivo, el tipo de CSV, el número de líneas del archivo, el número de líneas importadas con éxito, el total de líneas de cada archivo y el estado de cada importación.

Puedes importar más de un archivo CSV al mismo tiempo. Las importaciones de CSV se ejecutarán simultáneamente, lo que significa que no se garantiza que el orden de las actualizaciones sea en serie. Si necesitas que las importaciones de CSV se ejecuten una tras otra, debes esperar a que una importación de CSV haya finalizado antes de cargar una segunda.

Si el proceso de importación se encuentra con un error, aparecerá un icono de advertencia junto al número total de líneas del archivo. Puedes pasar el ratón por encima del icono para ver detalles sobre por qué fallaron determinadas líneas. Una vez finalizada la importación, todos los datos se añadirán a los perfiles existentes, o se crearán nuevos perfiles.

![La carga del archivo CSV se completó con errores relacionados con tipos de datos mezclados en una sola columna][4]{: style="max-width:70%"}

### Consideraciones

Si Braze detecta algo malformado en las filas superiores de tu archivo durante la carga, estos errores se mostrarán con el resumen. Por ejemplo, si tu archivo incluye una fila mal formada, este error se anotará en la vista previa cuando importes el archivo. Aunque un archivo puede importarse con errores, se recomienda que los corrijas antes de continuar con la importación.

Además, es importante examinar el archivo CSV completo antes de cargarlo, ya que Braze no escanea cada fila del archivo de entrada para la vista previa. Esto significa que pueden existir errores que Braze no detecta al generar esta vista previa.

Las filas malformadas y las que carezcan de ID externo no se importarán. Todos los demás errores pueden importarse, pero pueden interferir en el filtrado al crear un segmento. Para más información, pasa a la sección [Solución de problemas](#troubleshooting).

{% alert warning %}
Los errores se basan únicamente en el tipo de datos y la estructura del archivo. Por ejemplo, una dirección de correo electrónico mal formateada seguiría importándose, ya que aún puede analizarse como una cadena.
{% endalert %}

### Importación de usuarios Lambda en CSV

Puedes utilizar nuestro script de importación CSV de S3 Lambda sin servidor para cargar atributos de usuario en la plataforma. Esta solución funciona como un cargador de CSV en el que depositas tus CSV en un contenedor de S3, y los scripts los cargan a través de nuestra API.

Los tiempos de ejecución estimados para un fichero con un millón de filas deberían ser de unos cinco minutos. Para más información, consulta [Importación de atributos de usuario en CSV a Braze]({{site.baseurl}}/user_csv_lambda/).

## Segmentación

La importación de usuarios crea y actualiza perfiles de usuarios, y también puede utilizarse para crear segmentos. Para crear un segmento, selecciona **Generar automáticamente un segmento a partir de los usuarios importados de este CSV** antes de iniciar la importación.

Puedes establecer el nombre del segmento o aceptar el predeterminado, que es el nombre de tu archivo. Los archivos que se utilizaron para crear un segmento tendrán un enlace para ver el segmento una vez finalizada la importación.

El filtro utilizado para crear el segmento selecciona a los usuarios que se crearon o actualizaron en una importación seleccionada y está disponible con todos los demás filtros en la página de edición de segmentos.

## Solución de problemas {#troubleshooting}

### Filas que faltan

Hay algunas razones por las que el número de usuarios importados puede no coincidir con el total de filas de tu archivo CSV:

- **Duplicar ID externos:** Si hay columnas ID externas duplicadas, esto puede provocar filas mal formadas o no importadas, aunque las filas estén formateadas correctamente. En algunos casos puede que no informe de un error concreto. Comprueba si hay ID externos duplicados en tu CSV. Si es así, elimina los duplicados e intenta subirlos de nuevo.
- **Caracteres acentuados:** Tu archivo CSV puede tener nombres o atributos que incluyan acentos. Asegúrate de que tu archivo está codificado en UTF-8 para evitar problemas.

### Fila malformada

Debes incluir una fila de encabezado en tu archivo CSV para importar correctamente tus datos. Cada fila debe tener el mismo número de celdas que la fila de cabecera. Las filas con una longitud de más o menos valores que la fila de cabecera se excluirán de la importación. Las comas en un valor se interpretarán como un separador y pueden provocar este error. Además, todos los datos deben estar codificados en UTF-8.

Si tu archivo CSV tiene filas en blanco e importa menos filas que el total de líneas del archivo CSV, puede que esto no indique un problema con la importación, ya que no sería necesario importar las filas en blanco. Comprueba el número de líneas que se importaron correctamente y asegúrate de que coincide con el número de usuarios que intentas importar.

### Múltiples tipos de datos

Braze espera que cada valor de una columna sea del mismo tipo de datos. Los valores que no coincidan con el tipo de datos de su atributo provocarán errores en la segmentación.

### Fechas con formato incorrecto

Las fechas que no estén en formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) no se leerán como fechas en la importación.

### Cita de cadena

Los valores entre comillas simples ('') o dobles ("") se leerán como cadenas en la importación.

### Datos importados como atributo personalizado

Si ves un dato de usuario predeterminado (por ejemplo, `email` o `first_name`) importado como atributo personalizado, comprueba las mayúsculas y minúsculas y el espaciado de tu archivo CSV. Por ejemplo, `First_name` se importaría como un atributo personalizado, mientras que `first_name` se importaría correctamente en el campo "nombre" del perfil de un usuario.

[import_template]: {% image_buster /assets/download_file/braze-user-import-template-csv.xlsx %}
[events_template]: {% image_buster /assets/download_file/braze-csv-events-import-template.csv %}
[template_alias_attributes]: {% image_buster /assets/download_file/braze-user-import-alias-template-csv.xlsx %}
[template_alias_events]: {% image_buster /assets/download_file/braze-events-csv-example-user-alias.csv %}
[errors]:#common-errors
[1]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/
[12]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[13]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[14]: {{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/
[3]: {% image_buster /assets/img/importcsv5.png %}
[4]: {% image_buster /assets/img/importcsv2.png %}
[5]: {% image_buster /assets/img/importcsv3.png %}
[7]: {% image_buster /assets/img/segment-imported-users.png %}
[8]: {% image_buster /assets/img_archive/user_alias_import_1.png %}
[9]: {% image_buster /assets/img/subscription_group_import.png %}