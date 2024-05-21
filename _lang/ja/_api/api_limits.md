---
nav_title: レート制限
article_title: API レート制限
page_order: 4.5
description: "このリファレンス記事では、BrazeAPIインフラストラクチャのAPIレート制限について説明します。"
page_type: reference

---

# レート制限

> Braze API インフラストラクチャは、顧客ベース全体で大量のデータを処理するように設計されています。このために、ワークスペースごとにAPI レート制限を適用します。 

レート制限は、API が特定の期間に受信できるリクエストの数です。大規模システムにおける負荷ベースのサービス拒否インシデントの多くは、意図しないものです。これは、ソフトウェアや構成のエラーによるものです。悪意のある攻撃ではありません。レート制限は、このようなエラーが顧客からのBraze APIリソースを奪うことがないことを確認します。所定の時間内に送信されるリクエストが多すぎる場合、エラーレスポンスで`429` というステータスコードが表示されることがあります。これは、レート制限に達したことを示しています。

{% alert warning %}
APIレートリミットは、当社システムの適切な使用方法によって変更される場合があります。私たちは、破損や誤使用を防ぐためにAPIコールを行う際には、合理的な制限を推奨します。
{% endalert %}

## リクエストタイプ別のレート制限

次の表に、さまざまなリクエストタイプのデフォルトのAPI レート制限を示します。これらのデフォルトの制限は、要求に応じて増やすことができます。詳細については、カスタマー・サクセス・マネージャーにお問い合わせください。

{% alert note %}
このテーブルにリストされていないリクエストは、1 時間あたり 250,000 リクエストという合計デフォルトレート制限を共有します。
{% endalert %}

| 要求タイプ| デフォルトAPI レート制限|
| --- | --- |
| [`/users/track`][10] | **リクエスト:**1 分あたり 50,000 件のリクエスト。<br><br>**バッチ処理:**API リクエストごとに、75 個のイベント、75 個の購入、および75 個の属性。詳細については、[ユーザーのトラック要求のバッチ処理](#batch-user-track)を参照してください。|
| [`/users/export/ids`][11]| 1 分あたり2500 件のリクエスト|
| [`/users/delete`][12]<br>[`/users/alias/new`][13]<br>[`/users/alias/update`][45]<br>[`/users/identify`][14]<br>[`/users/merge`][44] | エンドポイント間で共有される、1 分あたり 20,000 件のリクエスト。|
| [`/users/external_id/rename`][20]| 1 分あたり1000 件のリクエスト|
| [`/users/external_id/remove`][21]| 1 分あたり1000 件のリクエスト|
| [`/events/list`][15] | 1,000 requests per hour, shared with the `/purchases/product_list` endpoint. |
| [`/purchases/product_list`][16] | 1,000 requests per hour, shared with the `/events/list` endpoint. |
| [`/campaigns/data_series`][17.3] | 50,000 requests per minute. |
| [`/messages/send`][17] | ブロードキャストコール(セグメントまたはConnected Audience のみを指定する場合) 1 分あたり250 件のリクエスト。それ以外の場合は、1 時間あたり250,000 件のリクエスト。|
| [`/campaigns/trigger/send`][17.1] | ブロードキャストコールに対する1 分あたり250 件のリクエスト(セグメントまたはConnected Audience のみを指定する場合)。それ以外の場合は、1 時間あたり250,000 件のリクエスト。|
| [`/canvas/trigger/send`][17.2] | ブロードキャストコール(セグメントまたはConnected Audience のみを指定する場合) 1 分あたり250 件のリクエスト。それ以外の場合は、1 時間あたり250,000 件のリクエスト。|
| [`/sends/id/create`][18] | 1 日あたり100 件のリクエスト。|
| [`/subscription/status/set`][19]| 1 分あたり5000 件のリクエスト|
| [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`][26]<br>[`/preference_center/v1/list`][27]<br>[`/preference_center/v1/{preferenceCenterExternalId}`][28] | 1 分あたり 1000 件のリクエスト (ワークスペースあたり) |
| [`/preference_center/v1`][29]<br>[`/preference_center/v1/{preferenceCenterExternalId}`][30] | 1 分あたり10 件の要求(ワークスペースあたり) |
| [`/catalogs/{catalog_name}`][31]<br>[`/catalogs`][32]<br>[`/catalogs`][33] | エンドポイント間で共有される 1 分あたり 50 リクエスト。|
| [`/catalogs/{catalog_name}/items`][34]<br>[`/catalogs/{catalog_name}/items`][35]<br>[`/catalogs/{catalog_name}/items`][36] | エンドポイント間で共有される1 分あたり16,000 件のリクエスト。|
| [`/catalogs/{catalog_name}/items/{item_id}`][37]<br>[`/catalogs/{catalog_name}/items/{item_id}`][38]<br>[`/catalogs/{catalog_name}/items`][39]<br>[`/catalogs/{catalog_name}/items/{item_id}`][40]<br>[`/catalogs/{catalog_name}/items/{item_id}`][41] | エンドポイント間で共有される 1 分あたり 50 リクエスト。|
| [`/scim/v2/Users/{id}`][22]<br>[`/scim/v2/Users?filter={userName@example.com}`][43]<br>[`/scim/v2/Users/{id}`][25]<br>[`/scim/v2/Users/{id}}`][24]<br>[`/scim/v2/Users/`][23] | エンドポイント間で共有される、1 日あたり1 社あたり5000 件のリクエスト。|
{: .reset-td-br-1 .reset-td-br-2}

<!-- Add during CDI endpoints GA
| [`/cdi/integrations`][46] | 50 requests per minute. |
| [`/cdi/integrations/{integration_id}/sync`][47] | 20 requests per minute. |
| [`/cdi/integrations/{integration_id}/job_sync_status`][48] | 100 requests per minute. |
-->

## API 要求のバッチ処理

BrazeAPI はバッチ処理をサポートするように構築されています。バッチ処理を使用すると、Braze は1 回のAPI 呼び出しでできるだけ多くのデータを取り込むことができるため、多くのAPI 呼び出しを行う必要がありません。データを一度に1 回の呼び出しで処理するよりも、Braze でデータを一度に処理する方が効率的です。たとえば、1000 回のバッチAPI コールを処理すると、75,000 回の個別コールを処理するよりも少ないリソースが必要になります。バッチ処理は、1 時間に75,000 回を超えるコールが必要なアプリケーションでは非常に重要です。

{% alert note %}
REST API レート制限の増加は、API バッチ機能を使用している顧客のニーズに基づいて考慮されます。
{% endalert %}

### ユーザートラック要求のバッチ処理 {#batch-user-track}

各`/users/track` リクエストには、最大75 個のイベントオブジェクト、75 個の属性オブジェクト、および75 個の購入オブジェクトを含めることができます。各オブジェクト(イベント、属性、購入アレイ)は、各1 人のユーザーを更新できます。これにより、1回の通話で最大225人のユーザを更新できます。また、1 つのユーザープロファイルを複数のオブジェクトで更新できます。

このエンドポイントに対して行われた要求は、通常、次の順序で処理を開始します。 

1. 属性
2. イベント
3. 購入

### バッチメッセージングエンドポイント要求

[メッセージングエンドポイント][1]への単一のリクエストは、次のいずれかに到達できます。

- 最大50 個の特定の`external_ids`、それぞれ個別のメッセージパラメータを含む
- Braze ダッシュボードで作成された任意のサイズのセグメント。Braze ダッシュボードで指定されます `segment_id`
- リクエストで[接続されたオーディエンス][2]オブジェクトとして定義されている任意のサイズの追加のオーディエンスフィルタに一致するユーザ

## レート制限の監視

Braze に送信された 1 つの API リクエストごとに、レスポンスヘッダーに以下の情報が返されます。

ヘッダ名| 説明
----------------------- | -----------------------
`X-RateLimit-Limit`     | 指定した間隔で実行できるリクエストの最大数(レート制限)。
`X-RateLimit-Remaining` | 現在のレート制限ウィンドウに残っている要求の数。
`X-RateLimit-Reset`     | 現在のレート制限ウィンドウがUTC エポック秒でリセットされる時間。
{: .reset-td-br-1 .reset-td-br-2}

この情報は、Braze ダッシュボードではなく、API 要求に対する応答のヘッダーに意図的に含まれています。これにより、システムは、API とやり取りする際にリアルタイムでより効果的に反応できます。たとえば、`X-RateLimit-Remaining` の値が特定のしきい値を下回った場合、すべてのトランザクションメールが確実に送信されるように送信を遅くすることができます。または、ゼロに達した場合は、`X-RateLimit-Reset` で指定した時間が経過するまで、すべての送信を一時停止することができます。

API 制限についてご質問がある場合は、カスタマーサクセスマネージャーにお問い合わせいただくか、[サポートチケット][support] を開きます。

### エンドポイント間の最適遅延

{% alert note %}
エラーを最小限に抑えるために、連続するエンドポイントコールの間に5 分の遅延を許可することをお勧めします。
{% endalert %}

Braze API を連続して呼び出す場合、エンドポイント間の最適な遅延を理解することが重要です。エンドポイントが他のエンドポイントの正常な処理に依存している場合、問題が発生し、呼び出しが早すぎるとエラーが発生する可能性があります。たとえば、ユーザーに`/user/alias/new` エンドポイント経由でエイリアスを割り当て、そのエイリアスをヒットして`/users/track` エンドポイント経由でカスタムイベントを送信する場合、どのくらいの期間待機する必要がありますか?

通常の条件下では、データの整合性が実現するまでの時間は10 ～100ms (1/10 秒) です。ただし、その整合性の発生に時間がかかる場合があるため、エラーの可能性を最小限に抑えるために、後続の呼び出しの間に5 分の遅延を許可することをお勧めします。

[1]: {{site.baseurl}}/api/endpoints/messaging/
[2]: {{site.baseurl}}/api/objects_filters/connected_audience/
[support]: {{site.baseurl}}/braze_support/
[10]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[11]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[12]: {{site.baseurl}}/api/endpoints/user_data/post_user_delete/
[13]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[14]: {{site.baseurl}}/api/endpoints/user_data/post_user_identify/
[15]: {{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/
[16]: {{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/
[17]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/
[17.1]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
[17.2]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/
[17.3]: {{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/
[18]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/
[19]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[20]: {{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/
[21]: {{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove/
[22]: {{site.baseurl}}/get_see_user_account_information/
[23]: {{site.baseurl}}/post_create_user_account/
[24]: {{site.baseurl}}/delete_existing_dashboard_user/
[25]: {{site.baseurl}}/post_update_existing_user_account/
[26]: {{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center/
[27]: {{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/
[28]: {{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/
[29]: {{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center/
[30]: {{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/
[31]: {{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/
[32]: {{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/
[33]: {{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/
[34]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk/
[35]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/
[36]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/
[37]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/
[38]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/
[39]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/
[40]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/
[41]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/
[43]: {{site.baseurl}}/get_search_existing_dashboard_user_email/
[44]: {{site.baseurl}}/api/endpoints/user_data/post_users_merge/
[45]: {{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/
[46]: {{site.baseurl}}/api/endpoints/cdi/get_integration_list/
[47]: {{site.baseurl}}/api/endpoints/cdi/job_sync/
[48]: {{site.baseurl}}/api/endpoints/cdi/job_sync_status/