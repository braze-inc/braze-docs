---
nav_title: Query Builder
article_title: Query Builder
page_order: 100
page_type: reference
description: "This reference article describes how to build reports using Braze data from Snowflake in the Query Builder."
tool: Reports
---

# Query builder

With the query builder, you can generate reports using Braze data in Snowflake. The query builder comes with pre-built SQL [query templates](#query-templates) to get you started. Currently only the templated queries are allowed, support for custom SQL queries will follow.

{% alert important %}
The query builder is in early access. If you'd like to participate in the early access, reach out to your customer success manager.
{% endalert %}

## Running reports in the query builder

To run a report:

1. Go to **Query Builder**, under **Data**.
2. Select the report you'd like to run.
3. Click **Run Report**.
4. To download a CSV of your report, click **Export**.

![Query builder showing the results for the templated query "Channel engagement and revenue for the last 30 days".]({% image_buster /assets/img_archive/query_builder.png %})

Results from each report can be generated once a day. If you run the same report more than once in one calendar day, you'll see the same results in both reports.

### Report timeout

Reports that take longer than 6 minutes to run will time out. If this is the first query you're running in some time, it may take longer to process and therefore has a higher likelishood of timing out. If this happens, try running the report again.

If a report times out or runs into errors even after retrying, please contact support.

## Query templates

All templates surface data from the last 30 days.

<style>
table th:nth-child(1) {
    width: 10%;
}
table th:nth-child(2) {
    width: 25%;
}
table th:nth-child(3) {
    width: 20%;
}
table th:nth-child(4) {
    width: 45%;
}
table td {
    word-break: break-word;
}
</style>


| Query name | Description | Metrics | Preview |
| --- | --- | --- | --- |
| Channel engagement and revenue | For each channel, you'll see all engagement metrics for that channel (opens, clicks, etc), revenue, number of transactions, and average price. | {::nomarkdown} <ul> <li> <b>Number of transactions:</b> number of purchase events </li> <li> <b>Average price:</b> revenue divided by transactions </li> </ul> {:/} | ![]({% image_buster /assets/img_archive/query_builder_q1.png %}) |
| Email bounces per domain | Number of bounces per email domain | | ![]({% image_buster /assets/img_archive/query_builder_q2.png %}) |
| Email performance by country | For each country, you'll see the following metrics: sends, indirect open rate, and direct open rate. Country is the country of the user at the time of push send. | | ![]({% image_buster /assets/img_archive/query_builder_q3.png %}) |
| Email subscription group opt-ins and opt-outs | For each week, you'll see the number of unique user opt-ins and opt-outs of any email subscription groups. | | ![]({% image_buster /assets/img_archive/query_builder_q4.png %}) |
| Email URLs clicked | This report shows the number of clicks each link in an email had. To run this report, you'll need to specify the API identifier for a campaign or Canvas. You can find a campaign's API identifier at the bottom of that campaign's details page, and you can find the Canvas API identifier under **Analyze Variants**. <br><br>For each de-personalized link, you'll see a count of clicks. Your CSV download will include the user IDs of all users that clicked, the link they clicked on, and a timestamp of when they clicked. | **De-personalized URLs:** URLs that are stripped of any Liquid tags | ![]({% image_buster /assets/img_archive/query_builder_q5.png %}) |
| Revenue by country | This report provides revenue per country for a specific campaign/Canvas. To run this report, you'll need to specify the API identifier for a campaign or Canvas. You can find a campaign's API identifier at the bottom of that campaign's details page, and you can find the Canvas API identifier under **Analyze Variants**.<br><br>For each country, you'll see the amount of revenue generated, number of orders, number of returns, net revenue, and gross revenue. | {::nomarkdown} <ul> <li> <b>Number of orders:</b> number of purchase events </li> <li> <b>Number of returns:</b> number of purchase events with negative revenue values </li> <li> <b>Net revenue:</b> revenue of all non-returns </li> <li> <b>Gross revenue:</b> revenue that includes the value of returns </li> </ul> {:/} | ![]({% image_buster /assets/img_archive/query_builder_q6.png %}) |
| Push performance by country | For each country, you'll see the following metrics: deliveries, open rate, and click rate. Country is the country of the user at the time of email send. | | ![]({% image_buster /assets/img_archive/query_builder_q7.png %}) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}