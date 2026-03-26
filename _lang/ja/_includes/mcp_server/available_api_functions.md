# Braze MCPサーバー機能

> Braze MCPサーバーは、特定のBraze REST APIエンドポイントに対応する読み取り専用API関数のセットを公開している。MCPクライアントであるClaudeやCursorは、これらの関数を呼び出すことで、個人を特定できる情報（PII）にアクセスしたりワークスペースを変更したりすることなくデータを取得できる。より一般的な情報については、[Braze MCPサーバー]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}を参照せよ。

{% multi_lang_include mcp_server/beta_alert.md %}

## 前提条件

この機能を使う前に、[Braze MCPサーバーの設定]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}が必要だ。

## 利用可能なBraze API関数

MCPクライアントは、Braze MCPサーバーとやり取りするために以下のAPI関数を参照する：
### 一般的な機能

| 機能 | 説明 |
|----------|-------------|
| `list_functions` | 利用可能なすべてのBraze API関数を、説明とパラメータと共に一覧表示する |
| `call_function` | 指定されたパラメータで特定のBraze API関数を呼び出す |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### キャンペーン

| 機能 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_campaign_list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | キャンペーンのリストとメタデータをエクスポートする。 |
| `get_campaign_details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | 特定のキャンペーンに関する詳細情報を入手する。 |
| `get_campaign_dataseries` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | キャンペーンの時系列分析データを取得する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Canvases

| 機能 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_canvas_list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | キャンバスのリストをメタデータと共にエクスポートする。 |
| `get_canvas_details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | 特定のキャンバスについて詳細な情報を得る。 |
| `get_canvas_data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | キャンバスのパフォーマンスに関する要約分析を取得する。 |
| `get_canvas_data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | キャンバスの時系列分析データを取得する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### カタログ

| 機能 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_catalogs` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | ワークスペース内のカタログのリストを返す。 |
| `get_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | ページネーションをサポートして、複数のカタログアイテムとその内容を返す。 |
| `get_catalog_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | 特定のカタログアイテムとその内容をIDで返す。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### クラウドデータ取り込み

| 機能 | エンドポイント | 説明 |
|----------|----------|-------------|
| `list_integrations` | [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | 既存のCDI統合のリストを返す。 |
| `get_integration_job_sync_status` | [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | 指定されたCDI統合の過去の同期ステータスを返す。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### コンテンツブロック

| 機能 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_content_blocks_list` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | 利用可能なコンテンツブロックをリストアップせよ。 |
| `get_content_blocks_info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | コンテンツブロックに関する情報を入手する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### カスタム属性

| 機能 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_custom_attributes` | [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) | アプリ用に記録されたカスタム属性をエクスポートする。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### イベント

| 機能 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_events_list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | アプリ用に記録されたカスタムイベントのリストをエクスポートする。 |
| `get_events_data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | カスタムイベントの時系列データを取得する。 |
| `get_events` | [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) | ページネーション機能付きの詳細なイベントデータを取得する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### KPI

| 機能 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_new_users_data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | 新規ユーザー数の日次推移。 |
| `get_dau_data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | デイリーアクティブユーザーの時系列データ。 |
| `get_mau_data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | 月間アクティブユーザーの時系列データ。 |
| `get_uninstalls_data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | アプリのアンインストール時系列データ。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### メッセージ

| 機能 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_scheduled_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled) | 今後のスケジュールされたキャンペーンとキャンバスを一覧表示する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### ユーザー設定センター

| 機能 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_preference_centers` | [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center) | 利用可能なユーザー設定センターをリストアップせよ。 |
| `get_preference_center_details` | [`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | 特定のユーザー設定センターの詳細を表示する。これにはHTMLコンテンツとオプションが含まれる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### 購入

| 機能 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | 商品IDのページ分けされたリストをエクスポートする。 |
| `get_revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | 収益分析の時系列データ。 |
| `get_quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | 購入数量の時系列データ。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### セグメント

| 機能 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_segment_list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | 分析追跡ステータス付きのセグメントリストをエクスポートする。 |
| `get_segment_data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | セグメントの時系列分析データ。 |
| `get_segment_details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | 特定のセグメントに関する詳細情報。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### 送信数

| 機能 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_send_data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | トラッキング対象キャンペーン送信の日常的な分析。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### セッション

| 機能 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_session_data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | アプリセッション数の時系列データ。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### SDK 認証キー

| 機能 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_sdk_authentication_keys` | [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | アプリ用のすべてのSDK認証キーをリストアップせよ。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Subscription

| 機能 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_user_subscription_groups` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) | 特定のユーザーの購読グループをリストアップし、取得する。 |
| `get_subscription_group_status` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) | サブスクリプショングループ内のユーザーのサブスクリプションステートを取得する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### テンプレート

| 機能 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_email_templates_list` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | 利用可能なメールテンプレートをリストアップせよ。 |
| `get_email_template_info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | Eメールテンプレートの情報を入手する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% multi_lang_include mcp_server/legal_disclaimer.md %}
