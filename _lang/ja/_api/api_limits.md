---
nav_title: レート制限
article_title: APIレート制限
page_order: 4.5
description: "この参考記事では、Braze API インフラの API レート制限について説明します。"
page_type: reference

---

# レート制限

> Braze の API インフラは、顧客ベース全体で大量のデータを処理できるように設計されています。このため、ワークスペースごとに API レート制限を設けています。

レート制限とは、API が一定時間内に受け取れるリクエスト数のことです。大規模システムにおける負荷ベースのサービス拒否インシデントの多くは、悪意のある攻撃ではなく、ソフトウェアや設定のエラーによって引き起こされる意図しないものです。レート制限は、このようなエラーによって Braze API のリソースがお客様に提供できなくなることを防ぎます。一定時間内に多くのリクエストが送信された場合、ステータスコード `429` のエラー応答が返されることがあります。これは、レート制限に達したことを示します。

{% alert warning %}
API レート制限は、システムの適切な使用状況に応じて変更される場合があります。損害や悪用を防ぐため、API コールを行う際には適切な制限を設けることを推奨します。
{% endalert %}

## リクエストタイプ別のレート制限

リクエストタイプ別のデフォルト API レート制限については、以下を参照してください。これらのデフォルトの制限は、リクエストに応じて増加できます。詳細については、カスタマーサクセスマネージャーにお問い合わせください。

### レート制限の異なるリクエスト

| リクエストのタイプ                                                                                                                                                                                                                                           | デフォルトの API レート制限                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)                                                                                                                                                                                                                                   | **リクエスト:** 3秒あたり3,000リクエスト。<br><br>**バッチ処理:** 1件の API リクエストあたり、`attributes`、`events`、`purchases` を合わせて最大75個のオブジェクト。レガシーレート制限が適用されているお客様は、各配列ごとに最大75個のオブジェクトを独立して含めることができます。詳細については、「[ユーザー追跡リクエストのバッチ処理](#batch-user-track)」を参照してください。<br><br>**2024-2025年度の月間アクティブユーザー数（MAU）の制限：ユニバーサルMAU、Web MAU、モバイルMAUについては、**[こちらの制限に関するガイダンスを]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25)参照してください。 |
| [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)                                                                                                                                                                                                                              | **2024年8月22日以降にオンボーディングした場合：** 毎分250リクエスト。<br><br> **2024年8月22日以前にオンボーディングした場合：** 毎分2,500リクエスト。                                                                                                                                                                                                                               |
| [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)<br>[`/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias/)<br>[`/users/alias/update`]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/)<br>[`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)<br>[`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)                                                                                                                    | 1分あたり20,000件のリクエストをエンドポイント間で共有します。                                                                                                                                                                                                                                                                                                                                 |
| [`/users/external_id/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/)                                                                                                                                                                                                                      | 1分あたり1,000件のリクエスト。                                                                                                                                                                                                                                                                                                                                                                |
| [`/users/external_id/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove/)                                                                                                                                                                                                                      | 1分あたり1,000件のリクエスト。                                                                                                                                                                                                                                                                                                                                                                |
| [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/)                                                                                                                                                                                                                                   | 1時間あたり1,000件のリクエスト、`/purchases/product_list` エンドポイントと共有されます。                                                                                                                                                                                                                                                                                                              |
| [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/)                                                                                                                                                                                                                        | 1時間あたり1,000件のリクエスト、`/events/list` エンドポイントと共有されます。                                                                                                                                                                                                                                                                                                                         |
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/)                                                                                                                                                                                                                       | 1分あたり50,000件のリクエスト。                                                                                                                                                                                                                                                                                                                                                               |
| [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)<br>[`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)<br>[`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)                                                                                                                                                          | ブロードキャストコール（セグメントやフィルター、接続済みオーディエンスを広く対象とする場合）では、全オーディエンス合計で毎分250リクエスト、**かつ**[ユニークオーディエンス]({{site.baseurl}}/api/api_limits/#what-counts-as-the-same-unique-audience)ごとに毎分10リクエスト（いずれか先に達した方が上限）。<br><br>それ以外の場合、個々の受信者を対象とするリクエストは、1時間あたり250,000リクエストの[共有レート制限]({{site.baseurl}}/api/api_limits/#requests-with-shared-rate-limits)に含まれます。                                                                                                                                                                                                                    |
| [`/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/)                                                                                                                                                                                                                               | 1日あたり100件のリクエスト。                                                                                                                                                                                                                                                                                                                                                                     |
| [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)                                                                                                                                                                                                                       | 毎分5,000リクエスト。                                                                                                                                                                                                                                                                                                                                                                |
| [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center/)<br>[`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/)<br>[`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/)                                                                            | 1分あたり1,000件のリクエスト。                                                                                                                                                                                                                                                                                                                                                 |
| [`/preference_center/v1`]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center/)<br>[`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/)                                                                                                                                                            | 1分あたり10件のリクエスト。                                                                                                                                                                                                                                                                                                                                                    |
| [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/)<br>[`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/)<br>[`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/)                                                                                                                                                                             | 1分あたり50件のリクエストをエンドポイント間で共有します。                                                                                                                                                                                                                                                                                                                                      |
| [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk/)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/)                                                                                                                             | 1分あたり16,000件のリクエストをエンドポイント間で共有します。                                                                                                                                                                                                                                                                                                                                  |
| [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/) | 1分あたり50件のリクエストをエンドポイント間で共有します。                                                                                                                                                                                                                                                                                                                                      |
| [`/catalogs/{catalog_name}/fields/{field_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field)<br>[`/catalogs/{catalog_name}/fields`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields)<br>[`/catalogs/{catalog_name}/selections/{selection_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection)<br>[`/catalogs/{catalog_name}/selections`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections) | 1分あたり50件のリクエストをエンドポイント間で共有します。 |
| [`/scim/v2/Users/{id}`]({{site.baseurl}}/get_see_user_account_information/)<br>[`/scim/v2/Users?filter={userName@example.com}`]({{site.baseurl}}/get_search_existing_dashboard_user_email/)<br>[`/scim/v2/Users/{id}`]({{site.baseurl}}/post_update_existing_user_account/)<br>[`/scim/v2/Users/{id}}`]({{site.baseurl}}/delete_existing_dashboard_user/)<br>[`/scim/v2/Users/`]({{site.baseurl}}/post_create_user_account/)                                                                          | 1日あたり5,000件のリクエスト（会社単位）をエンドポイント間で共有します。                                                                                                                                                                                                                                                                                                                        |
| [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list/)                                                                                                                                                                                                                              | 1分あたり50件のリクエスト。                                                                                                                                                                                                                                                                                                                                                                   |
| [`/cdi/integrations/{integration_id}/sync`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status/)                                                                                                                                                                                                        | 1分あたり20件のリクエスト。                                                                                                                                                                                                                                                                                                                                                                   |
| [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/post_job_sync/)                                                                                                                                                                                             | 1分あたり100件のリクエスト。                                                                                                                                                                                                                                                                                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### レート制限を共有するリクエスト

以下のリクエストには、1時間あたり250,000件のレート制限があり、リクエスト間で共有されます。

- [`/app_group/sdk_authentication/create`]({{site.baseurl}}/api/endpoints/sdk_authentication/post_create_sdk_authentication_key/)
- [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys/)
- [`/app_group/sdk_authentication/delete`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key)
- [`/app_group/sdk_authentication/primary`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key/)
- [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details)
- [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns)
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) （非ブロードキャストコールのみ&#8212;`external_user_ids` または `aliases` を指定するコール）
- [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/)
- [`/campaigns/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/)
- [`/campaigns/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/)
- [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/)
- [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/)
- [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/)
- [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/)
- [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) （非ブロードキャストコールのみ）
- [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)
- [`/canvas/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/)
- [`/canvas/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/)
- [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/)
- [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/)
- [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/)
- [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/)
- [`/email/blocklist`]({{site.baseurl}}/api/endpoints/email/post_blocklist/)
- [`/email/blacklist`]({{site.baseurl}}/api/endpoints/email/post_blacklist/)
- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces/)
- [`/email/hard_bounces`]({{site.baseurl}}/api/endpoints/email/get_list_hard_bounces/)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam/)
- [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/)
- [`/email/unsubscribes`]({{site.baseurl}}/api/endpoints/email/get_query_unsubscribed_email_addresses/)
- [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/)
- [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/)
- [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/)
- [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/)
- [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/)
- [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start)
- [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update/)
- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) （非ブロードキャストコールのみ）
- [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/)
- [`/messages/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/)
- [`/messages/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/)
- [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/)
- [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/)
- [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/)
- [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/)
- [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/)
- [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/)
- [`/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers/)
- [`/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers/)
- [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/)
- [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/)
- [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/)
- [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/)
- [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/)
- [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/)
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)

### 同一のユニークオーディエンスとしてカウントされる条件 {#what-counts-as-the-same-unique-audience}

これは以下の3つのエンドポイントに適用されます：[`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)、[`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)、および [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)。

これらのエンドポイントにおいて、以下の条件がすべて一致する場合、ブロードキャストリクエストは同一のユニークオーディエンスを対象としていると見なされます：

- トリガーされるキャンペーンまたはキャンバス（API リクエスト内の `campaign_id` または `canvas_id`（指定されている場合））
- 対象とするオーディエンス（セグメントやフィルター、あるいは API キャンペーンの場合は API リクエスト内の `segment_id`）
- 接続されたオーディエンスフィルター（API リクエスト内の `audience` オブジェクト（指定されている場合））

これらの属性のユニークな組み合わせはそれぞれが独立したオーディエンスとしてカウントされるため、各ユニークオーディエンスに対する追加のレート制限は、それぞれの組み合わせに対して個別に適用されます。

## API リクエストのバッチ処理

Braze の API は、バッチ処理をサポートするように構築されています。バッチ処理により、Braze は1回の API コールで可能な限り多くのデータを取り込むことができるため、多数の API コールを行う必要がなくなります。Braze にとって、データを一度に1コールずつ処理するよりも、バッチで処理する方が効率的です。例えば、1,000件のバッチ API コールを処理する場合、75,000回の個別のコールを処理する場合よりも必要なリソースが少なくなります。1時間あたり75,000回を超えるコールが必要なアプリケーションでは、バッチ処理は非常に重要です。

{% alert note %}
REST API のレート制限の増加は、API バッチ処理機能を利用しているお客様のニーズに基づいて検討されます。
{% endalert %}

### ユーザー追跡エンドポイントへのリクエストのバッチ処理 {#batch-user-track}

`/users/track` の各リクエストには、`attributes`、`events`、`purchases` を合わせて最大75個のオブジェクトを含めることができます。各オブジェクトは1人のユーザーを更新できます。単一のユーザープロファイルを複数のオブジェクトによって更新することもできます。

{% details レガシーレート制限 %}
レガシーレート制限が適用されているお客様の場合、各配列（`attributes`、`events`、`purchases`）にはそれぞれ独立して最大75個のオブジェクトを含めることができ、1リクエストあたり最大225個のオブジェクトを組み合わせることができます。
{% enddetails %}

`/users/track` のレート制限の詳細については、[POST: ユーザーの作成と更新]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を参照してください。

このエンドポイントへのリクエストは通常、以下の順序で処理が開始されます：

1. 属性
2. イベント
3. 購入

### メッセージングエンドポイントリクエストのバッチ処理

[メッセージングエンドポイント]({{site.baseurl}}/api/endpoints/messaging/)への単一のリクエストは、次のいずれかに到達できます：

- それぞれに個別のメッセージパラメーターを持つ、最大50個の特定の `external_ids`
- `segment_id` で指定される、Braze ダッシュボードで作成された任意のサイズのセグメント
- リクエストの中で[接続オーディエンス]({{site.baseurl}}/api/objects_filters/connected_audience/)オブジェクトとして定義された、任意のサイズの追加オーディエンスフィルターに一致するユーザー

### バッチリクエストの例

以下の例では、`external_id` を使って、メールと SMS の API コールを1回で行っています。

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@email.com"]
    },
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@email.com"]
    }
  ]
}
```

## レート制限の監視

Braze に送信されたすべての API リクエストは、レスポンスヘッダーに以下の情報を返します：

| ヘッダー名             | 説明                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| `X-RateLimit-Limit`     | 指定された間隔内に実行できるリクエストの最大数（レート制限）。 |
| `X-RateLimit-Remaining` | 現在のレート制限期間内に残っているリクエストの数。                          |
| `X-RateLimit-Reset`     | 現在のレート制限期間がリセットされる時刻（UTC エポック秒）。                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

この情報は、Braze ダッシュボードではなく、API リクエストに対するレスポンスのヘッダーに意図的に含まれています。これにより、お客様のシステムは API とのやり取り中にリアルタイムでより適切に対応できます。例えば、`X-RateLimit-Remaining` の値がある閾値を下回った場合、すべてのトランザクションメールが確実に送信されるように送信速度を落とすことができます。あるいは、ゼロに達した場合は、`X-RateLimit-Reset` で指定された時間が経過するまですべての送信を一時停止することもできます。

{% alert note %}
HTTP ヘッダーはすべて小文字で返されます。この動作は、すべてのヘッダーフィールド名を小文字にすることを義務付けた HTTP/2 プロトコルに準拠しています。これは、HTTP/1.X ではヘッダー名の大文字小文字は区別されないものの、一般的にさまざまな大文字表記で記述されていたのとは異なります。
{% endalert %}

API の制限についてご質問がある場合は、カスタマーサクセスマネージャーにお問い合わせいただくか、[サポートチケット]({{site.baseurl}}/braze_support/)を開いてください。

{% alert tip %}
[API 使用状況ダッシュボード]({{site.baseurl}}/user_guide/analytics/dashboard/api_usage_dashboard/)を使用すると、受信トラフィックをレート制限と比較して確認できます。
{% endalert %}

### エンドポイント間の最適な遅延

{% alert note %}
エラーを最小限に抑えるため、連続するエンドポイントコールの間に5分間の遅延を設けることを推奨します。
{% endalert %}

Braze API を連続して呼び出す場合は、エンドポイント間の最適な遅延を理解することが重要です。エンドポイントが他のエンドポイントの正常な処理に依存している場合、呼び出しが早すぎるとエラーが発生する可能性があります。例えば、`/user/alias/new` エンドポイントを通じてユーザーにエイリアスを割り当て、そのエイリアスを使用して `/users/track` エンドポイントを通じてカスタムイベントを送信する場合、どのくらい待つべきでしょうか？

通常の状態では、データの結果整合性が達成されるまでの時間は10〜100ミリ秒（1/10秒）です。しかし、整合性の達成に時間がかかる場合もあるため、エラーの確率を最小限にするために、後続のコールの間に5分間の遅延を設けることを推奨します。

### レート制限のリセット

レート制限は、ローリングウィンドウではなく、時計の正時にリセットされます。例えば、制限が1時間あたり250,000リクエストの場合、午後10時00分から午後10時59分の間に50,000リクエストを行い、午後11時00分から午後11時59分の間にさらに250,000リクエストを行うことができます。これは、カウンターが毎時の正時にリセットされるためです。