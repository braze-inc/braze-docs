---
nav_title: ろう付け時のSSL
article_title: SSL の概要
page_order: 5
page_type: reference
description: "この参照記事では、SSL、それが何のために使用されているか、およびブレーズでどのように使用されているかについて説明します。"
channel: email

---

# ろう付け時のSSL

{% multi_lang_include video.html id="zP1N_wN0SsQ" align="right" %}

> セキュアソケットレイヤー(SSL) は、安全性の低いHTTP ではなく、HTTPS を使用してURL を暗号化します。URL の HTTPS は、有効で信頼できる SSL または TLS 証明書が存在し、ウェブサイトにアクセスしても安全であり、危険なマルウェアの原因ではないことを示します。

## なぜSSLが重要なのか?

ほとんどのドメインはSSL を必要としませんが、Braze はこれらの主要な理由からSSL の使用を強く推奨します。

SSLでウェブサイトやリンクを保護することは、機密性の高い顧客情報を直接扱っていない企業にとっても、一般的な慣行です。ユーザーはSSLで保護されたリンクをより信頼しており、認証の追加レイヤーはデータの保護に役立ちます。

### クリックアンドオープントラッキングに必要

Brazeでは、私たちがメールを送信する際に、まずあなたのブランド化されたリンクトラッキングサブドメインを使用してあなたのリンクを変換し、ユーザーのクリックとオープンを追跡します。デフォルトでは、これらのリンクはHTTP で始まります。つまり、非セキュアトラフィックを制限するブラウザまたは拡張機能を持つユーザは、URL がセキュアであっても、宛先URL にランディングする前にリダイレクトを通過できないことがあります。これにより、画像が壊れたり、メール全体のクリックやオープントラッキングが不正確になる可能性があります。このため、SSLレイヤーをリンクトラッキングサブドメインに適用して、メールのセキュアなリダイレクトを確認することがベストプラクティスです。 

### ブラウザ要件

今日、Google Chromeのような主要なブラウザが、ユーザを保護するために非セキュアなURLを介してトラフィックを制限し始めているため、SSLプロトコルが普及しつつあります。自社のウェブサイトにSSLを掲載している企業は、これらの主要なブラウザで、自社のコンテンツが信頼されていることを確認し、メール内のリンクや画像の破損などのコンテンツ閲覧の問題を最小限に抑えます。

### HSTSドメイン要件 

HTTP Strict Transport Security (HSTS) ドメインがあり、必要なセキュリティ証明書を送信するようにCDN を設定している場合は、ユーザがどのブラウザからメールにアクセスしているかに関係なく、SSL を設定する必要があります。SSLの設定に失敗すると、イメージとWebリンクの両方が破損します。

## SSL 証明書の取得

SSL 証明書は、サードパーティ(通常はコンテンツ配信ネットワーク(CDN))を使用して取得できます。CDN はSSL 証明書をホストし、リンクの1 つをクリックするといつでもブラウザに提供できます。これは、必要な証明書を適用するために、CDN を介してトラフィックをリダイレクトしてから、電子メールパートナーのSendGrid またはSparkPost に送信することによって行われます。

SSL 設定を開始するには、Braze カスタマーサクセスマネージャーに連絡して、完全なBraze E メール設定を開始します。

Braze がこのセットアップを開始した後、次の手順に従います。
1\.Braze はドメインレジストリに追加するDNS レコードを提供します。
2\.Braze は、レコードがレジストリに正しく追加されているかどうかを確認します。
3\.この後、CDN を選択し、サードパーティプロバイダからSSL 証明書を取得します。
4\.この時点で、CDN を設定します。Braze は、CDN 設定のトラブルシューティングに役立ちません。その他のサポートについては、CDN プロバイダにお問い合わせください。
5\.SSL を有効にするには、カスタマーサクセスマネージャーに連絡します。

### CDNとは何か、なぜ必要なのか。

コンテンツ配信ネットワーク(CDN)は、セキュリティ証明書を処理しながら、複数のメディアにわたって高品質のコンテンツをすばやくロードできるようにするサーバーのプラットフォームです。 

{% alert important %}
CDN 設定は、必ず、Braze によって検証されたDNS レコードを取得した後に行います。このステップをまだ開始していない場合は、カスタマーサクセスマネージャーに連絡して、開始方法の詳細を確認してください。
{% endalert %}

Brazeでは、クリックしてトラッキングを開くために、私たちの配送パートナーはブランド化されたサブドメインを使用してリンクを変換し、CDNは新しく変換されたリンクにSSL証明書を適用します。多くの場合、当社の配信パートナーは、リンクや画像が正しく表示されるように、有効で信頼できる証明書をメール受信者のブラウザに提示する必要があります。Brazeは、このような証明書を要求または管理しないため、CDNを介して、最終的に設定する必要があります。 

{% alert note %}
クリックしてトラッキングを開くためにSSLを設定するときに、リストされたCDNを使用できない、または使用したくない場合は、カスタムSSL設定を設定できます。代替CDNまたはカスタムプロキシは、より複雑で微妙な設定になる可能性があることに注意してください。このトピックについては、[SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/)および[SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/)の記事を参照してください。
{% endalert %}

#### 追加リソース

{% alert important %}
CDN 設定のトラブルシューティングの詳細については、CDN プロバイダに問い合わせる必要があります。
{% endalert %}

次の表には、SendGrid およびSparkPost が特定のCDN の設定方法について説明した、段階的なガイドが含まれています。特定のCDN がリストされていない場合もありますが、CDN にSSL 証明書を適用する機能があることを確認する必要があります。

| SendGrid | SparkPost |
| -------- | --------- |
| [AWS Cloudfront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront)<br>[CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare)<br>[すばやく](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly)<br>[KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) | [AWS Cloudfront](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-aws-cloudfront)<br>[CloudFlare](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare)<br>[Cloudfront](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/)<br>[すばやく](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly)<br>[Google Cloud プラットフォーム](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-google-cloud-platform)<br>[Microsoft Azure](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-microsoft-azure) |

#### トラブルシューティング

CDN の設定、証明書、およびプロキシの問題は、CDN で処理する必要がありますが、SSL クリックトラッキング設定で一般的な問題を特定するための一般的なトラブルシューティングのヒントを次に示します。

##### ドメインレジストリの問題

dig コマンドを使用すると、リンクトラッキングをCDN で指しているかどうかを確認できます。これは、`dig CNAME link_tracking_subdomain` を実行することで、ターミナルで実行できます。コマンドが実行された後、`ANSWER SECTION` の下で、CNAME がどこを指しているかをリストします。CDN ではなく、選択したメールサービスプロバイダ(SendGrid またはSparkPost) を指し示している場合は、CDN を指し示すようにドメインレジストリを再設定してみてください。

##### CDN問題

設定中にライブメールリンクが途切れ始めた場合は、通常、DNS が正しく設定されていない状態でCDN に向かっていることを意味します。これは"wrong link" error として表示されることがあります。CDN プロバイダに連絡し、CDN 設定のトラブルシューティングに役立つドキュメントを確認します。

##### SSL使用可能状態

SSL 設定が完了しても、リンクがHTTPS ではなくHTTP として表示される場合は、Braze カスタマーサクセスマネージャーに連絡して、SSL がBraze によって有効になっていることを確認します。SSL は、SSL 設定のすべての機能が完了した後でのみ、Braze で有効にできます。

