---
nav_title: オッピジー
article_title: オッピジー 
alias: /partners/oppizi/
description: "この参考記事では、BrazeとOppiziのパートナーシップについて概説している。"
page_type: partner
search_tag: Partner
---

# オッピジー

> [Oppiziは](https://www.oppizi.com/)オフラインマーケティングのグローバルリーダーであり、測定可能でターゲットを絞ったダイレクトメールやチラシキャンペーンを実施するためのワンストップソリューションを企業に提供している。

_この統合はOppiziによって維持されている。_

## 前提条件

| 必要条件                    | 説明                                                                   |
| ------------------------------ | ----------------------------------------------------------------------------- |
| オッピジーアカウント                 | この統合を使用するには、アクティブなOppiziアカウントが必要である。                 |
| Oppizi API キー                 | Oppiziアカウントの**Integrations**>**Brazeに**ある。                |
| オッピジ・ダイレクトメール ワークフローID | Oppiziの**ダイレクトメールワークフローページで**ワークフローを作成し、IDを取得する。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

Oppiziとの統合で、あなたはできる：

* OppiziのWebhookとダイレクトメールワークフローに接続されたBrazeトリガーを使用して、**自動ダイレクトメールハガキを送信**。
* Oppiziのダイレクトメールワークフローで、**しきい値、ウェーブ、リミットを設定し**、キャンペーンの送信をコントロールする。
* Oppiziの内蔵デザインツールで**プロフェッショナルなポストカードをデザイン**しよう。
* Oppiziのダッシュボードでリアルタイムに**キャンペーンパフォーマンスを追跡**しよう。

## 統合

### ステップ 1: Oppizi APIキーを生成する 

BrazeでWebhookテンプレートを使用するには、まずOppizi APIキーを生成する必要がある。

1. Oppiziにログインする。
2. **Integrations**>**Brazeに**進む。
3. APIキーを生成する。

必要に応じて、このページからキーのマネージャー、失効、作成ができる。

### ステップ 2:BrazeのWebhookテンプレートを作成する。

次に、今後のキャンペーンやCanvasで使用するために、BrazeでOppizi用のWebhookテンプレートを作成する。

1. Brazeで**Templates**> Webhook templatesに進む。

Webhookテンプレートに、以下のフィールドを記入する：

- **WebhookのURL：** ```https://webhooks.oppizi.com/events```
- **リクエスト本文：****Raw Text**

リクエストメソッドとヘッダーについて、Oppizi は HTTP メソッドと以下の HTTP ヘッダーをテンプレートに含めることを要求する。以下のフィールドに入力します。

- **HTTPメソッドを使用する：**POST
- **リクエストヘッダー：**
  - **認可する：** `Bearer <oppiziAPIKey>`
  - **コンテンツタイプ：** `application/json`

![BrazeのOppizi webhookヘッダーの例。]({% image_buster /assets/img/oppizi/oppizi_braze_webhook_headers.png %})

**リクエストボディには**、フィールド**oppiziWorkflowID** を含めなければならない。このIDは、Oppizでワークフローを作成する際に生成され、受信者をどのダイレクトメールワークフローに追加するかを指定するために必要となる。Oppiziの各ダイレクトメールワークフローには固有のIDがあるので、BrazeでOppiziのWebhookテンプレートを作成する場合は、ワークフローIDを常に正しいものに更新するようにする。

{% alert note %}
ダイレクトメールを送信するために必要な、受信者の郵便住所に必要なカスタム属性がBrazeアカウントに設定されていることを確認する。
{% endalert %}

![BrazeのOppizi Webhookテンプレートの例。]({% image_buster /assets/img/oppizi/oppizi_braze_webhook_example.png %})

以下はリクエストボディの例である：

{% raw %}
```json
{
    "event" : "workflow.addRecipient",
    "oppiziWorkflowID" : "<oppiziWorkflowID>",
    "requestType" : "live",
    "recipient" : {
        "recipientID" : "{{${braze_id}}}",
        "firstName" : "{{${first_name}}}",
        "lastName" : "{{${last_name}}}",
        "address1" : "{{custom_attribute.${address1}}}",
        "address2" : "{{custom_attribute.${address2}}}",
        "city" : "{{custom_attribute.${city}}}",
        "country" : "{{${country}}}",
        "zipCode" : "{{custom_attribute.${zipCode}}}",
        "state" : "{{custom_attribute.${state}}}"
    }
}
```
{% endraw %}

### ステップ 3:Oppiziでダイレクトメールのワークフローを作成する

1. Oppiziで、**ダイレクトメールワークフロー**>**ワークフローを作成する**。
2. しきい値、ウェーブ、はがきフォーマット、アートワークなど、ワークフローの詳細を設定する。
3. Webhookの詳細セクションには、ワークフローIDを含むすぐに使えるリクエストボディがあり、Brazeに直接貼り付けることができる。

### ステップ 4: Brazeでリクエストのプレビューとテストを行う

OppiziのワークフローIDでリクエストボディを追加した後、テストを実行し、セットアップが期待通りに機能していることを確認する。

テストを実行するには、リクエストボディの`requestType` を`live` から`test` に更新する。このステップは、ダイレクトメールのオーディエンスにテスト受信者を追加しないために重要である。

テストが終わったら、`requestType` を`live` に更新し、キャンバスを保存する。これで、自動ダイレクトメールキャンペーンを開始する準備が整った。
