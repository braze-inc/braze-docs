---
nav_title: Twilioパートナーシップ
alias: /partners/twilio/

description: "この記事では、BrazeとTwilioのパートナーシップについて概説する。"
page_type: update
channel: 
  - SMS
  - Webhook
---

# トワイリオ

{% alert warning %}
なお、Twilio Webhook Integrationのサポートは2020年1月31日に終了する。BrazeでもSMSサービスにアクセスしたい場合は、[SMSのドキュメントを]({{site.baseurl}}/user_guide/message_building_by_channel/sms/)参照のこと。
{% endalert %}

この例では、Twilioの[メッセージ送信APIを介して][20]、ユーザーにSMSとMMSを送信するようにBrazeのWebhookチャンネルを設定する。便宜上、Twilioウェブフック・テンプレートがダッシュボードに含まれている。

## HTTP URL

WebhookのURLはダッシュボードでTwilioから提供される。このURLにはTwilioアカウントID(`TWILIO_ACCOUNT_SID`)が含まれているため、Twilioアカウントに固有のURLとなる。

Twilioの例では、WebhookのURLは`https://api.twilio.com/2010-04-01/Accounts/TWILIO_ACCOUNT_SID/Messages.json` 。このURLは、Twilioコンソールの*Getting Started*セクションに記載されている。

![Twilio_Console][28]

## リクエスト・ボディ

Twilio APIはリクエストボディがURLエンコードされていることを期待するので、Braze webhook composerでリクエストタイプを`Raw Text` に変更することから始める必要がある。リクエスト本文に必要なパラメータは、*To*、*From*、*Body*である。

次のスクリーンショットは、各ユーザーの電話番号に "Hello from Braze!"という本文でSMSを送信する場合のリクエストの例である。

- ターゲットとするユーザーのプロフィールには、有効な電話番号が必要だ。
- Twilioのリクエストフォーマットを満たすには、メッセージ内容に`url_param_escape` Liquidフィルターを使用する。例えば、電話番号`+12125551212` のプラス文字 (`+`) はURLエンコードされたデータでは禁止されており、`%2B12125551212` に変換される。

![ウェブフック・ボディ][29]

## リクエスト・ヘッダとメソッド

Twilioは2つのリクエストヘッダ、リクエストContent-Typeと\[HTTP Basic Authentication][32] ]ヘッダを要求する。ウェブフック・コンポーザーの横にある歯車のアイコンをクリックし、*「新しいペアを追加*」を2回クリックして、それらをウェブフックに追加する。

ヘッダー名 | ヘッダー値
--- | ---
コンテンツタイプ | `application/x-www-form-urlencoded`
認可 | `{% raw %}Basic {{ 'TWILIO_ACCOUNT_SID:TWILIO_AUTH_TOKEN' | base64_encode }}{% endraw %}`

`TWILIO_ACCOUNT_SID` と`TWILIO_AUTH_TOKEN` は必ずTwilioダッシュボードの値で置き換えること。最後に、TwilioのAPIエンドポイントはHTTP POSTリクエストを想定しているので、*HTTP Methodの*ドロップダウンでそのオプションを選択する。

![ウェブフック・メソッド][30]

## リクエストをプレビューする

ウェブフックコンポーザーを使って、ランダムなユーザー、または特定の認証情報を持つユーザーのリクエストをプレビューし、リクエストが適切にレンダリングされていることを確認する。

![Webhookプレビュー][31]

[20]: https://www.twilio.com/docs/api/rest/sending-messages
[28]: {% image_buster /assets/img_archive/Twilio_Console.png %}
[29]: {% image_buster /assets/img_archive/Webhook_Body.png %}
[30]: {% image_buster /assets/img_archive/Webhook_Method.png %}
[31]: {% image_buster /assets/img_archive/Webhook_Preview.png %}
[32]: https://en.wikipedia.org/wiki/Basic_access_authentication#Client_side
