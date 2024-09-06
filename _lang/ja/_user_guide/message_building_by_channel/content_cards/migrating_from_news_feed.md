---
nav_title: ニュースフィードからの移行
article_title: ニュースフィードからの移行
page_order: 10
description: "この参考記事では、ニュースフィードからBraze Content Cardsへの移行に関するガイダンスを提供する。"
channel:
  - content cards
  - news feed
  
---

# ニュースフィードからコンテンツカードへの移行

{% alert note %}
ニュースフィードは非推奨になります。Braze は、ニュースフィードツールを使っている顧客には、コンテンツカードのメッセージングチャネルに移行することを勧めています。
{% endalert %}

> ニュースフィードからコンテンツカードへの移行には時間がかかるが、採用は簡単だ！ニュースフィードからコンテンツカードにコンテンツを自動的に移行することはできない。しかし、コンテンツ・カードの新たな柔軟性により、それを見逃すことも気にすることもないだろう。

詳細については、Brazeのアカウント・マネージャーに問い合わせを。

## 特徴と機能性

コンテンツカードは、アクションベースやAPI配信などの追加配信オプションや、コンバージョントラッキングなどの強化されたアナリティクスなど、ニュースフィードではサポートされていない多くの機能を提供する。

ニュースフィードからコンテンツカードへの移行を計画する際、コンテンツカードとニュースフィードの主な違いに注意することが重要である：

- **セグメンテーションである：**コンテンツカードのセグメンテーションは、メッセージが送信された時点、あるいはカードが最初に閲覧された時点で評価することができる。ニュースフィードのセグメンテーションは、ニュースフィードカードが閲覧された時点で評価される。
- **パーソナライゼーション：**コンテンツ・カードのパーソナライゼーションは、メッセージ送信時またはカードが最初に表示された時にテンプレート化できる。ニュースフィードカードのパーソナライゼーションは、ニュースフィードカードが表示された時点でテンプレート化される。

以下の表は、ニュースフィードとコンテンツカードのサポートされる機能の違いをさらに詳しく説明したものである：

| 特徴 | ニュースフィード | コンテンツカードによって促進された |
|---|---|---|
| 多変量解析とマルチチャンネル・キャンペーン | <i class="fas fa-times" title="サポートされていない"></i> | <i class="fas fa-check" title="サポート"></i> |
| スケジュール配信、アクションベース配信、APIベース配信 | <i class="fas fa-times" title="サポートされていない"></i> | <i class="fas fa-check" title="サポート"></i> |
| APIで作成されたメッセージ | <i class="fas fa-times" title="サポートされていない"></i> | <i class="fas fa-check" title="サポート"></i> |
| A/B テスト | <i class="fas fa-times" title="サポートされていない"></i> | <i class="fas fa-check" title="サポート"></i> |
| [カードを解任し、固定する][4] | <i class="fas fa-times" title="サポートされていない"></i> | <i class="fas fa-check" title="サポート"></i> |
| [豊富なアナリティクス][3]（コンバージョントラッキングなど） | <i class="fas fa-times" title="サポートされていない"></i> | <i class="fas fa-check" title="サポート"></i> |
| [キャンバス地][2] | <i class="fas fa-times" title="サポートされていない"></i> | <i class="fas fa-check" title="サポート"></i> |
| [コネクテッドコンテンツ][5] | <i class="fas fa-times" title="サポートされていない"></i> | <i class="fas fa-check" title="サポート"></i> |
| パーソナライゼーションとセグメンテーション | 印象でテンプレート化 | 送信時または第一印象でテンプレート化される |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 実装

- コンテンツ・カードとニュース・フィードは別の製品なので、コンテンツ・カードを使うには、アプリやウェブサイトの簡単な統合が必要だ。
- 必要に応じて、既存のニュースフィードカードをコンテンツカードキャンペーンに手動で移行する必要がある。
- コンテンツ・カードはニュース・フィードの代わりであるため、ニュース・フィードと同時に使用することは意図されていない。
- コンテンツ・カードは現在、カテゴリーをサポートしていない。カテゴリーは、[カスタマイズとキーと値のペアで][1]実現できる。


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/multiple_feeds/
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/content-cards_in_canvas/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#step-2-compose-a-content-card
[5]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/
