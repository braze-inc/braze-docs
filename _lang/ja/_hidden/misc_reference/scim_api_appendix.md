---
nav_title: "SCIM API オブジェクトと付録"
article_title: SCIM API オブジェクトと付録
page_order: 8
page_type: reference
description: "この記事では、さまざまな SCIM API オブジェクトと付録について説明します。"
hidden: true
permalink: "/scim_api_appendix/"
---

# SCIM API オブジェクトと付録

## 権限オブジェクト

パーミッションオブジェクトは、SCIM ID パーミッションを介してユーザーリソースとやり取りするときに一部のリクエストとレスポンスに含まれるフィールドです。

{% alert note %}
アプリグループの名前が Braze のワークスペースに変更されましたが、このページのキーは古い用語（たとえば、など）を引き続き参照しています。`appGroup` `appGroupName`
{% endalert %}

```
{
  "permissions": {
    "companyPermissions": (required, array),
    "appGroup": (required, array)
  }
}
```

有効な権限オブジェクトは、以下のキーと値のペアを含む JSON オブジェクトです。

| キー | 必須 | データ型 | 説明 |
| --- | --- | --- | --- |
| `companyPermissions` | 必須 | 配列 | [会社の権限文字列テーブルにある会社レベルの権限文字列の配列](#company)。文字列が存在するかどうかは、対応する権限を持つユーザーに対応します。|
| `appGroup` | 必須 | 配列 | [ワークスペース権限オブジェクトの配列](#workspace-permission-object)。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### ワークスペース権限オブジェクト {#workspace-permission-object}

有効なアプリグループ権限オブジェクトは、次のキーと値のペアを含む JSON オブジェクトです。

| キー | 必須 | データ型 | 説明 |
| --- | --- | --- | --- |
| `appGroupName` | オプション| 文字列| ワークスペースの名前。このオブジェクトに含まれる権限がどのワークスペースに適用されるかを指定するために使用されます。|
| `appGroupId` | `appGroupName` がない場合は必須 | String | ワークスペースの ID。ワークスペースを指定する代替方法として使用できます。|
| `appGroupPermissionsSets` | オプション | 配列 | [単一のワークスペース権限セットオブジェクトを含む配列](#workspace-permissions-set-object)。|
| `appGroupPermissions` | 必須 | 配列 | [ワークスペース権限文字列テーブルにあるワークスペースレベルの権限文字列の配列](#workspace-strings)。この文字列が存在することは、指定されたワークスペースに対応する権限を持つユーザーに対応します。|
| `team` | オプション| 配列| [チーム権限オブジェクトの配列](#team-permissions-object)。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### ワークスペース権限セットオブジェクト {#workspace-permissions-set-object}

有効なワークスペース権限セットオブジェクトは、以下のキーと値のペアを含む JSON オブジェクトです。

| キー | 必須 | データ型 | 説明 |
| --- | --- | --- | --- |
`appGroupPermissionSetName`| | オプション | 文字列 | このワークスペースのユーザーに割り当てられているワークスペース権限設定の名前。|
| `appGroupPermissionSetID` | `appGroupPermissionSetName` がない場合は必須 | String | ワークスペースの ID。このワークスペースのユーザーに割り当てられたワークスペース権限セットを指定する代替方法となります。| |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### チーム権限オブジェクト

有効なチーム権限オブジェクトは、以下のキーと値のペアを含む JSON オブジェクトです。

| キー | 必須 | データ型 | 説明 |
| --- | --- | --- | --- |
| `teamName` | オプション | 文字列 | チームの名前。これを使用して、このオブジェクト内の権限がどのチームに適用されるかを指定できます。|
| `teamId` | `teamName` が欠落している場合は必須 | String | チームの ID。チームを指定する代替方法として使用できます。|
| `teamPermissions` | 必須 | 配列 | [チーム権限文字列テーブルにあるチームレベルの権限文字列の配列](#team)。この文字列が存在することは、指定されたチームに対応する権限を持つユーザーに対応します。| |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 付録

### 会社の権限文字列 {#company}

| UI に表示されているとおり | SCIM API 文字列 |
| --- | --- |
| 管理者 | `admin` |
| 会社の設定を管理できます | `manage_company_settings` |
| ワークスペースを追加/削除できます| | `add_remove_app_groups`
{: .reset-td-br-1 .reset-td-br-2}

### ワークスペース権限文字列 {#workspace-strings}

| パーミッション名 | SCIM API ストリング |
| --- | --- |
| 管理者 | `admin` |
| キャンペーン、キャンバス、カード、セグメント、メディアライブラリへのアクセス | | `basic_access`
| キャンペーン、キャンバスを送信する | | `send_campaigns_canvases`
| カードを公開 | `publish_cards` |
| セグメントの編集 | `edit_segments` |
| ユーザーデータのエクスポート | `export_user_data` |
| PII を表示 | `view_pii` |
| ユーザープロファイル表示の PII 準拠 | `view_user_profile` |
| ダッシュボードユーザーを管理 | `manage_dashboard_users` |
| メディアライブラリアセットを管理  | `manage_media_library` |
| 利用状況データを表示 | `view_usage_data` |
| ユーザーデータをインポートして更新 | `import_update_user_data` |
| 請求の詳細を表示 | `view_billing_details` |
| 開発コンソールにアクセス | `dev_console` |
| 外部統合を管理 | `manage_external_integrations` |
| アプリを管理 | `manage_apps` |
| チームを管理 | `manage_teams` |
| イベント、属性、購入を管理 | `manage_events_attributes_purchases` |
| タグを管理 | `manage_tags` |
|メール設定を管理 | `manage_email_settings` |
| サブスクリプショングループを管理 | `manage_subscription_groups` |
| 承認設定の管理 | `manage_approval_settings` |
| カタログダッシュボードの権限を管理 | `manage_catalogs_dashboard_permission` |
{: .reset-td-br-1 .reset-td-br-2}

### チーム権限文字列 {#team}

| パーミッション名 | SCIM API ストリング |
| --- | --- |
| 管理者 | `admin` |
| キャンペーン、キャンバス、カード、セグメント、メディアライブラリへのアクセス | | `basic_access`
| キャンペーン、キャンバスを送信 | `send_campaigns_canvases` |
| カードを発行 | `publish_cards` |
| セグメントを編集 | `edit_segments` |
| ユーザーデータをエクスポート| `export_user_data` |
| ユーザープロファイルを表示| `view_user_profile` |
| ダッシュボードユーザーを管理 | `manage_dashboard_users` |
| メディアライブラリアセットを管理  | `manage_media_library` |
{: .reset-td-br-1 .reset-td-br-2}

### 部門文字列

| UI に表示されているとおり | SCIM API 文字列 |
| --- | --- |
| 代理店 / サードパーティ | `agency` |
| BI / 分析 | `bi` |
| 経営幹部| `c_suite` |
| エンジニアリング | `engineering` |
| ファイナンス| `finance` |
| マーケティング / 編集| `marketing` |
| 製品管理  | `pm` |
{: .reset-td-br-1 .reset-td-br-2}
