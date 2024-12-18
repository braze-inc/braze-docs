---
nav_title: Webhookの作成
article_title: Webhookを作成する
page_order: 1
channel:
  - webhooks
description: "このリファレンス記事では、Webhook キャンペーンの作成方法と設定方法について説明します。"
search_rank: 2
---

# Webhookキャンペーンを作成する

> Webhookキャンペーンを作成したり、マルチチャネルキャンペーンにWebhookを含めることで、他のシステムやアプリケーションにリアルタイム情報を提供し、アプリ以外のアクションをトリガーすることができる。 

Webhookを使って、SalesforceやMarketoなどのシステムやバックエンドシステムに情報を送ることができる。例えば、顧客がカスタムイベントを一定回数行った後に、プロモーションで顧客のアカウントにクレジットを付与する場合があります。

{% alert tip %}
Webhookとは何か、Brazeでどのように使えるかについては、先に進む前に[「Webhookについて]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/)」をチェックしよう。
{% endalert %}

## ステップ 1: メッセージを作成する場所を選択する

メッセージは、キャンペーンとキャンバスのどちらを使用して配信すべきでしょうか。キャンペーンは単一のシンプルなメッセージングキャンペーンに適していますが、キャンバスはマルチステップのユーザーのジャーニーに適しています。

{% tabs %}
{% tab キャンペーン %}

**ステップ:**

1. [**メッセージング**] > [**キャンペーン**] の順に進み、[**キャンペーンを作成**] を選択します。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、[**エンゲージメント**] の下に [**キャンペーン**] が表示されます。
{% endalert %}

{:start="2"}
2\.[**Webhook**] を選択するか、複数のチャネルをターゲットにしたキャンペーンの場合は [**マルチチャネル**] を選択します。
3\.キャンペーンに、明確で意味のある名前を付けます。
4. (オプション）このキャンペーンがどのように使用されるかを説明するために説明を追加する。
4. 必要に応じて[チームや]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/) [タグを]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/)追加する。
   * タグを使用すると、キャンペーンを検索してレポートを作成しやすくなります。例えば、[[レポートビルダー]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/)] を使用する場合、特定のタグでフィルターできます。
5. キャンペーンに必要な数だけバリアントを追加して名前を付けます。追加された各バリアントに対して、異なるWebhookテンプレートを選択できます。このトピックの詳細については、「[多変量テストと AB テスト]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)」を参照してください。

{% alert tip %}
キャンペーン内のすべてのメッセージが類似しているか、同じ内容になる場合は、メッセージを作成してからバリアントを追加します。その後、[**バリアントを追加**] ドロップダウンから [**バリアントをコピー**] を選択できます。
{% endalert %}

{% endtab %}
{% tab キャンバス %}

**ステップ:**

1. キャンバス作成ツールを使用して [[キャンバスを作成]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)] します。
2. キャンバスを設定したら、キャンバスビルダーにステップを追加します。ステップに、明確で意味のある名前を付けます。
3. [[ステップスケジュール]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay)] を選択し、必要に応じて遅延を指定します。
4. 必要に応じて、このステップのオーディエンスをフィルターします。セグメントを指定し、フィルターを追加して、このステップの受信者をさらに絞り込むことができます。後から、メッセージの送信時に、オーディエンスオプションがチェックされます。
5. [[昇進動作]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/)] を選択します。
6. メッセージと組み合わせる他のメッセージングチャネルを選択します。

{% endtab %}
{% endtabs %}

## ステップ 2: Webhookを構築する

Webhookをゼロから作成するか、既存のテンプレートを使用するか、または当社の既存のテンプレートのいずれかを使用するかを選択できる。次に、エディタの**Compose**タブでWebhookを構築します。

「**作成**」タブには次のフィールドが含まれています:

- 言語
- Webhook URL
- HTTPメソッド
- Request body

![Facebook MessengerのWebhookテンプレートの例がある「Compose」タブ。]({% image_buster /assets/img_archive/webhook_compose.png %})

#### 言語 {#internationalization}

[国際化][16]は、URLおよびリクエストボディでサポートされています。メッセージを複数言語で送信するには、[**言語を追加**] をクリックして、必須フィールドに入力します。 

コンテンツを記述する前に言語を選択することをお勧めします。これにより、Liquid 内の適切な場所にテキストを入力することができます。利用可能なすべての言語のリストについては、[サポートされている言語]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported)を参照してください。

#### Webhook URL

Webhook URL、または HTTP URL は、エンドポイントを指定します。エンドポイントは、Webhook でキャプチャしている情報の送信先にする場所です。 

ベンダーに情報を送信する場合、ベンダーは API ドキュメントでこの URL を提供する必要があります。自社のシステムに情報を送信する場合は、開発者やエンジニアリング・チームに確認し、正しいURLを使用していることを確認すること。 

Brazeは、標準ポート`80`（HTTP）および`443`（HTTPS）で通信するURLのみを許可します。

##### Liquid の使用

[Liquid][15] を使用して Webhook URL をパーソナライズできます。場合によっては、特定のエンドポイントがユーザーを識別するか、URLの一部としてユーザー固有の情報を提供する必要がある場合があります。Liquidを使用する場合は、URLで使用するユーザー固有の情報ごとに[デフォルト値][19]を含めるようにしてください。

#### HTTPメソッド

送信する情報のエンドポイントに応じて、使用する[HTTPメソッド]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/#methods)が異なります。ほとんどのケースではPOSTを使う。

#### Request body

リクエスト本文は、指定した URL に送信される情報です。JSON キーと値のペアまたは生のテキストを使用して Webhook リクエストの本文を作成する方法は2通りあります。

##### JSONキーと値のペア

JSONキーと値のペアを使用すると、JSON形式を期待するエンドポイントへのリクエストを簡単に作成できます。JSONリクエストを期待するエンドポイントでのみ使用できる。例えば、キーが `message_body` の場合、対応する値には `Your order just arrived!` があります。キーと値のペアを入力すると、コンポーザーがリクエストをJSON構文で構成し、JSONリクエストのプレビューが自動的に表示されます。

![JSON キーと値のペアに設定されたリクエスト本文。]({% image_buster /assets/img/webhook_json_1.png %})

Liquid を使用してキーと値のペアをパーソナライズできます (ユーザー属性、[カスタム属性][17]、または[イベントプロパティ][18]を含めるなど)。例えば、リクエストに顧客の名とメールアドレスを含めることができます。各属性の[デフォルト値を][19]必ず含めること。

##### 生のテキスト

[生のテキスト] オプションを使用すると、任意の形式の本文を受け入れるエンドポイントへのリクエストを作成する柔軟性が得られます。例えば、リクエストがXML形式であることを期待するエンドポイントへのリクエストを書くためにこれを使うかもしれない。 

両方の[パーソナライゼーション][15]と[国際化][16]は、Liquidを使用して生のテキストでサポートされています。

![Liquid を使用した生のテキストを含むリクエスト本文の例。]({% image_buster /assets/img_archive/webhook_rawtext.png %})

`Content-Type` [リクエストヘッダー](#request-headers-optional) を `application/x-www-form-url-encoded` に設定した場合、リクエストボディは URL エンコードされた文字列としてフォーマットする必要があります。以下に例を示します。

{% raw %}
```
to={{custom_attribute.${example}}}&text=Your+order+just+arrived
```
{% endraw %}

![URL エンコードされた文字列を含むリクエスト本文。]({% image_buster /assets/img_archive/webhook_rawtext_URL-encoded.png %})

## ステップ 3:追加設定を構成する

#### リクエストヘッダー (オプション)

特定のエンドポイントでは、リクエストにヘッダーを含める必要がある場合があります。作成画面の [**作成**] セクションで、ヘッダーを必要な数だけ追加できます。

![リクエストヘッダーの「許可」キーと「コンテンツタイプ」キーの例]({% image_buster /assets/img_archive/webhook_request_headers_example.png %})

一般的なリクエストヘッダーは`Content-Type`仕様 (XML や JSON など、本文に含まれるデータのタイプを示す) と、ベンダーやシステムに対する認証情報を含む認証ヘッダーです。 

コンテンツタイプの仕様にはキー`Content-Type`を使用する必要があります。一般的な値は`application/json`または`application/x-www-form-urlencoded`です。

認証ヘッダーでは、`Authorization` キーを使用する必要があります。一般的な値は、{% raw %} `Bearer {{YOUR_TOKEN}}` または `Basic {{YOUR_TOKEN}}` {% endraw %} です。ここで、`YOUR_TOKEN` はベンダーまたはシステムから提供された認証情報です。

## ステップ 4:メッセージのテスト送信

キャンペーンを公開する前に、Brazeはリクエストが正しくフォーマットされていることを確認するためにWebhookをテストすることを推奨します。

そのためには、**テスト**タブに切り替えてテストWebhookを送信します。Webhook は、ランダムなユーザー、特定ユーザー (外部ユーザー ID のメールアドレスを入力)、または選択した属性を持つカスタマイズされたユーザーとしてテストできます。  

テストWebhookを送信した後、応答メッセージが表示されるダイアログが表示されます。Webhook リクエストが失敗した場合は、エラーメッセージを参照して Webhook のトラブルシューティングに役立ててください。次の例は、無効な webhook URL を持つ webhook の応答を詳しく示しています。

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

次に、キャンペーンの残りの部分を構築します。Webhook を作成するためにツールを活用する方法の詳細については、以下のセクションを参照してください。

#### 配信スケジュールまたはトリガーを選択する

Webhook は、スケジュールされた時刻、アクション、または API トリガーに基づいて配信できます。詳細については、[キャンペーンのスケジューリング]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/)を参照してください。

アクションベースの配信では、キャンペーンの継続時間と [[サイレント時間]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours)] を設定することもできます。

このステップでは、配信コントロールを指定できます。例えば、ユーザーを[再有効化]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns)してキャンペーンを受信できるようにしたり、[フリークエンシーキャップ]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping)ルールを有効にしたりできます。

#### ターゲットとするユーザーを選択する

次に、セグメントやフィルターを選択して[ターゲットユーザー]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/)を絞り込み、オーディエンスを絞り込む必要があります。このステップでは、セグメントからより多くのオーディエンスを選択し、必要に応じてフィルターを使用してさらにセグメントを絞り込みます。セグメントのおおよその人数について現在の状態を示すスナップショットが自動的に表示されます。正確なセグメントメンバーシップは常にメッセージが送信される直前に計算されることに注意してください。

#### コンバージョンイベントを選択する

Braze では、キャンペーンを受信した後、ユーザーが指定のアクションや[コンバージョンイベント]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/)を実行する頻度を追跡できます。ユーザーが指定したアクションを実行した場合にコンバージョンがカウントされる期間は、最大 30 日間まで設定できます。

{% endtab %}

{% tab キャンバス %}

キャンバスコンポーネントが完成していない場合は、残りのセクションを完成させます。詳細については、キャンバスの残りの部分を構築する方法、多変量テストとインテリジェントセレクションを実装する方法などについては、キャンバスドキュメントの[キャンバスを構築する]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas)ステップを参照してください。

{% endtab %}
{% endtabs %}

## ステップ 6:レビューと展開

キャンペーンまたはキャンバスの最後の構築が完了したら、その詳細を確認し、テストしてから送信してください！

## 知っておくべきこと

### エラー、リトライロジック、タイムアウト

webhookはBrazeサーバーが外部エンドポイントにリクエストを送信することに依存しており、構文やその他のエラーが発生する可能性があります。Webhookエラーを回避するための最初のステップは、Webhookキャンペーンを構文エラーについてテストし、パーソナライズされた変数にデフォルト値があることを確認することです。ただし、期限切れの API キー、レート制限、予期しないサーバーエラーなどの問題が原因で、Webhook が失敗する場合があります。Webhook の送信に失敗した場合、エラーメッセージが[メッセージアクティビティログ][42]に記録されます。

この説明には、エラーが発生した時間、アプリ名、およびエラーメッセージが含まれています:

![Webhook エラーとメッセージ「現在のユーザーに関する情報を照会するには、アクティブなアクセストークンを使用する必要があります」。]({% image_buster /assets/img_archive/webhook-error.png %})

メッセージ本文がエラーの原因について十分に明確でない場合、使用しているAPIエンドポイントのドキュメントを確認する必要があります。これらは通常、エンドポイントが使用するエラーコードの説明と、それらが通常引き起こされる原因を提供します。

他のキャンペーンと同様に、BrazeはWebhookキャンペーンの配信とそれに伴うコンバージョンを追跡します。Webhook リクエストが送信されると、受信側のサーバーは、リクエストの処理内容を示す応答コードを返します。 

次の表は、サーバーが送信する可能性のあるさまざまな応答、それらがキャンペーン分析に与える影響、およびエラーの場合にBrazeがキャンペーンを再配信しようとするかどうかをまとめたものです。

| 応答コード | 受領済みとしてマークされましたか？ | 再試行? |
|---------------|-----------|----------|
| `20x` (成功)  | はい |   該当なし  |
| `30x` (リダイレクション）  | いいえ | いいえ |
| `408` (リクエストタイムアウト）  | いいえ | はい |
| `429` (レート制限）  | いいえ | はい |
| `Other 4XX` (クライアントエラー)  | いいえ | いいえ |
| `5XX` (サーバーエラー)   | いいえ | はい |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
`5XX` エラーの場合、Brazeは指数関数的バックオフを使用して、30分間に最大5回までWebhook送信を再試行する。その他のエラーについては、Brazeは最大24時間再試行を続ける。<br><br>各Webhookはタイムアウトするまでに90秒が許可されています。
{% endalert %}

### IP 許可リスト {#ip-allowlisting}

Braze から Webhook が送信されると、Braze サーバーは顧客またはサードパーティのサーバーにネットワークリクエストを行います。IP 許可リストを使用することで、Webhook リクエストが実際に Braze から送信されていることを確認し、セキュリティレイヤーを追加することができます。

Brazeは次のIPからwebhookを送信します。リストされる IP は、許可リストにオプトインされているすべての API キーに自動的かつダイナミックに追加されます。

{% alert important %}
Braze-to-Braze Webhook を作成していて、許可リストを使用している場合は、`127.0.0.1` を含む次のすべての IP を許可リストに追加する必要があります。
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

| インスタンス `EU-01` と `EU-02` の場合:  |
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

| インスタンス `US-08` の場合:  |
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

以下を参照してください。
* [Messenger]({{site.baseurl}}/partners/message_orchestration/additional_channels/instant_chat/messenger/)
* [Remerge]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/remerge)
* [Lob.com]({{site.baseurl}}/partners/message_orchestration/additional_channels/direct_mail/lob)
* その他多くの[テクノロジーパートナー]({{site.baseurl}}/partners/home/)


[15]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/
[16]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages
[17]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#additional-notes-and-best-practices
[18]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[19]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/
[42]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/message_activity_log_tab/
