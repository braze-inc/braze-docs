---
nav_title: Query Builder
article_title: Query Builder
page_order: 100
page_type: reference
description: "This reference article describes how to build reports using Braze data from Snowflake in the Query Builder."
tool: Reports
---

# Query Builder

> With the Query Builder, you can generate reports using Braze data in Snowflake. The Query Builder comes with pre-built SQL [query templates](#query-templates) to get you started, or you can write your own custom SQL queries to unlock even more insights.

## Who has access

Because this feature allows direct access to some customer data, you can only access the Query Builder if you have "View PII" [permission]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/).

## Running reports in the Query Builder

To run a report:

1. Go to **Analytics** > **Query Builder**.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can find **Query Builder** under **Data**.
{% endalert %}

{:start="2"}
2. Click **Create New SQL Report**.
3. Your report is automatically given a name with the current date and time. Hover over the name and click <i class="fas fa-pencil" alt="Edit"></i> to give your SQL query a meaningful name.
4. Write your SQL query in the editor or select a [query template](#query-templates) from the **Query Templates** tab. If you choose to write your own SQL, see [custom SQL](#custom-sql) for requirements and resources.
5. Click **Run Query**.
6. Save your query.
7. To download a CSV of your report, click **Export**.

![Query Builder showing the results for the templated query "Channel engagement and revenue for the last 60 days".]({% image_buster /assets/img_archive/query_builder.png %})

Results from each report can be generated once a day. If you run the same report more than once in one calendar day, you'll see the same results in both reports.

### Report timeout

Reports that take longer than 6 minutes to run will time out. If this is the first query you're running in some time, it may take longer to process and therefore has a higher likelishood of timing out. If this happens, try running the report again.

If a report times out or runs into errors even after retrying, please contact support.

## Query templates

All templates surface data from the last 60 days. You can access query templates from **Reference** > **Query Templates**.

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
| Email bounces per domain | Number of bounces per email domain | | ![]({% image_buster /assets/img_archive/query_builder_q4.png %}) |
| Email performance by country | For each country, you'll see the following metrics: sends, indirect open rate, and direct open rate. Country is the country of the user at the time of push send. | | ![]({% image_buster /assets/img_archive/query_builder_q3.png %}) |
| Email subscription group opt-ins and opt-outs | For each week, you'll see the number of unique user opt-ins and opt-outs of any email subscription groups. | | ![]({% image_buster /assets/img_archive/query_builder_q2.png %}) |
| Email URLs clicked | This report shows the number of clicks each link in an email had. To run this report, you'll need to specify the API identifier for a campaign or Canvas. You can find a campaign's API identifier at the bottom of that campaign's details page, and you can find the Canvas API identifier under **Analyze Variants**. <br><br>For each de-personalized link, you'll see a count of clicks. Your CSV download will include the user IDs of all users that clicked, the link they clicked on, and a timestamp of when they clicked. | **De-personalized URLs:** URLs that are stripped of any Liquid tags | ![]({% image_buster /assets/img_archive/query_builder_q5.png %}) |
| Revenue by country | This report provides revenue per country for a specific campaign/Canvas. To run this report, you'll need to specify the API identifier for a campaign or Canvas. You can find a campaign's API identifier at the bottom of that campaign's details page, and you can find the Canvas API identifier under **Analyze Variants**.<br><br>For each country, you'll see the amount of revenue generated, number of orders, number of returns, net revenue, and gross revenue. | {::nomarkdown} <ul> <li> <b>Number of orders:</b> number of purchase events </li> <li> <b>Number of returns:</b> number of purchase events with negative revenue values </li> <li> <b>Net revenue:</b> revenue of all non-returns </li> <li> <b>Gross revenue:</b> revenue that includes the value of returns </li> </ul> {:/} | ![]({% image_buster /assets/img_archive/query_builder_q6.png %}) |
| Push performance by country | For each country, you'll see the following metrics: deliveries, open rate, and click rate. Country is the country of the user at the time of email send. | | ![]({% image_buster /assets/img_archive/query_builder_q7.png %}) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Custom SQL

Your SQL query should be written using [Snowflake syntax](https://docs.snowflake.com/en/sql-reference). Consult the [table reference]({{site.baseurl}}/sql_segments_tables/) for a full list of tables and columns available to be queried.

To view table details within the Query Builder:

1. From the **Query Builder** page, open the **Reference** panel and select **Available Data Tables** to view available data tables and their names.
3. Click <i class="fas fa-chevron-down" alt=""></i> **See Details** to view the table description and information about the table columns, such as data types.
4. To insert the table name in your SQL, click <i class="fas fa-copy" title="Copy table name to SQL editor"></i>.

To view pre-written queries provided by Braze:

1. Select the **Query Templates** tab.
2. Select the report you’d like to run.
3. Click **Run Query** to view results.

Restricting your query to a specific time period will help you generate results quicker. The following is an example query that gets the number of purchases and the revenue generated for the last hour.

```sql
SELECT COUNT(*) as Purchases, SUM(price) as Revenue
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('hour', -1, date_trunc('day',CURRENT_DATE()));
```

This query retrieves the number of email sends in the last month:

```sql
SELECT COUNT(*) as Sends
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('month', -1, date_trunc('day',CURRENT_DATE()));
```

### Troubleshooting

Your query may fail for any of the following reasons:

- Syntax errors in your SQL query
- Processing timeout (after 6 minutes)
    - Reports that take longer than 6 minutes to run will time out.
    - If a report times out, try to limit the time range in which you are querying data or query a more specific set of data.

## Data and results

Results, and exports of results, are tables that can contain up to 1,000 rows. For reports that require larger amounts of data, use another tool such as [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents) or Braze’s [export APIs]({{site.baseurl}}/api/endpoints/export).

## Monitoring your Query Builder usage

Each Braze workspace has 2,000 Query Builder credits available per month. Credits are used whenever you run a query or preview a table. Credit usage corresponds to the run time of your queries. 

Credit usage is correlated to the run time of your SQL query. The longer the run time is, the more credits a query will cost. Run time can vary depending on the complexity and size of your queries over time. The more complex and frequent queries you run, the larger your resource allocation and the faster your run time becomes.

{% alert note %}
The ability to track credit usage for each query is coming soon.
{% endalert %}

Credits are not used when writing, editing, or saving reports within the Braze SQL editor. Your credits will reset to 2,000 on the first of each month at 12 am UTC. You can monitor your monthly credit usage at the top of the Query Builder page.

![Query Builder showing the amount of credits used in the current month.]({% image_buster /assets/img_archive/query_builder_credits.png %}){: style="max-width:60%"}

When you reach the credit cap, you cannot run queries, but you can create, edit, and save SQL reports. If you want to purchase more Query Builder credits, please get in touch with your account manager.