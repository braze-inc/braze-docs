---
nav_title: "Resumen de la API"
article_title: Resumen de la API
page_order: 2.1
description: "Este artículo de referencia cubre los aspectos básicos de la API, incluyendo qué es una API REST, la terminología y un resumen de las claves de API."
page_type: reference
alias: /api/api_key/
---

# Resumen de la API

> Este artículo de referencia cubre los conceptos básicos de la API, incluida la terminología común y un resumen de las claves de la API REST, los permisos y cómo mantenerlos seguros.

## Colección API REST de Braze

| Colección                                                                 | Propósito                                                                               |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [Catálogos]({{site.baseurl}}/api/endpoints/catalogs/)                       | Crea y administra catálogos y artículos de catálogo para referenciarlos en tus campañas Braze.    |
| [Ingesta de datos de Cloud]({{site.baseurl}}/api/endpoints/cdi/)                | Gestiona las integraciones y sincronizaciones de tu almacén de datos.                                    |
| [Listas y direcciones de correo electrónico]({{site.baseurl}}/api/endpoints/email/)         | Configura y gestiona la sincronización bidireccional entre Braze y tus sistemas de correo electrónico.           |
| [Exportar]({{site.baseurl}}/api/endpoints/export/)                           | Accede y exporta varios detalles de tus campañas, Canvases, KPIs y mucho más.        |
| [Mensajes]({{site.baseurl}}/api/endpoints/messaging/)                      | Programa, envía y gestiona tus campañas y Lienzos.                               |
| [Centro de preferencias]({{site.baseurl}}/api/endpoints/preference_center/)     | Construye tu centro de preferencias y actualiza su estilo.                            |
| [SCIM]({{site.baseurl}}/api/endpoints/scim/)                               | Administra las identidades de los usuarios en aplicaciones y servicios basados en la nube.                      |
| [SMS]({{site.baseurl}}/api/endpoints/sms/)                                 | Gestiona los números de teléfono de tus usuarios en tus grupos de suscripción.                         |
| [Grupos de suscripción]({{site.baseurl}}/api/endpoints/subscription_groups/) | Enumera y actualiza los grupos de suscripción por SMS y correo electrónico almacenados en el panel Braze. |
| [Plantillas]({{site.baseurl}}/api/endpoints/templates/)                     | Crea y actualiza plantillas para mensajes por correo electrónico y bloques de contenido.                   |
| [Datos de usuario]({{site.baseurl}}/api/endpoints/user_data/)                     | Identifica, sigue y administra a tus usuarios.                                               |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Definiciones de la API

Lo que sigue es un resumen de los términos que puedes ver en la documentación de la API REST de Braze.

### Puntos finales

Braze gestiona varias instancias diferentes para nuestro panel y puntos finales REST. Cuando se aprovisione tu cuenta, accederás a una de las siguientes URL. Utiliza el punto final REST correcto en función de la instancia a la que estés aprovisionado. Si no estás seguro, abre un [ticket de soporte]({{site.baseurl}}/braze_support/) o utiliza la siguiente tabla para hacer coincidir la URL del panel que utilizas con el punto final REST correcto.

{% alert important %}
Cuando utilices puntos finales para las llamadas a la API, utiliza el punto final REST.

Para la integración de SDK, utiliza el [punto final SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/), no el punto final REST.
{% endalert %}

{% multi_lang_include data_centers.md datacenters='instances' %}

### Límites de API

Para la mayoría de las API, Braze tiene un límite de velocidad predeterminado de 250 000 solicitudes por hora. Sin embargo, a determinados tipos de solicitudes se les aplica su propio límite de velocidad para gestionar mejor los grandes volúmenes de datos de nuestra base de clientes. Para más detalles, consulta los [límites de velocidad de las API]({{site.baseurl}}/api/api_limits/)

### ID de usuario

- **ID externo del usuario**: La dirección `external_id` sirve como identificador único del usuario cuyos datos envías. Este identificador debe ser el mismo que el que estableciste en el SDK de Braze para evitar crear varios perfiles para el mismo usuario.
- **Braze ID de usuario**: `braze_id` sirve como identificador único de usuario que establece Braze. Este identificador puede utilizarse para eliminar usuarios a través de la API REST, además de external_ids.

Para más información, consulta los siguientes artículos en función de tu plataforma: [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/) y [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/).

## Acerca de las claves de API REST

Una clave de interfaz de programación de aplicaciones REST (clave de REST API) es un código único que se introduce en una API para autenticar la llamada a la API e identificar la aplicación o el usuario que realiza la llamada. El acceso a la API se realiza mediante solicitudes web HTTPS al punto final de la API REST de tu empresa. En Braze utilizamos claves de API REST junto con nuestras claves de identificador de aplicaciones para realizar el seguimiento, acceder, enviar, exportar y analizar datos, con el fin de asegurarnos de que todo funciona correctamente, tanto por tu parte como por la nuestra.

Los espacios de trabajo y las claves de API van de la mano en Braze. Los espacios de trabajo están diseñados para albergar versiones de la misma aplicación en varias plataformas. Muchos clientes también utilizan espacios de trabajo para contener versiones gratuitas y premium de sus aplicaciones en la misma plataforma. Como puedes observar, estos espacios de trabajo también utilizan la API REST y tienen sus propias claves de API REST. Se puede definir individualmente el ámbito de estas claves para que incluyan acceso a puntos finales específicos en la API. Cada llamada a la API tiene que incluir una clave con acceso al punto final.

Nos referimos tanto a la clave de la API REST como a la clave de la API del espacio de trabajo como `api_key`. El `api_key` se incluye en cada solicitud como encabezado de solicitud y actúa como clave de autenticación que te permite utilizar nuestras API REST. Estas API REST se utilizan para hacer un seguimiento de los usuarios, enviar mensajes, exportar datos de usuario, etc. Cuando crees una nueva clave de API REST, tendrás que darle acceso a puntos finales específicos. Al asignar permisos específicos a una clave de API, puedes limitar exactamente qué llamadas puede autenticar dicha clave.

![Panel de claves de API REST en la pestaña Claves de API.]({% image_buster /assets/img_archive/rest-api-key.png %})

{% alert tip %}
Además de las claves de API REST, también existe un tipo de clave llamada clave identificadora que puede utilizarse para hacer referencia a cosas concretas como aplicaciones, plantillas, lienzos, campañas, tarjetas de contenido y segmentos de la API. Para más información, consulta [Tipos de identificadores API]({{site.baseurl}}/api/identifier_types/).
{% endalert %}

### Crear claves de API REST

Para crear una nueva clave de API REST:

1. Ve a **Configuración** > **API e identificadores**.
2. Selecciona **Crear clave de API**.
3. Asigna un nombre a tu nueva clave para identificarla de un vistazo.
4. Especifica [las direcciones IP y subredes permitidas](#api-ip-allowlisting) para la nueva clave.
5. Selecciona los [permisos](#rest-api-key-permissions) que quieres asociar a tu nueva clave.

{% alert important %}
Ten en cuenta que después de crear una nueva clave de API, no puedes editar el alcance de los permisos ni las IP permitidas. Esta limitación se aplica por motivos de seguridad. Si necesitas cambiar el alcance de una clave, crea una nueva con los permisos actualizados e implementa esa clave en lugar de la anterior. Cuando hayas completado la implementación, puedes eliminar la clave antigua.
{% endalert %}

### Permisos de la clave de API REST

Los permisos de clave de API son permisos que puedes asignar a un usuario o grupo para limitar su acceso a determinadas llamadas de API. Para ver tu lista de permisos de clave de API, ve a **Configuración** > **API e identificadores**, y selecciona tu clave de API.

{% tabs %}
{% tab User Data %}

| Permiso | Punto de conexión | Descripción |
|---|---|---|
| `users.track` | [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) | Registra atributos de usuario, eventos personalizados y compras. |
| `users.delete` | [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) | Elimina cualquier usuario. |
| `users.alias.new` | [`/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias/) |Crea un nuevo alias para un usuario existente. |
| `users.identify` | [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) |Identifica a un usuario de sólo alias con un ID externo. |
| `users.export.ids` | [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) |Consulta la información del perfil de usuario por ID de usuario. |
| `users.export.segment` | [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) |Consulta la información del perfil de usuario por segmentos. |
| `users.merge` | [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) | Fusiona dos usuarios existentes entre sí. |
| `users.external_ids.rename` | [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/) | Cambia el ID externo de un usuario existente. |
| `users.external_ids.remove` | [`/users/external_ids/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove/) | Elimina el ID externo de un usuario existente. |
| `users.alias.update` | [`/users/alias/update`]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/) | Actualiza un alias para un usuario existente. |
| `users.export.global_control_group` | [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/) | Consulta la información del perfil de usuario en el grupo de control global. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

 {% endtab %}
 {% tab Email %}

| Permiso | Punto de conexión | Descripción |
|---|---|---|
| `email.unsubscribe` | [`/email/unsubscribes`]({{site.baseurl}}/api/endpoints/email/get_query_unsubscribed_email_addresses/) | Consulta las direcciones de correo electrónico que han cancelado su suscripción.  |
| `email.status` | [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/) | Cambia el estado de la dirección de correo electrónico. |
| `email.hard_bounces` | [`/email/hard_bounces`]({{site.baseurl}}/api/endpoints/email/get_list_hard_bounces/) | Consulta las direcciones de correo electrónico en rebote duro. |
| `email.bounce.remove` | [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces/) | Elimina direcciones de correo electrónico de tu lista de rebote duro. |
| `email.spam.remove` | [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam/) | Elimina direcciones de correo electrónico de tu lista de correo no deseado. |
| `email.blacklist` | [`/email/blacklist`]({{site.baseurl}}/api/endpoints/email/post_blacklist/) | Direcciones de correo electrónico de la lista de bloqueo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Messages %}

| Permiso | Punto de conexión | Descripción |
|---|---|---|
| `messages.send` | [`/messages/send `]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) | Envía un mensaje inmediato a usuarios concretos. |
| `messages.schedule.create` | [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/) | Programa un mensaje para que se envíe a una hora específica. |
| `messages.schedule.update` | [`/messages/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/) | Actualiza un mensaje programado. |
| `messages.schedule.delete` | [`/messages/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/) | Elimina un mensaje programado. |
| `messages.schedule_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/) | Consulta todos los mensajes emitidos programados. |
| `messages.live_activity.update` | [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update/) | Actualiza una Actividad en vivo de iOS. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Campaigns %}

| Permiso | Punto de conexión | Descripción |
|---|---|---|
| `campaigns.trigger.send` | [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) | Desencadenar el envío de una campaña existente. |
| `campaigns.trigger.schedule.create` | [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/) | Programa un envío futuro de una campaña con entrega desencadenada por API. |
| `campaigns.trigger.schedule.update` | [`/campaigns/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/) | Actualiza una campaña programada con entrega desencadenada por API. |
| `campaigns.trigger.schedule.delete` | [`/campaigns/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/) |Elimina una campaña programada con entrega desencadenada por API. |
| `campaigns.list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) | Consulta una lista de campañas. |
| `campaigns.data_series` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) | Consulta los análisis de la campaña en un intervalo de tiempo. |
| `campaigns.details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) | Consulta los detalles de una campaña concreta. |
| `sends.data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) | Consulta el análisis del envío de mensajes a lo largo de un intervalo de tiempo. |
| `sends.id.create` | [`/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/) | Crea un ID de envío para el seguimiento de la difusión de mensajes. |
| `campaigns.url_info.details` | [`/campaigns/url_info/details`]({{site.baseurl}}) | Consulta los detalles de la URL de una variación de mensaje concreta dentro de una campaña. |
| `transactional.send` | [`/transactional/v1/campaigns/{campaign_id}/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message/) | Permite enviar mensajes transaccionales utilizando el punto final de mensajería transaccional. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Canvas %}

| Permiso | Punto de conexión | Descripción |
|---|---|---|
| `canvas.trigger.send` | [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) | Desencadena el envío de un Canvas existente. |
| `canvas.trigger.schedule.create` | [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/) | Programa el envío futuro de un Canvas con entrega desencadenada por API. |
| `canvas.trigger.schedule.update` | [`/canvas/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/) | Actualiza un Canvas programado con entrega desencadenada por API. |
| `canvas.trigger.schedule.delete` | [`/canvas/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/)| Elimina un Canvas programado con entrega desencadenada por API. |
| `canvas.list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) |  Consulta una lista de Canvas. |
| `canvas.data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) | Consulta el análisis de Canvas a lo largo de un intervalo de tiempo. |
| `canvas.details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) | Consulta los detalles de un Canvas concreto. |
| `canvas.data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/) | Consulta el acumulado del análisis de Canvas a lo largo de un intervalo de tiempo. |
| `canvas.url_info.details` | [`/canvas/url_info/details`]({{site.baseurl}}/get_canvas_link_alias/) | Consulta los detalles de la URL de una variación específica de un mensaje dentro de un paso en Canvas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Segments %}

| Permiso | Punto de conexión | Descripción |
|---|---|---|
| `segments.list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) | Consulta una lista de segmentos. |
| `segments.data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/) | Consulta el análisis de segmentos en un intervalo de tiempo. |
| `segments.details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/) | Consulta los detalles de un segmento concreto. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Purchases %}

| Permiso | Punto de conexión | Descripción |
|---|---|---|
| `purchases.product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) | Consulta una lista de los productos adquiridos en tu aplicación. |
| `purchases.revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series/) | Consulta el total de dinero gastado al día en tu aplicación durante un intervalo de tiempo. |
| `purchases.quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases/) | Consulta el número total de compras diarias en tu aplicación en un intervalo de tiempo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Events %}

| Permiso | Punto de conexión | Descripción |
|---|---|---|
| `events.list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/) | Consulta una lista de eventos personalizados. |
| `events.data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/) | Consulta las apariciones de un evento personalizado en un intervalo de tiempo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Sessions %}

| Permiso | Punto de conexión | Descripción |
|---|---|---|
| `sessions.data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/) | Consulta las sesiones diarias durante un intervalo de tiempo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab KPIs %}

| Permiso | Punto de conexión | Descripción |
|---|---|---|
| `kpi.dau.data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/) |  Consulta los usuarios activos únicos al día durante un intervalo de tiempo. |
| `kpi.mau.data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/) | Consulta el total de usuarios activos únicos durante un período acumulado de 30 días durante un intervalo de tiempo. |
| `kpi.new_users.data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/) | Consulta los usuarios nuevos al día durante un intervalo de tiempo. |
| `kpi.uninstalls.data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/) | Consulta las desinstalaciones de aplicación por día durante un intervalo de tiempo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Templates %}

| Permiso | Punto de conexión | Descripción |
|---|---|---|
| `templates.email.create` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/) | Crea una nueva plantilla de correo electrónico en el panel. |
| `templates.email.info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | Consulta información sobre una plantilla concreta. |
| `templates.email.list` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) | Consulta una lista de plantillas de correo electrónico. |
| `templates.email.update` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/) | Actualiza una plantilla de correo electrónico almacenada en el panel. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab SSO %}

| Permiso | Descripción |
|---|---|---|
| `sso.saml.login` | Configura la sesión iniciada por el proveedor de identidad. Para más información, consulta el [inicio de sesión iniciado por el proveedor de servicios (SP)]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Content Blocks %}

| Permiso | Punto de conexión | Descripción |
|---|---|---|
| `content_blocks.info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) | Consulta información sobre una plantilla concreta. |
| `content_blocks.list` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) | Consulta una lista de bloques de contenido. |
| `content_blocks.create` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/) | Crea un nuevo bloque de contenido en el panel. |
| `content_blocks.update` | [`/content_blocks_update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) | Actualiza un bloque de contenido existente en el panel. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Preference Center %}

| Permiso | Punto de conexión | Descripción |
|---|---|---|
| `preference_center.get` | [`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | Consigue un centro de preferencias. |
| `preference_center.list` | [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/) | Haz una lista de los centros de preferencias. |
| `preference_center.update` | [`/preference_center/v1`]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center)<br><br>[`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/) | Crea o actualiza un centro de preferencias. |
| `preference_center.user.get` | [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center) | Consigue un enlace a un centro de preferencias para un usuario. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Subscription %}

| Permiso | Punto de conexión | Descripción |
|---|---|---|
| `subscription.status.set` | [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) | Configura el estado del grupo de suscripción. |
| `subscription.status.get` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) | Consigue el estado del grupo de suscripción. |
| `subscription.groups.get` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) | Obtén el estado de los grupos de suscripción a los que están suscritos y cancelados explícitamente determinados usuarios. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab SMS %}

| Permiso | Punto de conexión | Descripción |
|---|---|---|
| `sms.invalid_phone_numbers` | [`/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers/) | Consulta los números de teléfono no válidos. |
| `sms.invalid_phone_numbers.remove` | [`/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers/) | Retira la marca de número de teléfono no válido de los usuarios. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Catalogs %}

| Permiso | Punto de conexión | Descripción |
|---|---|---|
| `catalogs.add_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/) | Añade varios elementos a un catálogo existente. |
| `catalogs.update_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/) | Actualiza varios elementos en un catálogo existente. |
| `catalogs.delete_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk) | Elimina varios elementos de un catálogo existente. |
| `catalogs.get_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/) | Consigue un elemento único de un catálogo existente. |
| `catalogs.update_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/) | Actualiza un elemento único en un catálogo existente. |
| `catalogs.create_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/) | Crea un elemento único en un catálogo existente. |
| `catalogs.delete_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/) | Elimina un elemento único de un catálogo existente. |
| `catalogs.replace_item` | [` /catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/) | Sustituye un elemento único de un catálogo existente. |
| `catalogs.create` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/) | Crea un catálogo. |
| `catalogs.get` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) | Obtener una lista de catálogos |
| `catalogs.delete` | [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/) | Borrar un catálogo. |
| `catalogs.get_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/) | Obtén una vista previa de un catálogo existente. |
| `catalogs.replace_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/) | Reemplazar elementos de un catálogo existente. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab SDK Authentication %}

| Permiso | Punto de conexión | Descripción |
|---|---|---|
| `sdk_authentication.create` | [`/app_group/sdk_authentication/create`]({{site.baseurl}}/api/endpoints/sdk_authentication/post_create_sdk_authentication_key) | Crea una nueva clave de autenticación SDK para tu aplicación. |
| `sdk_authentication.primary` | [`/app_group/sdk_authentication/primary`]({{site.baseurl}}/api/endpoints/sdk_authentication/put_primary_sdk_authentication_key/) | Marca una clave de autenticación SDK como clave principal de tu aplicación. |
| `sdk_authentication.delete` | [`/app_group/sdk_authentication/delete`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key) | Elimina una clave de autenticación SDK para tu aplicación. |
| `sdk_authentication.keys` | [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | Obtén todas las claves de autenticación del SDK para tu aplicación. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% endtabs %}

### Gestión de claves de API REST

Puedes ver los detalles de las claves de API REST existentes o eliminarlas desde **Configuración** > **API e identificadores** > pestaña **Claves de API**. Ten en cuenta que las claves de API REST no se pueden editar una vez creadas.

La pestaña **Claves de API** incluye la siguiente información para cada clave:

| Campo        | Descripción                                                                                                         |
| ------------ | :------------------------------------------------------------------------------------------------------------------ |
| Nombre de clave de API | El nombre dado a la clave en el momento de su creación.                                                                            |
| Identificador   | La clave de API.                                                                                                        |
| Creación a cargo de   | La dirección de correo electrónico del usuario que creó la clave. Este campo aparecerá como "N/A" para las claves creadas antes de junio de 2023. |
| Fecha de creación | La fecha de creación de esta clave.                                                                                      |
| Visto por última vez    | La fecha en que se utilizó esta clave por última vez. Este campo aparecerá como "N/A" para las claves que nunca se hayan utilizado.                  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para ver los detalles de una clave de API, pasa el ratón por encima de la clave y selecciona <i class="fa-solid fa-eye" alt="View"></i> **Ver**. Esto incluye todos los permisos que tiene esta clave, las IP de la lista blanca (si las hay), y si esta clave está incluida en la lista blanca de IP de Braze.

![La lista de permisos de la clave de API en el panel Braze.]({% image_buster /assets/img_archive/view-api-key.png %})

Ten en cuenta que, al [eliminar un]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/) usuario, no se eliminarán las claves de API asociadas que haya creado. Para borrar una tecla, pasa el ratón sobre ella y selecciona <i class="fa-solid fa-trash-can" alt="Delete"></i> **Borrar**.

![Una clave de API llamada "Visto por última vez" con el icono de la papelera resaltado, mostrando "Eliminar".]({% image_buster /assets/img_archive/api-key-options.png %}){: style="max-width:30%;"}

### Seguridad de la clave de API REST

Las claves de API se utilizan para autenticar una llamada a la API. Cuando se crea una nueva clave de API REST, es necesario darle acceso a puntos finales específicos. Al asignar permisos específicos a una clave de API, puedes limitar exactamente qué llamadas puede autenticar dicha clave.

Dado que las claves de API REST permiten acceder a puntos finales de API REST potencialmente sensibles, protege estas claves y compártelas sólo con socios de confianza. Nunca pueden quedar expuestas al público. Por ejemplo, no utilices esta clave para hacer llamadas AJAX desde tu sitio web ni la expongas de ninguna otra forma pública.

Una buena práctica de seguridad es asignar a un usuario sólo el acceso necesario para completar su trabajo: este principio también puede aplicarse a las claves de API asignando permisos a cada clave. Estos permisos te proporcionan mayor seguridad y control sobre las distintas áreas de tu cuenta.

{% alert warning %}
Dado que las claves de API REST permiten acceder a puntos finales de API REST potencialmente sensibles, asegúrate de que se almacenan y utilizan de forma segura. Por ejemplo, no utilices esta clave para hacer llamadas AJAX desde tu sitio web ni la expongas de ninguna otra forma pública.
{% endalert %}

Si se produce una exposición accidental de una clave, puede borrarse desde la consola para desarrolladores. Si necesitas ayuda con este proceso, abre un [ticket de soporte]({{site.baseurl}}/braze_support/).

### Lista de direcciones IP permitidas de la API

Para mayor seguridad, puedes especificar una lista de direcciones IP y subredes a las que se permite realizar solicitudes de API REST para una clave de API REST determinada. Esto se denomina lista blanca o lista permitida. Para permitir direcciones IP o subredes específicas, añádelas a la sección **IPs de la lista blanca** al crear una nueva clave de API REST:

![Opción para permitir IPs de la lista al crear una clave de API.]({% image_buster /assets/img_archive/api-key-ip-whitelisting.png %})

Si no especifica ninguna, las peticiones pueden enviarse desde cualquier dirección IP.

{% alert tip %}
¿Hacer un webhook Braze-to-Braze y utilizar allowlisting? Consulta nuestra lista de [IPs en lista blanca]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-whitelisting).
{% endalert %}

## Recursos adicionales

### Biblioteca cliente Ruby

Si estás implementando Braze utilizando Ruby, puedes utilizar nuestra [biblioteca cliente Ruby](https://github.com/braze-inc/braze-api-client-ruby) para reducir el tiempo de importación de datos. Una biblioteca cliente es una colección de código específico de un lenguaje de programación -en este caso, Ruby- que facilita el uso de una API.

La biblioteca cliente Ruby admite los [puntos finales Usuario]({{site.baseurl}}/api/endpoints/user_data).

{% alert important %}
Esta biblioteca cliente está actualmente en fase beta. ¿Quieres ayudarnos a mejorar esta biblioteca? Envíanos tus comentarios a [smb-product@braze.com](mailto:smb-product@braze.com).
{% endalert %}

