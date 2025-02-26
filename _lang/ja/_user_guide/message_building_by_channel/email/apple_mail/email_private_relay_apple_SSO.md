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

> Apple のシングルサインオン (SSO) 機能は、ユーザーがメールアドレスを共有したり (`example@icloud.com`)、個人のメールアドレスではなくブランドに提供されるものをマスキングしてメールアドレスを隠したり (`tq1234snin@privaterelay.appleid.com`) することを可能にします。アップルは、リレーアドレスに送信されたメッセージをユーザの実際のメールアドレスに転送します。 

Apple のプライベートメールリレーにメールを送信するには、送信ドメインを Apple に登録します。Apple でドメインを設定しないと、リレーアドレスに送信されたメールがバウンスされます。

ユーザーがアプリのリレーメールへのメール転送を無効にした場合、Brazeは通常通りメールのバウンス情報を受信する。これらのユーザーは、Apple ID の設定ページから、Apple へのサインインを使用するアプリを管理することができます ([Apple のドキュメント](https://support.apple.com/en-us/HT210426)を参照してください)。

## SendGridでメールを送信する

SendGrid をメールプロバイダーとして使用している場合、DNS を変更せずに Apple にメールを送信することができます。 

1. [**Apple Certificate**] ページにアクセスし、Apple のメールリレーサービス経由での送信に使用するメールアドレス (希望の「差出人」アドレス) を許可します。
- アドレスは、`bounces+<YOUR_UID>@<YOUR_WHITELABELED_SUBDOMAIN_AND_DOMAIN>` (例: `bounces+1234567@braze.online.docs.com`) の形式にする必要があります。 

![Apple Certificate ページで個々のメールアドレスを許可するオプション。]({% image_buster /assets/img/email-relay-whitelabel-address.png %})

{:start="2"}
2\.Apple証明書ページにアドレスが追加されると、このドメインからのメールはApple Private Relayシステム経由で配信される。

{% alert important %}
希望する "From "アドレスが`abmail` の場合、サブドメインにそのアドレスを含める。例えば、`docs.braze.com` の代わりに`abmail.docs.braze.com` を使う。
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
2. [Apple のドキュメント](https://developer.apple.com/sign-in-with-apple/get-started/) に基づいて、必要な検証ファイルを作成し、これらのファイルを指定されたドメインのアクセス可能なディレクトリにホストします。
3. 検証ファイルがホストされているドメインを指す DNS 設定にレコードを追加します。これは、1回限りの検証プロセスです。
4. Apple でメールドメインを追加します。
5. Apple が自動的にドメインをチェックし、どのドメインが検証済みかを表示し、ドメインを再検証または削除するオプションを提供します。

{% alert important %}
このプロセスは、検証ファイルが作成されてから2 ～3 日以内に完了するようにしてください。そうしないと、有効期限が切れます。Apple ではこの有効期間を開示していません。
{% endalert %}

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
