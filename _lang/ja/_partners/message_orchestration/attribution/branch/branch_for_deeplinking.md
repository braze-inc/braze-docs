---
nav_title: Branch (ディープリンク)
article_title: Branch (ディープリンク)
alias: /partners/branch_for_deeplinking/
page_type: partner
description: "このリファレンス記事では、Braze と Branch のパートナーシップと、これを利用してディープリンクをサポートする方法について説明します。"
search_tag: Partner

---

# Branch (ディープリンク) {#branch}

{% multi_lang_include video.html id="PwGKqfwV-Ss" align="right" %}

> [Branch][1] はあらゆるデバイス、チャネル、プラットフォームでの獲得、エンゲージメント、測定を支援するモバイルリンクプラットフォームで、すべてのユーザータッチポイントの一元的なビューを提供しています。

_この統合は Branch によって管理されます。_

## 統合について

Braze とBranch の統合により、ユーザージャーニー開始を適切に[紐づける]({{site.baseurl}}/partners/message_orchestration/attribution/branch/branch_for_attribution/)ことができるようにして、より優れたエクスペリエンスを顧客に提供し、ディープリンクを使用して目的のロケーションに顧客を接続できます。

## 統合

[Branch の SDK 統合ガイド](https://help.branch.io/developers-hub/docs/native-sdks-overview)に従って、Branch と Braze の統合を稼働させます。その他の使用例については以下を参照のこと。

### iOSユニバーサルリンクをサポートする

BrazeからiOSユニバーサルリンクをディープリンクとして送信できるようにする：

1. [ユニバーサルリンク][3]の設定については、Branch のドキュメントの説明に従ってください。
2. アプリ内から[ユニバーサルリンクをルーティング][6]するには、Braze SDK 統合に [`BrazeDelegate`][4] メソッド [braze(_:shouldOpenURL:)][5] を実装します。

### 電子メールでのディープリンク

[ユニバーサルリンクとアプリリンク]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/)に関するドキュメントを参照するか、
[Branch のドキュメント](https://help.branch.io/developers-hub/docs/ios-universal-links#apps-that-always-work)を参照して、Braze 経由で送信されるメールからのディープリンクを設定します。

ユーザーがアプリにコール権限を付与しない限り、iOS 用の Gmail アプリでは電話番号へのリンク (`tel` を`href` に付加) はサポートされません。

ESPによっては、クリックトラッキングされたユニバーサルリンクをサポートするために追加のカスタマイズが必要になる場合がある。この情報については、専用の記事で紹介している。詳しくは以下の文献を参照されたい：

- [SendGrid][7]
- [SparkPost][9]


[1]: https://branch.io/
[2]: {{site.baseurl}}/partners/branch_for_attribution/
[3]: https://help.branch.io/developers-hub/docs/ios-universal-links
[4]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate
[5]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:shouldopenurl:)-6xxc5
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/#linking-handling-customization
[7]: https://help.branch.io/using-branch/page/braze-sendgrid
[9]: https://help.branch.io/using-branch/page/braze-sparkpost
