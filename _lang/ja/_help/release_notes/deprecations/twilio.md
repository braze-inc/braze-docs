---
nav_title: Twilioとのパートナーシップ
alias: /partners/twilio/

description: "この記事では、BrazeとTwilioのパートナーシップについて概説します。"
page_type: update
channel: 
  - SMS
  - Webhook
---

# Twilio

{% alert warning %}
なお、Twilio Webhook Integrationのサポートは2020年1月31日に終了します。BrazeでSMSサービスにアクセスしたい場合は、 [SMSのドキュメント]({{site.baseurl}}/user_guide/message_building_by_channel/sms/)をご覧ください。
{% endalert %}

この例では、Twilioの [メッセージ送信API][20]を介してSMSとMMSをユーザーに送信するようにBraze Webhookチャネルを構成します。便宜上、Twilio Webhook テンプレートがダッシュボードに含まれています。

## HTTP URL

Webhook URL は、Twilio によってダッシュボードで提供されます。この URL には Twilio アカウント ID ()`TWILIO_ACCOUNT_SID` が含まれているため、Twilio アカウントに固有です。

Twilio の例では、Webhook URL は `https://api.twilio.com/2010-04-01/Accounts/TWILIO_ACCOUNT_SID/Messages.json`です。この URL は、Twilio コンソールの *[はじめに* ] セクションにあります。

![Twilio\_Console][28]

## 要求本文

Twilio APIはリクエスト本文がURLエンコードされることを前提としているため、Braze Webhookコンポーザー `Raw Text`のリクエストタイプをに変更することから始める必要があります。要求の本文に必要なパラメーターは、 *To*、 *From*、および *Body* です。

次のスクリーンショットは、各ユーザーの電話番号に SMS を送信し、本文が "Hello from Braze!" の場合のリクエストの例です。

- ターゲットオーディエンスの各ユーザープロフィールに有効な電話番号が必要です。
- Twilioのリクエスト形式を満たすには、メッセージの内容にLiquidフィルターを使用します `url_param_escape` 。このフィルターは、すべての文字が HTML 要求で許可されるように文字列をエンコードします。たとえば、電話番号`+12125551212`のプラス文字 ()`+` は URL エンコードされたデータでは禁止されており、`%2B12125551212`.

![Webhook本文][29]

## 要求ヘッダーとメソッド

Twilio には、要求 Content-Type と [HTTP 基本認証][32] ヘッダーの 2 つの要求ヘッダーが必要です。Webhook コンポーザーの横にある歯車アイコンをクリックし、[ *Add New Pair]* を 2 回クリックして、ペアを Webhook に追加します。

ヘッダー名 |ヘッダー値
--- |---
コンテンツタイプ | `application/x-www-form-urlencoded`
オーソリゼーション | `{% raw %}Basic {{ 'TWILIO_ACCOUNT_SID:TWILIO_AUTH_TOKEN' | base64_encode }}{% endraw %}`

必ず と `TWILIO_AUTH_TOKEN` を Twilio ダッシュボードの値に置き換え`TWILIO_ACCOUNT_SID`てください。最後に、Twilio の API エンドポイントは HTTP POST リクエストを期待しているため、 *[HTTP メソッド]* のドロップダウンでそのオプションを選択します。

![Webhook方式][30]

## リクエストのプレビュー

Webhook コンポーザーを使用して、ランダムなユーザーまたは特定の資格情報を持つユーザーの要求をプレビューし、要求が正しくレンダリングされていることを確認します。

![Webhook プレビュー][31]

[20]: https://www.twilio.com/docs/api/rest/sending-messages
[28]: {% image_buster /assets/img_archive/Twilio_Console.png %}
[29]: {% image_buster /assets/img_archive/Webhook_Body.png %}
[30]: {% image_buster /assets/img_archive/Webhook_Method.png %}
[31]: {% image_buster /assets/img_archive/Webhook_Preview.png %}
[32]: https://en.wikipedia.org/wiki/Basic_access_authentication#Client_side
