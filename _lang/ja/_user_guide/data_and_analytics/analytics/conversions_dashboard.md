---
nav_title: Conversions Dashboard
article_title: Conversions Dashboard
alias: "/conversions_dashboard_v2/"
description: "The conversions dashboard allows you to analyze conversions across campaigns, Canvases, and channels, using different attribution methods."
page_order: 3
page_type: reference
tool: 
  - Reports
---

# Conversions dashboard

> The conversions dashboard allows you to analyze conversions across campaigns, Canvases, and channels, using different [attribution methods](#attribution-methods).When measuring your conversions, you can specify the time frame, conversion event, and conversion window.

## Setting up your report

To set up your conversions dashboard report:

1. Navigate to **Analytics** > **Conversions**.
2. Select a **Date Range** for your report, up to a 90-day window.
3. Select the campaigns or Canvases (or both) that you would like to analyze. 
   - If you would like to filter campaigns and Canvases by tag, select a **Tag**.  
4. Select the **Channel(s)** you would like to analyze for your messages.
5. (optional) If desired, select a **Breakdown** layer.This allows you to view different dimensions of data, such as by variant, Canvas step, country, or language.
6. (optional) If you are interested in calculating conversions of an event that was not set up as a conversion event on the campaign or Canvas, turn on [Use custom events](#using-custom-events).
7. Select an [Attribution Method](#attribution-methods) through which to analyze the selected messages.

{% alert note %}
If you are analyzing conversions for multiple channels, your **Attribution Method** will default to **Last-Touch Attribution**.
{% endalert %}

{:start="8"}
8\.Click **Create** to run the report.

After the page has loaded, select a **Conversion Event** to filter the report for conversion data.The available selections will include the events that were pre-configured on the Canvases and campaigns.If you selected a custom event when setting up your report (step 6), this option is not available.

### Using custom events

If you are interested in calculating conversions of an event that was not set up as a conversion event on the campaign or Canvas, you can select a specific custom event to use as a conversion event. 

1. When setting up your report, turn on **Use custom events**.
2. Select a custom event that you would like to use as the conversion event.
3. Select the conversion window within which that event should have occurred to be counted as a conversion.

{% alert note %}
If you select a custom event, you will not see the **Conversion Event** dropdown on the page and will have to re-run to report to view conversions for different custom events.
{% endalert %}

## Understanding your results

Your report is split into three sections:

- [Conversion details](#conversion-details)
- [Conversion funnel](#conversion-funnel)
- [Conversions over time](#conversions-over-time)

### Conversion details

The conversion details table will always show one column for *Recipients* and another for *Conversions* (rate and total).The remaining two table columns that appear depend on the options you selected when setting up your report.The following table describes possible metrics.

| Metric shown | Description |
 | --- | --- |
| Recipients | The number of users who received a message through the selected channel within the report's date range |
| Conversion Rate (Recipients) | Calculated as:(Number of conversions) / (Number of recipients) |
| Attribution method | Defined by the [attribution method](#attribution-methods) you selected when you set up the report.For Last Touch attribution or if multiple channels are selected, this appears as [Touches](#terms-to-know). |
| Conversion Rate (Attribution method) | Defined by the [attribution method](#attribution-methods) you selected when you set up the report.If multiple channels are selected, this defaults to last-touch attribution. |
{: .reset-td-br-1 .reset-td-br-2 }

![]({% image_buster /assets/img_archive/conversions2_details.png %})

レポートの設定時に、キャンペーンまたはキャンバスの内訳レベルの詳細を選択した場合 (ステップ 6) は、<i class="fas fa-angle-down"></i> をクリックして表を展開できます。

### Conversion funnel

This bar graph shows the absolute counts for each [engagement event]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events) based on the selected channel.The conversions count will be defined as per the selected attribution method.

By default, all selected campaigns and Canvases are shown.To deselect a campaign or Canvas, click on the name of the campaign or Canvas that you'd like to exclude.For additional details on the engagement event, you can hover over each bar.

To download the time series data, click and select your download option.Available options are PNG, JPEG, PDF, SVG, or CSV.

{% alert note %}
This graph only shows data for a single channel at a time.Use the **Channel** dropdown on the chart to select a single channel.
{% endalert %}

![]({% image_buster /assets/img_archive/conversions2_funnel.png %}){: style="max-width:70%"}

### Conversions over time

This time series graph includes a representation of the conversions per campaign or Canvas over time.By default, all selected campaigns and Canvases are shown.To deselect a campaign or Canvas, click on the name of the campaign or Canvas that you'd like to exclude.

To download the time series data, click <i class="fas fa-bars"></i> and select your download option.Available options are PNG, JPEG, PDF, SVG, or CSV.

![]({% image_buster /assets/img_archive/conversions2_over_time.png %}){: style="max-width:70%"}

### アトリビューション方法

| アトリビューション方法 | 定義 | レート計算 | チャネル固有のオプション |
| --- | --- | --- | --- |
| 受領時 | メッセージ受信後に発生した変換の総数 | （ユニーク受信コンバージョン）/（ユニーク受信者）として計算されます | {::nomarkdown}<ul><li>メール配信時</li><li>SMS 配信時</li></ul>{:/} |
| 送信時 | メッセージ送信後に発生した変換の総数 | (一意の送信コンバージョン) / (一意の受信者)として計算されます | {::nomarkdown}<ul><li>プッシュ通知送信時</li><li>Upon Content Card send</li><li>SMS 送信時</li></ul>{:/} |
| 開封時 | メッセージ開封後に発生した変換の総数 | (ユニーク開封コンバージョン) / (ユニーク受信者)として計算されます | {::nomarkdown}<ul><li>メール開封時</li><li>プッシュオープン時</li></ul>{:/} |
| クリック時 | クリックメッセージが発生した変換の総数 | (ユニーククリックコンバージョン) / (ユニーク受信者) として計算されます | {::nomarkdown}<ul><li>メールのクリック時</li><li>Upon Content Card click</li><li>IAM のクリック時</li></ul>{:/} |
| インプレッション時に | インプレッション後に発生した総コンバージョン数 | （ユニークインプレッションコンバージョン） / （ユニーク受信者）として計算されます | {::nomarkdown}<ul><li>IAM のインプレッション時</li><li>コンテンツカードのインプレッション時</li></ul>{:/} |
| 最終タッチ時 | コンバージョンウィンドウ中に最後にタッチまたはクリックされたメッセージにすべてのクレジットを与えるコンバージョン。 | (タッチ数) / (ユニーク受信者数) として計算されます | 最後のタッチアトリビューションは、複数のチャネルがレポートに追加された場合に自動的に選択されます。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## 知っておくべき用語

| 用語 | 定義 |
| --- | --- |
| タッチ | メッセージとの物理的な相互作用またはタッチポイント。<br><br>タッチには次のものが含まれます。<br>{::nomarkdown}<ul><li>メール クリック</li><li>プッシュオープン</li><li>Content Card Click</li><li>In-App Message Click</li><li>SMS 配信</li></ul>{:/} |
