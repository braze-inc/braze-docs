---
nav_title: Braze の SSL
article_title: SSLの概要
page_order: 5
page_type: reference
description: "この参考記事では、SSLについて、その使用目的、Brazeでの使用方法について説明する。"
channel: email

---

# Braze の SSL

{% multi_lang_include video.html id="zP1N_wN0SsQ" align="right" %}

> セキュアソケットレイヤ(SSL) は、HTTP ではなくHTTPS を使用してURL を暗号化します。HTTPS は、有効で信頼できるSSL またはTLS 証明書が存在し、Web サイトを安全に訪問できることを示します。

## なぜSSLが重要なのか？

ほとんどのドメインはSSL を必要としませんが、Braze ではこれらの理由からSSL の使用を強くお勧めします。

ウェブサイトやリンクをSSLで保護することは、機密性の高い顧客情報を直接扱わない企業でも一般的に行われている。SSLで保護されたリンクはユーザーからの信頼度が高く、認証のレイヤーが増えることでデータの保護に役立つ。

### クリックと開封の追跡に必要

Braze は、ブランド化されたリンク"トラッキングサブドメインを使用してリンクを変換し、クリックや開封を追跡します。デフォルトでは、これらのリンクはHTTP で始まります。非セキュアトラフィックを制限するブラウザまたは拡張機能を持つユーザは、URL がセキュアであっても、送信先 URL の前にリダイレクトを通過できない場合があります。これにより、"画像が破損し、キュレート "トラッキングが失われる可能性があります。SSL をリンク"トラッキングサブドメインに適用して、セキュアリダイレクトを確認します。

### ブラウザの要件

Google Chrome などの主要なブラウザは、ユーザーを保護するために、非セキュアURL を介してトラフィックを制限します。SSL を使用すると、コンテンツが信頼されていることを確認し、メール s のリンクの破損や"画像のような問題を最小限に抑えることができます。

### HSTSドメイン要件 

HTTP Strict Transport Security (HSTS) ドメインがある場合は、SSL を設定し、必要なセキュリティー証明書を送信するようにCDN を設定します。SSL を使用しないと、"画像とウェブリンクが切断されます。

## SSL証明書を取得する

通常はコンテンツデリバリネットワーク(CDN)を使用して、サードパーティからSSL 証明書を取得します。CDN は証明書をホストし、ユーザーがCDN 経由のトラフィックをアプリ ly 証明書 s にリダイレクトしてリンクをクリックしたときにブラウザーに提供してから、SendGrid またはSparkPost に送信します。

SSL 設定を開始するには、Braze 顧客の正常終了マネージャーに連絡して完全なBraze メール設定を開始します。

Braze が設定を開始した後、次のステップに従います。
1. Brazeは、ドメインレジストリに追加するDNSレコードを提供する。
2. Brazeは、レコードがレジストリに正しく追加されているかどうかを確認する。
3. この後、CDNを選択し、サードパーティーのプロバイダーからSSL証明書を取得する。 
4. この時点で、CDNを設定する。Braze は、CDN 設定のトラブルシューティングに役立ちません。詳細については、CDN プロバイダにお問い合わせください。
5. SSL を有効にするには、顧客のサクセスマネージャーに連絡してください。

### CDNとは何か、なぜ必要なのか？

コンテンツ配信ネットワーク(CDN)は、セキュリティ証明書を処理しながら、複数のメディアにわたるコンテンツの迅速な読み込む時間を確保するために役立つサーバーのプラットフォームです。 

{% alert important %}
CDNの設定は、常にBrazeによってDNSレコードが検証された後に行われる。このステップをまだ開始していない場合は、顧客のサクセスマネージャーに連絡して、開始方法を確認してください。
{% endalert %}

クリックと開封 "トラッキングの場合、配信パートナーはブランド化されたサブドメインを使用してリンクを変換し、CDN アプリはこれらの変換されたリンクへのSSL 証明書にあります。多くの場合、パートナーは受信者のブラウザーに有効な証明書を提示し、リンクと"画像を正しく表示する必要があります。Braze は証明書をリクエストまたは管理しないため、CDN を使用して設定する必要があります。 

{% alert note %}
SSL クリックアンド開封 "トラッキングにリストされたCDN を使用できない場合、または使用しない場合は、カスタムSSL 設定を設定できます。代替CDNまたはカスタムプロキシを使用すると、より複雑な設定になる場合があります。[SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/)および[SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/)ドキュメントを参照してください。
{% endalert %}

#### その他のリソース

{% alert important %}
CDN 設定のトラブルシューティングについては、CDN プロバイダにお問い合わせください。
{% endalert %}

以下の表に、ESP パートナーが作成した特定の CDN の設定方法に関するステップバイステップガイドを示します。特定のCDNがリストにない場合もあるが、CDNにSSL証明書を適用する機能があることを確認する必要がある。

| SendGrid | SparkPost |
| -------- | --------- |
| [AWS Cloudfront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront)<br>[CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare)<br>[Fastly](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly)<br>[KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) | [AWS Cloudfront](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-aws-cloudfront)<br>[CloudFlare](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare)<br>[Fastly](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly)<br>[Google Cloud Platform](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-google-cloud-platform)<br>[Microsoft Azure](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-microsoft-azure) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Amazon SES については、[オプション 2:HTTPS ドメイン](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) を設定し、Braze クラスターに基づいてリージョン別にAWS "トラッキングドメインを指定します。

- **Braze US クラスター:** `r.us-east-1.awstrack.me`
- **Braze EU クラスター:** `r.eu-central-1.awstrack.me`

{% alert important %}
CDN のクリック"トラッキングドメインを設定するときは、`X-Forwarded-Host` ヘッダーを有効にして、ホストヘッダー攻撃などの潜在的なセキュリティー問題を防ぎます。ステップについては、CDN ドキュメントまたはサポートチームを参照してください。
{% endalert %}

#### トラブルシューティング

CDN 設定、証明書 s、およびプロキシの問題をCDN で処理する必要がありますが、これらのヒントを使用して、一般的なSSL クリック"トラッキングの問題を特定します。

##### ドメイン・レジストリの問題

ダイグコマンドを実行して、リンク"トラッキングをCDN で指定することを確認します。ターミナルで`dig CNAME link_tracking_subdomain` を実行します。`ANSWER SECTION` の下で、CNAME がポイントする場所をリストします。CDN ではなくメール サービスプロバイダー(SendGrid またはSparkPost) を指している場合は、CDN を指し示すようにドメインレジストリを再設定します。

##### CDNの問題

設定中にライブメールリンクが切断された場合は、DNSをCDN に向けて設定する必要があります。これは「間違ったリンク」エラーとして表示されることがある。コンフィギュレーションのトラブルシューティングについては、CDN プロバイダーに連絡し、ドキュメントを確認してください。

##### SSL有効化ステータス

SSL 設定を完了し、まだHTTP としてアプリイヤーにリンクする場合は、Braze 顧客のサクセスマネージャーに連絡して、Brazeが有効なSSL を確認します。Braze は、すべての設定ステップが完了した後でのみSSL を有効にします。

