---
nav_title: ロブ
article_title: ロブ 
alias: /partners/lob/
description: "この参考記事では、BrazeとLob.comの提携について概説している。Lob.comを利用すれば、手紙やはがき、小切手などのダイレクトメールを郵送することができる。"
page_type: partner
search_tag: Partner

---

# ロブ

> \[Lob.com][38] は、ユーザーにダイレクトメールを送ることができるオンラインサービスである。

BrazeとLobの統合は、BrazeのウェブフックとLobのAPIを活用して、手紙、はがき、小切手などのメールをメールで送信する。  

## 前提条件

|必要条件| 説明|
| ---| ---|
|ロブアカウント | このパートナーシップを利用するには、ロブ・アカウントが必要である。 |
| ロブAPIキー | LobのAPIキーは、Lobダッシュボードのあなたの名前の下の設定セクションにある。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:Lobエンドポイントを選択する

WebhookでリクエストするHTTP URLは、Lobにできるアクションごとに異なる。以下の例では、postcards APIエンドポイント`https://api.lob.com/v1/postcards` を使っている。完全なエンドポイントリスト][39] ] にアクセスして、ユースケースに適したエンドポイントを選択する。 

| APIエンドポイント | 利用可能なエンドポイント |
| ------------ | ------------------- |
| https://api.lob.com/ | /v1/アドレス<br>/v1/addresses/{id}<br>/v1/ベリファイ<br>/v1/ポストカード<br>/v1/postcards/{id}<br>/v1/文字<br>/v1/letter/{id}<br>/v1/チェック<br>/v1/checks/{id}である。<br>/v1/bank_accounts<br>/v1/bank_accounts/{id}<br>/v1/bank_accounts/{id}/verify<br>/v1/エリア<br>/v1/areas/{id}である。<br>/v1/ルート/{zip_code}。<br>/v1/ルート<br>/v1/国<br>/v1/ステート|
{: .reset-td-br-1 .reset-td-br-2}

### ステップ2:BrazeのWebhookテンプレートを作成する

今後のキャンペーンやCanvasで使用するLobウェブフックテンプレートを作成するには、Brazeプラットフォームの**Templates**>**Webhook Templatesに**移動する。 

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、「**Engagement（エンゲージメント）**」＞「**Templates & Media（テンプレート＆メディア**）」＞「**Webhook Templates（ウェブフック・テンプレート**）」と進む。
{% endalert %}

単発のLob Webhookキャンペーンを作成したい場合、または既存のテンプレートを使用したい場合は、新しいキャンペーンを作成する際にBrazeで**Webhookを**選択する。

新しいWebhookテンプレートで、以下のフィールドに記入する：
- **ウェブフックのURL**： `<LOB_API_ENDPOINT>`
- **リクエスト・ボディ**Raw Text

#### リクエストヘッダと方法

Lobは認可のためのHTTPヘッダーとHTTPメソッドを必要とする。以下はすでにキーと値のペアとしてテンプレート内に含まれているが、**Settings**タブでは、`<LOB_API_KEY>` をあなたのLob APIキーに置き換える必要がある。このキーは、キーの直後に": "を含み、64進数でエンコードされていなければならない。 

- **HTTPメソッド**：POST
- **ヘッダーを要求する**：
  - **認可する**：ベーシック `{{'<LOB_API_KEY>:' | base64_encode}}`
  - **Content-Type**: application/json

![Braze webhook builderのcomposeタブに表示されるリクエストボディコードとwebhook URL。][35]

#### Request body

以下は、Lob postcardsエンドポイントのリクエストボディの例である。このリクエストボディは、Brazeの基本Lobテンプレートで提供されているが、他のエンドポイントを使用したい場合は、それに応じてLiquidフィールドを調整する必要がある。

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

この時点で、キャンペーンはテストと送信の準備ができているはずだ。エラーが発生した場合は、LobダッシュボードとBraze開発者コンソールのエラーメッセージログを確認する。例えば、以下のエラーは、認証ヘッダーのフォーマットが正しくないために発生した。 

![時間、アプリ名、チャンネル、エラーメッセージを示すメッセージエラーログ。エラーメッセージには、メッセージアラートとステータスコードが含まれる。][36]

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
