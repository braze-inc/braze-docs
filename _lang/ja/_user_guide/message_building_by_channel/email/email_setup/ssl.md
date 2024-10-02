---
nav_title: ブレイズのSSL
article_title: SSLの概要
page_order: 5
page_type: reference
description: "この参考記事では、SSLについて、その使用目的、Brazeでの使用方法について説明する。"
channel: email

---

# ブレイズのSSL

{% multi_lang_include video.html id="zP1N_wN0SsQ" align="right" %}

> セキュア・ソケット・レイヤー（SSL）は、安全性の低いHTTPではなく、HTTPSでURLを暗号化する。URLのHTTPSは、有効で信頼できるSSLまたはTLS証明書が存在し、ウェブサイトが安全に訪問でき、危険なマルウェアの発信源ではないことを示す。

## なぜSSLが重要なのか？

ほとんどのドメインはSSLを必要としないが、Brazeは以下の主な理由からSSLの使用を強く推奨している。

ウェブサイトやリンクをSSLで保護することは、機密性の高い顧客情報を直接扱わない企業でも一般的に行われている。SSLで保護されたリンクはユーザーからの信頼度が高く、認証のレイヤーが増えることでデータの保護に役立つ。

### クリックと開封のトラッキングに必要

Brazeでは、Eメールを送信する際、まずブランド化されたリンク追跡サブドメインを使用してリンクを変換し、ユーザーのクリックと開封を追跡する。デフォルトでは、これらのリンクはHTTPで始まる。つまり、非セキュアなトラフィックを制限するブラウザや拡張機能を使用しているユーザーは、たとえURLがセキュアであったとしても、リダイレクト先のURLに到達する前にリダイレクトを通過することが困難になる可能性がある。このため、画像が壊れたり、メール全体のクリックや開封のトラッキングが不正確になったりする可能性がある。このため、リンク追跡サブドメインにSSLレイヤーを適用し、Eメールでの安全なリダイレクトを確認するのがベストプラクティスである。 

### ブラウザの要件

グーグル・クロームのような主要なブラウザが、ユーザーを保護するために、安全でないURLからのトラフィックを制限し始めているため、SSLプロトコルは今日、より普及している。ウェブサイトにSSLを導入している企業は、そのコンテンツが信頼できるものであることをこれらの主要なブラウザで確認し、リンク切れや電子メール内の画像といったコンテンツ閲覧の問題を最小限に抑えている。

### HSTSドメイン要件 

HTTPストリクト・トランスポート・セキュリティ（HSTS）ドメインを持っている場合は、ユーザーがどのブラウザからメールにアクセスするかにかかわらず、SSLを設定し、必要なセキュリティ証明書を送信するようにCDNを設定する必要がある。SSLを設定しないと、画像もウェブリンクも壊れてしまう。

## SSL証明書を取得する

サードパーティ、通常はコンテンツ・デリバリー・ネットワーク（CDN）を利用することで、SSL証明書を取得することができる。CDNはSSL証明書をホストし、リンクがクリックされるたびにブラウザに提供することができる。これは、CDNを経由してトラフィックをリダイレクトし、必要な証明書を適用してから、メール・パートナーのSendGridまたはSparkPostに送信することで行われる。

SSLセットアップを開始するには、Brazeカスタマーサクセスマネージャーに連絡し、BrazeのフルEメールセットアップを開始する。

Brazeがこのセットアップを開始したら、以下の手順に従う：
1. Brazeは、ドメインレジストリに追加するDNSレコードを提供する。
2. Brazeは、レコードがレジストリに正しく追加されているかどうかを確認する。
3. この後、CDNを選択し、サードパーティーのプロバイダーからSSL証明書を取得する。 
4. この時点で、CDNを設定する。なお、BrazeではCDN設定のトラブルシューティングはできない。さらなるサポートが必要な場合は、CDNプロバイダーに問い合わせること。
5. SSLを有効にするには、カスタマー・サクセス・マネージャーに連絡しよう。

### CDNとは何か、なぜ必要なのか？

コンテンツ・デリバリー・ネットワーク（CDN）とは、複数のメディアにわたる高品質なコンテンツの迅速なロードタイムを保証すると同時に、セキュリティ証明書を扱うサーバーのプラットフォームである。 

{% alert important %}
CDNの設定は、常にBrazeによってDNSレコードが検証された後に行われる。まだこのステップを開始していない場合は、カスタマー・サクセス・マネージャーに連絡し、開始方法の詳細を確認する。
{% endalert %}

Brazeでは、クリックトラッキングとオープントラッキングを行うために、配信パートナーがブランドのサブドメインを使用してリンクを変換し、CDNが新しく変換されたリンクにSSL証明書を適用する。リンクや画像を正しく表示させるために、メール受信者のブラウザに有効で信頼できる証明書を提示する必要がある。Brazeはこのような証明書を要求したり管理したりしないため、CDNを通じてユーザー側で設定する必要がある。 

{% alert note %}
クリックトラッキングとオープントラッキングにSSLを設定する際に、リストアップされたCDNを使用できない、または使用したくない場合は、カスタムSSL設定を行うことができる。代替CDNやカスタムプロキシは、より複雑で微妙なセットアップになる可能性がある。このトピックについては、[SendGridと](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) [SparkPostの](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/)記事を参照のこと。
{% endalert %}

#### その他のリソース

{% alert important %}
CDNコンフィギュレーションのトラブルシューティングについては、CDNプロバイダーに問い合わせる必要がある。
{% endalert %}

以下の表には、SendGridとSparkPostが書いた、特定のCDNの設定方法に関するステップバイステップのガイドが含まれている。特定のCDNがリストにない場合もあるが、CDNにSSL証明書を適用する機能があることを確認する必要がある。

| SendGrid | SparkPost |
| -------- | --------- |
| [AWSクラウドフロント](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront)<br>[クラウドフレア](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare)<br>[迅速に](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly)<br>[キーシーディーエヌ](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) | [AWSクラウドフロント](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-aws-cloudfront)<br>[クラウドフレア](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare)<br>[クラウドフロント](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/)<br>[迅速に](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly)<br>[グーグル・クラウド・プラットフォーム](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-google-cloud-platform)<br>[マイクロソフト・アジュール](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-microsoft-azure) |

#### トラブルシューティング

CDNのコンフィギュレーション、証明書、プロキシの問題はCDNで対処すべきだが、SSLクリックトラッキングのセットアップでよくある問題を特定するのに役立つ一般的なトラブルシューティングのヒントをいくつか紹介しよう。

##### ドメイン・レジストリの問題

digコマンドは、リンク追跡がCDNに向いているかどうかを教えてくれる。これはターミナルで`dig CNAME link_tracking_subdomain` を実行することで行える。コマンドの実行後、`ANSWER SECTION` 、CNAMEが指す場所がリストされるはずである。CDNではなく、選択したメールサービスプロバイダ（SendGridまたはSparkPost）を指している場合は、CDNを指すようにドメインレジストリを再設定してみてほしい。

##### CDNの問題

ライブEメールのリンクがセットアップ中に壊れ始めた場合、これは一般的に、DNSが適切に設定されていないままCDNに向けられたことを意味する。これは「間違ったリンク」エラーとして表示されることがある。CDNプロバイダーに連絡し、CDN設定のトラブルシューティングに役立つドキュメントを確認する。

##### SSL有効化ステータス

SSLの設定が完了しても、リンクがHTTPSではなくHTTPとして表示される場合は、Brazeカスタマーサクセスマネージャーに連絡し、BrazeでSSLが有効になっていることを確認してください。BrazeでSSLが有効になるのは、SSLの設定がすべて完了した後である。

