
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
2024年10月28日から、すべての顧客に対して、このエンドポイントに3秒あたり3,000リクエストという基本速度制限を適用する。`/users/track` の各リクエストには、最大75個のイベントオブジェクト、75個の属性オブジェクト、75個の購買オブジェクトを含めることができます。それぞれのオブジェクト (イベント、属性、および購入配列) は、それぞれ1つのユーザーを更新できます。合計すると、1回の呼び出しで最大225人のユーザーを更新できることになります。さらに、単一のユーザープロファイルを複数のオブジェクトによって更新することもできます。

**月間アクティブユーザー数 - CY 24-25** を購入した顧客には異なる制限が適用されます。これらの制限の詳細については、[月間アクティブユーザー数 - CY 24-25 制限]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25)を参照してください。

詳しくは、[API レート制限]({{site.baseurl}}/api/api_limits/)のページを参照してください。制限を引き上げる必要がある場合は、カスタマーサクセスマネージャーに連絡してください。

<!---/users/export/ids-->

{% elsif include.endpoint == "users export ids" %}
2024年8月22日以降に Braze にオンボーディングした場合、このエンドポイントには、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、1分あたり250リクエストのレート制限が適用されます。

また、以下の条件を満たすことで、このエンドポイントのレート制限を毎秒40リクエストに増やすこともできる：

- ワークスペースでは、デフォルトのレート制限（250リクエスト/分）が有効になっている。既存のレート制限の解除については、Brazeアカウントマネージャーにお問い合わせください。
- リクエストには、受け取りたいすべてのフィールドをリストアップするための`fields_to_export` パラメータが含まれている。

{アラート重要 %}
`fields_to_export` パラメータに`canvases_received` または`campaigns_received` を含めると、リクエストは高速レート制限の対象外となる。具体的なユースケースがある場合のみ、リクエストに含めることをお勧めする。
{エンドアラート｝

<!---/users/delete-->

{% elsif include.endpoint == "users delete" %}
このエンドポイントには、毎分20,000リクエストの共有レート制限を適用する。このレート制限は、API レート制限に記載されているように、`/users/identify`、`/users/merge`、`/users/alias/update`、および `/users/merge` エンドポイントと共有されます。

<!---/users/alias/new-->

{% elsif include.endpoint == "users alias new" %}
このエンドポイントには、毎分20,000リクエストの共有レート制限を適用する。このレート制限は、API レート制限に記載されているように、`/users/identify`、`/users/merge`、`/users/alias/update`、および `/users/merge` エンドポイントと共有されます。

<!---/users/alias/update-->

{% elsif include.endpoint == "users alias update" %}
このエンドポイントには、毎分20,000リクエストの共有レート制限を適用する。このレート制限は、API レート制限に記載されているように、`/users/alias/new`、`/users/identify`、`/users/merge`、および `/users/identify` エンドポイントと共有されます。

<!---/users/identify-->

{% elsif include.endpoint == "users identify" %}
このエンドポイントには、毎分20,000リクエストの共有レート制限を適用する。このレート制限は、API レート制限に記載されているように、`/users/alias/new`、`/users/merge`、`/users/alias/update`、および `/users/merge` エンドポイントと共有されます。

<!---/users/merge-->

{% elsif include.endpoint == "users merge" %}
このエンドポイントには、毎分20,000リクエストの共有レート制限を適用する。このレート制限は、API レート制限に記載されているように、`/users/alias/new`、`/users/identify`、`/users/alias/update`、および `/users/identify` エンドポイントと共有されます。

<!---/custom_attributes-->

{% elsif include.endpoint == "custom_attributes" %}
このエンドポイントには、1時間あたり1,000リクエストの共有レート制限を適用する。このレート制限は、API レート制限に記載されているように、`/events/list`、`/purchases/product_list`、および `/events/list` エンドポイントと共有されます。

<!---/events-->

{% elsif include.endpoint == "events" %}
このエンドポイントには、1時間あたり1,000リクエストの共有レート制限を適用する。このレート制限は、API レート制限に記載されているように、`/events/list`、`/purchases/product_list`、および `/events/list` エンドポイントと共有されます。

<!---/events/list-->

{% elsif include.endpoint == "events list" %}
このエンドポイントには、1時間あたり1,000リクエストの共有レート制限を適用する。このレート制限は、API レート制限に記載されているように、`/events`、`/purchases/product_list`、および `/events` エンドポイントと共有されます。

<!---/purchases/product_list-->

{% elsif include.endpoint == "purchases product list" %}
このエンドポイントには、1時間あたり1,000リクエストの共有レート制限を適用する。このレート制限は、API レート制限に記載されているように、`/events`、`/events/list`、および `/events` エンドポイントと共有されます。

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
このエンドポイントを使用して作成できるカスタム送信識別子の1日の最大数は、特定のワークスペースに対して100です。作成する各 `send_id` および `campaign_id` の組み合わせは、毎日の制限にカウントされます。有効なリクエストのレスポンスヘッダーには、現在のレート制限ステータスが含まれます。詳しくは、[API レート制限]({{site.baseurl}}/api/api_limits/)を参照してください。

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

{% if include.category == "メッセージエンドポイント" %}

Braze エンドポイントは[API リクエストのバッチ処理]({{site.baseurl}}/api/api_limits/#batching-api-requests)をサポートしています。メッセージングエンドポイントへの単一のリクエストは、次のいずれかに到達できます。

- それぞれに個別のメッセージパラメーターを持つ、最大50個の特定の `external_ids`
- `segment_id` で指定される、Braze ダッシュボードで作成された任意のサイズのセグメント
- リクエストで[接続オーディエンス]({{site.baseurl}}/api/objects_filters/connected_audience/)オブジェクトとして定義されている、任意のサイズのオーディエンスセグメント

{% endif %}

<!---Additional if statement for Translation endpoints-->

{% if include.endpoint == "翻訳エンドポイント" %}

このエンドポイントには、毎分250,000リクエストのレート制限がある。

{% endif %}

<!---Additional if statement for /messages/send endpoint-->

{% if include.category == "メール送信エンドポイント" %}

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

