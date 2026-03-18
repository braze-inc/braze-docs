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

> セキュア・ソケット・レイヤー（SSL）は、URLをHTTPではなくHTTPSで暗号化する。HTTPSは、有効で信頼できるSSLまたはTLS証明書が存在し、そのWeb サイトが安全にアクセスできることを示す。

## なぜSSLが重要なのか？

ほとんどのドメインはSSLを必要としないが、Brazeは以下の理由からSSLの使用を強く推奨する。

ウェブサイトやリンクをSSLで保護することは、機密性の高い顧客情報を直接扱わない企業でも一般的に行われている。SSLで保護されたリンクはユーザーからの信頼度が高く、認証のレイヤーが増えることでデータの保護に役立つ。

### クリックと開封の追跡に必要

Brazeは、クリックと開封をトラッキングするために、あなたのブランド化されたリンクトラッキングサブドメインを使用してリンクを変換する。デフォルトでは、これらのリンクはHTTPで始まる。非セキュアな通信を制限するブラウザや拡張機能を使用しているユーザーは、たとえURLがセキュアであっても、送信先URLへのリダイレクトを通過できない可能性がある。これにより画像が破損したり、トラッキングが不正確になったりする。トラッキングサブドメインにSSLを適用し、安全なリダイレクトを確認する。

### ブラウザの要件

Google Chromeなどの主要ブラウザは、ユーザーを保護するため、非セキュアなURL経由の通信を制限している。SSLを使用することで、コンテンツが信頼できるものであることを確認でき、メール内のリンク切れや画像, 写真の表示不良といった問題を最小限に抑えられる。

### HSTSドメイン要件 

HTTP Strict Transport Security（HSTS）ドメインを持っているなら、SSLを設定し、必要なセキュリティ証明書を送信するようにCDNを構成せよ。SSLがないと、画像やWebリンクが壊れる。

## SSL証明書を取得する

SSL証明書を第三者、通常はコンテンツ配信ネットワーク（CDN）を通じて取得する。CDNは証明書をホストし、ユーザーがリンクをクリックすると、トラフィックをCDN経由でリダイレクトして証明書を適用した後、SendGridやSparkPostに送信する際にブラウザに証明書を提供する。

SSL設定を開始するには、Brazeの顧客サクセスマネージャーに連絡し、Brazeメール設定の完全な開始を依頼する。

Brazeが設定を開始したら、次のステップに従う：
1. Brazeは、ドメインレジストリに追加するDNSレコードを提供する。
2. Brazeは、レコードがレジストリに正しく追加されているかどうかを確認する。
3. この後、CDNを選択し、サードパーティーのプロバイダーからSSL証明書を取得する。 
4. この時点で、CDNを設定する。Braze は、CDN 設定のトラブルシューティングに役立ちません。追加のサポートが必要な場合は、CDNプロバイダーに連絡する。
5. SSLを有効にするには、顧客サクセスマネージャーに連絡するんだ。

### CDNとは何か、なぜ必要なのか？

コンテンツ配信ネットワーク（CDN）とは、複数の媒体にわたってコンテンツを迅速に読み込むと同時に、セキュリティ証明書も処理するサーバー群のプラットフォームである。 

{% alert important %}
CDNの設定は、常にBrazeによってDNSレコードが検証された後に行われる。このステップをまだ開始していない場合は、顧客サクセスマネージャーに連絡し、開始方法の詳細を確認すること。
{% endalert %}

クリックと開封のトラッキング, 追跡では、配送パートナーがリンクをブランド化されたサブドメインで変換し、CDNはその変換されたリンクにSSL証明書を適用する。パートナーは、リンクや画像, 写真が正しく表示されるように、受信者のブラウザに有効な証明書を提示しなければならないことが多い。Brazeは証明書を要求したり管理したりしないため、CDNを通じて設定する必要がある。 

{% alert note %}
リストされたCDNでSSLクリックと開封トラッキングが使えない、あるいは使いたくない場合、カスタムSSL設定を構築できる。代替CDNやカスタムプロキシは、より複雑な設定を招く可能性がある。[SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/)と[SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/)のドキュメントを参照せよ。
{% endalert %}

#### その他のリソース

{% alert important %}
CDN設定のトラブルシューティングについては、CDNプロバイダーに連絡せよ。
{% endalert %}

以下の表に、ESP パートナーが作成した特定の CDN の設定方法に関するステップバイステップガイドを示します。特定のCDNがリストにない場合もあるが、CDNにSSL証明書を適用する機能があることを確認する必要がある。

| SendGrid | SparkPost |
| -------- | --------- |
| [AWS Cloudfront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront)<br>[CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare)<br>[Fastly](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly)<br>[KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) | [AWS Cloudfront](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-aws-cloudfront)<br>[CloudFlare](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare)<br>[Fastly](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly)<br>[Google Cloud Platform](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-google-cloud-platform)<br>[Microsoft Azure](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-microsoft-azure) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Amazon SES については、[オプション 2:HTTPSドメイン](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html)を設定し、Brazeクラスターに基づいてリージョンごとにAWSトラッキングドメインを指定する：

- **Braze US クラスター:** `r.us-east-1.awstrack.me`
- **Braze EU クラスター:** `r.eu-central-1.awstrack.me`

{% alert important %}
CDNのクリックトラッキングドメインを設定する際は、ホストヘッダー攻撃などの潜在的なセキュリティ問題を防止するため、\`X-Click-Tracking\`ヘッダー`X-Forwarded-Host`をイネーブルメントせよ。ステップについては、CDNのドキュメントまたはサポートチームを参照せよ。
{% endalert %}

#### トラブルシューティング

CDNの設定や証明書、プロキシの問題はCDN事業者に任せるべきだが、一般的なSSLクリックトラッキングの問題を識別するには以下のヒントを活用するといい。

##### ドメイン・レジストリの問題

digコマンドを実行して、ポイントリンクのトラッキングがCDNを指していることを確認する。ターミナルで実行しろ`dig CNAME link_tracking_subdomain`。CNAMEレコードが指す先がここに表示される`ANSWER SECTION`。メールサービスプロバイダー（SendGridやSparkPost）を指していて、CDNを指していない場合、ドメインレジストリを再設定してCDNを指すようにする。

##### CDNの問題

設定中にメールのライブリンクが機能しなくなった場合、適切な設定を行う前にDNSをCDNに向けてしまった可能性が高い。これは「間違ったリンク」エラーとして表示されることがある。CDNプロバイダーに連絡し、設定のトラブルシューティングのためにそのドキュメントを確認する。

##### SSL有効化ステータス

SSLの設定を完了してもリンクがHTTPとして表示される場合は、Brazeのカスタマーサクセスマネージャーに連絡し、BrazeがSSLをイネーブルメントしていることを確認せよ。Brazeは、すべての設定ステップが完了した後にのみSSLをイネーブルメントする。

