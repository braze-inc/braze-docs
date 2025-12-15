---
nav_title: WhatsAppと外部システム
article_title: BrazeとWhatsAppを外部システムと統合する
page_order: 2
description: "この参考記事では、BrazeとWhatsAppを外部のAIやコミュニケーションシステムと統合するためのステップバイステップのガイドを提供する。"
page_type: reference
alias: /whatsapp_external_system_integration/
channel:
  - WhatsApp
---

# BrazeとWhatsAppを外部のAIやコミュニケーションシステムと連携させる

> WhatsAppチャネルでAIチャットボットとライブエージェントハンドオフのパワーを活用し、顧客サポート業務を効率化しよう。定型的な問い合わせをオートメーション化し、必要に応じて人間のエージェントにシームレスに移行することで、レスポンスタイムを大幅に改善し、カスタマーエクスペリエンス全体を向上させることができる。

## 仕組み

Brazeと外部のAIやコミュニケーションシステムとの統合は、Brazeがコミュニケーションチャネルであり、外部システムがメッセージを処理し、レスポンスを策定する「インテリジェント」であるという双方向として機能する。

統合ワークフローは、2つの主要なフローに分けられる：
**インバウンドの流れ：**ユーザーのメッセージがBrazeに届き、処理のために外部システムに転送される。
**アウトバウンドフロー：**外部システムはメッセージを処理した後、Brazeにレスポンスを送信し、Brazeはエンドユーザーにメッセージを配信する。

このコミュニケーションを効率的に自動化するために、この統合ではBrazeの2つの主要機能、[Webhookキャンペーンと]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) [APIトリガーキャンペーンを]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/)使用している。

![BrazeのWhatsAppチャネルと外部システムとの統合アーキテクチャ。]({% image_buster /assets/img/whatsapp/external_system_architecture.png %})
<sup>*BrazeのWhatsAppチャネルと外部システムとの統合アーキテクチャ。*</sup>

## 前提条件

| 前提条件 | 説明 |
| - | - |
| 外部システム | チャットボット、APIを使用した自動クライアントサービスシステム、またはその両方を構築・管理できるサードパーティのAIまたはコミュニケーションシステム。 |
| BrazeとWhatsAppの統合 | Brazeがマネージャーを務めるWhatsApp番号 |
| REST APIキー | `campaigns.trigger.send` の権限を持つ REST API キー。これはダッシュボードの**「設定」**>「**APIキー**」で作成できる。 |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

## 統合の設定

### ステップ 1: インバウンドメッセージ用のWebhookキャンペーンを作成する

まず、Webhookキャンペーンを作成し、Brazeで受信したWhatsAppメッセージを外部システムに送信する方法を確立する。

1. Brazeで、Webhookキャンペーンを作成する。
2. Webhook Composerで、**Compose webhookを**選択する。
3. **Webhook URL**フィールドに、メッセージを受信する外部システムのAPIエンドポイント（URL）を入力する。
4. リクエストボディに**Raw textを**選択し、パーソナライズされたペイロードを入力する。パーソナライズされたペイロードには、ユーザーの`external_id` 、電話番号、メッセージ内容、その他の関連情報などが含まれる：

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
5. キャンペーン作成画面の**配信スケジュール**ステップで、配信タイプに**「アクションベース**」を選択し、キャンペーントリガーに「**WhatsApp受信メッセージを送信**」を選択する。

![WhatsApp受信メッセージの送信をトリガーとしたアクションベースの配信。]({% image_buster /assets/img/whatsapp/inbound_message_trigger.png %})

{: start="6"}
6. キャンペーンの作成が完了したら、保存してキャンペーンを開始する。これで、メッセージを受信するたびに、Brazeは外部システムにWebhookを送信する。

### ステップ 2:アウトバウンドメッセージ用のAPIトリガーキャンペーンを作成する {#step-2}

次にAPIトリガーキャンペーンを作成し、外部システムからWhatsAppを通してユーザーへメッセージを送信する方法を確立する。

1. BrazeでWhatsAppキャンペーンを作成する。 
2. メッセージ作成画面で**WhatsAppテンプレートメッセージ**または**レスポンスメッセージの**いずれかを選択し、テンプレートまたはレスポンスメッセージのレイアウトを選択する。受信メッセージは24時間WhatsAppウィンドウを開封しているため、レスポンシブメッセージのレイアウトは自由である。

![メッセージタイプやメッセージレイアウトを選択できるメッセージ作成画面。]({% image_buster /assets/img/whatsapp/response_message_layout.png %})

{: start="3"}
3\.メッセージボディにAPIトリガープロパティを追加する。例えば、{% raw %}```{{api_trigger_properties.${external_system_msg+body}}}```{% endraw %} 。これにより、AIシステムが送信されるメッセージを入力できるようになる。

![トリガープロパティを含むメッセージボディを持つメッセージ作成画面。]({% image_buster /assets/img/whatsapp/api_trigger_properties.png %})

{: start="4"}
4. キャンペーンコンポーザーの**スケジュール配信**ステップで、配信タイプに**アクション**ベースを選択する。
5. キャンペーンを保存し、Brazeがこのキャンペーン用に生成したユニークな`campaign_id` をメモする。次のステップではIDが必要になる。

### ステップ 3:APIトリガーキャンペーンに外部システムを接続する。

最後に、外部システムがBrazeを呼び出し、レスポンスを送信するように設定する。

1. 外部システムのコードで、受信したメッセージを処理してレスポンスを生成した後、Braze`/messages/send` エンドポイントにPOSTリクエストを行う。
2. `/messages/send` リクエストボディに、[ステップ](#step-2)2の`campaign_id` 、ユーザーの`external_id` 、外部システムのレスポンスのコンテンツを含める。
3. [ステップ](#step-2)2のAPIトリガープロパティを使って外部システムのレスポンスを挿入し、このcURLの例のように、認証のためにリクエストヘッダーにAPIキーを含めることを忘れないこと：

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

これでAIチャットボットのワークフローを構築するための強固な基礎ができた！

### ワークフローをカスタマイズする

統合ロジックを次のように拡張することができる：
- Webhookキャンペーンをトリガーするキーワードを使い分ける。
- マルチステップAPIトリガーキャンペーンで、より複雑なカンバセーションフローを作成する。
- Brazeにチャット情報をカスタム属性として記録し、ユーザープロファイルを充実させ、将来のキャンペーンをセグメンテーションする。
