---
nav_title: Apple Private Relay へのメール送信
article_title: Apple Private Relay へのメール送信
alias: /email_relay/
page_order: 0
description: "この記事では、Apple Private Relayにメールを送信する手順について説明する。"
channel:
  - email
  
---

# Apple Private Relayにメールを送信する

> Apple では iOS 13 のリリースに伴い、同社の顧客向けメールが送信される方法に影響を与える機能を導入しました。Apple のシングルサインオン (SSO) 機能は、ユーザーがメールアドレスを共有したり (`example@icloud.com`)、個人のメールアドレスではなくブランドに提供されるものをマスキングしてメールアドレスを隠したり (`tq1234snin@privaterelay.appleid.com`) することを可能にします。

これらのユーザーは、Apple ID の設定ページから、Apple へのサインインを使用するアプリを管理することができます ([Apple のドキュメント](https://support.apple.com/en-us/HT210426)を参照してください)。ユーザーがアプリのリレーメールへのメール転送を無効にした場合、Brazeは通常通りメールのバウンス情報を受信する。Apple のプライベートメールリレーにメールを送信するには、送信ドメインを Apple に登録します。

## SendGridでメールを送信する

SendGrid をメールプロバイダーとして使用している場合、DNS を変更せずに Apple にメールを送信することができます。[**Apple Certificate**] ページにアクセスし、Apple のメールリレーサービス経由での送信に使用するメールアドレス (希望の「差出人」アドレス) を許可します。  

![Apple Certificate ページで個々のメールアドレスを許可するオプション。]({% image_buster /assets/img/email-relay-whitelabel-address.png %})

アドレスのフォーマットは次のようにします: `bounces+<YOUR_UID>@<YOUR_WHITELABELED_SUBDOMAIN_AND_DOMAIN>`(e.g., `bounces+1234567@braze.online.docs.com`)。Apple証明書ページにアドレスが追加されると、このドメインからのメールはApple Private Relayシステム経由で配信される。

{% alert important %}
希望する "From "アドレスが`abmail` の場合、サブドメインにそのアドレスを含める。例えば、`docs.braze.com` の代わりに`abmail.docs.braze.com` を使う。あなたの住所はそうではないかもしれない。SendGridのDNSレコードを確認する。
{% endalert %}

### 差出人アドレスの値

Apple Private Relayでメールアドレスを追加する際に使用するコンポーネントについては、この表を参照のこと。

| 値 | 説明 |
|---|---|
| UID | この値は、Braze が (SendGrid から) 提供する DNS レコードで提供されます。メールアドレスの UID に「u」の文字を含めることはできません。例えば、あなたのUIDがSendGridで`u1234567.wl134.sendgrid.net` と表示されている場合、`1234567` がUID値である。<br><br> DNSレコードにアクセスできない場合は、Brazeカスタマーサクセスマネージャーに連絡してUIDを提供してもらう。 |
| ホワイトラベル付きサブドメインとドメイン | SendGridに入力した最初のドメインとサブドメイン。SendGrid の DNS レコードで**HOST 値**を使用することもできます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## SparkPostのメールを送信する

SparkPost用のApple Private Relayを設定するには、以下の手順に従う： 

1. Appleでサインインする。 
2. メールのドメインを追加します。 
3. Apple が自動的にドメインをチェックし、どのドメインが検証済みかを表示し、ドメインを再検証または削除するオプションを提供します。

{% alert important %}
このプロセスは検証ファイルが作成されてから 2 〜 3 日以内に完了させる必要があります。そうでないと有効期限が切れます。Apple ではこの有効期間を開示していません。
{% endalert %}

さらにご不明な点がある場合は、[サポートチケット]({{site.baseurl}}/braze_support/)を作成してください。
