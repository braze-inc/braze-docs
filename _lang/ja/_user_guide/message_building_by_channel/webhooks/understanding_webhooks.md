---
nav_title: ウェブフックについて
article_title: ウェブフックについて
page_order: 0
channel:
  - webhooks
description: "この参考記事では、一般的なユースケース、ウェブフックの構造、Braze での使用方法など、ウェブフックの基本について説明しています。"

---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/understanding-webhooks){: style="float:right;width:120px;border:0;" class="noimgborder"}ウェブフックについて

> この参考記事では、ウェブフックの基本について説明し、独自のウェブフックを作成するために必要なビルディングブロックについて説明しています。Braze でウェブフックを作成する手順をお探しですか？「[ウェブフックの作成」][1] を参照してください。

Webhook は、アプリケーションがリアルタイムでデータを共有するための一般的な通信手段です。今日では、すべてを実行できるスタンドアロンアプリケーションはほとんどありません。ほとんどの場合、特定のタスクの実行に特化したさまざまなアプリやシステムで作業していますが、これらのアプリはすべて相互に通信できる必要があります。そこでウェブフックの出番です。

ウェブフックは、特定の基準が満たされた後に、あるシステムから別のシステムへの自動メッセージです。Braze では、通常、この基準によってカスタムイベントがトリガーされます。

基本的に、Webhookは、2つの別々のシステムがリアルタイムで送信されるデータに基づいて効果的なアクションを実行するためのイベントベースの方法です。このメッセージには、特定のタスクをいつ、どのように実行するかを受信システムに伝える指示が含まれています。そのため、Webhook を使用すると、データやプログラム機能へのより動的で柔軟なアクセスが可能になり、プロセスを合理化するカスタマージャーニーを設定できるようになります。

## ユースケース

Webhook はシステムを相互に接続するための優れた方法です。結局のところ、Webhook はアプリの通信手段です。Webhook が特に役立つ一般的なシナリオは次のとおりです。

- Braze へのデータ送信と Braze からのデータ送信
- Braze が直接サポートしていないチャネルを経由して顧客にメッセージを送信
- Braze API への投稿

より具体的なユースケースには、次のようなものがあります。

- ユーザーがメールの購読を解除した場合、Webhookに同じ情報で分析データベースまたはCRMを更新してもらい、そのユーザーの行動を全体的に把握できるようにすることができます。
- Facebook メッセンジャーまたは Line [内のユーザーにトランザクションメッセージを送信します]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign/)。
- [ウェブフックを使用してLOB.comなどのサードパーティサービスと通信することで、アプリ内アクティビティやウェブアクティビティに応じて顧客にダイレクトメールを送信します。]({{site.baseurl}}/partners/message_orchestration/additional_channels/direct_mail/lob/)
- ゲーマーが特定のレベルに達したり、特定のポイント数を獲得したりした場合は、Webhookと既存のAPI設定を使用して、キャラクターのアップグレードまたはコインをアカウントに直接送信します。マルチチャネルメッセージングキャンペーンの一環としてウェブフックを送信する場合、プッシュメッセージやその他のメッセージを送信して、同時にゲーマーに報酬について知らせることができます。
- 航空会社の場合は、Webhook と既存の API 設定を使用して、顧客が一定数のフライトを予約した後に、顧客のアカウントに割引を付与できます。
- 「If This Then That」([IFTTT](https://ifttt.com/about)) レシピは無限にあります。たとえば、顧客がメールでアプリケーションにログインした場合、そのアドレスを自動的に Salesforce に設定できます。

## ウェブフックの構造

ウェブフックは次の 3 つの部分で構成されています。

![例:ウェブフックは HTTP メソッド、HTTP URL、およびリクエストボディに分かれています。詳細については、次の表を参照してください。] [2]

| ウェブフックの一部 | 説明 |
| --- | --- |
| [HTTP メソッド](#methods) | API と同様に、ウェブフックにはリクエストメソッドが必要です。これらはWebhookがヒットしたURLに渡され、与えられた情報をどう処理するかをエンドポイントに指示します。指定できる HTTP メソッドは 4 つあります。投稿、取得、入力、削除。|
| HTTP URL | ウェブフックエンドポイントの URL アドレス。エンドポイントは、Webhook でキャプチャした情報を送信する場所です。|
| リクエストボディ | Webフックのこの部分には、エンドポイントに通信している情報が含まれています。リクエスト本文は JSON のキーと値のペアでも、未加工のテキストでもかまいません。|
{: .reset-td-br-1 .reset-td-br-2}

### HTTP メソッド {#methods}

次の表では、Webhook で指定できる 4 種類の HTTP メソッドについて説明します。

| HTTP メソッド | 説明 |
| ----------- | ----------- |
| POST | このメソッドは、受信サーバーに新しい情報を書き込みます。実際のアプリケーションでの POST メソッドの一般的な例は、Web [サイトのコンタクトフォームです](https://www.braze.com/company/contact)。フォームに入力した情報はすべてリクエストボディの一部となり、受信者に送信されます。これは、データを送信するときに使用される最も一般的な方法です。
| GET | このメソッドは、新しい情報を書き込むのではなく、既存の情報を取得します。これは、サーバーからデータを要求するときに使用される最も一般的な方法です。[`/segments/list`エンドポイントを例にとってみましょう]({{site.baseurl}}/api/endpoints/export/segments/get_segment/)。GET リクエストを行うと、セグメントのリストが返されます。
| PUT | このメソッドは、エンドポイントの情報を更新し、既存の情報をリクエスト本文の内容に置き換えます。
| 削除 | このメソッドは、HTTP URL内のリソースを削除します。
{: .reset-td-br-1 .reset-td-br-2}

## Braze のウェブフック

Braze では、ウェブフックをウェブフックキャンペーン、API キャンペーン、または Canvas コンポーネントとして作成できます。

{% tabs %}
{% tab Webhook Campaign %}

1. Braze 管理画面で [**キャンペーン**] に移動します。
2. 「**キャンペーンを作成**」をクリックし、「**Webhook**」を選択します。

詳細については、「[Webhook の作成]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)」を参照してください。

{% endtab %}
{% tab API Campaign %}

1. Braze 管理画面で [**キャンペーン**] に移動します。
2. 「**キャンペーンを作成**」をクリックし、「**API キャンペーン**」を選択します。
3. [**メッセージを追加**] をクリックし、[**Webhook**] を選択します。
4. [Webhook オブジェクトを含むように]({{site.baseurl}}/api/objects_filters/messaging/webhook_object/) API 呼び出しをフォーマットします。

詳細については、「[Webhook の作成]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)」を参照してください。

{% endtab %}
{% tab Canvas Component %}

1. キャンバスで、新しいコンポーネントを作成します。
2. コンポーネントの「**メッセージ**」セクションで、「**Webhook**」を選択します。

詳細については、「[Webhook の作成]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)」を参照してください。

{% endtab %}
{% endtabs %}


[1]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
[2]: {% image_buster /assets/img_archive/webhook_anatomy.png %}
