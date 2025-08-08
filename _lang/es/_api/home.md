---
page_order: 0
nav_title: Inicio
article_title: Guía de la API de Braze
layout: api_glossary
glossary_top_header: "Braze API Guide"
glossary_top_text: "Braze provides a high-performance REST API to allow you to track users, send messages, export data, and more. This page lists available Braze API endpoints and their uses."
page_type: glossary
description: "Esta página de inicio enumera los puntos finales disponibles de la API de Braze y sus usos."
glossary_tag_name: Endpoint Type

glossary_filter_text: "Select endpoint type to narrow the glossary:"

glossary_mid_text: "Endpoint Search"
guide_featured_list:
  - name: Resumen de la API
    image: /assets/img/braze_icons/annotation-info.svg
    link: /docs/api/basics/
  - name: Tipos de identificadores API
    link: /docs/api/identifier_types/
    image: /assets/img/braze_icons/clipboard-check.svg
  - name: Objetos y filtros
    link: /docs/api/objects_filters/
    image: /assets/img/braze_icons/settings-01.svg
  - name: Errores y respuestas
    link: /docs/api/errors/
    image: /assets/img/braze_icons/list.svg
  - name: Retención de datos
    link: /docs/api/data_retention/
    image: /assets/img/braze_icons/laptop-02.svg
  - name: Límites de tarifa
    link: /docs/api/api_limits/
    image: /assets/img/braze_icons/hand.svg

# channel to icon/fa or image mapping
glossary_tags:
  - name: Campañas
  - name: Canvas
  - name: Catálogos
  - name: Bloques de contenido
  - name: Eventos personalizados
  - name: Lista de correo electrónico
  - name: Plantillas de correo electrónico
  - name: KPI
  - name: Compras
  - name: Centro de preferencias
  - name: Programar mensajes
  - name: SCIM
  - name: Autenticación SDK
  - name: Segmentos
  - name: Enviar mensajes
  - name: SMS
  - name: Grupos de suscripción
  - name: Datos de usuario
  - name: Actividad en directo
  - name: Ingesta de datos de Cloud

glossaries:
  - name: "<a href='/docs/api/endpoints/user_data/post_user_alias/'>/users/alias/new</a>"
    description: "Añadir nuevos alias de usuario para usuarios identificados existentes, o para crear nuevos usuarios no identificados."
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_users_alias_update/'>/users/alias/update</a>"
    description: Actualice los nombres de alias de usuario existentes a nuevos nombres de alias de usuario.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_user_delete/'>/users/delete</a>"
    description: Elimina cualquier perfil de usuario especificando un identificador de usuario conocido.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/export/user_data/post_users_global_control_group/'>/users/export/global_control_group</a>"
    description: Exportar todos los usuarios de un Grupo de Control Global.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/export/user_data/post_users_identifier/'>/users/export/ids</a>"
    description: Exporte datos de cualquier perfil de usuario especificando un identificador de usuario.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/export/user_data/post_users_segment/'>/users/export/segment</a>"
    description: Exportar todos los usuarios de un segmento.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename/'>/users/external_ids/rename</a>"
    description: Cambie el nombre de los identificadores externos de sus usuarios.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove/'>/users/external_ids/remove</a>"
    description: Elimine los antiguos ID externos obsoletos de sus usuarios.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_user_identify/'>/users/identify</a>"
    description: Identificar a un usuario no identificado (solo alias).
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_user_track/'>/users/track</a>"
    description: "Registre eventos personalizados, compras y actualice los atributos del perfil del usuario."
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_users_merge/'>/users/merge</a>"
    description: Fusionar un perfil de usuario con otro usuario.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/'>/campaigns/trigger/send</a>"
    description: Envíe mensajes inmediatos y puntuales a usuarios designados a través de la entrega activada por API. - Enviar mensajes
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases/'>/canvas/trigger/send</a>"
    description: Envíe mensajes Canvas a través de la entrega activada por API. - Enviar mensajes
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_send_messages/'>/messages/send</a>"
    description: Envía mensajes inmediatos y puntuales a usuarios designados a través de la API Braze.
    tags:
      - Send Messages
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_create_send_ids/'>/sends/id/create</a>"
    description: "Cree ID de envío que puedan utilizarse para enviar mensajes y realizar un seguimiento del rendimiento de los mensajes mediante programación, sin necesidad de crear campañas para cada envío."
    tags:
      - Send Messages
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_send_transactional_message/'>/transactional/v1/campañas/{CAMPAIGN_ID}/enviar</a>"
    description: Envía inmediatamente mensajes transaccionales puntuales a un usuario designado.
    tags:
      - Send Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/'>/campaigns/trigger/schedule/create</a>"
    description: Envía mensajes de campaña creados en el panel mediante entrega desencadenada por API.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/'>/campaigns/trigger/schedule/delete</a>"
    description: Cancele los mensajes de campaña activados por la API que haya programado previamente antes de que se hayan enviado.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/'>/campaigns/trigger/schedule/update</a>"
    description: Actualice las campañas programadas activadas por API creadas en el panel de control.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/'>/canvas/trigger/schedule/delete</a>"
    description: Cancela un mensaje de Canvas que hayas programado antes mediante entrega desencadenada por API antes de que se haya enviado.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/'>/canvas/trigger/schedule/create</a>"
    description: Programa mensajes de Canvas mediante entrega desencadenada por API.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/'>/messages/schedule/update</a>"
    description: Actualizar los mensajes programados. Este punto final acepta actualizaciones del parámetro <code>schedule</code> o <code>messages</code> o ambos.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/'>/messages/schedule/delete</a>"
    description: Cancelar un mensaje programado previamente antes de que se haya enviado.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_messages/'>/messages/schedule/create</a>"
    description: "Programe una campaña, Canvas u otro mensaje para que se envíe a una hora determinada."
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/'>/canvas/trigger/schedule/update</a>"
    description: Actualice los lienzos programados activados por la API que se crearon en el panel de control.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled/'>/messages/scheduled_broadcasts</a>"
    description: Devuelve una lista JSON con información sobre las campañas programadas y los lienzos de entrada entre el momento actual y el momento designado. <code>end_time</code> especificado en la solicitud.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/live_activity/update/'>/messages/live_activity/update</a>"
    description: Actualizar una actividad de iOS Live.
    tags:
      - Live Activity
  - name: "<a href='/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status/'>/subscription/status/set</a>"
    description: Actualice por lotes el estado de suscripción de hasta 50 usuarios en el panel Braze.
    tags:
      - Subscription Groups
  - name: "<a href='/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/'>/v2/subscription/status/set</a>"
    description: Actualice por lotes el estado de suscripción de hasta 50 usuarios en el panel Braze.
    tags:
      - Subscription Groups
  - name: "<a href='/docs/api/endpoints/subscription_groups/get_list_user_subscription_group_status/'>/subscription/status/get</a>"
    description: Obtener el estado de suscripción de un usuario en un grupo de suscripción.
    tags:
      - Subscription Groups
  - name: "<a href='/docs/api/endpoints/subscription_groups/get_list_user_subscription_groups/'>/subscription/user/status</a>"
    description: Listar y obtener los grupos de suscripción de un determinado usuario.
    tags:
      - Subscription Groups
  - name: "<a href='/docs/api/endpoints/email/post_blacklist/'>/email/blacklist</a>"
    description: Dar de baja a un usuario de correo electrónico y marcarlo como rebote duro.
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/email/post_remove_hard_bounces/'>/email/bounce/remove</a>"
    description: Elimine direcciones de correo electrónico de su lista de rebotes Braze.
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/email/post_remove_spam/'>/email/spam/remove</a>"
    description: Elimine direcciones de correo electrónico de su lista de spam Braze.
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/email/post_email_subscription_status/'>/email/status</a>"
    description: Establezca el estado de suscripción de correo electrónico para sus usuarios.
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/templates/email_templates/post_create_email_template/'>/templates/email/create</a>"
    description: Cree plantillas de correo electrónico en el panel Braze.
    tags:
      - Email Templates
  - name: "<a href='/docs/api/endpoints/templates/email_templates/post_update_email_template/'>/templates/email/update</a>"
    description: Actualice las plantillas de correo electrónico en el panel Braze.
    tags:
      - Email Templates
  - name: "<a href='/docs/api/endpoints/email/get_list_hard_bounces/'>/email/hard_bounces</a>"
    description: "Obtén una lista de las direcciones de correo electrónico que se consideraron \"rebotes duros\" y rebotaron tus mensajes de correo electrónico en un plazo determinado."
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/email/get_query_unsubscribed_email_addresses/'>/email/unsubscribes</a>"
    description: Devuelve los correos electrónicos que se han dado de baja durante el periodo de tiempo de <code>start_date</code> a <code>end_date</code>.
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/templates/email_templates/get_see_email_template_information/'>/templates/email/info</a>"
    description: Obtenga información sobre sus plantillas de correo electrónico.
    tags:
      - Email Templates
  - name: "<a href='/docs/api/endpoints/templates/email_templates/get_list_email_templates/'>/templates/email/list</a>"
    description: Obtenga una lista de las plantillas de correo electrónico disponibles en su cuenta Braze.
    tags:
      - Email Templates
  - name: "<a href='/docs/api/endpoints/export/campaigns/get_campaign_analytics/'>/campaigns/data_series</a>"
    description: Recuperar una serie diaria de diversas estadísticas de una campaña a lo largo del tiempo.
    tags:
      - Campaigns
  - name: "<a href='/docs/api/endpoints/export/campaigns/get_campaign_details/'>/campaigns/details</a>"
    description: Recuperar información relevante sobre una campaña especificada.
    tags:
      - Campaigns
  - name: "<a href='/docs/api/endpoints/export/campaigns/get_campaigns/'>/campaigns/list</a>"
    description: "Exporte una lista de campañas, cada una de las cuales incluirá su nombre, el identificador API de la campaña, si se trata de una campaña API y las etiquetas asociadas a la campaña."
    tags:
      - Campaigns
  - name: "<a href='/docs/api/endpoints/export/campaigns/get_send_analytics/'>/sends/data_series</a>"
    description: Recuperar una serie diaria de diversas estadísticas de un seguimiento <code>send_id</code>.
    tags:
      - Campaigns
  - name: "<a href='/docs/api/endpoints/export/canvas/get_canvas_analytics/'>/canvas/data_series</a>"
    description: Exportar datos de series temporales para un lienzo.
    tags:
      - Canvas
  - name: "<a href='/docs/api/endpoints/export/canvas/get_canvas_analytics_summary/'>/canvas/data_summary</a>"
    description: "Exportar rollups de datos de series temporales para un lienzo, proporcionando un resumen conciso de los resultados de un lienzo."
    tags:
      - Canvas
  - name: "<a href='/docs/api/endpoints/export/canvas/get_canvas_details/'>/canvas/details</a>"
    description: "Exporte metadatos sobre un lienzo, como el nombre, la hora de creación, el estado actual, etc."
    tags:
      - Canvas
  - name: "<a href='/docs/api/endpoints/export/canvas/get_canvases/'>/canvas/list</a>"
    description: "Exporte una lista de lienzos, incluido el nombre, el identificador de API de lienzo y las etiquetas asociadas."
    tags:
      - Canvas
  - name: "<a href='/docs/api/endpoints/export/segments/get_segment_analytics/'>/segments/data_series</a>"
    description: Recupera una serie diaria del tamaño estimado de un segmento a lo largo del tiempo.
    tags:
      - Segments
  - name: "<a href='/docs/api/endpoints/export/segments/get_segment_details/'>/segments/details</a>"
    description: Recuperar información relevante sobre un segmento.
    tags:
      - Segments
  - name: "<a href='/docs/api/endpoints/export/segments/get_segment/'>/segments/list</a>"
    description: "Exporte una lista de segmentos, cada uno de los cuales incluirá su nombre, el identificador de la API del segmento y si tiene activado el seguimiento analítico."
    tags:
      - Segments
  - name: "<a href='/docs/api/endpoints/export/sessions/get_sessions_analytics/'>/sessions/data_series</a>"
    description: Recupera una serie del número de sesiones de tu aplicación durante un periodo de tiempo determinado.
    tags:
      - Sessions
  - name: "<a href='/docs/api/endpoints/export/custom_attributes/get_custom_attributes/'>/custom_attributes</a>"
    description: "Exporte una lista de atributos personalizados que incluya el nombre, la descripción, el tipo de datos, la longitud de la matriz (si procede), el estado y las etiquetas asociadas."
    tags:
      - Custom Attributes
  - name: "<a href='/docs/api/endpoints/export/custom_events/get_custom_events_analytics/'>/events/data_series</a>"
    description: Recupera una serie del número de ocurrencias de un evento personalizado en tu aplicación durante un periodo de tiempo designado.
    tags:
      - Custom Events
  - name: "<a href='/docs/api/endpoints/export/custom_events/get_custom_events_data/'>/eventos</a>"
    description: "Exporte una lista de eventos personalizados que incluya el nombre, la descripción, el estado, las etiquetas asociadas y la inclusión de informes analíticos."
    tags:
      - Custom Events
  - name: "<a href='/docs/api/endpoints/export/custom_events/get_custom_events/'>/events/list</a>"
    description: Exportar una lista de nombres de eventos personalizados que se han registrado para su aplicación.
    tags:
      - Custom Events
  - name: "<a href='/docs/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/'>/content_blocks/create</a>"
    description: Crear un bloque de contenido de correo electrónico.
    tags:
      - Content Blocks
  - name: "<a href='/docs/api/endpoints/templates/content_blocks_templates/post_update_content_block/'>/content_blocks/update</a>"
    description: Actualizar un bloque de contenido de correo electrónico.
    tags:
      - Content Blocks
  - name: "<a href='/docs/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/'>/content_blocks/info</a>"
    description: Información de llamada para su Bloque de contenido de correo electrónico existente.
    tags:
      - Content Blocks
  - name: "<a href='/docs/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/'>/content_blocks/list</a>"
    description: Enumere la información de los bloques de contenido existentes.
    tags:
      - Content Blocks
  - name: "<a href='/docs/api/endpoints/export/kpi/get_kpi_dau_date/'>/kpi/dau/data_series</a>"
    description: Recuperar una serie diaria del número total de usuarios activos únicos en cada fecha.
    tags:
      - KPI
  - name: "<a href='/docs/api/endpoints/export/kpi/get_kpi_mau_30_days/'>/kpi/mau/data_series</a>"
    description: Recuperar una serie diaria del número total de usuarios activos únicos durante una ventana móvil de 30 días.
    tags:
      - KPI
  - name: "<a href='/docs/api/endpoints/export/kpi/get_kpi_daily_new_users_date/'>/kpi/new_users/data_series</a>"
    description: Recuperar una serie diaria del número total de nuevos usuarios en cada fecha.
    tags:
      - KPI
  - name: "<a href='/docs/api/endpoints/export/kpi/get_kpi_uninstalls_date/'>/kpi/uninstalls/data_series</a>"
    description: Recupera una serie diaria del número total de desinstalaciones en cada fecha.
    tags:
      - KPI
  - name: "<a href='/docs/api/endpoints/sms/post_remove_invalid_numbers/'>/sms/invalid_phone_numbers/remove</a>"
    description: "Eliminar números de teléfono \"inválidos\" de la lista de inválidos en Braze. Se puede utilizar para volver a validar números de teléfono después de que se hayan marcado como no válidos."
    tags:
      - SMS
  - name: "<a href='/docs/api/endpoints/sms/get_query_invalid_numbers/'>/sms/invalid_phone_numbers</a>"
    description: "Obtenga una lista de los números de teléfono que se han considerado \"no válidos\" en un plazo determinado."
    tags:
      - SMS
  - name: "<a href='/docs/api/endpoints/export/purchases/get_list_product_id/'>/purchases/product_list</a>"
    description: Devuelve una lista paginada de IDs de productos.
    tags:
      - Purchases
  - name: "<a href='/docs/api/endpoints/export/purchases/get_number_of_purchases/'>/purchases/quantity_series</a>"
    description: Devuelve el número total de compras en tu aplicación durante un intervalo de tiempo.
    tags:
      - Purchases
  - name: "<a href='/docs/api/endpoints/export/purchases/get_revenue_series/'>/purchases/revenue_series</a>"
    description: Devuelve el dinero total gastado en tu aplicación durante un intervalo de tiempo.
    tags:
      - Purchases    
  - name: "<a href='/docs/api/endpoints/preference_center/get_create_url_preference_center'>/preference_center/v1/{preferenceCenterExternalId}/url/{userId}</a>"
    description: Crear una URL para un centro de preferencias.
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/preference_center/get_list_preference_center/'>/preference_center/v1/list</a>"
    description: Lista de centros de preferencia disponibles.
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/preference_center/get_view_details_preference_center'>/preference_center/v1/{preferenceCenterExternalId}</a>"
    description: "Vea los detalles de sus centros de preferencias, incluida la fecha de creación y actualización."
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/preference_center/post_create_preference_center'>/preference_center/v1</a>"
    description: Cree un centro de preferencias que permita a los usuarios gestionar sus preferencias de notificación para las campañas de correo electrónico.
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/preference_center/put_update_preference_center'>/preference_center/v1/{preferenceCenterExternalId}</a>"
    description: Actualizar un centro de preferencias.
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk'>/catalogs/{catalog_name}/items</a>"
    description: Elimina varios elementos de tu catálogo.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/'>/catalogs/{catalog_name}/items/{item_id}</a>"
    description: Enumerar un artículo del catálogo y sus detalles.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/'>/catalogs/{catalog_name}/items</a>"
    description: Edita varios elementos de tu catálogo.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/'>/catalogs/{catalog_name}/items</a>"
    description: Crea varios elementos en tu catálogo.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/'>/catalogs/{catalog_name}</a>"
    description: Borrar un catálogo.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/'>/catalogs</a>"
    description: Crear un catálogo.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/'>/catalogs</a>"
    description: Enumera los catálogos de un espacio de trabajo.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>"
    description: Crear un elemento en un catálogo.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>"
    description: Editar un elemento de un catálogo.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/'>/catalogs/{catalog_name}/items</a>"
    description: Devuelve varios elementos del catálogo y su contenido.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>"
    description: Eliminar un elemento de un catálogo.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>"
    description: Sustituye un elemento de un catálogo.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/'>/catalogs/{catalog_name}/items/</a>"
    description: Sustituye varios elementos de un catálogo.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields/'>/catalogs/{catalog_name}/fields/</a>"
    description: Crear varios campos en un catálogo.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field/'>/catalogs/{catalog_name}/fields/{field_name}</a>"
    description: Borrar un campo de un catálogo.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections/'>/catalogs/{catalog_name}/selections</a>"
    description: Crear una selección en un catálogo.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection/'>/catalogs/{catalog_name}/selections/{selection_name}</a>"
    description: Borrar una selección del catálogo.
    tags:
      - Catalogs
  - name: "<a href='/docs/post_create_user_account/'>/scim/v2/Users</a>"
    description: "Cree una nueva cuenta de usuario del cuadro de mandos especificando el correo electrónico, los nombres y apellidos y los permisos (para establecer permisos a nivel de empresa, espacio de trabajo y equipo)."
    tags:
      - SCIM
  - name: "<a href='/docs/get_see_user_account_information/'>/scim/v2/Usuarios/{id}</a>"
    description: Busca una cuenta de usuario existente en el panel especificando su ID de recurso.
    tags:
      - SCIM
  - name: "<a href='/docs/post_update_existing_user_account/'>/scim/v2/Usuarios/{id}</a>"
    description: "Actualice una cuenta de usuario existente en el cuadro de mandos especificando el correo electrónico, los nombres y apellidos, y los permisos (para establecer permisos a nivel de empresa, espacio de trabajo y equipo)."
    tags:
      - SCIM
  - name: "<a href='/docs/delete_existing_dashboard_user/'>/scim/v2/Usuarios/{id}</a>"
    description: Elimina de forma permanente a un usuario existente del panel.
    tags:
      - SCIM
  - name: "<a href='/docs/get_search_existing_dashboard_user_email/'>/scim/v2/Usuarios?filter={userName@example.com}</a>"
    description: Busca una cuenta de usuario existente en el panel especificando su dirección de correo electrónico.
    tags:
      - SCIM
  - name: "<a href='/docs/api/endpoints/cdi/get_integration_list/'>/cdi/integrations</a>"
    description: Devuelve una lista de las integraciones existentes.
    tags:
      - Cloud Data Ingestion
  - name: "<a href='/docs/api/endpoints/cdi/post_job_sync/'>/cdi/integrations/{integration_id}/sync</a>"
    description: Activar una sincronización para una integración determinada.
    tags:
      - Cloud Data Ingestion
  - name: "<a href='/docs/api/endpoints/cdi/get_job_sync_status/'>/cdi/integrations/{integration_id}/job_sync_status</a>"
    description: Devuelve una lista de estados de sincronización.
    tags:
      - Cloud Data Ingestion
  - name: "<a href='/docs/api/endpoints/sdk_authentication/post_create_sdk_authentication_key/'>/app_group/sdk_authentication/crear</a>"
    description: Crea una nueva clave de autenticación SDK para tu aplicación.
    tags:
      - SDK Authentication
  - name: "<a href='/docs/api/endpoints/sdk_authentication/get_sdk_authentication_keys/'>/app_group/sdk_authentication/keys</a>"
    description: Lista las claves de autenticación del SDK para tu aplicación.
    tags:
      - SDK Authentication
  - name: "<a href='/docs/api/endpoints/sdk_authentication/put_primary_sdk_authentication_key/'>/app_group/sdk_authentication/primario</a>"
    description: Establece una clave de autenticación SDK como clave principal de tu aplicación.
    tags:
      - SDK Authentication
  - name: "<a href='/docs/api/endpoints/sdk_authentication/delete_sdk_authentication_key/'>/app_group/sdk_autenticacion/eliminar</a>"
    description: Elimina una clave de autenticación SDK para tu aplicación.
    tags:
      - SDK Authentication  
---