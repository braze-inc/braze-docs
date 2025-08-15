---
nav_title: Query builder
article_title: Query Builder
page_order: 15
description: "This reference article describes how to build reports using Braze data from Snowflake in the Query Builder."
tool: Reports
alias: /query_builder/
---

# Query Builder

> The Query Builder generates reports using Braze data in Snowflake. The Query Builder comes with pre-built SQL [query templates]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/) to get you started, or you can write your own custom SQL queries to unlock even more insights.

Because the Query Builder allows direct access to some customer data, you can only access the Query Builder if you have the "View PII" [permission]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/).

## Running reports in the Query Builder

To run a Query Builder report:

1. Go to **Analytics** > **Query Builder**.
2. Select **Create SQL Query**. If you need inspiration or help in crafting your query, select **Query Template** and choose a template from the list. Otherwise, select **SQL Editor** to head straight to the editor.
3. Your report is automatically given a name with the current date and time. Hover over the name and select <i class="fas fa-pencil" alt="Edit"></i> to give your SQL query a meaningful name.
4. Write your SQL query in the editor or [get help from AI](#ai-query-builder) from the **AI Query Builder** tab. If writing your own SQL, see [Writing custom SQL queries](#custom-sql) for requirements and resources.
5. Select **Run Query**.
6. Save your query.
7. To download a CSV of your report, select **Export**.

![Query Builder showing the results for the templated query "Channel engagement and revenue for the last 30 days".]({% image_buster /assets/img_archive/query_builder.png %})

Results from each report can be generated once a day. If you run the same report more than once in one calendar day, you'll see the same results in both reports.

### Query templates

Access query templates by selecting **Create SQL Query** > **Query Template** when first creating a report.

See [Query templates]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/) for a list of available templates.

### Data timeframe

All queries surface data from the last 60 days.

### Query Builder time zone

The default time zone for querying our Snowflake database is UTC. As a result, there may be some data discrepancies between your **Email Channel Engagement** page (which follows your company's time zone) and your Query Builder results.

To convert the time zone in your query results, add the following SQL to your query and customize it for your company's time zone:

{% raw %}
```sql
SELECT
DATE_TRUNC(
'day',
CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME))
) AS send_date_sydney,
COUNT(ID) AS emails_sent
USERS_MESSAGES_EMAIL_SEND_SHARED
WHERE
-- Apply the date range in Sydney time as well
CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME)) >= '2025-03-25 00:00:00'
AND CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME)) < '2025-03-29 00:00:00'
AND APP_GROUP_ID = 'your app group ID'
GROUP BY
send_date_sydney
ORDER BY
send_date_sydney;
```
{% endraw %}

## Generating SQL with the AI Query Builder

The AI Query Builder leverages [GPT](https://openai.com/gpt-4), powered by OpenAI, to recommend SQL for your query.

![The SQL AI query builder.]({% image_buster /assets/img_archive/query_builder_ai_tab.png %}){: style="max-width:60%;" }

To generate SQL with the AI Query Builder:

1. After creating a report in the Query Builder, select the **AI Query Builder** tab.
2. Type in your prompt or select a sample prompt and select **Generate** to translate your prompt into SQL.
3. Review the generated SQL to make sure it looks correct, and then select **Insert into Editor**.

### Tips

- Familiarize yourself with the available [Snowflake data tables]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/). Asking for data that doesn't exist in these tables may result in ChatGPT making up a fake table.
- Familiarize yourself with the [SQL writing rules]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/#custom-sql) for this feature. Not following these rules will cause an error.
- You can send up to 20 prompts per minute with the AI Query Builder.

### How is my data used and sent to OpenAI?
<!-- Contact Legal for changes. -->

In order to generate your SQL, Braze will send your prompts to OpenAI’s API Platform. All queries sent to OpenAI from Braze are anonymized, meaning that OpenAI will not be able to identify from whom the query was sent unless you include uniquely identifiable information in the content you provide. As detailed in [OpenAI’s API Platform Commitments](https://openai.com/policies/api-data-usage-policies), data sent to OpenAI’s API via Braze is not used to train or improve their models and will be deleted after 30 days. Please ensure that you adhere to OpenAI’s policies relevant to you, including the [Usage Policy](https://openai.com/policies/usage-policies). Braze makes no warranty of any kind with respect to any AI-generated content. 

## Writing custom SQL queries {#custom-sql}

Write your SQL query using [Snowflake syntax](https://docs.snowflake.com/en/sql-reference). Consult the [table reference]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) for a full list of tables and columns available to be queried.

To view table details within the Query Builder:

1. From the **Query Builder** page, open the **Reference** panel and select **Available Data Tables** to view available data tables and their names.
3. Select <i class="fas fa-chevron-down" alt=""></i> **See Details** to view the table description and information about the table columns, such as data types.
4. To insert the table name in your SQL, select <i class="fas fa-copy" title="Copy table name to SQL editor"></i>.

To use pre-written queries provided by Braze, select **Query Template** when first creating a report in the Query Builder.

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

### Automatically populate the campaign variant name

If you want the campaign variant name to automatically populate, include the column name `MESSAGE_VARIATION_API_ID` in your query, such as in this example:

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID, MESSAGE_VARIATION_API_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED 
LIMIT 100
```

### Troubleshooting

Your query may fail for any of the following reasons:

- Syntax errors in your SQL query
- Processing timeout (after 6 minutes)
    - Reports that take longer than 6 minutes to run will time out.
    - If a report times out, try to limit the time range in which you are querying data or query a more specific set of data.

## Using variables

Use variables to use predefined variable types in SQL to reference values without needing to manually copy the value. For example, instead of manually copying a campaign's ID to the SQL editor, you can use {% raw %}`{{campaign.${My campaign}}}`{% endraw %} to directly select a campaign from a dropdown in the **Variables** tab.

After a variable is created, it will appear in the **Variables** tab of your Query Builder report. Benefits of using SQL variables include:

- Save time by creating a campaign variable to select from a list when creating your report, instead of pasting in campaign IDs.
- Swap in values by adding variables that allow you to reuse the report for slightly different use cases in the future (such as a different custom event).
- Reduce user error when editing your SQL by reducing the amount of editing needed for each report. Teammates that are more comfortable with SQL can create reports that less technical teammates can then use.

### Guidelines

Variables must adhere to the following Liquid syntax: {% raw %}`{{ type.${name}}}`{% endraw %}, where `type` must be one of the accepted types and `name` can be anything you choose. The labels for these variables default to the variable name.

By default, all variables are mandatory (and your report will not run unless variable values are selected) except for the date range, which defaults to the past 30 days when the value isn’t provided.

### Variable types

The following variable types are accepted:

- [Number](#number)
- [Date range](#date-range)
- [Messaging](#messaging)
- [Products](#products)
- [Custom events](#custom-events)
- [Custom events properties](#custom-event-properties)
- [Workspace](#workspace)
- [Catalogs](#catalogs)
- [Catalog fields](#catalog-fields)
- [Options](#options)
- [Segments](#segments)
- [String](#string)
- [Tags](#tags)

#### Number

- **Replacement value:** The provided value, such as `5.5`
- **Usage example:** {% raw %}`some_number_column < {{number.${some name}}}`{% endraw %}

#### Date range

If using both `start_date` and `end_date`, they must have the same name so you can use them as a date range.

##### Example values

The date range type can be relative, start date, end date, or date range.

All four types are shown if both `start_date` and `end_date` are used with the same name. If only one is used, then only the relevant types will show.

| Date range type | Description | Required values |
| --- | --- | --- |
| Relative | Specifies the past X days | Requires `start_date` |
| Start date | Specifies a start date | Requires `start_date` |
| End date | Specifies an end date | Requires `end_date` |
| Date range | Specifies both a start and end date | Requires both `start_date` and `end_date` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

- **Replacement value:** Replaces `start_date` and `end_date` with a Unix timestamp in seconds for a specified date in UTC, such as `1696517353`.
- **Usage example:** For all of relative, start date, end date, and date range variables:
    - {% raw %}`time > {{start_date.${some name}}} AND time < {{end_date.${some name}}}` {% endraw %}
        - You can use either `start_date` or `end_date` if you don’t want a date range.

#### Messaging

All messaging variables must share the same identifier when you want to tie together their state in one group.

##### Canvas

For selecting one Canvas. Sharing the same name with a campaign will result in a radio button within the **Variables** tab that for selecting either Canvas or campaign.

- **Replacement value:** Canvas BSON ID
- **Usage example:** {% raw %}`canvas_id = ‘{{canvas.${some name}}}’`{% endraw %}

##### Canvases

For selecting multiple Canvases. Sharing the same name with a campaign will result in a radio button within the **Variables** tab for selecting either Canvas or campaign.

- **Replacement value:** Canvases BSON IDs
- **Usage example:** {% raw %}`canvas_id IN ({{canvases.${some name}}})`{% endraw %}

##### Campaign

For selecting one campaign. Sharing the same name with a Canvas will result in a radio button within the **Variables** tab that for selecting either Canvas or campaign.

- **Replacement value:** Campaign BSON ID
- **Usage example:** {% raw %}`campaign_id = ‘{{campaign.${some name}}}’`{% endraw %}

##### Campaigns

For multi-selecting campaigns. Sharing the same name with a Canvas will result in a radio button within the **Variables** tab for selecting either Canvas or campaign.

- **Replacement value:** Campaigns BSON IDs
- **Usage example:** {% raw %}`campaign_id IN ({{campaigns.${some name}}})`{% endraw %}

##### Campaign variants

For selecting campaign variants that belong to the selected campaign. It must be used in conjunction with a campaign or campaigns variable.

- **Replacement value:** Campaign variants API IDs, strings delimited by commas such as `api-id1, api-id2`.
- **Usage example:** {% raw %}`message_variation_api_id IN ({{campaign_variants.${some name}}})`{% endraw %}

##### Canvas variants

For selecting Canvas variants that belong to a chosen Canvas. It must be used with a Canvas or Canvases variable.

- **Replacement value:** Canvas variants API IDs, strings delimited by commas such as in `api-id1, api-id2`.
- **Usage example:** {% raw %}`canvas_variation_api_id IN ({{canvas_variants.${some name}}})`{% endraw %}

##### Canvas step

For selecting a Canvas step that belongs to a chosen Canvas. It must be used with a Canvas variable.

- **Replacement value:** Canvas step API ID
- **Usage example:** {% raw %}`canvas_step_api_id = ‘{{canvas_step.${some name}}}’`{% endraw %}

##### Canvas steps

For selecting Canvas steps that belong to chosen Canvases. It must be used with a Canvas or Canvases variable.

- **Replacement value:** Canvas steps API IDs
- **Usage example:** {% raw %}`canvas_step_api_id IN ({{canvas_steps.${some name}}})`{% endraw %}
