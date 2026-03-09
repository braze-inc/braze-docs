# Fonctions du serveur Braze MCP

> Le serveur Braze MCP fournit un ensemble de fonctions API en lecture seule qui effectuent le mappage avec des endpoints API REST Braze spécifiques. Les clients MCP tels que Claude et Cursor peuvent appeler ces fonctions pour récupérer des données sans accéder aux informations personnelles identifiables ni apporter de modifications à votre espace de travail. Pour obtenir des informations générales, veuillez consulter [le serveur Braze MCP]{% if include.section == "user" %}.{{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/mcp_server/){% endif %}

{% multi_lang_include mcp_server/beta_alert.md %}

## Conditions préalables

Avant de pouvoir utiliser cette fonctionnalité, il est nécessaire de configurer le serveur Braze MCP.{% if include.section == "user" %}{{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}

## Fonctions API Braze disponibles

Votre client MCP fait référence aux fonctions API suivantes pour interagir avec le serveur Braze MCP :
### Fonctions générales

| Fonction | Description |
|----------|-------------|
| `list_functions` | Répertorie toutes les fonctions API Braze disponibles avec leurs descriptions et leurs paramètres. |
| `call_function` | Appelle une fonction API Braze spécifique avec les paramètres fournis. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Campagnes

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `get_campaign_list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | Veuillez exporter une liste des campagnes avec les métadonnées. |
| `get_campaign_details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | Obtenez des informations détaillées sur des campagnes spécifiques. |
| `get_campaign_dataseries` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | Récupérer les données d’analyse chronologiques pour les campagnes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Canvas

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `get_canvas_list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | Veuillez exporter une liste des toiles avec les métadonnées. |
| `get_canvas_details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | Obtenez des informations détaillées sur des toiles spécifiques. |
| `get_canvas_data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | Obtenez des analyses sommaires sur les performances de Canvas. |
| `get_canvas_data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | Récupérer les données d’analyse chronologiques pour les canevas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Catalogues

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `get_catalogs` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | Renvoie une liste des catalogues dans un espace de travail. |
| `get_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | Renvoyer plusieurs éléments du catalogue et leur contenu avec prise en charge de la pagination. |
| `get_catalog_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | Renvoie un élément spécifique du catalogue et son contenu par ID. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Ingestion de données cloud

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `list_integrations` | [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | Renvoie une liste des intégrations CDI existantes. |
| `get_integration_job_sync_status` | [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | Renvoie les statuts de synchronisation passés pour une intégration CDI donnée. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Blocs de contenu

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `get_content_blocks_list` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | Veuillez énumérer les blocs de contenu disponibles. |
| `get_content_blocks_info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | Obtenez des informations sur vos blocs de contenu. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Attributs personnalisés

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `get_custom_attributes` | [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) | Exportez les attributs personnalisés enregistrés pour votre application. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Événements

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `get_events_list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | Veuillez exporter une liste des événements personnalisés enregistrés pour votre application. |
| `get_events_data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | Récupérer les données chronologiques pour les événements personnalisés. |
| `get_events` | [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) | Obtenez des données détaillées sur les événements avec prise en charge de la pagination. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Indicateurs clé de performance

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `get_new_users_data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | Série quotidienne du nombre de nouveaux utilisateurs. |
| `get_dau_data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | Données chronologiques relatives aux utilisateurs actifs par jour. |
| `get_mau_data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | Données chronologiques sur les utilisateurs actifs par mois. |
| `get_uninstalls_data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | Données chronologiques relatives à la désinstallation d'applications. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Messages

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `get_scheduled_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled) | Veuillez répertorier les campagnes et les canevas en cours de planification. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Centres de préférences

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `get_preference_centers` | [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center) | Veuillez indiquer vos centres de préférences disponibles. |
| `get_preference_center_details` | [`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | Veuillez consulter les détails d'un centre de préférences spécifique, y compris le contenu HTML et les options. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Achats

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `get_product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | Veuillez exporter la liste paginée des ID des produits. |
| `get_revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | Données chronologiques relatives à l'analyse du chiffre d'affaires. |
| `get_quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | Veuillez acquérir les données chronologiques relatives aux quantités achetées. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Segments

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `get_segment_list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | Veuillez exporter la liste des segments avec le statut de suivi analytique. |
| `get_segment_data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | Données d'analyse chronologique pour les segments. |
| `get_segment_details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | Informations détaillées sur des segments spécifiques. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Envois

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `get_send_data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | Analyses quotidiennes des envois de campagnes suivies. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Sessions

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `get_session_data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | Données chronologiques relatives au nombre de sessions d'application. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Clés d'authentification SDK

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `get_sdk_authentication_keys` | [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | Veuillez lister toutes les clés d'authentification SDK pour votre application. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Abonnement

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `get_user_subscription_groups` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) | Répertorier et obtenir les groupes d’abonnement d’un certain utilisateur. |
| `get_subscription_group_status` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) | Obtenir le statut d’abonnement d’un utilisateur dans un groupe d’abonnement. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Modèles

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `get_email_templates_list` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | Veuillez énumérer les modèles d'e-mails disponibles. |
| `get_email_template_info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | Obtenir des informations sur vos modèles d’e-mail. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% multi_lang_include mcp_server/legal_disclaimer.md %}
