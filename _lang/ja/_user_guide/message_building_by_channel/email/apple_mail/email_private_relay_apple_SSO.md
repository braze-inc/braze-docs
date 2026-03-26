---
nav_title: Apple Private Relayにメールを送る
article_title: Apple Private Relayにメールを送る
alias: /email_relay/
page_order: 0
description: "この記事では、Apple Private Relayにメールを送信する手順について説明します。"
channel:
  - email
toc_headers: h2
---

# Apple Private Relayにメールを送る

> Apple のシングルサインオン (SSO) 機能を使用すると、ユーザーは自分のメールアドレス (`example@icloud.com`) を共有するか、パーソナルメールアドレスの代わりにマスキングされたアドレス (`tq1234snin@privaterelay.appleid.com`) をブランドに提供してメールアドレスを非公開にすることができます。Apple は、リレーアドレスに送信されたメッセージをユーザーの実際のメールアドレスに転送します。 

Apple のプライベートメールリレーにメールを送信するには、送信ドメインを Apple に登録してください。Apple でドメインを設定しないと、リレーアドレスに送信されたメールはバウンスされます。

ユーザーがアプリのリレーメールへのメール転送を無効にした場合、Braze は通常通りメールのバウンス情報を受信します。これらのユーザーは、Apple ID の設定ページから、Apple でサインインを使用するアプリを管理できます（[Apple のドキュメント](https://support.apple.com/en-us/HT210426)を参照してください）。

{% tabs %}
{% tab SendGrid %}

## SendGrid の設定 

SendGrid をメールプロバイダーとして使用している場合、DNS を変更せずに Apple にメールを送信できます。 

1. [Apple Developer Portal](https://developer.apple.com/) にログインします。
2. **Certificates, Identifiers & Profiles** ページに移動します。
3. **Services** > **Sign in with Apple for Email Communication** を選択します。
4. **Email Sources** セクションで、ドメインとサブドメインを追加します。
- アドレスは `bounces+<YOUR_UID>@<YOUR_WHITELABELED_SUBDOMAIN_AND_DOMAIN>` の形式にする必要があります（例: `bounces+1234567@braze.online.docs.com`）。 

希望する「From」アドレスが `abmail` アドレスの場合、サブドメインにそれを含めてください。例えば、`docs.braze.com` の代わりに `abmail.docs.braze.com` を使用します。

{% endtab %}
{% tab SparkPost %}

## SparkPost の設定 

SparkPost 用の Apple Private Relay を設定するには、以下の手順に従います： 

1. Apple でサインインします。
2. [Apple のドキュメント](https://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service)に従って、メールドメインを登録します。
3. Apple は自動的にドメインをチェックし、検証済みのドメインを表示して、再検証または削除するオプションを提供します。

### 送信ドメインがバウンスドメインでもある場合

送信ドメインがバウンスドメインとしても使用されている場合、レコードを保存することはできず、以下の追加手順に従う必要があります：

1. ドメインが既に SparkPost で検証されている場合は、MX および TXT レコードを作成する**必要があります**： 

| インスタンス | MX レコード                   | TXT レコード                                    |
|----------|-----------------------------|-----------------------------------------------|
| 米国       | `smtp.sparkpostmail.com`    | `"v=spf1 redirect=_spf.sparkpostmail.com"`    |
| 欧州       | `smtp.eu.sparkpostmail.com` | `"v=spf1 redirect=_spf.eu.sparkpostmail.com"` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert important %}
SPF の失敗を回避するには、CNAME レコードを削除する**前に** MX レコードと TXT レコードを作成し、DNS に反映させる必要があります。
{% endalert %}

{:start="2"}
2. CNAME レコードを削除します。
3. 適切なルーティングのために、MX レコードと TXT レコードに置き換えます。
4. CDN またはファイルホスティングを参照する A レコードを作成します。

{% endtab %}
{% tab Amazon SES %}

## Amazon SES の設定

### カスタム MAIL FROM ドメインの設定

Amazon Simple Email Service (SES) 用の Apple Private Relay を設定するには、まず SES でカスタム MAIL FROM ドメインを設定する必要があります。詳細については、[AWS のドキュメント](https://docs.aws.amazon.com/ses/latest/dg/mail-from.html)を参照してください。

### Apple へのドメイン登録

1. Apple でサインインします。
2. [Apple のドキュメント](https://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service)に従って、メールドメインを登録します。
3. Apple は自動的にドメインをチェックし、検証済みのドメインを表示して、再検証または削除するオプションを提供します。

{% endtab %}
{% endtabs %}

さらにご不明な点がある場合は、[サポートチケット]({{site.baseurl}}/braze_support/)を作成してください。