---
nav_title: WhatsApp・外部体制
article_title: BrazeとWhatsAppを外部と統合
page_order: 2
description: "このリファレンス記事では、BrazeとWhatsAppを外部AIまたは通信システムと統合するためのステップごとの手引きを提供します。"
page_type: reference
alias: /whatsapp_external_system_integration/
channel:
  - WhatsApp
---

# BrazeとWhatsAppを外部の人工知能または通信システムと統合

> WhatsApp チャネル上のAIチャットボットとライブエージェントのハンドオフ機能を活用して、顧客サポートオペレーションを合理化します。日常的な問い合わせを自動化し、必要に応じて人への移行をシームレスにすることで、応答時間を大幅に改善し、総合的なカスタマーエクスペリエンスを向上させることができます。

## 仕組み

Brazeと外部AIまたは通信システムとの統合は、双方向のストリートとして機能します。ここで、Brazeは通信チャネルであり、外部システムは"intelligence"メッセージを処理し、応答を形成します。

統合ワークフローは、2 つの主要なフローに分けることができます。
**インバウンドフロー:**ユーザーのメッセージはBrazeに到着し、処理のために外部システムに転送されます。
**アウトバウンドフロー:**メッセージを処理した後、外部システムはBrazeにレスポンスを送信し、その後、メッセージをend-ユーザーに配信します。

この通信を効率的に自動化するために、この統合では[Webhook キャンペーン s]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) と[API-トリガー ed キャンペーン s]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) の2 つの主要なBraze機能を使用します。

![Braze WhatsApp チャネルと外部システム間の統合のアーキテクチャ。]({% image_buster /assets/img/whatsapp/external_system_architecture.png %})
<sup>*Braze WhatsApp チャネルと外部システム間の統合のアーキテクチャ。*</sup>

## 前提条件

| 前提条件         | 説明                                                                                                                    |

| 外部システム| チャットボット、API を使用した自動クライアントサービスシステム、またはその両方を構築および管理できる、サードパーティ製のAI または通信システム。|
| BrazeおよびWhatsAppインテグレーション| Braze | によって管理されるWhatsApp番号
| Braze REST API キー | `campaigns.trigger.send` 権限を持つREST API キー。これは、**Settings** > **API Keys**.| に移動してBraze ダッシュボードで作成できます。
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

## 統合の設定

### ステップ 1: 着信メッセージ用のWebhook キャンペーンを作成する

まず、Webhook キャンペーンを作成して、Braze が受信したWhatsAppを外部システムに送信する方法を確立します。

1. Brazeで、Webhookキャンペーンを作成する。
2. Webhookコンポーザーで、**コンポーズWebhook**を選択します。
3. **WebフックURL**フィールドに、メッセージを受信する外部システムのAPI エンドポイント(URL)を入力します。
4. リクエストボディの**Raw text**を選択し、ユーザーの`external_id`と電話番号、メッセージの内容、および次のような他の関連情報を含むパーソナライゼーションを含む有料読み込むを入力します。

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
5. キャンペーン コンポーザーの**Schedule Delivery** ステップで、配信タイプに**Action-Based** を選択し、キャンペーン トリガーに**WhatsApp受信メッセージを送信します**。

![WhatsApp着信メッセージを送信するトリガーを使用したアクションベースの配信。]({% image_buster /assets/img/whatsapp/inbound_message_trigger.png %})

{: start="6"}
6. キャンペーンの作成を終了し、キャンペーンを保存して起動します。これで、メッセージを受信するたびに、Braze から外部システムにWebhookが送信されます。

### ステップ 2: アウトバウンドメッセージ用のAPI-トリガーed キャンペーンの作成 {#step-2}

次に、API-トリガー ed キャンペーンを作成して、外部システムがWhatsApp を介してユーザー s にメッセージを送信する方法を確立します。

1. Braze で、WhatsApp キャンペーンを作成します。 
2. メッセージ作成画面で、**WhatsApp テンプレート Message** または**Response Message** のいずれかを選択し、テンプレートまたはレスポンスメッセージレイアウトを選択します。受信メッセージが24時間WhatsAppウィンドウを開封したため、任意の応答メッセージレイアウトを選択できます。

![メッセージ・コンポーザーには、メッセージ・タイプとメッセージ・レイアウトを選択するオプションがあります。]({% image_buster /assets/img/whatsapp/response_message_layout.png %})

{: start="3"}
3\.API トリガー プロパティをメッセージ本文に追加します({% raw %}```{{api_trigger_properties.${external_system_msg+body}}}```{% endraw %} など)。これにより、AI システムは送信されるメッセージを入力できます。

![トリガーのプロパティーを含むメッセージ本文を持つメッセージコンポーザー。]({% image_buster /assets/img/whatsapp/api_trigger_properties.png %})

{: start="4"}
4\.キャンペーンコンポーザーの**Schedule Delivery**ステップで、配信種別に**Action-Based**を選択します。
5. キャンペーンを保存し、このキャンペーンに対してBraze が生成する一意の`campaign_id` を書き留めます。次回のステップには身分証明書が必要です。

### ステップ 3: 外部装置をAPI-トリガーed キャンペーンに接続します

最後に、Brazeを呼び出してレスポンスを送信するように外部システムを設定します。

1. 外部システムのコードで、受信したメッセージを処理してレスポンスを生成した後、Braze`/messages/send` エンドポイントに対してPOST リクエストを実行します。
2. `/messages/send` リクエストボディに、[ステップ2](#step-2)の`campaign_id`、ユーザーの`external_id`、および外部システムのレスポンスの内容を含めます。
3. [ステップ2](#step-2)のAPI トリガー プロパティを使用して外部システムのレスポンスを挿入し、次のcURLの例のように、認証のリクエストヘッダーにAPIキーを含めることを忘れないでください。

{% raw %}
```json
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

これで、AI チャットボットワークフローを構築するための強固な基盤ができました!

### ワークフローのカスタマイズ

統合ロジックは、次のように拡張できます。
- 異なるキーワードs を使用して、異なるWebhook キャンペーンs をトリガーします。
- マルチステップ API-トリガー ed キャンペーン s を使用して、より複雑な対話フローを作成します。
- ユーザープロファイルを豊かにし、将来のキャンペーンをSegmentするために、チャット情報をBrazeにカスタム属性として記録しましょう。
