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
| [カタログ]({{site.baseurl}}/api/endpoints/catalogs/)                       | Brazeのキャンペーンで参照するカタログやカタログ項目を作成、管理します。    |
| [クラウドデータ取り込み]({{site.baseurl}}/api/endpoints/cdi/)                | データウェアハウスの統合と同期を管理します。                                    |
| [メールリストとアドレス]({{site.baseurl}}/api/endpoints/email/)         | Brazeとお使いのメールシステム間の双方向同期を設定・管理。           |
| [エクスポート]({{site.baseurl}}/api/endpoints/export/)                           | キャンペーン、キャンバス、KPI などの様々な詳細にアクセスし、エクスポートします。        |
| [メッセージ]({{site.baseurl}}/api/endpoints/messaging/)                      | キャンペーンとキャンバスのスケジュールの設定、送信、管理を行います。                               |
| [ユーザー設定センター]({{site.baseurl}}/api/endpoints/preference_center/)     | ユーザー設定センターを構築し、そのスタイルを更新します。                            |
| [SCIM]({{site.baseurl}}/api/endpoints/scim/)                               | クラウドベースのアプリケーションやサービスにおけるユーザーIDを管理します。                      |
| [SMS]({{site.baseurl}}/api/endpoints/sms/)                                 | サブスクリプショングループでユーザーの電話番号を管理します。                         |
| [サブスクリプショングループ]({{site.baseurl}}/api/endpoints/subscription_groups/) | Brazeダッシュボードに保存されているSMSとEメールの購読グループをリストアップし、更新します。 |
| [テンプレート]({{site.baseurl}}/api/endpoints/templates/)                     | メールメッセージやコンテンツブロックのテンプレートを作成し、更新します。                   |
| [ユーザーデータ]({{site.baseurl}}/api/endpoints/user_data/)                     | ユーザーを特定し、追跡し、管理します。                                               |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## API定義

Braze REST API のドキュメントで使用される用語の概要を次に示します。

### エンドポイント

Brazeは、ダッシュボードとRESTエンドポイント用のさまざまなインスタンスを管理しています。アカウントのプロビジョニングが完了したら、以下のURLのいずれかにログインします。どのインスタンスにプロビジョニングされるかに基づいて、正しいRESTエンドポイントを使用します。不明な場合は、[サポートチケット]({{site.baseurl}}/braze_support/)を開くか、以下の表を使用して、使用するダッシュボードの URL と正しい REST エンドポイントを照合してください。

{% alert important %}
API呼び出しにエンドポイントを使用する場合は、RESTエンドポイントを使用します。

SDK 統合には、REST エンドポイントではなく [SDKエンドポイント]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/)を使用します。
{% endalert %}

{% multi_lang_include data_centers.md datacenters='instances' %}

### API制限

ほとんどのAPIについて、Brazeはデフォルトで1時間あたり250,000リクエストというレート制限を設けています。しかし、特定のリクエストタイプには、当社の顧客ベース全体で大量のデータをよりよく処理するために、独自のレート制限が適用されます。詳細は[API レート制限を]({{site.baseurl}}/api/api_limits/)参照してください。

### ユーザー ID

- **External user ID**:`external_id` は、データの送信対象となる一意のユーザー識別子として機能します。この識別子は、同じユーザーに複数のプロファイルが作成されるのを避けるため、Braze SDK で設定したものと同じでなければなりません。
- **BrazeユーザーID**：`braze_id` Brazeが設定する固有のユーザー識別子となる。この識別子を使用して、REST APIを通じてユーザーを削除することができる。 external_ids.

詳細については、[iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/)、[Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/)、[Webの]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/)各プラットフォームに応じた以下の記事を参照してください。

## REST APIキーについて

REST API キー（REST API key）とは、API 呼び出しを認証し、呼び出し元のアプリケーションまたはユーザーを識別子として識別するために API に渡す一意のコードである。自社のREST APIエンドポイントへのHTTPS Webリクエストを使ってAPIにアクセスする。Brazeでは、REST APIキーをApp Identifierキーと組み合わせて使用し、データの追跡、アクセス、送信、エクスポート、分析を行い、お客様とBrazeの両エンドですべてがスムーズに進むようサポートする。

ワークスペースとAPIキーはBrazeでは密接な関係にあります。ワークスペースは、複数のプラットフォームにまたがる同じアプリケーションのバージョンを収容するように設計されている。また、多くの顧客はワークスペースを使用して、無料版とプレミアム版のアプリケーションを同じプラットフォーム上に格納しています。お気づきかもしれませんが、これらのワークスペースも REST API を利用しており、独自の REST API キーが存在します。これらのキーは、API上の特定のエンドポイントへのアクセスを含むように、個別にスコープすることができます。API の各呼び出しには、エンドポイントヒットへのアクセス権を持つキーを含める必要があります。

REST API キーとワークスペース API キーの両方を`api_key` と呼びます。`api_key` はリクエストヘッダーとして各リクエストに含まれ、REST API を使用するための認証キーとして機能します。これらの REST API は、ユーザーの追跡、メッセージの送信、ユーザーデータのエクスポートなどに使用されます。新しい REST API キーを作成する際には、そのキーに特定のエンドポイントへのアクセス権を与える必要があります。API キーに特定の権限を割り当てることで、API キーが認証できる呼び出しを厳密に制限できます。

![API キータブにある REST API キーのパネル。]({% image_buster /assets/img_archive/rest-api-key.png %})

{% alert tip %}
REST API キーに加えて、識別子キーと呼ばれるタイプのキーも存在し、API からアプリ、テンプレート、キャンバス、キャンペーン、コンテンツカード、セグメントといった特定のものを参照するために使用できます。詳細については、「[API 識別子のタイプ]({{site.baseurl}}/api/identifier_types/)」を参照してください。
{% endalert %}

### REST APIキーを作成する

新しいREST APIキーを作成する：

1. [**設定**] ＞ [**API と識別子**] に進みます。
2. [**API キーを作成**] を選択します。
3. 一目で識別できるように、新しいキーに名前をつけてください。
4. 新しいキーに対して[許可リストに登録済みの IPアドレス](#api-ip-allowlisting)とサブネットを指定します。
5. 新しいキーに関連付ける[権限](#rest-api-key-permissions)を選択します。

{% alert important %}
新しい API キーを作成した後は、権限の範囲や許可リストに登録済みの IP を編集できないことに留意してください。この制限はセキュリティ上の理由から設けられています。キーのスコープを変更する必要がある場合は、更新されたパーミッションを持つ新しいキーを作成し、古いキーの代わりにそのキーを実装する。実装が完了したら、古いキーを削除できます。
{% endalert %}

### REST APIキーのパーミッション

APIキーのパーミッションは、特定のAPIコールへのアクセスを制限するために、ユーザーまたはグループに割り当てることができるパーミッションである。API キーのパーミッションのリストを表示するには、[**設定**] > [**API および識別子**] と進み、API キーを選択します。

{% tabs %}
{% tab User Data %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `users.track` | [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) | ユーザー属性、カスタムイベント、購入を記録します。 |
| `users.delete` | [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) | 任意のユーザーを削除します。 |
| `users.alias.new` | [`/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias/) |既存のユーザーのエイリアスを新規作成します。 |
| `users.identify` | [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) |外部IDを持つエイリアスのみのユーザーを特定します。 |
| `users.export.ids` | [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) |ユーザー ID でユーザープロファイル情報を照会します。 |
| `users.export.segment` | [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) |セグメント別のユーザープロファイル情報を照会します。 |
| `users.merge` | [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) | 既存の2人のユーザーを互いにマージします。 |
| `users.external_ids.rename` | [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/) | 既存のユーザーの外部IDを変更します。 |
| `users.external_ids.remove` | [`/users/external_ids/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove/) | 既存のユーザーの外部IDを削除します。 |
| `users.alias.update` | [`/users/alias/update`]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/) | 既存のユーザーのエイリアスを更新します。 |
| `users.export.global_control_group` | [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/) | グローバルコントロールグループのユーザープロファイル情報を照会します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

 {% endtab %}
 {% tab Email %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `email.unsubscribe` | [`/email/unsubscribes`]({{site.baseurl}}/api/endpoints/email/get_query_unsubscribed_email_addresses/) | 配信停止になっているメールアドレスを照会します。  |
| `email.status` | [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/) | メールアドレスのステータスを変更します。 |
| `email.hard_bounces` | [`/email/hard_bounces`]({{site.baseurl}}/api/endpoints/email/get_list_hard_bounces/) | ハードバウンスされたメールアドレスを照会します。 |
| `email.bounce.remove` | [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces/) | ハードバウンスリストからメールアドレスを削除します。 |
| `email.spam.remove` | [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam/) | スパムリストからメールアドレスを削除します。 |
| `email.blacklist` | [`/email/blacklist`]({{site.baseurl}}/api/endpoints/email/post_blacklist/) | ブロックリストのメールアドレス。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Messages %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `messages.send` | [`/messages/send `]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) | 特定のユーザーに即座にメッセージを送ります。 |
| `messages.schedule.create` | [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/) | 特定の時間にメッセージを送信するようスケジュールします。 |
| `messages.schedule.update` | [`/messages/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/) | スケジュールされたメッセージを更新します。 |
| `messages.schedule.delete` | [`/messages/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/) | スケジュールされたメッセージを削除します。 |
| `messages.schedule_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/) | スケジュールされたすべてのブロードキャストメッセージを問い合わせます。 |
| `messages.live_activity.update` | [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update/) | iOSのライブアクティビティを更新します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Campaigns %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `campaigns.trigger.send` | [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) | 既存のキャンペーンの送信をトリガーします。 |
| `campaigns.trigger.schedule.create` | [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/) | API トリガー配信でキャンペーンの将来の送信をスケジュールします。 |
| `campaigns.trigger.schedule.update` | [`/campaigns/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/) | APIトリガー配信でスケジュールされたキャンペーンを更新します。 |
| `campaigns.trigger.schedule.delete` | [`/campaigns/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/) |APIトリガー配信でスケジュールされたキャンペーンを削除します。 |
| `campaigns.list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) | キャンペーンの一覧を問い合わせます。 |
| `campaigns.data_series` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) | 時間範囲のキャンペーン分析を照会します。 |
| `campaigns.details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) | 特定のキャンペーンの詳細を問い合わせます。 |
| `sends.data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) | 特定の期間のメッセージ送信分析を照会します。 |
| `sends.id.create` | [`/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/) | メッセージブラスト追跡用の送信IDを作成します。 |
| `campaigns.url_info.details` | [`/campaigns/url_info/details`]({{site.baseurl}}) | キャンペーン内の特定のメッセージバリエーションのURL詳細を問い合わせます。 |
| `transactional.send` | [`/transactional/v1/campaigns/{campaign_id}/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message/) | トランザクションメッセージングエンドポイントを使用してトランザクションメッセージングを送信できるようにします。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Canvas %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `canvas.trigger.send` | [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) | 既存のキャンバスの送信をトリガーします。 |
| `canvas.trigger.schedule.create` | [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/) | API トリガー配信を使用してキャンバスの今後の送信をスケジュールします。 |
| `canvas.trigger.schedule.update` | [`/canvas/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/) | APIトリガー配信でスケジュールされたキャンバスを更新します。 |
| `canvas.trigger.schedule.delete` | [`/canvas/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/)| APIトリガー配信でスケジュールされたキャンバスを削除します。 |
| `canvas.list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) |  キャンバスのリストを問い合わせます。 |
| `canvas.data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) | 特定の期間のキャンバス分析を照会します。 |
| `canvas.details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) | 特定のキャンバスの詳細を照会します。 |
| `canvas.data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/) | 特定の期間のキャンバス分析のロールアップを照会します。 |
| `canvas.url_info.details` | [`/canvas/url_info/details`]({{site.baseurl}}/get_canvas_link_alias/) | キャンバスステップ内の特定のメッセージバリエーションの URL 詳細を照会します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Segments %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `segments.list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) | セグメントのリストを問い合わせます。 |
| `segments.data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/) | 時間範囲のセグメント分析を照会します。 |
| `segments.details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/) | 特定のセグメントの詳細を問い合わせます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Purchases %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `purchases.product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) | アプリで購入した商品のリストを問い合わせます。 |
| `purchases.revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series/) | 時間範囲にわたって、アプリで1日あたりに使われた金額の合計を照会します。 |
| `purchases.quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases/) | 特定の期間内の、1日あたりのアプリ内購入数の合計を照会します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Events %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `events.list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/) | カスタムイベントのリストを問い合わせます。 |
| `events.data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/) | 時間範囲にわたるカスタムイベントの発生を問い合わせます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Sessions %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `sessions.data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/) | 時間範囲内の1日あたりのセッションを問い合わせる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab KPIs %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `kpi.dau.data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/) |  特定の期間内の、1日あたりの固有のアクティブユーザー数を照会します。 |
| `kpi.mau.data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/) | 特定の期間内の、30日間ごとの固有のアクティブユーザー数の合計を照会します。 |
| `kpi.new_users.data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/) | 特定の期間内の、1日あたりの新規ユーザー数を照会します。 |
| `kpi.uninstalls.data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/) | 時間範囲における1日あたりのアプリのアンインストールを問い合わせる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Templates %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `templates.email.create` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/) | ダッシュボードで新しいEメールテンプレートを作成します。 |
| `templates.email.info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | 特定のテンプレートの情報を問い合わせる。 |
| `templates.email.list` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) | Eメールテンプレートのリストを問い合わせる。 |
| `templates.email.update` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/) | ダッシュボードに保存されているEメールテンプレートを更新します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab SSO %}

| 権限 | 説明 |
|---|---|---|
| `sso.saml.login` | ID プロバイダーが開始するログインをセットアップします。詳細については、[サービスプロバイダー （SP） が開始するログイン]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Content Blocks %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `content_blocks.info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) | 特定のテンプレートの情報を問い合わせる。 |
| `content_blocks.list` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) | コンテンツ・ブロックのリストを問い合わせる。 |
| `content_blocks.create` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/) | ダッシュボードに新しいコンテンツブロックを作成します。 |
| `content_blocks.update` | [`/content_blocks_update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) | ダッシュボード上の既存のコンテンツブロックを更新します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Preference Center %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `preference_center.get` | [`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | ユーザー設定センターを取得します。 |
| `preference_center.list` | [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/) | ユーザー設定センターをリストアップします。 |
| `preference_center.update` | [`/preference_center/v1`]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center)<br><br>[`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/) | ユーザー設定センターを作成または更新します。 |
| `preference_center.user.get` | [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center) | ユーザー用のユーザー設定センターリンクを取得します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Subscription %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `subscription.status.set` | [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) | サブスクリプショングループのステータスを設定します。 |
| `subscription.status.get` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) | サブスクリプショングループのステータスを取得します。 |
| `subscription.groups.get` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) | 特定のユーザーが明示的にサブスクライブおよびアンサブスクライブしているサブスクリプショングループのステータスを取得します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab SMS %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `sms.invalid_phone_numbers` | [`/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers/) | 無効な電話番号を照会します。 |
| `sms.invalid_phone_numbers.remove` | [`/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers/) | ユーザーから無効な電話番号フラグを削除します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Catalogs %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `catalogs.add_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/) | 既存のカタログに複数のアイテムを追加します。 |
| `catalogs.update_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/) | 既存のカタログの複数の項目を更新します。 |
| `catalogs.delete_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk) | 既存のカタログから複数の項目を削除します。 |
| `catalogs.get_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/) | 既存のカタログから単一の項目を取得します。 |
| `catalogs.update_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/) | 既存のカタログの単一項目を更新します。 |
| `catalogs.create_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/) | 既存のカタログに単一の項目を作成します。 |
| `catalogs.delete_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/) | 既存のカタログから単一の項目を削除します。 |
| `catalogs.replace_item` | [` /catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/) | 既存のカタログから単一の項目を置き換える。 |
| `catalogs.create` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/) | カタログを作成します。 |
| `catalogs.get` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) | カタログのリストを入手します。 |
| `catalogs.delete` | [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/) | カタログを削除します。 |
| `catalogs.get_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/) | 既存のカタログからアイテムのプレビューを取得します。 |
| `catalogs.replace_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/) | 既存のカタログのアイテムを置き換える。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab SDK Authentication %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `sdk_authentication.create` | [`/app_group/sdk_authentication/create`]({{site.baseurl}}/api/endpoints/sdk_authentication/post_create_sdk_authentication_key) | アプリ用に新しい SDK 認証キーを作成する。 |
| `sdk_authentication.primary` | [`/app_group/sdk_authentication/primary`]({{site.baseurl}}/api/endpoints/sdk_authentication/put_primary_sdk_authentication_key/) | SDK 認証キーをアプリのプライマリキーとしてマークします。 |
| `sdk_authentication.delete` | [`/app_group/sdk_authentication/delete`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key) | アプリの SDK 認証キーを削除する。 |
| `sdk_authentication.keys` | [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | アプリのすべての SDK 認証キーを取得する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% endtabs %}

### REST API キーを管理する

**設定**＞**APIと識別子**＞**APIキー**タブから、既存のREST APIキーの詳細を見たり、削除したりできる。REST APIキーは、作成後に編集することはできない。

**APIキー]**タブには、各キーについて以下の情報が含まれている：

| フィールド        | 説明                                                                                                         |
| ------------ | :------------------------------------------------------------------------------------------------------------------ |
| APIキー名 | 作成時にキーにつけられた名前。                                                                            |
| 識別子   | APIキー。                                                                                                        |
| 作成者   | 鍵を作成したユーザーのメールアドレス。このフィールドは、2023年6月以前に作成された鍵については「N/A」と表示される。 |
| 作成日 | このキーが作成された日付。                                                                                      |
| 最終閲覧日    | このキーが最後に使われた日付。使用されていないキーの場合、このフィールドには「N/A」と表示されます。                  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

API キーの詳細を表示するには、キーにカーソルを合わせて [<i class="fa-solid fa-eye" alt="View"></i> **表示**] を選択します。これには、このキーが持つすべての権限、ホワイトリストに登録されている IP (もしあれば)、このキーが Braze IP ホワイトリストに登録されているかどうかが含まれます。

![Braze ダッシュボードの API キー権限のリスト。]({% image_buster /assets/img_archive/view-api-key.png %})

[ユーザーを削除しても]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/)、そのユーザーが作成したAPIキーは削除されない。キーを削除するには、キーにカーソルを合わせ、[<i class="fa-solid fa-trash-can" alt="Delete"></i> **削除**] を選択します。

![ゴミ箱のアイコンが強調表示され、「削除」を示す「最終閲覧日」という API キー。]({% image_buster /assets/img_archive/api-key-options.png %}){: style="max-width:30%;"}

### REST APIキーのセキュリティ

APIキーは、APIコールを認証するために使用されます。新しい REST API キーを作成するときには、特定のエンドポイントへのアクセス権をキーに付与する必要があります。API キーに特定の権限を割り当てることで、API キーが認証できる呼び出しを厳密に制限できます。

REST API キーによって潜在的に機密性の高い REST API エンドポイントへのアクセスが許可される場合は、これらのキーをセキュリティで保護し、信頼できるパートナーとのみ共有します。これらのキーは一般公開しないでください。例えば、このキーを使ってウェブサイトからAJAXコールを行ったり、その他の一般的な方法で公開してはいけません。

適切なセキュリティープラクティスは、ジョブを完了するために必要なアクセス権のみをユーザーに割り当てることです。この原則は、各キーに権限を割り当てることによって API キーにも適用できます。これらのアクセス許可により、セキュリティが向上し、アカウントのさまざまな領域をコントロールできます。

{% alert warning %}
REST APIキーは、潜在的にセンシティブなREST APIエンドポイントへのアクセスを可能にするものであることを考慮し、それらが安全に保管され、使用されることを確認してください。例えば、このキーを使ってウェブサイトからAJAXコールを行ったり、その他の一般的な方法で公開してはいけません。
{% endalert %}

誤ってキーを公開してしまった場合は、開発者コンソールから削除することができる。このプロセスに関するヘルプについては、[[サポートチケット]({{site.baseurl}}/braze_support/)] を開きます。

### API IP の許可リスト

セキュリティをさらに強化するため、特定の REST API キーに対して REST API 要求を実行できる IP アドレスやサブネットのリストを指定できます。これは、許可リストまたはホワイトリストと呼ばれます。特定のIPアドレスやサブネットを許可するには、新しいREST APIキーを作成する際に、**Whitelist IPs**セクションに追加します。：

![API キーの作成時に IP を許可リストに登録するオプション]({% image_buster /assets/img_archive/api-key-ip-whitelisting.png %})

何も指定しない場合、すべての IP アドレスからリクエストを送信できます。

{% alert tip %}
Braze to Braze webhook を作成し、許可リストを使用する場合は、[ホワイトリストに追加する IP]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-whitelisting) のリストを確認してください。
{% endalert %}

## その他のリソース

### Rubyクライアント・ライブラリ

Ruby を使用してBrazeを実装している場合は、[Ruby クライアントライブラリ](https://github.com/braze-inc/braze-api-client-ruby) を使用してデータのインポート時間を短縮できます。クライアント・ライブラリとは、あるプログラミング言語（この場合はRuby）に特化したコードの集まりで、APIを使いやすくするものだ。

Ruby クライアントライブラリは、[ユーザーエンドポイント]({{site.baseurl}}/api/endpoints/user_data)をサポートしています。

{% alert important %}
このクライアント・ライブラリーはベータ版である。このライブラリをより良いものにするために協力してくれませんか?ご意見、ご感想は[smb-product@braze.com](mailto:smb-product@braze.com) まで。
{% endalert %}

