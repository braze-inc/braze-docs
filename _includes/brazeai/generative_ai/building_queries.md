> Learn how to use the Query Builder, so you can generate reports using Braze data in Snowflake. The Query Builder comes with pre-built SQL [query templates]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/) to get you started, or you can write your own custom SQL queries to unlock even more insights.

## Prerequisites

You'll need ["View PII" permissions]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) to use Query Builder, since it allows direct access to some customer data.

## Using the Query Builder

### Step 1: Create an SQL query

To create a new query, go to **Analytics** > **Query Builder**, then select **Create SQL Query**.

![The "Query Template" and "SQL Editor" options found within the "Create SQL Query" dropdown.]({% image_buster /assets/img_archive/create_sql_query_button.png %}){: style="max-width:60%;"}

If you need inspiration or help in crafting your query, choose **Query Template** and select a [pre-made template]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/). To start with a blank query, select **SQL Editor**.

Your report is automatically given a name with the current date and time. Hover over the name and select <i class="fas fa-pencil" alt="Edit"></i> to give your SQL query a meaningful name.

![An example report name "Channel engagement for May 2025".]({% image_buster /assets/img_archive/report_name_example.png %}){: style="max-width:80%;"}

### Step 2: Build your query

When building your query, you can choose to get help from AI or build it on your own.

{% tabs local %}
{% tab Using BrazeAI %}
The AI Query Builder leverages [GPT](https://openai.com/gpt-4), powered by OpenAI, to recommend SQL for your query. To generate SQL with the AI Query Builder:

1. After creating a report in the Query Builder, select the **AI Query Builder** tab.
2. Type in your prompt or select a sample prompt and select **Generate** to translate your prompt into SQL.
3. Review the generated SQL to make sure it looks correct, and then select **Insert into Editor**.

![The SQL AI query builder.]({% image_buster /assets/img_archive/query_builder_ai_tab.png %}){: style="max-width:60%;" }

#### Tips

- Familiarize yourself with the available [Snowflake data tables]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/). Asking for data that doesn't exist in these tables may result in ChatGPT making up a fake table.
- Familiarize yourself with the [SQL writing rules]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/#custom-sql) for this feature. Not following these rules will cause an error.
- You can send up to 20 prompts per minute with the AI Query Builder.

##{% multi_lang_include brazeai/generative_ai/policy.md %}
{% endtab %}

{% tab On My Own %}
Write your SQL query using [Snowflake syntax](https://docs.snowflake.com/en/sql-reference). Consult the [table reference]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) for a full list of tables and columns available to be queried.

To view table details within the Query Builder:

1. From the **Query Builder** page, open the **Reference** panel and select **Available Data Tables** to view available data tables and their names.
3. Select <i class="fas fa-chevron-down" alt=""></i> **See Details** to view the table description and information about the table columns, such as data types.
4. To insert the table name in your SQL, select <i class="fas fa-copy" title="Copy table name to SQL editor"></i>.

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

If you query for the `CANVAS_ID`, `CANVAS_VARIATION_API_ID`, or `CAMPAIGN_ID`, their associated name columns will automatically be included in the results table. You don’t need to include them in the `SELECT` query itself.

| ID name | Associated name column |
| --- | --- |
| `CANVAS_ID` | Canvas Name |
| `CANVAS_VARIATION_API_ID` | Canvas Variant Name |
| `CAMPAIGN_ID` | Campaign Name |
{: .reset-td-br-1 .reset-td-br-2 }

This query retrieves all three IDs and their associated name columns with a maximum of 100 rows:

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED 
LIMIT 100
```

#### Troubleshooting

Your query may fail for any of the following reasons:

- Syntax errors in your SQL query
- Processing timeout (after 6 minutes)
    - Reports that take longer than 6 minutes to run will time out.
    - If a report times out, try to limit the time range in which you are querying data or query a more specific set of data.
{% endtab %}
{% endtabs %}

### Step 3: Generate your report

When you're finished building your query, select **Run Query**. If there's no errors or [report timeouts](#report-timeouts), a CSV file will be generated from the query.

To download the CSV report, select **Export**.

![Query Builder showing the results for the templated query "Channel engagement and revenue for the last 30 days".]({% image_buster /assets/img_archive/query_builder.png %})

{% alert important %}
Each report can only generate results once per day. If you run the same report multiple times in a single calendar day, you'll see the same results in each report.
{% endalert %}

## Report timeouts

Reports that take longer than six minutes to run will time out. If this is the first query you're running in some time, it may take longer to process and therefore has a higher likelihood of timing out. If this happens, try running the report again.

If your report continues to time out after multiple attempts, [contact Support]({{site.baseurl}}/help/support#braze-support).

## Data and results

All queries surface data from the last 60 days. When you export your results, it will only contain up to 1,000 rows. For reports that require larger amounts of data, you can use tools such as [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) or the [export API endpoint]({{site.baseurl}}/api/endpoints/export).

## Snowflake credits

Each company has 5 Snowflake credits available per month, shared across all workspaces. A small portion of a Snowflake credit is used whenever you run a query or preview a table.

{% alert note %}
Snowflake credits are not shared between features. For example, credits across SQL Segment Extensions and Query Builder are independent of each other.
{% endalert %}

Credit usage is correlated to the run time of your SQL query. The longer the run time is, the higher the portion of a Snowflake credit a query will cost. Run time can vary depending on the complexity and size of your queries over time. The more complex and frequent queries you run, the larger your resource allocation and the faster your run time becomes.

Credits are not used when writing, editing, or saving reports within the Braze SQL editor. Your credits will reset to 5 on the first of each month at 12 am UTC. You can monitor your monthly credit usage at the top of the Query Builder page.

![Query Builder showing the amount of credits used in the current month.]({% image_buster /assets/img_archive/query_builder_credits.png %}){: style="max-width:60%;"}

When you reach the credit cap, you cannot run queries, but you can create, edit, and save SQL reports. If you want to purchase more Query Builder credits, please get in touch with your account manager.
