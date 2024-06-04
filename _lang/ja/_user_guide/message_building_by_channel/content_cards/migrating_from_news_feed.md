---
nav_title: ニュースフィードからの移行
article_title: ニュースフィードからの移行
page_order: 10
description: "このリファレンス記事では、ニュース フィードから Braze コンテンツ カードへの移行に関するガイダンスを提供します。"
channel:
  - content cards
  - news feed
  
---

# ニュースフィードからコンテンツカードへの移行

{% alert note %}
ニュースフィードは非推奨になります。Braze では、ニュース フィード ツールを使用しているお客様に、より柔軟性、カスタマイズ性、信頼性に優れたコンテンツ カード メッセージング チャネルへの移行を推奨しています。
{% endalert %}

> ニュース フィードからコンテンツ カードへの移行には時間がかかりますが、導入は簡単です。ニュース フィードからコンテンツ カードにコンテンツを自動的に移行することはできません。コンテンツ カードを最初から統合する必要があります。ただし、コンテンツ カードの新しい柔軟性により、それがなくても困ったり気にしたりすることはないと思います。

詳細については、Braze アカウント マネージャーにお問い合わせください。

## 特徴と機能

コンテンツ カードには、アクション ベースや API 配信などの追加の配信オプションや、コンバージョン トラッキングなどの強化された分析機能など、ニュース フィードではサポートされていない多くの機能が用意されています。

ニュース フィードからコンテンツ カードへの移行を計画する際には、コンテンツ カードとニュース フィードの主な違いに注意することが重要です。

- セグメンテーションコンテンツ カードのセグメンテーションは、メッセージが送信されたとき、またはカードが最初に表示されたときに評価できます。ニュース フィードのセグメンテーションは、ニュース フィード カードが表示された時点で評価されます。
- パーソナライゼーションコンテンツ カードのパーソナライズは、メッセージの送信時またはカードが最初に表示されたときにテンプレート化できます。ニュース フィード カードのパーソナライズは、ニュース フィード カードが表示された時点でテンプレート化されます。

次の表は、ニュース フィードとコンテンツ カードでサポートされる機能の違いをさらに示しています。

| 特集 | ニュースフィード | コンテンツカード |
|---|---|---|
| 多変量およびマルチチャネル キャンペーン | <i class="fas fa-times" title="サポートされていません"></i> | <i class="fas fa-check" title="サポートされています"></i> |
| スケジュール、アクションベース、API ベースの配信 | <i class="fas fa-times" title="サポートされていません"></i> | <i class="fas fa-check" title="サポートされています"></i> |
| API 作成メッセージ | <i class="fas fa-times" title="サポートされていません"></i> | <i class="fas fa-check" title="サポートされています"></i> |
| A/B テスト | <i class="fas fa-times" title="サポートされていません"></i> | <i class="fas fa-check" title="サポートされています"></i> |
| [カードの消去とピン留め][4] | <i class="fas fa-times" title="サポートされていません"></i> | <i class="fas fa-check" title="サポートされています"></i> |
| [豊富な分析機能][3] (コンバージョン トラッキングなど) | <i class="fas fa-times" title="サポートされていません"></i> | <i class="fas fa-check" title="サポートされています"></i> |
|[Canvas で利用可能][2] | <i class="fas fa-times" title="サポートされていません"></i> | <i class="fas fa-check" title="サポートされています"></i> |
| [接続されたコンテンツ][5] | <i class="fas fa-times" title="サポートされていません"></i> | <i class="fas fa-check" title="サポートされています"></i> |
| パーソナライゼーションとセグメンテーション | インプレッション時にテンプレート化 | 送信時または第一印象時にテンプレート化 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 実装

- コンテンツ カードとニュース フィードは別々の製品であるため、コンテンツ カードを使用するには、アプリまたは Web サイトに簡単に統合する必要があります。
- 必要に応じて、切り替え時に既存のニュース フィード カードを手動でコンテンツ カード キャンペーンに移行する必要があります。
- コンテンツ カードはニュース フィードの代わりとなるため、ニュース フィードと同時に使用することは想定されていません。
- コンテンツ カードは現在カテゴリをサポートしていません。カテゴリは [カスタマイズとキーと値のペア][1]によって実現できます。


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/multiple_feeds/
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/content-cards_in_canvas/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#step-2-compose-a-content-card
[5]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/
