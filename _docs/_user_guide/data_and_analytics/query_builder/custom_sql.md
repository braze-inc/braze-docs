---
nav_title: Custom SQL in Query Builder
article_title: Custom SQL in Query Builder
page_order: 1
page_type: reference
description: "This reference article describes how to use custom SQL to unlock new insights in the query builder."
tool: Reports
---

# Custom SQL in query builder

With the query builder, you can generate reports using Braze data in Snowflake, now using custom SQL to unlock new insights.

{% alert important %}
The SQL editor is in early access. If you're interested in participating in the early access, reach out to your customer success manager.
{% endalert %}

## Creating custom SQL reports

To run a report:

1. Go to **Query Builder**, under **Data**.
2. Click **Create New SQL Report**.
3. Your report is automatically given a name with the current date and time. Hover over the name and click <i class="fas fa-pencil" alt="Edit"></i> to give your SQL query a meaningful name.
4. Write your SQL query in the editor. See [Writing SQL](#writing-sql) for requirements and resources.
5. Click **Run Query**.
6. Save your query.
7. To download a CSV of your report, click **Export**.

## Data and results

Results, and exports of results, are tables that can contain up to 500 rows. For reports that require larger amounts of data, use another tool such as [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents) or Braze’s [export APIs]({{site.baseurl}}/api/endpoints/export).

## Writing SQL

Your SQL query should be written using [Snowflake syntax](https://docs.snowflake.com/en/sql-reference). Consult the [table reference]({{site.baseurl}}/sql_segments_tables/) for a full list of tables and columns available to be queried.

To view table details within the query builder:

1. From the **Query Builder** page, select the **Available Data Tables** tab to view available data tables and their names.
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

## Troubleshooting

Your query may fail for any of the following reasons:

- Syntax errors in your SQL query
- Processing timeout (after 6 minutes)
    - Reports that take longer than 6 minutes to run will time out.
    - If a report times out, try to limit the time range in which you are querying data or query a more specific set of data.