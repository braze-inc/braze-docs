---
nav_title: "SCIM API オブジェクトと付録"
article_title: SCIM API オブジェクトと付録
page_order: 8
page_type: reference
description: "この記事では、さまざまなSCIM APIオブジェクトと付録について説明する。"
hidden: true
permalink: "/scim_api_appendix/"
---

# SCIM API オブジェクトと付録

## 許可オブジェクト

permissionsオブジェクトは、SCIM IDパーミッションを通してユーザーリソースとインターフェースするときに、リクエストとレスポンスの一部に見られるフィールドである。

{% alert note %}
Brazeでは、アプリグループはワークスペースに改名されたが、このページのキーはまだ古い用語を参照している（例えば、`appGroup` 、`appGroupName` ）。
{% endalert %}

```
{
  "permissions": {
    "companyPermissions": (required, array),
    "appGroup": (required, array)
  }
}
```

有効なパーミッション・オブジェクトは、以下のキーと値のペアを持つJSONオブジェクトである：

| キー | required | データタイプ | 説明 |
| --- | --- | --- | --- |
| `companyPermissions` | required | 配列 | 文字列の存在は、対応するパーミッションを持つユーザーに対応する[。](#company) |
| `appGroup` | required | 配列 | [ワークスペース許可オブジェクトの](#workspace-permission-object)配列。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### ワークスペース許可オブジェクト {#workspace-permission-object}

有効なアプリグループ許可オブジェクトは、以下のキーと値のペアを持つJSONオブジェクトである：

| キー | required | データタイプ | 説明 |
| --- | --- | --- | --- |
| `appGroupName`| オプション | string | ワークスペースの名前。このオブジェクトに含まれるパーミッションがどのワークスペースに対するものかを指定するために使用される。 | 
| `appGroupId` | `appGroupName` がない場合は必須 | string | ワークスペースを指定する代替方法となる。 |
| `appGroupPermissionSets` | オプション | 配列 | [ワークスペース権限セットオブジェクトを](#workspace-permissions-set-object)1つ持つ配列。 |
| `appGroupPermissions` | required | 配列 | [ワークスペース・パーミッション文字列](#workspace-strings)テーブルのワークスペース・レベル・パーミッション文字列の配列で、文字列の存在は、指定されたワークスペースの対応するパーミッションを持つユーザーに対応する。 |
| `team` | オプション | 配列 | [チーム権限オブジェクトの](#team-permissions-object)配列。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### ワークスペース権限設定オブジェクト {#workspace-permissions-set-object}

有効なワークスペース権限セットオブジェクトは、以下のキーと値のペアを持つJSONオブジェクトである：

| キー | required | データタイプ | 説明 |
| --- | --- | --- | --- |
| `appGroupPermissionSetName` | オプション | string | このワークスペースのユーザーに割り当てられているワークスペース権限セットの名前。 |
| `appGroupPermissionSetID` | `appGroupPermissionSetName` がない場合は必須 | string | このワークスペースのユーザーに割り当てられているワークスペース権限セットを指定する代替方法として機能する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### チーム許可オブジェクト

有効なチーム・パーミッション・オブジェクトは、以下のキーと値のペアを持つJSONオブジェクトである：

| キー | required | データタイプ | 説明 |
| --- | --- | --- | --- |
| `teamName` | オプション | string | チーム名。このオブジェクト内のパーミッションがどのチームのものかを指定するために使用できる。 |
| `teamId` | `teamName` がない場合は必須 | string | チームのIDで、チームを指定する代替方法となる。 |
| `teamPermissions` | required | 配列 | この文字列が存在する場合、そのユーザーは指定された[チームの](#team)対応するパーミッションを持っていることになる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 付録

### 会社の許可文字列 {#company}

| UIに表示されている | SCIM API 文字列 |
| --- | --- |
| 管理者 | `admin` |
| 会社の設定を管理できる | `manage_company_settings` |
| ワークスペースを追加／削除できる| `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2}

### ワークスペース権限文字列 {#workspace-strings}

| 許可名 | SCIM API 文字列 |
| --- | --- |
| 管理者 | `admin` |
| アクセスキャンペーン、キャンバス、カード、セグメント、メディアライブラリー | `basic_access` |
| キャンペーン、キャンバスの送信 | `send_campaigns_canvases` |
| カードの発行 | `publish_cards` |
| セグメントの編集 | `edit_segments` |
| ユーザーデータのエクスポート | `export_user_data` |
| PIIを見る | `view_pii` |
| PII 準拠のユーザープロファイル表示 | `view_user_profile` |
| ダッシュボードユーザーの管理 | `manage_dashboard_users` |
| メディアライブラリアセットの管理 | `manage_media_library` |
| 利用データを見る | `view_usage_data` |
| ユーザーデータのインポートと更新 | `import_update_user_data` |
| 請求の詳細を見る | `view_billing_details` |
| デブ・コンソールにアクセスする | `dev_console` |
| コンテンツ・ブロックを立ち上げる | `launch_content_blocks` |
| 外部統合を管理する | `manage_external_integrations` |
| アプリを管理する | `manage_apps` |
| チームを管理する | `manage_teams` |
| イベント、属性、購入を管理する | `manage_events_attributes_purchases` |
| タグを管理する | `manage_tags` |
| Eメールの設定を管理する | `manage_email_settings` |
| 購読グループを管理する | `manage_subscription_groups` |
| 承認設定を管理する | `manage_approval_settings` |
| カタログ・ダッシュボードの権限を管理する | `manage_catalogs_dashboard_permission` |
{: .reset-td-br-1 .reset-td-br-2}

### チームの許可文字列 {#team}

| 許可名 | SCIM API 文字列 |
| --- | --- |
| 管理者 | `admin` |
| アクセスキャンペーン、キャンバス、カード、セグメント、メディアライブラリー | `basic_access` |
| キャンペーン、キャンバスの送信 | `send_campaigns_canvases` |
| カードの発行 | `publish_cards` |
| セグメントの編集 | `edit_segments` |
| ユーザーデータのエクスポート | `export_user_data` |
| ユーザープロフィールを見る | `view_user_profile` |
| ダッシュボードユーザーの管理 | `manage_dashboard_users` |
| メディアライブラリアセットの管理 | `manage_media_library` |
{: .reset-td-br-1 .reset-td-br-2}

### 部門の文字列

| UIに表示されている | SCIM API 文字列 |
| --- | --- |
| 代理店 / 第三者 | `agency` |
| BI / アナリティクス | `bi` |
| Cスイート | `c_suite` |
| エンジニアリング | `engineering` |
| ファイナンス | `finance` |
| マーケティング / 編集 | `marketing` |
| 製品管理 | `pm` |
{: .reset-td-br-1 .reset-td-br-2}
