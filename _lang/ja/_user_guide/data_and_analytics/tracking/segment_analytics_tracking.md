---
nav_title: セグメント分析の追跡
article_title: セグメント分析の追跡
page_order: 8
page_type: reference
description: "このリファレンス記事では、Segment 分析 \"トラッキングと、経時的な収益と購入、経時的なセッションs、経時的なカスタムイベントs の表示方法について説明します。"
tool: 
  - Segments
  - Reports
---

# セグメント分析の追跡

> 分析 "トラッキング がSegmentに対して有効になっている場合、そのSegmentのセッションs、カスタムイベントs、および収益を経時的に表示できます。

セグメント分析の追跡をオンにしなくても、そのセグメントの[リアルタイム統計情報][11]にアクセスして、ユーザーをキャンペーンのターゲットにすることができます。唯一の違いは、このページに記載されている特定の分析ツールにアクセスできるかどうかです。

## Segment 分析を有効にする

Segmentのページ** Segment Details** セクションで、**Analytics Tracking** を有効にします。

![Segmentの分析"トラッキングの切り替え][16]

アプリでは、最大 25 個のセグメントについて追跡をオンにすることができます。Braze では、キャンペーンがセッション、収益、および購入に及ぼす効果を把握するうえで、分析すべき重要なセグメントを追跡することをお勧めします。

## 経時的な収益と購入の表示

[このセグメントの収益と購入の推移][14]に関するデータを表示するには、\[**分析**] > \[**収益レポート**] に移動します。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation) を使用している場合、**Revenue** は**Data** にあります。
{% endalert %}

![Segment別売上高][17]

任意のカスタム期間のセグメントデータを視覚的に比較するには、セグメントをグラフに追加するか、グラフから削除します。****Breakdown**ドロップダウンで**Segment**を選択し、**Breakdown values**でSegmentを選択します。

グラフの上にある任意のSegmentネームを選択して、そのSegmentのメトリクスの表示/非表示を切り替えます。

![マルチSegmentの収益][21]

## セッション数の推移

同様に、[この特定セグメントのセッション数の推移][13]に関するデータは、\[**ホーム**] ページで確認できます。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、これは \[**概要**] ページです。
{% endalert %}

![Segment別セッションデーター][18]

## カスタムイベントsの経時的な表示

\[Segment s][20] の\[カスタムイベントの経時的推移] を**Analytics** > **カスタムイベントレポート** に移動して表示します。

## クエリービルダーのテンプレートの使用

分析の追跡をオンにすると、クエリビルダーのレポートテンプレートを使用して、キャンペーン、キャンバス、バリアント、ステップのパフォーマンス指標をセグメント別に分類できます。詳細については、「[セグメントデータ]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#performance-data-by-segment)」を参照してください。

[11]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#segment-statistics
[13]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_app_usage_data/#exporting-app-usage-data
[14]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/
[16]: {% image_buster /assets/img_archive/A_Tracking_2.png %}
[17]: {% image_buster /assets/img_archive/Revenue.png %}
[18]: {% image_buster /assets/img_archive/events_over_time2.png %}
[20]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#analytics
[21]: {% image_buster /assets/img_archive/segment_revenue_multiple.png %}
