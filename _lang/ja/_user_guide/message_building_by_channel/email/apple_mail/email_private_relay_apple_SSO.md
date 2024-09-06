---
nav_title: Appleプライベートリレーにメールを送信する
article_title: Appleプライベートリレーにメールを送信する
alias: /email_relay/
page_order: 0
description: "この記事では、Apple Private Relayにメールを送信する手順について説明する。"
channel:
  - email
  
---

# Apple Private Relayにメールを送信する

> iOS13のリリースに伴い、アップルはアップル顧客向けに、電子メールの送信方法に影響を与える機能を導入した。アップルのシングルサインオン（SSO）機能は、ユーザーがメールアドレスを共有したり（`example@icloud.com` ）、個人的なメールアドレスではなくブランドに提供されるものをマスキングしてメールアドレスを隠したり（`tq1234snin@privaterelay.appleid.com` ）することを可能にする。

これらのユーザーは、Apple IDの設定ページから、Appleとのサインインを使用するアプリを管理することができる（[Appleのドキュメントを](https://support.apple.com/en-us/HT210426)参照）。ユーザーがアプリのリレーメールへのメール転送を無効にした場合、Brazeは通常通りメールのバウンス情報を受信する。アップルのプライベート・メール・リレーにメールを送信するには、送信ドメインをアップルに登録する。

## SendGridでメールを送信する

メールプロバイダとしてSendGridを使用している場合、DNSを変更することなくアップルにメールを送信することができる。**アップル証明書の**ページにアクセスし、アップルのEメール・リレー・サービス経由で送信するために使用するEメールアドレスを許可する（希望の「From」アドレス）。  

![]({% image_buster /assets/img/email-relay-whitelabel-address.png %}) アップル証明書ページで個々のメールアドレスを許可するオプション。

アドレスの書式は次のようにする：`bounces+<YOUR_UID>@<YOUR_WHITELABELED_SUBDOMAIN_AND_DOMAIN>`(e.g.,`bounces+1234567@braze.online.docs.com`).Apple証明書ページにアドレスが追加されると、このドメインからのメールはApple Private Relayシステム経由で配信される。

{% alert important %}
希望する "From "アドレスが`abmail` の場合、サブドメインにそのアドレスを含める。例えば、`docs.braze.com` の代わりに`abmail.docs.braze.com` を使う。あなたの住所はそうではないかもしれない。SendGridのDNSレコードを確認する。
{% endalert %}

### アドレスの値

Apple Private Relayでメールアドレスを追加する際に使用するコンポーネントについては、この表を参照のこと。

| 価値 | 説明 |
|---|---|
| UID | この値は、Brazeが（SendGridから）提供するDNSレコードで提供される。メールアドレスのUIDに「u」を含めないこと。例えば、あなたのUIDがSendGridで`u1234567.wl134.sendgrid.net` と表示されている場合、`1234567` がUID値である。<br><br> DNSレコードにアクセスできない場合は、Brazeカスタマーサクセスマネージャーに連絡してUIDを提供してもらう。 |
| ホワイトラベル付きサブドメインとドメイン | SendGridに入力した最初のドメインとサブドメイン。SendGridのDNSレコードで**HOST値を**使用することもできる。 |
{: .reset-td-br-1 .reset-td-br-2}

## SparkPostのメールを送信する

SparkPost用のApple Private Relayを設定するには、以下の手順に従う： 

1. Appleでサインインする。 
2. Eメールのドメインを追加する。 
3. アップルは自動的にドメインをチェックし、どのドメインが確認済みかを表示し、ドメインを修正または削除するオプションを提供する。

{% alert important %}
検証ファイルが作成されてから2〜3日以内にこのプロセスを完了させなければならない。アップルは有効期間を明らかにしていない。
{% endalert %}

さらに質問がある場合は、[サポートチケットを]({{site.baseurl}}/braze_support/)開く。
