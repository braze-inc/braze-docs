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

> セキュア・ソケット・レイヤー（SSL）は、安全性の低いHTTPではなく、HTTPSでURLを暗号化する。URLのHTTPSは、有効で信頼できるSSLまたはTLS証明書が存在し、ウェブサイトが安全に訪問でき、危険なマルウェアの発信源ではないことを示す。

## なぜSSLが重要なのか？

ほとんどのドメインはSSLを必要としないが、Brazeは以下の主な理由からSSLの使用を強く推奨している。

ウェブサイトやリンクをSSLで保護することは、機密性の高い顧客情報を直接扱わない企業でも一般的に行われている。SSLで保護されたリンクはユーザーからの信頼度が高く、認証のレイヤーが増えることでデータの保護に役立つ。

### クリックと開封の追跡に必要

Brazeでは、Eメールを送信する際、まずブランド化されたリンク追跡サブドメインを使用してリンクを変換し、ユーザーのクリックと開封を追跡する。デフォルトでは、これらのリンクはHTTPで始まる。つまり、非セキュアなトラフィックを制限するブラウザや拡張機能を使用しているユーザーは、たとえURLがセキュアであったとしても、リダイレクト先のURLに到達する前にリダイレクトを通過することが困難になる可能性がある。このため、画像が壊れたり、メール全体のクリックや開封のトラッキングが不正確になったりする可能性がある。このため、リンク追跡サブドメインにSSLレイヤーを適用し、Eメールでの安全なリダイレクトを確認するのがベストプラクティスである。 

### ブラウザの要件

グーグル・クロームのような主要なブラウザが、ユーザーを保護するために、安全でないURLからのトラフィックを制限し始めているため、SSLプロトコルは今日、より普及している。ウェブサイトにSSLを導入している企業は、そのコンテンツが信頼できるものであることをこれらの主要なブラウザで確認し、リンク切れや電子メール内の画像といったコンテンツ閲覧の問題を最小限に抑えている。

### HSTSドメイン要件 

HTTPストリクト・トランスポート・セキュリティ（HSTS）ドメインを持っている場合は、ユーザーがどのブラウザからメールにアクセスするかにかかわらず、SSLを設定し、必要なセキュリティ証明書を送信するようにCDNを設定する必要がある。SSLを設定しないと、画像もウェブリンクも壊れてしまう。

## SSL証明書を取得する

サードパーティ、通常はコンテンツ配信ネットワーク (CDN) を利用することで、SSL 証明書を取得することができます。CDNはSSL証明書をホストし、リンクがクリックされるたびにブラウザに提供することができる。これは、CDNを経由してトラフィックをリダイレクトし、必要な証明書を適用してから、メール・パートナーのSendGridまたはSparkPostに送信することで行われる。

SSLセットアップを開始するには、Brazeカスタマーサクセスマネージャーに連絡し、BrazeのフルEメールセットアップを開始する。

Brazeがこのセットアップを開始したら、以下の手順に従う：
1. Brazeは、ドメインレジストリに追加するDNSレコードを提供する。
2. Brazeは、レコードがレジストリに正しく追加されているかどうかを確認する。
3. この後、CDNを選択し、サードパーティーのプロバイダーからSSL証明書を取得する。 
4. この時点で、CDNを設定する。Braze は、CDN 設定のトラブルシューティングに役立ちません。さらなるサポートが必要な場合は、CDNプロバイダーに問い合わせること。
5. SSL を有効にするには、カスタマーサクセスマネージャーに連絡してください。

### CDNとは何か、なぜ必要なのか？

コンテンツ配信ネットワーク (CDN) とは、セキュリティ証明書を処理しながら、複数のメディアにわたる高品質なコンテンツの迅速な読み込みを保証するのに役立つサーバーのプラットフォームです。 

{% alert important %}
CDNの設定は、常にBrazeによってDNSレコードが検証された後に行われる。このステップをまだ開始していない場合は、カスタマーサクセスマネージャーに問い合わせて開始方法の詳細を確認してください。
{% endalert %}

Brazeでは、クリックトラッキングとオープントラッキングを行うために、配信パートナーがブランドのサブドメインを使用してリンクを変換し、CDNが新しく変換されたリンクにSSL証明書を適用する。多くの場合、当社の配信パートナーは、リンクや画像を正しく表示できるように、有効で信頼できる証明書をメール受信者のブラウザに提示する必要があります。Braze はこのような証明書の要求や管理を行わないため、これは CDN を通じてユーザー側で設定する必要があります。 

{% alert note %}
クリックトラッキングとオープントラッキングにSSLを設定する際に、リストアップされたCDNを使用できない、または使用したくない場合は、カスタムSSL設定を行うことができる。代替 CDN やカスタムプロキシは、より複雑で細かい設定になる可能性があることに注意してください。このトピックについては、[SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) および [SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/) の記事を参照してください。
{% endalert %}

#### その他のリソース

{% alert important %}
CDN の構成のトラブルシューティングについては、CDN プロバイダーに問い合わせる必要があります。
{% endalert %}

以下の表に、ESP パートナーが作成した特定の CDN の設定方法に関するステップバイステップガイドを示します。特定のCDNがリストにない場合もあるが、CDNにSSL証明書を適用する機能があることを確認する必要がある。

| SendGrid | SparkPost |
| -------- | --------- |
| [AWS Cloudfront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront)<br>[CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare)<br>[Fastly](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly)<br>[KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) | [AWS Cloudfront](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-aws-cloudfront)<br>[CloudFlare](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare)<br>[Fastly](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly)<br>[Google Cloud Platform](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-google-cloud-platform)<br>[Microsoft Azure](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-microsoft-azure) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Amazon SES については、[オプション 2:HTTPS ドメインの設定](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html)を参照し、Braze クラスターに基づいてリージョン別の AWS 追跡ドメインを指定します。

- **Braze US クラスター:** `r.us-east-1.awstrack.me`
- **Braze EU クラスター:** `r.eu-central-1.awstrack.me`

{% alert important %}
CDN クリック追跡ドメインを設定するときに、`X-Forwarded-Host` ヘッダーを有効にしておいてください。これは、ホストヘッダー攻撃などの潜在的なセキュリティの問題を防ぐ目的で使用されます。手順は CDN によって異なるので、CDN のドキュメントを参照するか、サポートチームに連絡してください。
{% endalert %}

#### トラブルシューティング

CDN の構成、証明書、プロキシの問題は CDN で処理する必要がありますが、SSL のクリック追跡の設定でよくある問題を特定するのに役立つ一般的なトラブルシューティングのヒントをいくつか紹介します。

##### ドメイン・レジストリの問題

digコマンドは、リンク追跡がCDNに向いているかどうかを教えてくれる。これはターミナルで `dig CNAME link_tracking_subdomain` を実行することで行えます。コマンドの実行後、`ANSWER SECTION` の下に、CNAME がどこを指しているかが表示されます。CDN ではなく、選択したメールサービスプロバイダー (SendGrid または SparkPost) を指している場合は、CDN を指すようにドメインレジストリを再設定してみます。

##### CDNの問題

ライブEメールのリンクがセットアップ中に壊れ始めた場合、これは一般的に、DNSが適切に設定されていないままCDNに向けられたことを意味する。これは「間違ったリンク」エラーとして表示されることがある。CDN プロバイダーに連絡し、CDN 構成のトラブルシューティングに役立つドキュメントを確認してください。

##### SSL有効化ステータス

SSLの設定が完了しても、リンクがHTTPSではなくHTTPとして表示される場合は、Brazeカスタマーサクセスマネージャーに連絡し、BrazeでSSLが有効になっていることを確認してください。BrazeでSSLが有効になるのは、SSLの設定がすべて完了した後である。

