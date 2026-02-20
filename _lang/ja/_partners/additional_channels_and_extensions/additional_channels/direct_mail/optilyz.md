---
nav_title: optilyz
article_title: optilyz
description: "この参考記事では、Brazeとoptilyzのパートナーシップについて概説している。このパートナーシップにより、より顧客中心の、持続可能で収益性の高いダイレクトメールキャンペーンを実施することが可能になる。"
alias: /partners/optilyz/
page_type: partner
search_tag: Partner

---

# optilyz

> [optilyz](https://optilyz.com) はダイレクトメールオートメーションプラットフォームです。顧客中心型で持続可能かつ収益性の高いダイレクトメールキャンペーンを実施できます。 

_この統合は optilyz によって管理されます。_

## 統合について

optilyzとBrazeのウェブフック統合を使用して、手紙、はがき、セルフメーラーなどのダイレクトメールを顧客に送信する。

## 前提条件

| 必要条件 | 説明 |
|---|---|
|optilyzアカウント | このパートナーシップを活用するには、optilyz アカウントが必要です。 |
| optilyz APIキー<br><br>`<OPTILYZ_API_KEY>`| optilyz API キーは optilyz カスタマーサクセスマネージャーから提供されます。<br><br>このAPIキーでBrazeとoptilyzのアカウントを接続できる。 |
| optilyzオートメーションID<br><br>`<OPTILYZ_AUTOMATION_ID>` | オートメーションIDは、ページヘッダーのボックスに記載されている。<br><br>optilyz にログインしたら、データの送信先のオートメーションに移動できます。<br>最初にオートメーションをアクティブにする必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## ユースケース

ダイレクトメールをデジタルチャネルのように運用することは、大量の郵送から脱却し、チャネルを (デジタル) カスタマージャーニーの一部として活用することを意味します。最新のダイレクトメールアプローチの利点は、次のとおりです。
- 関連性の向上、ユースケースの追加、A/Bテストの容易化、クロスチャネル効果によるコンバージョン率の向上
- 自動化とエンド・ツー・エンド・ソリューションによる労力の削減
- フレーム契約とコストの透明性によるコスト削減

## 統合

optilyz と統合するには、[optilyz API](https://www.optilyz.com/doc/api/) を使用して受信者データを Braze Webhook に送信します。

### ステップ1:BrazeのWebhookテンプレートを作成する

将来のキャンペーンやCanvasで使用するoptilyzウェブフックテンプレートを作成するには、Brazeプラットフォームで「**Templates**>**Webhook Templates**」に移動する。 

1回限りの optilyz Webhook キャンペーンを作成するか、既存のテンプレートを使用する場合は、新しいキャンペーンを作成する際に Braze で **Webhook** を選択します。

新しいWebhookテンプレートで、以下のフィールドに記入する：
- **Webhook URL**:Webhook URL はお客様ごとに異なり、optilyz のカスタマーサクセスマネージャーから提供されます。
- **リクエスト本文**:Raw Text

#### リクエストヘッダと方法

optilyz には、認証用の HTTP ヘッダーと HTTP メソッドが必要です。以下の内容はすでにキーと値のペアとしてテンプレートに含まれていますが、[**設定**] タブで `<OPTILYZ_API_KEY>` を optilyz API キーに置き換える必要があります。このキーの直後に「:」が付加されており、またこのキーは64進数でエンコードされている必要があります。 

- **HTTPメソッド**：POST
- **リクエストヘッダー**:
  - **Authorization**: {% raw %} `{{ '<OPTILYZ_API_KEY>:' | base64_encode }}` {% endraw %}
  - **Content-Type**: application/json

![Braze webhookビルダーに表示されるリクエストヘッダーとHTTPメソッド。]({% image_buster /assets/img/optilyz/optilyz_settings.png %}){: style="max-width:50%"}

#### Request body

次のリクエスト本文では、任意の Liquid パーソナライゼーションタグを使用して、optilyz の [API ドキュメント](https://www.optilyz.com/doc/api/)に従ってカスタムリクエストテンプレートを作成できます。

`variation` フィールドはオプションであり、オートメーション内部のどのデザインを使用するかを定義できます。バリエーションが省略された場合、optilyzは定義されたバリエーションの1つをランダムに割り当てる。

{% raw %}
```json
{
    "address": {
        "title": "{{custom_attribute.${salutation}}}",
        "firstName": "{{${first_name}}}",
        "lastName": "{{${last_name}}}",
        "street": "{{custom_attribute.${street}}}",
        "houseNumber": "{{custom_attribute.${houseNumber}}}",
        "address2": "{{custom_attribute.${address2}}}",
        "zipCode": "{{custom_attribute.${zipCode}}}",
        "city": "{{custom_attribute.${city}}}",
        "country": "{{custom_attribute.${country}}}"
    },
    "variation": {{custom_attribute.${designVariation}}}
}
```
{% endraw %}

![Braze Webhook ビルダー作成タブに表示さているリクエスト本文のコードと Webhook URL の画像。]({% image_buster /assets/img/optilyz/optilyz_compose.png %})

### ステップ2:リクエストをプレビューする

次に、**Preview**パネルでリクエストをプレビューするか、**Test**タブに移動して、ランダムなユーザー、既存のユーザーを選択するか、ウェブフックをテストするために自分でカスタマイズする。ページを離れる前にテンプレートを保存することを忘れないこと！

![Braze webhookビルダーのテストタブで利用可能なさまざまなテストフィールド。]({% image_buster /assets/img/optilyz/optilyz_testing.png %})

{% alert important %}
ページを離れる前にテンプレートを保存することを忘れないこと！<br>更新されたWebhookテンプレートは、新しい[Webhookキャンペーンを]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)作成するときに、**保存されたWebhookテンプレート**リストで見つけることができる。
{% endalert %}


