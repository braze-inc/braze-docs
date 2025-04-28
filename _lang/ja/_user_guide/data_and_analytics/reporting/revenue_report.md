---
nav_title: 収益レポート
article_title: 収益レポート
page_type: reference
description: "このリファレンス記事では、[収益レポート] ページについて説明します。"
tool: Reports
---

# 収益レポート

> [収益レポート] ページでは、特定期間の収益、特定製品の収益、アプリの総収益に関するデータを表示できます。

ダッシュボードから収益レポートを表示するには、[**分析**] > [**収益レポート**] に移動します。 

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合、このページは [**データ**] の下にあります。
{% endalert %}

## 収益レポートのカスタマイズ

期間やレポート対象のアプリ、およびパラメーターを選択して、収益レポートをカスタマイズできます。

![パラメーターとして [収益] を設定した [経時的なパフォーマンス] グラフを表示している [収益レポート] ページ。][1]

### 日付とアプリを使用したフィルターの適用

収益レポートの期間を選択し、必要に応じてアプリを 1 つ以上選択します。

### パラメーターを使用したフィルターの適用

**経時的なパフォーマンス**グラフには、さまざまなパラメーターのデータが表示されます。これらのパラメーターは、[**次に関する統計**] ドロップダウンで選択できます。オプションで、[**内訳**] ドロップダウンで特定のパラメーターのデータを分類できます。

**経時的なパフォーマンス**グラフには、以下のデータを表示でます。
- KPI 式
- 購入
    - (オプション) 製品別購入数
- 収益
    - (オプション) セグメント別収益
    - (オプション) 製品別収益
- 1 時間あたりの収益
    - (オプション) セグメント別 1 時間あたりの収益
- ユーザーあたりの収益

## 収益計算の理解

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>指標</th>
            <th>定義</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-revenue">生涯収益</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Lifetime Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-value-per-user">ユーザーあたりの生涯価値</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='ユーザあたりの寿命値' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#average-daily-revenue">平均日割り売上</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='平均日割り売上' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#daily-purchases">日割り購入数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='日割り購入数' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#daily-revenue-per-user">ユーザーあたりの日割り収益</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='ユーザーあたりの日次収益' %}</td>
        </tr>
    </tbody>
</table>

## 製品の内訳の確認

選択した日付範囲内で購入された製品のリスト、各製品の購入数、および各製品で生成された収益の量については、**Product Breakdown**テーブルを参照してください。

![「製品名」、「購入数」、「収益」の各列を示す [製品の内訳] のテーブル][2]


[1]: {% image_buster /assets/img/revenue_report.png %}
[2]: {% image_buster /assets/img/revenue_report_product_breakdown.png %}
