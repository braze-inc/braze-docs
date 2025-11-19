# Braze MCP 서버 기능

> Braze MCP 서버는 특정 Braze REST API 엔드포인트에 매핑되는 읽기 전용 API 함수 집합을 노출합니다. Claude 및 Cursor와 같은 MCP 클라이언트는 이러한 함수를 호출하여 PII에 액세스하거나 작업 공간을 변경하지 않고도 데이터를 검색할 수 있습니다. 자세한 내용은 [Braze MCP 서버]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "개발자" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## 필수 조건

이 기능을 사용하려면 먼저 [Braze MCP 서버 설정]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "개발자" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## 사용 가능한 Braze API 기능

다음은 MCP 클라이언트가 The Braze MCP 서버와 상호 작용하기 위해 참조하는 API 함수입니다:

### 일반 기능

| 기능 | 설명 |
|----------|-------------|
| `list_functions` | 사용 가능한 모든 Braze API 함수를 설명 및 매개변수와 함께 나열합니다. |
| `call_function` | 제공된 파라미터로 특정 Braze API 함수를 호출합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### 캠페인

| 기능 | Endpoint | 설명 |
|----------|----------|-------------|
| `get_campaign_list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | 메타데이터가 포함된 캠페인 목록을 내보냅니다. |
| `get_campaign_details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | 특정 캠페인에 대한 자세한 정보를 확인하세요. |
| `get_campaign_dataseries` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | 캠페인에 대한 시계열 분석 데이터를 검색합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### 캔버스

| 기능 | Endpoint | 설명 |
|----------|----------|-------------|
| `get_canvas_list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | 메타데이터가 포함된 캔버스 목록을 내보냅니다. |
| `get_canvas_details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | 특정 캔버스에 대한 자세한 정보를 확인하세요. |
| `get_canvas_data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | 캔버스 성능/성과에 대한 요약 분석을 확인하세요. |
| `get_canvas_data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | 캔버스에 대한 시계열 분석 데이터를 검색합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### 카탈로그

| 기능 | Endpoint | 설명 |
|----------|----------|-------------|
| `get_catalogs` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | 워크스페이스의 카탈로그 목록을 반환합니다. |
| `get_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | 페이지 매김을 지원하여 여러 카탈로그 항목과 해당 콘텐츠를 반환합니다. |
| `get_catalog_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | 특정 카탈로그 항목과 해당 콘텐츠를 ID별로 반환합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### 클라우드 데이터 수집

| 기능 | Endpoint | 설명 |
|----------|----------|-------------|
| `list_integrations` | [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | 기존 CDI 통합 목록을 반환합니다. |
| `get_integration_job_sync_status` | [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | 특정 CDI 통합에 대한 과거 동기화 상태를 반환합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### 콘텐츠 블록

| 기능 | Endpoint | 설명 |
|----------|----------|-------------|
| `get_content_blocks_list` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | 사용 가능한 콘텐츠 블록을 나열합니다. |
| `get_content_blocks_info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | 콘텐츠 블록에 대한 정보를 확인하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Custom Attributes

| 기능 | Endpoint | 설명 |
|----------|----------|-------------|
| `get_custom_attributes` | [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) | 앱에 대해 기록된 커스텀 속성을 내보냅니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Events

| 기능 | Endpoint | 설명 |
|----------|----------|-------------|
| `get_events_list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | 앱에 대해 기록된 커스텀 이벤트 목록을 내보냅니다. |
| `get_events_data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | 커스텀 이벤트에 대한 시계열 데이터를 검색합니다. |
| `get_events` | [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) | 페이지 매김을 지원하여 상세한 이벤트 데이터를 확인하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### KPI

| 기능 | Endpoint | 설명 |
|----------|----------|-------------|
| `get_new_users_data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | 일일 신규 사용자 수 시리즈입니다. |
| `get_dau_data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | 일일 활성 사용자 시계열 데이터입니다. |
| `get_mau_data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | 월간 활성 사용자 시계열 데이터입니다. |
| `get_uninstalls_data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | 앱에서 시계열 데이터를 제거합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Messages

| 기능 | Endpoint | 설명 |
|----------|----------|-------------|
| `get_scheduled_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled) | 예정된 캠페인과 캔버스를 나열합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### 환경설정 센터

| 기능 | Endpoint | 설명 |
|----------|----------|-------------|
| `get_preference_centers` | [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center) | 사용 가능한 기본 설정 센터를 나열합니다. |
| `get_preference_center_details` | [`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | HTML 콘텐츠 및 옵션을 포함하여 특정 환경설정 센터에 대한 세부 정보를 확인합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Purchases

| 기능 | Endpoint | 설명 |
|----------|----------|-------------|
| `get_product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | 제품 ID의 페이지가 지정된 목록을 내보냅니다. |
| `get_revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | 매출 분석 시계열 데이터. |
| `get_quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | 구매 수량 시계열 데이터. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### 세그먼트

| 기능 | Endpoint | 설명 |
|----------|----------|-------------|
| `get_segment_list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | 분석 추적 상태와 함께 세그먼트 목록을 내보냅니다. |
| `get_segment_data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | 세그먼트에 대한 시계열 분석 데이터. |
| `get_segment_details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | 특정 세그먼트에 대한 자세한 정보. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Sends

| 기능 | Endpoint | 설명 |
|----------|----------|-------------|
| `get_send_data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | 추적된 캠페인 전송에 대한 일일 분석. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### 세션

| 기능 | Endpoint | 설명 |
|----------|----------|-------------|
| `get_session_data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | 앱 세션 수에 대한 시계열 데이터입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### 소프트웨어 개발 키트 인증 키

| 기능 | Endpoint | 설명 |
|----------|----------|-------------|
| `get_sdk_authentication_keys` | [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | 앱의 모든 소프트웨어 개발 키트 인증 키를 나열합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### 구독

| 기능 | Endpoint | 설명 |
|----------|----------|-------------|
| `get_user_subscription_groups` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) | 특정 사용자의 구독 그룹을 나열하고 가져옵니다. |
| `get_subscription_group_status` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) | 구독 그룹에 속한 사용자의 구독 상태를 가져옵니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Templates

| 기능 | Endpoint | 설명 |
|----------|----------|-------------|
| `get_email_templates_list` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | 사용 가능한 이메일 템플릿을 나열합니다. |
| `get_email_template_info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | 이메일 템플릿에 대한 정보를 얻으세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% multi_lang_include mcp_server/legal_disclaimer.md %}
