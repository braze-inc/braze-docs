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

> セグメント分析の追跡をオンにすると、そのセグメントのセッション数、カスタムイベント数、および収益の推移を表示できます。

![セグメント分析の追跡トグル][16]

セグメント分析の追跡をオンにしなくても、そのセグメントの[リアルタイム統計情報][11]にアクセスして、ユーザーをキャンペーンのターゲットにすることができます。唯一の違いは、このページに記載されている特定の分析ツールにアクセスできることです。

アプリでは、最大 25 個のセグメントについて追跡をオンにすることができます。Braze では、キャンペーンがセッション、収益、および購入に及ぼす効果を把握するうえで、分析すべき重要なセグメントを追跡することをお勧めします。

## 収益と購入の推移

[このセグメントの収益と購入の推移][14]に関するデータを表示するには、[**分析**] > [**収益レポート**] に移動します。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、[**収益**] は [**データ**] の下にあります。
{% endalert %}

任意のカスタム期間のセグメントデータを視覚的に比較するには、セグメントをグラフに追加するか、グラフから削除します。[**セグメント別**] を選択し、チャートに表示するセグメントを検索します。凡例項目をクリックすると、その指標の表示 / 非表示が切り替わります。

![セグメント別収益データ][17]

## セッション数の推移

同様に、[この特定セグメントのセッション数の推移][13]に関するデータは、[**ホーム**] ページで確認できます。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、これは [**概要**] ページです。
{% endalert %}

![セグメント別のセッション数データ] [18]

## カスタムイベント数の推移

Braze では、[**分析**] > [**カスタムイベントレポート**] に移動して、[セグメントのカスタムイベント数の推移][20]に関するデータを表示することもできます。

## クエリビルダー

分析の追跡をオンにすると、クエリビルダーのレポートテンプレートを使用して、キャンペーン、キャンバス、バリアント、ステップのパフォーマンス指標をセグメント別に分類できます。詳細については、「[セグメントデータ]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#performance-data-by-segment)」を参照してください。

[11]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#segment-statistics
[13]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_app_usage_data/#exporting-app-usage-data
[14]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/
[16]: {% image_buster /assets/img_archive/A_Tracking_2.png %}
[17]: {% image_buster /assets/img_archive/Revenue.png %}
[18]: {% image_buster /assets/img_archive/events_over_time2.png %}
[20]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#analytics
