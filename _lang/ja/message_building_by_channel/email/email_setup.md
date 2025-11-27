---
nav_title: メール設定
article_title: オンボーディングメールセットアップ
layout: dev_guide
page_order: 1
guide_top_header: "メール設定"
guide_top_text: "Brazeは、メールキャンペーンの送信を開始するのに役立ちます。ガイドに従うか、<a href='https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability' target='_blank'>メールオンボーディング</a>の Braze ラーニングコースを参照してください。"
page_type: landing
description: "このランディングページには、メールキャンペーンの開始に関するリソースが含まれており、IPやドメインの設定、IPウォーミング、メールの検証などが含まれています。"
channel: email

guide_featured_title: "セクションの記事"
guide_featured_list:
- name: "IPとドメインの設定"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/
  image: /assets/img/braze_icons/target-05.svg
- name: "IP ウォームアップ"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/ip_warming/
  image: /assets/img/braze_icons/annotation-alert.svg
- name: "メール検証"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/email_validation/
  image: /assets/img/braze_icons/check-square-broken.svg
- name: "メール認証"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/authentication/
  image: /assets/img/braze_icons/user-square.svg
- name: "メールリストのインポート"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/import_your_email_list/
  image: /assets/img/braze_icons/list.svg
- name: "SSLの概要"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/ssl/
  image: /assets/img/braze_icons/navigation-pointer-01.svg
- name: "同意と住所の収集"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/consent_and_address_collection/
  image: /assets/img/braze_icons/book-closed.svg
- name: "配信の落とし穴とスパムトラップ"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/deliverability_pitfalls_and_spam_traps/
  image: /assets/img/braze_icons/alert-triangle.svg
---

## 要件

メールを送信し始める前に、いくつか必要なものがあります。これらの要件について詳しく知るには、次の図を参照してください。

| 要件 | 説明 | ソース |
|---|---|---|
| 専用IP（インターネットプロトコル）| 専用 IP は、単一のホスティングアカウント用に提供される一意のインターネットアドレスです。 | Brazeは、メール送信者のレピュテーションを確実にコントロールするための専用IPを提供する。これは Braze のオンボーディングによって設定されます。|
| ホワイトラベルドメイン | これらはドメインとサブドメインで構成されています。ホワイトラベルを使用することで、DKIM および SPF のメール認証検査を通過できます。 | これらのドメインは Braze オンボーディングチームによって生成されますが、ドメインの名前は選択する必要があります。 |
| サブドメイン | これは、メールアドレス内のドメイン（「@news.company.com」など）のサブディビジョンです。サブドメインを持つことで、会社の公式メールの評判を損なう可能性のあるエラーを防ぐことができます。 | これはオンボーディングチームによって生成されますが、サブドメインの名前は決定する必要があります。Brazeの外部で現在使用されているサブドメインは使用できません。 |
| IP プール | これらは、1つのメールの評判が他のメールに影響を与えるのを防ぎ、より高い配信率をサポートするために、異なる種類のメール（「プロモーション」や「トランザクション」など）の評判を分けるために使用されるオプションの設定です。 | オンボーディングチームがプールを設定します。その後、メールを作成する際に、**ターゲットオーディエンスの**ステップでメールのIPプールを表示することができる。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## IPウォーミング

{% alert important %}
IP ウォーミングはメール設定のプロセスにおける**最も重要なステップ**です。これは最初のステップではありませんが（実際には最後のステップです）、ここでお知らせするのは、IPアドレスをウォームアップしなければ、送信するメールがスパムに送られたり、他の送信障害に遭遇したりする可能性があるためです。
{% endalert %}

[IPウォーミング]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/)とは、最初のバッチで比較的少数のメールを送信し、その後、次のバッチで徐々に量を増やしていき、通常の1日の量に達するまでのプロセスです。これはメール設定プロセスの一番最後に行われる。

少量のメールから始めることで、メールプロバイダーとの信頼関係を確立し、関連のあるユーザーにのみメールを送信していることを示します。最もエンゲージメントが高いユーザーに最初のメールを送ることで、プロバイダーからの信頼をより早く得ることができる。

IPのウォームアップが完了したら、[メールの作成と送信を開始できます]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/)！

<br><br>
