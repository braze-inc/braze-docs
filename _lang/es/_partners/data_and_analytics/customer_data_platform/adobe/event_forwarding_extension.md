---
nav_title: Extensión de reenvío de eventos
article_title: Adobe
description: "Este artículo de referencia cubre la extensión de reenvío de eventos Braze, que te permite aprovechar los datos capturados en la red Edge de Adobe Experience Platform y enviarlos a Braze en forma de eventos del lado del servidor."
page_type: partner
page_order: 2
search_tag: Partner

---

# Extensión de reenvío de eventos de la API Track Events

> La extensión de [reenvío de eventos](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/overview.html?lang=en) Braze Track Events API te permite aprovechar los datos capturados en Adobe Experience Platform Edge Network y enviarlos a Braze en forma de eventos del lado del servidor utilizando la [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) API.

Este documento cubre los casos de uso de la extensión, cómo instalarla en tus bibliotecas de reenvío de eventos y cómo emplear sus capacidades en una [regla de](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en) reenvío de eventos.

{% alert note %}
El envío de atributos a Braze puede aumentar el consumo de puntos de datos de Braze. Consulta con tu director de cuentas Braze antes de enviar atributos. Consulte la documentación de Braze sobre [puntos de datos facturables]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/#billable-data-points) para obtener más información.
{% endalert %}

## Casos prácticos

Esta ampliación debería utilizar los datos de la red Edge Network en Braze para aprovechar sus capacidades de análisis de clientes y segmentación.

Por ejemplo, considera una organización de comercio minorista con una presencia multicanal (sitio web y móvil) y que captura entradas transaccionales o conversacionales como datos de eventos de su sitio web y plataformas móviles. 

Utilizando varias reglas de [etiquetado](https://experienceleague.adobe.com/docs/experience-platform/tags/home.html?lang=en), estos datos se envían a la red Edge Network en tiempo real. A partir de aquí, la extensión de reenvío de eventos Braze envía automáticamente los eventos relevantes a Braze desde el lado del servidor.

## Límites de tarifa

| API | Límites de tarifa |
| --- | --- |
| Seguimiento del usuario | 50.000 solicitudes por minuto.<br><br>Consulte la [documentación de la API de seguimiento de usuarios]({{site.baseurl}}/api/endpoints/user_data/post_user_track#rate-limit) para obtener más información.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Recopilar los datos de configuración necesarios

Para conectar la red Edge Network a Braze, se necesita lo siguiente:

| Tipo de clave | Descripción |
| --- | --- |
| Instancia de soldadura | Puedes obtener tu instancia de Braze a través de tu administrador de incorporación a Braze o en la [página de resumen de la API]({{site.baseurl}}/api/basics/#endpoints). |
| Clave REST API de Braze | Una clave Braze REST API con todos los permisos. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Paso 2: Crear un secreto

Cree un nuevo [secreto de reenvío de eventos](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/secrets.html?lang=en) y establezca el valor en su [clave Braze API](https://experienceleague.adobe.com/docs/experience-platform/tags/extensions/server/braze/overview.html?lang=en#configuration-details). Esto se utilizará para autenticar la conexión a su cuenta manteniendo el valor seguro.

### Paso 3: Instalar y configurar la extensión Braze

1. Para instalar la extensión, [cree una propiedad de reenvío de eventos](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/overview.html?lang=en#properties) o elija una propiedad existente para editarla en su lugar.
2. A continuación, seleccione **Extensiones** en el menú de la izquierda. En la pestaña **Catálogo**, seleccione **Instalar** en la tarjeta para la extensión Braze.
3. En la siguiente pantalla, introduzca su instancia REST y su clave API y seleccione **Guardar** cuando haya terminado.

### Paso 4: Crear una regla de envío de eventos

Tras instalar la extensión, crea una nueva [regla ](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en) de reenvío de eventos y configura sus condiciones como desees. Al configurar las acciones para la regla, seleccione la extensión **Braze** y, a continuación, seleccione **Enviar evento** para el tipo de acción.

![]({% image_buster /assets/img/efe.png %})

{% tabs local %}
{% tab Identificación del usuario %}

| Entrada de datos | Descripción |
| --- | --- |
| ID de usuario externo | Un UUID o GUID largo, aleatorio y bien distribuido. Si eliges un método diferente para nombrar tus identificadores de usuario, también deben ser largos, aleatorios y estar bien distribuidos. Más información sobre [la convención de nomenclatura de ID de usuario sugerida]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids#suggested-user-id-naming-convention). |
| ID de usuario Braze | Identificador de usuario Braze. |
| Alias de usuario | Un alias sirve como identificador único alternativo del usuario. Utilice alias para identificar a los usuarios en dimensiones diferentes a su ID de usuario principal.<br><br>El objeto alias de usuario consta de dos partes: un `alias_name` para el propio identificador y un `alias_label` que indica el tipo de alias. Los usuarios pueden tener varios alias con etiquetas diferentes, pero sólo un `alias_name` por `alias_label`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Para vincular el evento a un usuario, debes rellenar el campo `External User ID`, el campo `Braze User Identifier` o la sección `User Alias`.
{% endalert %}

{% endtab %}
{% tab Datos del evento %}

| Entrada de datos | Descripción | Obligatoria |
| --- | --- | --- |
| Nombre de evento | Nombre del evento. | Sí |
| Hora del evento | Fecha-hora como cadena en formato ISO 8601 o en `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. | Sí |
| Identificador de la aplicación | El identificador de aplicación o `app_id` es un parámetro que asocia la actividad con una aplicación específica en su espacio de trabajo. Designa con qué aplicación del espacio de trabajo estás interactuando. | No |
| Propiedades del evento | Un objeto JSON que contiene propiedades personalizadas del evento. | No |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
La acción **Enviar evento de Braze** sólo requiere que se especifique un **Nombre de evento** y una **Hora de evento**, pero debe incluir tanta información como sea posible en el campo de propiedades personalizadas. Consulte el [objeto de evento]({{site.baseurl}}/api/objects_filters/event_object/) para obtener más detalles.
{% endalert %}

{% endtab %}
{% tab Atributo de usuario %}

Los atributos de usuario pueden ser un objeto JSON que contenga campos que crearán o actualizarán un atributo con el nombre y valor suministrados en el perfil de usuario especificado. Se admiten las siguientes propiedades:

| Atributo de usuario | Descripción |
| --- | --- |
| Nombre | Nombre del usuario. |
| Apellido | Apellido del usuario. |
| Teléfono | Número de teléfono del usuario. |
| Correo electrónico | Dirección de correo electrónico del usuario. |
| Género | Una de las siguientes cadenas: "M", "F", "O" (otro), "N" (no procede), "P" (prefiero no decirlo). |
| Localidad | La ciudad del usuario. |
| País | El país del usuario como cadena en formato [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). |
| Idioma | El idioma del usuario como cadena en formato [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). |
| Fecha de nacimiento | Los datos de nacimiento del usuario en cadena en formato "AAAA-MM-DD" (por ejemplo, 1980-12-21). |
| Zona horaria | Nombre de la zona horaria de la base de datos de [zonas horarias de IANA](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (por ejemplo, "América/Nueva_York" u "Hora del Este (EE.UU. y Canadá)"). |
| Facebook | Un hash que contiene cualquiera de los siguientes elementos: `id` (cadena), `likes` (matriz de cadenas), `num_friends` (entero). |
| X | Hash que contiene cualquiera de estos: id (entero), `screen_name` (cadena, X (antes Twitter) handle), `followers_count` (entero), `friends_count` (entero), `statuses_count`(entero). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Todos los atributos añadidos en la configuración se enviarán cada vez que el evento se envíe a Braze, independientemente de si el valor del atributo ha cambiado. Cuando configure los atributos de usuario, asegúrese de saber cómo afectarán al consumo de puntos de datos.
{% endalert %}

{% endtab %}
{% endtabs %}

### Paso 5: Crear una regla de envío de evento de compra

Tras instalar la extensión, crea una nueva [regla ](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en) de reenvío de eventos y configura sus condiciones como desees. Al configurar las acciones para la regla, seleccione la extensión **Braze** y, a continuación, seleccione **Enviar evento de compra** para el tipo de acción.

![]({% image_buster /assets/img/efe2.png %})

{% tabs local %}
{% tab Identificación del usuario %}

| Entrada de datos | Descripción |
| --- | --- |
| ID de usuario externo | Un UUID o GUID largo, aleatorio y bien distribuido. Si eliges un método diferente para nombrar tus identificadores de usuario, también deben ser largos, aleatorios y estar bien distribuidos. Más información sobre [la convención de nomenclatura de ID de usuario sugerida]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids#suggested-user-id-naming-convention). |
| ID de usuario Braze | Identificador de usuario Braze. |
| Alias de usuario | Un alias sirve como identificador único alternativo del usuario. Utilice alias para identificar a los usuarios en dimensiones diferentes a su ID de usuario principal.<br><br>El objeto alias de usuario consta de dos partes: un `alias_name` para el propio identificador y un `alias_label` que indica el tipo de alias. Los usuarios pueden tener varios alias con etiquetas diferentes, pero sólo un `alias_name` por `alias_label`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Para vincular el evento a un usuario, debes rellenar el campo `External User ID`, el campo `Braze User Identifier` o la sección `User Alias`.
{% endalert %}

{% endtab %}
{% tab Datos de compra %}

| Entrada de datos | Descripción | Obligatoria |
| --- | --- | --- |
| Identificación del producto | Identificador de la compra. (por ejemplo, nombre del producto o categoría del producto). | Sí |
| Tiempo de compra | Fecha-hora como cadena en formato ISO 8601 o en `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. | Sí |
| Divisa | Moneda como cadena en formato de código de moneda alfabético [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217). | Sí |
| Precio | El precio del objeto. | Sí |
| Cantidad | La cantidad comprada. Si no se proporciona, el valor predeterminado será 1. El valor máximo debe ser inferior a 100. | No |
| Identificador de la aplicación | El identificador de aplicación o `app_id` es un parámetro que asocia la actividad con una aplicación específica en su espacio de trabajo. Designa con qué aplicación del espacio de trabajo estás interactuando. | No |
| Propiedades de la compra | Un objeto JSON que contiene propiedades personalizadas de la compra. | No |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
La acción **Enviar evento de compra** sólo requiere que se especifique `Product ID`, `Purchase Time`, `Currency` y `Price`, pero debes incluir toda la información posible en el campo propiedades de la compra. Consulte el [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/) para obtener más información.
{% endalert %}

{% endtab %}
{% tab Atributos del usuario %}

Puede elegir si desea enviar atributos con cada evento dentro de la vista de configuración.

Los atributos de usuario pueden ser un objeto JSON que contenga campos que crearán o actualizarán un atributo con el nombre y valor suministrados en el perfil de usuario especificado. Se admiten las siguientes propiedades:

| Atributo de usuario | Descripción |
| --- | --- |
| Nombre | Nombre del usuario. |
| Apellido | Apellido del usuario. |
| Teléfono | Número de teléfono del usuario. |
| Correo electrónico | Dirección de correo electrónico del usuario. |
| Género | Una de las siguientes cadenas: "M", "F", "O" (otro), "N" (no procede), "P" (prefiero no decirlo). |
| Localidad | La ciudad del usuario. |
| País | El país del usuario como cadena en formato [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). |
| Idioma | El idioma del usuario como cadena en formato [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). |
| Fecha de nacimiento | Los datos de nacimiento del usuario en cadena en formato "AAAA-MM-DD" (por ejemplo, 1980-12-21). |
| Zona horaria | Nombre de la zona horaria de la base de datos de [zonas horarias de IANA](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (por ejemplo, "América/Nueva_York" u "Hora del Este (EE.UU. y Canadá)"). |
| Facebook | Un hash que contiene cualquiera de los siguientes elementos: `id` (cadena), `likes` (matriz de cadenas), `num_friends` (entero). |
| X | Hash que contiene cualquiera de estos: id (entero), `screen_name` (cadena, X (antes Twitter) handle), `followers_count` (entero), `friends_count` (entero), `statuses_count`(entero). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Todos los atributos añadidos en la configuración se enviarán cada vez que el evento se envíe a Braze, independientemente de si el valor del atributo ha cambiado. Al configurar los atributos de usuario, asegúrese de saber cómo afectará esto al consumo de puntos de datos.
{% endalert %}

{% endtab %}
{% endtabs %}

### Paso 6: Validación de datos en Braze

Si la recopilación de eventos y la integración de Adobe Experience Platform se han realizado correctamente, verá los eventos en la consola Braze al [ver los perfiles de usuario]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/). En concreto, los nuevos datos de eventos enviados a Braze se reflejan en la sección **Compras** o **Eventos personalizados** de la [pestaña de resumen]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#overview-tab) de un usuario concreto.

