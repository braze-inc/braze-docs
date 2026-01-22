# Funciones del servidor Braze MCP

> El servidor Braze MCP expone un conjunto de funciones API de sólo lectura que se mapean a puntos finales específicos de la API REST de Braze. Los clientes MCP como Claude y Cursor pueden llamar a estas funciones para recuperar datos sin acceder a la PII ni hacer cambios en tu espacio de trabajo. Para más información general, consulta [Servidor MCP de Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "desarrollador" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Requisitos previos

Antes de poder utilizar esta característica, tendrás que [configurar el servidor Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "desarrollador" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## Funciones disponibles de la API Braze

Éstas son las funciones API a las que hace referencia tu cliente MCP para interactuar con el servidor MCP Braze:

### Funciones generales

| Función | Descripción |
|----------|-------------|
| `list_functions` | Lista todas las funciones disponibles de la API de Braze con sus descripciones y parámetros |
| `call_function` | Llama a una función específica de la API de Braze con los parámetros proporcionados |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Campañas

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `get_campaign_list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | Exporta una lista de campañas con metadatos. |
| `get_campaign_details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | Obtén información detallada sobre campañas concretas. |
| `get_campaign_dataseries` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | Recupera datos de análisis de series temporales para campañas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Canvas

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `get_canvas_list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | Exporta una lista de Lienzos con metadatos. |
| `get_canvas_details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | Obtén información detallada sobre Lienzos concretos. |
| `get_canvas_data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | Obtén un análisis resumido del rendimiento de Canvas. |
| `get_canvas_data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | Recuperar datos de análisis de series temporales para Lienzos. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Catálogos

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `get_catalogs` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | Devuelve una lista de los catálogos de un espacio de trabajo. |
| `get_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | Devuelve varios elementos del catálogo y su contenido con soporte de paginación. |
| `get_catalog_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | Devuelve un elemento concreto del catálogo y su contenido por ID. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Ingesta de datos de Cloud

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `list_integrations` | [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | Devuelve una lista de las integraciones CDI existentes. |
| `get_integration_job_sync_status` | [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | Devuelve los estados de sincronización anteriores de una integración CDI determinada. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Bloques de contenido

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `get_content_blocks_list` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | Lista tus bloques de contenido disponibles. |
| `get_content_blocks_info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | Obtén información sobre tus bloques de contenido. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Atributos personalizados

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `get_custom_attributes` | [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) | Exporta atributos personalizados registrados para tu aplicación. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Eventos

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `get_events_list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | Exporta una lista de eventos personalizados grabados para tu aplicación. |
| `get_events_data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | Recuperar datos de series temporales para eventos personalizados. |
| `get_events` | [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) | Obtén datos detallados de los eventos con soporte de paginación. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### KPI

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `get_new_users_data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | Serie diaria de recuentos de nuevos usuarios. |
| `get_dau_data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | Datos de series temporales de usuarios activos diarios. |
| `get_mau_data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | Datos de series temporales de usuarios activos al mes. |
| `get_uninstalls_data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | Desinstalar aplicación de datos de series temporales. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Mensajes

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `get_scheduled_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled) | Enumera las próximas campañas y lonas programadas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Centros de preferencias

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `get_preference_centers` | [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center) | Enumera tus centros de preferencia disponibles. |
| `get_preference_center_details` | [`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | Ver los detalles de un centro de preferencias concreto, incluido el contenido HTML y las opciones. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Compras

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `get_product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | Exportar lista paginada de ID de producto. |
| `get_revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | Datos de series temporales de análisis de ingresos. |
| `get_quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | Datos de series temporales de cantidades de compra. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Segmentos

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `get_segment_list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | Exportar lista de segmentos con estado de seguimiento de análisis. |
| `get_segment_data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | Datos de análisis de series temporales por segmentos. |
| `get_segment_details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | Información detallada sobre segmentos específicos. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Envíos

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `get_send_data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | Análisis diario de los envíos de campaña seguidos. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Sesiones

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `get_session_data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | Datos de series temporales para el recuento de sesiones de la aplicación. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Claves de autenticación SDK

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `get_sdk_authentication_keys` | [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | Lista todas las claves de autenticación SDK de tu aplicación. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Suscripción

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `get_user_subscription_groups` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) | Listar y obtener los grupos de suscripción de un determinado usuario. |
| `get_subscription_group_status` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) | Obtener el estado de suscripción de un usuario en un grupo de suscripción. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Plantillas

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `get_email_templates_list` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | Haz una lista de tus plantillas de correo electrónico disponibles. |
| `get_email_template_info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | Obtenga información sobre sus plantillas de correo electrónico. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% multi_lang_include mcp_server/legal_disclaimer.md %}
