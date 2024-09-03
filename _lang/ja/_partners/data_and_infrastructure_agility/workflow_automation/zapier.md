---
nav_title: Zapier
article_title: Zapier
alias: /partners/zapier/
description: "この参考記事では、BrazeとZapier（ウェブアプリ間でデータを共有し、その情報を使ってアクションを自動化できる自動化ウェブツール）のパートナーシップについて概説している。"
page_type: partner
search_tag: Partner

---
# Zapierとの統合

> [Zapierは][1]自動化ウェブツールで、ウェブアプリ間でデータを共有し、その情報を使ってアクションを自動化することができる。 

BrazeとZapierのパートナーシップは、Braze APIとBraze[webhooksを][3]活用して、Google Workplace、Slack、Salesforce、WordPressなどのサードパーティアプリケーションと接続し、さまざまなアクションを自動化する。

## 前提条件

| 要件 | 説明 |
|---|---|
| Zapierアカウント | このパートナーシップを利用するには、Zapierアカウントが必要だ。 |
| Braze RESTエンドポイント | RESTエンドポイントのURL。エンドポイントは、[インスタンスのBraze URLに][0]依存する。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

以下のZapierの例では、POST webhookを使ってWordPressからBrazeに情報を送信する。この情報をもとに、ブレイズ・キャンバスを作成することができる。

### ステップ1:Zapierトリガーを作成する

Zapierの用語を使えば、"ザップ "とはアプリやサービスをつなぐ自動化されたワークフローのことだ。どのようなザップでも、最初の部分はトリガーを指定することだ。ザップが有効になると、トリガーが検出されるたびにZapierが自動的にそれぞれのアクションを実行する。

WordPressの例を使って、Zapierプラットフォームで、WordPressの新しい投稿が追加されたときにトリガーされるようにzapを設定し、**Post Statusと** **Post Typeとして** **Publishedと** **Postsを**選択する。 

![Zapierプラットフォームで、zapの中で、トリガーを "新しいコメント"、"任意のウェブフック"、"新しい投稿 "のいずれかに選択する。この例では、"new post "が選択されている。 ] \[5]

![Zapierプラットフォームで、ザップ内で、希望の投稿ステータスと投稿タイプを選択してトリガーを設定する。この例では、"Published "と "Posts "が選択されている。] \[6]

### ステップ2:アクションウェブフックを追加する

次に、ザップアクションを定義する。ザップが有効になり、トリガーが検出されると、自動的にアクションが発生する。

この例の続きで、BrazeのエンドポイントにJSONとしてPOSTリクエストを送りたい。これは、**Appsの**下にある**Webhooks**オプションを選択することで行うことができる。

![][7]

### ステップ3:Braze POSTをセットアップする

Webhookを設定する際は、以下の設定を使用し、Webhook URLにBraze RESTエンドポイントを指定する。完了したら、**Publishを**選択する。

- **方法**：POST
- **ウェブフックのURL**： `https://rest.iad-01.braze.com/canvas/trigger/send`
- **データのパススルー**False
- **アンフラッテン**だ：いいえ
- **ヘッダーをリクエストする**：
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

### ステップ4:Brazeのキャンペーンを作成する

ザップの設定が完了したら、リキッドフォーマットを使ってメッセージに情報を表示することで、BrazeのキャンペーンやキャンバスをWordPressのデータでカスタマイズすることができる。

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