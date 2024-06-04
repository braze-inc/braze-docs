---
nav_title: アップルメールプライバシー保護
article_title: iOS用Apple Mail Privacy Protection 15
page_order: 1
description: "このリファレンス記事では、Apple Mail Privacy Protectionのプライバシー更新について説明します。この更新によって影響を受けることになります。また、この機能を準備するためのいくつかの次の手順についても説明します。"
channel:
  - email

---

# アップルのメールプライバシー保護

## AppleのMail Privacy Protectionのアップデートは?

AppleのMail Privacy Protection(MPP)は、2021年9月中旬にリリースされたiOS 15、iPadOS 15、macOS Monterey、およびwatchOS 8のApple Mailアプリのユーザーが利用できるプライバシーアップデートです。MPP を選択したユーザ(ほとんどのユーザが行うと予測されます) の場合、メールはプロキシサーバを使用してプリロードされ、イメージがキャッシュされ、[open tracking]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#changing-location-of-tracking-pixel) のようなメトリクスのトラッキングピクセルを活用する機能が妨げられます。 

ブランドは、MPPが電子メール配信可能性メトリクスに関する問題や、これらのメトリクスに基づいてトリガーされる既存のキャンペーンやキャンバスに関する問題をもたらすことを期待すべきです。電子メール配信の影響を理解するには、[電子メールレポート]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/)を参照してください。

### これは誰に影響を与えるか?

ネイティブのApple Mail アプリを使用しているすべての受信者:

- iOS 15
- iPadOS 15
- macOSモントレー
- ウォッチOS 8

これは、メールサービス(Gmail、Outlook、Yahoo、AOLなど)に関係なく、メールアカウントをApple Mailアプリに接続し、セキュリティ機能を選択したすべてのユーザーに適用されます。この影響は、Appleでメールを受信する契約者には制約されません/iCloud/me.com email addresses.

{% alert important %}
電子メール配信可能性に対するこれらの更新は重要ですが、MPPは、電子メールと配信可能性を管理するルールを根本的に変更しません。その代わりに、ベンチマークの成功の仕方や、今後どのようなメールツールや機能を利用できるかに影響します。
{% endalert %} 

## MPP の準備方法

MPPへの対応や、メールマーケティングや顧客エンゲージメント全体への潜在的な影響について考え始めたばかりのブランドにとって、時間は本質的なものである。ユーザーは、次のことを実行することをお勧めします。

- MPPがマーケティング活動にもたらすリスクを評価する
- Brazeプラットフォームの自動化調整に対応し、配信可能性のベストプラクティスを強化し、パフォーマンスを測定するための広範囲なメトリクスを開発する、ターゲットを絞ったMPP応答計画をまとめます。
- できるだけ早く対応計画を実行する

AppleのMail Privacy Protectionの準備方法について詳しくは、[ブログ投稿](https://www.braze.com/resources/articles/apple-mail-privacy-protection-how-to-prepare)をご覧ください。 
