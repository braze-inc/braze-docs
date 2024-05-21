---
nav_title: 収益および総収益データのエクスポート
article_title: 収益および総収益データのエクスポート
page_order: 4
page_type: reference
description: "このリファレンス記事では、収益データと統計値をエクスポートする方法について説明します。"
tool: 
  - Reports

---

# 収益および総収益データのエクスポート

> ダッシュボードの [[収益レポート]({{site.baseurl}}/user_guide/data_and_analytics/reporting/revenue_report/)] ページでは、特定の期間の収益、特定の製品の収益、およびアプリの総収益のデータを確認できます。

**収益レポート**は [**分析**] の下にあります。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、[**収益**] は [**データ**] の下にあります。
{% endalert %}

{% alert tip %}
収益データを取得する他の方法を探している場合は、[コンバージョンイベント]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/)として、キャンペーンやキャンバスに (製品購入に加えて) 購入行動を追加してみてください。
{% endalert %}

収益データをエクスポートするには、[**経時的なパフォーマンス**] の<i class="fas fa-bars" title="[チャート] のコンテキストメニュー"></i>をクリックして、エクスポートオプションを選択します。

## [経時的なパフォーマンス] グラフ

[**経時的なパフォーマンス**] グラフから、以下のデータにアクセスできます。

- KPI 式
- 購入
    - (オプション) 製品別購入数
- 収益
    - (オプション) セグメント別収益
    - (オプション) 製品別収益
- 1 時間あたりの収益
    - (オプション) セグメント別 1 時間あたりの収益
- ユーザーあたりの収益

![収益グラフ][9]

## 総収益

[[キャンペーン分析]({{site.baseurl}}/user_guide/data_and_analytics/reporting/campaign_analytics/)] または [[キャンバス分析]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/)] のページで、ケースバイケースでの収益を確認できます。総収益の統計値は、キャンペーンの 1 次コンバージョン期間内に購入を行ったキャンペーン受信者から生成されます。

{% alert tip %}
収益レポートは API 経由でエクスポートできません。CSV のエクスポートに関するヘルプについては、「[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)」を参照してください。
{% endalert %}

{% comment %}

## 直接収益

[レポートビルダー][1]を使用してキャンペーン比較レポートを作成すると、収益に関する以下の追加指標を確認できます。

- [直接収益の合計][2]
- [直接購入数の合計][3]
- [ユニーク直接購入数][4]
- [受信者あたりの収益][5]

これらの指標は最終クリックのアトリビューションに基づきます。つまり、収益がキャンペーンに起因するには、そのキャンペーンは次の要件を満たす必要があります。

1. ユーザーが購入前にクリックした最後のキャンペーンである
    <br>**かつ**<br>
2. 購入前 3 日以内にユーザーがクリックする

{% endcomment %}

[1]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#total-direct-revenue
[3]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#total-direct-purchases
[4]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#unique-direct-purchases
[5]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#revenue-per-recipient



[9]: {% image_buster /assets/img_archive/Export_revenue_graph.png %}
