---
nav_title: 式の作成
article_title: 式の作成
page_order: 1.2
page_type: reference
description: "このリファレンス記事では、式の作成と管理について説明します。式は、データ内に存在する複雑な関係を簡単に把握するうえで役立ちます。"
tool: Reports

---
# 式の作成

> Braze で分析を確認するときに、複数のデータポイントを組み合わせると、ユーザーデータに関する貴重なインサイトを得ることができます。これらは式と呼ばれます。式を使用すると、月間アクティブユーザー数 (MAU) と 1 か月あたりのアクティブユーザー数 (DAU) の合計に基づいて、時系列データを正規化することができます。また、データ内に存在する複雑な関係を簡単に把握するうえでも役立ちます。 

例えば、特定のセグメントに該当する日次アクティブユーザーが完了したカスタムイベントの数を、一般層 (または他のセグメント) と比較できます。

## ユースケース

式を使用すると、特にカスタムイベントと組み合わせると、アプリ内のユーザー行動をよりよく把握できます。また、Google 広告やテレビなどの有料メディアを Braze とともに使用している場合でも、式によりセグメントの購入パターンについてより深いインサイトが得られます。 

以下に、式を使用して検出できる行動パターンの種類の例をいくつか示します。

- **ライドシェアアプリ:** ユーザーが乗車をキャンセルしたときのカスタムイベントがある場合、「キャンセルされた乗車回数 / DAU」という関数を設定することで、特定のユーザーセグメントが他のユーザーセグメントより多くの乗車をキャンセルする傾向があるかどうかを調べることができます。
- **e コマースアプリ:**「特定の商品 ID の購入数 / MAU」の関数を設定すると、Braze を使用してすべてのプロモーションを追跡できなくても、最近プロモーションを行った商品の人気をセグメント間で比較できます。
- **広告を使用したメディアアプリ:** ユーザー体験が動画やオーディオクリップの間にある広告によって中断される場合、広告途中の離脱をカスタムイベントとして記録し、「広告途中の離脱 / DAU」の比率を計算することで、広告なしのプレミアムサブスクリプションのキャンペーンでターゲットにする最適なセグメントを見つけることができます。

## 式の作成

式には、ダッシュボードの [[ホーム][9]]、[[収益][10]]、[[カスタムイベント][11]] の各ページにある {統計] パネルからアクセスできます。このパネルを表示するには、[**次に関する統計を表示**] ドロップダウンを [**KPI 式**] に変更します。

![Braze ダッシュボードに KPI 式の統計を表示][16]

新規の式を作成するには、次の手順に従います。

1. 適切なダッシュボード (ホーム、収益、またはカスタムイベント) に移動します。
2. [**KPI 式を管理**] をクリックします。
3. 式の名前を入力します。
4. 該当する分子と分母を選択します。
5. [**保存**] をクリックします。

## 利用可能な分子と分母

<style>
  div.small_table + table {
    max-width: 50%;
  }
  div.large_table + table {
    max-width: 75%;
  }
table th:nth-child(1),
table th:nth-child(2),
table th:nth-child(3),
table td:nth-child(1),
table td:nth-child(2),
table td:nth-child(3) {
    width:25%;
}
table td {
    word-break: break-word;
}
</style>

<div class="small_table"></div>

### 概要ダッシュボード

| 分子 | 分母 |
| --- | --- |
| DAU | MAU |
| セッション数 | DAU |
| | セグメントサイズ |
{: .reset-td-br-1 .reset-td-br-2}

### 収益ダッシュボード

| 分子 | 分母 |
| --- | --- |
| 購入数 (すべて) | DAU |
| 選択購入数 (ギフトカードや製品 ID など) | MAU |
{: .reset-td-br-1 .reset-td-br-2}

### カスタムイベントダッシュボード

| 分子 | 分母 |
| --- | --- |
| カスタムイベント数 | MAU |
|  | DAU |
|  | セグメントサイズ ([分析の追跡][17]が有効になっているセグメントのみが使用可能) |
{: .reset-td-br-1 .reset-td-br-2}

[9]: {{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/
[10]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/
[11]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[16]: {% image_buster /assets/img_archive/kpi_forms.png %}
[17]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/