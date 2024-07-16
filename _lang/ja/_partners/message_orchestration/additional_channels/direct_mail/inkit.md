---
nav_title: Inkit
article_title:Inkit
alias: /partners/inkit/
description:"この参考記事では、ダイレクトメールキャンペーンをオートメーション化することで時間と労力を節約し、オフラインの顧客をオンラインに戻すことを可能にする、BrazeとInkitのパートナーシップについて概説している。"
page_type: partner
search_tag:Partner

---

# Inkit

> [Inkitと][1]Brazeは、デジタルでもダイレクトメールでも、ドキュメントを安全に作成・配布できるようにする。

BrazeとInkitの統合により、BrazeのWebhookを使ってドキュメントを作成し、Brazeユーザーに直接郵送することができる。

## 前提条件

|必要条件| 説明|
| ---| ---|
|Inkitアカウント | このパートナーシップを利用するには、[Inkitアカウントが](https://www.inkit.com/)必要である。 |
| API キー<br><br>`<INKIT_API_TOKEN>` | このキーは、[Inkitダッシュボードの](https://app.inkit.io/#/account/integrations)「**開発」**タブにあり、BrazeとInkitアカウントの接続をイネーブルメントする。|
| テンプレートID<br><br>`<INKIT_TEMPLATE_ID>` | テンプレート作成後、**テンプレート**タブからテンプレートIDをコピーし、Brazeのテンプレートで使用することができる。<br><br>例えば、Inkit環境に`invoice_template` というテンプレートをテンプレートID:`tmpl_3bDScFl9cwr3OAVR1RSdEC` で作成するとする。
| HTTPヘッダー | HTTPヘッダーは、BrazeからInkitに送信するAPIリクエストの一部である。その中に、Inkit APIへのコールを認証および承認するためのInkit APIキーを含める。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 統合

### ステップ1:テンプレートを作成する

Inkitプラットフォーム上で、Brazeキャンペーンで使用するテンプレートをHTML、Word、PowerPoint、Excel、またはPDFで作成する。詳しくは[Inkitのドキュメントを](https://docs.inkit.com/docs/create-a-template)学習しよう。

### ステップ2:BrazeのWebhookテンプレートを作成する。

今後のキャンペーンやCanvasで使用するInkit Webhookテンプレートを作成するには、Brazeプラットフォームの「**テンプレート**」>「**Webhookテンプレート**」に移動する。 

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、**エンゲージメント**>**テンプレートとメディア**>**Webhookテンプレートに**移動する。
{% endalert %}

単発のInkit Webhookキャンペーンを作成する場合、または既存のテンプレートを使用する場合は、新規キャンペーン作成時にBrazeで**Webhookを**選択する。

![Templates & MediaセクションのWebhook Templatesタブにある、利用可能なデザイン済みWebhookテンプレートのセレクション。][7]

InkitのWebhookテンプレートを選択すると、次のように表示される：
- **WebhookのURL**：空白
- **リクエスト・ボディ**Raw Text

Webhook URLフィールドで、Inkit Webhook URLを[作成](https://docs.inkit.com/docs/set-up-a-webhook-to-an-event)し、入力する必要がある。

![Braze webhook builderのcomposeタブに表示されるリクエストボディコードとWebhook URL。][5]

#### リクエストヘッダーとメソッド

Inkitは、認証のために、ベース64でエンコードされたInkit APIキーを含む、`HTTP Header` 。以下はすでにキーと値のペアとしてテンプレート内部に含まれているが、**設定**タブでは、`<INKIT_API_TOKEN>` をあなたの Inkit API キーに置き換える必要がある。

{% raw %}
- **HTTPメソッド**：POST
- **リクエストヘッダー**：
  - **認可する**：ベーシック `{{ '<INKIT_API_TOKEN>' | base64_encode }}`
  - **Content-Type**: application/json
{% endraw %}

#### Request body

あなたのリキッドが、以下の必須フィールドとオプションフィールドに関連する適切なカスタム属性と一致していることを確認する。あらゆるリクエストに顧客データフィールドを追加することもできる。

```json
{% raw %}{
  "api_token": "<INKIT_API_TOKEN>",
  "template_id": "<INKIT_TEMPLATE_ID>",
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}",
  "email": "{{${email_address}}}",
  "company": "{{custom_attribute.${company_name}}}",
  "phone" : "{{${phone_number}}}",
  "address_line_1": "{{custom_attribute.${address}}}",
  "address_line_2": "{{custom_attribute.${address2}}}",
  "address_city": "{{${city}}}",
  "address_state": "{{custom_attribute.${state}}}",
  "address_zip": "{{custom_attribute.${zip}}}",
  "address_country": "{{${country}}}",
  "source" : "Braze"
}{% endraw %}
```

### ステップ3:リクエストをプレビューする

該当するBrazeタグであれば、生テキストが自動的にハイライトされる。`street`このWebhookを送信するには、`unit` 、`state` 、`zip` を[カスタム属性として][3]設定する必要がある。

**プレビュー**パネルでリクエストをプレビューするか、**テスト**タブに移動し、ランダムユーザー、既存ユーザー、またはWebhookをテストするための独自のカスタマイズを選択することができる。

{% alert important %}
ページを離れる前にテンプレートを保存することを忘れないこと！<br>更新されたWebhookテンプレートは、新しい[Webhookキャンペーンを]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)作成するときに、**保存されたWebhookテンプレート**リストで見つけることができる。
{% endalert %}

[1]: https://www.inkit.com
[2]: https://help.inkit.com/hc/en-us/articles/360036546873-Braze-Inkit-Integration
[3]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attributes
[5]: {% image_buster /assets/img/inkit-integration.png %}
[6]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
[7]: {% image_buster /assets/img/inkit-webhook-template.png %}