---
nav_title: Report Builder
article_title: Report Builder
alias: /report_builder/
page_order: 4
page_type: reference
description: "This reference article covers how to run a report using the report builder including campaign and Canvas creating comparison reports, and building reports and charts."
tool: 
  - Reports

---

# Report Builder

> The Report Builder allows you to compare the results of multiple campaigns or Canvases in a single view so that you can easily determine which engagement strategies most impacted your key metrics.キャンペーンとキャンバスの両方について、データをエクスポートし、レポートを保存して今後表示できます。

![キャンペーン比較例][5]{: style="max-width:80%;"}

このレポートを使用して、主要なエンゲージメントに関する質問の答えを求めます。以下に例を示します。

- Which were the best performing campaigns or Canvases for a specific tag or channel?
- Which variants of multivariant campaigns had the most uplift over the control?  
- Which seasonal promotion campaign led to a higher purchase rate—the summer sale, fall sale, or winter sale?
- Which push notifications within this Canvas had the highest open rates?
- Which steps in this group of Canvases had the most conversions?
- Did Version 1 of a welcome email or Version 2 of a welcome email lead to higher engagement and conversion?Did the changes work?
- How do different delivery methods (for example, 3 scheduled pushes, 3 action-based pushes, and 3 API-triggered pushes) impact your open rates, conversion rates, or purchase rates?
- Have the ongoing improvements to lapsing user messages positively impacted your KPIs over time?

{% alert tip %}
Try to use the same conversion events for conversion A, B, etc. across campaigns and Canvases you wish to compare, so that you can line up these conversions in your Report Builder reports.
{% endalert %}

## Run a report

### Step 1:Create a new report

Within the dashboard, navigate to **Analytics** > **Report Builder**.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can find **Report Builder** under **Data**.
{% endalert %}

Click **Create New Report** and select either a campaign comparison report or a Canvas comparison report.

If you choose to run a report on campaigns, you can select between a **Manual** or **Automated** report.Reports may contain either campaigns or Canvases, but not both together.過去 6 か月以内に最後にメッセージを送信したキャンペーンおよびキャンバスがすべて、レポートの対象になります。

![キャンペーン・ダッシュボード][6]{: style="max-width:80%;"}

この 2 つのオプションの違いを以下に示します。

| **アクション (Action)** | **マニュアル** | **自動化された** |
| ---- | ---------- | ------------- |
| **建物レポート** | フィルターを使ってキャンペーンリストを絞り込み、特定のキャンペーンにチェックを入れることができる。 | フィルターオプションを使ってキャンペーンリストを絞り込み、レポートを作成する。 |
| **レポートの保存と閲覧** | レポートを保存することができる。これらのキャンペーンはまだ「最後に送信されたもの」フィルターに該当するため、次に表示するときは、以前に追加したのと同じキャンペーンを表示することができる。 | レポートを保存することができる。次回の閲覧時には、レポートが自動的に更新され、現在フィルターに一致するすべてのキャンペーンが含まれるようになる。 |
| **編集レポート** | レポートの編集をクリックすると、レポートからキャンペーンを追加または削除できる。 | フィルター基準を調整することで、レポートを編集することができる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %}
Both **Manual** and **Automated** reports can include a maximum of 250 campaigns in a report.
{% endalert %}

Canvas reports work similarly to a manual campaign report in that Canvas selections and report updates must also be done manually.You can include at most five Canvases in one report.

### Step 2:Choose your metrics

Once you've created your report, you'll find a blank table containing campaigns in each row.\[**列を編集**] を選択し、追加する指標を選択すると、テーブルにデータが読み込まれます。

![キャンペーン・オプション][15]{: style="max-width:80%;"}

選択した指標がテーブルに読み込まれます。For definitions of these metrics, refer to the [Report Metrics Glossary][16].Some metrics are only available for campaign comparison reports.

You can also toggle calculations for the **Average** of any rate or numerical metric and **Total** for any numerical metric.

### Step 3:Choose a time period

You can select a specific time period to view your report's data for.特定のキャンペーン、キャンバス、キャンバスバリアント、またはキャンバスコンポーネントに選択した期間のデータがない場合、その行の結果は空白になります。 

![キャンペーンの数値指標][4]{: style="max-width:60%;"}

### ステップ 4:Name and save your report

Name your report before saving it.レポートに名前を付けずに保存すると、Braze によりデフォルトの名前である「キャンペーン比較レポート」が適用されます。

![キャンペーンノート][7]{: style="max-width:60%;"}

準備ができたら、\[**保存**] をクリックします。Saved reports can be viewed at a later point on the **Report Builder** page.

## Campaign comparison report with multivariate campaigns

For any multivariate campaigns, you can view these metrics broken down by your variants and control group by clicking the arrow next to the campaign name.バリアントを含む行にはそのバリアントのパフォーマンス結果が含まれ、コントロールを含む行にはコンバージョンイベントの結果のみが含まれます。 

![キャンペーンノート][3]{: style="float:right;max-width:15%;margin-left:15px;"}

キャンペーン全体の行にある指標には、そのバリアントのパフォーマンスが反映されますが、コントロールのパフォーマンスは含まれません。For instance, Primary Conversion Event A for your overall campaign will be the sum of the Primary Conversion Event A for your variants, and this will not include the Primary Conversion Event A for your control.

{% alert important %}
If you delete a variant from a multivariant campaign, the data from that variant will not be available for use in a future report.
{% endalert %}

## Canvas comparison report breakdown

Within a Canvas report, you can view your Canvases broken down by variant, steps, or message.

### Variant

\[**バリアントごとの内訳**] を選択すると、キャンバス全体の大まかな統計情報と、各バリアントの統計情報が表示されます。これらの統計情報は、キャンバス名の横にある矢印をクリックすると展開できます。

![バリエーション][12]{: style="max-width:90%;"}

### ステップ 

\[**ステップごとの内訳**] を選択すると、ステップレベルの指標を表示できます。レポートの各行にステップの行が含まれます。

![ステップ][13]{: style="max-width:90%;"}

### メッセージ

Similar to a step-level breakdown, selecting **breakdown by message** shows the name of steps in each row.ただし、\[**列を編集**] では、メールクリック数やプッシュ通知の開封数など、チャネル固有の統計情報のようなメッセージレベルの指標にアクセスできます。

![レポート][14]{: style="max-width:90%;"}

なお、Braze ダッシュボードでは、キャンバスレポートの最初の 50 行をプレビューできます。You can access the full report when you export a CSV.

## Accessing saved reports

When you access a saved **Manual Report**, you will be able to view the same campaigns you previously added, as these campaigns still fall under your "Last Sent" filter.

When you access a saved **Automatic Report**, the report will automatically update to include all campaigns that currently match your filters.For instance, if your report filtered campaigns with the tag "Promotion," then each time you view this report, you will be able to see all campaigns with the "Promotion" tag, even if these campaigns were created after you made this report.

## Editing reports

In a **Manual Report**, you can edit a report by clicking **Edit**.From there, you can select or deselect campaigns to include in your report.

In an **Automatic Report**, simply toggle your filters to narrow down the results in your report.

## Exporting reports

You can also click **Export** to download your report to CSV.

If your report contains any multivariant campaigns, your export will include two CSV files: 

- One file containing only the top-level metrics for each campaign
- One file that contains variant-level metrics

The file containing variant metrics will have `variant_` appended to the beginning of its name.自動レポートを初めてエクスポートするときに、複数ファイルのダウンロードの許可を求めるポップアップが表示されます。\[**許可**] をクリックします。

![キャンペーンダウンロード][8]{: style="max-width:60%;"}

### キャンバス比較レポートのエクスポート

Your CSV export will reflect whichever breakdown view you were on when you clicked **Export**.For instance, if you were on the step-level breakdown view, your export will contain data on your step metrics.To export data from a different breakdown, you'll need to navigate to that breakdown first, and click **Export** from there.

If you download a variant breakdown Canvas report, you'll receive two CSV files:

- One file containing only top-level metrics for each Canvas
- One file that contains variant-level metrics

## Building Charts 

Use charts to visualize a selected metric in your report.チャートは、キャンペーンに関するレポートで、その列に少なくとも 1 つの指標が追加されている場合に使用できます。

![キャンペーン・パフォーマンス・チャート。][17]

デフォルトでは、各レポートのチャートに、レポートの最初の列の指標が表示されます。To select a different metric to graph, choose your metric from the dropdown.Any metric in your report table will be available to display in your chart.

You can graph at most three metrics.The units for all metrics must be the same—for instance, if you choose a rate in the first dropdown, then only rates will be available for selection in the second dropdown.

If your chart contains only one metric, then it will display up to 30 campaigns in descending order based on the metric you've selected.For example, if your chart's metric is email clicks, then your chart will display the 30 email campaigns with the most clicks, ordered from most to fewest clicks.If your report contains more than 30 campaigns, only the top 30 will be displayed in the chart.If you select more than one metric, then your graph will only display the top five campaigns based on the first metric selected.

Charts are currently not saved when you save your report.


[3]: {% image_buster /assets/img/campaign_comparison/compare_note.png %}
[4]: {% image_buster /assets/img/campaign_comparison/metric.png %}
[5]: {% image_buster /assets/img/campaign_comparison/campaign_main.png %}
[6]: {% image_buster /assets/img/campaign_comparison/create_report.png %}
[7]: {% image_buster /assets/img/campaign_comparison/comparison_name.png %}
[8]: {% image_buster /assets/img/campaign_comparison/download.png %}
[12]: {% image_buster /assets/img/campaign_comparison/campaign_comparison1.png %}
[13]: {% image_buster /assets/img/campaign_comparison/campaign_comparison2.png %}
[14]: {% image_buster /assets/img/campaign_comparison/campaign_comparison3.png %}
[15]: {% image_buster /assets/img/campaign_comparison/campaign_comparison_columns.png %}
[17]: {% image_buster /assets/img/campaign_comparison/report_builder_charts.png %}

[16]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/
