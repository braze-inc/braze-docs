---
nav_title: Apple Mail のプライバシー保護
article_title: iOS 15のAppleメールプライバシー保護
page_order: 1
description: "この記事では、Apple Mail のプライバシー保護の更新内容について説明します。この更新によって影響を受けるのは誰か、また、この機能を準備するための次の手順についても説明します。"
channel:
  - email

---

# Appleのメールプライバシー保護

## Apple のメールプライバシー保護の更新とは何ですか?

AppleのMailプライバシー保護（MPP）は、2021年9月中旬にリリースされたiOS 15、iPadOS 15、MacOS Monterey、およびwatchOS 8のApple Mailアプリのユーザー向けに利用可能なプライバシー更新です。MPP にオプトインするユーザー (ほとんどのユーザーがそうすると予測されます) の場合、メールはプロキシサーバーを使用してプリロードされ、画像がキャッシュされ、[開封トラッキング]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#changing-location-of-tracking-pixel)などの指標のためのトラッキングピクセルを利用できなくなります。 

ブランドとしては、MPP によって、メール配信可能性指標に関する問題や、これらの指標に基づいてトリガーされる既存のキャンペーンやキャンバスに関する問題が発生することが予想されます。メール配信可能性への影響を理解するには、[メールレポート]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/)を参照してください。

### 誰に影響を与えるか

ネイティブのApple Mailアプリを使用しているすべての受信者に: 

- iOS 15
- iPadOS 15
- MacOS Monterey
- watchOS 8

これは、メールアカウントをApple Mailアプリに接続し、セキュリティ機能にオプトインしたすべてのユーザーに適用されます。メールサービス（Gmail、Outlook、Yahoo、AOLなど）に関係なく適用されます。この影響は、Apple/iCloud/me.com メールアドレスでメールを受信するサブスクライバーにはトレーニングされません。

{% alert important %}
メール配信のこれらの更新は重要ですが、MPP はメールと配信を管理するルールを根本的に変えるものではありません。代わりに、MPP は成功のベンチマーク方法や、今後使用できるメールツールと機能に影響を与えます。
{% endalert %} 

## MPPの準備方法は？

ブランドがMPPへの対応方法とそのメールマーケティングおよび全体的なカスタマーエンゲージメントへの潜在的な影響について考え始めるためには、時間が本質的なものです。次のことを行うことをお勧めします:

- MPP がブランドのマーケティング活動に与えるリスクを評価する
- Braze プラットフォームのオートメーション調整に対応し、配信可能性のベストプラクティスを強化し、パフォーマンスを測定するための広範囲な指標を開発するために、ターゲットを絞った MPP 措置計画をまとめます。
- できるだけ早くその対応計画を実行してください

Appleのメールプライバシー保護の準備方法についての詳細な概要は、私たちの[ブログ投稿](https://www.braze.com/resources/articles/apple-mail-privacy-protection-how-to-prepare)をご覧ください。 
