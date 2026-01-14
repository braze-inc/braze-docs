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
Braze では、アプリグループはワークスペースに改名されましたが、このページのキーはまだ古い用語を参照しています (例えば、`appGroup`、`appGroupName`)。
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
| `companyPermissions` | オプション | 配列 | [会社許可文字列](#company) テーブルからの会社レベルの許可文字列の配列。文字列の存在は、対応する許可を持つユーザに対応します。 |
| `roles` | オプション | 配列 | [ロールオブジェクト](#role-object)の配列。 |
| `appGroup` | required | 配列 | [ワークスペース許可オブジェクト](#workspace-permission-object)の配列。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### ワークスペース許可オブジェクト {#workspace-permission-object}

有効なアプリグループ許可オブジェクトは、以下のキーと値のペアを持つ JSON オブジェクトです。

| キー | required | データタイプ | 説明 |
| --- | --- | --- | --- |
| `appGroupName`| オプション | string | ワークスペースの名前。このオブジェクトに含まれるパーミッションがどのワークスペースに対するものかを指定するために使用される。 | 
| `appGroupId` | `appGroupName` がない場合は必須 | string | ワークスペースの ID。ワークスペースを指定する別の方法として機能します。 |
| `appGroupPermissionSets` | オプション | 配列 | 単一の[ワークスペース許可セットオブジェクト](#workspace-permissions-set-object)を持つ配列。 |
| `appGroupPermissions` | required | 配列 | [ワークスペース許可文字列](#workspace-strings)テーブルからのワークスペースレベルの許可文字列の配列。文字列の存在は、指定されたワークスペースに対する対応する許可を持つユーザーに対応します。 |
| `team` | オプション | 配列 | [チーム許可オブジェクト](#team-permissions-object)の配列。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### ワークスペース権限設定オブジェクト {#workspace-permissions-set-object}

有効なワークスペース権限セットオブジェクトは、以下のキーと値のペアを持つJSONオブジェクトである：

| キー | required | データタイプ | 説明 |
| --- | --- | --- | --- |
| `appGroupPermissionSetName` | オプション | string | このワークスペースのユーザーに割り当てられているワークスペース権限セットの名前。 |
| `appGroupPermissionSetID` | `appGroupPermissionSetName` がない場合は必須 | string | ワークスペースの ID。このワークスペースに対してユーザーに割り当てられたワークスペース許可セットを指定する代替方法として機能します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### チーム許可オブジェクト

有効なチーム・パーミッション・オブジェクトは、以下のキーと値のペアを持つJSONオブジェクトである：

| キー | required | データタイプ | 説明 |
| --- | --- | --- | --- |
| `teamName` | オプション | string | チーム名。このオブジェクト内のパーミッションがどのチームのものかを指定するために使用できる。 |
| `teamId` | `teamName` がない場合は必須 | string | チームのIDで、チームを指定する代替方法となる。 |
| `teamPermissions` | required | 配列 | [チーム許可文字列](#team) テーブルからのチームレベルの許可文字列の配列。文字列の存在は、指定されたチームに対する対応する許可を持つユーザーに対応します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 役割オブジェクト

有効なロールオブジェクトは、以下のキーと値のペアを持つJSONオブジェクトである：

| キー | required | データタイプ | 説明 |
| --- | --- | --- | --- |
| `roleName` | オプション | string | ユーザーに割り当てられているロールの名前。 |
| `roleId` | `roleName` がない場合は必須 | string | ロールの ID。ロールを指定する代替方法として機能します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 付録

### 会社の許可文字列 {#company}

| UI に表示 | SCIM API 文字列 |
| --- | --- |
| 管理者 | `admin` |
| 会社の設定を管理できる | `manage_company_settings` |
| ワークスペースを追加／削除できる| `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### ワークスペース権限文字列 {#workspace-strings}

| 許可名 | SCIM API 文字列 |
| --- | --- |
| 管理者 | `admin` |
| アクセスキャンペーン、キャンバス、カード、セグメント、メディアライブラリー | `basic_access` |
| キャンバスの承認と拒否 | `approve_deny_campaigns` |
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
| 開発コンソールにアクセス | `dev_console` |
| コンテンツブロックを開始 | `launch_content_blocks` |
| 外部統合を管理する | `manage_external_integrations` |
| アプリを管理する | `manage_apps` |
| チームを管理 | `manage_teams` |
| イベント、属性、購入を管理する | `manage_events_attributes_purchases` |
| タグを管理する | `manage_tags` |
| メール設定を管理 | `manage_email_settings` |
| サブスクリプショングループを管理 | `manage_subscription_groups` |
| 承認設定を管理する | `manage_approval_settings` |
| カタログ・ダッシュボードの権限を管理する | `manage_catalogs_dashboard_permission` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### チームの許可文字列 {#team}

| 許可名 | SCIM API 文字列 |
| --- | --- |
| 管理者 | `admin` |
| アクセスキャンペーン、キャンバス、カード、セグメント、メディアライブラリー | `basic_access` |
| キャンバスの承認と拒否 | `approve_deny_campaigns` |
| キャンペーン、キャンバスの送信 | `send_campaigns_canvases` |
| カードの発行 | `publish_cards` |
| セグメントの編集 | `edit_segments` |
| ユーザーデータのエクスポート | `export_user_data` |
| ユーザープロフィールを見る | `view_user_profile` |
| ダッシュボードユーザーの管理 | `manage_dashboard_users` |
| メディアライブラリアセットの管理 | `manage_media_library` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 部門の文字列

| UI に表示 | SCIM API 文字列 |
| --- | --- |
| 代理店 / サードパーティ | `agency` |
| BI / アナリティクス | `bi` |
| 経営幹部 | `c_suite` |
| エンジニアリング | `engineering` |
| ファイナンス | `finance` |
| マーケティング / 編集 | `marketing` |
| 製品管理 | `pm` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
