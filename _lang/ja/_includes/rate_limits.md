<!---DEFAULT RATE LIMIT-->

{% if include.endpoint == "default" %}
[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、このエンドポイントには Braze のデフォルトのレート制限である1時間あたり250,000リクエストが適用されます。

<!---PUT /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "update dashboard user" %}
このエンドポイントには、1日あたり1会社あたり5,000リクエストのレート制限があります。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/scim/v2/Users/` GET、DELETE、および POST エンドポイントと共有されます。

<!---GET /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "look up dashboard user" %}
このエンドポイントには、1日あたり1会社あたり5,000リクエストのレート制限があります。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/scim/v2/Users/` PUT、GET、DELETE、および POST エンドポイントと共有されます。

<!---DELETE /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "delete dashboard user" %}
このエンドポイントには、1日あたり1会社あたり5,000リクエストのレート制限があります。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/scim/v2/Users/` PUT、GET、および POST エンドポイントと共有されます。

<!---POST /scim/v2/Users--->
{% elsif include.endpoint == "create dashboard user" %}
このエンドポイントには、1日あたり1会社あたり5,000リクエストのレート制限があります。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/scim/v2/Users/` PUT、GET、および DELETE エンドポイントと共有されます。

<!---GET /scim/v2/Users--->
{% elsif include.endpoint == "look up dashboard user email" %}
このエンドポイントには、1日あたり1会社あたり5,000リクエストのレート制限があります。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/scim/v2/Users/` PUT、GET、DELETE、および POST エンドポイントと共有されます。

<!---/users/external_id/rename-->
<!---/users/external_id/remove-->

{% elsif include.endpoint == "external id migration" %}
[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、このエンドポイントには1分あたり1,000リクエストのレート制限が適用されます。

<!---/users/track-->

{% elsif include.endpoint == "users track" %}
2024年10月28日より、すべての顧客に対して、このエンドポイントに3秒あたり3,000リクエストの基本速度制限を適用します。各 `/users/track` リクエストには、最大75個のイベントオブジェクト、75個の属性オブジェクト、75個の購入オブジェクトを含めることができます。各オブジェクト（イベント、属性、および購入配列）は、それぞれ1人のユーザーを更新できます。合計すると、1回の呼び出しで最大225人のユーザーを更新できることになります。さらに、1つのユーザープロファイルを複数のオブジェクトで更新することもできます。

**Monthly Active Users - CY 24-25** を購入した顧客には異なる制限が適用されます。これらの制限の詳細については、[Monthly Active Users - CY 24-25 の制限]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25-universal-mau-web-mau-and-mobile-mau)を参照してください。

詳細については、[API レート制限]({{site.baseurl}}/api/api_limits/)のページを参照してください。制限の引き上げが必要な場合は、カスタマーサクセスマネージャーにお問い合わせください。

<!---/users/export/ids-->

{% elsif include.endpoint == "users export ids" %}
2024年8月22日以降に Braze にオンボーディングした場合、このエンドポイントには、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、1分あたり250リクエストのレート制限が適用されます。

また、以下の条件を満たすことで、このエンドポイントのレート制限を1秒あたり40リクエストに引き上げることもできます。

- ワークスペースでデフォルトのレート制限（1分あたり250リクエスト）が有効になっていること。既存のレート制限の解除については、Braze アカウントマネージャーにお問い合わせください。
- リクエストに、受け取りたいすべてのフィールドを列挙した `fields_to_export` パラメーターが含まれていること。

{% alert important %}
`fields_to_export` パラメーターに `canvases_received` または `campaigns_received` を含めると、リクエストは高速レート制限の対象外となります。具体的なユースケースがある場合にのみ、リクエストに含めることをお勧めします。
{% endalert %}

<!---/users/delete-->

{% elsif include.endpoint == "users delete" %}
このエンドポイントには、1分あたり20,000リクエストの共有レート制限が適用されます。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/users/alias/new`、`/users/identify`、`/users/merge`、および `/users/alias/update` エンドポイントと共有されます。

<!---/users/alias/new-->

{% elsif include.endpoint == "users alias new" %}
このエンドポイントには、1分あたり20,000リクエストの共有レート制限が適用されます。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/users/delete`、`/users/identify`、`/users/merge`、および `/users/alias/update` エンドポイントと共有されます。

<!---/users/alias/update-->

{% elsif include.endpoint == "users alias update" %}
このエンドポイントには、1分あたり20,000リクエストの共有レート制限が適用されます。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/users/delete`、`/users/alias/new`、`/users/identify`、および `/users/merge` エンドポイントと共有されます。

<!---/users/identify-->

{% elsif include.endpoint == "users identify" %}
このエンドポイントには、1分あたり20,000リクエストの共有レート制限が適用されます。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/users/delete`、`/users/alias/new`、`/users/merge`、および `/users/alias/update` エンドポイントと共有されます。

<!---/users/merge-->

{% elsif include.endpoint == "users merge" %}
このエンドポイントには、1分あたり20,000リクエストの共有レート制限が適用されます。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/users/delete`、`/users/alias/new`、`/users/identify`、および `/users/alias/update` エンドポイントと共有されます。

<!---/custom_attributes-->

{% elsif include.endpoint == "custom_attributes" %}
このエンドポイントには、1時間あたり1,000リクエストの共有レート制限が適用されます。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/events`、`/events/list`、および `/purchases/product_list` エンドポイントと共有されます。

<!---/events-->

{% elsif include.endpoint == "events" %}
このエンドポイントには、1時間あたり1,000リクエストの共有レート制限が適用されます。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/custom_attributes`、`/events/list`、および `/purchases/product_list` エンドポイントと共有されます。

<!---/events/list-->

{% elsif include.endpoint == "events list" %}
このエンドポイントには、1時間あたり1,000リクエストの共有レート制限が適用されます。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/custom_attributes`、`/events`、および `/purchases/product_list` エンドポイントと共有されます。

<!---/purchases/product_list-->

{% elsif include.endpoint == "purchases product list" %}
このエンドポイントには、1時間あたり1,000リクエストの共有レート制限が適用されます。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/custom_attributes`、`/events`、および `/events/list` エンドポイントと共有されます。

<!---/messages/send-->
<!---/campaigns/trigger/send-->
<!---/canvas/trigger/send-->

{% elsif include.endpoint == "send endpoints" %}
リクエストで Connected Audience フィルターを使用する場合、このエンドポイントには1分あたり250リクエストのレート制限が適用されます。それ以外の場合、`external_id` を指定すると、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/messages/send`、`/campaigns/trigger/send`、および `/canvas/trigger/send` 間で共有される1時間あたり250,000リクエストのデフォルトのレート制限が適用されます。

Braze エンドポイントは API リクエストのバッチ処理をサポートしています。メッセージングエンドポイントへの単一のリクエストは、次のいずれかに到達できます。

- それぞれに個別のメッセージパラメーターを持つ、最大50個の特定の `external_ids`
- Connected Audience オブジェクトとしてリクエストで定義された、任意のサイズのオーディエンスセグメント

<!---/transactional/v1/campaigns/{campaign_id}/send -->

{% elsif include.endpoint == "transactional email" %}
`/transactional/v1/campaigns/{campaign_id}/send` エンドポイントは、1時間あたりの単位で課金される有料エンドポイントです（例：パッケージに応じて1時間あたり50,000）。エンドポイントごとの個別のレート制限はありません。割り当てられた量を超えて送信することは可能ですが、SLA でカバーされるのは割り当てられた量のみです。このエンドポイントへのリクエストは、[外部 API 全体のレート制限]({{site.baseurl}}/api/api_limits/)にカウントされます。その制限を超えると（例：すべてのエンドポイントで1時間あたり250,000リクエスト）、Braze は 429 を返し、リクエストはスロットルされます。トランザクション量のカウントは1時間ごとにリセットされるため、1時間後には新たな割り当てが利用可能になります。SLA でカバーされるボリューム内であれば、99.9% のメールは1分以内に送信されます。

<!---/sends/id/create-->

{% elsif include.endpoint == "sends id create" %}
このエンドポイントを使用して、指定されたワークスペースで1日あたり最大100個のカスタム送信識別子を作成できます。作成する各 `send_id` と `campaign_id` の組み合わせは、1日の制限にカウントされます。有効なリクエストの応答ヘッダーには、現在のレート制限ステータスが含まれます。詳細については、[API レート制限]({{site.baseurl}}/api/api_limits/)を参照してください。

<!---/subscription/status/set-->
{% elsif include.endpoint == "subscription status set" %}
このエンドポイントには、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/subscription/status/set` および `/v2/subscription/status/set` エンドポイント間で共有される1分あたり5,000リクエストのレート制限があります。

<!-- Add this phrase back ", as documented in [API rate limits]({{site.baseurl}}/api/api_limits/)" to CDI endpoints for GA -->

<!---GET /cdi/integrations--->
{% elsif include.endpoint == "cdi list integrations" %}
このエンドポイントには、1分あたり50リクエストのレート制限があります。

<!---POST /cdi/integrations/{integration_id}/sync--->
{% elsif include.endpoint == "cdi job sync" %}
このエンドポイントには、1分あたり20リクエストのレート制限があります。

<!---POST /cdi/integrations/{integration_id}/job_sync_status--->
{% elsif include.endpoint == "cdi job sync status" %}
このエンドポイントには、1分あたり100リクエストのレート制限があります。

{% endif %}

<!---Additional if statement for Messaging endpoints-->

{% if include.category == "message endpoints" %}

Braze エンドポイントは [API リクエストのバッチ処理]({{site.baseurl}}/api/api_limits/#batching-api-requests)をサポートしています。メッセージングエンドポイントへの単一のリクエストは、次のいずれかに到達できます。

- それぞれに個別のメッセージパラメーターを持つ、最大50個の特定の `external_ids`
- `segment_id` で指定される、Braze ダッシュボードで作成された任意のサイズのセグメント
- リクエストで [Connected Audience]({{site.baseurl}}/api/objects_filters/connected_audience/) オブジェクトとして定義された、任意のサイズのオーディエンスセグメント

{% endif %}

{% if include.category == "send messages endpoints" %}

Braze エンドポイントは [API リクエストのバッチ処理]({{site.baseurl}}/api/api_limits/#batching-api-requests)をサポートしています。メッセージングエンドポイントへの単一のリクエストは、次のいずれかに到達できます。

- それぞれに個別のメッセージパラメーターを持つ、最大50個の特定の `external_ids`
- リクエストで [Connected Audience]({{site.baseurl}}/api/objects_filters/connected_audience/) オブジェクトとして定義された、任意のサイズのオーディエンスセグメント

{% endif %}

<!---Additional if statement for Translation endpoints-->

{% if include.endpoint == "translation endpoints" %}

このエンドポイントには、1分あたり250,000リクエストのレート制限があります。

{% endif %}

<!---Additional if statement for /messages/send endpoint-->

{% if include.category == "message send endpoint" %}

Braze エンドポイントは [API リクエストのバッチ処理]({{site.baseurl}}/api/api_limits/#batching-api-requests)をサポートしています。メッセージングエンドポイントへの単一のリクエストは、次のいずれかに到達できます。

- 最大50個の特定の `external_ids`
- `segment_id` で指定される、Braze ダッシュボードで作成された任意のサイズのセグメント
- リクエストで [Connected Audience]({{site.baseurl}}/api/objects_filters/connected_audience/) オブジェクトとして定義された、任意のサイズのオーディエンスセグメント

{% endif %}

{% if include.endpoint == "asynchronous catalog item" %}

このエンドポイントには、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、すべての非同期カタログアイテムエンドポイント間で1分あたり16,000リクエストの共有レート制限があります。

{% endif %}

{% if include.endpoint == "synchronous catalog item" %}

このエンドポイントには、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、すべての同期カタログアイテムエンドポイント間で1分あたり50リクエストの共有レート制限があります。

{% endif %}

{% if include.endpoint == "synchronous catalog" %}

このエンドポイントには、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、すべての同期カタログエンドポイント間で1分あたり50リクエストの共有レート制限があります。

{% endif %}

{% if include.endpoint == "asynchronous catalog fields" or include.endpoint == "asynchronous catalog selections" %}

このエンドポイントには、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、すべての非同期カタログフィールドおよびセレクションエンドポイント間で1分あたり50リクエストの共有レート制限があります。

{% endif %}

{% if include.endpoint == "export campaign analytics" %}

このエンドポイントには、1分あたり50,000リクエストのレート制限があります。

{% endif %}