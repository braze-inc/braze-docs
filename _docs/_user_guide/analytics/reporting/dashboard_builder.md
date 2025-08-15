---
nav_title: Dashboard Builder
article_title: Dashboard Builder
alias: "/dashboard_builder/"
description: "This reference article covers how to use Dashboard Builder to create dashboards and visualizations using reports created in Query Builder."
page_type: reference
tool:
    - Reports
page_order: 6.1
---

# Dashboard Builder

> Use Dashboard Builder to create dashboards and visualizations using reports created in Report Builder or Query Builder.

Dashboard Builder empowers you to compose and visualize custom analytic dashboards from scratch and from Braze-supplied templates. You can use either a no-code data source (Report Builder) or SQL data source (Query Builder) to power your dashboard, or start from one of many Braze templates.

## Creating a custom dashboard

1. Go to **Analytics** > **Dashboard Builder**.
2. Select **Create Dashboard**.
3. Select which data source will power your reports:
- **Reports** that were built in Report Builder
- **Custom Queries** that were created in Query Builder<br><br>![Window to select your data source for your dashboard.]({% image_buster /assets/img/select_data_source.png %})<br><br>

Now, follow the respective steps for your data source:

{% tabs %}
{% tab Reports %}

{: start="4"}
4. Select **+ Add Tile** and then choose one of the reports you created in [Report Builder (New)]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/).
5. Select the pencil icon to change how the title and chart type display in the tile.
    - You can toggle between different chart types below the default visualization. The current options include bar charts (horizontal or vertical), and line charts (only available if you selected **Date** as a drilldown option in the Report Builder setup).<br><br>![Toggles for different chart types.]({% image_buster /assets/img/report_builder_types.png %})<br><br>
    - Use the metrics dropdown to select which metrics to include in your visualization. By default, the first column in the report will be the default displayed metric.
6. Select **Save** after you've changed the visualization to your liking.
7. Add a name, description, and tag to make your dashboard easier to find later.
{% endtab %}
{% tab Custom Queries %}
{: start="4"}
4. Select **+ Add Tile** and then choose a query you’ve run in Query Builder.
5. To edit how the query results display in the tile, select the pencil icon to change the title and chart type.
    - You can toggle between different chart types below the default visualization. Current options include tables, bar charts (horizontal or vertical), and line charts.<br><br>![Toggles for different chart types.]({% image_buster /assets/img/query_builder_types.png %})<br><br>
        - If you choose one of the chart options, use the **X-axis** dropdown to select a single column from your query results to use as your x-axis.
        - Use the **Y-axis** dropdown to select which metrics to include in your visualization. By default, all columns from your query results will display, so de-select the columns you’re not interested in viewing.<br><br>![Toggles for different chart types.]({% image_buster /assets/img/query_builder_axis.png %})<br><br>
        - (Optional) You can use the **Grouping** dropdown to group together your query results. For example, if you have campaign ID as a column result and you want to add together all the rows with that value, use the **Grouping** dropdown.  
        - (Optional) To edit the data being displayed, select the query that is attached to the visual and make your edits in [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/). 
6. Select **Save** after you've changed the visualization to your liking.
7. Add a name, description, and tag to make your dashboard easier to find later.
{% endtab %}
{% endtabs %}

{: start="8"}
8. Repeat steps 4—7 for your respective method until you create your desired dashboard.
9. Select **View Dashboard** > select **Run Dashboard**. 

Your dashboard may take up to a few minutes to finish generating reports.

{% alert note %}
You can add up to 10 tiles to a dashboard.
{% endalert %}

## Managing dashboard tiles

### Delete tiles

Delete a dashboard tile by selecting **Delete Tile** at the bottom of the tile. **This action can’t be reverted.**

### Duplicate tiles

Make a copy of your tile by selecting **Duplicate Tile** at the bottom of the tile.

### Adjust tile size and position

Adjust the tile size by dragging the bottom-right corner of the tile, and adjust the tile position on the dashboard by dragging the handle at the top right corner of the tile.

## Running a dashboard template

1. Go to **Analytics** > **Dashboard Builder**. The home page lists all existing dashboards within your workspace, with Braze-created templates at the top. These are denoted with "(Braze)" in the title.
2. Select the dashboard you’re interested in.
3. Select **Run Dashboard** to load the respective dashboard using that template.

### Available dashboard templates

Braze provides pre-built dashboard templates for frequent use cases such as analysis of revenue using last-touch attribution. Note that the ability to edit a template dashboard is not yet available. Reach out to your customer success manager if you'd like to see certain dashboard templates in future template releases.

#### Revenue - Last Touch Attribution

The **Revenue - Last Touch Attribution** template provides a review of revenue across campaigns, Canvases, and channels. All revenue data is attributed to the last-touched message during the attribution window.

Touches include _Email Click_ (link click), _Content Card Click_, _In-App Message Click_ (excluding close buttons), _Push Opens_, _SMS Short Link Click_, _WhatsApp Read_, and _Webhook Send_.

| Metric | Definition |
| --- | --- |
| Total Last Touch Revenue | A sum of all campaign and Canvas revenue events with a last-touch event within the selected date range and attribution window. |
| Total Purchase Conversions | A count of all campaign and Canvas revenue events with a qualifying last-touch event. |
| Average Days to Convert | The average time between all campaign and Canvas purchase events with a qualifying last-touch event. |
| Revenue per Recipient | Sum of the revenue from qualified revenue events divided by the number of unique users that received a message within the date range. |
| Unique Purchasers | Count of the unique users with a qualified revenue event. |
| Revenue by Country | Sum of all campaign and Canvas revenue events with a last-touch event, grouped by country. |
| Revenue by Campaign | Sum of all campaign and Canvas revenue events with a qualifying last-touch event, grouped by campaign. |
| Revenue by Campaign Variant | Sum of all campaign and Canvas revenue events with a qualifying last-touch event, grouped by campaign variant. |
| Revenue by Canvas | Sum of all campaign and Canvas revenue events with a qualifying last-touch event, grouped by Canvas. |
| Revenue by Canvas Variant | Sum of all campaign and Canvas revenue events with a qualifying last-touch event, grouped by Canvas variant. |
| Purchases per Product | A count of all purchases grouped by product. |
| Revenue by Channel | Sum of all campaign and Canvas revenue events with a qualifying last-touch event, grouped by channel. | 
| Revenue Time Series | Sum of all campaign and Canvas revenue events with a qualifying last-touch event, grouped by day in UTC. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Devices and carriers

| Metric | Definition |
| --- | --- |
| Device Carriers | Count of users in the selected date range who opened a push notification, grouped by device carrier. |
| Device Model | Count of users in the selected date range who opened a push notification, grouped by device model. |
| Device Operating System | Count of users in the selected date range who opened a push notification, grouped by device operating system. |
| Device Screen Size | Count of users in the selected date range who opened a push notification, grouped by device screen resolution (size). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Segment Insights - Email

| Metric  | Definition  |
|---|---|
| Weekly Email Metrics (Rates) | Email engagement rates (delivery, bounce, open, click, unsubscribe rates) grouped by segment and displayed as weekly time series.|
| Weekly Email Metrics (Counts) | Email engagement counts (sent, delivered, bounces, opens, clicks, unsubscribes) grouped by segment and displayed as weekly time series.|
| Weekly Purchase Metrics (Rates) | Purchase conversion rates (revenue per recipient) from email opens and clicks, grouped by segment and displayed as weekly time series.|
| Weekly Purchase Metrics (Counts) | Purchase counts and revenue totals from email opens and clicks, grouped by segment and displayed as weekly time series.|
| Email Engagement by Segment | Summary table showing total email engagement metrics (sent, delivered, bounces, opens, clicks, unsubscribes and their rates) aggregated by segment.|
| Purchases & Revenue by Segment | Summary table showing total purchase metrics (purchases, revenue, and revenue per recipient) from email opens and clicks, aggregated by segment.|
| Top 10 Campaigns for Engagement Metrics | Ranked list of campaigns with highest email engagement metrics (configurable metric for ranking).|
| Bottom 10 Campaigns for Engagement Metrics | Ranked list of campaigns with lowest email engagement metrics (configurable metric for ranking).|
| Top 10 Canvases for Engagement Metrics | Ranked list of canvases with highest email engagement metrics (configurable metric for ranking).|
| Bottom 10 Canvases for Engagement Metrics | Ranked list of canvases with lowest email engagement metrics (configurable metric for ranking).|
| Top 10 Campaigns for Purchase Metrics | Ranked list of campaigns with highest purchase conversion metrics from email engagement (configurable metric for ranking).|
| Bottom 10 Campaigns for Purchase Metrics | Ranked list of campaigns with lowest purchase conversion metrics from email engagement (configurable metric for ranking).|
| Top 10 Canvases for Purchase Metrics | Ranked list of canvases with highest purchase conversion metrics from email engagement (configurable metric for ranking).|
| Bottom 10 Canvases for Purchase Metrics | Ranked list of canvases with lowest purchase conversion metrics from email engagement (configurable metric for ranking).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Session Analytics

| Metric | Definition  |
|---|---|
| # of sessions by day (time series) | Count of unique sessions grouped by day within the selected date range, displayed as a time series.|
| Avg # of sessions per user | Average number of sessions per user calculated as total sessions divided by unique users within the selected date range.|
| campaigns convert to sessions | Count of unique sessions that occurred at the same time as campaign conversions, grouped by campaign ID and ranked by session count.|
| canvases convert to sessions | Count of unique sessions that occurred at the same time as canvas conversions, grouped by canvas ID and ranked by session count.|
| Total # of sessions per user | List of top 1,000 users by their total session count within the selected date range.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Share your feedback with us

Select the **Send feedback** button or contact your customer success manager to share your feedback with us.

