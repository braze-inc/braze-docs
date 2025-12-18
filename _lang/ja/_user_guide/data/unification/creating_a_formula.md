---
nav_title: 式の作成
article_title: 式の作成
page_order: 1.2
page_type: reference
description: "このリファレンス記事では、式の作成と管理について説明します。式は、データ内に存在する複雑な関係を簡単に把握するうえで役立ちます。"
tool: Reports

---
# 式の作成

> Braze で分析を確認する場合、複数のデータポイントを組み合わせてユーザーデータに関する貴重なインサイトを得ることができます。これらは式と呼ばれます。数式を使用して、月次アクティブユーザー(MAU)と日次アクティブユーザー(DAU)の総数に基づいて時系列データを正規化します。 

数式は、データに存在する複雑な関係を理解するのに役立ちます。例えば、特定のセグメントに該当する日次アクティブユーザーが完了したカスタムイベントの数を、一般層 (または他のセグメント) と比較できます。

## ユースケース

式を使用して、特にカスタムイベントと組み合わせると、アプリ内のユーザー行動を理解するのに役立ちます。また、Google 広告やテレビなどの有料メディアを Braze とともに使用している場合でも、式によりセグメントの購入パターンについてより深いインサイトが得られます。 

以下に、式を使用して検出できる行動パターンの種類の例をいくつか示します。

- **ライドシェアアプリ:**ユーザー キャンセルが乗車するときにカスタムイベントがある場合は、キャンセル ed Rides / DAU の機能を設定して、特定のユーザー Segmentが他よりも多くの乗車をキャンセルする傾向があるかどうかを確認できます。
- **e コマースアプリ:**特定の商品ID/MAUを購入する機能を設定することで、すべてのプロモーションをBrazeで追跡できなくても、最近プロモーションした商品の人気をSegments間で比較することができます。
- **広告を使用したメディアアプリ:**ユーザー体験が動画やオーディオクリップの間にある広告によって中断される場合、広告途中の離脱をカスタムイベントとして記録し、「広告途中の離脱 / DAU」の比率を計算することで、広告なしのプレミアムサブスクリプションのキャンペーンでターゲットにする最適なセグメントを見つけることができます。

## 式の作成

式には、ダッシュボードの [[ホーム]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard/)]、[[収益レポート]({{site.baseurl}}/user_guide/data/export_braze_data/exporting_revenue_data/)]、[[カスタムイベントレポート]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)] の各ページにある統計パネルからアクセスできます。このパネルを表示するには、**Performance Over Time** チャートに移動し、**Statistics For** ドロップダウンを**KPI Formulas** に変更してから、少なくとも1 つのKPI 数式を選択してチャートに入力します。

![Braze ダッシュボードでのKPI 数式の統計の表示]({% image_buster /assets/img_archive/kpi_forms.png %})

新規の式を作成するには、次の手順に従います。

1. 適切なダッシュボード ([**ホーム**]、[**収益レポート**]、または [**カスタムイベントレポート**]) に移動します。
2. **KPI 数式の管理**を選択します。
3. 式の名前を入力します。
4. 該当する分子と分母を選択します。
5. [**保存**] を選択します。

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
| セッション | DAU |
| | セグメントサイズ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 収益ダッシュボード

| 分子 | 分母 |
| --- | --- |
| 購入(全額) | DAU |
| 購入を選択(ギフトカードや商品IDなど) | MAU |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### カスタムイベントダッシュボード

| 分子 | 分母 |
| --- | --- |
| カスタムイベントカウント | MAU |
|  | DAU |
|  | セグメントサイズ([アナリティクストラッキング]({{site.baseurl}}/viewing_and_understanding_segment_data/)が有効なセグメントのみ使用できます) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

