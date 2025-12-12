# Braze MCPサーバーの設定

> BrazeのMCPサーバーの設定方法を学習し、ClaudeやCursorのようなツールを使って自然言語でBrazeのデータと対話できるようにする。より一般的な情報については、[Braze MCP server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## 前提条件

開始する前に、次のものが必要になります。

| 前提条件 | 説明 |
|--------------|-------------|
| APIキー | 必要な権限を持つBraze APIキー。[Braze MCPサーバーの設定](#create-api-key)時に新しいキーを作成する。 |
| MCPクライアント | 現在、[Claudeと](https://claude.ai/) [Cursorのみが](https://cursor.com/)公式にサポートされている。Braze MCPサーバーを使用するには、これらのクライアントのいずれかのアカウントが必要である。 |
| ターミナル | ターミナルアプリで、コマンドを実行したり、ツールをインストールしたりできる。お好みのターミナルアプリか、コンピューターにプリインストールされているものを使う。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Braze MCPサーバーの設定

### ステップ 1: インストールする `uv`

まず、依存関係管理とPythonパッケージ・ハンドリングのための[Astral社のコマンドライン・ツール](https://docs.astral.sh/uv/getting-started/installation/)、`uv`をインストールする。

{% tabs local %}
{% tab MacOSとLinux %}
ターミナル・アプリケーションを開封し、以下のコマンドを貼り付け、<kbd>Enter</kbd>キーを押す。

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

出力は以下のようになる：

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

{% tab ウィンドウズ %}
 Windows PowerShellを開封し、以下のコマンドを貼り付け、<kbd>Enterを</kbd>押す。

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

出力は以下のようになる：

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

### ステップ 2:APIキーを作成する {#create-api-key}

Braze MCPサーバーは、ユーザープロファイルからデータを返さない38の読み取り専用エンドポイントをサポートしている。**設定**＞**APIと識別子**＞**APIキーと**進み、以下の一部またはすべての権限を持つ新しいキーを作成する。

{% details 読み取り専用、非PII権限のリスト %}
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
既存のAPIキーを再利用せず、MCPクライアント専用のAPIキーを作成する。さらに、エージェントがBraze内のデータの書き込みや削除を試みる可能性があるため、読み取り専用、非PII権限のみを割り当てること。
{% endalert %}

### ステップ 3:IDとエンドポイントを取得する

MCPクライアントを設定する際、APIキーの識別子とワークスペースのRESTエンドポイントが必要になる。これらの詳細を得るには、ダッシュボードの**APIキー**ページに戻る。このページは開封しておき、[次のステップで](#configure-client)参照できるようにしておく。

![Brazeの「APIキー」に、新しく作成されたAPIキーとユーザーのRESTエンドポイントが表示されている。]({% image_buster /assets/img/mcp_server/get_indentifer_and_endpoint.png %}){: style="max-width:85%;"}

### ステップ 4: MCPクライアントを設定する {#configure-client}

事前に提供された設定ファイルを使用して、MCPクライアントを設定する。

{% tabs %}
{% tab クロード %}
[クロード・デスクトップで](https://claude.ai/download)、**設定**>**開発者**>**設定を編集に**進み、以下のスニペットを追加する：

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

`key-identifier` と`rest-endpoint` をBrazeの**API Keys**ページにある対応する値に置き換える。コンフィギュレーションは以下のようなものであるべきだ：

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

完了したら、設定を保存し、クロードデスクトップを再起動する。
{% endtab %}

{% tab カーソル %}
[カーソルで](https://cursor.com/)、**設定**＞**ツールと統合**＞**MCPツール**＞**カスタムMCPの追加と**進み、以下のスニペットを追加する：

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

`key-identifier` と`rest-endpoint` をBrazeの**API Keys**ページにある対応する値に置き換える。コンフィギュレーションは以下のようなものであるべきだ：

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

完了したら、設定を保存し、Cursorを再起動する。
{% endtab %}
{% endtabs %}

### ステップ 5: テストプロンプトを送信する

Braze MCPサーバーの設定が完了したら、MCPクライアントにテストプロンプトを送信してみる。その他の例やベストプラクティスについては、[Braze MCPサーバーの使用]]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

{% tabs %}
{% tab クロード %}
![]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab カーソル %}
![]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

## トラブルシューティング

### 端末エラー

#### `uvx` コマンドが見つからない

`uvx` コマンドが見つからないというエラーが表示されたら、`uv` を再インストールし、ターミナルを再起動する。

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### `spawn uvx ENOENT` エラー

もし、`spawn uvx ENOENT` エラーが出る場合は、クライアントの設定ファイルのファイルパスを更新する必要があるかもしれない。まず、ターミナルを開封し、以下のコマンドを実行する：

```bash
which uvx
```

コマンドは以下のようなメッセージを返すはずだ：

```bash
/Users/alex-lee/.local/bin/uvx
```

メッセージをクリップボードにコピーし、[クライアントの設定ファイルを](#configure-client)開封する。`"command": "uvx"` をコピーしたパスに置き換えて、クライアントを再起動する。以下に例を示します。

```json
"command": "/Users/alex-lee/.local/bin/uvx"
```

#### パッケージのインストールに失敗する

パッケージのインストールに失敗した場合は、代わりに特定のPythonバージョンをインストールしてみてほしい。

```bash
uvx --python 3.12 braze-mcp-server@latest
```

### クライアントの設定

#### MCPクライアントがBrazeサーバーを見つけられない。

1. MCPクライアントの設定構文が正しいことを確認する。
2. 設定変更後、MCPクライアントを再起動する。
3. `uvx` がシステム`PATH` に入っていることを確認する。

#### 認証エラー

1. `BRAZE_API_KEY` が正しく、アクティブであることを確認する。
2. `BRAZE_BASE_URL` がBrazeインスタンスと一致していることを確認する。
3. APIキーに[正しい権限が](#create-api-key)あることを確認する。

#### 接続タイムアウトまたはネットワークエラー

1. インスタンスの`BRAZE_BASE_URL` が正しいことを確認する。
2. ネットワーク接続とファイアウォールの設定を確認する。
3. ベースURLにHTTPSを使用していることを確認する。

{% multi_lang_include mcp_server/legal_disclaimer.md %}
