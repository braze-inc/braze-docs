---
nav_title: ニュースフィードからの移行
article_title: ニュースフィードからの移行
page_order: 10
description: "このリファレンス記事では、ニュースフィードから Braze のコンテンツカードへの移行に関するガイダンスを提供します。"
channel:
  - content cards
  - news feed
  
---

# ニュースフィードからコンテンツカードへの移行

{% alert note %}
ニュースフィードは非推奨になります。Braze は、ニュースフィードツールを使っている顧客には、コンテンツカードのメッセージングチャネルに移行することを勧めています。
{% endalert %}

> ニュースフィードからコンテンツカードへの移行には時間がかかりますが、容易に採用できます。コンテンツをニュースフィードからコンテンツカードに自動的に移行することはできません。コンテンツカードをゼロから統合する必要があります。しかし、コンテンツカードには新しい柔軟性があるため、うまくいかなかったり、心配する必要はありません。

詳細については、Brazeのアカウント・マネージャーに問い合わせを。

## 特長と機能

コンテンツカードは、アクションベースの配信や API 配信などの追加配信オプションや、コンバージョン追跡などの強化された分析など、ニュースフィードではサポートされていない多くの機能を備えています。

ニュースフィードからコンテンツカードへの移行を計画する際、コンテンツカードとニュースフィードの主な違いに注意することが重要である：

- **セグメンテーション:**コンテンツカードのセグメンテーションは、メッセージが送信された時点、あるいはカードが最初に閲覧された時点で評価することができる。ニュースフィードのセグメンテーションは、ニュースフィードカードが閲覧された時点で評価される。
- **パーソナライゼーション:**コンテンツ・カードのパーソナライゼーションは、メッセージ送信時またはカードが最初に表示された時にテンプレート化できる。ニュースフィードカードのパーソナライゼーションは、ニュースフィードカードが表示された時点でテンプレート化される。

以下の表は、ニュースフィードとコンテンツカードのサポートされる機能の違いをさらに詳しく説明したものである：

| 特徴 | ニュースフィード | コンテンツカードによって促進された |
|---|---|---|
| 多変量キャンペーンとマルチチャネルキャンペーン | <i class="fas fa-times" title="サポートしない"></i> | <i class="fas fa-check" title="サポートする"></i> |
| スケジュール配信、アクションベース配信、APIベース配信 | <i class="fas fa-times" title="サポートしない"></i> | <i class="fas fa-check" title="サポートする"></i> |
| APIで作成されたメッセージ | <i class="fas fa-times" title="サポートしない"></i> | <i class="fas fa-check" title="サポートする"></i> |
| A/B テスト | <i class="fas fa-times" title="サポートしない"></i> | <i class="fas fa-check" title="サポートする"></i> |
| [カードのピン留めとその解除][4] | <i class="fas fa-times" title="サポートしない"></i> | <i class="fas fa-check" title="サポートする"></i> |
| [豊富なアナリティクス][3]（コンバージョントラッキングなど） | <i class="fas fa-times" title="サポートしない"></i> | <i class="fas fa-check" title="サポートする"></i> |
| [キャンバスで使用可能][2] | <i class="fas fa-times" title="サポートしない"></i> | <i class="fas fa-check" title="サポートする"></i> |
| [コネクテッドコンテンツ][5] | <i class="fas fa-times" title="サポートしない"></i> | <i class="fas fa-check" title="サポートする"></i> |
| パーソナライゼーションとセグメンテーション | インプレッション時にテンプレート化 | 送信時または第一印象でテンプレート化される |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 実装

- コンテンツカードとニュースフィードは別の製品であるため、コンテンツカードを使用するには、アプリや Web サイトのシンプルな連携が必要です。
- 必要に応じて、切り替え時に既存のニュースフィードカードを手動でコンテンツカードキャンペーンに移行する必要があります。
- コンテンツ・カードはニュース・フィードの代わりであるため、ニュース・フィードと同時に使用することは意図されていない。
- コンテンツ・カードは現在、カテゴリーをサポートしていない。カテゴリは、[カスタマイズおよびキーと値のペア][1]で実現できます。


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/multiple_feeds/
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/content-cards_in_canvas/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#step-2-compose-a-content-card
[5]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/
