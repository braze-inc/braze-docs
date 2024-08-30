---
nav_title: バウチャリファイ
article_title: バウチャリファイ
page_order: 1
alias: /partners/voucherify/voucherify/
description: "この参考記事では、BrazeとVoucherifyの提携について概説している。Voucherifyは、パーソナライズされたクーポン、ギフトカード、ロイヤルティカード、紹介コードなどを、ユーザーがBrazeのアカウントを通じて自動的に送信できるオールインワンのプロモーションプラットフォームで、あらゆるステップで利用状況やキャンペーンの成長を追跡できる。"
page_type: partner
search_tag: Partner

---

# バウチャリファイ

> [Voucherifyは](https://www.voucherify.io/)、パーソナライズされたキャンペーンとロイヤリティ・プログラムを可能にするオールインワンのプロモーション・プラットフォームで、ユーザーのエンゲージメントとリテンションを促進する。 

<iframe src="https://player.vimeo.com/video/745340934?h=17ceae8c3c" width="640" height="360" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>

BrazeとVoucherifyの統合により、ユニークなコードを送信することで、プロモーションキャンペーンを拡大することができる：

- [コネクテッド・コンテンツ]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/voucherify/voucherify_fetching_data_through_braze_connected_content)Braze Connected Contentを通じてBrazeキャンペーンにユニークなコードを追加する。この機能を使えば、Voucherifyの割引クーポン、ギフトカードキャンペーン、ポイントカード、紹介コードを使うことができる。
- [カスタム属性]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/voucherify/voucherify_distribution_with_braze_custom_attributes)：カスタム属性により、Voucherify独自のクーポン、ギフトカード、ロイヤルティカード、紹介コードをBrazeのユーザープロファイルに割り当てることができる。その結果、メールキャンペーンで添付コードや属性を送信し、ユーザーと共有することができる。
- [プロモーションコード一覧]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/voucherify/voucherify_using_braze_promotion_codes_list)：Voucherifyが生成したプロモーションコードを使い、Brazeにアップロードする。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
|Voucherifyアカウント | このパートナーシップを利用するには、Voucherifyのアカウントが必要である。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

Voucherifyの統合に関する追加リソースについては、以下の記事を参照されたい：
- [Braze Connected Contentでデータを取得する]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/voucherify/voucherify_fetching_data_through_braze_connected_content)
- [Brazeのカスタム属性を使ったディストリビューション]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/voucherify/voucherify_distribution_with_braze_custom_attributes)
- [Brazeのプロモーションコードを使用する]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/voucherify/voucherify_using_braze_promotion_codes_list)