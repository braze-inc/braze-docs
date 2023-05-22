---
nav_title: Conversions Dashboard
article_title: Conversions Dashboard
page_order: 3
page_type: reference
description: "This reference article covers the Conversions Dashboard, which allows you to analyze conversions across campaigns, Canvases, and channels using different attribution methods."
tool: 
  - Reports

---

# Conversions dashboard

> The conversions dashboard allows you to analyze conversions across campaigns, Canvases, and channels, using different attribution methods.

You can specifically track these attribution methods:
- **Open conversions:** Conversions that occurred after a user opened the message
- **Click conversions:** Conversions that occurred after a user clicked the message
- **Received conversions:** Conversions that occurred after a user receved the message
- **Last-click conversions:** Conversions that occurred after a user clicked the message if the message was the most recent one the user clicked (This feature is currently being tested on a small subset of early access customers)

When measuring your conversions, you can specify the time frame, conversion event, and conversion window.

{% alert important %}
This feature is in early access and is under active development. If you're interested in participating in the early access, please reach out to your customer success manager.
{% endalert %}

## Setting up your report

{% alert note %}
If you are using our [updated navigation]({{site.baseurl}}/navigation), you can find **Conversions** under **Analytics** > **Analytics Dashboards** > **Conversions**.
{% endalert %}

1. Navigate to the **Conversions** page, under **Data**.
2. Select a time period for your report, up to 365 days in the past.
3. Select a conversion event, **Started session**, **Performed custom event**, or **Made a specific purchase**.
4. Decide if you want your report to include [untracked events](#untracked-events) (Optional, this feature is currently being tested on a small subset of early access customers).
5. Select a conversion window, up to 7 days. This is how much time users have after they perform the message engagement action for the conversion event to count as a conversion. Conversion events that occur outside of this window are not counted in your report.
6. Click **Refresh**.

### Untracked events

Untracked events are events that were not originally assigned as conversion events for the campaigns and Canvases in your report. If unselected, then your report will only include conversion metrics for events that were originally included as conversion events, and any other occurences of that event during the time frame are not counted in your report.

For example, let's say you're running your report on campaign A (see the next section, [Filtering your report](#filtering-your-report), for how to filter reports to a specific campaign). You're interested in seeing the conversion rate for users who received campaign A and performed custom event X, but custom event X was not one of the four conversion events tracked for this campaign. If you choose to not include untracked events, then your report will show 0 conversions. However, if you do include untracked events, then Braze will generate a report of users who performed custom event X after receiving, opening, or clicking campaign A.

### Filtering your report

You can filter by campaign, Canvas step, or channel to narrow down your report's results. You must select a channel to run the report.

- **Filter by campaign:** Select up to 10 campaigns to show conversions that occurred after receiving, opening, or clicking any of the selected campaigns.
- **Filter by Canvas step:** Select up to 10 Canvases or 10 Canvas steps to show conversiosn that occurred after receiving, opening, or clicking any of the selected Canvases or steps.
- **Filter by channel:** Select one channel (required) to show conversions that occurred after receiving, opening, or clicking any messages sent from that channel. By default, the email channel is selected.
- **Filter by country:** Select up to 10 countries to show conversions for users with those countries in their profile.

## Understanding your results

Your report is split into three sections: **Total conversions**, **Unique conversions**, and **Conversion performance by channel**.

### Total conversions

The total conversions are total counts and are not de-duplicated when users convert multiple times. For example, if a user converts two times within the conversion window, then two additional total conversions are incremented.

This section includes the following metric tiles:

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
.leftHeader{font-size: 12px; font-weight: bold; background-color: #f4f4f7; text-transform: uppercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky">Number of conversions</th>
    <th class="tg-0pky">Total conversions per user</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="leftHeader">Received conversions</td>
    <td class="tg-0pky">The number of times your selected conversion event occurred after message receipt, within the selected conversion window.</td>
    <td class="tg-0pky">Calculated as (Number of total conversions from time period) / (Number of unique recipients from time period)</td>
  </tr>
  <tr>
    <td class="leftHeader">Open conversions</td>
    <td class="tg-0pky">The number of times your selected conversion event occurred after message open, within the selected conversion window.</td>
    <td class="tg-0pky">Calculated as (Number of conversions from time period) / (Number of unique recipients from time period)</td>
  </tr>
  <tr>
    <td class="leftHeader">Click conversions</td>
    <td class="tg-0pky">The number of times your selected conversion event occurred after message click, within the selected conversion window.</td>
    <td class="tg-0pky">Calculated as (Number of conversions from time period) / (Number of unique recipients from time period)</td>
  </tr>
</tbody>
</table>

### Unique conversions

The unique conversions rates and counts track the number of users who converted one or more times. This section includes the following metrics.

| Metric | Calculation |
| --- | --- | ---- |
| Unique received conversions rate | (Number of users that converted at least once after message receipt, within selected conversion window) / (Number of unique recipients) |
| Unique open conversions rate | (Number of users that converted at least once after message open, within selected conversion window) / (Number of unique recipients) |
| Unique click conversions rate | (Number of users that converted at least once after message click, within selected conversion window) / (Number of unique recipients) |
| Last click conversions rate (This feature is currently being tested on a small subset of early access customers) | (Number of users that converted at least once if their most recent click within the conversion window was for this message) / (Number of unique recipients)
{: .reset-td-br-1 .reset-td-br-2}

### Conversion performance by channel

This section shows the conversion results for each messaging channel. Due to how opens and clicks are tracked across channels, not all metrics are available for all channels. 

{% alert note %}
Receipt events vary from channel to channel, therefore the _unique recipients_ metric used in the denominator of total and unique conversion calculations will alter slightly from channel to channel. For example, in-app messages track impressions rather than receipts. That means for the in-app message channel, the calculations for _Total conversions_ and _Unique conversions_ use the number of impressions in the denominator.
{% endalert %}

The following table lists how each attribution method is tracked for each channel.

<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky">Receipt Conversions</th>
    <th class="tg-0pky">Open Conversions</th>
    <th class="tg-0pky">Click Conversions</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="leftHeader">Email</td>
    <td class="tg-0pky">Email receipts</td>
    <td class="tg-0pky">Email opens</td>
    <td class="tg-0pky">Email clicks</td>
  </tr>
  <tr>
    <td class="leftHeader">SMS</td>
    <td class="tg-0pky">SMS sends</td>
    <td class="tg-0pky">N/A</td>
    <td class="tg-0pky">N/A</td>
  </tr>
  <tr>
    <td class="leftHeader">Push</td>
    <td class="tg-0pky">Push sends</td>
    <td class="tg-0pky">Push influenced opens</td>
    <td class="tg-0pky">Push direct opens</td>
  </tr>
  <tr>
    <td class="leftHeader">In-app message</td>
    <td class="tg-0pky">In-app message impressions</td>
    <td class="tg-0pky">N/A</td>
    <td class="tg-0pky">In-app message clicks</td>
  </tr>
  <tr>
    <td class="leftHeader">Content Card</td>
    <td class="tg-0pky">Content Card impressions</td>
    <td class="tg-0pky">N/A</td>
    <td class="tg-0pky">Content Card clicks</td>
  </tr>
</tbody>
</table>
