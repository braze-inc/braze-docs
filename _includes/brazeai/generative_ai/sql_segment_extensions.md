# SQL Segment Extensions

> You can generate a Segment Extension using Snowflake SQL queries of [Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/) data. SQL can help you unlock new segment use cases because it offers the flexibility to describe the relationships between data in ways that aren't achievable through other segmentation features.
>
> Like standard Segment Extensions, you can query events from up to the past two years (730 days) in your SQL Segment Extension.

## Prerequisites

Because it's possible to access PII data through this feature, you must have PII permissions to run SQL segment queries.

## Creating a Segment Extension

### Step 1: Choose an editor

There are two types of SQL editors to choose from when creating your SQL Segment Extension: the SQL Editor, and the Incremental SQL Editor.

- **Full Refresh:** Each time your segment refreshes, Braze will query all available data to update your segment, which will use more credits than incremental refreshes. Full refresh extensions can automatically regenerate membership daily, but can’t be refreshed using incremental refresh.
- **Incremental refresh:** Incremental refresh calculates only the last two days' worth of data, which is more cost-efficient and uses up fewer credits each time. When you create an incremental refresh SQL segment, you can set it to automatically regenerate membership daily. This let's you set your segment to automatically refresh membership daily, which helps reduce the cost of a daily data refresh for SQL Segment Extensions.
- **AI SQL generator:** The AI SQL Generator lets you write a prompt in plain language and turns it into a SQL query for your segment. It's a quick way to get started without needing to write the SQL yourself.

{% alert tip %}
You can do a manual full refresh on all SQL Segments created in either SQL editor.
{% endalert %}

{% tabs local %}
{% tab Full refresh %}

To create a full refresh SQL Segment Extension:

1. Go to **Audience** > **Segment Extensions**.
2. Select **Create New Extension**, then select **Full refresh**.<br><br>
   ![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. Add a name for your Segment Extension and input your SQL. Refer to [Step 2](#step-2-write-your-sql) for requirements and resources.<br><br>
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
2. Select **Create New Extension** and select **Incremental refresh**.<br><br>
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

1. Select **Launch AI SQL Generator** after creating a [SQL segment]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments) using either full or incremental refresh.
2. Type your prompt and select **Generate** to translate your prompt into SQL.
3. Review the generated SQL to make sure it looks correct, and then save your segment.

#### Example prompts
- Users who received an email in the last month
- Users who made less than five purchases in the last year

#### Tips
- Familiarize yourself with the available [Snowflake data tables]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/). Asking for data that doesn't exist in these tables may result in ChatGPT making up a fake table.
- Familiarize yourself with the [SQL writing rules]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments?tab=sql%20editor#writing-sql) for this feature. Not following these rules will cause an error. For example, your SQL code must select the `user_id` column. Starting your prompt with "users who" can help.
- You can send up to 20 prompts per minute with the AI SQL Generator.

##{% multi_lang_include brazeai/generative_ai/policy.md %}
{% endtab %}
{% endtabs %}

{% alert note %}
SQL queries that take longer than 20 minutes to run will time out.
{% endalert %}

When the extension finishes processing, you can [create a segment]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension#step-5-use-your-extension-in-a-segment) using your Segment Extension and target this new segment with your campaigns and Canvases.

### Step 2: Write your SQL

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

#### Additional rules

Additionally, your standard SQL query must adhere to the following rules:

- You cannot use `DECLARE` statements.
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

{% alert tip %}
Incremental refresh segments take into account late events, which are events that occurred more than 2 days ago (for example, SDK events that weren’t sent at the time they were captured).
{% endalert %}

#### Additional rules

Additionally, your incremental refresh query must adhere to the following rules:

- Write a single SQL statement. Do not include any semicolons.
- Your incremental SQL segment would be able to refer to just one single event. Your dropdowns for date and count are in reference to your chosen event.
- Your SQL must have the following columns: `user_id`, `$start_date`, and an aggregation function (such as `COUNT`). Any SQL saved without these three fields will result in an error.
- You cannot use `DECLARE` statements.
{% endtab %}
{% endtabs %}

{% alert note %}
If you're creating a SQL segment that uses the table `CATALOGS_ITEMS_SHARED`, you must specify a catalog ID. For example:

```sql
SELECT * FROM CATALOGS_ITEMS_SHARED
WHERE CATALOG_ID = 'XYZ'
LIMIT 10
```
{% endalert %}

### Step 3: Preview the query

Before saving, you can run a preview of your query. Query previews are automatically limited to 100 rows and will timeout after 60 seconds. The `user_id` column requirement does not apply when running a preview.

For incremental SQL Segment Extensions, the preview will not include the additional criteria from your operator, number of times, and time period fields.

### Step 4: Determine if you need to invert SQL

Next, determine if you need to invert SQL. While it's not possible to directly query for users with zero events, you can use **Invert SQL** to target these users.

{% alert note %}
By default, **Invert SQL** is not toggled on. However, if you use the AI SQL generator to generate a SQL statement that needs to be negated, ChatGPT could return an output that automatically toggles this feature on.
{% endalert %}

For example, to target users who have fewer than three purchases, first write a query to select users who have three or more purchases. Then, select the **Invert SQL** to target users with fewer than three purchases (including those with zero purchases).

{% alert important %}
Unless you're specifically aiming to target users with zero events, you won't need to invert SQL. If **Invert SQL** is selected, confirm that the feature is needed and that the segment matches your desired audience. For example, if a query targets users with at least one event, it will only target users with zero events when inverted.
{% endalert %}

![Segment Extension named "Clicked 1-4 emails in the last 30 days" with the option to invert SQL selected.]({% image_buster /assets/img_archive/sql_segment_invert_sql.png %}){: style="max-width:90%;"}

## Refreshing segment membership

To refresh the segment membership of any Segment Extension created using SQL, open the Segment Extension and select **Refresh**.

{% alert tip %}
If you created a segment where you expect users to enter and exit regularly, manually refresh the Segment Extension it uses before targeting that segment in a campaign or Canvas.
{% endalert %}

## Managing your Segment Extensions

On the **Segment Extensions** page, segments generated using SQL are denoted with <i class="fas fa-code" alt="SQL Segment Extension"></i> next to their name.

Select a SQL Segment Extension to view where the extension is being used, archive the extension, or manually [refresh the segment membership](#refreshing-segment-membership).

![Messaging Use section of the SQL editor showing where the SQL segment is being used.]({% image_buster /assets/img_archive/sql_segments_usage.png %}){: style="max-width:70%;"}

### Designating refresh settings

{% multi_lang_include segments.md section='Refresh settings' %}

## Snowflake credits

Each Braze workspace has 5 Snowflake credits available per month. If you need more credits, contact your account manager. Credits are used whenever you refresh, or save and refresh, a SQL Segment’s membership. Credits are not used when you run previews within a SQL Segment or save or refresh a classic Segment Extension.

{% alert note %}
Snowflake credits are not shared between features. For example, credits across SQL Segment Extensions and Query Builder are independent of each other.
{% endalert %}

Credit usage is correlated to the run time of your SQL query. The longer the run time is, the more credits a query will cost. Run time can vary depending on the complexity and size of your queries over time. The more complex and frequent queries you run, the larger your resource allocation and the faster your run time becomes.

To save on credits, preview your query to ensure it is correct before saving the SQL Segment Extension.

Your credits will reset to 5 on the first of each month at 12 am UTC. You can monitor your credit usage throughout the month within the credits usage panel. From the **Segment Extensions** page, click <i class="fa-solid fa-chart-column"></i> **View SQL Credit Usage**.

![SQL Credit Usage panel in the SQL Segment Extensions page]({% image_buster /assets/img_archive/sql_segments_credits.png %}){: style="max-width:60%"}

The following will happen when your credits reach zero:

- Any SQL Segment Extensions set up to automatically refresh stop refreshing, impacting the membership of these segments and any campaigns or Canvases that target these segments.
- You can only save new SQL Segment Extensions as drafts for the remainder of the month.

All company users who created a SQL Segment and your company admins will receive a notification email when you have used up 50%, 80%, and 100% of your credits. After your credits reset at the start of the next month, you can create more SQL Segments, and automatic refreshes will resume.

If you want to purchase more SQL Segment credits or additional Segment Extensions, please contact your account manager.
