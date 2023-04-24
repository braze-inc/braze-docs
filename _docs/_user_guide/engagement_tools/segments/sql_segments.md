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

> You can generate a Segment Extension using Snowflake SQL queries of [Snowflake]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/) data. SQL can help you unlock new segment use cases because it offers the flexibility to describe the relationships between data in ways that aren't achievable through other segmentation features.

{% alert important %}
The SQL editor is in early access. If you're interested in participating in the early access, reach out to your customer success manager.
{% endalert %}

## Creating Segment Extensions using SQL

To create a Segment Extension using SQL:

1. Go to **Segments** > **Segment Extensions**.
2. Click **Create New Extension** and select **SQL Editor**.<br><br>
   ![Dropdown button on the Segment Extension page to open the SQL editor.][1]{: style="max-width:40%" }<br><br>
3. Add a name for your Segment Extension and input your SQL. See the following sections for requirements and resources.<br><br>
   ![SQL editor showing an example SQL Segment Extension.][2]<br><br>
4. Save your Segment Extension.

{% alert note %}
SQL queries that take longer than 20 minutes to run will time out.
{% endalert %}

When the extension finishes processing, you can [create a segment]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension#step-5-use-your-extension-in-a-segment) using your Segment Extension and target this new segment with your campaigns and Canvases.

### Writing SQL

Your SQL query should be written using [Snowflake syntax](https://docs.snowflake.com/en/sql-reference.html). Consult the [table reference]({{site.baseurl}}/sql_segments_tables/) for a full list of tables and columns available to be queried.

Your SQL must additionally adhere to the following rules:

- Write a single SQL statement. Do not include any semicolons.
- Your SQL must select only one column: the `user_id` column. This means your SQL must contain:

```sql
SELECT DISTINCT user_id FROM "INSERT TABLE NAME"
```

### Previewing results

Before saving, you can run a preview of your query. Query previews are automatically limited to 100 rows and will timeout after 60 seconds. The `user_id` column requirement does not apply when running a preview.

## Managing SQL Segment Extensions

On the **Segment Extensions** page, segments generated using SQL are denoted with <i class="fas fa-code" alt="SQL Segment Extension"></i> next to their name.

Select a SQL Segment Extension to view where the extension is being used, archive the extension, or manually [refresh the segment membership](#refreshing-segment-membership).

![Messaging Use section of the SQL Editor showing where the SQL segment is being used.][3]

### Refreshing segment membership

To refresh the segment membership of any Segment Extension created using SQL, open the Segment Extension and select **Refresh**. Currently SQL Segment Extensions do not automatically regenerate.

{% alert tip %}
If you created a segment where you expect users to enter and exit regularly, manually refresh the Segment Extension it uses before targeting that segment in a campaign or Canvas.
{% endalert %}

## Monitoring your SQL Segments usage

Each Braze app group has 1,000 SQL Segment credits available per month. Credits are used whenever you refresh, or save and refresh, a SQL Segment’s membership. Credits are not used when you run previews within a SQL Segment or save or refresh a classic Segment Extension.

Your credits will reset to 1,000 on the first of each month at 12 am UTC. You can monitor your credits usage throughout the month within the SQL credits usage panel. From the **Segment Extensions** page, click <i class="fa-solid fa-chart-column"></i> **View SQL Credit Usage**.

![SQL Credit Usage panel in the SQL Segment Extensions page][4]{: style="max-width:60%"}

The following will happen when your credits reach zero:

- Any SQL Segment Extensions set up to automatically refresh stop refreshing, impacting the membership of these segments and any campaigns or Canvases that target these segments.
- You can only save new SQL Segment Extensions as drafts for the remainder of the month.

All company users who created a SQL Segment and your company admins will receive a notification email when you have used up 50%, 80%, and 100% of your credits. After your credits reset at the start of the next month, you can create more SQL Segments, and automatic refreshes will resume.

If you want to purchase more SQL Segment credits or additional Segment Extensions, please reach out to your account manager.

## Troubleshooting

Your query may fail for any of the following reasons:

- Syntax errors in your SQL query
- SQL does not adhere to the SQL rules
- Processing timeout (after 20 minutes)

[1]: {% image_buster /assets/img_archive/sql_segments_create.png %}
[2]: {% image_buster /assets/img_archive/sql_segments_editor.png %}
[3]: {% image_buster /assets/img_archive/sql_segments_usage.png %}
[4]: {% image_buster /assets/img_archive/sql_segments_credits.png %}
