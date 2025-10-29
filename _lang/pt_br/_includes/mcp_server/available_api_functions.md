# Funções do servidor Braze MCP

> O servidor Braze MCP expõe um conjunto de funções API somente de leitura que mapeiam para pontos de extremidade específicos da Braze REST API. Clientes MCP como Claude e Cursor podem chamar essas funções para recuperar dados sem acessar IPI ou fazer alterações no seu espaço de trabalho. Para saber mais sobre informações gerais, consulte [Braze MCP server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Pré-requisitos

Antes de poder usar esse recurso, você precisará [configurar o servidor Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## Funções disponíveis da API do Braze

Essas são as funções da API que seu cliente MCP referencia para interagir com o servidor Braze MCP:

### Funções gerais

| Função | Descrição |
|----------|-------------|
| `list_functions` | Lista todas as funções disponíveis da Braze API com suas descrições e parâmetros |
| `call_function` | Chama uma função específica da Braze API com os parâmetros fornecidos |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Campanhas

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `get_campaign_list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | Exportar uma lista de campanhas com metadados. |
| `get_campaign_details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | Obtenha informações detalhadas sobre campanhas específicas. |
| `get_campaign_dataseries` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | Recupere dados de análises de séries temporais para campanhas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Canvas

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `get_canvas_list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | Exportar uma lista de telas com metadados. |
| `get_canvas_details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | Obtenha informações detalhadas sobre telas específicas. |
| `get_canvas_data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | Obtenha análises resumidas da performance do Canva. |
| `get_canvas_data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | Recupere dados de análises de séries temporais para Canvas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Catálogos

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `get_catalogs` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | Retorna uma lista de catálogos em um espaço de trabalho. |
| `get_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | Retorna vários itens de catálogo e seu conteúdo com suporte a paginação. |
| `get_catalog_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | Retorna um item de catálogo específico e seu conteúdo por ID. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Ingestão de dados na nuvem

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `list_integrations` | [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | Retorna uma lista das integrações CDI existentes. |
| `get_integration_job_sync_status` | [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | Retorna os status de sincronização anteriores para uma determinada integração CDI. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Blocos de conteúdo

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `get_content_blocks_list` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | Liste seus blocos de conteúdo disponíveis. |
| `get_content_blocks_info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | Obtenha informações sobre seus blocos de conteúdo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Atributos personalizados

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `get_custom_attributes` | [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) | Exporte atributos personalizados registrados para o seu app. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Eventos

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `get_events_list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | Exporte uma lista de eventos personalizados registrados para o seu app. |
| `get_events_data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | Recupere dados de séries temporais para eventos personalizados. |
| `get_events` | [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) | Obtenha dados detalhados de eventos com suporte a paginação. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### KPIs

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `get_new_users_data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | Série diária de contagens de novos usuários. |
| `get_dau_data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | Dados de série temporal de usuários ativos diários. |
| `get_mau_data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | Dados de série temporal de usuários ativos mensais. |
| `get_uninstalls_data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | Desinstalação do app de dados de séries temporais. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Mensagens

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `get_scheduled_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled) | Liste as próximas campanhas e telas programadas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Centrais de Preferências

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `get_preference_centers` | [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center) | Liste seus centros de preferências disponíveis. |
| `get_preference_center_details` | [`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | Visualize os detalhes de um centro de preferências específico, incluindo o conteúdo e as opções de HTML. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Compras

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `get_product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | Exportar lista paginada de IDs de produtos. |
| `get_revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | Dados de séries temporais de análise de receitas. |
| `get_quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | Dados de séries temporais de quantidade de compra. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Segmentos

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `get_segment_list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | Exporte a lista de segmentos com status de rastreamento de análise de dados. |
| `get_segment_data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | Dados de análises de séries temporais para segmentos. |
| `get_segment_details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | Informações detalhadas sobre segmentos específicos. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Envios

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `get_send_data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | Análise diária de dados para envios de campanhas rastreadas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Sessões

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `get_session_data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | Dados de séries temporais para contagens de sessões do app. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Chaves de autenticação do SDK

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `get_sdk_authentication_keys` | [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | Liste todas as chaves de autenticação do SDK para seu app. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Inscrição

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `get_user_subscription_groups` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) | Liste e obtenha os grupos de inscrições de um determinado usuário. |
| `get_subscription_group_status` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) | Obtenha o estado da inscrição de um usuário em um grupo de inscrições. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Modelos

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `get_email_templates_list` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | Liste seus modelos de e-mail disponíveis. |
| `get_email_template_info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | Obtenha informações sobre seus modelos de e-mail. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% multi_lang_include mcp_server/legal_disclaimer.md %}
