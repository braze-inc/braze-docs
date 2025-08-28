---
nav_title: セグメント分析の追跡
article_title: セグメント分析の追跡
page_order: 8
page_type: reference
description: "このリファレンス記事では、セグメント分析の追跡と、収益と購入の推移、セッション数の推移、およびカスタムイベント数の推移を確認する方法について説明します。"
tool: 
  - Segments
  - Reports
---

# セグメント分析の追跡

> あるセグメントについて、[分析の追跡] がオンになっている場合、そのセグメントのセッション、カスタムイベント、および収益の推移を表示できます。

セグメント分析の追跡をオンにしなくても、そのセグメントの[リアルタイム統計情報]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#segment-statistics)にアクセスして、ユーザーをキャンペーンのターゲットにすることができます。唯一の違いは、このページに記載されている特定の分析ツールにアクセスできるかどうかです。

## Segment 分析を有効にする

Segmentのページ** Segment Details** セクションで、**Analytics Tracking** を有効にします。

![セグメントの [分析の追跡] トグル]({% image_buster /assets/img_archive/A_Tracking_2.png %})

アプリでは、最大 25 個のセグメントについて追跡をオンにすることができます。Braze では、キャンペーンがセッション、収益、および購入に及ぼす効果を把握するうえで、分析すべき重要なセグメントを追跡することをお勧めします。

## 収益と購入の推移の表示

[このセグメントの収益と購入の推移]({{site.baseurl}}/user_guide/data/export_braze_data/exporting_revenue_data/)に関するデータを表示するには、[**分析**] > [**収益レポート**] に移動します。

![セグメント別収益データ]({% image_buster /assets/img_archive/Revenue.png %})

任意のカスタム期間のセグメントデータを視覚的に比較するには、セグメントをグラフに追加するか、グラフから削除します。**Breakdown**ドロップダウンで**Segment**を選択し、**Breakdown values**でSegmentを選択します。

グラフの上にある任意のSegmentネームを選択して、そのSegmentのメトリクスの表示/非表示を切り替えます。

![複数セグメントの収益]({% image_buster /assets/img_archive/segment_revenue_multiple.png %})

## セッション数の推移

同様に、[この特定セグメントのセッション数の推移]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_app_usage_data/#exporting-app-usage-data)に関するデータは、[**ホーム**] ページで確認できます。

![セグメント別セッションデータ]({% image_buster /assets/img_archive/events_over_time2.png %})

## カスタムイベントsの経時的な表示

[**分析**] > [**カスタムイベントレポート**] に移動して、[セグメントのカスタムイベント数の推移に関するデータ]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#analytics)を表示します。

## クエリビルダーのテンプレートの使用

分析の追跡をオンにすると、クエリビルダーのレポートテンプレートを使用して、キャンペーン、キャンバス、バリアント、ステップのパフォーマンス指標をセグメント別に分類できます。詳細については、「[セグメントデータ]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#performance-data-by-segment)」を参照してください。

