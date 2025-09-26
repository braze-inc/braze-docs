---
nav_title: Inkit
article_title: Inkit
alias: /partners/inkit/
description: "この参考記事では、BrazeとInkitのパートナーシップについて概説している。Inkitは、ダイレクトメール・キャンペーンを自動化することで時間と労力を節約し、オフラインの顧客をオンラインに戻すことを可能にする。"
page_type: partner
search_tag: Partner

---

# Inkit

> [Inkit](https://www.inkit.com) と Braze により、デジタルでもダイレクトメールでも、企業が安全に文書を作成して配布することができます。

_この統合は Inkit によって管理されます。_

## 統合について

Braze と Inkit の統合により、文書を生成し、Braze Webhook を使用して Braze ユーザーに直接メールで送信できます。

## 前提条件

|必要条件| 説明|
| ---| ---|
|Inkitアカウント | このパートナーシップを活用するには、[Inkit アカウント](https://www.inkit.com/)が必要です。 |
| Inkit API キー<br><br>`<INKIT_API_TOKEN>` | このキーは [Inkit Dashboard](https://app.inkit.io/#/account/integrations) の [**Development**] タブにあります。このキーにより Braze アカウントと Inkit アカウントを接続できるようになります。|
| Inkitテンプレート ID<br><br>`<INKIT_TEMPLATE_ID>` | テンプレートを作成した後、**テンプレート**タブからテンプレートIDをコピーしてBrazeのテンプレートで使用することができる。<br><br>たとえば、Inkit 環境にテンプレート ID: `tmpl_3bDScFl9cwr3OAVR1RSdEC` で `invoice_template` というテンプレートを作成できます。
| HTTPヘッダー | HTTPヘッダーは、BrazeからInkitに送信するAPIリクエストの一部である。この中には、Inkit API の呼び出しを認証および許可するための Inkit API キーが含まれます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 統合

### ステップ1:Inkit テンプレートを作成する

Inkitプラットフォーム上で、Brazeキャンペーンで使用するテンプレートをHTML、Word、PowerPoint、ExcelまたはPDFで作成する。詳細については、[Inkit のドキュメント](https://docs.inkit.com/docs/create-a-template)を参照してください。

### ステップ2:BrazeのWebhookテンプレートを作成する

今後のキャンペーンやCanvasで使用するInkitウェブフックテンプレートを作成するには、Brazeプラットフォームの**「テンプレート**」>「**ウェブフックテンプレート**」に移動する。 

単発のInkitウェブフックキャンペーンを作成したい場合、または既存のテンプレートを使用したい場合は、新しいキャンペーンを作成する際にBrazeの**ウェブフックを**選択する。

![「Templates & Media」セクションの「Webhook Templates」タブにある、一連の利用可能な事前設計済み Webhook テンプレート。]({% image_buster /assets/img/inkit-webhook-template.png %})

Inkitウェブフック・テンプレートを選択すると、以下のように表示される：
- **Webhook URL**:空白
- **リクエスト本文**:Raw Text

[Webhook URL] フィールドで、Inkit Webhook URL を[作成](https://docs.inkit.com/docs/set-up-a-webhook-to-an-event)して入力する必要があります。

![Braze Webhook ビルダー作成タブに表示されているリクエスト本文のコードと Webhook URL。]({% image_buster /assets/img/inkit-integration.png %})

#### リクエストヘッダと方法

Inkit の認証には、Base64 でエンコードされた Inkit API キーを含む `HTTP Header` が必要です。以下の内容はすでにキーと値のペアとしてテンプレートに含まれていますが、[**設定**] タブで `<INKIT_API_TOKEN>` を Inkit API キーに置き換える必要があります。

{% raw %}
- **HTTPメソッド**：POST
- **リクエストヘッダー**:
  - **Authorization**:Basic `{{ '<INKIT_API_TOKEN>' | base64_encode }}`
  - **Content-Type**: application/json
{% endraw %}

#### Request body

Liquid が、以下の必須フィールドとオプションフィールドに関連付けられている適切なカスタム属性を照合することを確認します。また、どのリクエストにもカスタムデータフィールドを追加できます。

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

生のテキストが適切な Braze タグである場合、このテキストが自動的に強調表示されます。この Webhook を送信するには、`street`、`unit`、`state`、`zip` が[カスタム属性]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attributes)として設定されている必要があります。

**Preview**パネルでリクエストをプレビューするか、**Test**タブに移動して、ランダムなユーザー、既存のユーザーを選択するか、ウェブフックをテストするために自分でカスタマイズする。

{% alert important %}
ページを離れる前にテンプレートを保存することを忘れないこと！<br>更新されたWebhookテンプレートは、新しい[Webhookキャンペーンを]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)作成するときに、**保存されたWebhookテンプレート**リストで見つけることができる。
{% endalert %}


