---
nav_title: 電話番号の取得
article_title: 電話番号取得
page_order: 3
description: "この記事では、Twilio と Infobip から電話番号を取得する方法について説明します。"
page_type: reference
channel:
  - WhatsApp
---

# 電話番号の取得

> WhatsApp メッセージングチャネルを使用するには、[Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) または [On-Premises API](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers) の要件を満たす電話番号が必要です。

電話番号は自分で取得する必要があります。Brazeは番号を提供しません。ビジネス電話プロバイダーを通じて物理的な電話をSIMカード付きで購入するか、当社のパートナーの1つを使用することができます。Twilio または Infoblip。**Twilio または Infobip のアカウントを持っていなければなりません。これは Braze を通じて行うことはできません。**

## WhatsApp API 要件

お使いの電話番号は、これらのWhatsApp API要件を満たしている必要があります:

- お客様のビジネスが所有する番号である 
- 国番号と市外局番を持っている（例えば、固定電話と携帯電話番号）
- 音声通話やSMSを受信可能
- アカウント設定中にアクセス可能（認証コードを受け取るため）
- 短いコードではありません
- 以前にWhatsAppビジネスプラットフォームで使用されていません
- 個人のWhatsAppアカウントに接続されていません

## Twilioの電話番号を取得する

### ステップ 1: TwilioコンソールまたはAPIから電話番号を購入する

1. Twilioコンソールから、**開発** > **電話番号** > **管理** > **番号を購入** に移動します。このオプションが表示されない場合は、**製品を探す**を選択し、**スーパー ネットワーク**までスクロールして、**電話番号** > **番号を購入**を選択します。<br><br>![「開発」タブが開かれ、「番号を購入」オプションが表示されているTwilioコンソール。]({% image_buster /assets/img/whatsapp/develop_buy_number.png %}){: style="max-width:20%;"}<br><br>

2. 目的の市外局番または地域 （該当する場合） を入力します。数字を見つけて、**購入**を選択します。<br><br> ![記載の電話番号を購入するボタン。]({% image_buster /assets/img/whatsapp/buy.png %})<br><br>

3. 電話番号を購入した後、**Active Numbers**に移動して、購入したばかりの電話番号を選択します。<br><br>![購入した電話番号を示す「アクティブ番号」。]({% image_buster /assets/img/whatsapp/active_numbers.png %}){: style="max-width:70%;"}<br><br>

### ステップ 2: 電話番号を設定する

Twilioの指示に従って、[Twilio Voice Onlyを使ってTwilioの電話番号を設定し、認証コードをメールで受け取る](https://www.twilio.com/docs/whatsapp/self-sign-up#verify-your-whatsapp-sender)。**それ以外のステップの指示には従わないでください。この電話番号は Braze ではなく Twilio に接続する必要があります。**

{% alert warning %}
**Twilioの指示に従って確認コードを受け取ってください。**

Twilio の指示にある以下の手順に従うと、電話番号を Twilio に接続できます。つまり、移行を行うか、別の番号を購入しない限り、その番号をBrazeに接続することはできません。
{% endalert %}

### ステップ 3: 埋め込みサインアップワークフローを完了する

1. Twilioの設定が完了したら、Brazeのダッシュボード > **Technology Partners** > **WhatsApp** に移動し、**Begin integration** または **Add WhatsApp Business Account** のいずれかが表示された方を選択して、[embedded sign up workflow]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/) をトリガーします。<br><br>「**WhatsAppの電話番号を追加する**」ステップで、電話番号の確認方法として「**電話**」を選択します。<br><br>![テキストメッセージまたは電話で電話番号を確認するオプションがあるセクション。]({% image_buster /assets/img/whatsapp/verify.png %}){: style="max-width:50%;"}<br><br>

2. 認証コードがメールの受信トレイに送信されるまで数分待ってから、認証コードを入力して設定を完了してください。

## Infobipの電話番号を取得する 

1. Infobipコンソールで、**チャネルと番号**に移動し、**番号**を選択します。<br><br>![Infoblip の「Channels and Numbers」セクションに表示された「Numbers」。]({% image_buster /assets/img/whatsapp/infoblip_numbers.png %}){: style="max-width:30%;"}<br><br>

2. **購入番号**を選択 > メッセージを送信したい国を選択 > **SMS**。<br><br>![番号を購入するボタン。]({% image_buster /assets/img/whatsapp/infoblip_buy.png %})<br><br>

3. 選択した国によっては、追加の登録手続き（米国の電話番号の場合は10 DLCまたはフリーダイヤルオプションの選択など）が必要になる場合があります。利用可能なオプションを選択してください。<br><br>![番号の種類を選択するように求めるページ: 10 DLC またはフリーダイヤルのいずれか。]({% image_buster /assets/img/whatsapp/infoblip_10dlc.png %}){: style="max-width:70%;"}<br><br>

4. 利用可能なオファーを選択し、残りの手順を進めて、リクエストが処理されるのを待ちます。**Numbers** > **My Request** に移動してステータスを確認できます。<br><br>![料金や補償を含む情報を提供するオファー。]({% image_buster /assets/img/whatsapp/infoblip_offer.png %}){: style="max-width:70%;"}<br><br>

5. 選択した国によっては、Infobipチームからの登録詳細の連絡を待つ（米国の10DLCの場合など）。<br><br>

6. Infobipで電話番号の準備ができたら、Brazeのダッシュボード > **Technology Partners** > **WhatsApp** に移動し、**Begin integration** または **Add WhatsApp Business Account** のいずれかが表示されたら選択して、[embedded sign up workflow]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/) をトリガーします。<br><br> **WhatsApp**のステップで電話番号を追加するには、電話番号の確認方法として**テキストメッセージ**を選択します。<br><br>![テキストメッセージまたは電話で電話番号を確認するためのオプションがあるセクション。]({% image_buster /assets/img/whatsapp/infoblip_verify.png %})<br><br>

7. Infobipの[ログを分析](https://www.infobip.com/docs/analyze/analyze-logs)して、顧客ポータルで確認コードを確認してください。表示されるまでに数分かかる場合がありますので、その後、確認コードを入力してセットアップを完了してください。




