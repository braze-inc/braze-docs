# Braze MCP サーバーのセットアップ

> Braze MCP サーバーを設定する方法について説明します。この方法では、クロードやカーソルなどのツールを使用して、自然言語でBrazeデータを操作できます。詳しくは、[Braze MCP サーバ]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}を参照してください。

{% multi_lang_include mcp_server/beta_alert.md %}

## 前提条件

開始する前に、次のものが必要になります。

| 前提条件 | 説明 |
|--------------|-------------|
| Braze API キー | 必要な権限を持つBraze API キー。[ Braze MCP サーバー](#create-api-key) を設定すると、新しい鍵が作成されます。 |
| MCPクライアント | 現在、[Claude](https://claude.ai/)と[Cursor](https://cursor.com/)のみが公式にサポートされています。Braze MCP サーバーを使用するには、次のいずれかのクライアントのアカウントが必要です。 |
| 端子 | 端末アプリを使用して、コマンドを実行したり、ツールをインストールしたりできます。お使いのコンピューターにあらかじめインストールされている端末アプリを使用してください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Braze MCP サーバーのセットアップ

### ステップ 1: インストール `uv`

まず、`uv`-a [コマンドラインツールをAstral](https://docs.astral.sh/uv/getting-started/installation/)でインストールし、依存性管理とPythonパッケージ処理を行います。

{% tabs local %}
{% tab MacOS and Linux %}
端末アプリアプリケーションを開き、次のコマンドを貼り付けてから、<kbd>Enter</kbd> を押します。

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

出力は次のようになります。

```bash
$ curl -LsSf https://astral.sh/uv/install.sh | sh

downloading uv 0.8.9 aarch64-apple-darwin
no checksums to verify
installing to /Users/Isaiah.Robinson/.local/bin
  uv
  uvx
everything's installed!
```
{% endtab %}

{% tab Windows %}
 Windows PowerShell を開き、次のコマンドを貼り付けて、<kbd>Enter</kbd> を押します。

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

出力は次のようになります。

```powershell
PS C:\Users\YourUser> irm https://astral.sh/uv/install.ps1 | iex

Downloading uv 0.8.9 (x86_64-pc-windows-msvc)
no checksums to verify
installing to C:\Users\YourUser\.local\bin
  uv.exe
  uvx.exe
everything's installed!
```
{% endtab %}
{% endtabs %}

### ステップ 2:API キーの作成 {#create-api-key}

Braze MCP サーバーは、Braze ユーザープロファイルs からデータを返さない38 個の読み取り専用エンドポイントs をサポートします。**Settings** > **APIs and Identifiers** > **API Keys**に移動し、以下の一部またはすべての権限を持つ新しいキーを作成します。

{% details List of read-only, non-PII permissions %}
#### キャンペーン

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | `campaigns.data_series` |
| [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | `campaigns.details` |
| [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | `campaigns.list` |
| [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | `sends.data_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### キャンバス

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | `canvas.data_series` |
| [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | `canvas.data_summary` |
| [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | `canvas.details` |
| [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | `canvas.list` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### カタログ

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | `catalogs.get` |
| [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | `catalogs.get_items` |
| [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | `catalogs.get_item` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### クラウドデータ取り込み

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | `cdi.integration_list` |
| [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | `cdi.integration_job_status` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### コンテンツブロック

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | `content_blocks.list` |
| [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | `content_blocks.info` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### カスタム属性

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) | `custom_attributes.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### イベント

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | `events.list` |
| [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | `events.data_series` |
| [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) | `events.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### KPI

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | `kpi.new_users.data_series` |
| [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | `kpi.dau.data_series` |
| [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | `kpi.mau.data_series` |
| [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | `kpi.uninstalls.data_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### メッセージ

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled) | `messages.schedule_broadcasts` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### ユーザー設定センター

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center) | `preference_center.list` |
| [`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | `preference_center.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### 購入

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | `purchases.product_list` |
| [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | `purchases.revenue_series` |
| [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | `purchases.quantity_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### セグメント

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | `segments.list` |
| [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | `segments.data_series` |
| [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | `segments.details` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### 送信数

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | `sends.data_series` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

#### セッション

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | `sessions.data_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### SDK 認証キー

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | `sdk_authentication.keys` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Subscription

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) | `subscription.status.get` |
| [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) | `subscription.groups.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### テンプレート

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | `templates.email.list` |
| [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | `templates.email.info` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% enddetails %}

{% alert warning %}
既存のAPI キーを再利用しないでください。作成は、MCP クライアント専用です。さらに、エージェントがBrazeでデータの書き込みまたは削除を試みる可能性があるため、読み取り専用の非PII権限のみを割り当てます。
{% endalert %}

### ステップ 3:識別子とエンドポイントを入手する

MCP クライアントを設定するには、API キーの識別子とワークスペースのREST エンドポイントが必要です。これらの詳細を取得するには、ダッシュボード-keep this page 開封の**API Keys** ページに戻ります。そのため、[次回のステップ](#configure-client) 時に参照できます。

![新しく作成されたAPI キーを示すBrazeの「API キー」とユーザーのREST エンドポイント。]({% image_buster /assets/img/mcp_server/get_indentifer_and_endpoint.png %}){: style="max-width:85%;"}

### ステップ 4: MCP クライアントの設定 {#configure-client}

付属の設定ファイルを使用して、MCP クライアントを設定します。

{% tabs %}
{% tab Claude %}
[Claude Desktop](https://claude.ai/download) で、**Settings** > **Developer** > **Edit Config** に移動し、次のスニペットを追加します。

```json
{
  "mcpServers": {
    "braze": {
      "command": "uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "key-identifier",
        "BRAZE_BASE_URL": "rest-endpoint"
      }
    }
  }
}
```

`key-identifier` および`rest-endpoint` を、Braze の**API Keys** ページの対応する値に置き換えます。設定は次のようになります。

```json
{
  "mcpServers": {
    "braze": {
      "command": "uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "2e8b-3c6c-d12e-bd75-4f0e2a8e5c71",
        "BRAZE_BASE_URL": "https://torchie.braze.com"
      }
    }
  }
}
```

完了したら、構成を保存し、Claude Desktop を再起動します。
{% endtab %}

{% tab Cursor %}
[Cursor](https://cursor.com/)で、**Settings**> **Tools and Integrations**> **MCP Tools**> **Add Custom MCP**に進み、次のスニペットを追加します。

```json
{
  "mcpServers": {
    "braze": {
      "command": "uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "your-braze-api-key",
        "BRAZE_BASE_URL": "your-braze-endpoint-url"
      }
    }
  }
}
```

`key-identifier` および`rest-endpoint` を、Braze の**API Keys** ページの対応する値に置き換えます。設定は次のようになります。

```json
{
  "mcpServers": {
    "braze": {
      "command": "uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "2e8b-3c6c-d12e-bd75-4f0e2a8e5c71",
        "BRAZE_BASE_URL": "https://torchie.braze.com"
      }
    }
  }
}
```

終了したら、設定を保存し、Cursor を再起動します。
{% endtab %}
{% endtabs %}

### ステップ 5: テストプロンプトを送信する

Braze MCP サーバーを設定したので、MCP クライアントにテストプロンプトを送信してみてください。他の例およびベストプラクティスについては、[Braze MCP サーバーの使用]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %})を参照してください。

{% tabs %}
{% tab Claude %}
![「私の利用可能なBraze機能は何ですか?」とクラウドで尋ねられ、答えられました。]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![カーソルで質問され、答えられている「私の利用可能なBraze機能は何ですか」。]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

## トラブルシューティング

### 端子エラーs

#### `uvx` コマンドが見つかりません

`uvx` コマンドが見つからないというエラーが表示された場合は、`uv` を再インストールし、端末を再起動します。

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### `spawn uvx ENOENT` エラー

`spawn uvx ENOENT` エラーs を受け取った場合は、クライアントの設定ファイルのファイルパスを更新する必要があります。まず、端末を開封し、次のコマンドを実行します。

```bash
which uvx
```

このコマンドは、次のようなメッセージを返します。

```bash
/Users/alex-lee/.local/bin/uvx
```

メッセージをクリップボードにコピーし、[クライアントの設定ファイル](#configure-client)を開封します。`"command": "uvx"` をコピーしたパスに置き換え、クライアントを再起動します。以下に例を示します。

```json
"command": "/Users/alex-lee/.local/bin/uvx"
```

#### パッケージのインストールが失敗する

パッケージのインストールが失敗した場合は、代わりに特定のPython バージョンをインストールしてみてください。

```bash
uvx --python 3.12 braze-mcp-server@latest
```

### クライアント設定

#### MCP クライアントがBraze サーバーを見つけられない

1. MCP クライアントの構成が正しいことを確認します。
2. 設定変更後、MCP クライアントを再起動します。
3. `uvx` がシステム`PATH` にあることを確認します。

#### 認証エラー

1. `BRAZE_API_KEY` が正しくアクティブであることを確認します。
2. `BRAZE_BASE_URL` がBrazeインスタンスと一致していることを確認します。
3. API キーに[正しい権限](#create-api-key)があることを確認します。

#### 接続タイムアウトまたはネットワークエラー

1. `BRAZE_BASE_URL` がインスタンスに適していることを確認します。
2. ネットワークコネクションとファイヤーウォール設定を確認してください。
3. ベースURL でHTTPS を使用していることを確認します。

{% multi_lang_include mcp_server/legal_disclaimer.md %}
