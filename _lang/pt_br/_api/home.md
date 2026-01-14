---
page_order: 0
nav_title: Início
article_title: Guia da API do Braze
layout: api_glossary
glossary_top_header: "Braze API Guide"
glossary_top_text: "Braze provides a high-performance REST API to allow you to track users, send messages, export data, and more. This page lists available Braze API endpoints and their uses."
page_type: glossary
description: "Esta landing page lista os endpoints da API Braze disponíveis e seus usos."
glossary_tag_name: Endpoint Type

glossary_filter_text: "Select endpoint type to narrow the glossary:"

glossary_mid_text: "Endpoint Search"
guide_featured_list:
  - name: Visão geral da API
    image: /assets/img/braze_icons/annotation-info.svg
    link: /docs/api/basics/
  - name: Tipos de identificadores de API
    link: /docs/api/identifier_types/
    image: /assets/img/braze_icons/clipboard-check.svg
  - name: Objetos e filtros
    link: /docs/api/objects_filters/
    image: /assets/img/braze_icons/settings-01.svg
  - name: Erros e respostas
    link: /docs/api/errors/
    image: /assets/img/braze_icons/list.svg
  - name: Retenção de dados
    link: /docs/api/data_retention/
    image: /assets/img/braze_icons/laptop-02.svg
  - name: Limites de frequência
    link: /docs/api/api_limits/
    image: /assets/img/braze_icons/hand.svg

# channel to icon/fa or image mapping
glossary_tags:
  - name: Campanhas
  - name: Canva
  - name: Catálogos
  - name: Blocos de conteúdo
  - name: Eventos personalizados
  - name: Lista de e-mails
  - name: Modelos de e-mail
  - name: KPI
  - name: Compras
  - name: Central de Preferências
  - name: Envio de mensagens
  - name: SCIM
  - name: Autenticação do SDK
  - name: Segmentos
  - name: Envio de mensagens
  - name: SMS
  - name: Grupos de inscrições
  - name: Dados de usuários
  - name: Atividade ao vivo
  - name: Ingestão de dados na nuvem

glossaries:
  - name: "<a href='/docs/api/endpoints/user_data/post_user_alias/'>/users/alias/new</a>"
    description: Adicione novos aliases de usuário para usuários identificados existentes ou para criar novos usuários não identificados.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_users_alias_update/'>/users/alias/update</a>"
    description: Atualize os nomes de alias de usuário existentes para novos nomes de alias de usuário.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_user_delete/'>/users/delete</a>"
    description: Exclua qualquer perfil de usuário especificando um identificador de usuário conhecido.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/export/user_data/post_users_global_control_group/'>/users/export/global_control_group</a>"
    description: Exportar todos os usuários de um Grupo de Controle Global.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/export/user_data/post_users_identifier/'>/users/export/ids</a>"
    description: Exporte dados de qualquer perfil de usuário especificando um identificador de usuário.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/export/user_data/post_users_segment/'>/users/export/segment</a>"
    description: Exporte todos os usuários de um segmento.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename/'>/users/external_ids/rename</a>"
    description: Renomeie as IDs externas de seus usuários.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove/'>/users/external_ids/remove</a>"
    description: Remova as IDs externas antigas e obsoletas de seus usuários.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_user_identify/'>/users/identify</a>"
    description: Identificar um usuário não identificado (somente alias).
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_user_track/'>/users/track</a>"
    description: "Registre eventos personalizados, compras e atualize os atributos do perfil do usuário."
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_users_merge/'>/users/merge</a>"
    description: Mesclar um perfil de usuário em outro usuário.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/'>/campaigns/trigger/send</a>"
    description: Envie mensagens únicas e imediatas para usuários designados por meio da entrega disparada pela API. - Envio de mensagens
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases/'>/canvas/trigger/send</a>"
    description: Envie mensagens de canva por meio de entrega disparada por API. - Envio de mensagens
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_send_messages/'>/messages/send</a>"
    description: Envie mensagens únicas e imediatas para usuários designados por meio da API do Braze.
    tags:
      - Send Messages
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_create_send_ids/'>/sends/id/create</a>"
    description: "Crie IDs de envio que possam ser usados para enviar mensagens e rastrear o desempenho das mensagens de forma programática, sem a criação de campanhas para cada envio."
    tags:
      - Send Messages
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_send_transactional_message/'>/transactional/v1/campaigns/{CAMPAIGN_ID}/send</a>"
    description: Envie mensagens transacionais únicas e imediatas para um usuário designado.
    tags:
      - Send Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/'>/campaigns/trigger/schedule/create</a>"
    description: Envie mensagens de campanha criadas no dashboard por meio de entrega disparada por API.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/'>/campaigns/trigger/schedule/delete</a>"
    description: Cancelar mensagens de campanha de mensagens disparadas pela API que você programou anteriormente antes de serem enviadas.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/'>/campaigns/trigger/schedule/update</a>"
    description: Atualizar campanhas programadas disparadas por API criadas no dashboard.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/'>/canvas/trigger/schedule/delete</a>"
    description: Cancelar uma mensagem do canva que você programou anteriormente via API - disparada antes de ser enviada.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/'>/canvas/trigger/schedule/create</a>"
    description: Programe o envio de mensagens do canva por meio da entrega disparada pela API.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/'>/messages/schedule/update</a>"
    description: Atualizar envios de mensagens programadas. Esse ponto de extremidade aceita atualizações para o <code>schedule</code> ou <code>messages</code> ou ambos.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/'>/messages/schedule/delete</a>"
    description: Cancelar uma mensagem que você programou anteriormente antes de ela ter sido enviada.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_messages/'>/messages/schedule/create</a>"
    description: "Programe o envio de uma campanha, canva ou outra mensagem em um horário determinado."
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/'>/canva/trigger/schedule/update</a>"
    description: Atualize os canvas programadas disparados pela API que foram criados no dashboard.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled/'>/messages/scheduled_broadcasts</a>"
    description: Retorna uma lista JSON de informações sobre campanhas agendadas e canvas de entrada entre agora e um período designado <code>end_time</code> especificado na solicitação.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/live_activity/update/'>/messages/live_activity/update</a>"
    description: Atualizar uma atividade do iOS Live.
    tags:
      - Live Activity
  - name: "<a href='/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status/'>/subscription/status/set</a>"
    description: Atualize em lote o estado da inscrição de até 50 usuários no dashboard da Braze.
    tags:
      - Subscription Groups
  - name: "<a href='/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/'>/v2/subscription/status/set</a>"
    description: Atualize em lote o estado da inscrição de até 50 usuários no dashboard da Braze.
    tags:
      - Subscription Groups
  - name: "<a href='/docs/api/endpoints/subscription_groups/get_list_user_subscription_group_status/'>/subscription/status/get</a>"
    description: Obtenha o estado da inscrição de um usuário em um grupo de inscrições.
    tags:
      - Subscription Groups
  - name: "<a href='/docs/api/endpoints/subscription_groups/get_list_user_subscription_groups/'>/subscription/user/status</a>"
    description: Liste e obtenha os grupos de inscrições de um determinado usuário.
    tags:
      - Subscription Groups
  - name: "<a href='/docs/api/endpoints/email/post_blacklist/'>/email/blacklist</a>"
    description: Cancelar inscrição de um usuário no e-mail e marcá-lo como hard bounce.
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/email/post_remove_hard_bounces/'>/email/bounce/remove</a>"
    description: Remova endereços de e-mail de sua lista de bounce da Braze.
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/email/post_remove_spam/'>/email/spam/remove</a>"
    description: Remova endereços de e-mail de sua lista de spam do Braze.
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/email/post_email_subscription_status/'>/email/status</a>"
    description: Defina o estado da inscrição de e-mail para seus usuários.
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/templates/email_templates/post_create_email_template/'>/templates/email/create</a>"
    description: Crie modelos de e-mail no dashboard do Braze.
    tags:
      - Email Templates
  - name: "<a href='/docs/api/endpoints/templates/email_templates/post_update_email_template/'>/templates/email/update</a>"
    description: Atualize os modelos de e-mail no dashboard do Braze.
    tags:
      - Email Templates
  - name: "<a href='/docs/api/endpoints/email/get_list_hard_bounces/'>/email/hard_bounces</a>"
    description: "Obtenha uma lista de endereços de e-mail que tenham \"hard bounce\" suas mensagens de e-mail em um determinado período de tempo."
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/email/get_query_unsubscribed_email_addresses/'>/email/unsubscribes</a>"
    description: Retornar e-mails que cancelaram inscrição durante o período de <code>start_date</code> para <code>end_date</code>.
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/templates/email_templates/get_see_email_template_information/'>/templates/email/info</a>"
    description: Obtenha informações sobre seus modelos de e-mail.
    tags:
      - Email Templates
  - name: "<a href='/docs/api/endpoints/templates/email_templates/get_list_email_templates/'>/templates/email/list</a>"
    description: Obtenha uma lista dos modelos de e-mail disponíveis em sua conta Braze.
    tags:
      - Email Templates
  - name: "<a href='/docs/api/endpoints/export/campaigns/get_campaign_analytics/'>/campaigns/data_series</a>"
    description: Recupere uma série diária de várias estatísticas de uma campanha ao longo do tempo.
    tags:
      - Campaigns
  - name: "<a href='/docs/api/endpoints/export/campaigns/get_campaign_details/'>/campaigns/details</a>"
    description: Recupere informações relevantes sobre uma campanha específica.
    tags:
      - Campaigns
  - name: "<a href='/docs/api/endpoints/export/campaigns/get_campaigns/'>/campaigns/list</a>"
    description: "Exporte uma lista de campanhas, cada uma das quais incluirá seu nome, o identificador da API da campanha, se é uma campanha de API e as tags associadas à campanha."
    tags:
      - Campaigns
  - name: "<a href='/docs/api/endpoints/export/campaigns/get_send_analytics/'>/sends/data_series</a>"
    description: Recupere uma série diária de várias estatísticas para um rastreamento <code>send_id</code>.
    tags:
      - Campaigns
  - name: "<a href='/docs/api/endpoints/export/canvas/get_canvas_analytics/'>/canvas/data_series</a>"
    description: Exportar dados de séries temporais para um Canva.
    tags:
      - Canvas
  - name: "<a href='/docs/api/endpoints/export/canvas/get_canvas_analytics_summary/'>/canva/data_summary</a>"
    description: "Exporte rollups de dados de séries temporais para um canva, fornecendo um resumo conciso dos resultados de um canva."
    tags:
      - Canvas
  - name: "<a href='/docs/api/endpoints/export/canvas/get_canvas_details/'>/canvas/details</a>"
    description: "Exporte metadados sobre um canva, como o nome, a hora de criação, o status atual e muito mais."
    tags:
      - Canvas
  - name: "<a href='/docs/api/endpoints/export/canvas/get_canvases/'>/canvas/list</a>"
    description: "Exporte uma lista de canvas, incluindo o nome, o identificador da API dos canvas e as tags associadas."
    tags:
      - Canvas
  - name: "<a href='/docs/api/endpoints/export/segments/get_segment_analytics/'>/segments/data_series</a>"
    description: Recupera uma série diária do tamanho estimado de um segmento ao longo do tempo.
    tags:
      - Segments
  - name: "<a href='/docs/api/endpoints/export/segments/get_segment_details/'>/segments/details</a>"
    description: Recupere informações relevantes sobre um segmento.
    tags:
      - Segments
  - name: "<a href='/docs/api/endpoints/export/segments/get_segment/'>/segments/list</a>"
    description: "Exporte uma lista de segmentos, cada um dos quais incluirá seu nome, o identificador da API do segmento e se tem a análise de dados ativada."
    tags:
      - Segments
  - name: "<a href='/docs/api/endpoints/export/sessions/get_sessions_analytics/'>/sessions/data_series</a>"
    description: Recupere uma série do número de sessões do seu app em um período de tempo designado.
    tags:
      - Sessions
  - name: "<a href='/docs/api/endpoints/export/custom_attributes/get_custom_attributes/'>/custom_attributes</a>"
    description: "Exporte uma lista de atributos personalizados, incluindo o nome, a descrição, o tipo de dados, o comprimento da matriz (se aplicável), o status e as tags associadas."
    tags:
      - Custom Attributes
  - name: "<a href='/docs/api/endpoints/export/custom_events/get_custom_events_analytics/'>/events/data_series</a>"
    description: Recupere uma série do número de ocorrências de um evento personalizado em seu app durante um período de tempo designado.
    tags:
      - Custom Events
  - name: "<a href='/docs/api/endpoints/export/custom_events/get_custom_events_data/'>/events</a>"
    description: "Exporte uma lista de eventos personalizados, incluindo o nome, a descrição, o status, as tags associadas e a inclusão de relatórios de análise de dados."
    tags:
      - Custom Events
  - name: "<a href='/docs/api/endpoints/export/custom_events/get_custom_events/'>/events/list</a>"
    description: Exporte uma lista de nomes de eventos personalizados que foram registrados para o seu aplicativo.
    tags:
      - Custom Events
  - name: "<a href='/docs/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/'>/content_blocks/create</a>"
    description: Crie um bloco de conteúdo de e-mail.
    tags:
      - Content Blocks
  - name: "<a href='/docs/api/endpoints/templates/content_blocks_templates/post_update_content_block/'>/content_blocks/update</a>"
    description: Atualizar um bloco de conteúdo de e-mail.
    tags:
      - Content Blocks
  - name: "<a href='/docs/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/'>/content_blocks/info</a>"
    description: Informações de chamada para seu bloco de conteúdo de e-mail existente.
    tags:
      - Content Blocks
  - name: "<a href='/docs/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/'>/content_blocks/list</a>"
    description: Liste suas informações de blocos de conteúdo existentes.
    tags:
      - Content Blocks
  - name: "<a href='/docs/api/endpoints/export/kpi/get_kpi_dau_date/'>/kpi/dau/data_series</a>"
    description: Recupere uma série diária do número total de usuários ativos exclusivos em cada data.
    tags:
      - KPI
  - name: "<a href='/docs/api/endpoints/export/kpi/get_kpi_mau_30_days/'>/kpi/mau/data_series</a>"
    description: Recupere uma série diária do número total de usuários ativos diários exclusivos em uma janela contínua de 30 dias.
    tags:
      - KPI
  - name: "<a href='/docs/api/endpoints/export/kpi/get_kpi_daily_new_users_date/'>/kpi/new_users/data_series</a>"
    description: Recupere uma série diária do número total de novos usuários em cada data.
    tags:
      - KPI
  - name: "<a href='/docs/api/endpoints/export/kpi/get_kpi_uninstalls_date/'>/kpi/uninstalls/data_series</a>"
    description: Recupera uma série diária do número total de desinstalações em cada data.
    tags:
      - KPI
  - name: "<a href='/docs/api/endpoints/sms/post_remove_invalid_numbers/'>/sms/invalid_phone_numbers/remove</a>"
    description: "Remover números de telefone \"inválidos\" da lista de inválidos no Braze. Isso pode ser usado para revalidar números de telefone depois de terem sido marcados como inválidos."
    tags:
      - SMS
  - name: "<a href='/docs/api/endpoints/sms/get_query_invalid_numbers/'>/sms/invalid_phone_numbers</a>"
    description: "Obtenha uma lista de números de telefone que foram considerados \"inválidos\" em um determinado período de tempo."
    tags:
      - SMS
  - name: "<a href='/docs/api/endpoints/export/purchases/get_list_product_id/'>/purchases/product_list</a>"
    description: Retorna uma lista paginada de IDs de produtos.
    tags:
      - Purchases
  - name: "<a href='/docs/api/endpoints/export/purchases/get_number_of_purchases/'>/purchases/quantity_series</a>"
    description: Retorna o número total de compras em seu app em um intervalo de tempo.
    tags:
      - Purchases
  - name: "<a href='/docs/api/endpoints/export/purchases/get_revenue_series/'>/purchases/revenue_series</a>"
    description: Retorna o total de dinheiro gasto em seu app em um intervalo de tempo.
    tags:
      - Purchases    
  - name: "<a href='/docs/api/endpoints/preference_center/get_create_url_preference_center'>/preference_center/v1/{preferenceCenterExternalId}/url/{userId}</a>"
    description: Crie um URL para uma Central de Preferências.
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/preference_center/get_list_preference_center/'>/preference_center/v1/list</a>"
    description: Liste os centros de preferências disponíveis.
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/preference_center/get_view_details_preference_center'>/preference_center/v1/{preferenceCenterExternalId}</a>"
    description: "Veja os detalhes de suas Centrais de Preferências, inclusive quando foram criadas e atualizadas."
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/preference_center/post_create_preference_center'>/preference_center/v1</a>"
    description: Crie uma central de Preferências para permitir que os usuários gerenciem suas preferências de notificação para campanhas de e-mail.
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/preference_center/put_update_preference_center'>/preference_center/v1/{preferenceCenterExternalId}</a>"
    description: Atualizar uma Central de Preferências.
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk'>/catalogs/{catalog_name}/items</a>"
    description: Excluir vários itens em seu catálogo.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/'>/catalogs/{catalog_name}/items/{item_id}</a>"
    description: Listar um item de catálogo e seus detalhes.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/'>/catalogs/{catalog_name}/items</a>"
    description: Edite vários itens em seu catálogo.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/'>/catalogs/{catalog_name}/items</a>"
    description: Crie vários itens em seu catálogo.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/'>/catalogs/{catalog_name}</a>"
    description: Excluir um catálogo.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/'>/catalogs</a>"
    description: Criar um catálogo.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/'>/catalogs</a>"
    description: Listar os catálogos em um espaço de trabalho.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>"
    description: Criar um item em um catálogo.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>"
    description: Editar um item em um catálogo.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/'>/catalogs/{catalog_name}/items</a>"
    description: Retorna vários itens de catálogo e seu conteúdo.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>"
    description: Excluir um item em um catálogo.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>"
    description: Substituir um item em um catálogo.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/'>/catalogs/{catalog_name}/items/</a>"
    description: Substituir vários itens em um catálogo.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields/'>/catalogs/{catalog_name}/fields/</a>"
    description: Criar vários campos em um catálogo.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field/'>/catalogs/{catalog_name}/fields/{field_name}</a>"
    description: Excluir um campo de um catálogo.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections/'>/catalogs/{catalog_name}/selections</a>"
    description: Criar uma seleção em um catálogo.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection/'>/catalogs/{catalog_name}/selections/{selection_name}</a>"
    description: Excluir uma seleção de catálogo.
    tags:
      - Catalogs
  - name: "<a href='/docs/post_create_user_account/'>/scim/v2/Users</a>"
    description: "Crie uma nova conta de usuário do dashboard especificando e-mail, nome e sobrenome, permissões (para definir permissões no nível da empresa, do espaço de trabalho e da equipe)."
    tags:
      - SCIM
  - name: "<a href='/docs/get_see_user_account_information/'>/scim/v2/Users/{id}</a>"
    description: Procure uma conta de usuário existente no dashboard especificando o ID do recurso.
    tags:
      - SCIM
  - name: "<a href='/docs/post_update_existing_user_account/'>/scim/v2/Users/{id}</a>"
    description: "Atualize uma conta de usuário do dashboard existente especificando e-mail, nomes e sobrenomes, permissões (para definir permissões no nível da empresa, do espaço de trabalho e da equipe)."
    tags:
      - SCIM
  - name: "<a href='/docs/delete_existing_dashboard_user/'>/scim/v2/Users/{id}</a>"
    description: Exclua permanentemente um usuário do dashboard existente.
    tags:
      - SCIM
  - name: "<a href='/docs/get_search_existing_dashboard_user_email/'>/scim/v2/Users?filter={userName@example.com}</a>"
    description: Procure uma conta de usuário existente no dashboard especificando seu e-mail.
    tags:
      - SCIM
  - name: "<a href='/docs/api/endpoints/cdi/get_integration_list/'>/cdi/integrations</a>"
    description: Retorna uma lista de integrações existentes.
    tags:
      - Cloud Data Ingestion
  - name: "<a href='/docs/api/endpoints/cdi/post_job_sync/'>/cdi/integrations/{integration_id}/sync</a>"
    description: Disparar uma sincronização para uma determinada integração.
    tags:
      - Cloud Data Ingestion
  - name: "<a href='/docs/api/endpoints/cdi/get_job_sync_status/'>/cdi/integrations/{integration_id}/job_sync_status</a>"
    description: Retorna uma lista de status de sincronização.
    tags:
      - Cloud Data Ingestion
  - name: "<a href='/docs/api/endpoints/sdk_authentication/post_create_sdk_authentication_key/'>/app_group/sdk_authentication/create</a>"
    description: Crie uma nova chave de autenticação do SDK para seu app.
    tags:
      - SDK Authentication
  - name: "<a href='/docs/api/endpoints/sdk_authentication/get_sdk_authentication_keys/'>/app_group/sdk_authentication/keys</a>"
    description: Liste as chaves de autenticação do SDK para seu app.
    tags:
      - SDK Authentication
  - name: "<a href='/docs/api/endpoints/sdk_authentication/put_primary_sdk_authentication_key/'>/app_group/sdk_authentication/primary</a>"
    description: Defina uma chave de autenticação do SDK como a chave primária de seu app.
    tags:
      - SDK Authentication
  - name: "<a href='/docs/api/endpoints/sdk_authentication/delete_sdk_authentication_key/'>/app_group/sdk_authentication/delete</a>"
    description: Exclua uma chave de autenticação do SDK para seu app.
    tags:
      - SDK Authentication  
---