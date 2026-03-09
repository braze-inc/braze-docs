## 細粒度権限の移行

{% alert important %}
細分化された権限設定は早期アクセス段階にある。自社の移行が計画された場合、Brazeの管理者はメールとダッシュボード上のバナーで通知を受け取る。これらは[詳細な権限の移行]({{site.baseurl}}/granular_permissions_migration/)について知らせるものだ。
{% endalert %}

既存のSCIM統合と[レガシーSCIM APIオブジェクトは、]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api)4月下旬の細分化された権限移行後も引き続き動作する。 

すぐに何かのアクションを起こす必要はない。ただし、統合設定において権限が細分化される可能性があるため、それらを確認することを推奨する。例えば、現在API`basic_access`で送信している場合、細分化後に統合を更新し、特定の権限（例：`"appGroupPermissions":["view_campaigns","edit_campaigns"]`）を含めることを推奨する。Brazeは、粒度の細かい権限設定への移行後も、既存の連携が壊れないように、従来の文字列（`basic_access`例：）を引き続き受け付ける。

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
| `companyPermissions` | オプション | 配列 | [企業レベルの権限文字列]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_company)の配列であり、文字列が存在する場合、ユーザーが対応する権限を持っていることを示す。 |
| `roles` | オプション | 配列 | [ロールオブジェクト]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_role-object)の配列。 |
| `appGroup` | 必須かどうか | 配列 | [ワークスペース許可オブジェクト]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-permissions-object)の配列。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### ワークスペース権限オブジェクト

有効なアプリグループ許可オブジェクトは、以下のキーと値のペアを持つ JSON オブジェクトです。

| キー | required | データタイプ | 説明 |
| --- | --- | --- | --- |
| `appGroupName`| オプション | string | ワークスペースの名前。このオブジェクトに含まれるパーミッションがどのワークスペースに対するものかを指定するために使用される。 | 
| `appGroupId` | `appGroupName` がない場合は必須 | string | ワークスペースの ID。ワークスペースを指定する別の方法として機能します。 |
| `appGroupPermissionSets` | オプション | 配列 | 単一の[ワークスペース許可セットオブジェクト]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-permissions-set-object)を持つ配列。 |
| `appGroupPermissions` | 必須かどうか | 配列 | [ワークスペース許可文字列]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-strings)テーブルからのワークスペースレベルの許可文字列の配列。文字列の存在は、指定されたワークスペースに対する対応する許可を持つユーザーに対応します。 |
| `team` | オプション | 配列 | [チーム許可オブジェクト]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_team-permissions-object)の配列。 |
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
| `teamPermissions` | 必須かどうか | 配列 | [チーム許可文字列]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_team) テーブルからのチームレベルの許可文字列の配列。文字列の存在は、指定されたチームに対する対応する許可を持つユーザーに対応します。 |
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
| 会社設定の管理 | `manage_company_settings` |
| ワークスペースの作成と削除s| `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### ワークスペース権限文字列 {#workspace-strings}

| 許可名 | SCIM API 文字列 |
| --- | --- |
| キャンペーンを表示 | `view_campaigns` |
| キャンペーンを編集 | `edit_campaigns` |
| キャンペーンをアーカイブ | `archive_campaigns` |
| キャンバスを表示 | `view_canvases` |
| キャンバスを編集 | `edit_canvases` |
|  個のキャンバス  | `archive_canvases` |
| フリークエンシーキャップルールを表示 | `view_frequency_caps` |
| フリークエンシーキャップルールを編集 | `edit_frequency_caps` |
| メッセージの優先順位付けを表示 | `view_message_prioritization` |
| メッセージの優先順位付けを編集 | `edit_message_prioritization` |
| コンテンツブロックを表示 | `view_content_blocks` |
| コンテンツブロックを編集 | `edit_content_blocks` |
| コンテンツブロックをアーカイブ | `archive_content_blocks` |
| フィーチャーフラグを表示 | `view_feature_flags` |
| フィーチャーフラグを編集 | `edit_feature_flags` |
| フィーチャーフラグをアーカイブ | `archive_feature_flags` |
| セグメントを表示 | `view_segments` |
| セグメントの編集 | `edit_segments` |
| セグメントをアーカイブ | `archive_segments` |
| グローバルコントロールグループを表示 | `view_global_control_group` |
| グローバルコントロールグループを編集する | `edit_global_control_group` |
| IAM テンプレートを表示 | `view_iam_templates` |
| IAM テンプレートを編集 | `edit_iam_templates` |
| IAM テンプレートをアーカイブ | `archive_iam_templates` |
| メールテンプレートを表示 | `view_email_templates` |
| メールテンプレートを編集 | `edit_email_templates` |
| メールテンプレートをアーカイブ | `archive_email_templates` |
| Webhook テンプレートを表示 | `view_webhook_templates` |
| Webhook テンプレートを編集 | `edit_webhook_templates` |
| Webhook テンプレートをアーカイブ | `archive_webhook_templates` |
| リンクテンプレートを表示 | `view_link_templates` |
| リンクテンプレートを編集 | `edit_link_templates` |
| メディアライブラリアセットを表示 | `view_media_library_assets` |
| 場所を表示 | `view_locations` |
| 場所を編集 | `edit_locations` |
| アーカイブ場所 | `archive_locations` |
| プロモーションコードを見る | `view_promotion_codes` |
| プロモーションコードを編集する | `edit_promotion_codes` |
| 輸出促進コード | `export_promotion_codes` |
| ユーザー設定センターを表示 | `view_preference_centers` |
| ユーザー設定センターを編集 | `edit_preference_centers` |
| レポートを編集する | `edit_reports` |
| 配置を見る | `view_placements` |
| 配置を編集する | `edit_placements` |
| 配置のアーカイブ | `archive_placements` |
| バナーテンプレートを表示 | `view_banner_templates` |
| 多言語設定を表示する | `view_multi_language_settings` |
| 演算子を使う | `use_operator` |
| Decisioning Studioエージェントを表示する | `view_decisioning_studio_agents` |
| Decisioning Studio オーディエンスを表示 |`view_decisioning_studio_audience` |
| Decisioning Studioのコンバージョンイベントを表示する | `view_decisioning_studio_conversion_event` |
| Decisioning Studio ガードレールを表示 | `view_decisioning_studio_guardrails` |
| キャンペーンを開始 | `launch_campaigns` |
| キャンバスを起動 | `launch_canvases` |
| ダッシュボードユーザーを編集 | `edit_dashboard_users` |
| メディアライブラリアセットを編集 | `edit_media_library_assets` |
| メディアライブラリアセットを削除 | `delete_media_library_assets` |
| インポートユーザーを閲覧 | `view_import_users` |
| ユーザーをインポート	| `import_users` |
| ユーザーデータを編集 | `edit_user_data` |
| ユーザーマージ記録を閲覧 | `view_user_merge_records` |
| 重複ユーザーのマージ | `merge_duplicate_users` |
| API キーを表示 | `view_api_keys` |
| API キーを編集 | `edit_api_keys` |
| 内部グループを表示する | `view_internal_user_groups` |
| 内部グループを編集する | `edit_internal_user_groups` |
| 内部グループを削除する | `delete_internal_user_groups` |
| メッセージアクティビティログを表示 | `view_message_activity_log` |
| イベントユーザーログを閲覧 | `view_event_user_log` |
| API 識別子を表示 | `view_api_identifiers` |
| API 使用状況ダッシュボードを表示 | `view_api_usage_dashboard` |
| API 制限を表示 | `view_api_limits` |
| API 使用アラートを表示 | `view_api_usage_alerts` |
| API 使用アラートを編集 | `edit_api_usage_alerts` |
| SDK デバッガーを表示 | `view_sdk_debugger` |
| SDK デバッガーを編集 | `edit_sdk_debugger` |
| コンテンツブロックを開始 | `launch_content_blocks` |
| クラウドデータの取り込みを編集 | `edit_cloud_data_ingestion` |
| アプリの設定を表示 | `view_app_settings` |
| アプリ設定を編集 | `edit_app_settings` |
| プッシュ設定を表示 | `view_push_settings` |
| プッシュ設定を編集 | `edit_push_settings` |
| チームを表示 | `view_teams` |
| チームを編集 | `edit_teams` |
| チームをアーカイブ | `archive_teams` |
| カスタム属性を表示 | `view_custom_attributes` |
| カスタム属性を編集 | `edit_custom_attributes` |
| 禁止リストのカスタム属性 | `blocklist_custom_attributes` |
| カスタム属性を削除 | `delete_custom_attributes` |
| カスタム属性をエクスポートする | `export_custom_attributes` |
| カスタムイベントを表示	 | `view_custom_events` |
| カスタムイベントを編集 | `edit_custom_events` |
| 禁止リストのカスタムイベント | `blocklist_custom_events` |
| カスタムイベントを削除 | `delete_custom_events` |
| カスタムイベントのエクスポート | `export_custom_events` |
| カスタムイベントプロパティのセグメンテーションを編集 | `edit_custom_event_property_segmentation` |
| 製品を表示 | `view_products` |
| 製品を編集	 | `edit_products` |
| 禁止リストの製品 | `blocklist_products` |
| 購入プロパティのセグメンテーションを編集 | `edit_purchase_property_segmentation` |
| タグを表示 | `view_tags` |
| タグを編集 | `edit_tags` |
| タグを削除 | `delete_tags` |
| メール設定を表示	| `view_email_settings` |
| メール設定を編集 | `edit_email_settings` |
| カタログを表示 | `view_catalogs` |
| カタログを編集	 | `edit_catalogs` |
| カタログをエクスポート | `export_catalogs` |
| カタログを削除 | `delete_catalogs` |
| WhatsAppの設定を表示する | `view_whatsapp_settings` |
| 編集テクノロジーパートナーズ | `edit_technology_partners` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### チームの許可文字列 {#team}

| 許可名 | SCIM API 文字列 |
| --- | --- |
| キャンペーンを表示 | `view_campaigns` |
| キャンペーンを編集 | `edit_campaigns` |
| キャンペーンをアーカイブ | `archive_campaigns` |
| キャンバスを表示 | `view_canvases` |
| キャンバスを編集 | `edit_canvases` |
|  個のキャンバス  | `archive_canvases` |
| フリークエンシーキャップルールを表示 | `view_frequency_caps` |
| フリークエンシーキャップルールを編集 | `edit_frequency_caps` |
| メッセージの優先順位付けを表示 | `view_message_prioritization` |
| メッセージの優先順位付けを編集 | `edit_message_prioritization` |
| コンテンツブロックを表示 | `view_content_blocks` |
| フィーチャーフラグを表示 | `view_feature_flags` |
| フィーチャーフラグを編集 | `edit_feature_flags` |
| フィーチャーフラグをアーカイブ | `archive_feature_flags` |
| セグメントを表示 | `view_segments` |
| セグメントの編集 | `edit_segments` |
| グローバルコントロールグループを編集する | `edit_global_control_group` |
| IAM テンプレートを表示 | `view_iam_templates` |
| IAM テンプレートを編集 | `edit_iam_templates` |
| IAM テンプレートをアーカイブ | `archive_iam_templates` |
| メールテンプレートを表示 | `view_email_templates` |
| メールテンプレートを編集 | `edit_email_templates` |
| メールテンプレートをアーカイブ | `archive_email_templates` |
| Webhook テンプレートを表示 | `view_webhook_templates` |
| Webhook テンプレートを編集 | `edit_webhook_templates` |
| Webhook テンプレートをアーカイブ | `archive_webhook_templates` |
| リンクテンプレートを表示 | `view_link_templates` |
| リンクテンプレートを編集 | `edit_link_templates` |
| メディアライブラリアセットを表示 | `view_media_library_assets` |
| 場所を表示 | `view_locations` |
| 場所を編集 | `edit_locations` |
| アーカイブ場所 | `archive_locations` |
| プロモーションコードを見る | `view_promotion_codes` |
| プロモーションコードを編集する | `edit_promotion_codes` |
| 輸出促進コード | `export_promotion_codes` |
| ユーザー設定センターを表示 | `view_preference_centers` |
| ユーザー設定センターを編集 | `edit_preference_centers` |
| レポートを見る | `view_reports` |
| レポートを作成する | `create_reports` |
| レポートを編集する | `edit_reports` |
| バナーテンプレートを表示 | `view_banner_templates` |
| 多言語設定を表示する | `view_multi_language_settings` |
| 演算子を使う | `use_operator` |
| Decisioning Studioエージェントを表示する | `view_decisioning_studio_agents` |
| Decisioning Studioのコンバージョンイベントを表示する | `view_decisioning_studio_conversion_event` |
| キャンペーンを開始 | `launch_campaigns` |
| キャンバスを起動 | `launch_canvases` |
| ダッシュボードユーザーを編集 | `edit_dashboard_users` |
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