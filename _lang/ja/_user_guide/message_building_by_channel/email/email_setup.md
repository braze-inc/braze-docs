---
nav_title: Eメール設定
article_title: オンボーディングメールの設定
layout: dev_guide
page_order: 1
guide_top_header: "Eメール設定"
guide_top_text: "BrazeはEメールキャンペーンを開始するお手伝いをいたします。ガイドに従うか、<a href='https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability' target='_blank'>Email Onboarding</a> Braze Learningコースをチェックしてください。"
page_type: landing
description: "このランディングページには、IPやドメインの設定、IPウォーミングアップ、メール検証など、メールキャンペーンを始めるためのリソースが含まれています。"
channel: email

guide_featured_title: "セクション記事"
guide_featured_list:
- name: "Setting Up IPs and Domains"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/
  fa_icon: far fa-dot-circle
- name: "IP Warming"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/ip_warming/
  fa_icon: fas fa-exclamation
- name: "Email Validation"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/email_validation/
  fa_icon: fas fa-check-square
- name: "Email Authentication"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/authentication/
  fa_icon: fas fa-user-shield
- name: "Importing Your Email List"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/import_your_email_list/
  fa_icon: fas fa-list
- name: "SSL Overview"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/ssl/
  fa_icon: fas fa-mouse-pointer
- name: "Consent and Address Collection"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/consent_and_address_collection/
  fa_icon: fas fa-address-book
- name: "Deliverability Pitfalls and Spam Traps"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/deliverability_pitfalls_and_spam_traps/
  fa_icon: fas fa-exclamation-triangle
---

## 要件

Eメールの送信を始める前に、必要なものがいくつかあります。これらの要件の詳細については、以下の表を参照のこと。

| 要件｜説明｜ソース
|---|---|---|
| 専用IP（インターネットプロトコル）｜専用IPとは、1つのホスティングアカウントだけに提供されるユニークなインターネットアドレスです。| Brazeでは、お客様に専用IPを提供することで、メール送信者のレピュテーションを確実に管理することができます。Brazeのオンボーディングで設定します。
| ホワイトラベル・ドメイン｜ドメインとサブドメインからなる。ホワイトラベルを使用することで、DKIMとSPFのメール認証チェックをパスすることができます。| Brazeオンボーディングチームがこれらのドメインを生成しますが、ドメイン名はお客様が選択する必要があります。|
| サブドメイン｜メールアドレスの中にあるドメイン（「@news.company.com」など）を細分化したもの。サブドメインを持つことで、貴社の公式Eメールの評判を落とすようなエラーを防ぐことができます。| サブドメインはオンボーディングチームが作成いたしますが、サブドメイン名はご自身でお決めください。現在Braze以外で使用されているサブドメインは使用できません。|
| IPプールとは、異なるタイプのメール（例えば「プロモーション」と「トランザクション」）のレピュテーションを分離し、一方のレピュテーションが他方のレピュテーションに影響するのを防ぎ、より高い配信性をサポートするためのオプション設定です。| プールの設定はオンボーディングチームが行います。次に、メールを作成する際に、**Target Users**ページの**IP Pool**ドロップダウンからメールのIPプールを選択します。
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## IP ウォームアップ

{% alert important %}
IPウォーミングは、Eメール設定プロセスで**最も重要なステップ**です。これは最初のステップではありませんが（実際には最後のステップです）、IPアドレスをウォームアップしておく必要があります。
{% endalert %}

[IPウォーミングとは]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/)、最初のバッチで比較的少ない数のメールを送信し、その後時間をかけて、1日の典型的なボリュームに達するまで、次のバッチのボリュームを少しずつ増やしていくことです。これはメール設定プロセスの一番最後に行います。

少量のメールから始めることで、メールプロバイダーとの信頼関係を確立し、関連性の高いユーザーにのみメールを送信していることを示すことができます。最初のEメールを最もエンゲージメントの高いユーザーに送ることで、プロバイダーからの信頼をより早く得ることができます。

IPのウォームアップが終わったら、[メールの作成と送信を始めましょう]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/)！

<br><br>