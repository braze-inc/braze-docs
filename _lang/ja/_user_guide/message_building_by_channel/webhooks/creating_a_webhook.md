---
nav_title: ウェブフックの作成
article_title: ウェブフックの作成
page_order: 1
channel:
  - webhooks
description: "この参考記事では、Webhook を作成して設定する方法について説明します。"
search_rank: 2
---

# ウェブフックの作成

> Webhookキャンペーンを作成するか、マルチチャネルキャンペーンにWebhookを含めると、アプリ以外のアクションをトリガーできます。具体的には、[Webhook][14] を使用して他のシステムやアプリケーションにリアルタイムの情報を提供できます。 

ウェブフックを使用して Salesforce や Marketo などのシステムに情報を送信できます。Webhook を使用してバックエンドシステムに情報を送信することもできます。たとえば、顧客がカスタムイベントを一定回数実行した後に、プロモーションを顧客のアカウントにクレジットしたい場合があります。

ウェブフックとは何か、Braze でどのように使用できるかについて詳しく知りたい場合は、先に進む前に「[ウェブフックについて]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/)」をご覧ください。

## ステップ 1:メッセージを作成する場所を選択してください

メッセージをキャンペーンとキャンバスのどちらを使用して送信すべきかわからない?キャンペーンは単一のシンプルなメッセージキャンペーンに適していますが、キャンバスは複数段階のユーザージャーニーに適しています。

{% tabs %}
{% tab Campaign %}

**ステップ:**

1. [**メッセージング**] > [**キャンペーン**] に移動し、[<i class="fas fa-plus"></i>**キャンペーンを作成**] をクリックします。
{% alert note %}
[古いナビゲーションを使用している場合は]({{site.baseurl}}/navigation)、[**エンゲージメント**] に [**キャンペーン**] が表示されます。
{% endalert %}

{:start="2"}
2\.[**Webhook**] を選択するか、複数のチャネルをターゲットとするキャンペーンの場合は [**マルチチャネルキャンペーン**] を選択します。
3\.キャンペーンには明確で意味のある名前を付けてください。
4\.[[必要に応じてチームとタグを追加します]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/)]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/)。
   \* タグを使うと、キャンペーンを簡単に見つけてレポートを作成できます。たとえば、[レポートビルダーを使用する場合]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/)、特定のタグでフィルタリングできます。
5\.キャンペーンに必要な数だけバリエーションを追加して名前を付けてください。追加したバリアントごとに異なるWebhookテンプレートを選択できます。このトピックの詳細については、「[多変量分析と]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) A/B テスト」を参照してください。

{% alert tip %}
キャンペーン内のすべてのメッセージが類似または同じ内容になる場合は、バリエーションを追加する前にメッセージを作成してください。次に、「**バリエーションを追加**」**ドロップダウンから「バリアントからコピー**」を選択できます。
{% endalert %}

{% endtab %}
{% tab Canvas %}

**ステップ:**

1. [Canvas コンポーザーを使用して Canvas を作成します]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)。
2. キャンバスを設定したら、キャンバスビルダーにステップを追加します。ステップに明確で意味のある名前を付けてください。
3. [ステップスケジュールを選択し]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay)、必要に応じて遅延を指定します。
4. このステップでは、必要に応じてオーディエンスを絞り込んでください。セグメントを指定し、フィルターを追加して、このステップの受信者をさらに絞り込みます。後から、メッセージの送信時に、オーディエンスオプションがチェックされます。
5. [昇進行動を選択してください]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/)。
6. メッセージとペアリングしたい他のメッセージングチャネルを選択してください。

{% endtab %}
{% endtabs %}

## ステップ 2:ウェブフックを作成

Webhook をゼロから作成するか、既存のテンプレートのいずれかを使用するかを選択できます。次に、エディターの [**作成**] タブでウェブフックを作成します。

![Compose tab when creating a webhook in Braze]({% image_buster /assets/img_archive/webhook_compose.png %})

「**作成**」タブは以下のフィールドで構成されています。

#### 言語 {#internationalization}

[国際化は][16] URL とリクエスト本文でサポートされています。メッセージを国際化するには、「**言語を追加**」をクリックして必須フィールドに入力します。Liquidの該当箇所にテキストを入力できるように、コンテンツを書く前に言語を選択することをおすすめします。[利用可能な言語の一覧をご覧ください]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported)。

#### Webhook URL

ウェブフック URL または HTTP URL は、エンドポイントを指定します。エンドポイントは、Webhook でキャプチャした情報を送信する場所です。ベンダーに情報を送信する場合、ベンダーはこの URL を API ドキュメントに記載する必要があります。自社のシステムに情報を送信する場合は、開発チームまたはエンジニアリングチームに問い合わせて、正しい URL を使用していることを確認してください。 

Braze では、標準ポート `80` (HTTP) および `443` (HTTPS) を介して通信する URL のみを許可しています。

[Liquidを使用してウェブフックURLをパーソナライズできます。][15]特定のエンドポイントでは、ユーザーを特定したり、URL の一部としてユーザー固有の情報を提供したりする必要がある場合があります。Liquidを使用するときは、[URLに使用するユーザー固有の情報ごとにデフォルト値を必ず含めてください][19]。

#### リクエスト本文

リクエストボディは、指定した URL に送信される情報です。Webhook リクエストの本文を作成するには 2 つの方法があります。

##### JSON キーと値のペア

JSON キーと値のペアを使用すると、JSON 形式を必要とするエンドポイントへのリクエストを簡単に記述できます。この機能は、JSON リクエストを必要とするエンドポイントでのみ使用できます。たとえば、キーがの場合`message_body`、対応する値はになります`Your order just arrived!`。キーと値のペアを入力すると、コンポーザーがリクエストを JSON 構文で設定し、JSON リクエストのプレビューが自動的に表示されます。

![リクエスト本文を JSON キーと値のペアに設定] [21]

[Liquidを使用して][15]、ユーザー属性、[カスタム属性][17]、[またはイベントプロパティをリクエストに含めるなど][18]、キーと値のペアをパーソナライズできます。たとえば、顧客の名とメールアドレスをリクエストに含めることができます。[各属性にデフォルト値を含めることを忘れないでください][19]。

##### 生のテキスト

未加工テキストオプションを使用すると、任意の形式の本文を想定するエンドポイントへのリクエストを柔軟に記述できます。たとえば、この機能を使用して、リクエストが XML 形式であることを期待するエンドポイントへのリクエストを作成できます。[[Liquidを使用したパーソナライゼーションと国際化の両方が未加工テキストでサポートされています][16]][15]。

![リクエスト本文を未加工テキストに設定] [22]

`Content-Type`[リクエストヘッダーをに設定する場合`application/x-www-form-url-encoded`、リクエスト本文は](#request-headers-optional) URL でエンコードされた文字列としてフォーマットする必要があります。例えば:

{% raw %}
```
to={{custom_attribute.${example}}}&text=Your+order+just+arrived
```
{% endraw %}

![URL でエンコードされた文字列を含むリクエスト本文。] [23]

## ステップ 3:その他の設定を行う

#### リクエストヘッダー (オプション)

特定のエンドポイントでは、リクエストにヘッダーを含める必要がある場合があります。コンポーザーの「設定 (**Settings**)」セクションでは、ヘッダーをいくつでも追加できます。一般的なリクエストヘッダーは、`Content-Type`仕様 (XML や JSON など、本文にどのような種類のデータが含まれるのかを記述したもの) と、ベンダーまたはシステムの認証情報を含む認証ヘッダーです。 

コンテンツタイプの指定にはキーを使用する必要があります`Content-Type`。`application/json``application/x-www-form-urlencoded`一般的な値はまたはです。

認証ヘッダーはキーを使用する必要があります`Authorization`。一般的な値は、{% raw %}`Bearer {{YOUR_TOKEN}}``Basic {{YOUR_TOKEN}}`{% endraw %}`YOUR_TOKEN`ベンダーまたはシステムから提供された認証情報です。

#### HTTP メソッド

使用すべき [HTTP メソッドは]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/#methods)、情報を送信するエンドポイントによって異なります。ほとんどの場合、POST を使用します。

![コンポーザーの [設定] タブでリクエストヘッダと HTTP メソッドを指定] [26]

## ステップ 4: メッセージをテスト送信

キャンペーンを公開する前に、BrazeはWebhookをテストしてリクエストが適切にフォーマットされていることを確認することを推奨しています。

そのためには、[**テスト] タブに切り替えて、テスト** Webhook を送信します。Webhookは、ランダムユーザー、特定のユーザー（メールアドレスまたは外部ユーザーIDを入力）、または任意の属性を持つカスタマイズされたユーザーとしてテストできます。  

テスト Webhook を送信すると、応答メッセージを含むダイアログが表示されます。Webhook リクエストが失敗した場合は、エラーメッセージを参照して Webhook のトラブルシューティングに役立ててください。次の例では、ウェブフック URL が無効な Web フックの応答の詳細を示しています。

\`\`\`json
404 見つかりません

{
"error": {
"message": "Unrecognized request URL. Please see https://lob.com/docs or email us at support@lob.com.",
"status_code": 404
}
  }

\`\`\`

## ステップ 5: 残りのキャンペーンやキャンバスを作成

{% tabs %}
{% tab Campaign %}

次に、残りのキャンペーンを作成します。当社のツールを最大限に活用してウェブフックを構築する方法の詳細については、以下のセクションを参照してください。

#### 配送スケジュールまたはトリガーを選択

Webhook は、スケジュールされた時間、アクション、または API トリガーに基づいて配信できます。詳細については、「[キャンペーンのスケジュール]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/)」を参照してください。

アクションベースの配信では、[キャンペーンの期間と待機時間を設定することもできます]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours)。

このステップでは、[ユーザーにキャンペーンの再受領を許可したり]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns)、[フリークエンシーキャップルールを有効にするなどの配信制御を指定することもできます]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping)。

#### ターゲットにするユーザーを選択

次に、[セグメントまたはフィルターを選択してユーザーをターゲットにし]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/)、オーディエンスを絞り込む必要があります。このステップでは、セグメントからより多くのオーディエンスを選択し、必要に応じてフィルターを使用してそのセグメントをさらに絞り込みます。現在のおおよそのセグメント人口がどのようになっているかのスナップショットが自動的に表示されます。正確なセグメントメンバーシップは常にメッセージが送信される直前に計算されることに注意してください。

#### コンバージョンイベントを選択する

Brazeでは、キャンペーンを受け取った後、[ユーザーが特定のアクションやコンバージョンイベントを実行する頻度を追跡できます]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/)。ユーザーが指定したアクションを実行した場合にコンバージョンがカウントされる期間を最大 30 日間設定できます。

{% endtab %}

{% tab Canvas %}

まだ行っていない場合は、Canvasステップの残りのセクションを完了してください。Canvasの残りの部分を構築する方法、多変量分析テストやインテリジェントセレクションを実装する方法などの詳細については、[Canvasドキュメントの「キャンバスの構築]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas)」ステップを参照してください。

{% endtab %}
{% endtabs %}

## ステップ 6:確認とデプロイ

最後のキャンペーンやキャンバスの作成が終わったら、詳細を確認してテストし、送信しましょう！

## 知っておくべきこと

### エラー、リトライロジック、タイムアウト

Webhookは、Brazeサーバーが外部エンドポイントにリクエストを行うことに依存しているため、構文やその他のエラーが発生する可能性があります。Webhookエラーを回避するための最初のステップは、Webhookキャンペーンの構文エラーをテストし、パーソナライズされた変数にデフォルト値があることを確認することです。ただし、APIキーの期限切れ、レート制限、予期しないサーバーエラーなどの問題が原因で、Webhookが機能しなくなる可能性があります。Webhook が送信に失敗すると、エラーメッセージが [メッセージアクティビティログ] [42] に記録されます。

この説明には、エラーが発生した時刻、アプリ名、およびエラーメッセージが含まれています。

![「現在のユーザーに関する情報を照会するには、アクティブなアクセストークンを使用する必要があります」というメッセージが表示される Webhook エラー] [43]

メッセージ本文がエラーの原因について十分に明確でない場合は、使用している API エンドポイントのドキュメントを確認する必要があります。これらは通常、エンドポイントが使用するエラーコードとその一般的な原因の説明を提供します。

他のキャンペーンと同様に、BrazeはWebhookキャンペーンの配信とそれらから生じるコンバージョンを追跡します。Webhook リクエストが送信されると、受信サーバーはリクエストで何が起こったかを示す応答コードを返します。次の表は、サーバーが送信する可能性のあるさまざまな応答、それらがキャンペーン分析に与える影響、エラーが発生した場合に Braze がキャンペーンの再配信を試みるかどうかをまとめたものです。

| 応答コード | 受信済みとマークされていますか？| 再試行?|
|---------------|-----------|----------|
| 20倍 (成功) | はい | 該当なし |
| 30x (リダイレクト) | いいえ | いいえ |
| 408 (リクエストタイムアウト) | いいえ | はい |
| 429 (レート制限) | いいえ | はい |
| その他の 4xx (クライアントエラー) | いいえ | いいえ |
| 5xx (サーバーエラー) | いいえ | はい |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

再試行すると、Brazeは指数バックオフを使用して約30分間5回試行した後、個々のWebhook呼び出しを中止します。

各 Webhook は、タイムアウトの 90 秒前に許可されます。

### IP 許可リスト {#ip-allowlisting}

BrazeからWebhookが送信されると、Brazeサーバーはお客様または第三者のサーバーにネットワークリクエストを送信します。IP許可リストを使用すると、Webhooksリクエストが実際にBrazeから送信されていることを確認でき、セキュリティがさらに強化されます。

Braze は次の IP アドレスからウェブフックを送信します。リストされている IP は、許可リストにオプトインされているすべての API キーに自動的かつ動的に追加されます。

{% alert important %}
Braze to Braze のウェブフックを作成して許可リストに登録する場合は、以下を含むすべての IP を許可リストに登録する必要があります。`127.0.0.1`
{% endalert %}

| インスタンスの場合`US-01`、`US-02`、`US-03``US-04`、`US-05`、`US-06`、および`US-07`:|
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

| `EU-01` インスタンスと`EU-02`:|
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

| 例えば`US-08`:|
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

### Braze パートナーとのウェブフックの使用 {#utilizing-webhooks}

Webhook を利用する方法は多数ありますが、当社のテクノロジーパートナー (Alloys) では、Webhook を使用して顧客やユーザーとの直接的なコミュニケーションを強化できます。

チェックアウト:
* [メッセンジャー]({{site.baseurl}}/partners/additional_channels/instant_chat/messenger/)
* [リマージ]({{site.baseurl}}/partners/advertising_technologies/retargeting/remerge/)
* [Lob.com]({{site.baseurl}}/partners/additional_channels/direct_mail/lob/)
\* そして、[さらに多くのテクノロジーパートナー]({{site.baseurl}}/partners/home/)！

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
