<!---DEFAULT RATE LIMIT-->

{% if include.endpoint == "default" %}
[API レート制限]({{site.baseurl}}/api/api_limits/)で説明されているように、このエンドポイントにはデフォルトの1時間あたり25万リクエストのBraze レート 制限が適用されます。

<!---PUT /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "update dashboard user" %}
このエンドポイントには、1日あたり1社あたり5000リクエストのレート制限があります。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/scim/v2/Users/` GET、DELETE、および POST エンドポイントと共有されます。

<!---GET /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "look up dashboard user" %}
このエンドポイントには、1日あたり1社あたり5000リクエストのレート制限があります。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/scim/v2/Users/` PUT、GET、DELETE、およびPOST エンドポイントと共有されます。

<!---DELETE /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "delete dashboard user" %}
このエンドポイントには、1日あたり1社あたり5000リクエストのレート制限があります。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/scim/v2/Users/` PUT、GET、および POST エンドポイントと共有されます。

<!---POST /scim/v2/Users--->
{% elsif include.endpoint == "create dashboard user" %}
このエンドポイントには、1日あたり1社あたり5000リクエストのレート制限があります。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/scim/v2/Users/` PUT、GET、および DELETE エンドポイントと共有されます。

<!---GET /scim/v2/Users--->
{% elsif include.endpoint == "look up dashboard user email" %}
このエンドポイントには、1日あたり1社あたり5000リクエストのレート制限があります。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/scim/v2/Users/` PUT、GET、DELETE、およびPOST エンドポイントと共有されます。

<!---/users/external_id/rename-->
<!---/users/external_id/remove-->

{% elsif include.endpoint == "external id migration" %}
[API レート制限]({{site.baseurl}}/api/api_limits/)で説明されているように、このエンドポイントに1分あたり1000リクエストのレート制限を適用します。

<!---/users/track-->

{% elsif include.endpoint == "users track" %}
2024年10月28日から、すべての顧客に対して、このエンドポイントに3秒あたり3,000リクエストという基本速度制限を適用する。`/users/track` の各リクエストには、最大 75 個のイベントオブジェクト、75 個の属性オブジェクト、75 個の購買オブジェクトを含めることができます。各オブジェクト（イベント、アトリビュート、購入アレイ）は、それぞれ1人のユーザーを更新することができる。合計すると、1回の通話で最大225人のユーザーを更新できることになる。さらに、1つのユーザープロファイルを複数のオブジェクトで更新することもできる。

**月間アクティブユーザー数 - CY 24-25** を購入した顧客には異なる制限が適用されます。これらの制限の詳細については、[月間アクティブユーザー数 - CY 24-25 制限]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25)を参照してください。

詳細については、[APIレート制限の]({{site.baseurl}}/api/api_limits/)ページを参照のこと。また、制限の引き上げが必要な場合は、カスタマー・サクセス・マネージャーに連絡すること。

<!---/users/export/ids-->

{% elsif include.endpoint == "users export ids" %}
2024年8月22日以降に Braze にオンボーディングした場合、このエンドポイントには、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、1分あたり250リクエストのレート制限が適用されます。

また、以下の条件を満たすことで、このエンドポイントのレート制限を毎秒40リクエストに増やすこともできる：

- ワークスペースでは、デフォルトのレート制限（250リクエスト/分）が有効になっている。既存のレート制限の解除については、Brazeアカウントマネージャーにお問い合わせください。
- リクエストには、受け取りたいすべてのフィールドをリストアップするための`fields_to_export` パラメータが含まれている。

{% alert important %}
`fields_to_export` パラメータに`canvases_received` または`campaigns_received` を含めると、リクエストは高速レート制限の対象外となる。具体的なユースケースがある場合のみ、リクエストに含めることをお勧めする。
{% endalert %}

<!---/users/delete-->

{% elsif include.endpoint == "users delete" %}
このエンドポイントには、毎分20,000リクエストの共有レート制限を適用する。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/users/alias/new`、`/users/identify`、`/users/merge`、および `/users/alias/update` エンドポイントと共有されます。

<!---/users/alias/new-->

{% elsif include.endpoint == "users alias new" %}
このエンドポイントには、毎分20,000リクエストの共有レート制限を適用する。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/users/delete`、`/users/identify`、`/users/merge`、および `/users/alias/update` エンドポイントと共有されます。

<!---/users/alias/update-->

{% elsif include.endpoint == "users alias update" %}
このエンドポイントには、毎分20,000リクエストの共有レート制限を適用する。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/users/delete`、`/users/alias/new`、`/users/identify`、および `/users/merge` エンドポイントと共有されます。

<!---/users/identify-->

{% elsif include.endpoint == "users identify" %}
このエンドポイントには、毎分20,000リクエストの共有レート制限を適用する。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/users/delete`、`/users/alias/new`、`/users/merge`、および `/users/alias/update` エンドポイントと共有されます。

<!---/users/merge-->

{% elsif include.endpoint == "users merge" %}
このエンドポイントには、毎分20,000リクエストの共有レート制限を適用する。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/users/delete`、`/users/alias/new`、`/users/identify`、および `/users/alias/update` エンドポイントと共有されます。

<!---/custom_attributes-->

{% elsif include.endpoint == "custom_attributes" %}
このエンドポイントには、1時間あたり1,000リクエストの共有レート制限を適用する。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/events`、`/events/list`、および `/purchases/product_list` エンドポイントと共有されます。

<!---/events-->

{% elsif include.endpoint == "events" %}
このエンドポイントには、1時間あたり1,000リクエストの共有レート制限を適用する。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/custom_attributes`、`/events/list`、および `/purchases/product_list` エンドポイントと共有されます。

<!---/events/list-->

{% elsif include.endpoint == "events list" %}
このエンドポイントには、1時間あたり1,000リクエストの共有レート制限を適用する。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/custom_attributes`、`/events`、および `/purchases/product_list` エンドポイントと共有されます。

<!---/purchases/product_list-->

{% elsif include.endpoint == "purchases product list" %}
このエンドポイントには、1時間あたり1,000リクエストの共有レート制限を適用する。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/custom_attributes`、`/events`、および `/events/list` エンドポイントと共有されます。

<!---/messages/send-->
<!---/campaigns/trigger/send-->
<!---/canvas/trigger/send-->

{% elsif include.endpoint == "send endpoints" %}
リクエストでセグメントまたは接続済みのオーディエンスを指定する際、このエンドポイントには1分あたり250リクエストのレート制限が適用されます。それ以外の場合、`external_id` を指定すると、このエンドポイントは、[API レート制限]({{site.baseurl}}/api/api_limits/) に記載されているように、`/messages/send`、`/campaigns/trigger/send`、および `/canvas/trigger/send` 間で共有される1時間あたり250,000リクエストのデフォルトのレート制限が適用されます。

<!---/transactional/v1/campaigns/{campaign_id}/send -->

{% elsif include.endpoint == "transactional email" %}
Braze トランザクションメールはレート制限の対象外です。選択したパッケージに応じて、1時間あたりに設定された数のトランザクションメールが SLA によってカバーされます。このレートを超えるリクエストは送信されますが、SLA ではカバーされません。メールの99.9%が1分以内に送信されます。

<!---/sends/id/create-->

{% elsif include.endpoint == "sends id create" %}
このエンドポイントを使用して、与えられたワークスペースで1日に100個までカスタム送信識別子を作成できる。作成する各 `send_id` および `campaign_id` の組み合わせは、毎日の制限にカウントされます。有効なリクエストのレスポンスヘッダーには、現在のレート制限ステータスが 含まれる。詳細は[APIレート制限を]({{site.baseurl}}/api/api_limits/)参照のこと。

<!---/subscription/status/set-->
{% elsif include.endpoint == "subscription status set" %}
このエンドポイントには、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/subscription/status/set` および `/v2/subscription/status/set` エンドポイントで共有される1分あたり5000リクエストのレート制限があります。

<!-- Add this phrase back ", as documented in [API rate limits]({{site.baseurl}}/api/api_limits/)" to CDI endpoints for GA -->

<!---GET /cdi/integrations--->
{% elsif include.endpoint == "cdi list integrations" %}
このエンドポイントには、1分あたり、50リクエストのレート制限があります。

<!---POST /cdi/integrations/{integration_id}/sync--->
{% elsif include.endpoint == "cdi job sync" %}
このエンドポイントには、1分あたり、20リクエストのレート制限があります。

<!---POST /cdi/integrations/{integration_id}/job_sync_status--->
{% elsif include.endpoint == "cdi job sync status" %}
このエンドポイントには、1分あたり、100リクエストというレート制限があります。

{% endif %}

<!---Additional if statement for Messaging endpoints-->

{% if include.category == "message endpoints" %}

Braze エンドポイントは[API リクエストのバッチ処理]({{site.baseurl}}/api/api_limits/#batching-api-requests)をサポートしています。メッセージングエンドポイントへの単一のリクエストは、次のいずれかに到達できます。

- それぞれに個別のメッセージパラメーターを持つ、最大50個の特定の `external_ids`
- `segment_id` で指定される、Braze ダッシュボードで作成された任意のサイズのセグメント
- リクエストで[接続オーディエンス]({{site.baseurl}}/api/objects_filters/connected_audience/)オブジェクトとして定義されている、任意のサイズのオーディエンスセグメント

{% endif %}

{% if include.category == "send messages endpoints" %}

Braze エンドポイントは[API リクエストのバッチ処理]({{site.baseurl}}/api/api_limits/#batching-api-requests)をサポートしています。メッセージングエンドポイントへの単一のリクエストは、次のいずれかに到達できます。

- それぞれに個別のメッセージパラメーターを持つ、最大 50 個の特定の `external_ids`
- リクエストで[接続オーディエンス]({{site.baseurl}}/api/objects_filters/connected_audience/)オブジェクトとして定義されている、任意のサイズのオーディエンスセグメント

{% endif %}

<!---Additional if statement for Translation endpoints-->

{% if include.endpoint == "translation endpoints" %}

このエンドポイントには、1分あたり、50,000リクエストというレート制限があります。

{% endif %}

<!---Additional if statement for /messages/send endpoint-->

{% if include.category == "message send endpoint" %}

Braze エンドポイントは[API リクエストのバッチ処理]({{site.baseurl}}/api/api_limits/#batching-api-requests)をサポートしています。メッセージングエンドポイントへの単一のリクエストは、次のいずれかに到達できます。

- 最大50個の特定の `external_ids`
- `segment_id` で指定される、Braze ダッシュボードで作成された任意のサイズのセグメント
- リクエストで[接続オーディエンス]({{site.baseurl}}/api/objects_filters/connected_audience/)オブジェクトとして定義されている、任意のサイズのオーディエンスセグメント

{% endif %}

{% if include.endpoint == "asynchronous catalog item" %}

このエンドポイントは、[API レート制限]({{site.baseurl}}/api/api_limits/)で説明されているように、すべての非同期カタログアイテムエンドポイント間で1分あたり16,000リクエストの共有レート制限があります。

{% endif %}

{% if include.endpoint == "synchronous catalog item" %}

このエンドポイントは、[API レート制限]({{site.baseurl}}/api/api_limits/)で説明されているように、すべての同期カタログアイテムエンドポイント間で毎分50リクエストの共有レート制限があります。

{% endif %}

{% if include.endpoint == "synchronous catalog" %}

このエンドポイントは、[API レート制限]({{site.baseurl}}/api/api_limits/)で説明されているように、すべての同期カタログエンドポイント間で1分あたり50リクエストの共有レート制限があります。

{% endif %}

{% if include.endpoint == "asynchronous catalog fields" or include.endpoint == "asynchronous catalog selections" %}

このエンドポイントは、[API レート制限]({{site.baseurl}}/api/api_limits/)で説明されているように、すべての非同期カタログフィールドとセレクションエンドポイント間で1分あたり50リクエストの共有レート制限があります。

{% endif %}

{% if include.endpoint == "export campaign analytics" %}

このエンドポイントには、1分あたり、50,000リクエストというレート制限があります。

{% endif %}

