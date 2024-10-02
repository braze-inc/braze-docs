---
nav_title: ディープリンクのためのブランチ
article_title: ディープリンクのためのブランチ
alias: /partners/branch_for_deeplinking/
page_type: partner
description: "この参考記事では、BrazeとBranchのパートナーシップと、ディープリンクの実践をサポートするための利用方法について説明している。"
search_tag: Partner

---

# ディープリンク用ブランチ {#branch}

{% multi_lang_include video.html id="PwGKqfwV-Ss" align="right" %}

> モバイルリンクプラットフォームである[Branchは][1]、すべてのユーザータッチポイントを総合的に把握することで、あらゆるデバイス、チャネル、プラットフォームでの獲得、エンゲージメント、測定を支援する。

BrazeとBranchの統合により、ユーザージャーニーの開始を適切に[属性化]({{site.baseurl}}/partners/advertising_technologies/attribution/branch_for_attribution/)し、ディープリンクを通じて目的の場所へとつなげることができるため、顧客により良い体験を提供することができる。

通話リンク(`href=tel:`)を含む場合、

## 統合

[BranchのSDK統合ガイドに従って](https://help.branch.io/developers-hub/docs/native-sdks-overview)、Branch統合を立ち上げ、実行する。その他の使用例については以下を参照のこと。

### iOSユニバーサルリンクをサポートする

BrazeからiOSユニバーサルリンクをディープリンクとして送信できるようにする：

1. [ユニバーサルリンクの][3]設定については、Branchのドキュメントに従うこと。
2. アプリ内からユニバーサルリンクをルーティングするために [`BrazeDelegate`][4]メソッド[braze(_:shouldOpenURL:)を][5]実装し、アプリ内から[ユニバーサルリンクをルーティング][6]する。

### 電子メールでのディープリンク

[ユニバーサルリンクとアプリリンクに関する]({{site.baseurl}}/help/help_articles/email/universal_links/)ドキュメントを参照する。
または、[Brazeを通して](https://docs.branch.io/pages/integrations/braze/)送信されたメールからのディープリンクを設定するための[Branchのドキュメントを](https://docs.branch.io/pages/integrations/braze/)参照のこと。

iOS用Gmailアプリでは、ユーザーがアプリに通話許可を与えない限り、電話番号へのリンク（`href` に`tel` を付加）はサポートされていない。

ESPによっては、クリックトラッキングされたユニバーサルリンクをサポートするために追加のカスタマイズが必要になる場合がある。この情報については、専用の記事で紹介している。詳しくは以下の文献を参照されたい：

- [SendGrid][7]
- [SparkPost][9]

[1]: https://branch.io/
[2]: {{site.baseurl}}/partners/branch_for_attribution/
[3]: https://docs.branch.io/pages/deep-linking/universal-links/#search
[4]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate
[5]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:shouldopenurl:)-6xxc5
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/#linking-handling-customization
[7]: https://help.branch.io/using-branch/page/braze-sendgrid
[9]: https://help.branch.io/using-branch/page/braze-sparkpost
