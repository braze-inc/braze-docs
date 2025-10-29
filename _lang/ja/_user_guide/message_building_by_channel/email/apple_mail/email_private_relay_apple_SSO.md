---
nav_title: Apple Private Relayにメールを送信する
article_title: Apple Private Relay へのメール送信
alias: /email_relay/
page_order: 0
description: "この記事では、Apple Private Relayにメールを送信する手順について説明する。"
channel:
  - email
  
---

# Apple Private Relayにメールを送信する

> Apple のシングルサインオン (SSO) 機能は、ユーザーがメールアドレスを共有したり (`example@icloud.com`)、個人のメールアドレスではなくブランドに提供されるものをマスキングしてメールアドレスを隠したり (`tq1234snin@privaterelay.appleid.com`) することを可能にします。アップルは、リレーアドレスに送信されたメッセージをユーザの実際のメールアドレスに転送します。 

Apple のプライベートメールリレーにメールを送信するには、送信ドメインを Apple に登録します。Apple でドメインを設定しないと、リレーアドレスに送信されたメールがバウンスされます。

ユーザーがアプリのリレーメールへのメール転送を無効にした場合、Brazeは通常通りメールのバウンス情報を受信する。これらのユーザーは、Apple ID の設定ページから、Apple へのサインインを使用するアプリを管理することができます ([Apple のドキュメント](https://support.apple.com/en-us/HT210426)を参照してください)。

## SendGridでメールを送信する

SendGrid をメールプロバイダーとして使用している場合、DNS を変更せずに Apple にメールを送信することができます。 

1. [Apple Developer Portalにログインします](https://developer.apple.com/)
2. **証明書、識別子& プロファイルの**ページにアクセスする。
3. [**Services**] > [**Sign in with Apple for Email Communication**] を選択します。
4. [**Email Sources**] セクションで、ドメインとサブドメインを追加します。
- アドレスは、`bounces+<YOUR_UID>@<YOUR_WHITELABELED_SUBDOMAIN_AND_DOMAIN>` (例: `bounces+1234567@braze.online.docs.com`) の形式にする必要があります。 

希望する "From "アドレスが`abmail` の場合、サブドメインにそのアドレスを含める。例えば、`docs.braze.com` の代わりに`abmail.docs.braze.com` を使う。

## SparkPostのメールを送信する

SparkPost用のApple Private Relayを設定するには、以下の手順に従う： 

1. Appleでサインインする。
2. [Appleのドキュメント](https://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service)に従って、メールドメインを登録します。
3. Appleは自動的にドメインをチェックし、どのドメインが検証されているかを表示し、ドメインを元に戻すか削除するオプションを提供します。

### 考慮事項

送信ドメインがバウンスドメインとしても使用されている場合、レコードを保存することはできず、次の追加手順に従う必要があります。

1. ドメインが既に SparkPost で検証されている場合は、MX および TXT レコードを作成する**必要があります**。 

| インスタンス | MX レコード                   | TXT レコード                                    |
|----------|-----------------------------|-----------------------------------------------|
| 米国       | `smtp.sparkpostmail.com`    | `"v=spf1 redirect=_spf.sparkpostmail.com"`    |
| 欧州       | `smtp.eu.sparkpostmail.com` | `"v=spf1 redirect=_spf.eu.sparkpostmail.com"` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert important %}
SPF 失敗を回避するには、MX レコードとTXT レコードを作成し、CNAME レコードを削除する**前に** DNS に反映する必要があります。
{% endalert %}

{:start="2"}
2\.CNAME レコードを削除します。
3\.正しくルーティングするために、MX レコードとTXT レコードに置き換えます。
4\.CDN またはファイルホスティングを参照するレコードを作成します。

さらにご不明な点がある場合は、[サポートチケット]({{site.baseurl}}/braze_support/)を作成してください。
