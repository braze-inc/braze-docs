# Braze MCP Server-Funktionen

> Der Braze MCP Server stellt eine Reihe von schreibgeschützten API-Funktionen bereit, die auf bestimmte Braze REST API Endpunkte abgebildet werden. MCP-Clients wie Claude und Cursor können diese Funktionen aufrufen, um Daten abzurufen, ohne auf PII zuzugreifen oder Änderungen an Ihrem Workspace vorzunehmen. Weitere allgemeine Informationen finden Sie unter [Braze MCP Server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "Entwickler:in" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Voraussetzungen

Bevor Sie dieses Feature nutzen können, müssen Sie [den Braze MCP Server einrichten]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "Entwickler:in" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## Verfügbare Braze API-Funktionen

Dies sind die API-Funktionen, die Ihr MCP Client referenziert, um mit dem Braze MCP Server zu interagieren:

### Allgemeine Funktionen

| Funktion | Beschreibung |
|----------|-------------|
| `list_functions` | Listet alle verfügbaren Braze API-Funktionen mit ihren Beschreibungen und Parametern auf |
| `call_function` | Ruft eine bestimmte Braze API-Funktion mit den angegebenen Parametern auf |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Kampagnen

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `get_campaign_list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | Exportieren Sie eine Liste von Kampagnen mit Metadaten. |
| `get_campaign_details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | Erhalten Sie detaillierte Informationen über bestimmte Kampagnen. |
| `get_campaign_dataseries` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | Rufen Sie Analytics-Daten aus Zeitreihen für Kampagnen ab. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Canvase

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `get_canvas_list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | Exportieren Sie eine Liste von Canvase mit Metadaten. |
| `get_canvas_details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | Erhalten Sie detaillierte Informationen über bestimmte Canvase. |
| `get_canvas_data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | Erhalten Sie zusammenfassende Analytics für die Performance von Canvas. |
| `get_canvas_data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | Rufen Sie Zeitreihen-Analytics-Daten für Canvase ab. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Kataloge

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `get_catalogs` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | Gibt eine Liste der Kataloge in einem Workspace zurück. |
| `get_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | Liefern Sie mehrere Katalogartikel und deren Inhalt mit Paginierung. |
| `get_catalog_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | Gibt einen bestimmten Artikel und dessen Inhalt nach ID zurück. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Ingestion von Cloud-Daten

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `list_integrations` | [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | Gibt eine Liste der vorhandenen CDI Integrationen zurück. |
| `get_integration_job_sync_status` | [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | Liefert frühere Synchronisierungsstatus für eine bestimmte CDI Integration. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Content-Blöcke

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `get_content_blocks_list` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | Listen Sie Ihre verfügbaren Content-Blöcke auf. |
| `get_content_blocks_info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | Erhalten Sie Informationen über Ihre Content-Blöcke. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Angepasste Attribute

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `get_custom_attributes` | [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) | Exportieren Sie angepasste Attribute, die für Ihre App aufgezeichnet wurden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Events

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `get_events_list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | Exportieren Sie eine Liste der angepassten Events, die für Ihre App aufgezeichnet wurden. |
| `get_events_data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | Rufen Sie Zeitreihendaten für angepasste Events ab. |
| `get_events` | [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) | Erhalten Sie detaillierte Daten zu einem Ereignis mit Paginierung. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### KPIs

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `get_new_users_data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | Tägliche Zählung der neuen Nutzer:innen. |
| `get_dau_data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | Täglich aktive Nutzer:innen Zeitreihendaten. |
| `get_mau_data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | Monatliche aktive:r Nutzer:innen Zeitreihendaten. |
| `get_uninstalls_data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | App Zeitreihen-Daten deinstallieren. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Nachrichten

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `get_scheduled_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled) | Liste der anstehenden geplanten Kampagnen und Canvase. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Präferenzzentren

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `get_preference_centers` | [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center) | Listen Sie Ihre verfügbaren Präferenzzentren auf. |
| `get_preference_center_details` | [`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | Zeigen Sie Details zu einem bestimmten Einstellungscenter an, einschließlich HTML-Inhalt und Optionen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Käufe

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `get_product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | Exportieren Sie eine paginierte Liste von Produkt IDs. |
| `get_revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | Revenue Analytics Zeitreihendaten. |
| `get_quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | Daten aus Zeitreihen zum Kauf von Mengen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Segmente

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `get_segment_list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | Exportieren Sie die Liste der Segmente mit dem Analytics Tracking-Status. |
| `get_segment_data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | Zeitreihen-Analytics-Daten für Segmente. |
| `get_segment_details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | Detaillierte Informationen über bestimmte Segmente. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Sendungen

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `get_send_data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | Tägliche Analytics für getrackte Kampagnensendungen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Sitzungen

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `get_session_data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | Zeitreihendaten für die Anzahl der App-Sitzungen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### SDK-Authentifizierungsschlüssel

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `get_sdk_authentication_keys` | [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | Listen Sie alle SDK Authentifizierungsschlüssel für Ihre App auf. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Abo

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `get_user_subscription_groups` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) | Auflisten und Abrufen der Abo-Gruppen eines bestimmten Nutzer:innen. |
| `get_subscription_group_status` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) | Holen Sie sich den Abo-Status eines Nutzers:innen in einer Abo-Gruppe. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Vorlagen

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `get_email_templates_list` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | Listen Sie Ihre verfügbaren E-Mail Templates auf. |
| `get_email_template_info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | Informieren Sie sich über Ihre E-Mail Templates. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% multi_lang_include mcp_server/legal_disclaimer.md %}
