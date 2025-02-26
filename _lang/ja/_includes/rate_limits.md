
<!---DEFAULT RATE LIMIT-->

{% if include.endpoint == "default" %}
[API レート制限]({{site.baseurl}}/api/api_limits/)で説明されているように、このエンドポイントにはデフォルトの1時間あたり25万リクエストのBraze レート 制限が適用されます。

<!---PUT /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "ダッシュボードユーザーの更新" %}
このエンドポイントには、1日あたり1社あたり5000リクエストのレート制限があります。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/scim/v2/Users/` GET、DELETE、および POST エンドポイントと共有されます。

<!---GET /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "ダッシュボードユーザーを検索する" %}
このエンドポイントには、1日あたり1社あたり5000リクエストのレート制限があります。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/scim/v2/Users/` PUT、GET、DELETE、およびPOST エンドポイントと共有されます。

<!---DELETE /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "ダッシュボードーザーを消去する" %}
このエンドポイントには、1日あたり1社あたり5000リクエストのレート制限があります。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/scim/v2/Users/` PUT、GET、および POST エンドポイントと共有されます。

<!---POST /scim/v2/Users--->
{% elsif include.endpoint == "ダッシュボードユーザーを作成する" %}
このエンドポイントには、1日あたり1社あたり5000リクエストのレート制限があります。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/scim/v2/Users/` PUT、GET、および DELETE エンドポイントと共有されます。

<!---GET /scim/v2/Users--->
{% elsif include.endpoint == "ダッシュボードユーザーメールを調べる" %}
このエンドポイントには、1日あたり1社あたり5000リクエストのレート制限があります。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/scim/v2/Users/` PUT、GET、DELETE、およびPOST エンドポイントと共有されます。

<!---/users/external_id/rename-->
<!---/users/external_id/remove-->

{% elsif include.endpoint == "external ID 移行" %}
[API レート制限]({{site.baseurl}}/api/api_limits/)で説明されているように、このエンドポイントに1分あたり1000リクエストのレート制限を適用します。

<!---/users/track-->

{% elsif include.endpoint == "ユーザー追跡" %}
2024年10月28日から、すべての顧客に対して、このエンドポイントに3秒あたり3,000リクエストという基本速度制限を適用する。`/users/track` の各リクエストには、最大75個のイベントオブジェクト、75個の属性オブジェクト、75個の購買オブジェクトを含めることができます。それぞれのオブジェクト (イベント、属性、および購入配列) は、それぞれ1つのユーザーを更新できます。合計すると、1回の呼び出しで最大225人のユーザーを更新できることになります。さらに、単一のユーザープロファイルを複数のオブジェクトによって更新することもできます。

**月間アクティブユーザー数 - CY 24-25** を購入した顧客には異なる制限が適用されます。これらの制限の詳細については、[月間アクティブユーザー数 - CY 24-25 制限]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25)を参照してください。

詳しくは、[API レート制限]({{site.baseurl}}/api/api_limits/)のページを参照してください。制限を引き上げる必要がある場合は、カスタマーサクセスマネージャーに連絡してください。

<!---/users/export/ids-->

{% elsif include.endpoint == "ユーザーエクスポート ID" %}
2024年8月22日以降に Braze にオンボーディングした場合、このエンドポイントには、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、1分あたり250リクエストのレート制限が適用されます。

<!---/users/delete-->

{% elsif include.endpoint == "ユーザーの消去" %}
2021年9月16日以降に Braze にオンボーディングした顧客の場合、このエンドポイントには、1分あたり20,000リクエストの共有レート制限が適用されます。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/users/alias/new`、`/users/identify`、および `/users/merge` エンドポイントと共有されます。

<!---/users/alias/new-->

{% elsif include.endpoint == "users alias new" %}
2021年9月16日以降に Braze にオンボーディングした顧客の場合、このエンドポイントには、1分あたり20,000リクエストの共有レート制限が適用されます。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/users/delete`、`/users/identify`、`/users/merge`、および `/users/alias/update` エンドポイントと共有されます。

<!---/users/alias/update-->

{% elsif include.endpoint == "users alias update" %}
2021年9月16日以降に Braze にオンボーディングした顧客の場合、このエンドポイントには、1分あたり20,000リクエストの共有レート制限が適用されます。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/users/delete`、`/users/identify`、`/users/merge`、および `/users/alias/new` エンドポイントと共有されます。

<!---/users/alias/update-->

{% elsif include.endpoint == "users alias update" %}
2021年9月16日以降に Braze にオンボーディングした顧客の場合、このエンドポイントには、1分あたり20,000リクエストの共有レート制限が適用されます。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/users/delete`、`/users/identify`、および `/users/merge` エンドポイントと共有されます。

<!---/users/identify-->

{% elsif include.endpoint == "ユーザー ID" %}
2021年9月16日以降に Braze にオンボーディングした顧客の場合、このエンドポイントには、1分あたり20,000リクエストの共有レート制限が適用されます。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/users/delete`、`/users/alias/new`、`/users/merge`、および `/users/alias/update` エンドポイントと共有されます。

<!---/users/merge-->

{% elsif include.endpoint == "ユーザーのマージ" %}
2021年9月16日以降に Braze にオンボーディングした顧客の場合、このエンドポイントには、1分あたり20,000リクエストの共有レート制限が適用されます。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/users/delete`、`/users/alias/new`、`/users/identify`、および `/users/alias/update` エンドポイントと共有されます。

<!---/custom_attributes-->

{% elsif include.endpoint == "custom_属性" %}
2021年9月16日以降に Braze にオンボーディングした顧客の場合、このエンドポイントには、1時間あたり1,000リクエストの共有レート制限が適用されます。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/events`、`/events/list`、および `/purchases/product_list` エンドポイントと共有されます。

<!---/events-->

{% elsif include.endpoint == "イベント" %}
2021年9月16日以降に Braze にオンボーディングした顧客の場合、このエンドポイントには、1時間あたり1,000リクエストの共有レート制限が適用されます。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/custom_attributes`、`/events/list`、および `/purchases/product_list` エンドポイントと共有されます。

<!---/events/list-->

{% elsif include.endpoint == "イベントリスト" %}
2021年9月16日以降に Braze にオンボーディングした顧客の場合、このエンドポイントには、1時間あたり1,000リクエストの共有レート制限が適用されます。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/custom_attributes`、`/events`、および `/purchases/product_list` エンドポイントと共有されます。

<!---/purchases/product_list-->

{% elsif include.endpoint == "購入品リスト" %}
2021年9月16日以降に Braze にオンボーディングした顧客の場合、このエンドポイントには、1時間あたり1,000リクエストの共有レート制限が適用されます。このレート制限は、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/custom_attributes`、`/events`、および `/events/list` エンドポイントと共有されます。

<!---/messages/send-->
<!---/campaigns/trigger/send-->
<!---/canvas/trigger/send-->

{% elsif include.endpoint == "エンドポイントの送信" %}
リクエストでセグメントまたは接続済みのオーディエンスを指定する際、このエンドポイントには1分あたり250リクエストのレート制限が適用されます。それ以外の場合、`external_id` を指定すると、このエンドポイントは、[API レート制限]({{site.baseurl}}/api/api_limits/) に記載されているように、`/messages/send`、`/campaigns/trigger/send`、および `/canvas/trigger/send` 間で共有される1時間あたり250,000リクエストのデフォルトのレート制限が適用されます。

<!---/transactional/v1/campaigns/{campaign_id}/send -->

{% elsif include.endpoint == "トランザクションメール" %}
Braze トランザクションメールはレート制限の対象外です。選択したパッケージに応じて、1時間あたりに設定された数のトランザクションメールが SLA によってカバーされます。このレートを超えるリクエストは送信されますが、SLA ではカバーされません。メールの99.9%が1分以内に送信されます。

<!---/sends/id/create-->

{% elsif include.endpoint == "ID 作成を送信する" %}
このエンドポイントを使用して作成できるカスタム送信識別子の1日の最大数は、特定のワークスペースに対して100です。作成する各 `send_id` および `campaign_id` の組み合わせは、毎日の制限にカウントされます。有効なリクエストのレスポンスヘッダーには、現在のレート制限ステータスが含まれます。詳しくは、[API レート制限]({{site.baseurl}}/api/api_limits/)を参照してください。

<!---/subscription/status/set-->
{% elsif include.endpoint == "サブスクリプションステータスセット" %}
このエンドポイントには、[API レート制限]({{site.baseurl}}/api/api_limits/)に記載されているように、`/subscription/status/set` および `/v2/subscription/status/set` エンドポイントで共有される1分あたり5000リクエストのレート制限があります。

<!-- Add this phrase back ", as documented in [API rate limits]({{site.baseurl}}/api/api_limits/)" to CDI endpoints for GA -->

<!---GET /cdi/integrations--->
{% elsif include.endpoint == "cdi リストの統合" %}
このエンドポイントには、1分あたり、50リクエストのレート制限があります。

<!---POST /cdi/integrations/{integration_id}/sync--->
{% elsif include.endpoint == "cdi ジョブの同期" %}
このエンドポイントには、1分あたり、20リクエストのレート制限があります。

<!---POST /cdi/integrations/{integration_id}/job_sync_status--->
{% elsif include.endpoint == "cdi ジョブ同期ステータス" %}
このエンドポイントには、1分あたり、100リクエストというレート制限があります。

{% endif %}

<!---Additional if statement for Messaging endpoints-->

{% if include.category == "メッセージエンドポイント" %}

Braze エンドポイントは[API リクエストのバッチ処理]({{site.baseurl}}/api/api_limits/#batching-api-requests)をサポートしています。メッセージングエンドポイントへの単一のリクエストは、次のいずれかに到達できます。

- それぞれに個別のメッセージパラメーターを持つ、最大50個の特定の `external_ids`
- `segment_id` で指定される、Braze ダッシュボードで作成された任意のサイズのセグメント
- リクエストで[接続オーディエンス]({{site.baseurl}}/api/objects_filters/connected_audience/)オブジェクトとして定義されている、任意のサイズのオーディエンスセグメント

{% endif %}

<!---Additional if statement for /messages/send endpoint-->

{% if include.category == "メール送信エンドポイント" %}

Braze エンドポイントは[API リクエストのバッチ処理]({{site.baseurl}}/api/api_limits/#batching-api-requests)をサポートしています。メッセージングエンドポイントへの単一のリクエストは、次のいずれかに到達できます。

- 最大50個の特定の `external_ids`
- `segment_id` で指定される、Braze ダッシュボードで作成された任意のサイズのセグメント
- リクエストで[接続オーディエンス]({{site.baseurl}}/api/objects_filters/connected_audience/)オブジェクトとして定義されている、任意のサイズのオーディエンスセグメント

{% endif %}

{% if include.endpoint == "非同期カタログアイテム" %}

このエンドポイントは、[API レート制限]({{site.baseurl}}/api/api_limits/)で説明されているように、すべての非同期カタログアイテムエンドポイント間で1分あたり16,000リクエストの共有レート制限があります。

{% endif %}

{% if include.endpoint == "同期カタログアイテム" %}

このエンドポイントは、[API レート制限]({{site.baseurl}}/api/api_limits/)で説明されているように、すべての同期カタログアイテムエンドポイント間で毎分50リクエストの共有レート制限があります。

{% endif %}

{% if include.endpoint == "同期カタログ" %}

このエンドポイントは、[API レート制限]({{site.baseurl}}/api/api_limits/)で説明されているように、すべての同期カタログエンドポイント間で1分あたり50リクエストの共有レート制限があります。

{% endif %}

{% if include.endpoint == "非同期カタログフィールド" またはエンドポイントを含める == "非同期カタログ選択" %}

このエンドポイントは、[API レート制限]({{site.baseurl}}/api/api_limits/)で説明されているように、すべての非同期カタログフィールドとセレクションエンドポイント間で1分あたり50リクエストの共有レート制限があります。

{% endif %}

{% if include.endpoint == "キャンペーン分析のエクスポート" %}

このエンドポイントには、1分あたり、50,000リクエストというレート制限があります。

{% endif %}
