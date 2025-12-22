---
nav_title: Zapier
article_title: Zapier
alias: /partners/zapier/
description: "この参考記事では、BrazeとZapier（ウェブアプリ間でデータを共有し、その情報を使ってアクションを自動化できる自動化ウェブツール）のパートナーシップについて概説している。"
page_type: partner
search_tag: Partner

---
# Zapierとの統合

> [Zapier](https://zapier.com/) は、Web アプリ間でデータを共有し、その情報を使用してアクションを自動化できるオートメーション Web ツールです。 

Braze と Zapier のパートナーシップでは、Braze API と Braze [Webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#creating-a-webhook) を活用してサードパーティアプリケーション (Google Workplace、Slack、Salesforce、WordPress など) に接続し、さまざまなアクションを自動化できます。

## 前提条件

| 要件 | 説明 |
|---|---|
| Zapierアカウント | このパートナーシップを活用するには、Zapier アカウントが必要です。 |
| Braze RESTエンドポイント | REST エンドポイントのURL。エンドポイントはインスタンスの [Braze URL]({{site.baseurl}}/api/basics/#api-definitions) に応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

以下のZapierの例では、POST webhookを使ってWordPressからBrazeに情報を送信する。この情報を使用して Braze キャンバスを作成することができます。

### ステップ1:Zapierトリガーを作成する

Zapierの用語を使えば、"ザップ "とはアプリやサービスをつなぐ自動化されたワークフローのことだ。どのようなザップでも、最初の部分はトリガーを指定することだ。zap が有効になると、トリガーが検出されるたびにZapier によって対応するアクションが自動的に実行されます。

WordPressの例を使って、Zapierプラットフォームで、WordPressの新しい投稿が追加されたときにトリガーされるようにzapを設定し、**Post Statusと** **Post Typeとして** **Publishedと** **Postsを**選択する。 

![Zapierプラットフォームで、zap 内でトリガーとして「new comment」、「any webhook」、「new post」のいずれかを選択する。この例では、"new post "が選択されている。][5]

![Zapier プラットフォームで、zap 内で目的の post status と post type を選択してトリガーを設定する。この例では、"Published "と "Posts "が選択されている。］[6]

### ステップ2:アクションウェブフックを追加する

次に zap アクションを定義します。zap が有効になり、トリガーが検出されると、アクションが自動的に発生します。

この例の続きで、BrazeのエンドポイントにJSONとしてPOSTリクエストを送りたい。これを行うには、[**Apps**] の下にある [**Webhooks**] オプションを選択します。

![]({% image_buster /assets/img_archive/zapier3.png %})

### ステップ 3:Braze POSTをセットアップする

Webhook を設定するときに、次の設定を使用して Webhook URL に Braze REST エンドポイントを指定します。完了したら [**Publish**] を選択します。

- **方法**：POST
- **Webhook URL**: `https://rest.iad-01.braze.com/canvas/trigger/send`
- **Data Pass-Though**:False
- **Unflatten**:いいえ
- **リクエストヘッダー**:
  - **Content-Type**: application/json
  - **Authorization**:Bearer YOUR-API-KEY
- **Data**: 

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

![]({% image_buster /assets/img/zapier.png %}){: style="max-width:70%;"}

### ステップ 4: Brazeのキャンペーンを作成する

zap の設定が完了したら、Liquid フォーマットを使用してメッセージの情報を表示することで、WordPress データを使用して Braze キャンペーンまたはキャンバスをカスタマイズできます。

[5]: {% image_buster /assets/img_archive/zapier1.png %}
[6]: {% image_buster /assets/img_archive/zapier2.png %}
