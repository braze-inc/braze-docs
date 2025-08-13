---
nav_title: Webhook について
article_title: Webhook について
page_order: 0
channel:
  - webhooks
description: "このリファレンス記事では、一般的なユースケース、Webhook の構造、Braze での使用方法など、Webhook の基本について説明します。"

---

# [![Braze ラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/understanding-webhooks){: style="float:right;width:120px;border:0;" class="noimgborder"}Webhook について

> このリファレンス記事では、Webhook の基礎を説明し、独自に作成する必要のある構成要素を示します。BrazeでWebhookを作成する手順をお探し？[ウェブフックの作成]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)」を参照のこと。

Webhook は、アプリケーションがリアルタイムでデータを共有するための一般的な通信方法です。今の時代、1つのスタンドアローン・アプリケーションですべてをこなせることはほとんどない。ほとんどの場合、特定のタスクを実行するために特化した多くの異なるアプリやシステムで作業しており、これらのアプリはすべて互いに通信できる必要がある。そこでウェブフックの出番だ。

ウェブフックとは、ある基準が満たされた後に、あるシステムから別のシステムへ自動送信されるメッセージのことである。Brazeでは、この基準は通常、カスタムイベントのトリガーとなる。

根本的に、Webhook は 2 つの個別システムがリアルタイムで送信されるデータに基づいて効果的なアクションを実行するための、イベントベースの方法です。そのメッセージには、特定のタスクをいつ、どのように実行するかを受信側システムに伝える指示が含まれています。そのため、Webhook を使用すると、データおよびプログラム機能へのよりダイナミックで柔軟なアクセスが可能になり、プロセスを合理化するカスタマージャーニーを設定できます。

## ユースケース

Webhook は、複数のシステムを接続するための優れた方法です。結局、Webhook はアプリの通信方法です。ウェブフックが特に役立つ一般的なシナリオをいくつか紹介しよう：

- Braze とデータを送受信する
- Brazeが直接サポートしていないチャネル経由で顧客にメッセージを送信する
- Braze APIに投稿する

より具体的な使用例としては、以下のようなものがある：

- ユーザーがメール配信を停止した場合、WebhookでアナリティクスデータベースやCRMに同じ情報を更新させることができ、ユーザーの行動を全体的に把握することができる。
- FacebookメッセンジャーやLINE内でユーザーに[トランザクションメッセージを]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign/)送信する。
- Webhook を使用して[Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob/) などのサードパーティサービスと通信し、アプリ内および Web のアクティビティに応じて顧客にダイレクトメールを送信する。
- ゲーマーのレベルが一定に達したり、ポイントが一定数に達したら、ウェブフックと既存のAPIセットアップを使って、キャラクターのアップグレードやコインを直接アカウントに送る。マルチチャネルメッセージングキャンペーンの一環として Webhook を送信する場合は、プッシュ通知やその他のメッセージを送信して、同時にゲーマーに報酬を通知できる。
- もしあなたが航空会社なら、ウェブフックと既存のAPIセットアップを利用して、顧客が一定数のフライトを予約した後、顧客のアカウントに割引をクレジットすることができる。
- 無限の "If This Then That"[（IFTTT](https://ifttt.com/about)）レシピ-例えば、顧客がEメールでアプリにサインインすると、そのアドレスが自動的にSalesforceに設定される。

## ウェブフックの構造

Webhookを構成する要素を以下に示します。

| Webhookの一部 | 説明 |
| --- | --- |
| [HTTP メソッド](#methods) | API と同様に、Webhook にはリクエストメソッドが必要です。これらは、ウェブフックがヒットするURLに与えられ、与えられた情報で何をすべきかをエンドポイントに伝える。指定できるHTTPメソッドは4つある：POST、GET、PUT、および DELETE。 |
| HTTP URL | ウェブフック・エンドポイントのURLアドレス。エンドポイントは、Webhook でキャプチャしている情報の送信先にする場所です。 |
| Request body | Webhookのこの部分には、エンドポイントに伝える情報が含まれている。リクエスト本文には、JSON キーと値のペア、または生のテキストを使用できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![HTTP メソッド、HTTP URL、リクエストボディを含む Webhook の例]({% image_buster /assets/img_archive/webhook_anatomy.png %})

### HTTPメソッド {#methods}

次の表は、Webhookで指定できる4つの異なるHTTPメソッドについて説明している。

| HTTPメソッド | 説明 |
| ----------- | ----------- |
| POST | このメソッドは、受信サーバーに新しい情報を書き込む。実際のアプリケーションでPOSTメソッドを使う一般的な例としては、ウェブサイトの[問い合わせフォームが](https://www.braze.com/company/contact)ある。フォームに入力した情報はすべてリクエストボディの一部となり、レシーバーに送信される。これはデータを送信する際に最もよく使われる方法である。
| GET | このメソッドは、新しい情報を書き込むのではなく、既存の情報を取得します。定義上、GETリクエストはリクエストボディをサポートしない。これは、サーバーにデータを要求するときに使われる最も一般的な方法である。例えば、[`/segments/list` エンドポイント]({{site.baseurl}}/api/endpoints/export/segments/get_segment/).があるとします。GETリクエストをすると、セグメントのリストが返される。
| PUT: | このメソッドはエンドポイントの情報を更新し、既存の情報をリクエストボディの内容に置き換えます。 
| 削除 | このメソッドはHTTP URLのリソースを削除する。 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## BrazeのWebhooks

Braze では、Webhook を、Webhook キャンペーン、API キャンペーン、またはキャンバスコンポーネントとして作成できます。

{% tabs %}
{% tab Webhook キャンペーン %}

1. Braze ダッシュボードの [**キャンペーン**] に移動します。
2. [**キャンペーンを作成**] をクリックし、[**Webhook**] を選択します。

詳細については、[Webhook の作成]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)を参照してください。

{% endtab %}
{% tab APIキャンペーン %}

1. Braze ダッシュボードの [**キャンペーン**] に移動します。
2. [**キャンペーンを作成**] をクリックし、[**API キャンペーン**] を選択します。
3. [**メッセージを追加**] をクリックし、[**Webhook**] を選択します。
4. [Webhookオブジェクト]({{site.baseurl}}/api/objects_filters/messaging/webhook_object/)を含むように API 呼び出しをフォーマットします。

詳細については、[「Webhook の作成」]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)を参照してください。

{% endtab %}
{% tab キャンバスコンポーネント %}

1. キャンバスで、新しいコンポーネントを作成します。
2. コンポーネントの [**メッセージ**] セクションで、[**Webhook**] を選択します。

詳細については、[「Webhook の作成」]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)を参照してください。

{% endtab %}
{% endtabs %}

## Webhook のエラー処理とレート制限

Braze は、Webhook コールからのエラー応答を受信すると、以下の応答ヘッダーに基づいて Webhook の送信動作を自動的に調整します。

- `Retry-After`
- `X-Rate-Limit-Limit`
- `X-Rate-Limit-Remaining`
- `X-Rate-Limit-Reset`

これらのヘッダーは、レート制限を解釈し、それに応じて送信速度を調整し、今後エラーが発生しないようにするうえで役立ちます。また、再試行には指数バックオフ戦略を採用しており、再試行の間隔を広げることでサーバーに負荷がかかるリスクを軽減できます。

特定のホストへの Webhook リクエストの大部分が失敗していることが検出された場合には、そのホストへのすべての送信試行を一時的に延期します。その後、定義されているクールダウン期間を経過したら送信を再開し、システムを回復させます。


