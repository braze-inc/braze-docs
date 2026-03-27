---
nav_title: 電話番号の取得
article_title: 電話番号取得
page_order: 4
description: "この参照記事では、Twilio と Infobip から電話番号を取得する方法について説明します。"
page_type: reference
channel:
  - WhatsApp
---

# 電話番号の取得

> WhatsApp メッセージングチャネルを使用するには、WhatsApp の [Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) または [On-Premises API](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers) の要件を満たす電話番号が必要です。

電話番号はご自身で取得する必要があります。Braze が番号を提供することはありません。ビジネス電話プロバイダーを通じて SIM カード付きの物理的な電話を購入するか、当社のパートナーである Twilio または Infobip を利用できます。**Twilio または Infobip のアカウントをお持ちである必要があります。Braze を通じて行うことはできません。**

## WhatsApp API 要件

お使いの電話番号は、以下の WhatsApp API 要件を満たしている必要があります:

- お客様のビジネスが所有する番号である
- 国番号と市外局番を持っている（固定電話や携帯電話番号など）
- 音声通話や SMS を受信可能である
- アカウント設定中にアクセス可能である（認証コードを受け取るため）
- ショートコードではない
- 以前に WhatsApp ビジネスプラットフォームで使用されていない
- 個人の WhatsApp アカウントに接続されていない

## Twilio の電話番号を取得する

### ステップ 1: Twilio コンソールまたは API から電話番号を購入する

1. Twilio コンソールから、**Develop** > **Phone Numbers** > **Manage** > **Buy a number** に移動します。このオプションが表示されない場合は、**Explore Products** を選択し、**Super Networks** までスクロールして、**Phone Number** > **Buy a number** を選択します。<br><br>![「Develop」タブが開かれ、「Buy a number」オプションが表示されている Twilio コンソール。]({% image_buster /assets/img/whatsapp/develop_buy_number.png %}){: style="max-width:20%;"}<br><br>

2. 希望する市外局番または地域（該当する場合）を入力します。番号を見つけて、**Buy** を選択します。<br><br> ![記載の電話番号を購入するボタン。]({% image_buster /assets/img/whatsapp/buy.png %})<br><br>

3. 電話番号を購入した後、**Active Numbers** に移動して、購入したばかりの電話番号を選択します。<br><br>![購入した電話番号を示す「Active Numbers」。]({% image_buster /assets/img/whatsapp/active_numbers.png %}){: style="max-width:70%;"}<br><br>

### ステップ 2: 電話番号を設定する

Twilio の指示に従って、[Twilio Voice](https://www.twilio.com/docs/whatsapp/self-sign-up#add-your-whatsapp-phone-number) を**のみ**使用してメールで認証コードを受信できるよう Twilio の電話番号を設定します。**それ以外のステップの指示には従わないでください。**

{% alert warning %}
Twilio の指示に従って認証コードを受け取る手順のみを実行してください。
次のステップの指示に従うと、電話番号が Twilio に接続されます。つまり、移行を行うか別の番号を購入しない限り、その番号を Braze に接続することはできません。
{% endalert %}

1. Twilio コンソールで、[Active Numbers ページ](https://www.twilio.com/console/phone-numbers/incoming)に移動し、購入した電話番号を選択します。
2. **Voice Configuration** セクションに移動し、**Configure with** ドロップダウンで **Webhook, TwiML Bin, Function, Studio Flow, Proxy Service** を選択します。
3. **A call comes in** の行で **Webhook** を選択し、URL を `https://twimlets.com/voicemail?Email=YOUR_EMAIL_ADDRESS` に設定します。`YOUR_EMAIL_ADDRESS` はご自身のメールアドレスに置き換えてください。
4. Twilio コンソールで、**2. Link WhatsApp Business Account with your number** > **2. Copy the phone number you register** に移動し、電話番号の横にある **Copy** を選択します。
5. **Self Sign-up** ウィンドウの **Add your WhatsApp phone number** ページで、**Add a new phone number** を選択し、電話番号を貼り付けます。
6. 認証方法として **Phone call** を選択し、**Next** を選択します。
7. 10 分以内にメールで認証コードが届きます。

### ステップ 3: 埋め込みサインアップワークフローを完了する

1. Twilio の設定が完了したら、Braze のダッシュボード > **テクノロジーパートナー** > **WhatsApp** に移動し、**Begin integration** または **Add WhatsApp Business Account** のいずれか表示された方を選択して、[埋め込みサインアップワークフロー]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/)をトリガーします。<br><br>**Add a phone number for WhatsApp** のステップで、電話番号の確認方法として **Phone call** を選択します。<br><br>![テキストメッセージまたは電話で電話番号を確認するオプションがあるセクション。]({% image_buster /assets/img/whatsapp/verify.png %}){: style="max-width:50%;"}<br><br>

2. 認証コードがメールの受信トレイに送信されるまで数分待ってから、認証コードを入力して設定を完了します。

## Infobip の電話番号を取得する

1. Infobip コンソールで、**Channels and Numbers** に移動し、**Numbers** を選択します。<br><br>![Infobip の「Channels and Numbers」セクションに表示された「Numbers」。]({% image_buster /assets/img/whatsapp/infoblip_numbers.png %}){: style="max-width:30%;"}<br><br>

2. **Buy Number** を選択 > メッセージを送信したい国を選択 > **SMS** を選択します。<br><br>![番号を購入するボタン。]({% image_buster /assets/img/whatsapp/infoblip_buy.png %})<br><br>

3. 選択した国によっては、追加の登録手続き（米国の電話番号の場合は 10DLC またはフリーダイヤルオプションの選択など）が必要になる場合があります。利用可能なオプションを選択してください。<br><br>![番号の種類を選択するように求めるページ: 10DLC またはフリーダイヤルのいずれか。]({% image_buster /assets/img/whatsapp/infoblip_10dlc.png %}){: style="max-width:70%;"}<br><br>

4. 利用可能なオファーを選択し、残りのステップを進めて、リクエストが処理されるのを待ちます。**Numbers** > **My Request** に移動してステータスを確認できます。<br><br>![料金やカバレッジなどの情報を含むオファー。]({% image_buster /assets/img/whatsapp/infoblip_offer.png %}){: style="max-width:70%;"}<br><br>

5. 選択した国に応じて、Infobip チームから登録の詳細（米国での 10DLC など）について連絡があるのを待ちます。<br><br>

6. Infobip で電話番号の準備ができたら、Braze のダッシュボード > **テクノロジーパートナー** > **WhatsApp** に移動し、**Begin integration** または **Add WhatsApp Business Account** のいずれか表示された方を選択して、[埋め込みサインアップワークフロー]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/)をトリガーします。<br><br>**Add a phone number for WhatsApp** のステップで、電話番号の確認方法として **Text message** を選択します。<br><br>![テキストメッセージまたは電話で電話番号を確認するオプションがあるセクション。]({% image_buster /assets/img/whatsapp/infoblip_verify.png %})<br><br>

7. Infobip のカスタマーポータルで [analyze logs](https://www.infobip.com/docs/analyze/analyze-logs) を確認して認証コードを取得します。表示されるまでに数分かかる場合があります。認証コードを入力してセットアップを完了します。