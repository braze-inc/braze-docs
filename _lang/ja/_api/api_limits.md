---
nav_title: レート制限
article_title: APIレート制限
page_order: 4.5
description: "この参考記事では、Braze API インフラの API レート制限について説明します。"
page_type: reference

---

# レート制限

> BrazeのAPIインフラストラクチャは、顧客ベース全体で大量のデータを処理できるように設計されている。このため、ワークスペースごとにAPIレートの制限を設けている。

レート制限とは、APIが一定時間内に受け取れるリクエスト数のことである。大規模システムにおける負荷ベースのサービス拒否インシデントの多くは、悪意のある攻撃ではなく、ソフトウェアや設定のエラーによって引き起こされる意図的でないものである。レート制限は、このようなエラーがBraze APIのリソースをお客様から奪うことがないようにチェックする。一定時間内に多くのリクエストが送信された場合、ステータスコード`429` のエラー応答が表示されることがある。これは、レート制限にヒットしたことを示す。

{% alert warning %}
API レート制限は、システムの適切な使用状況に応じて変更される場合があります。損害や悪用を防ぐため、APIコールを行う際には常識的な制限を設けることを推奨する。
{% endalert %}

## リクエストタイプ別のレート制限

以下の表に、リクエストタイプ別のデフォルトのAPIレート制限を示す。これらのデフォルトの制限は、リクエストに応じて増加できます。詳細については、カスタマーサクセスマネージャーにお問い合わせください。

{% alert note %}
この表に記載されていないリクエストは、合計で 1 時間あたり 250,000 件のリクエストというデフォルトのレート制限を共有します。
{% endalert %}

| リクエストのタイプ                                                                                                                                                                                                                                           | デフォルトの API レート制限                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [`/users/track`][10]                                                                                                                                                                                                                                   | **リクエスト:**3000リクエスト/3秒。<br><br>**バッチ処理:**1 件の API リクエストあたり、75 件のイベント、75 件の購入、75 個の属性。詳細については、「[ユーザー追跡リクエストのバッチ処理](#batch-user-track)」を参照してください。<br><br>**CY24-25の月間アクティブユーザーの制限：** [CY24-25の月間アクティブユーザーの制限]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25)を参照してください。 |
| [`/users/export/ids`][11]                                                                                                                                                                                                                              | **2024年8月22日以降にオンボーディングした場合：**毎分250リクエスト。<br><br> **2024年8月22日以前にオンボーディングした場合：**毎分2500リクエスト。                                                                                                                                                                   |
| [`/users/delete`][12]<br>[`/users/alias/new`][13]<br>[`/users/alias/update`][45]<br>[`/users/identify`][14]<br>[`/users/merge`][44]                                                                                                                    | 1 分あたり 20,000 件のリクエストをエンドポイント間で共有します。                                                                                                                                  |
| [`/users/external_id/rename`][20]                                                                                                                                                                                                                      | 1 分あたり 1,000 件のリクエスト。                                                                                                                                                                 |
| [`/users/external_id/remove`][21]                                                                                                                                                                                                                      | 1 分あたり 1,000 件のリクエスト。                                                                                                                                                                 |
| [`/events/list`][15]                                                                                                                                                                                                                                   | 1 時間あたり 1,000 件のリクエスト、`/purchases/product_list` エンドポイントと共有されます。                                                                                                               |
| [`/purchases/product_list`][16]                                                                                                                                                                                                                        | 1 時間あたり 1,000 件のリクエスト、`/events/list` エンドポイントと共有されます。                                                                                                                          |
| [`/campaigns/data_series`][17.3]                                                                                                                                                                                                                       | 1 分あたり 50,000 件のリクエスト。                                                                                                                                                                |
| [`/messages/send`][17]<br>[`/campaigns/trigger/send`][17.1]<br>[`/canvas/trigger/send`][17.2]                                                                                                                                                          | ブロードキャストコールの場合、1 分あたり 250 リクエスト (セグメントまたはコネクテッドオーディエンスのみを指定した場合)。それ以外の場合は、エンドポイント間で 1 時間あたり 250,000 件のリクエストが共有されます。                     |
| [`/sends/id/create`][18]                                                                                                                                                                                                                               | 1 日あたり 100 件のリクエスト。                                                                                                                                                                      |
| [`/subscription/status/set`][19]                                                                                                                                                                                                                       | 毎分5000リクエスト。                                                                                                                                                                 |
| [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`][26]<br>[`/preference_center/v1/list`][27]<br>[`/preference_center/v1/{preferenceCenterExternalId}`][28]                                                                            | ワークスペースごとに毎分1,000リクエスト。                                                                                                                                                  |
| [`/preference_center/v1`][29]<br>[`/preference_center/v1/{preferenceCenterExternalId}`][30]                                                                                                                                                            | ワークスペースごとに 1 分あたり 10 件のリクエスト。                                                                                                                                                     |
| [`/catalogs/{catalog_name}`][31]<br>[`/catalogs`][32]<br>[`/catalogs`][33]                                                                                                                                                                             | 1 分あたり 50 件のリクエストをエンドポイント間で共有します。                                                                                                                                       |
| [`/catalogs/{catalog_name}/items`][34]<br>[`/catalogs/{catalog_name}/items`][35]<br>[`/catalogs/{catalog_name}/items`][36]                                                                                                                             | 1 分あたり 16,000 件のリクエストをエンドポイント間で共有します。                                                                                                                                   |
| [`/catalogs/{catalog_name}/items/{item_id}`][37]<br>[`/catalogs/{catalog_name}/items/{item_id}`][38]<br>[`/catalogs/{catalog_name}/items`][39]<br>[`/catalogs/{catalog_name}/items/{item_id}`][40]<br>[`/catalogs/{catalog_name}/items/{item_id}`][41] | 1 分あたり 50 件のリクエストをエンドポイント間で共有します。                                                                                                                                       |
| [`/scim/v2/Users/{id}`][22]<br>[`/scim/v2/Users?filter={userName@example.com}`][43]<br>[`/scim/v2/Users/{id}`][25]<br>[`/scim/v2/Users/{id}}`][24]<br>[`/scim/v2/Users/`][23]                                                                          | 1 分あたり 5,000 件のリクエストをエンドポイント間で共有します。                                                                                                                         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<!-- Add during CDI endpoints GA
| [`/cdi/integrations`][46] | 50 requests per minute. |
| [`/cdi/integrations/{integration_id}/sync`][47] | 20 requests per minute. |
| [`/cdi/integrations/{integration_id}/job_sync_status`][48] | 100 requests per minute. |
-->

## APIリクエストをバッチ処理する

BrazeのAPIは、バッチ処理をサポートするように構築されている。バッチ処理により、Brazeは1回のAPIコールで可能な限り多くのデータを取り込むことができるため、多くのAPIコールを行う必要がなくなる。Brazeにとって、データを一度に1コールずつ処理するよりも、バッチで処理する方が効率的なのだ。例えば、1,000 件のバッチ API 呼び出しを処理する場合、75,000 回の個別の呼び出しを処理する場合よりも必要なリソースが少なくなります。1 時間あたり 75,000 回を超える呼び出しが必要なアプリケーションでは、バッチ処理は非常に重要です。

{% alert note %}
REST API のレート制限の増加は、API バッチ処理機能を利用している顧客のニーズに基づいて検討されます。
{% endalert %}

### ユーザー追跡リクエストのバッチ処理 {#batch-user-track}

`/users/track` の各リクエストには、最大 75 個のイベントオブジェクト、75 個の属性オブジェクト、75 個の購買オブジェクトを含めることができます。各オブジェクト（イベント、アトリビュート、購入アレイ）は、それぞれ1人のユーザーを更新することができる。合計すると、1 回の呼び出しで最大 225 人のユーザーを更新できることになります。さらに、単一のユーザープロファイルを複数のオブジェクトによって更新することもできます。

このエンドポイントへのリクエストは通常、この順番で処理を開始する：

1. 属性
2. イベント
3. 購入

### メッセージングエンドポイントリクエストのバッチ処理

[メッセージングエンドポイント][1]への単一のリクエストは、次のいずれかに到達できます。

- それぞれに個別のメッセージパラメーターを持つ、最大 50 個の特定の `external_ids`
- `segment_id` で指定される、Braze ダッシュボードで作成された任意のサイズのセグメント
- リクエストの中で[接続オーディエンス][2]オブジェクトとして定義された、任意のサイズの追加オーディエンスフィルターにマッチするユーザー。

### バッチリクエストの例

以下の例では、`external_id` を使って、EメールとSMSのAPIコールを1回行っている。

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

Brazeに送信されたすべてのAPIリクエストは、レスポンスヘッダに以下の情報を返す：

| ヘッダー名             | 説明                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| `X-RateLimit-Limit`     | 指定された間隔内に実行できるリクエストの最大数 (レート制限)。 |
| `X-RateLimit-Remaining` | 現在のレート制限期間内に残っているリクエストの数。                          |
| `X-RateLimit-Reset`     | 現在のレート制限期間が UTC エポック秒でリセットされる時刻。                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

この情報は、Brazeダッシュボードではなく、APIリクエストに対するレスポンスのヘッダーに意図的に含まれている。これにより、あなたのシステムは、あなたが私たちのAPIとやりとりしているときにリアルタイムでよりよく反応することができる。例えば、`X-RateLimit-Remaining` の値がある閾値を下回った場合、すべてのトランザクションメールが送信されるように、送信を遅くしたいかもしれない。あるいは、ゼロになったら、`X-RateLimit-Reset` で指定された時間が経過するまで、すべての送信を一時停止することもできる。

{% alert note %}
HTTPヘッダーはすべて小文字で返される。この動作は、すべてのヘッダーフィールド名を小文字にすることを義務付けたHTTP/2プロトコルと一致している。これは、HTTP/1.Xではヘッダー名の大文字小文字は区別されないが、一般的に 様々な大文字で書かれていたのとは異なる。
{% endalert %}

API の制限についてご質問がある場合は、カスタマーサクセスマネージャーにお問い合わせいただくか、[サポートチケット][support]を開いてください。

### エンドポイント間の最適遅延

{% alert note %}
エラーを最小限に抑えるため、連続するエンドポイント・コールの間に5分間の遅延を設けることを推奨する。
{% endalert %}

Braze API を連続して呼び出す場合は、エンドポイント間の最適な遅延を理解することが重要です。エンドポイントが他のエンドポイントの正常な処理に依存している場合に問題が発生すると、呼び出しが早すぎる場合はエラーが発生する可能性があります。例えば、`/user/alias/new` エンドポイントを通じてユーザーにエイリアスを割り当て、そのエイリアスを使用して`/users/track` エンドポイントを通じてカスタム・イベントを送信する場合、どのくらい待つべきか？

通常の条件下では、データの最終的な一貫性が実現されるまでの時間は 10 ～ 100 ミリ秒 (1/10 秒) です。しかし、その整合性が取れるまでに時間がかかる場合もあるので、エラーの確率を最小限にするために、後続のコールをかける間隔を5分ほど空けることをお勧めする。

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
