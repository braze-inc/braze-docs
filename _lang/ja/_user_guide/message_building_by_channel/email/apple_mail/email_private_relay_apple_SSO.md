---
nav_title: Apple プライベートリレーにメールを送信する
article_title: Apple プライベートリレーにメールを送信する
alias: /email_relay/
page_order: 0
description: "この記事では、Apple Private Relay に電子メールを送信するプロセスについて説明します。"
channel:
  - email
  
---

# Appleプライベートリレーにメールを送信する

> iOS 13 のリリースにより、Apple は Apple 顧客向けにメールの送信方法に影響を与える機能を導入しました。Appleのシングルサインオン（SSO）機能により、ユーザーはメールアドレスを共有できる（`example@icloud.com`) またはブランドに提供された情報をマスクしてメールアドレスを隠す (`tq1234snin@privaterelay.appleid.com`) を使用します。

これらのユーザーは、Apple ID 設定ページから Apple サインインを使用するアプリを管理できます ([Apple のドキュメント](https://support.apple.com/en-us/HT210426)を参照)。ユーザーがアプリのリレーメールへのメール転送を無効にすると、Braze は通常どおりメールの返信情報を受信します。Apple のプライベート メール リレーにメールを送信するには、送信ドメインを Apple に登録します。

## SendGrid のメール送信

SendGrid をメールプロバイダーとして使用すると、DNS を変更せずに Apple にメールを送信できます。**Apple 証明書** ページに移動し、Apple のメールリレーサービス経由で送信するために使用するメール アドレス (希望する「送信元」アドレス) を許可します。  

![Option to allowlist individual email addresses on the Apple Certificate page.]({% image_buster /assets/img/email-relay-whitelabel-address.png %})

アドレスは次のようにフォーマットする必要があります: `bounces+<YOUR_UID>@<YOUR_WHITELABELED_SUBDOMAIN_AND_DOMAIN>`（例えば、 `bounces+1234567@braze.online.docs.com`）。アドレスが Apple 証明書ページに追加されると、このドメインからのメールは Apple プライベートリレーシステム経由で配信されます。

{% alert important %}
希望する「差出人」アドレスが `abmail` アドレスがある場合は、それをサブドメインに含めます。例えば、 `abmail.docs.braze.com` の代わりに `docs.braze.com`。あなたの住所ではそうではないかもしれません。SendGrid で DNS レコードを確認してください。
{% endalert %}

### 送信元アドレスの値

Apple Private Relay を使用して電子メール アドレスを追加するときに使用するコンポーネントについては、この表を参照してください。

| 値 | 説明 |
|---|---|
| UID | この値は、Braze (SendGrid から) によって提供される DNS レコードで提供されます。電子メール アドレスの UID に文字「u」を含めないでください。たとえば、SendGridでUIDが次のように表示される場合 `u1234567.wl134.sendgrid.net`、 それから `1234567` UID 値です。<br><br> DNS レコードにアクセスできない場合は、Braze カスタマー サクセス マネージャーに連絡して UID を伝えてください。 |
| ホワイトラベル サブドメインとドメイン | SendGrid に入力した最初のドメインとサブドメイン。SendGrid の DNS レコードで **HOST 値** を使用することもできます。 |
{: .reset-td-br-1 .reset-td-br-2}

## SparkPost のメール送信

SparkPost 用に Apple プライベートリレーを設定するには、次の手順に従います。 

1. Appleでサインインします。 
2. 電子メールドメインを追加します。 
3. Apple は自動的にドメインをチェックし、検証済みのドメインを表示し、ドメインを再検証するか削除するかのオプションを提供します。

{% alert important %}
検証ファイルが作成されてから 2 ～ 3 日以内にこのプロセスを完了してください。完了しないと、検証ファイルは期限切れになります。Apple は、その有効期間を明らかにしていません。
{% endalert %}

さらに質問がある場合は、 [サポート チケットを]({{site.baseurl}}/braze_support/)開いてください。
