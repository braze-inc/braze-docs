---
nav_title: WhatsAppと外部システム
article_title: BrazeとWhatsAppを外部システムと統合する
page_order: 2
description: "この参考記事は、BrazeとWhatsAppの連携を外部AIシステムや通信システムに統合するためのステップを説明する。"
page_type: reference
alias: /whatsapp_external_system_integration/
channel:
  - WhatsApp
---

# BrazeとWhatsAppを外部AIまたは通信システムと統合する

> WhatsAppチャネルでAIチャットボットとライブエージェントへの引き継ぎを活用し、顧客サポート業務を効率化せよ。定型的な問い合わせをオートメーション化し、必要に応じて人間エージェントにシームレスに移行することで、応答時間を大幅に改善し、カスタマーエクスペリエンスを高めることができる。

## 仕組み

Brazeと外部AIまたは通信システムとの連携は双方向で機能する。Brazeが通信チャネルとなり、外部システムがメッセージを処理し応答を生成する「知能」となる。

統合ワークフローは、二つの主要な流れに分けられる：
**流入量：**ユーザーのメッセージがBrazeに届くと、処理のために外部システムに転送される。
**アウトバウンドフロー：**メッセージを処理した後、外部システムはBrazeに応答を送信する。その後、Brazeがメッセージをエンドユーザーに配信する。

この通信を効率的にオートメーションするため、この統合ではBrazeの2つの主要機能を使用する：[webhookキャンペーン]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)と[APIトリガー型キャンペーン]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/)だ。

![BrazeのWhatsAppチャネルと外部システム間の統合アーキテクチャ。]({% image_buster /assets/img/whatsapp/external_system_architecture.png %})
<sup>*BrazeのWhatsAppチャネルと外部システム間の統合アーキテクチャ。*</sup>

## 前提条件

| 前提条件 | 説明 |
| - | - |
| 外部システム | サードパーティのAIまたは通信システムで、チャットボットやオートメーションされた顧客サービスシステムを構築・管理できるもの、あるいはその両方に対応するものである。 |
| BrazeとWhatsAppの連携 | Brazeが管理するWhatsApp番号 |
| Braze REST APIキー | 権限`campaigns.trigger.send`付きのREST APIキー。これはBrazeダッシュボードの**「設定**」＞「**API キー」**から作成できる。 |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

## 統合の設定

### ステップ 1: 受信メッセージ用のWebhookキャンペーンを作成する

まず、Brazeが受信したWhatsAppメッセージを外部システムに送信する方法を確立するため、webhookキャンペーンを作成する。

1. Brazeで、Webhookキャンペーンを作成する。
2. Webhookコンポーザーで、**「Webhookを作成」**を選択する。
3. **Webhook URL**フィールドには、メッセージを受信する外部システムのAPIエンドポイント（URL）を入力する。
4. リクエスト本文には**「Raw text」**を選択し、ユーザーの`external_id`氏名と電話番号、メッセージ内容、その他の関連情報を含むパーソナライゼーションされたペイロードを入力する。例えば：

{% raw %}
```liquid
{
  "user_id": "{{${user_id}}}",
  "phone_number": "{{${phone_number}}}",
  "message": "{{whats_app.${inbound_message_body}}}"
}
```
{% endraw %}

{: start="5"}
5. キャンペーン作成ツールの「**配信スケジュール**」ステップで、配信タイプに**「アクションベース」**を選択し、キャンペーンのトリガーに「**WhatsAppインバウンドメッセージを送信**」**を設定する**。

![WhatsAppの受信メッセージ送信をトリガーとするアクションベースの配信。]({% image_buster /assets/img/whatsapp/inbound_message_trigger.png %})

{: start="6"}
6. キャンペーンの作成を完了したら、保存してキャンペーンを開始する。キャンペーンを開始すると、メッセージを受信するたびに、Brazeは外部システムにWebhookを送信する。

### ステップ 2:APIトリガーによる送信メッセージキャンペーンを作成する {#step-2}

次に、APIトリガー型キャンペーンを作成する。これにより、外部システムからWhatsAppを通じてユーザーへメッセージを返信する仕組みを構築する。

1. BrazeでWhatsAppキャンペーンを作成する。 
2. メッセージ作成画面で、**WhatsAppテンプレートメッセージ**か**返信メッセージ**のいずれかを選択し、次にテンプレートまたは返信メッセージのレイアウトを選ぶ。受信メッセージが24時間のWhatsAppウィンドウを開封したため、任意の返信メッセージレイアウトを選択できる。

![メッセージ作成画面。メッセージの種類とレイアウトを選択するオプション付き。]({% image_buster /assets/img/whatsapp/response_message_layout.png %})

{: start="3"}
3\.メッセージ本文にAPIトリガープロパティを追加する。例えば{% raw %}```{{api_trigger_properties.${external_system_msg+body}}}```{% endraw %}。これにより、AIシステムが送信されるメッセージを生成できるようになる。

![トリガープロパティを含むメッセージ本文を持つメッセージ作成画面。]({% image_buster /assets/img/whatsapp/api_trigger_properties.png %})

{: start="4"}
4. キャンペーン作成ツールの**「配信スケジュール**」ステップで、配信タイプとして**「アクションベース」**を選択する。
5. キャンペーンを保存し、その後、Brazeがこのキャンペーン用に生成した一意のID`campaign_id`をメモしておく。次のステップにはIDが必要だ。

### ステップ 3:外部システムをAPIトリガー型キャンペーンに接続する

最後に、外部システムを設定してBrazeを呼び出し、応答を送信する。

1. 外部システムのコードでは、受信したメッセージを処理し応答を生成した後、Braze`/messages/send`のエンドポイントに対してPOSTリクエストを送信する。
2. リクエスト`/messages/send`本文には、ステップ`campaign_id`[2](#step-2)からの値、ユーザーのID`external_id`、および外部システムの応答内容を記載する。
3. [ステップ2](#step-2)のAPIトリガープロパティを使って外部システムの応答を挿入する。認証のためリクエストヘッダーにAPI キーを含めるのを忘れるな。例えば以下のcURL例のように：

{% raw %}
```bash
curl -X POST \
  -H 'Content-Type:application/json' \
  -H 'Authorization: Bearer a valid rest API key' \
  -d '{
    "campaign_id": "campaign_id",
    "recipients": [
      {
        "external_user_id": "external_id",
        "trigger_properties": {
          "external_system_msg_body": "your external system message"         
        }
      }
    ]
  }' \
  {{Braze endpoint}}/campaigns/trigger/send
```
{% endraw %}

これでAIチャットボットのワークフローを構築するための確かな基盤ができた！

### ワークフローをカスタマイズする

統合ロジックを次のように拡張できる：
- 異なるキーワードを使って、それぞれ別のWebhookキャンペーンをトリガーする。
- 複数のステップからなるAPIトリガー型キャンペーンで、より複雑なコンバージョンの流れを作成する。
- Brazeでチャット情報をカスタム属性として記録し、ユーザープロファイルを充実させ、将来のキャンペーンをセグメント化する。
