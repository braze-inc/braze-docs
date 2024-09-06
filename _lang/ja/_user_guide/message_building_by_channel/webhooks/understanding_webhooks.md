---
nav_title: ウェブフックについて
article_title: ウェブフックについて
page_order: 0
channel:
  - webhooks
description: "このリファレンス記事では、一般的な使用例、Webhookの解剖学、Brazeでの使用方法など、Webhookの基本をカバーしている。"

---

# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/understanding-webhooks){: style="float:right;width:120px;border:0;" class="noimgborder"}webhookについて

> このリファレンス記事では、Webhookの基本をカバーし、独自のWebhookを作成するために必要な構成要素を提供する。BrazeでWebhookを作成する手順をお探し？[ウェブフックの作成][1]」を参照のこと。

Webhookは、アプリケーションがリアルタイムでデータを共有するための一般的な通信手段だ。今の時代、1つのスタンドアローン・アプリケーションですべてをこなせることはほとんどない。ほとんどの場合、特定のタスクを実行するために特化した多くの異なるアプリやシステムで作業しており、これらのアプリはすべて互いに通信できる必要がある。そこでウェブフックの出番だ。

ウェブフックとは、ある基準が満たされた後に、あるシステムから別のシステムへ自動送信されるメッセージのことである。Brazeでは、この基準は通常、カスタムイベントのトリガーとなる。

Webhookは、リアルタイムで送信されるデータに基づいて、2つの別々のシステムが効果的なアクションを起こすためのイベントベースの手法である。そのメッセージには、いつ、どのように特定のタスクを実行するかを受信システムに伝える指示が含まれている。このため、Webhookはデータやプログラム機能によりダイナミックで柔軟なアクセスを提供し、プロセスを合理化するカスタマージャーニーの設定を可能にする。

## ユースケース

Webhookはシステム同士を接続する優れた方法である-結局のところ、Webhookはアプリが通信する方法なのだ。ウェブフックが特に役立つ一般的なシナリオをいくつか紹介しよう：

- Brazeとデータを送受信する
- Brazeが直接サポートしていないチャネル経由で顧客にメッセージを送信する
- Braze APIに投稿する

より具体的な使用例としては、以下のようなものがある：

- ユーザーがメール配信を停止した場合、WebhookでアナリティクスデータベースやCRMに同じ情報を更新させることができ、ユーザーの行動を全体的に把握することができる。
- FacebookメッセンジャーやLINE内でユーザーに[トランザクションメッセージを]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign/)送信する。
- Webhooksを使用して、以下のようなサードパーティ・サービスと通信することで、アプリ内やWebでのアクティビティに応じて顧客にダイレクトメールを送信する。 [Lob.com]({{site.baseurl}}/partners/message_orchestration/additional_channels/direct_mail/lob/).
- ゲーマーのレベルが一定に達したり、ポイントが一定数に達したら、ウェブフックと既存のAPIセットアップを使って、キャラクターのアップグレードやコインを直接アカウントに送る。マルチチャネル・メッセージング・キャンペーンの一環としてウェブフックを送信する場合、プッシュやその他のメッセージを送信して、ゲーマーに報酬を同時に知らせることができる。
- もしあなたが航空会社なら、ウェブフックと既存のAPIセットアップを利用して、顧客が一定数のフライトを予約した後、顧客のアカウントに割引をクレジットすることができる。
- 無限の "If This Then That"[（IFTTT](https://ifttt.com/about)）レシピ-例えば、顧客がEメールでアプリにサインインすると、そのアドレスが自動的にSalesforceに設定される。

## ウェブフックの構造

ウェブフックは以下の3つの部分から構成される：

![HTTPメソッド、HTTP URL、リクエスト・ボディに分割されたウェブフックの例。詳細は以下の表を参照のこと。][2]

| Webhookの一部 | 説明 |
| --- | --- |
| [HTTPメソッド](#methods) | APIと同様に、ウェブフックにはリクエスト・メソッドが必要だ。これらは、ウェブフックがヒットするURLに与えられ、与えられた情報で何をすべきかをエンドポイントに伝える。指定できるHTTPメソッドは4つある：POST、GET、PUT、DELETEである。 |
| HTTP URL | ウェブフック・エンドポイントのURLアドレス。エンドポイントは、ウェブフックに取り込んだ情報を送信する場所だ。 |
| Request body | Webhookのこの部分には、エンドポイントに伝える情報が含まれている。リクエスト・ボディはJSONキー・バリュー・ペアか生のテキストである。 |
{: .reset-td-br-1 .reset-td-br-2}

### HTTPメソッド {#methods}

次の表は、Webhookで指定できる4つの異なるHTTPメソッドについて説明している。

| HTTPメソッド | 説明 |
| ----------- | ----------- |
| POST | このメソッドは、受信サーバーに新しい情報を書き込む。実際のアプリケーションでPOSTメソッドを使う一般的な例としては、ウェブサイトの[問い合わせフォームが](https://www.braze.com/company/contact)ある。フォームに入力した情報はすべてリクエストボディの一部となり、レシーバーに送信される。これはデータを送信する際に最もよく使われる方法である。
| GET | この方法は、新しい情報を書き込むのではなく、既存の情報を検索する。これは、サーバーにデータを要求するときに使われる最も一般的な方法である。例えば、[`/segments/list` ]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) 。GETリクエストをすると、セグメントのリストが返される。
| プット | このメソッドは、エンドポイント上の情報を更新し、既存の情報をリクエスト・ボディの内容と置き換える。 
| 削除 | このメソッドはHTTP URLのリソースを削除する。 
{: .reset-td-br-1 .reset-td-br-2}

## BrazeのWebhooks

Brazeでは、Webhookキャンペーン、APIキャンペーン、またはCanvasコンポーネントとしてWebhookを作成できる。

{% tabs %}
{% tab ウェブフックキャンペーン %}

1. Brazeのダッシュボードで、**Campaignsに**行く。
2. **Create Campaignを**クリックし、**Webhookを**選択する。

詳しくは[ウェブフックの]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)作成を参照のこと。

{% endtab %}
{% tab APIキャンペーン %}

1. Brazeのダッシュボードで、**Campaignsに**行く。
2. **Create Campaignを**クリックし、**API Campaignを**選択する。
3. **Add Messagesを**クリックし、**Webhookを**選択する。
4. [Webhookオブジェクトを]({{site.baseurl}}/api/objects_filters/messaging/webhook_object/)含むようにAPIコールをフォーマットする。

詳しくは[ウェブフックの]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)作成を参照のこと。

{% endtab %}
{% tab キャンバス・コンポーネント %}

1. キャンバスで、新しいコンポーネントを作成する。
2. コンポーネントの**Message**セクションで、**Webhookを**選択する。

詳しくは[ウェブフックの]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)作成を参照のこと。

{% endtab %}
{% endtabs %}


[1]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
[2]: {% image_buster /assets/img_archive/webhook_anatomy.png %}
