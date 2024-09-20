---
nav_title: optilyz
article_title: optilyz
description: "この参考記事では、Brazeとoptilyzのパートナーシップについて概説している。このパートナーシップにより、より顧客中心の、持続可能で収益性の高いダイレクトメールキャンペーンを実施することが可能になる。"
alias: /partners/optilyz/
page_type: partner
search_tag: Partner

---

# optilyz

> [optilyzは][1]、より顧客中心の、持続可能で収益性の高いダイレクトメールキャンペーンの実施を可能にするダイレクトメール自動化プラットフォームである。 

optilyzとBrazeのウェブフック統合を使用して、手紙、はがき、セルフメーラーなどのダイレクトメールを顧客に送信する。

## 前提条件

| 必要条件 | 説明 |
|---|---|
|optilyzアカウント | このパートナーシップを利用するには、optilyzアカウントが必要である。 |
| optilyz APIキー<br><br>`<OPTILYZ_API_KEY>`| optilyzカスタマーサクセスマネージャーがoptilyz APIキーを提供する。<br><br>このAPIキーでBrazeとoptilyzのアカウントを接続できる。 |
| optilyzオートメーションID<br><br>`<OPTILYZ_AUTOMATION_ID>` | オートメーションIDは、ページヘッダーのボックスに記載されている。<br><br>optilyzにログインすると、データを送信したいオートメーションに移動することができる。<br>まずオートメーションを作動させなければならない。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## ユースケース

ダイレクトメールをデジタル・チャネルのように運用することは、大量発送から脱却し、カスタマージャーニーの一部として活用することを意味する。ダイレクトメールの現代的なアプローチの利点は以下の通りである：
- 関連性の向上、ユースケースの追加、A/Bテストの容易化、クロスチャネル効果によるコンバージョン率の向上
- 自動化とエンド・ツー・エンド・ソリューションによる労力の削減
- フレーム契約とコストの透明性によるコスト削減

## 統合

optilyzと統合するには、[optilyz APIを][2]使用して受信者データをBrazeのウェブフックに送信する。

### ステップ1:BrazeのWebhookテンプレートを作成する

将来のキャンペーンやCanvasで使用するoptilyzウェブフックテンプレートを作成するには、Brazeプラットフォームで「**Templates**>**Webhook Templates**」に移動する。 

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、「**Engagement（エンゲージメント）**」＞「**Templates & Media（テンプレート＆メディア**）」＞「**Webhook Templates（ウェブフック・テンプレート**）」と進む。
{% endalert %}

単発のoptilyzウェブフックキャンペーンを作成したい場合、または既存のテンプレートを使用したい場合は、新しいキャンペーンを作成する際にBrazeで**ウェブフックを**選択する。

新しいWebhookテンプレートで、以下のフィールドに記入する：
- **ウェブフックのURL**：WebhookのURLは顧客ごとに異なり、オプティリズのカスタマーサクセスマネージャーが提供する。
- **リクエスト・ボディ**Raw Text

#### リクエストヘッダと方法

optilyzはまた、認可のためのHTTPヘッダーとHTTPメソッドを必要とする。以下はすでにキーと値のペアとしてテンプレート内に含まれているが、**設定**タブでは、`<OPTILYZ_API_KEY>` をあなたの optilyz API キーに置き換える必要がある。このキーは、キーの直後に": "を含み、64進数でエンコードされていなければならない。 

- **HTTPメソッド**：POST
- **ヘッダーを要求する**：
  - **認可する**： {% raw %} `{{ '<OPTILYZ_API_KEY>:' | base64_encode }}` {% endraw %}
  - **Content-Type**: application/json

![Braze webhookビルダーに表示されるリクエストヘッダーとHTTPメソッド。][6]{: style="max-width:50%"}

#### Request body

以下のリクエストボディでは、任意のLiquidパーソナライゼーションタグを使用し、optilyzの[APIドキュメントに従って][2]カスタムリクエストテンプレートを構築することができる。

`variation` フィールドはオプションで、オートメーション内部のどのデザインを使用するかを定義することができる。バリエーションが省略された場合、optilyzは定義されたバリエーションの1つをランダムに割り当てる。

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

![Braze webhook builderのcomposeタブに表示されるリクエストボディコードとwebhook URLのイメージ。][5]

### ステップ2:リクエストをプレビューする

次に、**Preview**パネルでリクエストをプレビューするか、**Test**タブに移動して、ランダムなユーザー、既存のユーザーを選択するか、ウェブフックをテストするために自分でカスタマイズする。ページを離れる前にテンプレートを保存することを忘れないこと！

![Braze webhookビルダーのテストタブで利用可能なさまざまなテストフィールド。][7]

{% alert important %}
ページを離れる前にテンプレートを保存することを忘れないこと！<br>更新されたWebhookテンプレートは、新しい[Webhookキャンペーンを]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)作成するときに、**保存されたWebhookテンプレート**リストで見つけることができる。
{% endalert %}

[1]: https://optilyz.com
[2]: https://www.optilyz.com/doc/api/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template/
[5]: {% image_buster /assets/img/optilyz/optilyz_compose.png %}
[6]: {% image_buster /assets/img/optilyz/optilyz_settings.png %}
[7]: {% image_buster /assets/img/optilyz/optilyz_testing.png %}
[9]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/