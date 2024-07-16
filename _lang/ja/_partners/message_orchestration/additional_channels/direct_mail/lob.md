---
nav_title: Lob
article_title:Lob
alias: /partners/lob/
description:"この参考記事では、BrazeとLob.comの提携について概説している。この提携により、手紙、はがき、小切手などのダイレクトメールを郵送で送ることができる。"
page_type: partner
search_tag:Partner

---

# Lob

> \[Lob.com][38] は、ユーザーにダイレクトメールを送ることができるオンラインサービスだ。

BrazeとLobの統合は、BrazeのWebhookとLobのAPIを活用して、手紙、はがき、小切手などのメールをメールで送信する。  

## 前提条件

|必要条件| 説明|
| ---| ---|
|Lobアカウント | このパートナーシップを利用するにはLobアカウントが必要である。 |
| Lob API キー | LobのAPIキーは、ダッシュボードのあなたの名前の下の設定セクションにある。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:Lobエンドポイントを選択する

WebhookでリクエストするHTTP URLは、Lobにできるアクションごとに異なる。以下の例では、postcards APIエンドポイント`https://api.lob.com/v1/postcards` を使っている。ユースケースに適したエンドポイントを選択するには、\[エンドポイント一覧][39] ] を参照すること。 

| APIエンドポイント | 利用可能なエンドポイント |
| ------------ | ------------------- |
| https://api.lob.com/ | /v1/addresses<br>/v1/addresses/{id}<br>/v1/verify<br>/v1/postcards<br>/v1/postcards/{id}<br>/v1/letter<br>/v1/letter/{id}<br>/v1/checks<br>/v1/checks/{id}<br>/v1/bank_accounts<br>/v1/bank_accounts/{id}<br>/v1/bank_accounts/{id}/verify<br>/v1/areas<br>/v1/areas/{id}<br>/v1/routes/{zip_code}<br>/v1/routes<br>/v1/countries<br>/v1/states|
{: .reset-td-br-1 .reset-td-br-2}

### ステップ2:BrazeのWebhookテンプレートを作成する。

今後のキャンペーンやCanvasで使用するLob Webhookテンプレートを作成するには、Brazeプラットフォームの「**テンプレート**」>「**Webhookテンプレート**」に移動する。 

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、**エンゲージメント**>**テンプレートとメディア**>**Webhookテンプレートに**移動する。
{% endalert %}

単発のLob Webhookキャンペーンを作りたい、または既存のテンプレートを使いたい場合は、新規キャンペーン作成時にBrazeで**Webhookを**選択する。

新しいWebhookテンプレートで、以下のフィールドに記入する：
- **WebhookのURL**： `<LOB_API_ENDPOINT>`
- **リクエスト・ボディ**Raw Text

#### リクエストヘッダーとメソッド

Lobは認可のためのHTTPヘッダーとHTTPメソッドを必要とする。以下はすでにキーと値のペアとしてテンプレート内部に含まれているが、**設定**タブでは、`<LOB_API_KEY>` をあなたのLob APIキーに置き換える必要がある。このキーは、キーの直後に": "を含み、64進数でエンコードされていなければならない。 

- **HTTPメソッド**：POST
- **リクエストヘッダー**：
  - **認可する**：ベーシック `{{'<LOB_API_KEY>:' | base64_encode}}`
  - **Content-Type**: application/json

![Braze webhook builderのcomposeタブに表示されるリクエストボディコードとWebhook URL。][35]

#### Request body

以下はLob postcardsエンドポイントのリクエストボディの例である。このリクエストボディは、BrazeのベースLobテンプレートで提供されているが、他のエンドポイントを使用したい場合は、それに応じてLobidフィールドを調整する必要がある。

```json
{% raw %}"description": "Demo Postcard",
"to": {
    "name": "{{${first_name}}} {{${last_name}}}",
    "address_line1": "{{custom_attribute.${address_line1}}}",
    "address_city": "{{custom_attribute.${address_city}}}",
    "address_zip": "{{custom_attribute.${address_zip}}}",
    "address_country": "{{custom_attribute.${address_country}}}"
},
"front": "https://lob.com/postcardfront.pdf",
"back": "https://lob.com/postcardback.pdf"{% endraw %}
```

### ステップ3:リクエストをプレビューする

この時点で、キャンペーンをテストして送信する準備が整っているはずだ。エラーに遭遇した場合は、LobダッシュボードとBraze開発者コンソールのエラーメッセージログを確認する。例えば、以下のエラーは、認証ヘッダーが正しくフォーマットされていないことが原因である。 

![時間、アプリ名、チャネル、エラーメッセージを示すメッセージエラーログ。エラーメッセージには、メッセージアラートとステータスコードが含まれる。][36]

{% alert important %}
ページを離れる前にテンプレートを保存することを忘れないこと！<br>更新されたWebhookテンプレートは、新しい[Webhookキャンペーンを]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)作成するときに、**保存されたWebhookテンプレート**リストで見つけることができる。
{% endalert %}

[33]: {% image_buster /assets/img_archive/lob_api_key.png %}
[34]: {% image_buster /assets/img_archive/lob_success_response.png %}
[35]: {% image_buster /assets/img_archive/lob_full_request.png %}
[36]: {% image_buster /assets/img_archive/error_log.png %}
[37]: {% image_buster /assets/img_archive/lob_api_endpoint.png %}
[38]: https://lob.com
[39]: https://lob.com/docs#intro
[40]: https://lob.com/docs#auth
