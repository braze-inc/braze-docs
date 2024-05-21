---
nav_title: "API の概要"
article_title: API の概要
page_order: 2.1
description: "このリファレンス記事では、REST API とは何か、用語、API キーの概要などのAPI の基本について説明します。"
page_type: reference
alias: /api/api_key/
---

# APIの概要

> このリファレンス記事では、一般的な用語やREST API キーの概要、権限、セキュリティ保護の方法など、API の基本について説明します。 

## API定義

以下に、Braze REST API のドキュメントに記載されている用語の概要を示します。

### エンドポイント

Braze は、ダッシュボードおよびREST エンドポイントのさまざまなインスタンスを管理します。アカウントがプロビジョニングされると、次のいずれかのURL にログインします。プロビジョニング先のインスタンスに基づいて、正しいREST エンドポイントを使用します。不明な場合は、[support ticket][support] を開くか、次の表を使用して、使用するダッシュボードのURL を正しいREST エンドポイントに一致させます。

{% alert important %}
API コールにエンドポイントを使用する場合は、REST エンドポイントを使用します。

SDK 統合では、REST エンドポイントではなく、[SDK エンドポイント]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) を使用します。
{% endalert %}

|インスタンス|URL|RESTエンドポイント|SDKエンドポイント|
|---|---|---|
|US-01| `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com` | `sdk.iad-01.braze.com` |
|US-02| `https://dashboard-02.braze.com` | `https://rest.iad-02.braze.com` | `sdk.iad-02.braze.com` |
|US-03| `https://dashboard-03.braze.com` | `https://rest.iad-03.braze.com` | `sdk.iad-03.braze.com` |
|US-04| `https://dashboard-04.braze.com` | `https://rest.iad-04.braze.com` | `sdk.iad-04.braze.com` |
|US-05| `https://dashboard-05.braze.com` | `https://rest.iad-05.braze.com` | `sdk.iad-05.braze.com` |
|US-06| `https://dashboard-06.braze.com` | `https://rest.iad-06.braze.com` | `sdk.iad-06.braze.com` |
|US-07| `https://dashboard-07.braze.com` | `https://rest.iad-07.braze.com` | `sdk.iad-07.braze.com` |
|US-08| `https://dashboard-08.braze.com` | `https://rest.iad-08.braze.com` | `sdk.iad-08.braze.com` |
|EU-01| `https://dashboard-01.braze.eu` | `https://rest.fra-01.braze.eu` | `sdk.fra-01.braze.eu` |
|EU-02| `https://dashboard-02.braze.eu` | `https://rest.fra-02.braze.eu` | `sdk.fra-02.braze.eu` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### APIの制限

ほとんどのAPI では、Braze のデフォルトのレート制限は1 時間あたり250,000 リクエストです。ただし、特定のリクエストタイプには、顧客ベース全体で大量のデータをより適切に処理するために適用されるレート制限があります。詳細は[APIレートリミット]({{site.baseurl}}/api/api_limits/)を参照してください。

### ユーザーID 

- **External user ID**:`external_id` は、データを送信する一意のユーザ識別子として機能します。この識別子は、同じユーザーに複数のプロファイルを作成しないように、Braze SDK で設定したものと同じにする必要があります。
- **Braze ユーザID**:`braze_id`は、Brazeによって設定される一意のユーザ識別子として機能します。この識別子は、external\_ids に加えてREST API を使用してユーザーを削除するために使用できます。

詳細については、プラットフォームに基づいて次の記事を参照してください。[iOS][9]、[Android][10]、および[Web][13]。

## REST API キー

REST Application Programming Interface キー(REST API キー) は、API 呼び出しを認証し、呼び出し元のアプリケーションまたはユーザーを識別するためにAPI に渡される一意のコードです。API アクセスは、会社のREST API エンドポイントへのHTTPS ウェブリクエストを使用して行われます。BrazeのREST APIキーは、アプリIDキーと連動して使用し、データの追跡、アクセス、送信、エクスポート、分析を行い、お客様と弊社の両方ですべてがスムーズに実行されるようにします。

ワークスペースとAPI キーは、Braze の手元にあります。ワークスペースは、複数のプラットフォームにまたがって同じアプリケーションのバージョンを格納するように設計されています。また、多くのお客様は、ワークスペースを使用して、同じプラットフォーム上にアプリケーションの無料およびプレミアムバージョンを格納します。気付くかもしれないが、これらのワークスペースはREST API も使用しており、独自のREST API キーを持っている。これらのキーに個別のスコープを設定すれば、API 上の特定のエンドポイントにアクセスできるようになります。API の呼び出しには必ず、エンドポイントへのアクセス権を持つキーを含める必要があります。

REST API キーとワークスペースAPI キーの両方を`api_key` と呼びます。`api_key` は、リクエストヘッダーとして各リクエストに含まれ、REST API を使用できる認証キーとして機能します。これらのREST API は、ユーザーの追跡、メッセージの送信、ユーザーデータのエクスポートなどに使用されます。新しいREST API キーを作成するときは、特定のエンドポイントにアクセスできるようにする必要があります。API キーに特定の権限を割り当てることで、API キーを呼び出すことで認証できるコールを厳密に制限できます。

![APIキーページのREST APIキーパネル][27]

{% alert tip %}
REST API キーに加えて、アプリ、テンプレート、キャンバス、キャンペーン、コンテンツカード、API のセグメントなど、特定のものを参照するために使用できるIdentifier キーと呼ばれるキーのタイプもあります。詳細については、[API Identifier types]({{site.baseurl}}/api/identifier_types/)を参照してください。
{% endalert %}

### REST API キー権限

API キーパーミッションは、特定のAPI コールへのアクセスを制限するためにユーザーまたはグループに割り当てることができるパーミッションです。API キー権限のリストを表示するには、**Settings** > **API Keys** に移動し、API キーを選択します。

{% tabs %}
{% tab User Data %}

| 権限| エンドポイント| 説明|
|---|---|---|
| `users.track` | [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) | Rユーザー属性、カスタムイベント、および購入を記録します。 |
| `users.delete` | [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) | ユーザーを削除します。 |
| `users.alias.new` | [`/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias/) |既存のユーザーの新しいエイリアスを作成します。 |
| `users.identify` | [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) |外部 ID を持つエイリアス専用ユーザーを識別します。 |
| `users.export.ids` | [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) |ユーザー ID を使用してユーザープロファイル情報を照会します。 |
| `users.export.segment` | [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) |セグメントを使用してユーザープロファイル情報を照会します。|
| `users.merge` | [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) | 既存ユーザー 2 人を双方向マージ |
| `users.external_ids.rename` | [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/) | 既存のユーザーの外部 ID を変更します。|
| `users.external_ids.remove` | [`/users/external_ids/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove/) | 既存のユーザーの external ID を削除します。 |
| `users.alias.update` | [`/users/alias/update`]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/) | 既存ユーザーのエイリアスを更新します。|
| `users.export.global_control_group` | [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/) | グローバルコントロールグループ内のユーザープロファイル情報を照会します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

 {% endtab %}
 {% tab Email %}

| 権限| エンドポイント| 説明|
|---|---|---|
| `email.unsubscribe` | [`/email/unsubscribes`]({{site.baseurl}}/api/endpoints/email/get_query_unsubscribed_email_addresses/) | 配信停止されたメールアドレスを照会します。  |
| `email.status` | [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/) | メールアドレスのステータスを変更します。 |
| `email.hard_bounces` | [`/email/hard_bounces`]({{site.baseurl}}/api/endpoints/email/get_list_hard_bounces/) | ハードバウンスされたメールアドレスを照会します。 |
| `email.bounce.remove` | [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces/) | ハードバウンスリストからメールアドレスを削除します。 |
| `email.spam.remove` | [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam/) | 迷惑メールリストからメールアドレスを削除します。|
| `email.blacklist` | [`/email/blacklist`]({{site.baseurl}}/api/endpoints/email/post_blacklist/) | ブロックリストの電子メールアドレス。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Messages %}

| 権限| エンドポイント| 説明|
|---|---|---|
| `messages.send` | [`/messages/send `]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) | 直接メッセージを特定のユーザに送信します。|
| `messages.schedule.create` | [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/) |メッセージを特定の時刻に送信するようにスケジュールします。 |
| `messages.schedule.update` | [`/messages/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/) | スケジュールされたメッセージを更新します。 |
| `messages.schedule.delete` | [`/messages/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/) | スケジュールされたメッセージを削除します。 |
| `messages.schedule_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/) | スケジュールされたブロードキャストメッセージをすべて照会します。 |
| `messages.live_activity.update` | [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update/) | iOS ライブアクティビティを更新 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Campaigns %}

| 権限| エンドポイント| 説明|
|---|---|---|
| `campaigns.trigger.send` | [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) |既存のキャンペーンの送信をトリガーします。|
| `campaigns.trigger.schedule.create` | [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/) | 今後のキャンペーン送信をAPI トリガ配信でスケジュールします。|
| `campaigns.trigger.schedule.update` | [`/campaigns/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/) | API トリガ配信でスケジュールされたキャンペーンを更新します。|
| `campaigns.trigger.schedule.delete` | [`/campaigns/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/) |API トリガ配信でスケジュールされたキャンペーンを削除します。|
| `campaigns.list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) | キャンペーンのリストのクエリ。|
| `campaigns.data_series` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) | 時間範囲にわたるキャンペーンアナリティクスのクエリ。|
| `campaigns.details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) | 特定のキャンペーンの詳細についてのクエリ。|
| `sends.data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) | 時間範囲にわたるメッセージ送信アナリティクスのクエリ。|
| `sends.id.create` | [`/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/) | メッセージブラストトラッキングの送信ID を作成します。|
| `campaigns.url_info.details` | [`/campaigns/url_info/details`]({{site.baseurl}}) | キャンペーン内の特定のメッセージバリエーションのURL 詳細のクエリ。|
| `transactional.send` | [`/transactional/v1/campaigns/{campaign_id}/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message/) | Transactional メッセージングエンドポイントを使用してトランザクションメッセージングを送信できるようにします。|
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Canvas %}

| 権限| エンドポイント| 説明|
|---|---|---|
| `canvas.trigger.send` | [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) | 既存のキャンバスの送信をトリガします。|
| `canvas.trigger.schedule.create` | [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/) | 今後のCanvas の送信を、API トリガによる配信でスケジュールします。|
| `canvas.trigger.schedule.update` | [`/canvas/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/) | API トリガー配信でスケジュールされたキャンバスを更新します。|
| `canvas.trigger.schedule.delete` | [`/canvas/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/)| API トリガ配信でスケジュールされたキャンバスを削除します。|
| `canvas.list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) | キャンバスのリストのクエリ。|
| `canvas.data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) | 時間範囲にわたるキャンバスアナリティクスのクエリ。|
| `canvas.details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) | 特定のキャンバスの詳細を問い合わせます。|
| `canvas.data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/) | 時間範囲にわたるCanvas アナリティクスのロールアップのクエリ。|
| `canvas.url_info.details` | [`/canvas/url_info/details`]({{site.baseurl}}/get_canvas_link_alias/) | キャンバスステップ内の特定のメッセージバリエーションのURL 詳細を取得するクエリ|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Segments %}

| 権限| エンドポイント| 説明|
|---|---|---|
| `segments.list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) | セグメントのリストのクエリ。|
| `segments.data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/) | 時間範囲にわたるセグメント分析のクエリ。|
| `segments.details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/) | 特定のセグメントの詳細を問い合わせます。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Purchases %}

| 権限| エンドポイント| 説明|
|---|---|---|
| `purchases.product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) | アプリで購入した製品のリストのクエリ。|
| `purchases.revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series/) | アプリ内で1 日に費やされた時間範囲の合計金額のクエリ。|
| `purchases.quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases/) | アプリ内の1 日あたりの購入総数の時間範囲内でのクエリ。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Events %}

| 権限| エンドポイント| 説明|
|---|---|---|
| `events.list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/) | カスタムイベントのリストのクエリ。|
| `events.data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/) | 時間範囲にわたるカスタムイベントの出現を照会します。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab News Feed %}

{% alert note %}
ニュースフィードは非推奨になります。Braze では、News Feed ツールを使用するお客様は、コンテンツカードメッセージングチャネルに移動することを推奨しています。このチャネルは、より柔軟でカスタマイズ可能で、信頼性が高いものです。詳細については、[マイグレーションガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)を参照してください。
{% endalert %}

| 権限| エンドポイント| 説明|
|---|---|---|
| `feed.list` | [`/feed/list`]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_cards/) | News Feed カードのリストを問い合わせます。|
| `feed.data_series` | [`/feed/data_series`]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_card_analytics/) | 時間範囲にわたるニュースフィード分析のクエリ。|
| `feed.details` | [`/feed/details`]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_card_details/) | 特定のニュースフィードの詳細を問い合わせます。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Sessions %}

| 権限| エンドポイント| 説明|
|---|---|---|
| `sessions.data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/) | 時間範囲にわたる1 日あたりのセッションのクエリ。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab KPIs %}

| 権限| エンドポイント| 説明|
|---|---|---|
| `kpi.dau.data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/) | 一日に一意のアクティブユーザーのクエリ。|
| `kpi.mau.data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/) | 時間範囲の30 日間のローリングウィンドウでの一意のアクティブユーザーの合計のクエリ。|
| `kpi.new_users.data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/) | 時間範囲の1 日あたりの新規ユーザーのクエリ。|
| `kpi.uninstalls.data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/) | 時間範囲にわたる1 日あたりのアプリのアンインストールのクエリ。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Templates %}

| 権限| エンドポイント| 説明|
|---|---|---|
| `templates.email.create` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/) | ダッシュボードに新しいメールテンプレートを作成します。|
| `templates.email.info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | 特定のテンプレートの情報を問い合わせます。|
| `templates.email.list` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) | メールテンプレートのリストのクエリ。|
| `templates.email.update` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/) | ダッシュボードに保存されているメールテンプレートを更新します。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab SSO %}

| 権限| 説明|
|---|---|---|
| `sso.saml.login` | ID プロバイダが開始するログインを設定します。詳細については、[サービスプロバイダー(SP)によって開始されたログイン]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/)を参照してください。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Content Blocks %}

| 権限| エンドポイント| 説明|
|---|---|---|
| `content_blocks.info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) | 特定のテンプレートの情報を問い合わせます。|
| `content_blocks.list` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) | コンテンツブロックのリストのクエリ。|
| `content_blocks.create` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/) | ダッシュボードに新しいコンテンツブロックを作成します。|
| `content_blocks.update` | [`/content_blocks_update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) | ダッシュボード上の既存のコンテンツブロックを更新します。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Preference Center %}

| 権限| エンドポイント| 説明|
|---|---|---|
| `preference_center.get` | [`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | 設定センターを取得します。|
| `preference_center.list` | [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/) | List preference centers. |
| `preference_center.update` | [`/preference_center/v1`]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center)<br><br>[`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/) | 環境設定センターを作成または更新します。|
| `preference_center.user.get` | [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center) | ユーザのプリファレンスセンターリンクを取得します。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Subscription %}

| 権限| エンドポイント| 説明|
|---|---|---|
| `subscription.status.set` | [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) | サブスクリプショングループのステータスを設定します。|
| `subscription.status.get` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) | サブスクリプショングループのステータスを取得します。|
| `subscription.groups.get` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) | 特定のユーザが明示的に購読および購読解除されている購読グループのステータスを取得します。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab SMS %}

| 権限| エンドポイント| 説明|
|---|---|---|
| `sms.invalid_phone_numbers` | [`/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers/) | 不正な電話番号の問い合わせ|
| `sms.invalid_phone_numbers.remove` | [`/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers/) | 無効な電話番号フラグをユーザから削除します。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Catalogs %}

| 権限| エンドポイント| 説明|
|---|---|---|
| `catalogs.add_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/) | 既存のカタログに複数のアイテムを追加します。|
| `catalogs.update_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/) | 既存のカタログ内の複数のアイテムを更新します。|
| `catalogs.delete_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk) | 既存のカタログから複数のアイテムを削除します。|
| `catalogs.get_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/) | 既存のカタログから単一のアイテムを取得します。|
| `catalogs.update_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/) | 既存のカタログ内の単一のアイテムを更新します。|
| `catalogs.create_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/) | 既存のカタログに単一のアイテムを作成します。|
| `catalogs.delete_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/) | 既存のカタログから単一のアイテムを削除します。|
| `catalogs.replace_item` | [` /catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/) | 既存のカタログから1つのアイテムを置き換えます。|
| `catalogs.create` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/) | カタログの作成。|
| `catalogs.get` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) | カタログのリストを取得する|
| `catalogs.delete` | [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/) | カタログの削除。|
| `catalogs.get_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/) | 既存のカタログからアイテムのプレビューを取得します。|
| `catalogs.replace_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/) | 既存のカタログ内のアイテムを置き換えます。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% endtabs %}

## REST API キーの作成

新しいREST API キーを作成するには

1. **Settings** > **API Keys** に移動します。このページには、既存のAPI キーが表示されます。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation) を使用している場合は、**Developer Console**> **API Settings** からAPI キーを作成できます。
{% endalert %}

{:start="2"}
2\.**\+ Create New API Key**をクリックします。
3\.新しいキーに一目で識別用の名前を付けます。
4\.新しいキーに関連付ける[権限](#rest-api-key-permissions)を選択します。
5\.新しいキーの[allowlisted IP addresses](#api-ip-allowlisting) とサブネットを指定します。

{% alert important %}
新しいAPI キーを作成した後は、権限のスコープや許可されたIP を編集できないことに注意してください。この制限は、セキュリティ上の理由から設けられています。キーのスコープを変更する必要がある場合は、更新された権限を持つ新しいキーを作成し、古いキーの代わりにそのキーを実装します。実装が完了したら、古いキーを削除します。
{% endalert %}

## REST API キーの管理

REST API キーは、作成後に編集できませんが、**API Keys** ページから既存のREST API キーの詳細を表示または削除できます。**Rest API Keys**リストには、各キーの以下の情報が一覧表示されます。

| フィールド| 説明|
| ------------ | :------------------------------------------------------------------------------------------------------------------ |
| API キー名| 作成時にキーに付けられた名前。|
| 識別子| API キー。|
| 作成者| キーを作成したユーザのメールアドレス。このフィールドは"N と表示されます/A" for keys created before June 2023. |
| Date Created | The date this key was created.                                                                                      |
| Last Seen    | The date this key was last used. This field will show as "N/A" for keys that have never been used.                  |
{: .reset-td-br-1 .reset-td-br-2}

特定のキーの詳細を表示するには、リストからキーを選択します。次に、このキーにあるすべての権限、ホワイトリストに登録されたIP(ある場合)、およびこのキーがBraze IP ホワイトリストに選択されているかどうかを確認できます。

![][30]

キーを削除するには、<i class="fas fa-gear" alt="Settings"></i>をクリックし、対応するオプションを選択します。

![][29]

## REST API キーセキュリティ

API キーは、API 呼び出しを認証するために使用されます。新しい REST API キーを作成するときには、特定のエンドポイントへのアクセス権をキーに付与する必要があります。API キーに特定の権限を割り当てることで、API キーを呼び出すことで認証できるコールを厳密に制限できます。

REST API キーを使用すると、機密性が高い可能性のあるREST API エンドポイントへのアクセスが許可されるため、これらのキーを保護し、信頼できるパートナーとのみ共有します。ただしこれらのキーは一般公開しないでください。たとえば、このキーを使用してウェブサイトからAJAX コールを発信したり、他のパブリックな方法で公開したりしないでください。

優れたセキュリティプラクティスは、ジョブを完了するために必要なだけのアクセス権をユーザーに割り当てることです。この原則は、各キーに権限を割り当てることによってAPI キーにも適用できます。これらの権限により、アカウントのさまざまな領域に対するセキュリティとコントロールが向上します。 

![API キーの作成時に使用可能なAPI キー権限][25]

{% alert warning %}
REST API キーを使用すると、機密性が高い可能性のあるREST API エンドポイントへのアクセスが許可されるため、それらが安全に保存され、使用されていることを確認します。たとえば、このキーを使用してウェブサイトからAJAX コールを発信したり、他のパブリックな方法で公開したりしないでください。
{% endalert %}

キーの誤露出が発生した場合は、Developer Console から削除できます。このプロセスのヘルプを表示するには、[サポートチケット] [サポート] を開きます。

### API IP の許可リスト化

さらなるセキュリティ強化のため、特定の REST API キーに対して REST API 要求が許可されている IP アドレスやサブネットのリストを指定できます。これを許可リスト化またはホワイトリスト化と呼びます。特定の IP アドレスやサブネットを許可するには、新規の REST API キーを作成する際に [**ホワイトリスト IP (Whitelist IP)**] のセクションにこれらを追加します。 

![API キーの作成時にIP をホワイトリストに登録するオプション][26]

特に指定しない場合は、すべての IP アドレスから要求を送信できます。

{% alert tip %}
Braze 間の Webhook を行う際に許可リストを使用する場合は、[ホワイトリスト化が必要な IP]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-whitelisting)のリストをご確認ください。
{% endalert %}

## 追加リソース

### Rubyクライアントライブラリ

Ruby を使用してBrazeを実装している場合は、[Ruby クライアントライブラリ](https://github.com/braze-inc/braze-api-client-ruby) を使用してデータのインポート時間を短縮できます。クライアントライブラリは、1 つのプログラミング言語に固有のコードのコレクションです。この場合、Ruby は、API を使いやすくします。

Ruby クライアントライブラリは、[User Endpoints]({{site.baseurl}}/api/endpoints/user_data) をサポートします。

{% alert note %}
このクライアントライブラリは現在ベータ版です。私たちがこの図書館をもっと良くするのを手伝ってあげたいですか？[smb-product@braze.com](mailto:smb-product@braze.com)にご意見をお寄せください。
{% endalert %}

[1]: https://en.wikipedia.org/wiki/UTF-8
[7]: {{site.baseurl}}/api/objects_filters/connected_audience/
[9]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/
[2]: {{site.baseurl}}/api/identifier_types/
[5]: {{site.baseurl}}/api/basics/
[6]: https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro
[25]: {% image_buster /assets/img_archive/api-key-permissions.png %}
[26]: {% image_buster /assets/img_archive/api-key-ip-whitelisting.png %}
[support]: {{site.baseurl}}/braze_support/
[28]: {% image_buster /assets/img_archive/create-new-key.png %}
[29]: {% image_buster /assets/img_archive/api-key-options.png %}
[27]: {% image_buster /assets/img_archive/rest-api-key.png %}
[30]: {% image_buster /assets/img_archive/view-api-key.png %}
