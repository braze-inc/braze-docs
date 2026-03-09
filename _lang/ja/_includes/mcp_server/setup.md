# Braze MCPサーバーの設定

> Braze MCPサーバーの設定方法を学習すれば、ClaudeやCursorといったツールを使って自然言語でBrazeデータとやり取りできるようになる。より一般的な情報については、[Braze MCPサーバー]{% if include.section == "user" %}を参照せよ{{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}。{{site.baseurl}}/developer_guide/mcp_server/){% endif %}

{% multi_lang_include mcp_server/beta_alert.md %}

## 前提条件

開始する前に、次のものが必要になります。

| 前提条件 | 説明 |
|--------------|-------------|
| Braze API キー | 必要な権限を持つBraze API キー。[Braze MCPサーバーを設定する](#create-api-key)際に、新しいキーを作成する。 |
| MCPクライアント | [Claude](https://claude.ai/)、[Cursor](https://cursor.com/)、[Google Gemini CLI](https://docs.cloud.google.com/gemini/docs/codeassist/gemini-cli)は公式にサポートされている。これらのクライアントのいずれかのアカウントを持っている必要がある。そうしなければ、Braze MCPサーバーを利用できない。 |
| ターミナル | ターミナルアプリだ。これでコマンドを実行したりツールをインストールしたりできる。お気に入りのターミナルアプリを使うか、コンピューターにあらかじめインストールされているものを使え。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Braze MCPサーバーの設定

### ステップ 1: インストール `uv`

まず、[Astralが提供する](https://docs.astral.sh/uv/getting-started/installation/)依存関係管理とPythonパッケージ処理のための[コマンドライン](https://docs.astral.sh/uv/getting-started/installation/)ツールを`uv`インストールする。

{% tabs local %}
{% tab MacOS and Linux %}
ターミナルアプリケーションを開封し、以下のコマンドを貼り付けて、<kbd>Enterキー</kbd>を押す。

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

出力は以下のようなものになる：

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
 Windows PowerShellを開封し、次のコマンドを貼り付けて<kbd>Enterキー</kbd>を押す。

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

出力は以下のようなものになる：

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

### ステップ 2:API キーを作成する {#create-api-key}

Braze MCPサーバーは、Brazeユーザープロファイルからデータを返さない読み取り専用エンドポイントを38個サポートしている。**設定**＞**APIと識別子**＞**API キー**に移動し、以下の権限の一部または全てを持つ新しいキーを作成する。

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
既存のAPI キーを再利用してはならない。MCPクライアント専用に新規に作成すること。さらに、エージェントがBraze内のデータを書き換えたり削除したりしようとする可能性があるため、読み取り専用かつ個人を特定できない情報（非PII）へのアクセス権限のみを割り当てること。
{% endalert %}

### ステップ 3:識別子とエンドポイントを取得せよ

MCPクライアントを設定する際には、API キーの識別子とワークスペースのRESTエンドポイントが必要だ。これらの詳細を取得するには、ダッシュボードの**API キー**ページに戻る。このページは開いたままにしておけ。[次のステップ](#configure-client)で参照できるようにするためだ。

![Brazeの「API キー」には、新しく作成されたAPI キーとユーザーのRESTエンドポイントが表示されている。]({% image_buster /assets/img/mcp_server/get_indentifer_and_endpoint.png %}){: style="max-width:85%;"}

### ステップ 4: MCPクライアントを設定する {#configure-client}

あらかじめ用意された設定ファイルを使って、MCPクライアントを設定する。

{% tabs %}
{% tab Claude %}
[クロードデスクトップ](https://claude.ai/download)コネクタディレクトリを使ってMCPサーバーを設定する。 

1. Claude Desktopで、**設定**＞**コネクタ**＞**コネクタの参照**＞**デスクトップ拡張機能**＞**Braze MCPサーバー**＞**インストール**を選択する。
2. API キーとベースURLを入力せよ。
3. 設定を保存し、Claude Desktopを再起動する。

{% endtab %}

{% tab Cursor %}
[カーソル](https://cursor.com/)で、**設定**＞**ツールと統合**＞**MCPツール**＞**カスタムMCPを追加**へ移動し、以下のスニペットを追加する：

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

と を、Brazeの**API **`rest-endpoint`**キー**ページ`key-identifier`にある対応する値で置き換える。設定は以下のようなものになるはずだ：

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

設定が終わったら、設定を保存してCursorを再起動しろ。
{% endtab %}
{% tab Gemini CLI %}
Gemini CLIはユーザー設定を.`~/.gemini/settings.json`から読み込む。これが存在しない場合、ターミナルで以下のコマンドを実行して作成できる：

```powershell
mkdir -p ~/.gemini
nano ~/.gemini/settings.json
```

次に、ターミナルのプロンプトで`@BZXXXXXXXX`、の前にある文字列を正確に`yourname`置き換える。次に、と`key-identifier`をBrazeの**API キー**`rest-endpoint`ページにある対応する値で置き換える。 

設定は以下のようなものになるはずだ：

```json
{
  "mcpServers": {
    "braze": {
      "command": "/Users/yourname/.local/bin/uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "2e8b-3c6c-d12e-bd75-4f0e2a8e5c71",
        "BRAZE_BASE_URL": "https://torchie.braze.com"
      }
    }
  }
}
```

設定が終わったら、設定を保存してGemini CLIを再起動しろ。次に、Geminiで以下のコマンドを実行し、Braze MCPサーバーがリストされていることと、ツールとスキーマが使用可能であることを確認する：

```powershell
gemini
/mcp
/mcp desc
/mcp schema
```

利用可能なツールとスキーマと共にサーバー`braze`が一覧表示されるはずだ。

{% endtab %}
{% endtabs %}

### ステップ 5: テストプロンプトを送れ

Braze MCPサーバーを設定したら、MCPクライアントにテストプロンプトを送信してみろ。その他の例やベストプラクティスについては、[Braze MCPサーバーの使用方法]{% if include.section == "user" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}{{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}を参照せよ。

{% tabs %}
{% tab Claude %}
![「利用可能なBrazeの機能は何か？」という質問がClaudeで尋ねられ、回答されている。]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![「利用可能なBraze機能は何か」という質問がCursorで尋ねられ、回答されている。]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}

{% tab Gemini CLI %}
![Gemini CLIで「利用可能なBraze関数は何か？」と質問され、回答されている。]({% image_buster /assets/img/mcp_server/gemini_cli/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

## トラブルシューティング

### ターミナルエラー

#### `uvx` コマンドが見つからない

コマンドが見つからない`uvx`というエラーが表示されたら、再インストール`uv`してターミナルを再起動しろ。

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### `spawn uvx ENOENT` エラー

エラー`spawn uvx ENOENT`が発生した場合、クライアントの設定ファイル内のファイルパスを更新する必要があるかもしれない。まず、ターミナルを開いて次のコマンドを実行する：

```bash
which uvx
```

コマンドは以下のようなメッセージを返すはずだ：

```bash
/Users/alex-lee/.local/bin/uvx
```

メッセージをクリップボードにコピーし、[クライアントの設定ファイル](#configure-client)を開け。コピーしたパスで`"command": "uvx"`置き換え、クライアントを再起動せよ。以下に例を示します。

```json
"command": "/Users/alex-lee/.local/bin/uvx"
```

#### パッケージのインストールに失敗した

パッケージのインストールに失敗した場合は、代わりに特定のPythonバージョンをインストールしてみよ。

```bash
uvx --python 3.12 braze-mcp-server@latest
```

### クライアント設定

#### MCPクライアントはBrazeサーバーを見つけられない

1. MCPクライアントの設定構文が正しいことを確認せよ。
2. 設定変更後はMCPクライアントを再起動せよ。
3. システムに  が含まれている`uvx``PATH`か確認しろ。

#### 認証エラー

1. メールアドレスが正しく`BRAZE_API_KEY`有効であることを確認せよ。
2. あなたの`BRAZE_BASE_URL`設定がBrazeインスタンスと一致していることを確認せよ。
3. API キーに[正しい権限](#create-api-key)が設定されているか確認せよ。

#### 接続タイムアウトまたはネットワークエラー

1. インスタンスに対して正しい`BRAZE_BASE_URL`ことを確認せよ。
2. ネットワーク接続とファイアウォールの設定を確認せよ。
3. ベースURLでHTTPSを使用していることを確認せよ。

{% multi_lang_include mcp_server/legal_disclaimer.md %}
