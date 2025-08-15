---
nav_title: Lob
article_title: Lob 
alias: /partners/lob/
description: "この参考記事では、BrazeとLob.comの提携について概説している。Lob.comを利用すれば、手紙やはがき、小切手などのダイレクトメールを郵送することができる。"
page_type: partner
search_tag: Partner

---

# Lob

> [Lob.com][38] は、ユーザーにダイレクトメールを送ることができるオンラインサービスである。

Braze と Lob の統合では、Braze Webhook と Lob API を使用して、手紙、ポストカード、小切手などを郵送します。  

## 前提条件

|必要条件| 説明|
| ---| ---|
|Lob アカウント | このパートナーシップを活用するには、Lob アカウントが必要です。 |
| Lob API キー | Lob API キーは、Lob ダッシュボードのお客様の名前の下にある設定セクションで確認できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ1:Lobエンドポイントを選択する

Webhook で要求する HTTP URL は、Lob に対して実行できるアクションごとに異なります。以下の例では、postcards APIエンドポイント`https://api.lob.com/v1/postcards` を使っている。[すべてのエンドポイントのリスト][39]にアクセスして、ユースケースに適したエンドポイントを選択します。 

| APIエンドポイント | 利用可能なエンドポイント |
| ------------ | ------------------- |
| https://api.lob.com/ | /v1/addresses<br>/v1/addresses/{id}<br>/v1/verify<br>/v1/postcards<br>/v1/postcards/{id}<br>/v1/letter<br>/v1/letter/{id}<br>/v1/checks<br>/v1/checks/{id}<br>/v1/bank_accounts<br>/v1/bank_accounts/{id}<br>/v1/bank_accounts/{id}/verify<br>/v1/areas<br>/v1/areas/{id}<br>/v1/routes/{zip_code}<br>/v1/routes<br>/v1/countries<br>/v1/states|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### ステップ2:BrazeのWebhookテンプレートを作成する

今後のキャンペーンやCanvasで使用するLobウェブフックテンプレートを作成するには、Brazeプラットフォームの**Templates**>**Webhook Templatesに**移動する。 

単発のLob Webhookキャンペーンを作成したい場合、または既存のテンプレートを使用したい場合は、新しいキャンペーンを作成する際にBrazeで**Webhookを**選択する。

新しいWebhookテンプレートで、以下のフィールドに記入する：
- **Webhook URL**: `<LOB_API_ENDPOINT>`
- **リクエスト本文**:Raw Text

#### リクエストヘッダと方法

Lob には、認証用の HTTP ヘッダーと HTTP メソッドが必要です。以下の内容はすでにキーと値のペアとしてテンプレートに含まれていますが、[**設定**] タブで `<LOB_API_KEY>` をご使用の Lob API キーに置き換える必要があります。このキーの直後に「:」が付加されており、またこのキーは64進数でエンコードされている必要があります。 

- **HTTPメソッド**：POST
- **リクエストヘッダー**:
  - **Authorization**:Basic `{{'<LOB_API_KEY>:' | base64_encode}}`
  - **Content-Type**: application/json

![Braze Webhook ビルダー作成タブに表示されているリクエスト本文のコードと Webhook URL。][35]

#### Request body

Lob ポストカードエンドポイントのリクエスト本文の例を次に示します。このリクエスト本文は Braze の 基本 Lobテンプレートで提供されますが、他のエンドポイントを使用する場合は、それに応じて Liquid フィールドを調整する必要があります。

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

この時点で、あなたのキャンペーンはテストと送信の準備ができているはずです。エラーが発生した場合は、LobダッシュボードとBraze開発者コンソールのエラーメッセージログを確認する。例えば、以下のエラーは、認証ヘッダーのフォーマットが正しくないために発生した。 

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
