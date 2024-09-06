---
nav_title: Webhookの作成
article_title: Webhookの作成
page_order: 1
channel:
  - webhooks
description: "このリファレンス記事では、Webhookの作成と設定方法について説明します。"
search_rank: 2
---

# Webhookを作成する

> Webhookキャンペーンを作成するか、Webhookをマルチチャネルキャンペーンに含めることで、アプリ以外のアクションをトリガーできます。より具体的には、[webhook][14]は他のシステムやアプリケーションにリアルタイム情報を提供するために使用できます。 

webhookを使用して、SalesforceやMarketoなどのシステムに情報を送信できます。webhookを使用して、情報をバックエンドシステムに送信することもできます。例えば、カスタムイベントを一定回数行った後に、プロモーションで顧客のアカウントにクレジットを付与したい場合があります。

webhookとは何か、またBrazeでの使用方法について詳しく知りたい場合は、先に[webhookについて]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/)をご覧ください。

## ステップ 1:メッセージを作成する場所を選択する

メッセージは、キャンペーンとキャンバスのどちらを使用して配信すべきでしょうか。キャンペーンは単一のシンプルなメッセージングキャンペーンに適していますが、キャンバスはマルチステップのユーザーのジャーニーに適しています。

{% tabs %}
{% tab キャンペーン %}

**ステップ:**

1. **メッセージング** > **キャンペーン** に移動し、<i class="fas fa-plus"></i> **キャンペーンを作成** をクリックします。
{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、\[**エンゲージメント**] の下に \[**キャンペーン**] が表示されます。
{% endalert %}

{:start="2"}
2\.**Webhook**を選択するか、複数のチャネルをターゲットにしたキャンペーンの場合は**マルチチャネルキャンペーン**を選択します。
3\.キャンペーンに、明確で意味のある名前を付けます。
4\.必要に応じて、\[[チーム]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/)] と \[[タグ]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/)] を追加します。
   * タグを使用すると、キャンペーンを検索してレポートを作成しやすくなります。例えば、\[[レポートビルダー]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/)] を使用する場合、特定のタグでフィルターできます。
5. キャンペーンに必要な数だけバリアントを追加して名前を付けます。追加された各バリアントに対して、異なるWebhookテンプレートを選択できます。このトピックの詳細については、「[多変量テストと AB テスト]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)」を参照してください。

{% alert tip %}
キャンペーン内のすべてのメッセージが類似しているか、同じ内容になる場合は、メッセージを作成してからバリアントを追加します。その後、\[**バリアントを追加**] ドロップダウンから \[**バリアントをコピー**] を選択できます。
{% endalert %}

{% endtab %}
{% tab キャンバス %}

**ステップ:**

1. キャンバス作成ツールを使用して \[[キャンバスを作成]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)] します。
2. キャンバスを設定したら、キャンバスビルダーにステップを追加します。ステップに、明確で意味のある名前を付けます。
3. \[[ステップスケジュール]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay)] を選択し、必要に応じて遅延を指定します。
4. 必要に応じて、このステップのオーディエンスをフィルターします。セグメントを指定し、フィルターを追加して、このステップの受信者をさらに絞り込むことができます。後から、メッセージの送信時に、オーディエンスオプションがチェックされます。
5. \[[昇進動作]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/)] を選択します。
6. メッセージと組み合わせる他のメッセージングチャネルを選択します。

{% endtab %}
{% endtabs %}

## ステップ 2:Webhookを作成する

Webhookをゼロから構築するか、既存のテンプレートのいずれかを使用するかを選択できます。次に、エディタの**Compose**タブでWebhookを構築します。

![BrazeでWebhookを作成する際の作成タブ]({% image_buster /assets/img_archive/webhook_compose.png %})

「**作成**」タブには次のフィールドが含まれています:

#### 言語 {#internationalization}

[国際化][16]は、URLおよびリクエストボディでサポートされています。メッセージを国際化するには、**言語を追加**をクリックして、必要なフィールドに記入してください。コンテンツを書く前に言語を選択することをお勧めします。そうすれば、Liquidに適切な場所にテキストを入力できます。[利用可能な言語]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported)の完全なリストをご覧ください。

#### Webhook URL

Webhook URL、またはHTTP URLは、エンドポイントを指定します。エンドポイントは、Webhookでキャプチャしている情報を送信する場所です。ベンダーに情報を送信したい場合、ベンダーはAPIドキュメントにこのURLを提供する必要があります。自分のシステムに情報を送信する場合は、開発チームまたは開発チームに確認して、正しいURLを使用していることを確認してください。 

Brazeは、標準ポート`80`（HTTP）および`443`（HTTPS）で通信するURLのみを許可します。

[Liquid][15]を使用してWebhook URLをパーソナライズできます。場合によっては、特定のエンドポイントがユーザーを識別するか、URLの一部としてユーザー固有の情報を提供する必要がある場合があります。Liquidを使用する場合は、URLで使用するユーザー固有の情報ごとに[デフォルト値][19]を含めるようにしてください。

#### Request body

リクエストボディは、指定したURLに送信される情報です。Webhookリクエストの本文を作成する方法は2つあります:

##### JSONキーと値のペア

JSONキーと値のペアを使用すると、JSON形式を期待するエンドポイントへのリクエストを簡単に作成できます。この機能は、JSONリクエストを期待するエンドポイントでのみ使用できます。例えば、あなたのキーが`message_body`の場合、対応する値は`Your order just arrived!`かもしれません。キーと値のペアを入力すると、コンポーザーがリクエストをJSON構文で構成し、JSONリクエストのプレビューが自動的に表示されます。

![リクエストボディをJSONキーと値のペアに設定][21]

リクエストに[Liquid][15]を使用して、任意のユーザー属性、[カスタム属性][17]、または[イベントプロパティ][18]を含めるなど、キーと値のペアをパーソナライズできます。例えば、リクエストに顧客の名とメールを含めることができます。各属性に[デフォルト値][19]を含めることを忘れないでください！

##### 生のテキスト

生のテキストオプションを使用すると、任意の形式の本文を期待するエンドポイントへのリクエストを作成する柔軟性が得られます。例えば、この機能を使用して、リクエストがXML形式であることを期待するエンドポイントへのリクエストを作成することができます。両方の[パーソナライゼーション][15]と[国際化][16]は、Liquidを使用して生のテキストでサポートされています。

![リクエストボディが生のテキストに設定されました][22]

`Content-Type` [リクエストヘッダー](#request-headers-optional) を `application/x-www-form-url-encoded` に設定した場合、リクエストボディは URL エンコードされた文字列としてフォーマットする必要があります。以下に例を示します。

{% raw %}
```
to={{custom_attribute.${example}}}&text=Your+order+just+arrived
```
{% endraw %}

![URLエンコードされた文字列を含むリクエストボディ。][23]

## ステップ 3:追加設定を構成する

#### リクエストヘッダー（オプション）

特定のエンドポイントでは、リクエストにヘッダーを含める必要がある場合があります。作成者の**設定**セクションでは、好きなだけヘッダーを追加できます。一般的なリクエストヘッダーは`Content-Type`仕様（本文にどのようなデータが含まれるかを示すもので、XMLやJSONなど）と、ベンダーやシステムに対する認証情報を含む認証ヘッダーです。 

コンテンツタイプの仕様にはキー`Content-Type`を使用する必要があります。一般的な値は`application/json`または`application/x-www-form-urlencoded`です。

Authorization headers must use the key `Authorization`.一般的な値は{% raw %} `Bearer {{YOUR_TOKEN}}`または`Basic {{YOUR_TOKEN}}` {% endraw %}で、`YOUR_TOKEN`はベンダーまたはシステムによって提供される資格情報です。

#### HTTPメソッド

送信する情報のエンドポイントに応じて、使用する[HTTPメソッド]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/#methods)が異なります。ほとんどの場合、POSTを使用します。

![作成者の設定タブでリクエストヘッダーとHTTPメソッドを指定します][26]

## ステップ 4:テストメッセージを送信

キャンペーンを公開する前に、Brazeはリクエストが正しくフォーマットされていることを確認するためにWebhookをテストすることを推奨します。

そのためには、**テスト**タブに切り替えてテストWebhookを送信します。Webhook をランダムなユーザー、特定のユーザー（外部ユーザーIDのメールアドレスを入力することによって）、または選択した属性を持つカスタマイズされたユーザーとしてテストできます。  

テストWebhookを送信した後、応答メッセージが表示されるダイアログが表示されます。Webhookリクエストが失敗した場合は、トラブルシューティングのためにエラーメッセージを参照してください。次の例は、無効なWebhook URLを持つWebhookの応答を詳述しています。

```json
404 Not Found

{
  "error": {
    "message": "Unrecognized request URL. Please see https://lob.com/docs or email us at support@lob.com.",
    "status_code": 404
  }
}

```

## ステップ 5: キャンペーンまたはキャンバスの残りの部分を作成する

{% tabs %}
{% tab キャンペーン %}

次に、キャンペーンの残りの部分を構築します。ツールを使用してwebhookを構築する方法の詳細については、次のセクションを参照してください。

#### 配信スケジュールまたはトリガーを選択する

webhookは、スケジュールされた時間、アクション、またはAPIトリガーに基づいて配信されます。詳細については、[キャンペーンのスケジューリング]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/)を参照してください。

アクションベースの配信では、キャンペーンの継続時間と \[[サイレント時間]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours)] を設定することもできます。

このステップでは、ユーザーがキャンペーンを受け取るために[再適格]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns)になることを許可したり、[フリークエンシーキャップ]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping)ルールを有効にしたりするなど、配信制御を指定することもできます。

#### ターゲットとするユーザーを選択する

次に、セグメントやフィルターを選択して[ターゲットユーザー]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/)を絞り込み、オーディエンスを絞り込む必要があります。このステップでは、セグメントからより大きなオーディエンスを選択し、必要に応じてフィルターでそのセグメントをさらに絞り込みます。セグメントのおおよその人数について現在の状態を示すスナップショットが自動的に表示されます。正確なセグメントメンバーシップは常にメッセージが送信される直前に計算されることに注意してください。

#### コンバージョンイベントを選択する

Braze では、キャンペーンを受信した後、ユーザーが指定のアクションや[コンバージョンイベント]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/)を実行する頻度を追跡できます。ユーザーが指定したアクションを実行した場合にコンバージョンがカウントされる期間は、最大 30 日間まで設定できます。

{% endtab %}

{% tab キャンバス %}

もしまだ行っていない場合は、キャンバスステップの残りのセクションを完了してください。詳細については、キャンバスの残りの部分を構築する方法、多変量テストとインテリジェントセレクションを実装する方法などについては、キャンバスドキュメントの[キャンバスを構築する]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas)ステップを参照してください。

{% endtab %}
{% endtabs %}

## ステップ 6:レビューと展開

キャンペーンまたはキャンバスの最後の構築が完了したら、その詳細を確認し、テストしてから送信してください！

## 知っておくべきこと

### エラー、リトライロジック、タイムアウト

webhookはBrazeサーバーが外部エンドポイントにリクエストを送信することに依存しており、構文やその他のエラーが発生する可能性があります。Webhookエラーを回避するための最初のステップは、Webhookキャンペーンを構文エラーについてテストし、パーソナライズされた変数にデフォルト値があることを確認することです。ただし、webhookは期限切れのAPIキー、レート制限、予期しないサーバーエラーなどの問題により失敗する可能性があります。Webhook が送信に失敗した場合、エラーメッセージが \[メッセージアクティビティログ][42] に記録されます。

この説明には、エラーが発生した時間、アプリ名、およびエラーメッセージが含まれています:

![Webhookエラー: メッセージ「現在のユーザーに関する情報を照会するにはアクティブなアクセス トークンを使用する必要があります」][43]

メッセージ本文がエラーの原因について十分に明確でない場合、使用しているAPIエンドポイントのドキュメントを確認する必要があります。これらは通常、エンドポイントが使用するエラーコードの説明と、それらが通常引き起こされる原因を提供します。

他のキャンペーンと同様に、BrazeはWebhookキャンペーンの配信とそれに伴うコンバージョンを追跡します。Webhookリクエストが送信されると、受信サーバーはリクエストに何が起こったかを示す応答コードを返します。次の表は、サーバーが送信する可能性のあるさまざまな応答、それらがキャンペーン分析に与える影響、およびエラーの場合にBrazeがキャンペーンを再配信しようとするかどうかをまとめたものです。

| 応答コード | 受領済みとしてマークされましたか？ | リトライ？ |
|---------------|-----------|----------|
| 20x (成功)  | はい |   該当なし  |
| 30x（リダイレクト）  | いいえ | いいえ |
| 408 (リクエストタイムアウト)  | いいえ | はい |
| 429（レート制限）  | いいえ | はい |
| その他の4xx（クライアントエラー）  | いいえ | いいえ |
| 5xx (サーバーエラー)   | いいえ | はい |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

BrazeはWebhookの送信を最大24時間再試行します。再試行する場合、Braze は指数バックオフを使用して約 30 分間にわたって FIVE 回試行し、個々の Webhook 呼び出しを中止します。

各Webhookはタイムアウトするまでに90秒が許可されています。

### IP 許可リスト {#ip-allowlisting}

BrazeからWebhookが送信されると、Brazeサーバーは顧客またはサードパーティのサーバーにネットワークリクエストを行います。IP許可リストを使用すると、WebhookリクエストがBrazeから送信されていることを確認でき、セキュリティの層が追加されます。

Brazeは次のIPからwebhookを送信します。記載されているIPは、許可リストにオプトインしたすべてのAPIキーに自動的かつ動的に追加されます。

{% alert important %}
Braze-to-Braze webhook を作成していて、許可リストを使用している場合は、`127.0.0.1` を含む次のすべての IP を許可リストに追加する必要があります。
{% endalert %}

| インスタンス `US-01`、`US-02`、`US-03`、`US-04`、`US-05`、`US-06`、および `US-07` の場合: |
|---|
| `127.0.0.1`
| `23.21.118.191`
| `34.206.23.173`
| `50.16.249.9`
| `52.4.160.214`
| `54.87.8.34`
| `54.156.35.251`
| `52.54.89.238`
| `18.205.178.15`

| インスタンス `EU-01` および `EU-02` の場合: |
|---|
| `127.0.0.1`
| `52.58.142.242`
| `52.29.193.121`
| `35.158.29.228`
| `18.157.135.97`
| `3.123.166.46`
| `3.64.27.36`
| `3.65.88.25`
| `3.68.144.188`
| `3.70.107.88` 

| 例えば`US-08`: |
|---|
| `52.151.246.51`
| `52.170.163.182`
| `40.76.166.157`
| `40.76.166.170`
| `40.76.166.167`
| `40.76.166.161`
| `40.76.166.156`
| `40.76.166.166`
| `40.76.166.160`
| `40.88.51.74`
| `52.154.67.17`
| `40.76.166.80`
| `40.76.166.84`
| `40.76.166.85`
| `40.76.166.81`
| `40.76.166.71`
| `40.76.166.144`
| `40.76.166.145`

### Brazeパートナー{#utilizing-webhooks}とwebhookを使用する

webhookを使用する方法はたくさんあり、私たちの技術パートナー（Alloys）と一緒に、顧客やユーザーと直接コミュニケーションを向上させるためにwebhookを使用できます。

チェックアウト：
* [Messenger]({{site.baseurl}}/partners/message_orchestration/additional_channels/instant_chat/messenger/)
* [Remerge]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/remerge)
* [Lob.com]({{site.baseurl}}/partners/message_orchestration/additional_channels/direct_mail/lob)
* そして、私たちの多くの[技術パートナー]({{site.baseurl}}/partners/home/)も！

[14]: https://sendgrid.com/blog/whats-webhook
[15]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/
[16]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages
[17]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#additional-notes-and-best-practices
[18]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[19]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/
[21]: {% image_buster /assets/img/webhook_json_1.png %}
[22]: {% image_buster /assets/img_archive/webhook_rawtext.png %}
[23]: {% image_buster /assets/img_archive/webhook_rawtext_URL-encoded.png %}
[26]: {% image_buster /assets/img_archive/webhook_request_header.png %}
[42]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/message_activity_log_tab/
[43]: {% image_buster /assets/img_archive/webhook-error.png %}
