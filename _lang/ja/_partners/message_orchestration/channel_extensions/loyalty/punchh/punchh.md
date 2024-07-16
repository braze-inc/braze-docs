---
nav_title: Punchh
article_title:Punchh
page_order:1
description:"この参考記事では、ロイヤルティとエンゲージメントのプラットフォームであるBrazeとPunchhのパートナーシップについて概説しており、2つのプラットフォーム間でデータを同期することができる。Brazeで公開されたデータはセグメンテーションに利用でき、Brazeで設定したWebhookテンプレートを介してユーザーデータをPunchhに同期することができる。"
page_type: partner
search_tag:Partner

---

# Punchh

> [Punchhは](https://punchh.com/)業界をリードするロイヤルティとエンゲージメントのプラットフォームで、ブランドは店舗とデジタルの両方でオムニチャネルの顧客ロイヤルティプログラムを提供することができる。 

BrazeとPunchhの統合により、2つのプラットフォーム間でギフトやロイヤルティ目的のデータを同期することができる。Brazeで公開されたデータはセグメンテーションに利用でき、BrazeのWebhook経由でユーザーデータをPunchhに同期することができる。

## メリットは何でしょうか。

- ロイヤルティデータをPunchhからBrazeにリアルタイムで取り込む。 
- Brazeのパワフルなオーディエンスデータを活用し、レイヤー化することで、意味のあるダイナミックなクロスチャネルエクスペリエンスを提供（アプリ、モバイル、Web、メール、SMS）。
  - 顧客はメールを開封したか？顧客は店舗の近くでアプリを開封したか？
- Brazeを通じて送信されるトランザクションメールのルック＆フィールを標準化する。
- ABテストや最適化が可能なジャーニーを作成する。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| パンチアカウント | このパートナーシップを利用するには、アクティブなPunchhアカウントが必要だ。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これはダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント | \[あなたの REST エンドポイント URL][6].エンドポイントはインスタンスのBraze URLに依存する。 |
{: .reset-td-br-1 .reset-td-br-2}

## 他に知っておくべきことは？

#### 統合の前に

- Brazeとの統合を利用する場合、PunchhとBrazeの2つのキャンペーンが必要になる。例えば、オファーが添付されたキャンペーンを送信する場合、ギフトキャンペーンはPunchh内で設定され、通知はBrazeから送信できる。
- ゲストはすでにパンチとBrazeに存在しているはずだ。Punchhはまだロイヤルティを持っていない顧客をフィルターにかける。

#### 重要な注意事項

- Punchhは、デフォルトユーザー属性のBrazeへの送信を無効にする機能を追加し、顧客はデータポイント超過料金が発生しないようにした。これはアダプターのセットアップ時に設定する。
- 定期的なキャンペーンでセグメンテーションを使用する場合、IDはキャンペーンが実行されるたびに変更されるため、キャンペーンIDの代わりにキャンペーン名を使用する必要がある。
- Punchhの各ギフトキャンペーンで利用可能なコミュニケーションチャネルには、リッチメッセージ、プッシュ通知、SMS、メールなどがある。
- ユーザーがBrazeからPunchhカスタムセグメンテーションに送られた後、削除することはできない。既存のセグメンテーションに追加できるのは、新しい顧客のみである。既存のPunchhカスタムセグメントから顧客を削除する必要がある場合、Brazeで新しいWebhookキャンペーンを作成し、ユーザーを新しいPunchhカスタムセグメントに送信する必要がある。

## 統合

Punchhは、Braze顧客が以下のPunchh APIエンドポイントを使用してPunchhプラットフォームに外部IDを追加するのに役立つエンドポイントをいくつか提供している。外部IDが追加されたら、Punchhでアダプターを作成し、Braze認証情報を入力し、同期したいイベントを選択する。次に、PunchhセグメントIDを取得し、それを使用してPunchh webhookを構築し、カスタマージャーニーで顧客の同期をトリガーすることができる。

Punchh`user_id` 、Brazeユーザープロファイルにカスタム属性 "punchh_user_id "として追加する必要がある。同様に、Brazeで使用している`external_id` 、Punchhユーザープロファイルの`external_source_id` フィールドとして含める必要がある。 

### ステップ1:外部IDインジェスト・エンドポイントの設定

Brazeからの外部IDは、新規および既存のPunchユーザーに対して、以下のエンドポイントを使用して追加することができる。

{% alert important %}
`external_source` 、`external_source_id` のフィールド値は、Punchhに固有のものでなければならず、既存のプロファイルと関連付けられてはならない。
{% endalert %}

1. 新しいPunchhユーザー<br>
Punchhのサインアップエンドポイントで、`external_source` と`external_source_id` フィールドを使用して、Punchhに新規ユーザーを作成する。Punchhでは、以下のサインアップエンドポイントのいずれかを介して、ユーザープロファイルと共に外部識別子を送信することができる：
- [モバイル登録API](https://developers.punchh.com/docs/dev-portal-mobile/2e67abf6f8e12-sign-up-register)
- [SSOサインアップAPI](https://developers.punchh.com/docs/dev-portal-online-ordering/58f18dfdd2a3d-signup-with-email-and-password)<br><br>
2. 既存のパンチ・ユーザー <br>
既存のPunchhユーザー向けに`external_source_id` を更新。Punchhでは、ユーザーAPIの更新エンドポイントを介して、外部識別子をプロファイルに追加することができる： 
- [モバイルユーザー更新](https://developers.punchh.com/docs/dev-portal-mobile/c9b928e35a6f3-update-user-profile)
- [SSOユーザー更新](https://developers.punchh.com/docs/dev-portal-online-ordering/eef4eef6c97a0-update-user-information)
- [ダッシュボードユーザー更新](https://developers.punchh.com/docs/dev-portal-platform-functions/6351feaf591aa-update-a-user)
<br><br>
{% tabs local %}
{% tab User sign-up API example %}
この例では、サインアップ時にユーザープロファイルとともに外部識別子を送信することができる。これは、`external_source` を "customer_id"、`external_source_id` を "1111111111111111 "として文字列データ型として送信することで行われる。

```json
curl --location --request POST 'https://server_name_goes_here.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'x-pch-digest: SIGNATURE' \
--header 'Accept-Timezone: Etc/UTC' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--data-raw '{
    "client":"CLIENT",
    "user" : {
      "email": "test@example.com",
      "password": "PASSWORD",
      "first_name":"FIRST_NAME",
      "last_name":"LAST_NAME",
      "terms_and_conditions":"true",
      "anniversary":"2014-02-02",
      "zip_code":"94497",
      "birthday":"2004-02-02",
      "external_source":"customer_id",
      "external_source_id":"111111111111111111"
      }
}'
```
{% endtab %}
{% tab User update API example %}
この例では、ユーザープロファイルで外部識別子を更新することができる。これは、`external_source` を "customer_id"、`external_source_id` を "1111111111111111 "として文字列データ型として送信することで行われる。

```json
curl --location --request PUT 'https://server_name_goes_here.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--header 'x-pch-digest: SIGNATURE' \
--header 'Authorization: Bearer ACCESS_TOKEN' \
--data-raw '{
    "client":"CLIENT",
    "user": {
        "external_source":"customer_id",
        "external_source_id":"111111111111111111"
    }
}'
```
{% endtab %}
{% endtabs %}

{% alert note %}
**プラットフォーム構成：**Punchhで外部識別子をイネーブルメントにするには、Punchhのダッシュボードから、**Cockpit**> Dashboard > External**User Identifierに**移動する。
{% endalert %}

### ステップ2:パンチでBrazeアダプターをセットアップする

#### 同期可能なイベント {#available-events-to-sync}

1. **Guest:** サインアップ、ゲストプロファイルの更新、非アクティブ化、削除時にトリガーされる。
2. **ロイヤルティ・チェックイン：**ロイヤルティ取引やレシートのバーコードをスキャンすることでトリガーされる。
3. **ギフト・チェックイン：**キャンペーンでプレゼントされたポイントにトリガーがかかる
4. **Redemption:** Punchhクーポンを除く報酬の引き換えの場合、発行と引き換えを含むクーポンイベントとして別途送信されるため、トリガーされる。
5. **Rewards:** キャンペーン、アクティビティ、ポイントから報酬へのコンバージョン、または管理者による報酬贈与からトリガーされる。
6. **取引通知：**パンチシステム内でユーザーがトランザクションを行った際にトリガーされる（例：ポイント失効）。
7. **マーケター通知：**ユーザーのセグメンテーションに関連するPunchhのさまざまなキャンペーン設定に基づいてトリガーされる。

{% alert note %}
これらの利用可能なイベントのペイロードのサンプルについては、Punchhのドキュメントを参照のこと。
{% endalert %}

このアダプターの設定については、Punchhのインプリメンテーション・マネージャーと相談してほしい。

BrazeとPunchhの統合を設定するには、以下のようにする：

1. Punchhのダッシュボードで、**Cockpit**>**Dashboard**>**Major Features**>**Enable Webhook**Managementに移動し、**Enable Webhook** Managementをオンに切り替える。<br><br>
2. 次に、**設定の**管理 >**Webhooksマネージャー**>**設定**>**アダプタを表示** **タブに**移動して、アダプタをイネーブルメントにする。<br><br>
3. **設定]**タブから**Webhooks**マネージャーに移動し、\[**アダプタ]**タブを選択し、\[**アダプタの作成**]をクリックする。<br><br>![][1]<br><br>
4. アダプタ名、説明、管理者のメールを入力する。アダプターとして**Brazeを**選択し、Braze REST APIエンドポイントとBraze APIキーを指定する。<br><br>
5. 次に、イネーブルメントにしたいイベントを選択する。これらのイベントのリストは、「[同期可能なイベント](#available-events-to-sync)」で確認できる。<br><br>![][3]<br><br>
6. **Submitを**クリックしてWebhookをイネーブルメントにする。

## BrazeでPunchh webhookを作成する

Brazeは、Punchhカスタムセグメントを利用したWebhookを通じて、ユーザーをPunchhセグメントに追加することができる。

1. Punchhでカスタムセグメントを作成し、以下のようにPunchhセグメントダッシュボードのURLに`custom_segment_id` 。クラシック・セグメンテーション・ビルダーもベータ・セグメンテーション・ビルダーも使用できる。しかし、クラシックはいずれ非推奨となるため、ベータ版を推奨する。<br><br>Punchhプラットフォームで、**Guest**>**Segment**>**Custom List**>**New Custom List**に移動する。<br><br>![][8]<br><br>

2. ユーザーをカスタムセグメンテーションに追加するためのPunchhエンドポイントをWebhook URLとして、BrazeでWebhookキャンペーンを作成する。ここでは、URLから引き出された`custom_segment_id` 、`user_id` 、キーと値のペアとして提供することができる。<br><br>![][4]<br><br>

3. このWebhookは、Singularキャンペーンとして、またはキャンバス内のステップとして設定することができる。また、ユーザーをこの特定のPunchhセグメンテーションに追加するWebhookが複数のキャンペーンやキャンバスで使用される場合は、[テンプレートとして]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template#creating-a-webhook-template)設定することもできる。<br><br>
Webhook 内の`user_id` キーが Punchh ユーザー ID に対応する。この識別子は、ユーザーをPunchhカスタムセグメントに追加するためにBrazeで作成されるすべてのWebhookに追加する必要がある。`punch_user_id` カスタム属性は、[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#pre-formatted-variables) を使って`user_id` キーの値としてダイナミックな入力をすることができる。カスタム属性変数`punchh_user_id` は、テンプレート化されたテキストフィールドの右上にある青い「プラス」アイコンを使って挿入できる。<br><br>![][10]{: style="max-width:65%;"}<br><br>![][11]{: style="max-width:65%;"}<br><br>

4. Webhookが保存されると、以下のようにユーザーを同期するために使用することができる。例えば、このBraze webhookキャンペーンが開始されると、136人の顧客がPunchカスタムセグメンテーションに追加される。<br><br>![BrazeとPunchhの統合により保存されたWebhookを使用してユーザーを同期する例。][7]

BrazeでのWebhookの使用方法については、[Webhookの]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)作成を参照。 

## ユースケース キャンペーン

### キャンペーンとキャンバスの設定

#### トリガー

報酬イベントやゲストイベントなど、Brazeに送信されるPunchhイベントをトリガーとするBrazeメッセージングのユースケースは、関連するPunchhイベントをトリガーとする[アクションベースのキャンペーン]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery#action-based-delivery)またはCanvasesとして作成することができる。

トリガーを追加すると、Brazeで作成されたイベントのリストが表示される。キャンペーンまたはキャンバスをトリガーするイベントを選択し、イベントを記録したユーザーに送信する。

![][12]

プロパティフィルターを追加して、トリガーイベントをさらにフィルターすることができる。例えば、顧客が "checkins_gift "イベントをトリガーし、そのイベントのプロパティが "approved"(`true`)である場合にのみ、メッセージがトリガーされるべきである。これはオプション機能であり、すべてのユースケースに適用できるとは限らない。 

#### セグメンテーション

多くの場合、PunchhイベントによってトリガーされるBrazeキャンペーンやキャンバスは、これらのイベントをトリガーするユーザーのセグメンテーションがPunchh内で決定されるため、「すべてのユーザー」オーディエンスに設定することができる。しかし、イベントによってトリガーされるBrazeメッセージングを受信するユーザーのオーディエンスをさらに絞り込みたい顧客は、キャンペーン作成画面の**ターゲットオーディエンス**またはキャンバス作成画面の**エントリー**オーディエンスのセクションに、追加のフィルターやセグメントを追加することで可能です。 

### ユースケース

{% tabs local %}
{% tab Signup %}
#### 登録キャンペーン

オファーが添付されたサインアップキャンペーンにBrazeの設定を利用する場合、サインアップギフトキャンペーンをPunchhで設定し、Brazeでウェルカムメッセージを設定する必要がある。 

Punchhは、サインアップキャンペーンに実行遅延を追加し、Brazeがゲストイベントに基づいてウェルカムメッセージを最初にトリガーできるようにすることを推奨する。ユーザーにギフトが贈られたことを知らせるフォローアップメッセージを送りたい場合、報酬イベントに基づいてトリガーすることができる。

サインアップキャンペーンの場合、登録されたすべてのユーザーがセグメンテーションに使用できるため、Brazeのカスタムセグメントは必要ない。

パンチングコンフィギュレーションが必要である：
- Campaign: 登録する 
- Segment: 全員が登録した
- Reward: 顧客の選択
必要なイベント
- 報酬イベント
- ゲストイベント
Considerations:
- 実行遅延、ゲストに5～10分の遅延を追加することを勧める

![A user segment is configured in punch, and guests sign up for a loyalty program. After this, the guest event, if triggered, and the Braze messaging campaign is triggered. Next, the Punchh sign-up gifting campaign is triggered after 10 minutes, triggering the reward event and optional follow-up message.]({% image_buster /assets/img/punchh/usecase3.png %})

{% endtab %}
{% tab Mass offer %}
#### 大量オファーキャンペーン

ギフトにマスオファーキャンペーンを利用する場合、Punchhでマスオファーキャンペーンを設定し、Brazeでメッセージングキャンペーンを設定する必要がある。

キャンペーンにBrazeセグメントを利用したい場合、またはPunchhプラットフォームで顧客にギフトを贈る前にBrazeからコミュニケーションを送信したい場合は、Punchhギフトキャンペーンに[カスタムPunchhセグメントが]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#step-3-create-punchh-webhook-in-braze)必要になる。 

Brazeでこのオファーを受け取るユーザーのセグメンテーションを作成することは、Punchhで利用できない属性を使用する場合にのみ推奨される。そうでなければ、Punchhのセグメンテーションを使用することができ、Brazeメッセージングキャンペーンは、ユーザーが報酬を受け取ったことをトリガーとするアクションベースのキャンペーンとして作成される（Punchhによってトリガーされる報酬イベント）。

パンチングコンフィギュレーションが必要である：
- Campaign: マス・オファー
- Segment: カスタムリストまたは顧客の選択
- Reward: 顧客の選択

**セグメンテーションとギフトにはPunchhを、メッセージングにはBrazeを使用している：**<br>
例えば、2ドル割引の報酬は、Punchh内で設定可能なセグメンテーションに送信され、メッセージングはBrazeを通じて送信される。<br>
![A user segment can be configured in Punchh, and users receive a gift through a Punchh mass offer campaign. Next, a reward event is triggered, and then the Braze messaging campaign is triggered.]({% image_buster /assets/img/punchh/usecase6.png %}){: style="max-width:80%;"}

**Brazeのセグメンテーションとメッセージング、Punchhをギフトに使う：**<br>
例えば、2ドル引きの報酬とメッセージングを、Punchhでは利用できない属性を持つセグメンテーションに送信する。<br>
![A user segment can be configured in Braze, and then a message can be sent from a Braze-to-Braze segment. Next, the users are sent to the Punchh custom segment through a Braze webhook with segment and user ID. After this, the user receives a gift through Punchh mass offer campaign with a custom segment. After this the reward event is triggered.]({% image_buster /assets/img/punchh/usecase5.png %}){: style="max-width:80%;"}

**BrazeのセグメンテーションとPunchhをギフトやメッセージング、またはその両方に使用する：**<br>
例えば、Punchhで利用できない属性を持つセグメンテーションに2ドル引きの報酬を送るが、メッセージングは必要ない、またはメッセージングはPunchhを通して送ることができる（すべてのゲストがPunchhに存在する必要があることに注意）。<br>
![A user segment can be configured in Braze, and the users are sent to Punchh custom segment through a Braze webhook with segment and user ID. After this, the user receives a gift through Punchh mass offer campaign with a custom segment. After this the reward event is triggered.]({% image_buster /assets/img/punchh/usecase4.png %})

{% endtab %}
{% tab Recurring mass offer %}
#### 定期的な大量オファーキャンペーン

ギフト用の定期的なマスオファーキャンペーンを利用する場合、Punchhでマスオファーキャンペーンを設定し、Brazeでメッセージングキャンペーンを設定する必要がある。顧客がBrazeセグメンテーションを使用したい場合は、Punchhカスタム属性が必要となる（Punchhで利用できない属性を利用する場合のみ推奨）。そうでなければ、Punchhセグメンテーションを使用することができ、報酬イベントに基づいてメッセージングキャンペーンがトリガーされる。

パンチングコンフィギュレーションが必要である：
- Campaign: 定期的な大量オファー
- Segment: カスタムリストまたは顧客の選択
- Reward: 顧客の選択
Considerations:
- キャンペーンIDとキャンペーン名は、イベントのイベントプロパティとしてBrazeに送られる。BrazeでPunchhキャンペーン識別子を使用して、キャンペーンを受け取るオーディエンスをさらにフィルターしたい場合、キャンペーンIDは毎日変更されるため、キャンペーン名を使用する必要がある。

{% endtab %}
{% tab Post check-in offer with notification %}
#### チェックイン後の通知付きキャンペーン

ポストチェックインキャンペーンを利用する場合、Brazeはギフトに関する通知を送信し、宿泊客がチェックインすると、Punchhのポストチェックインキャンペーンからギフトが贈られる。したがって、チェックイン後のオファーキャンペーンをPunchhで設定し、メッセージングキャンペーンをBrazeで設定する必要がある（顧客にキャンペーンを通知する場合）。

パンチングコンフィギュレーションが必要である：
- Campaign: チェックイン後のオファー
- Segment: 顧客リスト
- Reward: 顧客の選択

例えば、Punchhでは利用できない属性を持つセグメンテーションに、今週末に来店するとポイントが2倍になることを知らせるメールを送る。Punchhは、対象となるチェックインとBrazeからのオプションのメッセージングの後、このセグメンテーションにポイントを贈呈する。 

![A user segment is configured in Braze, and messages are sent from Braze post check-in campaign. Next, the qualifying users are sent to Punchh custom segment through Braze webhook with segment and user ID. Lastly, the qualifying user in the custom segment checks in and receives the gift and optional message through post check-in campaign]({% image_buster /assets/img/punchh/update7.png %})

{% endtab %}
{% tab Post check-in offer without notification %}
#### 通知なしのチェックイン後のキャンペーン

顧客に最初に通知しないチェックイン後のオファーキャンペーンを利用する場合、キャンペーンはギフト（オプションのメッセージング）を行い、Braze内で任意の通知をトリガーする。そのため、チェックイン後のオファーキャンペーンをPunchh内で設定する必要があるが、カスタムリストは必要ない。その代わり、Punchhの中で好きなセグメンテーションを選ぶことができる。 

パンチングコンフィギュレーションが必要である：
- Campaign: チェックイン後のオファー
- Segment: 顧客の選択
- Reward: 顧客の選択

例えば、パンチで利用可能なセグメンテーションに、驚きと喜びのBrazeキャンペーンを送り、来店客に感謝の意を表し、次回来店時に2ドル引きの報酬を与える。

![An qualifying user segment can be configured within Punchh, and a qualifying user checks in and receives a gift through a Punchh post-check-in campaign. After this, a reward event is triggered and the recall message is sent notifying guests of the reward sent from Braze.]({% image_buster /assets/img/punchh/usecase2.png %})

{% endtab %}
{% tab Anniversary %}
#### 周年キャンペーン 

アニバーサリーキャンペーンを利用する場合、ユーザーはまずPunchhキャンペーンからアニバーサリーギフトを受け取る。このギフト（報酬イベント）は、ユーザーにギフトを通知するBraze内のメッセージングキャンペーンのトリガーとなる。したがって、カスタムリストは必要ない。その代わり、Punchhの中でセグメンテーションと記念日の設定を選ぶことができる。

パンチングコンフィギュレーションが必要である：
- Campaign: 周年キャンペーン
- Segment: 顧客の選択
- Reward: 顧客の選択
Considerations:
- 入会月のギフト
- 有効期間（誕生日報酬の有効期間は？）
- 定期的に行われるキャンペーン、スケジュール必須 

![An optional segment can be created within Punchh, and a qualifying user receives a reward through a Punchh anniversary campaign. After this, a reward event is triggered and the recall message is sent notifying guests of the reward sent from Braze.]({% image_buster /assets/img/punchh/usecase1.png %})

{% endtab %}
{% tab Recall %}
#### リコールキャンペーン

非アクティブに基づいてユーザーをターゲティングする場合、リコールキャンペーンを使用することができる。顧客はPunchh内でセグメンテーションとキャンペーンを作成できるが、メッセージングにはBrazeを利用する。

Brazeで作成したセグメンテーションを使用したい場合は、非アクティブに基づいた[カスタムPunchhセグメントを]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#step-3-create-punchh-webhook-in-braze)、定期的なマスオファーキャンペーンに添付することができる。

パンチングコンフィギュレーションが必要である：
- Campaign: リコールキャンペーン
- Segment: 顧客の選択
- Reward: 顧客の選択
Considerations:
- キャンペーンはスケジュールされたものである。

![An optional segment can be created within Punchh, and a qualifying user receives a reward through a Punchh recall campaign. After this, a reward event is triggered, and the recall message is sent notifying guests of the reward sent from Braze.]({% image_buster /assets/img/punchh/usecase.png %})

{% endtab %}
{% endtabs %}


[1]: {% image_buster /assets/img/punchh/punchh1.png %}
[2]: {% image_buster /assets/img/punchh/punchh2.png %}
[3]: {% image_buster /assets/img/punchh/punchh3.png %}
[4]: {% image_buster /assets/img/punchh/punchh4.png %}
[5]: {% image_buster /assets/img/punchh/punchh5.png %}
[7]: {% image_buster /assets/img/punchh/punchh6.png %}
[6]: {{site.baseurl}}/api/basics?redirected=true#endpoints
[8]: {% image_buster /assets/img/punchh/update1.png %}
[9]: {% image_buster /assets/img/punchh/update2.png %}
[10]: {% image_buster /assets/img/punchh/update3.png %}
[11]: {% image_buster /assets/img/punchh/update4.png %}
[12]: {% image_buster /assets/img/punchh/update5.png %}
[13]: {% image_buster /assets/img/punchh/update6.png %}
[14]: {% image_buster /assets/img/punchh/update7.png %}
