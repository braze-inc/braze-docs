---
nav_title: Twilioパートナーシップ
alias: /partners/twilio/

description: "この記事では、BrazeとTwilioのパートナーシップについて概説する。"
page_type: update
channel: 
  - SMS
  - Webhook
---

# Twilio

{% alert warning %}
Twilio Webhook Integration のサポートは2020年1月31日に廃止されることにご注意ください。BrazeでもSMSサービスにアクセスしたい場合は、[SMSのドキュメントを]({{site.baseurl}}/user_guide/message_building_by_channel/sms/)参照のこと。
{% endalert %}

この例では、Twilio の[メッセージ送信API](https://www.twilio.com/docs/api/rest/sending-messages) を介して、SMS とMMS をユーザーに送信するようにBraze Webhook チャネルを設定します。便宜上、ダッシュボードには Twilio Webhook テンプレートが含まれています。

## HTTP URL

WebhookのURLはダッシュボードでTwilioから提供される。このURLにはTwilioアカウントID(`TWILIO_ACCOUNT_SID`)が含まれているため、Twilioアカウントに固有のURLとなる。

Twilio の例では、Webhook URL は `https://api.twilio.com/2010-04-01/Accounts/TWILIO_ACCOUNT_SID/Messages.json` です。このURLは、Twilioコンソールの*Getting Started*セクションに記載されている。

![Twilio_Console]({% image_buster /assets/img_archive/Twilio_Console.png %})

## リクエスト本文

Twilio API では、リクエスト本文が URL エンコードされていると想定しているため、まず Braze Webhook コンポーザーのリクエストタイプを `Raw Text` に変更する必要があります。リクエスト本文に必要なパラメータは、*To*、*From*、*Body*である。

次のスクリーンショットは、各ユーザーの電話番号に "Hello from Braze!"という本文でSMSを送信する場合のリクエストの例である。

- ターゲットオーディエンスのユーザープロファイルごとに、有効な電話番号が必要です。
- Twilio のリクエスト形式に対応するため、メッセージコンテンツに `url_param_escape` Liquid フィルターを使用します。このフィルターは文字列をエンコードするため、HTML リクエストですべての文字が許可されます。例えば、電話番号 `+12125551212` のプラス文字 (`+`) はURL エンコードデータでは禁止されており、`%2B12125551212` に変換されます。

![Webhook 本文]({% image_buster /assets/img_archive/Webhook_Body.png %})

## リクエストヘッダーとメソッド

Twilio では、リクエストコンテンツタイプと [HTTP 基本認証](https://en.wikipedia.org/wiki/Basic_access_authentication#Client_side)ヘッダーの2つのリクエストヘッダーが必要です。ウェブフック・コンポーザーの横にある歯車のアイコンをクリックし、*「新しいペアを追加*」を2回クリックして、それらをウェブフックに追加する。

ヘッダー名 | ヘッダー値
--- | ---
コンテンツタイプ | `application/x-www-form-urlencoded`
許可 | `{% raw %}Basic {{ 'TWILIO_ACCOUNT_SID:TWILIO_AUTH_TOKEN' | base64_encode }}{% endraw %}`

`TWILIO_ACCOUNT_SID` と`TWILIO_AUTH_TOKEN` は、必ず Twilio ダッシュボードの値で置き換えてください。最後に、Twilio のAPI エンドポイントはHTTP POST リクエストを期待しているので、*HTTP Method* のドロップダウンでそのオプションを選択します。

![Webhook メソッド]({% image_buster /assets/img_archive/Webhook_Method.png %})

## リクエストのプレビュー

ウェブフックコンポーザーを使って、ランダムなユーザー、または特定の認証情報を持つユーザーのリクエストをプレビューし、リクエストが適切にレンダリングされていることを確認する。

![Webhook プレビュー]({% image_buster /assets/img_archive/Webhook_Preview.png %})

