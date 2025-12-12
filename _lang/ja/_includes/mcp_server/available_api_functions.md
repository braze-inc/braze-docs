# BrazeのMCPサーバー機能

> Braze MCP サーバーは、特定のBraze REST API エンドポイントにマップする一連の読み取り専用API ファンクションを公開します。クロードやカーソルなどのMCP クライアントは、これらの関数を呼び出して、PIIにアクセスしたりワークスペースを変更したりすることなくデータを取得できます。詳しくは、[Braze MCP サーバー]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){%elsif include.section="開発者" %}({{site.baseurl}}/developer_guide/mcp_server/){%endif %}を参照してください。

{% multi_lang_include mcp_server/beta_alert.md %}

## 前提条件

この機能を使用するには、[Braze MCP サーバー]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){%elsif include.section="開発者" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){%endif %}を設定する必要があります。

## Braze機能一覧

以下は、MCP クライアントがBraze MCP サーバーと対話するために参照するAPI 機能です。

### 一般機能

| 機能 | 説明 |
|----------|-------------|
| `list_functions` | 使用可能なすべてのBraze API 関数とその説明およびパラメータを一覧表示します |
| `call_function` | 指定したパラメータで指定したBraze API 関数を呼び出す |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### キャンペーン

| 機能 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_campaign_list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | メタデータを含むキャンペーンの一覧をエクスポートします。 |
| `get_campaign_details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | キャンペーンの詳細を取得します。 |
| `get_campaign_dataseries` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | キャンペーンs の時系列分析を取得します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Canvases

| 機能 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_canvas_list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | メタデータを含むキャンバスのリストをエクスポートします。 |
| `get_canvas_details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | 特定のキャンバスに関する詳細情報を取得します。 |
| `get_canvas_data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | キャンバスパフォーマンスの概要分析を取得します。 |
| `get_canvas_data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | キャンバスの時系列分析を取得します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### カタログ

| 機能 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_catalogs` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | ワークスペースのカタログs の一覧を返します。 |
| `get_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | 複数のカタログ項目とその内容をページネーションサポートで返します。 |
| `get_catalog_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | 指定したカタログアイテムとその内容を返します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### クラウドデータ取り込み

| 機能 | エンドポイント | 説明 |
|----------|----------|-------------|
| `list_integrations` | [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | 既存のCDI 統合のリストを返します。 |
| `get_integration_job_sync_status` | [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | 指定したCDI インテグレーションのシンクステータスes を超えて返します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### コンテンツブロック

| 機能 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_content_blocks_list` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | 使用可能なコンテンツブロックを一覧表示します。 |
| `get_content_blocks_info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | コンテンツブロック s の情報を取得します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### カスタム属性

| 機能 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_custom_attributes` | [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) | アプリに記録されたカスタム属性をエクスポートします。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### イベント

| 機能 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_events_list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | アプリに記録されたカスタムイベントの一覧をエクスポートします。 |
| `get_events_data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | カスタムイベントs の時系列データを取得します。 |
| `get_events` | [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) | ページ分割サポートを使用して詳細なイベントデータを取得します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### KPI

| 機能 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_new_users_data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | 毎日の一連の新しいユーザー数。 |
| `get_dau_data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | 日次アクティブユーザーの時系列データ。 |
| `get_mau_data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | 月次アクティブユーザーの時系列データ。 |
| `get_uninstalls_data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | アプリの時系列データのアンインストール。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### メッセージ

| 機能 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_scheduled_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled) | 次回のスケジュールされた キャンペーンとキャンバスを一覧表示します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### ユーザー設定センター

| 機能 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_preference_centers` | [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center) | 使用可能なユーザー設定センターを一覧表示します。 |
| `get_preference_center_details` | [`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | HTMLの内容や選択肢など、具体的なユーザー設定センターの詳細を表示します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### 購入

| 機能 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | ページ化された製品ID のリストをエクスポートします。 |
| `get_revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | 収益分析の時系列データ。 |
| `get_quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | 購入数量時系列データ。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### セグメント

| 機能 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_segment_list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | Segmentの一覧を分析 "トラッキング ステータスでエクスポートします。 |
| `get_segment_data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | Segmentsの時系列分析。 |
| `get_segment_details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | 具体的なSegmentの詳細 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### 送信数

| 機能 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_send_data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | 追跡されたキャンペーンセンドの毎日の分析。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### セッション

| 機能 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_session_data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | アプリ セッション数の時系列データ。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### SDK 認証キー

| 機能 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_sdk_authentication_keys` | [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | アプリのすべてのSDK認証鍵を一覧表示します。 |
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
| `get_email_templates_list` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | 使用可能なメール テンプレートを一覧表示します。 |
| `get_email_template_info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | Eメールテンプレートの情報を入手する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% multi_lang_include mcp_server/legal_disclaimer.md %}
