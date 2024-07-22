---
nav_title: "APIの概要"
article_title: APIの概要
page_order: 2.1
description: "このリファレンス記事では、REST APIとは何か、用語、APIキーの概要など、APIの基本をカバーしている。"
page_type: reference
alias: /api/api_key/
---

# APIの概要

> このリファレンス記事では、一般的な用語、REST APIキーやパーミッションの概要、それらを安全に保つ方法など、APIの基本をカバーしている。

## Braze REST APIコレクション

| コレクション                                                                 | 目的                                                                               |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [カタログ]({{site.baseurl}}/api/endpoints/catalogs/)                       | Brazeのキャンペーンで参照するカタログやカタログ項目を作成、管理する。    |
| [クラウドデータ取り込み]({{site.baseurl}}/api/endpoints/cdi/)                | データウェアハウスの統合と同期を管理する。                                    |
| [電子メールリストとアドレス]({{site.baseurl}}/api/endpoints/email/)         | Brazeとお使いのメールシステム間の双方向同期を設定・管理。           |
| [エクスポート]({{site.baseurl}}/api/endpoints/export/)                           | キャンペーン、キャンバス、KPIなどの様々な詳細にアクセスし、エクスポートする。        |
| [メッセージ]({{site.baseurl}}/api/endpoints/messaging/)                      | キャンペーンとキャンバスのスケジュール設定、送信、管理ができる。                               |
| [プリファレンスセンター]({{site.baseurl}}/api/endpoints/preference_center/)     | プリファレンス・センターを構築し、そのスタイリングを更新する。                            |
| [SCIM]({{site.baseurl}}/api/endpoints/scim/)                               | クラウドベースのアプリケーションやサービスにおけるユーザーIDを管理する。                      |
| [SMS]({{site.baseurl}}/api/endpoints/sms/)                                 | サブスクリプショングループでユーザーの電話番号を管理する。                         |
| [サブスクリプショングループ]({{site.baseurl}}/api/endpoints/subscription_groups/) | Brazeダッシュボードに保存されているSMSとEメールの購読グループをリストアップし、更新する。 |
| [テンプレート]({{site.baseurl}}/api/endpoints/templates/)                     | メールメッセージやコンテンツブロックのテンプレートを作成し、更新する。                   |
| [ユーザーデータ]({{site.baseurl}}/api/endpoints/user_data/)                     | ユーザーを特定し、追跡し、管理する。                                               |
{: .reset-td-br-1 .reset-td-br-2}

## API定義

以下は、Braze REST APIのドキュメントで目にする用語の概要である。

### エンドポイント

Brazeは、ダッシュボードとRESTエンドポイント用のさまざまなインスタンスを管理している。アカウントのプロビジョニングが完了したら、以下のURLのいずれかにログインする。どのインスタンスにプロビジョニングされるかに基づいて、正しいRESTエンドポイントを使用する。不明な場合は、\[support ticket]\[support] ] を開くか、以下の表を使用して、使用するダッシュボードの URL を正しい REST Endpoint に一致させる。

{% alert important %}
API呼び出しにエンドポイントを使用する場合は、RESTエンドポイントを使用する。

SDK統合には、RESTエンドポイントではなく[SDKエンド]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/)ポイントを使用する。
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

### API制限

ほとんどのAPIについて、Brazeはデフォルトで1時間あたり250,000リクエストというレート制限を設けている。しかし、特定のリクエストタイプには、当社の顧客ベース全体で大量のデータをよりよく処理するために、独自のレート制限が適用される。詳細は[APIレート制限を]({{site.baseurl}}/api/api_limits/)参照のこと。

### ユーザー ID 

- **External user ID**:`external_id` は、あなたがデータを提出する際の一意のユーザー識別子の役割を果たす。この識別子は、同じユーザーに複数のプロファイルが作成されるのを避けるため、Braze SDKで設定したものと同じでなければならない。
- **BrazeユーザーID**：`braze_id` は、Brazeが設定する固有のユーザー識別子の役割を果たす。この識別子は、external_idsに加えて、REST APIを通じてユーザーを削除するために使用できる。

詳細については、[iOS][9]、[Android][10]、[Webの][13]各プラットフォームに応じた以下の記事を参照のこと。

## REST APIキー

REST Application Programming Interfaceキー（REST APIキー）は、APIコールを認証し、コールするアプリケーションやユーザーを識別するためにAPIに渡される一意のコードである。APIアクセスは、御社のREST APIエンドポイントへのHTTPSウェブリクエストを使って行われる。Brazeでは、REST APIキーをApp Identifierキーと組み合わせて使用し、データの追跡、アクセス、送信、エクスポート、分析を行い、お客様とBrazeの両エンドですべてがスムーズに進むようサポートする。

Brazeでは、ワークスペースとAPIキーは密接な関係にある。ワークスペースは、複数のプラットフォームにまたがる同じアプリケーションのバージョンを収容するように設計されている。また、多くの顧客はワークスペースを使用して、無料版とプレミアム版のアプリケーションを同じプラットフォーム上に格納している。お気づきかもしれないが、これらのワークスペースもREST APIを利用しており、独自のREST APIキーを持っている。これらのキーは、API上の特定のエンドポイントへのアクセスを含むように、個別にスコープすることができる。APIへの各コールは、エンドポイントヒットにアクセスできるキーを含まなければならない。

REST API キーとワークスペース API キーの両方を`api_key` と呼ぶ。`api_key` はリクエストヘッダとして各リクエストに含まれ、REST APIを使用するための認証キーとして機能する。これらのREST APIは、ユーザーの追跡、メッセージの送信、ユーザーデータのエクスポートなどに使用される。新しいREST APIキーを作成する際には、そのキーに特定のエンドポイントへのアクセス権を与える必要がある。APIキーに特定の権限を割り当てることで、APIキーが認証できるコールを厳密に制限することができる。

![API KeysページにあるREST APIキーのパネル。][27]

{% alert tip %}
REST APIキーに加えて、Identifierキーと呼ばれるタイプのキーも存在し、これはAPIからアプリ、テンプレート、Canvases、キャンペーン、Content Card、セグメントといった特定のものを参照するために使用できる。詳細については、[API Identifier typesを]({{site.baseurl}}/api/identifier_types/)参照のこと。
{% endalert %}

### REST APIキーのパーミッション

APIキーのパーミッションは、特定のAPIコールへのアクセスを制限するために、ユーザーまたはグループに割り当てることができるパーミッションである。APIキーのパーミッションのリストを表示するには、**「Settings（設定**）」＞「**API Keys（APIキー**）」と進み、APIキーを選択する。

{% tabs %}
{% tab User Data %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `users.track` | [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) | ユーザー属性、カスタムイベント、購入を記録する。 | 
| `users.delete` | [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) | 任意のユーザーを削除する。 |
| `users.alias.new` | [`/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias/) |既存のユーザーのエイリアスを新規作成する。 |
| `users.identify` | [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) |外部IDを持つエイリアスのみのユーザーを特定する。 |
| `users.export.ids` | [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) |ユーザーIDでユーザープロファイル情報を照会する。 |
| `users.export.segment` | [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) |セグメント別のユーザープロファイル情報を照会する。 | 
| `users.merge` | [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) | 既存の2人のユーザーを互いにマージする。 |
| `users.external_ids.rename` | [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/) | 既存のユーザーの外部IDを変更する。 |
| `users.external_ids.remove` | [`/users/external_ids/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove/) | 既存のユーザーの外部IDを削除する。 |
| `users.alias.update` | [`/users/alias/update`]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/) | 既存のユーザーのエイリアスを更新する。 |
| `users.export.global_control_group` | [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/) | グローバルコントロールグループのユーザープロファイル情報を照会する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

 {% endtab %}
 {% tab Email %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `email.unsubscribe` | [`/email/unsubscribes`]({{site.baseurl}}/api/endpoints/email/get_query_unsubscribed_email_addresses/) | 配信停止になっているメールアドレスを問い合わせる。  |
| `email.status` | [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/) | メールアドレスのステータスを変更する。 |
| `email.hard_bounces` | [`/email/hard_bounces`]({{site.baseurl}}/api/endpoints/email/get_list_hard_bounces/) | ハードバウンスされたメールアドレスを問い合わせる。 |
| `email.bounce.remove` | [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces/) | ハードバウンスリストからメールアドレスを削除する。 |
| `email.spam.remove` | [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam/) | スパムリストからメールアドレスを削除する。 |
| `email.blacklist` | [`/email/blacklist`]({{site.baseurl}}/api/endpoints/email/post_blacklist/) | ブロックリストのメールアドレス。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Messages %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `messages.send` | [`/messages/send `]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) | 特定のユーザーに即座にメッセージを送る。 |
| `messages.schedule.create` | [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/) | 特定の時間にメッセージを送信するようスケジュールする。 |
| `messages.schedule.update` | [`/messages/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/) | スケジュールされたメッセージを更新する。 |
| `messages.schedule.delete` | [`/messages/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/) | スケジュールされたメッセージを削除する。 |
| `messages.schedule_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/) | スケジュールされたすべてのブロードキャストメッセージを問い合わせる。 |
| `messages.live_activity.update` | [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update/) | iOSのライブアクティビティを更新する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Campaigns %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `campaigns.trigger.send` | [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) | 既存のキャンペーンの送信をトリガーする。 |
| `campaigns.trigger.schedule.create` | [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/) | APIトリガー配信でキャンペーンの将来の送信をスケジュールする。 |
| `campaigns.trigger.schedule.update` | [`/campaigns/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/) | APIトリガー配信でスケジュールされたキャンペーンを更新する。 |
| `campaigns.trigger.schedule.delete` | [`/campaigns/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/) |APIトリガー配信でスケジュールされたキャンペーンを削除する。 |
| `campaigns.list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) | キャンペーンの一覧を問い合わせる。 |
| `campaigns.data_series` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) | 時間範囲のキャンペーン分析を照会する。 |
| `campaigns.details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) | 特定のキャンペーンの詳細を問い合わせる。 |
| `sends.data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) | 時間範囲内のメッセージ送信分析を問い合わせる。 |
| `sends.id.create` | [`/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/) | メッセージブラスト追跡用の送信IDを作成する。 |
| `campaigns.url_info.details` | [`/campaigns/url_info/details`]({{site.baseurl}}) | キャンペーン内の特定のメッセージバリエーションのURL詳細を問い合わせる。 |
| `transactional.send` | [`/transactional/v1/campaigns/{campaign_id}/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message/) | トランザクション・メッセージング・エンドポイントを使ってトランザクション・メッセージングを送信できるようにする。 |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Canvas %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `canvas.trigger.send` | [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) | 既存のキャンバスの送信をトリガーする。 |
| `canvas.trigger.schedule.create` | [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/) | APIトリガー配信でキャンバスの将来の送信をスケジュールする。 |
| `canvas.trigger.schedule.update` | [`/canvas/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/) | APIトリガー配信でスケジュールされたキャンバスを更新する。 |
| `canvas.trigger.schedule.delete` | [`/canvas/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/)| APIトリガー配信でスケジュールされたキャンバスを削除する。 |
| `canvas.list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) |  キャンバスのリストを問い合わせる。 |
| `canvas.data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) | キャンバスのアナリティクスを時間範囲でクエリーする。 |
| `canvas.details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) | 特定のキャンバスの詳細を問い合わせる。 |
| `canvas.data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/) | キャンバスのアナリティクスのロールアップを時間範囲で検索する。 |
| `canvas.url_info.details` | [`/canvas/url_info/details`]({{site.baseurl}}/get_canvas_link_alias/) | Canvasステップ内の特定のメッセージバリエーションのURLの詳細を問い合わせる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Segments %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `segments.list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) | セグメントのリストを問い合わせる。 |
| `segments.data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/) | 時間範囲のセグメント分析を照会する。 |
| `segments.details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/) | 特定のセグメントの詳細を問い合わせる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Purchases %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `purchases.product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) | アプリで購入した商品のリストを問い合わせる。 |
| `purchases.revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series/) | 時間範囲にわたって、アプリで1日あたりに使われた金額の合計を照会する。 |
| `purchases.quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases/) | ある時間範囲における、アプリでの1日あたりの購入数の合計を問い合わせる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Events %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `events.list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/) | カスタムイベントのリストを問い合わせる。 |
| `events.data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/) | 時間範囲にわたるカスタムイベントの発生を問い合わせる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab News Feed %}

{% alert note %}
ニュースフィードは非推奨になります。Braze では、News Feed ツールを使用するお客様は、コンテンツカードメッセージングチャネルに移動することを推奨しています。これは、より柔軟でカスタマイズ可能で、信頼性が高いチャネルです。詳しくは[マイグレーションガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。
{% endalert %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `feed.list` | [`/feed/list`]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_cards/) | ニュースフィードカードの一覧を問い合わせる。 |
| `feed.data_series` | [`/feed/data_series`]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_card_analytics/) | ニュースフィードの分析を時間範囲にわたって照会する。 |
| `feed.details` | [`/feed/details`]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_card_details/) | 特定のニュースフィードの詳細を問い合わせる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Sessions %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `sessions.data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/) | 時間範囲内の1日あたりのセッションを問い合わせる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab KPIs %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `kpi.dau.data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/) |  時間範囲内の1日あたりのユニークアクティブユーザーを検索する。 |
| `kpi.mau.data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/) | 30日間の時間範囲で、ユニークアクティブユーザーの合計を検索する。 |
| `kpi.new_users.data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/) | 時間範囲内の1日あたりの新規ユーザーを照会する。 |
| `kpi.uninstalls.data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/) | 時間範囲における1日あたりのアプリのアンインストールを問い合わせる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Templates %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `templates.email.create` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/) | ダッシュボードで新しいEメールテンプレートを作成する。 |
| `templates.email.info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | 特定のテンプレートの情報を問い合わせる。 |
| `templates.email.list` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) | Eメールテンプレートのリストを問い合わせる。 |
| `templates.email.update` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/) | ダッシュボードに保存されているEメールテンプレートを更新する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab SSO %}

| 許可 | 説明 |
|---|---|---|
| `sso.saml.login` | IDプロバイダ主導のログインを設定する。詳細については、[サービスプロバイダー（SP）主導のログインを]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/)参照のこと。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Content Blocks %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `content_blocks.info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) | 特定のテンプレートの情報を問い合わせる。 |
| `content_blocks.list` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) | コンテンツ・ブロックのリストを問い合わせる。 |
| `content_blocks.create` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/) | ダッシュボードに新しいコンテンツブロックを作成する。 |
| `content_blocks.update` | [`/content_blocks_update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) | ダッシュボード上の既存のコンテンツブロックを更新する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Preference Center %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `preference_center.get` | [`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | プリファレンスセンターを利用する。 |
| `preference_center.list` | [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/) | 優先センターをリストアップする。 |
| `preference_center.update` | [`/preference_center/v1`]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center)<br><br>[`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/) | プリファレンス・センターを作成または更新する。 |
| `preference_center.user.get` | [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center) | ユーザーのプリファレンスセンターリンクを取得する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Subscription %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `subscription.status.set` | [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) | 購読グループのステータスを設定する。 |
| `subscription.status.get` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) | サブスクリプショングループのステータスを取得する。 |
| `subscription.groups.get` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) | 特定のユーザーが明示的にサブスクライブおよびアンサブスクライブしているサブスクリプショングループのステータスを取得する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab SMS %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `sms.invalid_phone_numbers` | [`/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers/) | 無効な電話番号を問い合わせる。 |
| `sms.invalid_phone_numbers.remove` | [`/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers/) | ユーザーから無効な電話番号フラグを削除する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Catalogs %}

| 許可 | エンドポイント | 説明 |
|---|---|---|
| `catalogs.add_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/) | 既存のカタログに複数のアイテムを追加する。 |
| `catalogs.update_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/) | 既存のカタログの複数の項目を更新する。 |
| `catalogs.delete_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk) | 既存のカタログから複数の項目を削除する。 |
| `catalogs.get_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/) | 既存のカタログから単一の項目を取得する。 |
| `catalogs.update_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/) | 既存のカタログの単一項目を更新する。 |
| `catalogs.create_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/) | 既存のカタログに単一の項目を作成する。 |
| `catalogs.delete_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/) | 既存のカタログから単一の項目を削除する。 |
| `catalogs.replace_item` | [` /catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/) | 既存のカタログから単一の項目を置き換える。 |
| `catalogs.create` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/) | カタログを作成する。 |
| `catalogs.get` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) | カタログのリストを入手する |
| `catalogs.delete` | [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/) | カタログを削除する。 |
| `catalogs.get_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/) | 既存のカタログからアイテムのプレビューを取得する。 |
| `catalogs.replace_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/) | 既存のカタログのアイテムを置き換える。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% endtabs %}

## REST APIキーを作成する

新しいREST APIキーを作成する：

1. **設定**＞**APIと識別子に**進む。

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、**Developer Console**>**API Settingsから**APIキーを作成できる。
{% endalert %}

{:start="2"}
2\.**Create API Keyを**選択する。
3\.一目で識別できるように、新しいキーに名前をつける。
4\.新しいキーのために、[許可リストのIPアドレスと](#api-ip-allowlisting)サブネットを指定する。
5. 新しいキーに関連付けたい[パーミッションを](#rest-api-key-permissions)選択する。

{% alert important %}
新しいAPIキーを作成した後は、権限の範囲や許可するIPを編集できないことに留意してほしい。この制限はセキュリティ上の理由から設けられている。キーのスコープを変更する必要がある場合は、更新されたパーミッションを持つ新しいキーを作成し、古いキーの代わりにそのキーを実装する。実装が完了したら、古いキーを削除する。
{% endalert %}

## REST API キーを管理する

REST APIキーは、作成後に編集することはできない。ただし、**API Keys**ページから、既存のREST APIキーの詳細を見たり、削除したりすることはできる。**Rest APIキーの**リストには、各キーについて以下の情報が一目でわかるようになっている：

| フィールド        | 説明                                                                                                         |
| ------------ | :------------------------------------------------------------------------------------------------------------------ |
| APIキー名 | 作成時にキーにつけられた名前。                                                                            |
| 識別子   | APIキー。                                                                                                        |
| 作成者   | 鍵を作成したユーザーのメールアドレス。このフィールドは、2023年6月以前に作成された鍵については「N/A」と表示される。 |
| 作成日 | このキーが作成された日付。                                                                                      |
| 最後に見たもの    | このキーが最後に使われた日付。このフィールドは、一度も使用されたことのないキーの場合、"N/A "と表示される。                  |
{: .reset-td-br-1 .reset-td-br-2}

特定のキーの詳細を表示するには、リストからキーを選択する。すると、このキーが持つすべての権限、ホワイトリストに登録されているIP（もしあれば）、このキーがBraze IPホワイトリストに登録されているかどうかを確認できる。

![][30]

[ユーザーを削除]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/)する場合、そのユーザーが作成した関連APIキーは削除されないことに注意すること。キーを削除するには、<i class="fas fa-gear" alt="Settings"></i> をクリックし、対応するオプションを選択する。

![][29]

## REST APIキーのセキュリティ

APIキーは、APIコールを認証するために使用される。新しいREST APIキーを作成する際には、そのキーに特定のエンドポイントへのアクセス権を与える必要がある。APIキーに特定の権限を割り当てることで、APIキーが認証できるコールを厳密に制限することができる。

REST APIキーは、潜在的にセンシティブなREST APIエンドポイントへのアクセスを可能にすることを考慮し、これらのキーを保護し、信頼できるパートナーとのみ共有する。彼らは決して公にされるべきではない。例えば、このキーを使ってウェブサイトからAJAXコールを行ったり、その他の一般的な方法で公開したりしてはならない。

この原則は、各キーに権限を割り当てることで、APIキーにも適用できる。これらの許可は、あなたのアカウントのさまざまな領域に対するより良いセキュリティとコントロールを与える。 

![APIキーの作成時に利用できるAPIキーの権限。][25]

{% alert warning %}
REST APIキーは、潜在的にセンシティブなREST APIエンドポイントへのアクセスを可能にするものであることを考慮し、それらが安全に保管され、使用されることを確認すること。例えば、このキーを使ってウェブサイトからAJAXコールを行ったり、その他の一般的な方法で公開したりしてはならない。
{% endalert %}

偶発的にキーが露出してしまった場合、Developer Consoleから削除することができる。このプロセスに関するヘルプは、\[サポートチケット]\[support].

### API IP の許可リスト

さらなるセキュリティのために、与えられたREST APIキーに対するREST APIリクエストを許可するIPアドレスとサブネットのリストを指定することができる。これは、許可リストまたはホワイトリストと呼ばれます。特定のIPアドレスやサブネットを許可するには、新しいREST APIキーを作成する際に、**Whitelist IPs**セクションに追加する： 

![APIキーの作成時にIPをホワイトリストに登録するオプションが追加された。][26]

何も指定しない場合、すべての IP アドレスからリクエストを送信できます。

{% alert tip %}
Braze to Braze webhook を作成し、許可リストを使用する場合は、[ホワイトリストに追加する IP]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-whitelisting) のリストを確認してください。
{% endalert %}

## その他のリソース

### Rubyクライアント・ライブラリ

Ruby を使用してBrazeを実装している場合は、[Ruby クライアントライブラリ](https://github.com/braze-inc/braze-api-client-ruby) を使用してデータのインポート時間を短縮できます。クライアント・ライブラリとは、あるプログラミング言語（この場合はRuby）に特化したコードの集まりで、APIを使いやすくするものだ。

Rubyクライアント・ライブラリは、[ユーザー・エンドポイントを]({{site.baseurl}}/api/endpoints/user_data)サポートしている。

{% alert note %}
このクライアント・ライブラリは現在ベータ版である。この図書館をより良いものにするために、私たちに協力したい？ご意見、ご感想は[smb-product@braze.com](mailto:smb-product@braze.com) まで。
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
\[support] ： {{site.baseurl}}/braze_support/
[28]: {% image_buster /assets/img_archive/create-new-key.png %}
[29]: {% image_buster /assets/img_archive/api-key-options.png %}
[27]: {% image_buster /assets/img_archive/rest-api-key.png %}
[30]: {% image_buster /assets/img_archive/view-api-key.png %}
