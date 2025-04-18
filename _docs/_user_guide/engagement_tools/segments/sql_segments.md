---
nav_title: "SQL Segment Extensions"
article_title: SQL Segment Extensions
alias: "/sql_segments/"
page_order: 3.2

page_type: reference
description: "This article describes how to create a SQL Segment Extension using Snowflake queries."
tool: Segments
---

# SQL Segment Extensions

> You can generate a Segment Extension using Snowflake SQL queries of [Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/) data. SQL can help you unlock new segment use cases because it offers the flexibility to describe the relationships between data in ways that aren't achievable through other segmentation features.

Like standard Segment Extensions, you can query events from up to the past two years (730 days) in your SQL Segment Extension.

## Types of SQL Segment Extensions

There are two types of SQL editors to choose from when creating your SQL Segment Extension: the SQL Editor, and the Incremental SQL Editor.

- **Creating extensions with SQL Editor (full refresh):** Each time your segment refreshes, Braze will query all available data to update your segment, which will use more credits than incremental refreshes. Full refresh extensions can automatically regenerate membership daily, but can’t be refreshed using incremental refresh.
- **Creating extensions with Incremental SQL Editor (incremental refresh):** Incremental refresh calculates only the last two days' worth of data, which is more cost-efficient and uses up fewer credits each time. When you create an incremental refresh SQL segment, you can set it to automatically regenerate membership daily. <br><br>The main benefit of extensions with incremental refresh is that you can set your segment to automatically refresh membership daily. Segments created with our regular SQL editor can only have their membership refreshed manually. This helps reduce the cost of a daily data refresh for SQL Segment Extensions.

{% alert tip %}
You can do a manual full refresh on all SQL Segments created in either SQL editor.
{% endalert %}

## Creating SQL Segment Extensions

{% tabs local %}
{% tab Full refresh %}

To create a full refresh SQL Segment Extension:

1. Go to **Audience** > **Segment Extensions**.
2. Click **Create New Extension** and select **Full refresh**.<br><br>
   ![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. Add a name for your Segment Extension and input your SQL. Refer to the section [Writing SQL](#writing-sql) for requirements and resources.<br><br>
   ![SQL editor showing an example SQL Segment Extension.]({% image_buster /assets/img_archive/sql_segments_editor.png %}){: style="max-width:60%" }<br><br>
4. Save your Segment Extension.

{% endtab %}
{% tab Incremental refresh %}

The Incremental refresh SQL editor allows user query aggregations to happen on a per date basis for an event within a given time frame. To create an incremental refresh SQL Segment Extension:

1. Go to **Audience** > **Segment Extensions**.
{% alert note %}

If you are using the [older navigation]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/), you can find this page at **Engagement** > **Segments** > **Segment Extensions**.
{% endalert %}

{:start="2"}
2. Click **Create New Extension** and select **Incremental refresh**.<br><br>
   ![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. Add a name for your Segment Extension and input your SQL. Refer to the section [Writing SQL](#writing-sql) for requirements and resources.<br><br>
   ![SQL editor showing an example incremental SQL Segment Extension.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:60%" }<br><br>
4. If desired, select **Regenerate Extension Daily**.<br><br>
   ![Checkbox to regenerate the extension daily.]({% image_buster /assets/img_archive/sql_segments_regenerate.png %}){: style="max-width:60%" }<br><br>
   When selected, Braze will update segment membership each day automatically. This means that each day at midnight in your company’s time zone (with a potential delay of an hour), Braze will check for new users in your segment and automatically add them to your segment. If a Segment Extension has not been used in 7 days, Braze will automatically pause daily regeneration. An unused Segment Extension is one that is not part of a campaign or Canvas (the campaign or Canvas doesn't need to be active for the extension to be considered "used").<br><br>
5. Save your Segment Extension.

{% endtab %}

{% tab AI SQL Generator %}

{% alert note %}
The AI SQL generator is currently available as a beta feature. Contact your customer success manager if you're interested in participating in this beta trial.
{% endalert %}

The AI SQL generator leverages [GPT](https://openai.com/gpt-4), powered by OpenAI, to recommend SQL for your SQL segment.

![AI SQL generator with the prompt "Users that received a notification last month"]({% image_buster /assets/img/ai_sql_generator.png %}){: style="max-width:70%;"}

To use the AI SQL generator, do the following:

1. Click **Launch AI SQL Generator** after creating a [SQL segment]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments) using either full or incremental refresh.
2. Type in your prompt and click **Generate** to translate your prompt into SQL.
3. Review the generated SQL to make sure it looks correct, and then save your segment.

### Example prompts
- Users who received an email in the last month
- Users who made less than five purchases in the last year

### Tips
- Familiarize yourself with the available [Snowflake data tables]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/). Asking for data that doesn't exist in these tables may result in ChatGPT making up a fake table.
- Familiarize yourself with the [SQL writing rules]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments?tab=sql%20editor#writing-sql) for this feature. Not following these rules will cause an error. For example, your SQL code must select the `user_id` column. Starting your prompt with "users who" can help.
- You can send up to 20 prompts per minute with the AI SQL Generator.

### How is my data used and sent to OpenAI?

In order to generate your SQL, Braze will send your prompts to OpenAI’s API Platform. All queries sent to OpenAI from Braze are anonymized, meaning that OpenAI will not be able to identify from whom the query was sent unless you include uniquely identifiable information in the content you provide. As detailed in [OpenAI’s API Platform Commitments](https://openai.com/policies/api-data-usage-policies), data sent to OpenAI’s API via Braze is not used to train or improve their models and will be deleted after 30 days. Please ensure that you adhere to OpenAI’s policies relevant to you, including the [Usage Policy](https://openai.com/policies/usage-policies). Braze makes no warranty of any kind with respect to any AI-generated content. 
{% endtab %}
{% endtabs %}

{% alert note %}
SQL queries that take longer than 20 minutes to run will time out.
{% endalert %}

When the extension finishes processing, you can [create a segment][4] using your Segment Extension and target this new segment with your campaigns and Canvases.

## Writing SQL

Your SQL query should be written using [Snowflake syntax](https://docs.snowflake.com/en/sql-reference.html). Consult the [table reference]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) for a full list of tables and columns available to be queried.

{% alert important %}
Note that the tables available to query contain only event data. If you wish to query for user attributes, you should combine your SQL segment with custom attribute filters from the [classic segmenter]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).
{% endalert %} 

{% tabs %}
{% tab SQL Editor %}

Your SQL must additionally adhere to the following rules:

- Write a single SQL statement. Do not include any semicolons.
- Your SQL must select only one column: the `user_id` column. This means your SQL must contain:

```sql
SELECT DISTINCT user_id FROM "INSERT TABLE NAME"
```

- It isn't possible to query for users with zero events, which means any query for users that have done an event less than X times would need to follow this workaround:
   1. Write a query to select users who have the event MORE than X times.
   2. When referencing your Segment Extension in your segment, select `doesn't include` to invert the result.

{% endtab %}
{% tab Incremental SQL Editor %}

All incremental refresh queries consist of two parts: a query, and schema details.

1. In the editor, write a query that selects `user_id`s from your desired table.
2. Add schema details by selecting an **Operator**, **Number of times**, and **Time period** from the fields above the editor. The query will check if the sum of the aggregate column meets a certain condition specified by the {% raw %}`{{operator}}` and `{{number of times}}`{% endraw %} placeholders. This functions similarly to the workflow for creating classic Segment Extensions.<br><br>
   - **Operator:** Indicate if the event has happened more than, less than, or equal to a number of occurrences.<br>
   ![Operator field with "More than" selected.]({% image_buster /assets/img_archive/sql_segments_operator.png %})<br><br>
   - **Number of times:** How many times you would like to evaluate the event in relation to the operator.<br>
   ![Number of times with "5" entered.]({% image_buster /assets/img_archive/sql_segments_times.png %})<br><br>
   - **Time period:** Number of days from 1 to 730 in which you want to check instances of the event. This time period refers to past days relative to the current day. The following example shows querying for users that performed the event more than 5 times in the past 365 days.<br>
   ![Time period field with "365" entered.]({% image_buster /assets/img_archive/sql_segments_period.png %})

In the following example, the resulting segment would contain users that performed the `favorited` event more than 3 times during the last 30 days, after a specified date.

![SQL editor showing an example incremental SQL Segment Extension.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:65%" }

![SQL preview of an incremental SQL Segment Extension.]({% image_buster /assets/img_archive/sql_segments_incremental_preview.png %}){: style="max-width:85%" }

### Additional rules

Your incremental refresh query must additionally adhere to the following rules:

- Write a single SQL statement. Do not include any semicolons.
- Your incremental SQL segment would be able to refer to just one single event. Your dropdowns for date and count are in reference to your chosen event.
- Your SQL must have the following columns: `user_id`, `$start_date`, and an aggregation function (such as `COUNT`). Any SQL saved without these three fields will result in an error.

{% alert tip %}
Incremental refresh segments take into account late events, which are events that occurred more than 2 days ago (for example, SDK events that weren’t sent at the time they were captured).
{% endalert %}

{% endtab %}
{% endtabs %}

## Previewing results

Before saving, you can run a preview of your query. Query previews are automatically limited to 100 rows and will timeout after 60 seconds. The `user_id` column requirement does not apply when running a preview.

For incremental SQL Segment Extensions, the preview will not include the additional criteria from your operator, number of times, and time period fields.

## Managing SQL Segment Extensions

On the **Segment Extensions** page, segments generated using SQL are denoted with <i class="fas fa-code" alt="SQL Segment Extension"></i> next to their name.

Select a SQL Segment Extension to view where the extension is being used, archive the extension, or manually [refresh the segment membership](#refreshing-segment-membership).

![Messaging Use section of the SQL editor showing where the SQL segment is being used.][3]

### Refreshing segment membership

To refresh the segment membership of any Segment Extension created using SQL, open the Segment Extension and select **Refresh**. Only incremental refresh SQL Segment Extensions can automatically regenerate (if selected).

{% alert tip %}
If you created a segment where you expect users to enter and exit regularly, manually refresh the Segment Extension it uses before targeting that segment in a campaign or Canvas.
{% endalert %}

## Monitoring your SQL Segments usage

Each Braze workspace has 5 Snowflake credits available per month. If you need more credits, contact your account manager. Credits are used whenever you refresh, or save and refresh, a SQL Segment’s membership. Credits are not used when you run previews within a SQL Segment or save or refresh a classic Segment Extension.

{% alert note %}
Snowflake credits are not shared between features. For example, credits across SQL Segment Extensions and Query Builder are independent of each other.
{% endalert %}

Credit usage is correlated to the run time of your SQL query. The longer the run time is, the more credits a query will cost. Run time can vary depending on the complexity and size of your queries over time. The more complex and frequent queries you run, the larger your resource allocation and the faster your run time becomes.

To save on credits, preview your query to ensure it is correct before saving the SQL Segment Extension.

Your credits will reset to 5 on the first of each month at 12 am UTC. You can monitor your credit usage throughout the month within the credits usage panel. From the **Segment Extensions** page, click <i class="fa-solid fa-chart-column"></i> **View SQL Credit Usage**.

![SQL Credit Usage panel in the SQL Segment Extensions page][5]{: style="max-width:60%"}

The following will happen when your credits reach zero:

- Any SQL Segment Extensions set up to automatically refresh stop refreshing, impacting the membership of these segments and any campaigns or Canvases that target these segments.
- You can only save new SQL Segment Extensions as drafts for the remainder of the month.

All company users who created a SQL Segment and your company admins will receive a notification email when you have used up 50%, 80%, and 100% of your credits. After your credits reset at the start of the next month, you can create more SQL Segments, and automatic refreshes will resume.

If you want to purchase more SQL Segment credits or additional Segment Extensions, please contact your account manager.

## Troubleshooting

Your query may fail for any of the following reasons:

- Syntax errors in your SQL query
- SQL does not adhere to the [SQL rules](#writing-sql)
- Processing timeout (after 20 minutes)

[1]: {% image_buster /assets/img_archive/sql_segments_create.png %}
[2]: {% image_buster /assets/img_archive/sql_segments_editor.png %}
[3]: {% image_buster /assets/img_archive/sql_segments_usage.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension#step-5-use-your-extension-in-a-segment
[5]: {% image_buster /assets/img_archive/sql_segments_credits.png %}
[6]: {% image_buster /assets/img/ai_sql_generator.png %}
