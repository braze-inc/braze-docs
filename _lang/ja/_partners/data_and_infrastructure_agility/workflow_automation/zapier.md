---
nav_title: Zapier
article_title:Zapier
alias: /partners/zapier/
description:"この参考記事では、Brazeと、ウェブアプリ間でデータを共有し、その情報を使ってアクションを自動化できるオートメーション・ウェブ・ツールであるZapierとのパートナーシップについて概説している。"
page_type: partner
search_tag:Partner

---
# Zapierとの統合

> [Zapierは][1]、ウェブアプリ間でデータを共有し、その情報を使ってアクションを自動化できるオートメーション・ウェブツールだ。 

BrazeとZapierのパートナーシップは、Braze APIとBraze[webhookを][3]活用して、Google Workplace、Slack、Salesforce、WordPressなどのサードパーティアプリケーションと接続し、さまざまなアクションを自動化する。

## 前提条件

| 要件 | 説明 |
|---|---|
| Zapierアカウント | このパートナーシップを利用するには、Zapierアカウントが必要だ。 |
| Braze RESTエンドポイント | RESTエンドポイントのURL。エンドポイントは[インスタンスのBraze URLに][0]依存する。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

以下のZapierの例では、POST Webhookを使ってWordPressからBrazeに情報を送信する。この情報を使ってBrazeキャンバスを作成することができる。

### ステップ1:Zapierトリガーを作成する

Zapierの用語を使えば、「Zap」とはアプリやサービスをつなぐオートメーション・ワークフローのことだ。どんなザップでも、最初にトリガーを指定する。ザップがイネーブルメントされると、Zapierはトリガーが検出されるたびにそれぞれのアクションを自動的に実行する。

WordPressの例を使って、Zapierプラットフォームで、WordPressの新しい投稿が追加されたときにトリガーするようにZapを設定し、**投稿ステータスと** **投稿タイプとして** **Publishedと** **Postsを**選択する。 

![Zapierプラットフォームで、Zapの中で、トリガーを "新しいコメント"、"任意のWebhook"、"新しい投稿 "のいずれかに選択する。

![ZapierプラットフォームのZap内で、希望の投稿ステータスと投稿タイプを選択してトリガーを設定する。

### ステップ2:アクションWebhookを追加する

次に、ザップアクションを定義する。ザップがイネーブルメントになり、トリガーが検出されると、アクションが自動的に発生する。

例の続きで、BrazeエンドポイントにJSONとしてPOSTリクエストを送りたい。これは、**アプリの**下にある**Webhooks**オプションを選択することで行うことができる。

![][7]

### ステップ3:Braze POSTの設定

Webhookを設定する際は、以下の設定を使用し、Webhook URLにBraze RESTエンドポイントを指定する。完了したら、**Publishを**選択する。

- **方法**：ポスト
- **WebhookのURL**： `https://rest.iad-01.braze.com/canvas/trigger/send`
- **データのパススルー**False
- **アンフラッテン**だ：いいえ
- **リクエストヘッダー**：
  - **Content-Type**: application/json
  - **認可する**：Bearer YOUR-API-KEY
- **データ**だ： 

```json
{
  "canvas_id": "your_canvas_identifier",
  "recipients": [
    {
      "external_user_id": "external_user_identifier",
      "canvas_entry_properties":{
        "string_property": "Your example string",
        "example_integer_property": 1
      }
    }
  ]
}
```

![][4]{: style="max-width:70%;"}

### ステップ 4:Brazeキャンペーンを作成する

ザップの設定が完了したら、BrazeのキャンペーンやCanvasesをWordPressのデータでカスタマイズすることができ、メッセージの情報をLiquidフォーマットで表示することができる。

[0]: {{site.baseurl}}/api/basics/#api-definitions
[1]: https://zapier.com/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#creating-a-webhook
[4]:{% image_buster /assets/img/zapier.png %}
[5]:{% image_buster /assets/img_archive/zapier1.png %}
[6]:{% image_buster /assets/img_archive/zapier2.png %}
[7]:{% image_buster /assets/img_archive/zapier3.png %}
[8]:{% image_buster /assets/img_archive/zapier4.png %}
[10]:{% image_buster /assets/img_archive/zapier5.png %}
[12]:{% image_buster /assets/img_archive/zapier6.png %}