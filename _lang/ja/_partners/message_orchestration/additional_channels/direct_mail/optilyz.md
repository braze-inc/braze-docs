---
nav_title: optilyz
article_title: optilyz
description:この記事では、Brazeとoptilyzの提携について説明しており、より顧客中心で持続可能かつ収益性の高いダイレクトメールキャンペーンを実施できるようにします。
alias: /partners/optilyz/
page_type: partner
search_tag:Partner

---

# optilyz

> [optilyz][1] は、より顧客中心で持続可能かつ収益性の高いダイレクトメールキャンペーンを実行できるダイレクトメール自動化プラットフォームです。 

オプティリズとBrazeのウェブフック統合を使用して、手紙、はがき、セルフメーラーなどのダイレクトメールを顧客に送信します。

## 前提条件

| 要件 | 説明 |
|---|---|
|optilyz アカウント | このパートナーシップを利用するには、optilyzアカウントが必要です。 |
| optilyz APIキー<br><br>`<OPTILYZ_API_KEY>`| あなたのoptilyzカスタマーサクセスマネージャーがoptilyz APIキーを提供します。<br><br>このAPIキーを使用すると、Brazeとoptilyzのアカウントを接続できます。 |
| optilyz オートメーション ID<br><br>`<OPTILYZ_AUTOMATION_ID>` | オートメーションIDはページヘッダーのボックスにあります。<br><br>optilyzにログインすると、データを送信したいオートメーションに移動できます。<br>自動化は最初に有効化されなければなりません。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## ユースケース

デジタルチャネルのようにダイレクトメールを実行することは、大量の郵送から離れ、チャネルを（デジタル）顧客ジャーニーの一部として活用することを意味します。現代的なダイレクトメールアプローチの利点は次のとおりです：
- 関連性の向上、追加のユースケース、より簡単なA/Bテスト、およびクロスチャネル効果によるコンバージョン率の向上
- 自動化とエンドツーエンドのソリューションによる労力の削減
- フレーム契約とコストの透明性によるコスト削減

## 統合

optilyzと統合するには、[optilyz API][2]を使用して受信者データをBraze webhookに送信します。

### ステップ1:BrazeのWebhookテンプレートを作成する

将来のキャンペーンやキャンバスで使用するためのoptilyz webhookテンプレートを作成するには、Brazeプラットフォームの**テンプレート** > **Webhookテンプレート**に移動します。 

{% alert note %}
古いナビゲーションを使用している場合は、[エンゲージメント]({{site.baseurl}}/navigation) > **テンプレートとメディア** > **Webhookテンプレート**に移動します。
{% endalert %}

新しいキャンペーンを作成する際にBrazeで**Webhook**を選択すると、ワンオフのoptilyz webhookキャンペーンを作成したり、既存のテンプレートを使用したりできます。

新しいWebhookテンプレートに、次のフィールドに記入してください:
- **Webhook URL**: ウェブフックURL:Webhook URLは各顧客に固有のものであり、optilyzのカスタマーサクセスマネージャーがそれを提供します。
- **リクエスト本文**:Raw Text

#### リクエストヘッダーとメソッド

optilyzは、認証のためのHTTPヘッダーとHTTPメソッドも必要です。次の内容はすでにテンプレート内にキーと値のペアとして含まれていますが、**設定**タブで`<OPTILYZ_API_KEY>`をoptilyz APIキーに置き換える必要があります。このキーにはキーの直後に「:」を含め、base 64でエンコードする必要があります。 

- **HTTPメソッド**:ポスト
- **リクエストヘッダー**:
  - **認可**: {% raw %} `{{ '<OPTILYZ_API_KEY>:' | base64_encode }}` {% endraw %}
  - **Content-Type**: application/json

![Braze Webhookビルダーに表示されるリクエストヘッダーとHTTPメソッド。][6]{: style="max-width:50%"}

#### Request body

次のリクエストボディでは、任意のLiquidパーソナライゼーションタグを使用し、optilyzの[APIドキュメント][2]に従ってカスタムリクエストテンプレートを作成できます。

`variation` フィールドは任意であり、自動化内で使用するデザインを定義できます。バリエーションが省略された場合、optilyzは定義されたバリエーションのいずれかをランダムに割り当てます。

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

![BrazeのWebhookビルダーの作成タブに表示されるリクエストボディコードとWebhook URLの画像。][5]

### ステップ2:リクエストをプレビュー

次に、**プレビュー**パネルでリクエストをプレビューするか、**テスト**タブに移動して、ランダムなユーザー、既存のユーザーを選択するか、独自のユーザーをカスタマイズしてWebhookをテストします。ページを離れる前にテンプレートを保存することを忘れないでください！

![Braze Webhookビルダーのテストタブで利用可能なさまざまなテストフィールド。][7]

{% alert important %}
ページを離れる前にテンプレートを保存することを忘れないでください！<br>新しい**webhookテンプレート**を作成する際に、更新されたwebhookテンプレートは[保存されたWebhookテンプレート]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)リストにあります。
{% endalert %}

[1]: https://optilyz.com
[2]: https://www.optilyz.com/doc/api/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template/
[5]: {% image_buster /assets/img/optilyz/optilyz_compose.png %}
[6]: {% image_buster /assets/img/optilyz/optilyz_settings.png %}
[7]: {% image_buster /assets/img/optilyz/optilyz_testing.png %}
[9]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/