---
nav_title: Braze の SSL
article_title: SSLの概要
page_order: 5
page_type: reference
description: "この参考記事では、SSLについて、その使用目的、Brazeでの使用方法について説明します。"
channel: email

---

# Braze の SSL

{% multi_lang_include video.html id="zP1N_wN0SsQ" align="right" %}

> セキュアソケットレイヤー（SSL）は、URLをHTTPではなくHTTPSで暗号化します。HTTPSは、有効で信頼できるSSLまたはTLS証明書が存在し、そのWeb サイトが安全にアクセスできることを示します。

## なぜSSLが重要なのか？

ほとんどのドメインはSSLを必要としませんが、Brazeは以下の理由からSSLの使用を強く推奨しています。

Web サイトやリンクをSSLで保護することは、機密性の高い顧客情報を直接扱わない企業でも一般的に行われています。SSLで保護されたリンクはユーザーからの信頼度が高く、認証のレイヤーが増えることでデータの保護に役立ちます。

### クリックと開封のトラッキングに必要

Brazeは、クリック数と開封をトラッキングするために、ブランド化されたリンクトラッキングサブドメインを使用してリンクを変換します。デフォルトでは、これらのリンクはHTTPで始まります。非セキュアな通信を制限するブラウザや拡張機能を使用しているユーザーは、たとえURLがセキュアであっても、送信先URLへのリダイレクトを通過できない可能性があります。これにより画像が破損したり、トラッキングが不正確になったりすることがあります。リンクトラッキングサブドメインにSSLを適用して、安全なリダイレクトを確保してください。

### ブラウザの要件

Google Chromeなどの主要ブラウザは、ユーザーを保護するため、非セキュアなURL経由の通信を制限しています。SSLを使用することで、コンテンツが信頼できるものであることを確認でき、メール内のリンク切れや画像の表示不良といった問題を最小限に抑えられます。

### HSTSドメインの要件 

HTTP Strict Transport Security（HSTS）ドメインをお持ちの場合は、SSLを設定し、必要なセキュリティ証明書を送信するようにCDNを構成してください。SSLがないと、画像やWebリンクが壊れます。

## SSL証明書を取得する

SSL証明書はサードパーティ、通常はコンテンツ配信ネットワーク（CDN）を通じて取得します。CDNは証明書をホストし、ユーザーがリンクをクリックした際に、トラフィックをCDN経由でリダイレクトして証明書を適用してから、SendGridやSparkPostに送信することでブラウザに証明書を提供します。

SSL設定を開始するには、Brazeのカスタマーサクセスマネージャーに連絡し、Brazeメールの完全な設定の開始を依頼してください。

Brazeが設定を開始したら、以下のステップに従ってください：
1. Brazeが、ドメインレジストリに追加するDNSレコードを提供します。
2. Brazeが、レコードがレジストリに正しく追加されているかどうかを確認します。
3. その後、CDNを選択し、サードパーティのプロバイダーからSSL証明書を取得します。 
4. この時点で、CDNを設定します。なお、BrazeではCDN設定のトラブルシューティングをサポートできません。追加のサポートが必要な場合は、CDNプロバイダーにお問い合わせください。
5. SSLを有効にするには、カスタマーサクセスマネージャーにご連絡ください。

### CDNとは何か、なぜ必要なのか？

コンテンツ配信ネットワーク（CDN）とは、複数のメディアにわたってコンテンツの迅速な読み込みを実現すると同時に、セキュリティ証明書も処理するサーバー群のプラットフォームです。 

{% alert important %}
CDNの設定は、常にBrazeによってDNSレコードが検証された後に行います。このステップをまだ開始していない場合は、カスタマーサクセスマネージャーに連絡し、開始方法の詳細を確認してください。
{% endalert %}

クリックと開封のトラッキングでは、配信パートナーがリンクをブランド化されたサブドメインで変換し、CDNがその変換されたリンクにSSL証明書を適用します。パートナーは、リンクや画像が正しく表示されるように、受信者のブラウザに有効な証明書を提示しなければならないことが多くあります。Brazeは証明書を要求したり管理したりしないため、CDNを通じて設定する必要があります。 

{% alert note %}
リストされたCDNでSSLクリックと開封のトラッキングが使えない、あるいは使いたくない場合は、カスタムSSL設定を構築できます。代替CDNやカスタムプロキシは、より複雑な設定になる可能性があります。[SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/)と[SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/)のドキュメントを参照してください。
{% endalert %}

#### その他のリソース

{% alert important %}
CDN設定のトラブルシューティングについては、CDNプロバイダーにお問い合わせください。
{% endalert %}

特定のCDNの設定方法については、ESPパートナーが提供する以下のリソースを参照してください。お使いのCDNがリストにない場合もありますが、CDNにSSL証明書を適用する機能があることを確認する必要があります。

**SendGrid**

- [AWS Cloudfront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront)
- [CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare)
- [Fastly](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly)
- [KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn)

**SparkPost**
- [AWS Cloudfront](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-aws-cloudfront)
- [CloudFlare](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare)
- [Fastly](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly)
- [Google Cloud Platform](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-google-cloud-platform)
- [Microsoft Azure](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-microsoft-azure) 

**Amazon SES:**
- [Configuring custom domains to handle open and click tracking](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html)を参照し、Brazeクラスターに基づいてリージョンごとにAWSトラッキングドメインを指定してください：
    - **Braze USクラスター:** `r.us-east-1.awstrack.me`
    - **Braze EUクラスター:** `r.eu-central-1.awstrack.me`
- [AWS Cloudfront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html)
- [CloudFlare](https://developers.cloudflare.com/ssl/get-started/)
- [Fastly](https://www.fastly.com/documentation/guides/getting-started/domains/securing-domains/setting-up-tls-with-certificates-fastly-manages/)
- [KeyCDN](https://www.keycdn.com/support/how-to-setup-custom-ssl)
- [Google Cloud](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs)


{% alert important %}
CDNのクリックトラッキングドメインを設定する際は、ホストヘッダー攻撃などの潜在的なセキュリティ問題を防止するため、`X-Forwarded-Host`ヘッダーを有効にしてください。手順については、CDNのドキュメントまたはサポートチームを参照してください。
{% endalert %}

#### トラブルシューティング

CDNの設定や証明書、プロキシの問題はCDNプロバイダーに対応を依頼してください。ここでは、一般的なSSLクリックトラッキングの問題を特定するためのヒントを紹介します。

##### ドメインレジストリの問題

digコマンドを実行して、リンクトラッキングがCDNを指していることを確認します。ターミナルで`dig CNAME link_tracking_subdomain`を実行してください。`ANSWER SECTION`に、CNAMEレコードが指す先が表示されます。メールサービスプロバイダー (ESP)（SendGridやSparkPost）を指していて、CDNを指していない場合は、ドメインレジストリを再設定してCDNを指すようにしてください。

##### CDNの問題

設定中にメールのライブリンクが機能しなくなった場合、適切な設定を行う前にDNSをCDNに向けてしまった可能性が高いです。これは「間違ったリンク」エラーとして表示されることがあります。CDNプロバイダーに連絡し、設定のトラブルシューティングのためにドキュメントを確認してください。

##### SSL有効化ステータス

SSLの設定を完了してもリンクがHTTPとして表示される場合は、Brazeのカスタマーサクセスマネージャーに連絡し、BrazeがSSLを有効にしていることを確認してください。Brazeは、すべての設定ステップが完了した後にのみSSLを有効にします。