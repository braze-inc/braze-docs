---
nav_title: Importación de usuarios
article_title: Importación de usuarios
page_order: 4
page_type: reference
description: "Este artículo de referencia explica cómo importar usuarios a tu panel de Braze utilizando la API REST, la ingesta de datos en la nube, CSV y las buenas prácticas de importación."

---
# Importación de usuarios

> Braze ofrece diversas formas de importar los datos de los usuarios a la plataforma: SDK, API, ingesta de datos en la nube, integraciones de socios tecnológicos y archivos CSV.

Antes de continuar, nota que Braze no sanea (valida o formatea correctamente) los datos HTML durante la importación. Esto significa que las etiquetas de script deben eliminarse de todos los datos de importación destinados a la personalización web.

Al importar datos a Braze destinados específicamente al uso de personalización en un navegador web, asegúrese de que estén desprovistos de HTML, JavaScript o cualquier otra etiqueta de secuencia de comandos que pueda ser aprovechada de forma malintencionada al visualizarse en un navegador web.  

Alternativamente, para HTML, puedes utilizar los filtros Braze Liquid (`strip_html`) para escapar caracteres HTML del texto representado. Por ejemplo:

{% tabs local %}
{% tab Entrada %}
{% raw %}
```liquid
{{ "Have <em>you</em> read <strong>Ulysses</strong>?" | strip_html }}
```
{% endraw %}
{% endtab %}
{% tab Salida %}
{% raw %}
```liquid
Have you read Ulysses?
```
{% endraw %}
{% endtab %}
{% endtabs %}

## API REST

Utiliza el punto final [`/users/track`][12] para registrar eventos personalizados, atributos de usuario y compras de usuarios.

## Ingesta de datos de Cloud

Utiliza Braze [Ingesta de datos en la nube][14] para importar y mantener los atributos de los usuarios. 

## Importación CSV

Puedes subir y actualizar perfiles de usuario mediante archivos CSV desde **Audiencia** > Importar **usuarios.**

La importación de CSV permite registrar y actualizar atributos de usuario como el nombre y el correo electrónico, además de atributos personalizados como la talla de calzado. Puede importar un CSV especificando uno de los dos identificadores únicos de usuario: un `external_id` o un alias de usuario.

{% alert note %}
Si estás cargando una mezcla de usuarios con `external_id` y usuarios sin , necesitas crear un CSV para cada importación. Un CSV no puede contener tanto `external_ids` como alias de usuario.
{% endalert %}

### Creación del CSV

Existen varios tipos de datos en Braze. Al importar o actualizar perfiles de usuario con un archivo CSV, puede crear o actualizar atributos de usuario predeterminados o atributos personalizados.

- Los atributos de usuario por defecto son claves reservadas en Braze. Por ejemplo, `first_name` o `email`.
- Los atributos personalizados se adaptan a su empresa. Por ejemplo, una aplicación de reservas de viajes puede tener un atributo personalizado llamado `last_destination_searched`.

{% alert important %}
Al importar datos de clientes, los encabezados de columna que utilice deben coincidir exactamente con la ortografía y las mayúsculas de los atributos de usuario predeterminados. De lo contrario, Braze creará automáticamente un atributo personalizado en el perfil de ese usuario.
{% endalert %}

Braze acepta datos de usuario en formato CSV estándar de archivos de hasta 500 MB de tamaño. Consulte las secciones anteriores sobre importación para descargar plantillas CSV.

#### Consideraciones sobre los puntos de datos

Cada dato de cliente importado de un archivo CSV sobrescribirá el valor existente en los perfiles de usuario y contará como un punto de datos, excepto los ID externos y los valores en blanco. 

- Los ID externos cargados desde un archivo CSV no consumirán puntos de datos. Si está cargando un CSV para segmentar usuarios Braze existentes cargando sólo ID externos, puede hacerlo sin consumir puntos de datos. Si tuviera que añadir datos adicionales como correos electrónicos o números de teléfono de usuarios en su importación, eso sobrescribiría los datos de usuarios existentes, consumiendo sus puntos de datos.
  - Las importaciones CSV con fines de segmentación (importaciones realizadas con `external_id`, `braze_id`, o `user_alias_name` como único campo) no consumirán puntos de datos.
- Los valores en blanco no sobrescribirán los valores existentes en el perfil de usuario, y no es necesario que incluya todos los atributos de usuario existentes en su archivo CSV.
- La actualización de `email_subscribe`, `push_subscribe`, `subscription_group_id` o `subscription_state` no contará para el consumo de puntos de datos.

{% alert important %}
Establecer `language` o `country` en un usuario a través de la importación CSV o API evitará que Braze capture automáticamente esta información a través del SDK.
{% endalert %}

#### Encabezados de columna de datos de usuario por defecto

| CAMPO DE PERFIL DE USUARIO | TIPO DE DATOS | INFORMACIÓN | REQUIRED |
|---|---|---|---|
| `external_id` | Cadena | Un identificador de usuario único para su cliente. | Sí, véase la nota siguiente |
| `user_alias_name` | Cadena | Un identificador de usuario único para usuarios anónimos. Una alternativa a `external_id`. | No, véase la nota siguiente |
| `user_alias_label` | Cadena | Una etiqueta común para agrupar los alias de usuario. | Sí, si se utiliza `user_alias_name`  |
| `first_name` | Cadena | El nombre de pila de sus usuarios tal y como lo han indicado (por ejemplo, `Jane`). | No |
| `last_name` | Cadena | El apellido de sus usuarios tal y como lo han indicado (por ejemplo, `Doe`). | No |
| `email` | Cadena | El correo electrónico de sus usuarios tal y como lo han indicado (por ejemplo, `jane.doe@braze.com`). | No |
| `country` | Cadena | Los códigos de país deben pasarse a Braze en la norma ISO-3166-1 alfa-2 (por ejemplo, `GB`). | No |
| `dob` | Cadena | Debe introducirse en el formato "AAAA-MM-DD" (por ejemplo, `1980-12-21`). Esto importará la fecha de nacimiento de su usuario y le permitirá dirigirse a usuarios cuyo cumpleaños sea "hoy". | No |
| `gender` | Cadena | "M", "F", "O" (otro), "N" (no aplicable), "P" (prefiere no decirlo) o nil (desconocido). | No |
| `home_city` | Cadena | La ciudad de residencia de sus usuarios tal y como la han indicado (por ejemplo, `London`). | No |
| `language` | Cadena | El idioma debe pasarse a Braze en la norma ISO-639-1 (por ejemplo, `en`). <br>Consulta nuestra [lista de idiomas aceptados][1]. | No |
| `phone` | Cadena | Un número de teléfono indicado por sus usuarios, en formato `E.164` (por ejemplo, `+442071838750`). <br> Consulte [Números de teléfono de usuario][2] para obtener orientación sobre el formato. | No |
| `email_open_tracking_disabled` | Booleano | verdadero o falso aceptado.  Establézcalo en true para desactivar que el píxel de seguimiento de apertura se añada a todos los futuros correos electrónicos enviados a este usuario.   | No |
| `email_click_tracking_disabled` | Booleano | verdadero o falso aceptado.  Establecer en true para desactivar el seguimiento de clics para todos los enlaces dentro de un futuro correo electrónico, enviado a este usuario. | No |
| `email_subscribe` | Cadena | Los valores disponibles son `opted_in` (inscrito explícitamente para recibir mensajes de correo electrónico), `unsubscribed` (excluido explícitamente de recibir mensajes de correo electrónico) y `subscribed` (ni inscrito ni excluido). | No |
| `push_subscribe` | Cadena | Los valores disponibles son `opted_in` (se ha registrado explícitamente para recibir mensajes push), `unsubscribed` (se ha excluido explícitamente de los mensajes push) y `subscribed` (ni se registró ni se excluyó). | No |
| `time_zone` | Cadena | La zona horaria debe pasarse a Braze en el mismo formato que la base de datos de zonas horarias de IANA (por ejemplo, `America/New_York` o `Eastern Time (US & Canada)`).  | No |
| `date_of_first_session` <br><br> `date_of_last_session`| Cadena | Puede transmitirse en uno de los siguientes formatos ISO 8601: {::nomarkdown} <ul> <li> "AAAA-MM-DD" </li> <li> "YYYY-MM-DDTHH:MM:SS+00:00" </li> <li> "AAAA-MM-DDTHH:MM:SSZ" </li> <li> "AAAA-MM-DDTHH:MM:SS" (por ejemplo, 2019-11-20T18:38:57) </li> </ul> {:/} | No |
| `subscription_group_id` | Cadena | La dirección `id` de su grupo de suscripción. Este identificador se encuentra en la página del grupo de suscripción de su panel de control. | No |
| `subscription_state` | Cadena | El estado de suscripción para el grupo de suscripción especificado por `subscription_group_id`. Los valores permitidos son `unsubscribed` (no en el grupo de suscripción) o `subscribed` (en el grupo de suscripción). | No, pero se recomienda encarecidamente si se utiliza `subscription_group_id`  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Aunque `external_id` en sí no es obligatorio, **debes** incluir uno de estos campos:
- `external_id`: Un identificador de usuario único para su cliente <br> \- O -
- `braze_id`: Un identificador de usuario único extraído para los usuarios existentes de Braze <br> \- O -
- `user_alias_name`: Un identificador de usuario único para un usuario anónimo
{% endalert %}

### Importar un CSV

Para importar tu archivo CSV, ve a **Audiencias** > **Importación de usuarios**. Aquí encontrará una tabla que enumera las importaciones más recientes, que incluye detalles como la fecha de carga, el nombre del cargador, el nombre del archivo, la disponibilidad de destino, el número de filas importadas y el estado de cada importación.

![La página "Importar usuarios" del panel de Braze.][3]

Seleccione **Examinar archivos** y su archivo. Braze cargará su archivo y comprobará los encabezados de columna y los tipos de datos de cada columna.

Para descargar una plantilla CSV, consulte las secciones [Importar con ID externo](#importing-with-external-id) o [Importar con alias de usuario](#importing-with-user-alias) en esta página.

{% alert important %}
Las importaciones CSV distinguen entre mayúsculas y minúsculas. Esto significa que las mayúsculas en las importaciones CSV escribirán el campo como un atributo personalizado en lugar de uno estándar. Por ejemplo, "email" es correcto, pero "Email" se escribiría como atributo personalizado.
{% endalert %}

Una vez completada la carga, verás un modal con una vista previa del contenido de tu archivo. Toda la información de esta tabla se basa en los valores de las primeras filas de su archivo CSV. En las cabeceras de columna, los atributos estándar se escriben en texto normal, mientras que los atributos personalizados aparecen en cursiva y su tipo se indica entre paréntesis. También hay un resumen de su expediente en la parte superior de la ventana emergente.

Puede importar más de un CSV al mismo tiempo. Las importaciones de CSV se ejecutan simultáneamente, por lo que no se garantiza que el orden de las actualizaciones sea en serie. Si necesita que las importaciones CSV se ejecuten una tras otra, espere a que una importación CSV haya finalizado antes de cargar una segunda.

Si Braze detecta algo malformado en tu archivo durante la carga, estos errores se mostrarán con el resumen. Por ejemplo, si su archivo incluye una fila mal formada, ese error se observa en la vista previa al importar el archivo. Así, un archivo puede importarse con errores, pero una importación no puede cancelarse o revertirse una vez iniciada. Revise la vista previa y, si encuentra algún error, cancele la importación y modifique su archivo. 

{% alert important %}
Examine el archivo CSV completo antes de cargarlo, ya que Braze no escanea todas las filas del archivo de entrada para la vista previa. Esto significa que pueden existir errores que Braze no detecta al generar esta vista previa.
{% endalert %}

Las filas malformadas y las que carecen de ID externo no se importarán. Todos los demás errores pueden importarse, pero pueden interferir con el filtrado al crear un segmento. Para más información, pasa a la sección [Solución de problemas](#troubleshooting).

![Carga de CSV completada con errores relacionados con tipos de datos mixtos en una sola columna][4]{: style="max-width:70%"}

{% alert warning %}
Los errores se basan únicamente en el tipo de datos y la estructura del archivo. Por ejemplo, una dirección de correo electrónico mal formateada podría importarse, ya que aún puede analizarse como una cadena.
{% endalert %}

Cuando estés satisfecho con la carga, inicia la importación. La ventana emergente se cerrará y la importación comenzará en segundo plano. Puede seguir su progreso en la página **Importación de usuarios**, que se actualizará cada cinco segundos, o pulsando el botón de actualización del cuadro **Importaciones recientes**.

Bajo **Líneas procesadas** se muestra el progreso de la importación; el estado cambiará a **Completo** cuando haya finalizado. Puedes seguir utilizando el resto del panel de control de Braze durante la importación, y recibirás notificaciones cuando comience y termine la importación.

Si el proceso de importación se topa con un error, aparecerá un icono amarillo de advertencia junto al número total de líneas del archivo. Puede pasar el ratón por encima del icono para ver detalles sobre por qué fallaron determinadas líneas. Una vez finalizada la importación, todos los datos se añadirán a los perfiles existentes o se crearán perfiles nuevos.

### Importación con ID externo

Al importar tus datos de clientes, tendrás que especificar el identificador único de cada cliente (`external_id`). Antes de iniciar la importación de CSV, es importante que su equipo de ingeniería sepa cómo se identificarán los usuarios en Braze. Normalmente, se trata de un ID interno de la base de datos. Esto debería alinearse con la forma en que los usuarios serán identificados por el SDK Braze en móviles y web y está diseñado para que cada cliente tenga un único perfil de usuario dentro de Braze en todos sus dispositivos. Más información sobre el [ciclo de vida del perfil de usuario][13] de Braze.

Cuando proporcione un `external_id` en su importación, Braze actualizará cualquier usuario existente con el mismo `external_id` o creará un nuevo usuario identificado con ese conjunto `external_id` si no se encuentra ninguno.

**Descargar:** [Plantilla de importación CSV][plantilla]

### Importación con alias de usuario

Para dirigirse a usuarios que no tienen un `external_id`, puede importar una lista de usuarios con alias de usuario. Un alias sirve como identificador de usuario único alternativo, y puede ser útil si estás intentando comercializar con usuarios anónimos que no se han registrado o creado una cuenta en tu aplicación.

Si está cargando o actualizando perfiles de usuario que son sólo alias, debe tener las dos columnas siguientes en su CSV:

- `user_alias_name`: Un identificador único de usuario; una alternativa al `external_id`
- `user_alias_label`: Una etiqueta común para agrupar los alias de usuario

| user_alias_name | user_alias_label | last_name | correo electrónico | sample_attribute |
| --- | --- | --- | --- | --- |
| 182736485 | my_alt_identifier | Smith | smith@user.com | TRUE |
| 182736486 | my_alt_identifier | Nguyen | nguyen@user.com | FALSO |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Cuando proporcione `user_alias_name` y `user_alias_label` en su importación, Braze actualizará cualquier usuario existente con los mismos `user_alias_name` y `user_alias_label`. Si no se encuentra un usuario, Braze creará un nuevo usuario identificado con ese conjunto `user_alias_name`.

{% alert important %}
No puede utilizar una importación CSV para actualizar un usuario existente con un `user_alias_name` si ya tiene un `external_id`. En su lugar, se creará un nuevo perfil de usuario con la dirección `user_alias_name` asociada. Para asociar un usuario de solo alias con un `external_id`, utiliza el [punto final Identificar usuarios]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/).
{% endalert %}

**Descargar:** [Plantilla de importación de alias CSV][template_alias]

### Importación con Braze ID

Para actualizar perfiles de usuario existentes en Braze utilizando un valor interno de ID de Braze en lugar de un valor de `external_id` o `user_alias_name` y `user_alias_label`, especifica `braze_id` como cabecera de columna.

Esto puede ser útil si has exportado datos de usuario desde Braze a través de nuestra opción de exportación CSV dentro de la segmentación y quieres añadir un nuevo atributo personalizado a esos usuarios existentes.

{% alert important %}
No se puede utilizar una importación CSV para crear un nuevo usuario utilizando `braze_id`. Este método sólo puede utilizarse para actualizar usuarios preexistentes en la plataforma Braze.
{% endalert %}

{% alert tip %}
El valor `braze_id` puede aparecer etiquetado como `Appboy ID` en las exportaciones CSV del cuadro de mandos Braze. Este ID será el mismo que el de `braze_id` para un usuario, por lo que puede cambiar el nombre de esta columna a `braze_id` cuando vuelva a importar el CSV.
{% endalert %}

### Importación con direcciones de correo electrónico y números de teléfono

Puedes omitir un ID externo o un alias de usuario y utilizar simplemente una dirección de correo electrónico o un número de teléfono para importar usuarios. Antes de importar un archivo CSV con direcciones de correo electrónico o números de teléfono, comprueba lo siguiente:

- Comprueba que no tienes ID externos ni alias de usuario para estos perfiles.
- Confirma que tu archivo CSV tiene el formato adecuado.

{% alert note %}
Si incluyes tanto direcciones de correo electrónico como números de teléfono en tu archivo CSV, la dirección de correo electrónico tendrá prioridad sobre el número de teléfono a la hora de buscar perfiles.
{% endalert %}

Si un perfil existente tiene esa dirección de correo electrónico o número de teléfono, ese perfil se actualizará, y Braze no creará un perfil nuevo. Si hay varios perfiles con esa misma dirección de correo electrónico, Braze utilizará la misma lógica que el [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), donde se actualizará el perfil actualizado más recientemente.

Si no existe un perfil con esa dirección de correo electrónico o número de teléfono, Braze creará un nuevo perfil con ese identificador. Puedes utilizar el [punto final`/users/identify` ]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) para identificar este perfil más adelante. Para eliminar un perfil de usuario, también puedes utilizar el punto final [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete).

### Importar datos personalizados

Cualquier encabezado que no coincida exactamente con los datos de usuario predeterminados creará un atributo personalizado dentro de Braze.

En la importación de usuarios se aceptan los siguientes tipos de datos:
- **Fecha y hora:** Debe almacenarse en formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 
- **Booleano:** `true` o `false`
- **Número:** Número entero o flotante sin espacios ni comas, los flotantes deben utilizar un punto (`.`) como separador decimal
- **Cadena:** Puede contener comas si hay comillas dobles (`""`) rodeando el valor de la columna
- **En blanco:** Los valores en blanco no sobrescribirán los valores existentes en el perfil de usuario, y no es necesario que incluyas todos los atributos de usuario existentes en tu archivo CSV

{% alert important %}
Las matrices, los tokens push y los tipos de datos de eventos personalizados no son compatibles con la importación de usuarios.
Especialmente en el caso de las matrices, las comas de tu archivo CSV se interpretarán como un separador de columnas, por lo que cualquier coma en los valores provocará errores al analizar el archivo.<br><br>Para cargar este tipo de valores, utiliza el [punto final `/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) o [la Ingesta de datos en la nube]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/).
{% endalert %}

### Importación de usuarios Lambda en CSV

Puede utilizar nuestro script de importación CSV de S3 Lambda sin servidor para cargar atributos de usuario en la plataforma. Esta solución funciona como un cargador de CSV en el que depositas tus CSV en un bucket de S3 y los scripts los cargan a través de nuestra API.

Los tiempos de ejecución estimados para un archivo con 1.000.000 de filas deberían rondar los cinco minutos. Consulte [Importación de atributos de usuario CSV a Braze]({{site.baseurl}}/user_csv_lambda/) para obtener más información.

### Actualización del estado del grupo de suscripción

Puede añadir usuarios a grupos de suscripción por correo electrónico o SMS mediante la importación de usuarios. Esto es especialmente útil para los SMS, ya que un usuario debe estar inscrito en un grupo de suscripción SMS para recibir mensajes con el canal SMS. Para más información, consulta [Grupos de suscripción por SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement).

Si está actualizando el estado del grupo de suscripción, debe tener las dos columnas siguientes en su CSV:

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
Sólo se puede establecer un único `subscription_group_id` por fila en la importación de usuarios. Diferentes filas pueden tener diferentes valores `subscription_group_id`. Sin embargo, si necesitas inscribir a los mismos usuarios en varios grupos de suscripción, tendrás que hacer varias importaciones.
{% endalert %}

## Crear segmentos a partir de una importación de usuarios

La importación de usuarios también puede utilizarse para crear segmentos seleccionando **Generar automáticamente un segmento a partir de los usuarios que se importan de este CSV** antes de iniciar la importación.

Puede establecer el nombre del segmento o aceptar el predeterminado, que es el nombre de su archivo. Los archivos que se utilizaron para crear un segmento tendrán un enlace para ver el segmento una vez finalizada la importación.

El filtro utilizado para crear el segmento selecciona los usuarios que se crearon o actualizaron en una importación seleccionada y está disponible con todos los demás filtros en la página de edición de segmentos.

## Consideraciones

{% multi_lang_include email-via-sms-warning.md %}

## Solución de problemas

### Filas que faltan

Existen varias razones por las que el número de usuarios importados puede no coincidir con el total de filas de su archivo CSV:

- **Duplicar ID externos:** Si hay columnas ID externas duplicadas, esto puede provocar filas mal formadas o no importadas, aunque las filas estén formateadas correctamente. En algunos casos, es posible que no se notifique un error concreto. Compruebe si hay ID externos duplicados en su CSV. Si es así, elimine los duplicados e intente cargarlos de nuevo.
- **Caracteres acentuados:** Su CSV puede tener nombres o atributos que incluyan acentos. Asegúrate de que tu archivo está codificado en UTF-8 para evitar problemas.

### Fila malformada

Debe haber una fila de encabezamiento para importar datos correctamente. Cada fila debe tener el mismo número de celdas que la fila de cabecera. Las filas con una longitud superior o inferior a la fila de cabecera se excluirán de la importación. Las comas en un valor se interpretarán como un separador y pueden provocar este error. Además, todos los datos deben estar codificados en UTF-8.

Si su archivo CSV tiene filas en blanco e importa menos filas que el total de líneas del archivo CSV, puede que esto no indique un problema con la importación, ya que no sería necesario importar las filas en blanco. Compruebe el número de líneas que se han importado correctamente y asegúrese de que coincide con el número de usuarios que está intentando importar.

### Múltiples tipos de datos

Braze espera que cada valor de una columna sea del mismo tipo de datos. Los valores que no coincidan con el tipo de datos de su atributo provocarán errores en la segmentación.

### Fechas con formato incorrecto

Las fechas que no estén en formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) no se leerán como `datetimes` en la importación.

### Cita de cadena

Los valores entre comillas simples (`''`) o dobles (`""`) se leerán como cadenas en la importación.

### Datos importados como atributo personalizado

Si un dato de usuario predeterminado (como `email` o `first_name`) se importa como atributo personalizado, comprueba las mayúsculas y minúsculas y el espaciado de tu archivo CSV. Por ejemplo, `First_name` se importaría como atributo personalizado, mientras que `first_name` se importaría correctamente en el campo "nombre" del perfil de un usuario.

[1]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/
[3]: {% image_buster /assets/img/importcsv5.png %}
[4]: {% image_buster /assets/img/importcsv2.png %}
[7]: {% image_buster /assets/img/segment-imported-users.png %}
[8]: {% image_buster /assets/img_archive/user_alias_import_1.png %}
[9]: {% image_buster /assets/img/subscription_group_import.png %}
[12]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[13]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[14]: {{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/
[errors]:#common-errors
[template]: {% image_buster /assets/download_file/braze-user-import-template-csv.xlsx %}
[template_alias]: {% image_buster /assets/download_file/braze-user-import-alias-template-csv.xlsx %}
