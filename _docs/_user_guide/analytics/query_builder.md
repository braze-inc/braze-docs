---
nav_title: Query Builder
article_title: Query Builder
page_order: 15
page_type: reference
description: "This reference article describes how to build reports using Braze data from Snowflake in the Query Builder."
tool: Reports
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

## Generating SQL with the AI Query Builder

The AI Query Builder leverages [GPT](https://openai.com/gpt-4), powered by OpenAI, to recommend SQL for your query.

![][2]{: style="max-width:60%;" }

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

### Troubleshooting

Your query may fail for any of the following reasons:

- Syntax errors in your SQL query
- Processing timeout (after 6 minutes)
    - Reports that take longer than 6 minutes to run will time out.
    - If a report times out, try to limit the time range in which you are querying data or query a more specific set of data.

## Using variables

Use variables to use predefined variable types in SQL to reference values without needing to manually copy the value. For example, instead of manually copying a campaign's ID to the SQL editor, you can use {% raw %}`{{campaign.${My campaign}}}`{% endraw %} to directly select a campaign from a dropdown in the **Variables** tab.

![][3]

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

![][4]{: style="max-width:50%;"}

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

![][5]{: style="max-width:50%;"}

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

##### Canvas Step

For selecting a Canvas step that belongs to a chosen Canvas. It must be used with a Canvas variable.

- **Replacement value:** Canvas step API ID
- **Usage example:** {% raw %}`canvas_step_api_id = ‘{{canvas_step.${some name}}}’`{% endraw %}

##### Canvas Steps

For selecting Canvas steps that belong to chosen Canvases. It must be used with a Canvas or Canvases variable.

- **Replacement value:** Canvas steps API IDs
- **Usage example:** {% raw %}`canvas_step_api_id IN ({{canvas_steps.${some name}}})`{% endraw %}

#### Products

For selecting a list of product names.

- **Replacement value:** Product names are surrounded by single quotes and separated by commas, such as in `product1, product2`
- **Usage example:** {% raw %}`product_id IN ({{products.${product name (optional)}}})`{% endraw %}

#### Custom events

For selecting a list of custom events.

- **Replacement value:** Custom event property names are separated by commas such as in `event1, event2`
- **Usage example:** {% raw %}`name = ‘{{custom_events.${event names)}}}’`{% endraw %}

#### Custom event properties

For selecting a list of custom event property names. It must be used with the custom events variable.

- **Replacement value:** Custom event property names are separated by commas such as in `property1, property2`
- **Usage example:** {% raw %}`name = ‘{{custom_event_properties.${property names)}}}’`{% endraw %}

#### Workspace

For selecting a workspace.

- **Replacement value:** Workspace BSON ID
- **Usage example:** {% raw %}`workspace_id = ‘{{workspace.${app_group_id}}}’`{% endraw %}

#### Catalogs

For selecting catalogs.

- **Replacement value:** Catalog BSON IDs
- **Usage example:** {% raw %}`catalog_id = ‘{{catalogs.${catalog}}}’`{% endraw %}

#### Catalog Fields

For selecting catalog fields. It must be used with the catalogs variable.

- **Replacement value:** Catalog field names
- **Usage example:** {% raw %}`field_name = '{{catalog_fields.${some name}}}’`{% endraw %}

#### Options {#options}

For selecting from a list of options.

- **Replacement value:** The value of the selected options
- **Usage example:**
    - For select dropdown: {% raw %}`{{options.${metrics} | is_multi_select: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}`{% endraw %}
        - `is_multi_select` allows specifying whether the end user can select more than one option
    - For radio button: {% raw %}`{{options.${metrics} | is_radio_button: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}`{% endraw %}

#### Segments

For selecting segments that have [Analytics Tracking]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/) turned on.

- **Replacement value:** The segment analytics ID, which corresponds to the IDs stored in the `user_segment_membership_ids` column in the tables where this column is available.
- **Usage example:** {% raw %}`{{segments.${analytics_segments}}}`{% endraw %}

#### String

For changing repetitive string values between report runs. Use this variable to avoid hardcoding a value multiple times in your SQL.

- **Replacement value:** The string as is without any surrounding quotes
- **Usage example:** {% raw %}`{{string.${some name}}}`{% endraw %}

#### Tags

For selecting tags for campaigns and Canvases.

- **Replacement value:** Campaigns and Canvases with single-quoted comma-separated BSON IDs that are associated with the selected tags
- **Usage example:** {% raw %}`{{tags.${some tags}}}`{% endraw %}

### Variable metadata

Metadata can be attached to a variable to change its behavior by appending the metadata with a pipe ( &#124; ) character following the variable name. The ordering of the metadata doesn’t matter and you can append any number of them. Additionally, all types of metadata can be used for any variable, except for special metadata that is specific to certain variables (this will be indicated in those cases). The usage of all metadata is optional and is used to change the default’s variable behavior.

**Usage example:** {% raw %}`{{string.${my var}| is_required: ‘false’ | description: ‘My optional string var’}}`{% endraw %}

#### Visible

For whether variables are visible. All variables are visible by default in the **Variables** tab, where you can input values.

There are several special variables whose value is dependent on another variable, such as whether another variable has a value. These special variables are marked as not visible so they don't show in the **Variables** tab.

**Usage example:** `visible: ‘false’`

#### Required

For whether variables are required by default. An empty value for a variable usually leads to an incorrect query.

**Usage example:** `required: ‘false’`

#### Order

For selecting the position of the variable in the **Variables** tab.

**Usage example:** `order: ‘1’`

#### Include single quotes

For surrounding the values of a variable with single quotes.

**Usage example:** `include_quotes: ‘true’`

#### Include double quotes

For surrounding the values of a variable with double quotes.

**Usage example:** `include_double_quotes: ‘true’`

#### Multi-select

For whether the select dropdown allows a single or multi-select. For now, you can include this metadata only if you use the [Options](#options) variable.

**Usage example:** `is_multi_select: ‘true’`

![][7]{: style="max-width:50%;"}

#### Radio button

For showing options as radio buttons instead of a select dropdown in the **Variables** tab. You can include this metadata only if you use the [Options](#options) variable.

**Usage example:** `is_radio_button: ‘true’`

![][6]{: style="max-width:50%;"}

#### Options 

For providing the list of selectable options in the form of a label and value. The label is what gets shown and the value is what the variable gets replaced with when the option is selected. You can include this metadata only if you use the [Options](#options) variable.

**Usage example:** `options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'`

#### Placeholder

For specifying the placeholder text shown in the variable’s input field.

**Usage example:** `placeholder: ‘enter some value’`

#### Description

For specifying the description text shown under the variable’s input field.

**Usage example:** `description: ‘some description’`

#### Default value

For specifying the default value for the variable when no value is specified.

**Usage example:** `default_value: ‘5’`

#### Hide label

For hiding the variable's name label. The variable's name is used as a default label.

**Usage example:** `hide_label: ‘true’`

### Special variables

The following variables can be used with other variables:

#### Presence or absence of another variable’s value

For knowing whether a variable’s value is filled. This is useful for optional variables where you want to short-circuit a condition if a variable’s value is not filled.

- **Replacement value:** `true` or `false` depending on the other variable’s value
- **Usage example:** {% raw %}`{{string.${type_name_has_no_value} | visible: 'false'}} or {{string.${type_name_has_value} | visible: 'false'}}`{% endraw %}

`type` and `name` refer to the referenced variable. For example, to short-circuit the following optional variable: {% raw %}`{{campaigns.${messaging}}`, you can use the following:
`{{string.${campaigns_messaging_has_no_value}  | visible: 'false'}} OR campaign_id IN ({{campaigns.${messaging} | is_required: ‘false’}})`{% endraw %}

## Report timeout

Reports that take longer than six minutes to run will time out. If this is the first query you're running in some time, it may take longer to process and therefore has a higher likelihood of timing out. If this happens, try running the report again.

If a report times out or runs into errors even after retrying, contact [Support]({{site.baseurl}}/help/support#braze-support).

## Data and results

Results, and exports of results, are tables that can contain up to 1,000 rows. For reports that require larger amounts of data, you can use tools such as [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) or the [export API endpoint]({{site.baseurl}}/api/endpoints/export).

## Monitoring your Query Builder usage

Each Braze workspace has 5 Snowflake credits available per month. A small portion of a Snowflake credit is used whenever you run a query or preview a table.

{% alert note %}
Snowflake credits are not shared between features. For example, credits across SQL Segment Extensions and Query Builder are independent of each other.
{% endalert %}

Credit usage is correlated to the run time of your SQL query. The longer the run time is, the higher the portion of a Snowflake credit a query will cost. Run time can vary depending on the complexity and size of your queries over time. The more complex and frequent queries you run, the larger your resource allocation and the faster your run time becomes.

Credits are not used when writing, editing, or saving reports within the Braze SQL editor. Your credits will reset to 5 on the first of each month at 12 am UTC. You can monitor your monthly credit usage at the top of the Query Builder page.

![Query Builder showing the amount of credits used in the current month.][1]{: style="max-width:60%;"}

When you reach the credit cap, you cannot run queries, but you can create, edit, and save SQL reports. If you want to purchase more Query Builder credits, please get in touch with your account manager.

[1]: {% image_buster /assets/img_archive/query_builder_credits.png %}
[2]: {% image_buster /assets/img_archive/query_builder_ai_tab.png %}
[3]: {% image_buster /assets/img_archive/sql_variables_panel.png %}
[4]: {% image_buster /assets/img_archive/query_builder_time_range.png %}
[5]: {% image_buster /assets/img_archive/sql_variables_canvases.png %}
[6]: {% image_buster /assets/img_archive/sql_variables_campaigns.png %}
[7]: {% image_buster /assets/img_archive/sql_variables_productname.png %}
