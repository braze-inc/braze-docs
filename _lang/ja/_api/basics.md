---
nav_title: "APIの概要"
article_title: API の概要
page_order: 2.1
description: "このリファレンス記事では、REST API とは何か、用語、API キーの概要など、API の基本について説明します。"
page_type: reference
alias: /api/api_key/
---

# APIの概要

> このリファレンス記事では、一般的な用語、REST API キーや権限の概要、それらを安全に保つ方法など、API の基本について説明します。

## Braze REST APIコレクション

| コレクション                                                                 | 目的                                                                               |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [カタログ]({{site.baseurl}}/api/endpoints/catalogs/)                       | Brazeのキャンペーンで参照するカタログやカタログアイテムを作成、管理します。    |
| [クラウドデータ取り込み]({{site.baseurl}}/api/endpoints/cdi/)                | データウェアハウスの統合と同期を管理します。                                    |
| [メールリストとアドレス]({{site.baseurl}}/api/endpoints/email/)         | Brazeとお使いのメールシステム間の双方向同期を設定・管理します。           |
| [エクスポート]({{site.baseurl}}/api/endpoints/export/)                           | キャンペーン、キャンバス、KPI などのさまざまな詳細にアクセスし、エクスポートします。        |
| [メディアライブラリ]({{site.baseurl}}/api/endpoints/media_library/)             | Braze内でアセットを管理します。                                                           |
| [メッセージ]({{site.baseurl}}/api/endpoints/messaging/)                      | キャンペーンとキャンバスのスケジュールの設定、送信、管理を行います。                               |
| [ユーザー設定センター]({{site.baseurl}}/api/endpoints/preference_center/)     | ユーザー設定センターを構築し、そのスタイルを更新します。                            |
| [SCIM]({{site.baseurl}}/api/endpoints/scim/)                               | クラウドベースのアプリケーションやサービスにおけるユーザーIDを管理します。                      |
| [SMS]({{site.baseurl}}/api/endpoints/sms/)                                 | サブスクリプショングループでユーザーの電話番号を管理します。                         |
| [サブスクリプショングループ]({{site.baseurl}}/api/endpoints/subscription_groups/) | Brazeダッシュボードに保存されているSMSとメールのサブスクリプショングループをリストアップし、更新します。 |
| [テンプレート]({{site.baseurl}}/api/endpoints/templates/)                     | メールメッセージやコンテンツブロックのテンプレートを作成し、更新します。                   |
| [ユーザーデータ]({{site.baseurl}}/api/endpoints/user_data/)                     | ユーザーを特定し、追跡し、管理します。                                               |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## API定義

Braze REST API のドキュメントで使用される用語の概要を次に示します。

### エンドポイント

Brazeは、ダッシュボードとRESTエンドポイント用のさまざまなインスタンスを管理しています。アカウントがプロビジョニングされたら、以下のいずれかのURLにログインします。どのインスタンスにプロビジョニングされるかに基づいて、正しいRESTエンドポイントを使用してください。不明な場合は、[サポートチケット]({{site.baseurl}}/braze_support/)を開くか、以下の表を使用して、使用するダッシュボードの URL と正しい REST エンドポイントを照合してください。

BrazeでRESTエンドポイントを見つけるには：

1. Brazeにログインし、**設定** > **APIと識別子** > **APIキー**に移動します。
2. 既存のAPIキーを選択するか、**APIキーを作成**を選択して新しいキーを作成します。
3. このタブに表示されているRESTエンドポイントをコピーし、APIリクエストにそのエンドポイントを使用します。

{% alert important %}
API呼び出しにエンドポイントを使用する場合は、RESTエンドポイントを使用してください。

SDK統合には、RESTエンドポイントではなく[SDKエンドポイント]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/)を使用してください。
{% endalert %}

{% multi_lang_include data_centers.md datacenters='instances' %}

### API制限

ほとんどのAPIについて、Brazeはデフォルトで1時間あたり250,000リクエストというレート制限を設けています。ただし、特定のリクエストタイプには独自のレート制限が適用されます。これにより、顧客ベース全体での大量データ処理を適切に管理できます。詳細は[APIレート制限]({{site.baseurl}}/api/api_limits/)を参照してください。

### ユーザー ID

- **External user ID**：`external_id` は、データの送信対象となる一意のユーザー識別子として機能します。この識別子は、同じユーザーに複数のプロファイルが作成されるのを避けるため、Braze SDK で設定したものと同じでなければなりません。
- **BrazeユーザーID**：`braze_id` はBrazeが設定する一意のユーザー識別子として機能します。この識別子を使って、external_idsに加えてREST APIを通じてユーザーを削除できます。

詳細については、[iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/)、[Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/)、[Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/)の各プラットフォームに応じた以下の記事を参照してください。

## REST APIキーについて

RESTアプリケーションAPIキー（REST APIキー）とは、API呼び出しを認証し、呼び出し元となるアプリケーションやユーザーを識別するためにAPIに渡す一意のコードです。貴社のREST APIエンドポイントに対してHTTPSウェブリクエストを送信することで、APIにアクセスします。REST APIキーは、App Identifierキーと連携してデータのトラッキング、アクセス、送信、エクスポート、分析を行い、すべてが円滑に動作していることを保証するのに役立ちます。

ワークスペースとAPIキーはBrazeでは密接な関係にあります。ワークスペースは、複数のプラットフォームにまたがる同じアプリケーションのバージョンを収容するように設計されています。また、多くの顧客はワークスペースを使用して、無料版とプレミアム版のアプリケーションを同じプラットフォーム上に格納しています。お気づきかもしれませんが、これらのワークスペースもREST APIを利用しており、独自のREST APIキーが存在します。これらのキーは、API上の特定のエンドポイントへのアクセスを含むように、個別にスコープすることができます。APIの各呼び出しには、対象エンドポイントへのアクセス権を持つキーを含める必要があります。

REST APIキーとワークスペースAPIキーの両方を`api_key`と呼びます。`api_key`はリクエストヘッダーとして各リクエストに含まれ、REST APIを使用するための認証キーとして機能します。これらのREST APIは、ユーザーの追跡、メッセージの送信、ユーザーデータのエクスポートなどに使用されます。新しいREST APIキーを作成する際には、特定のエンドポイントへのアクセス権を付与する必要があります。APIキーに特定の権限を割り当てることで、APIキーが認証できる呼び出しを厳密に制限できます。

![APIキータブにあるREST APIキーのパネル。]({% image_buster /assets/img_archive/rest-api-key.png %})

{% alert tip %}
REST APIキーに加えて、識別子キーと呼ばれるタイプのキーも存在し、APIからアプリ、テンプレート、キャンバス、キャンペーン、コンテンツカード、セグメントといった特定のものを参照するために使用できます。詳細については、「[API識別子のタイプ]({{site.baseurl}}/api/identifier_types/)」を参照してください。
{% endalert %}

### REST APIキーを作成する

新しいREST APIキーを作成するには：

1. **設定** > **APIと識別子**に移動します。
2. **APIキーを作成**を選択します。
3. 一目で識別できるように、新しいキーに名前をつけます。
4. 新しいキーに対して[許可リストに登録するIPアドレス](#api-ip-allowlisting)とサブネットを指定します。
5. 新しいキーに関連付ける[権限](#rest-api-key-permissions)を選択します。

{% alert important %}
新しいAPIキーを作成した後は、権限の範囲や許可リストに登録済みのIPを編集できないことに留意してください。この制限はセキュリティ上の理由から設けられています。キーのスコープを変更する必要がある場合は、更新された権限を持つ新しいキーを作成し、古いキーの代わりにそのキーを実装してください。実装が完了したら、古いキーを削除できます。
{% endalert %}

### REST APIキーの権限

APIキーの権限は、特定のAPI呼び出しへのアクセスを制限するために、ユーザーまたはグループに割り当てることができる権限です。APIキーの権限のリストを表示するには、**設定** > **APIと識別子**と進み、APIキーを選択します。

{% tabs %}
{% tab User Data %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `users.track` | [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) | ユーザー属性、カスタムイベント、購入を記録します。 |
| `users.delete` | [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) | 任意のユーザーを削除します。 |
| `users.alias.new` | [`/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias/) |既存のユーザーのエイリアスを新規作成します。 |
| `users.identify` | [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) |external IDを使用してエイリアスのみのユーザーを特定します。 |
| `users.export.ids` | [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) |ユーザーIDでユーザープロファイル情報を照会します。 |
| `users.export.segment` | [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) |セグメント別のユーザープロファイル情報を照会します。 |
| `users.merge` | [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) | 既存の2人のユーザーを互いにマージします。 |
| `users.external_ids.rename` | [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/) | 既存のユーザーのexternal IDを変更します。 |
| `users.external_ids.remove` | [`/users/external_ids/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove/) | 既存のユーザーのexternal IDを削除します。 |
| `users.alias.update` | [`/users/alias/update`]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/) | 既存のユーザーのエイリアスを更新します。 |
| `users.export.global_control_group` | [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/) | グローバルコントロールグループのユーザープロファイル情報を照会します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

 {% endtab %}
 {% tab Email %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `email.unsubscribe` | [`/email/unsubscribes`]({{site.baseurl}}/api/endpoints/email/get_query_unsubscribed_email_addresses/) | 配信停止になっているメールアドレスを照会します。  |
| `email.status` | [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/) | メールアドレスのステータスを変更します。 |
| `email.hard_bounces` | [`/email/hard_bounces`]({{site.baseurl}}/api/endpoints/email/get_list_hard_bounces/) | ハードバウンスされたメールアドレスを照会します。 |
| `email.bounce.remove` | [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces/) | ハードバウンスリストからメールアドレスを削除します。 |
| `email.spam.remove` | [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam/) | スパムリストからメールアドレスを削除します。 |
| `email.blacklist` | [`/email/blacklist`]({{site.baseurl}}/api/endpoints/email/post_blacklist/) | メールアドレスをブロックリストに登録します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Messages %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `messages.send` | [`/messages/send `]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) | 特定のユーザーに即座にメッセージを送信します。 |
| `messages.schedule.create` | [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/) | 特定の時間にメッセージを送信するようスケジュールします。 |
| `messages.schedule.update` | [`/messages/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/) | スケジュールされたメッセージを更新します。 |
| `messages.schedule.delete` | [`/messages/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/) | スケジュールされたメッセージを削除します。 |
| `messages.schedule_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/) | スケジュールされたすべてのブロードキャストメッセージを照会します。 |
| `messages.live_activity.update` | [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update/) | iOSのライブアクティビティを更新します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Campaigns %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `campaigns.trigger.send` | [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) | 既存のキャンペーンの送信をトリガーします。 |
| `campaigns.trigger.schedule.create` | [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/) | APIトリガーによる配信でキャンペーンの送信をスケジュールします。 |
| `campaigns.trigger.schedule.update` | [`/campaigns/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/) | APIトリガー配信でスケジュールされたキャンペーンを更新します。 |
| `campaigns.trigger.schedule.delete` | [`/campaigns/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/) |APIトリガー配信でスケジュールされたキャンペーンを削除します。 |
| `campaigns.list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) | キャンペーンの一覧を照会します。 |
| `campaigns.data_series` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) | 時間範囲のキャンペーン分析を照会します。 |
| `campaigns.details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) | 特定のキャンペーンの詳細を照会します。 |
| `sends.data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) | 特定の期間のメッセージ送信分析を照会します。 |
| `sends.id.create` | [`/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/) | メッセージブラストトラッキング用の送信IDを作成します。 |
| `campaigns.url_info.details` | [`/campaigns/url_info/details`]({{site.baseurl}}) | キャンペーン内の特定のメッセージバリエーションのURL詳細を照会します。 |
| `transactional.send` | [`/transactional/v1/campaigns/{campaign_id}/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message/) | トランザクションメッセージングエンドポイントを使用してトランザクションメッセージを送信できるようにします。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Canvas %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `canvas.trigger.send` | [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) | 既存のキャンバスの送信をトリガーします。 |
| `canvas.trigger.schedule.create` | [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/) | APIトリガーによる配信でキャンバスの送信をスケジュールします。 |
| `canvas.trigger.schedule.update` | [`/canvas/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/) | APIトリガー配信でスケジュールされたキャンバスを更新します。 |
| `canvas.trigger.schedule.delete` | [`/canvas/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/)| APIトリガー配信でスケジュールされたキャンバスを削除します。 |
| `canvas.list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) |  キャンバスのリストを照会します。 |
| `canvas.data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) | 特定の期間のキャンバス分析を照会します。 |
| `canvas.details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) | 特定のキャンバスの詳細を照会します。 |
| `canvas.data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/) | 特定の期間のキャンバス分析のロールアップを照会します。 |
| `canvas.url_info.details` | [`/canvas/url_info/details`]({{site.baseurl}}/get_canvas_link_alias/) | キャンバスステップ内の特定のメッセージバリエーションのURL詳細を照会します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Segments %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `segments.list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) | セグメントのリストを照会します。 |
| `segments.data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/) | 時間範囲のセグメント分析を照会します。 |
| `segments.details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/) | 特定のセグメントの詳細を照会します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Purchases %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `purchases.product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) | アプリで購入された製品のリストを照会します。 |
| `purchases.revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series/) | 時間範囲にわたって、アプリで1日あたりに使われた金額の合計を照会します。 |
| `purchases.quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases/) | 特定の期間内の、1日あたりのアプリ内購入数の合計を照会します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Events %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `events.list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/) | カスタムイベントのリストを照会します。 |
| `events.data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/) | 時間範囲にわたるカスタムイベントの発生を照会します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Sessions %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `sessions.data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/) | 時間範囲内の1日あたりのセッション数を照会します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab KPIs %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `kpi.dau.data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/) |  特定の期間内の、1日あたりのユニークアクティブユーザー数を照会します。 |
| `kpi.mau.data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/) | 特定の期間内の、30日間ローリングウィンドウでのユニークアクティブユーザー数の合計を照会します。 |
| `kpi.new_users.data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/) | 特定の期間内の、1日あたりの新規ユーザー数を照会します。 |
| `kpi.uninstalls.data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/) | 時間範囲における1日あたりのアプリのアンインストール数を照会します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Templates %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `templates.email.create` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/) | ダッシュボードで新しいメールテンプレートを作成します。 |
| `templates.email.info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | 特定のテンプレートの情報を照会します。 |
| `templates.email.list` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) | メールテンプレートのリストを照会します。 |
| `templates.email.update` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/) | ダッシュボードに保存されているメールテンプレートを更新します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab SSO %}

| 権限 | 説明 |
|---|---|---|
| `sso.saml.login` | IDプロバイダーが開始するログインをセットアップします。詳細については、[サービスプロバイダー（SP）が開始するログイン]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Content Blocks %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `content_blocks.info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) | 特定のテンプレートの情報を照会します。 |
| `content_blocks.list` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) | コンテンツブロックのリストを照会します。 |
| `content_blocks.create` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/) | ダッシュボードに新しいコンテンツブロックを作成します。 |
| `content_blocks.update` | [`/content_blocks_update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) | ダッシュボード上の既存のコンテンツブロックを更新します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Preference Center %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `preference_center.get` | [`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | ユーザー設定センターを取得します。 |
| `preference_center.list` | [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/) | ユーザー設定センターをリストアップします。 |
| `preference_center.update` | [`/preference_center/v1`]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center)<br><br>[`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/) | ユーザー設定センターを作成または更新します。 |
| `preference_center.user.get` | [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center) | ユーザー用のユーザー設定センターリンクを取得します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Subscription %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `subscription.status.set` | [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) | サブスクリプショングループのステータスを設定します。 |
| `subscription.status.get` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) | サブスクリプショングループのステータスを取得します。 |
| `subscription.groups.get` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) | 特定のユーザーが明示的に購読中および配信停止しているサブスクリプショングループのステータスを取得します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab SMS %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `sms.invalid_phone_numbers` | [`/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers/) | 無効な電話番号を照会します。 |
| `sms.invalid_phone_numbers.remove` | [`/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers/) | ユーザーから無効な電話番号フラグを削除します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Catalogs %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `catalogs.add_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/) | 既存のカタログに複数のアイテムを追加します。 |
| `catalogs.update_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/) | 既存のカタログの複数のアイテムを更新します。 |
| `catalogs.delete_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk) | 既存のカタログから複数のアイテムを削除します。 |
| `catalogs.get_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/) | 既存のカタログから単一のアイテムを取得します。 |
| `catalogs.update_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/) | 既存のカタログの単一アイテムを更新します。 |
| `catalogs.create_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/) | 既存のカタログに単一のアイテムを作成します。 |
| `catalogs.delete_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/) | 既存のカタログから単一のアイテムを削除します。 |
| `catalogs.replace_item` | [` /catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/) | 既存のカタログの単一のアイテムを置き換えます。 |
| `catalogs.create` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/) | カタログを作成します。 |
| `catalogs.get` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) | カタログのリストを取得します。 |
| `catalogs.delete` | [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/) | カタログを削除します。 |
| `catalogs.get_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/) | 既存のカタログからアイテムのプレビューを取得します。 |
| `catalogs.replace_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/) | 既存のカタログのアイテムを置き換えます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab SDK Authentication %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `sdk_authentication.create` | [`/app_group/sdk_authentication/create`]({{site.baseurl}}/api/endpoints/sdk_authentication/post_create_sdk_authentication_key) | アプリ用に新しいSDK認証キーを作成します。 |
| `sdk_authentication.primary` | [`/app_group/sdk_authentication/primary`]({{site.baseurl}}/api/endpoints/sdk_authentication/put_primary_sdk_authentication_key/) | SDK認証キーをアプリのプライマリキーとしてマークします。 |
| `sdk_authentication.delete` | [`/app_group/sdk_authentication/delete`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key) | アプリのSDK認証キーを削除します。 |
| `sdk_authentication.keys` | [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | アプリのすべてのSDK認証キーを取得します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% endtabs %}

### REST APIキーを管理する

**設定** > **APIと識別子** > **APIキー**タブから、既存のREST APIキーの詳細を表示したり、削除したりできます。REST APIキーは作成後に編集できないことに注意してください。

**APIキー**タブには、各キーについて以下の情報が含まれています：

| フィールド        | 説明                                                                                                         |
| ------------ | :------------------------------------------------------------------------------------------------------------------ |
| APIキー名 | 作成時にキーにつけられた名前。                                                                            |
| 識別子   | APIキー。                                                                                                        |
| 作成者   | キーを作成したユーザーのメールアドレス。このフィールドは、2023年6月以前に作成されたキーに対して「N/A」と表示されます。 |
| 作成日 | このキーが作成された日付。                                                                                      |
| 最終使用日    | このキーが最後に使用された日付。このフィールドは、一度も使用されたことのないキーに対して「N/A」と表示されます。                  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

APIキーの詳細を表示するには、キーにカーソルを合わせて<i class="fa-solid fa-eye" alt="View"></i> **表示**を選択します。これには、このキーが持つすべての権限、ホワイトリストに登録されているIP（もしあれば）、このキーがBraze IPホワイトリストにオプトインしているかどうかが含まれます。

![Brazeダッシュボードの APIキー権限のリスト。]({% image_buster /assets/img_archive/view-api-key.png %})

[ユーザーを削除する]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/)際、Brazeはそのユーザーが作成した関連するAPIキーを削除しないことに注意してください。キーを削除するには、キーにカーソルを合わせて<i class="fa-solid fa-trash-can" alt="Delete"></i> **削除**を選択します。

![ゴミ箱のアイコンが強調表示され、「削除」を示す「Last Seen」というAPIキー。]({% image_buster /assets/img_archive/api-key-options.png %}){: style="max-width:30%;"}

### REST APIキーのセキュリティ

APIキーは、API呼び出しを認証するために使用されます。新しいREST APIキーを作成するときには、特定のエンドポイントへのアクセス権をキーに付与する必要があります。APIキーに特定の権限を割り当てることで、APIキーが認証できる呼び出しを厳密に制限できます。

REST APIキーによって潜在的に機密性の高いREST APIエンドポイントへのアクセスが許可されるため、これらのキーを安全に保管し、信頼できるパートナーとのみ共有してください。これらのキーは一般公開しないでください。例えば、このキーを使ってWeb サイトからAJAX呼び出しを行ったり、その他の公開的な方法で公開してはいけません。

適切なセキュリティプラクティスは、業務を完了するために必要なアクセス権のみをユーザーに割り当てることです。この原則は、各キーに権限を割り当てることによってAPIキーにも適用できます。これらの権限により、セキュリティが向上し、アカウントのさまざまな領域をコントロールできます。

{% alert warning %}
REST APIキーは、潜在的にセンシティブなREST APIエンドポイントへのアクセスを可能にするものであることを考慮し、安全に保管・使用されていることを確認してください。例えば、このキーを使ってWeb サイトからAJAX呼び出しを行ったり、その他の公開的な方法で公開してはいけません。
{% endalert %}

キーを誤って公開してしまった場合、開発者コンソールから削除できます。このプロセスに関するヘルプについては、[サポートチケット]({{site.baseurl}}/braze_support/)を開いてください。

### REST APIキーとSDK APIキーのセキュリティ

REST APIキーとSDK APIキーは、セキュリティプロファイルが異なります。

| | REST APIキー | SDK APIキー |
|---|---|---|
| 目的 | REST APIのサーバーサイド認証（メッセージの送信、データのエクスポート、ユーザーの管理） | Braze SDKのクライアントサイド識別（データの取り込み、アプリ内メッセージ、コンテンツカード） |
| 可視性 | **非公開にする必要があります**。クライアントサイドのコード、公開リポジトリ、またはユーザーアプリケーションに公開してはいけません。 | 公開されることを前提に設計されています。アプリのバイナリにバンドルされるか、WebブラウザのJavaScriptで表示されます。Google AnalyticsのトラッキングIDと同様です。 |
| 公開された場合の対処 | 直ちにキーを無効化し、**設定** > **APIと識別子** > **APIキー**で代替キーを作成してください。公開されたREST APIキーは、メッセージの送信、ユーザーデータのエクスポート、またはアカウント設定の変更に使用される可能性があります。 | 対処は不要です。SDK APIキーはデータの取り込みとクライアントサイドのメッセージング（アプリ内メッセージやコンテンツカードなど）の取得のみが可能です。ユーザーデータのエクスポート、代理でのメッセージ送信、キャンペーンの変更はできません。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### API IPの許可リスト

セキュリティをさらに強化するため、特定のREST APIキーに対してREST APIリクエストを実行できるIPアドレスやサブネットのリストを指定できます。これは、許可リストまたはホワイトリストと呼ばれます。特定のIPアドレスやサブネットを許可するには、新しいREST APIキーを作成する際に、**Whitelist IPs**セクションに追加します：

![APIキーの作成時にIPを許可リストに登録するオプション。]({% image_buster /assets/img_archive/api-key-ip-whitelisting.png %})

何も指定しない場合、すべてのIPアドレスからリクエストを送信できます。

{% alert tip %}
Braze to Braze Webhookを作成し、許可リストを使用する場合は、[ホワイトリストに登録するIP]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-whitelisting)アドレスのリストを参照してください。
{% endalert %}

## API認証とセキュリティ

### ベアラートークン認証

Brazeは、`Authorization`リクエストヘッダーにベアラートークンとして渡されたREST APIキーを使用して、REST APIリクエストを認証します。リクエストを送信する際は、APIキーを次の形式で含めてください：

```bash
Authorization: Bearer YOUR_REST_API_KEY
```

各リクエストに対して、Brazeは以下のサーバーサイド検証チェックを実行します：

1. **トークンの有効性：**REST APIキーがBrazeに存在し、有効であることを確認します（例えば、失効または無効化されていない状態であること）。
2. **トークンの認可：**APIキーが要求されたエンドポイントに必要な権限を持っていることを確認します。

認証が失敗した場合、APIはHTTPステータスコード付きのエラー応答を返します。例えば、`401 Unauthorized`はキーが無効または欠落していることを示し、`403 Forbidden`はキーが要求されたエンドポイントに対する権限を持っていないことを示します。詳細については、[APIエラー]({{site.baseurl}}/api/errors/)を参照してください。

### ネットワークレベルのセキュリティ

BrazeへのREST APIリクエストは、リクエストパス全体でトランスポート層セキュリティ（TLS）暗号化によって保護されています。以下の表は、お客様のサーバーからBrazeへのAPIリクエストのネットワークフローを説明するものです：

| ステップ | コンポーネント | 説明 |
| --- | --- | --- |
| 1 | お客様のサーバー | TLS暗号化を用いたHTTPSリクエストを開始します。 |
| 2 | Cloudflare | クライアントのTLS接続を終端し、ネットワークレベルの保護を適用します。 |
| 3 | ネットワークロードバランサー（NLB） | パケットをアプリケーションインフラに転送します。NLBはレイヤー4で動作するため、レイヤー7のプロキシングは行われません。パケットはHTTPレベルの検査や変更なしに転送されます。 |
| 4 | NGINXイングレス | 内部のTLS接続を終端し、リクエストをルーティングします。 |
| 5 | Unicorn（アプリケーションサーバー） | 認証されたリクエストを処理します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

TLS暗号化は、チェーンのすべてのリンクをカバーします。お客様のサーバーはTLS経由でCloudflareに接続し、CloudflareはNLBを介してNGINXイングレスへ別のTLS接続を確立するため、APIキーとリクエストデータは転送中に暗号化されたままとなります。

## その他のリソース

### Rubyクライアントライブラリー

RubyでBrazeを実装する場合、[Rubyクライアントライブラリー](https://github.com/braze-inc/braze-api-client-ruby)を使用すればデータインポート時間を短縮できます。クライアントライブラリーとは、あるプログラミング言語（この場合はRuby）に特化したコードの集まりで、APIを使いやすくするものです。

Rubyクライアントライブラリーは、[ユーザーエンドポイント]({{site.baseurl}}/api/endpoints/user_data)をサポートしています。

{% alert important %}
このクライアントライブラリーはベータ版です。このライブラリーをより良くするために、フィードバックを[smb-product@braze.com](mailto:smb-product@braze.com)宛にお送りください。
{% endalert %}