---
nav_title: Inkit
article_title: Inkit
alias: /partners/inkit/
description: "この参考記事では、BrazeとInkitのパートナーシップについて概説している。Inkitは、ダイレクトメール・キャンペーンを自動化することで時間と労力を節約し、オフラインの顧客をオンラインに戻すことを可能にする。"
page_type: partner
search_tag: Partner

---

# Inkit

> [Inkitと][1]Brazeは、デジタルでもダイレクトメールでも、企業が安全に文書を作成・配布できるようにする。

BrazeとInkitの統合により、BrazeのWebhookを使って文書を生成し、Brazeユーザーに直接郵送することができる。

## 前提条件

|必要条件| 説明|
| ---| ---|
|Inkitアカウント | このパートナーシップを利用するには、[Inkitアカウントが](https://www.inkit.com/)必要である。 |
| InkitのAPIキー<br><br>`<INKIT_API_TOKEN>` | このキーは、[Inkitダッシュボードの](https://app.inkit.io/#/account/integrations) **開発**タブにあり、BrazeとInkitのアカウントを接続することができる。|
| InkitテンプレートID<br><br>`<INKIT_TEMPLATE_ID>` | テンプレートを作成した後、**テンプレート**タブからテンプレートIDをコピーしてBrazeのテンプレートで使用することができる。<br><br>例えば、Inkit環境にテンプレートID:`tmpl_3bDScFl9cwr3OAVR1RSdEC` で`invoice_template` というテンプレートを作成する。
| HTTPヘッダー | HTTPヘッダーは、BrazeからInkitに送信するAPIリクエストの一部である。その中に、Inkit APIへの呼び出しを認証および承認するためのInkit APIキーを含める。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 統合

### ステップ1:Inkitテンプレートを作成する

Inkitプラットフォーム上で、Brazeキャンペーンで使用するテンプレートをHTML、Word、PowerPoint、ExcelまたはPDFで作成する。詳しくは[Inkitのドキュメントを](https://docs.inkit.com/docs/create-a-template)参照されたい。

### ステップ2:BrazeのWebhookテンプレートを作成する

今後のキャンペーンやCanvasで使用するInkitウェブフックテンプレートを作成するには、Brazeプラットフォームの**「テンプレート**」>「**ウェブフックテンプレート**」に移動する。 

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、「**Engagement（エンゲージメント）**」＞「**Templates & Media（テンプレート＆メディア**）」＞「**Webhook Templates（ウェブフック・テンプレート**）」と進む。
{% endalert %}

単発のInkitウェブフックキャンペーンを作成したい場合、または既存のテンプレートを使用したい場合は、新しいキャンペーンを作成する際にBrazeの**ウェブフックを**選択する。

![Templates & MediaセクションのWebhook Templatesタブにある、利用可能なデザイン済みWebhookテンプレートのセレクション。][7]

Inkitウェブフック・テンプレートを選択すると、以下のように表示される：
- **ウェブフックのURL**：空白
- **リクエスト・ボディ**Raw Text

Webhook URLフィールドで、InkitのWebhook URLを[作成](https://docs.inkit.com/docs/set-up-a-webhook-to-an-event)し、入力する必要がある。

![Braze webhook builderのcomposeタブに表示されるリクエストボディコードとwebhook URL。][5]

#### リクエストヘッダと方法

Inkitは、認証のために、Base 64でエンコードされたInkit APIキーを含む、`HTTP Header` 。以下はすでにキーと値のペアとしてテンプレート内に含まれているが、**「設定」**タブでは、`<INKIT_API_TOKEN>` をあなたのInkit APIキーに置き換える必要がある。

{% raw %}
- **HTTPメソッド**：POST
- **ヘッダーをリクエストする**：
  - **認可する**：ベーシック `{{ '<INKIT_API_TOKEN>' | base64_encode }}`
  - **Content-Type**: application/json
{% endraw %}

#### Request body

リキッドが以下の必須フィールドとオプションフィールドに関連する適切なカスタム属性と一致していることを確認する。また、どのリクエストにもカスタムデータフィールドを追加することができる。

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

Brazeタグに該当するテキストは自動的にハイライトされる。`street`このWebhookを送信するには、`unit` 、`state` 、`zip` を[カスタム属性として][3]設定する必要がある。

**Preview**パネルでリクエストをプレビューするか、**Test**タブに移動して、ランダムなユーザー、既存のユーザーを選択するか、ウェブフックをテストするために自分でカスタマイズする。

{% alert important %}
ページを離れる前にテンプレートを保存することを忘れないこと！<br>更新されたWebhookテンプレートは、新しい[Webhookキャンペーンを]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)作成するときに、**保存されたWebhookテンプレート**リストで見つけることができる。
{% endalert %}

[1]: https://www.inkit.com
[2]: https://help.inkit.com/hc/en-us/articles/360036546873-Braze-Inkit-Integration
[3]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attributes
[5]: {% image_buster /assets/img/inkit-integration.png %}
[6]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
[7]: {% image_buster /assets/img/inkit-webhook-template.png %}