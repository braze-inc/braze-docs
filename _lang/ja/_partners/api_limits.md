---
nav_title: レート制限
article_title: API レート制限
page_order: 4.5
description: "この参考記事では、Braze API インフラストラクチャの API レート制限について説明します。"
page_type: reference

---

# レート制限

> Braze API インフラストラクチャは、当社の顧客ベース全体で大量のデータを処理するように設計されています。このため、ワークスペースごとに API レート制限を適用しています。 

レート制限は、特定の期間に API が受信できるリクエストの数です。大規模システムにおける負荷ベースのサービス拒否インシデントの多くは、意図しないもの (ソフトウェアまたは構成のエラーによって引き起こされる) であり、悪意のある攻撃ではありません。レート制限は、このようなエラーによってお客様の Braze API リソースが奪われないことを確認します。特定の時間枠で送信されたリクエストが多すぎる場合、レート制限に達したことを示すステータスコードのエラーレスポンスが表示されることがあります。`429`

{% alert warning %}
APIレート制限は、システムの適切な使用状況に応じて変更される場合があります。損傷や誤用を防ぐために、API 呼び出しを行う際には適切な制限を設けることをお勧めします。
{% endalert %}

## リクエストタイプ別のレート制限

次の表は、さまざまなリクエストタイプのデフォルトの API レート制限を示しています。これらのデフォルト制限は、リクエストに応じて増やすことができます。詳細については、カスタマーサクセスマネージャーにお問い合わせください。

{% alert note %}
この表に記載されていないリクエストのデフォルトレート制限は、1 時間あたり 250,000 リクエストです。
{% endalert %}

| リクエストのタイプ | デフォルト API レート制限 |
| --- | --- |
| [`/users/track`][10] | **リクエスト:**1 分あたり 50,000 リクエスト。<br><br>**バッチ処理:**API リクエストごとに 75 件のイベント、75 件の購入、75 件の属性。詳細については、「[ユーザートラックリクエストの一括処理](#batch-user-track)」を参照してください。 |
| [`/users/export/ids`][11] | 1 分あたり 2,500 件のリクエスト。 |
| [`/users/delete`][12]<br>[`/users/alias/new`][13]<br>[`/users/alias/update`][45]<br>[`/users/identify`][14]<br>[`/users/merge`][44] | 1 分あたり 20,000 件のリクエストがエンドポイント間で共有されます。 |
| [`/users/external_id/rename`][20] | 1 分あたり 1,000 リクエスト。 |
| [`/users/external_id/remove`][21] | 1 分あたり 1,000 リクエスト。 |
| [`/events/list`][15] | 1 時間あたり 1,000 件のリクエスト、`/purchases/product_list`エンドポイントと共有されます。 |
| [`/purchases/product_list`][16] | 1 時間あたり 1,000 件のリクエスト、`/events/list`エンドポイントと共有されます。 |
| [`/campaigns/data_series`][17.3] | 1 分あたり 50,000 リクエスト。 |
| [`/messages/send`][17]<br>[`/campaigns/trigger/send`][17.1]<br>[`/canvas/trigger/send`][17.2]| ブロードキャストコールの 1 分あたり 250 リクエスト（セグメントまたは接続オーディエンスのみを指定した場合）。それ以外の場合は、1 時間あたり 250,000 件のリクエストがエンドポイント間で共有されます。 |
| [`/sends/id/create`][18] | 1 日あたり 100 リクエスト。 |
| [`/subscription/status/set`][19] | 1 分あたり 5,000 リクエスト。 |
| [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`][26]<br>[`/preference_center/v1/list`][27]<br>[`/preference_center/v1/{preferenceCenterExternalId}`][28] | 1 分あたり、1 ワークスペースあたり 1,000 リクエスト。 |
| [`/preference_center/v1`][29]<br>[`/preference_center/v1/{preferenceCenterExternalId}`][30] | 1 ワークスペースあたり 1 分あたり 10 リクエスト |
| [`/catalogs/{catalog_name}`][31]<br>[`/catalogs`][32]<br>[`/catalogs`][33] | 1 分あたり 50 リクエストがエンドポイント間で共有されます。 |
| [`/catalogs/{catalog_name}/items`][34]<br>[`/catalogs/{catalog_name}/items`][35]<br>[`/catalogs/{catalog_name}/items`][36] | 1 分あたり 16,000 リクエストがエンドポイント間で共有されます。 |
| [`/catalogs/{catalog_name}/items/{item_id}`][37]<br>[`/catalogs/{catalog_name}/items/{item_id}`][38]<br>[`/catalogs/{catalog_name}/items`][39]<br>[`/catalogs/{catalog_name}/items/{item_id}`][40]<br>[`/catalogs/{catalog_name}/items/{item_id}`][41] | 1 分あたり 50 リクエストがエンドポイント間で共有されます。 |
| [`/scim/v2/Users/{id}`][22]<br>[`/scim/v2/Users?filter={userName@example.com}`][43]<br>[`/scim/v2/Users/{id}`][25]<br>[`/scim/v2/Users/{id}}`][24]<br>[`/scim/v2/Users/`][23] | 1 社あたり 1 日あたり 5,000 件のリクエストをエンドポイント間で共有します。 |
{: .reset-td-br-1 .reset-td-br-2}

<!-- Add during CDI endpoints GA
| [`/cdi/integrations`][46] | 50 requests per minute. |
| [`/cdi/integrations/{integration_id}/sync`][47] | 20 requests per minute. |
| [`/cdi/integrations/{integration_id}/job_sync_status`][48] | 100 requests per minute. |
-->

## API リクエストのバッチ処理

Braze API はバッチ処理をサポートするように構築されています。バッチ処理を使用すると、Braze は 1 回の API 呼び出しでできるだけ多くのデータを取り込むことができるため、多くの API 呼び出しを行う必要がありません。Braze では、一度に 1 回の呼び出しでデータを処理するよりも、データをバッチで処理する方が効率的です。たとえば、バッチ処理された API 呼び出しを 1,000 回処理する方が、75,000 回の個別呼び出しを処理する場合よりも必要なリソースは少なくなります。バッチ処理は、1 時間あたり 75,000 回を超える呼び出しを必要とするアプリケーションにとって非常に重要です。

{% alert note %}
REST API のレート制限の引き上げは、API バッチ機能を利用するお客様のニーズに基づいて検討されます。
{% endalert %}

### ユーザートラックリクエストの一括処理 {#batch-user-track}

`/users/track`各リクエストには、最大 75 個のイベントオブジェクト、75 個の属性オブジェクト、75 個の購入オブジェクトを含めることができます。各オブジェクト (イベント、属性、購入配列) は、それぞれ 1 人のユーザーを更新できます。つまり、1回の呼び出しで最大225人のユーザーを更新できます。さらに、1 つのユーザープロファイルを複数のオブジェクトで更新できます。

このエンドポイントに対して行われたリクエストは、通常、次の順序で処理を開始します。 

1. 属性
2. イベント
3. 購入

### メッセージングエンドポイントリクエストのバッチ処理

[Messaging エンドポイントへの単一のリクエストは][1]、次のいずれかに到達できます。

- 最大50個まで`external_ids`、それぞれに個別のメッセージパラメータがあります
- Braze ダッシュボードで作成された任意のサイズのセグメント。 `segment_id`
- [リクエストでコネクテッドオーディエンスオブジェクトとして定義された、任意のサイズの追加のオーディエンスフィルターに一致するユーザー][2]

### バッチリクエストの例

次の例では、`external_id`を使用して電子メールと SMS の API 呼び出しを 1 回行います。

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

Braze に送信されるすべての API リクエストは、レスポンスヘッダーに次の情報を返します。

ヘッダー名             | 説明
----------------------- | -----------------------
`X-RateLimit-Limit`     | 指定した間隔 (レート制限) に実行できるリクエストの最大数。
`X-RateLimit-Remaining` | 現在のレート制限ウィンドウに残っているリクエストの数。
`X-RateLimit-Reset`     | 現在のレート制限ウィンドウがリセットされる時間（UTC エポック秒）。
{: .reset-td-br-1 .reset-td-br-2}

この情報は、Braze ダッシュボードではなく、API リクエストへの応答のヘッダーに意図的に含まれています。これにより、お客様が API を操作しているときに、システムがリアルタイムでより適切に反応できるようになります。たとえば、`X-RateLimit-Remaining`値が特定のしきい値を下回った場合は、送信速度を遅くして、すべてのトランザクションメールが送信されるようにしたい場合があります。または、ゼロになった場合は、`X-RateLimit-Reset`で指定した時間が経過するまですべての送信を一時停止したい場合があります。

API 制限について質問がある場合は、カスタマーサクセスマネージャーに問い合わせるか、[サポートチケットを開いてください][support]。

### エンドポイント間の最適な遅延

{% alert note %}
エラーを最小限に抑えるために、連続するエンドポイント呼び出しの間に 5 分間の遅延を設けることをお勧めします。
{% endalert %}

Braze API を連続して呼び出す場合は、エンドポイント間の最適な遅延を理解することが重要です。エンドポイントが他のエンドポイントの正常な処理に依存している場合に問題が発生し、呼び出しが早すぎるとエラーが発生する可能性があります。たとえば、エンドポイントを介してユーザーにエイリアスを割り当て、`/user/alias/new`そのエイリアスをヒットしてエンドポイントを介してカスタムイベントを送信する場合、どのくらい待つ必要がありますか？`/users/track`

通常の状態では、データの最終的な整合性が生じるまでの時間は 10 ～ 100 ミリ秒 (1/10 秒) です。ただし、整合性が保たれるまでに時間がかかる場合もあるため、エラーの可能性を最小限に抑えるために、2 回目以降の呼び出しの間に 5 分間の遅延を設けることをお勧めします。

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
