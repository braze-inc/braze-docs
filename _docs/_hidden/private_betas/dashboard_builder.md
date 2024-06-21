---
nav_title: Dashboard Builder
article_title: Dashboard Builder
permalink: "/dashboard_builder/"
description: "This reference article covers how to use Dashboard Builder to create dashboards and visualizations using reports created in Query Builder."
page_type: reference
hidden: true
---

# Dashboard Builder

> Use Dashboard Builder to create dashboards and visualizations using reports created in Query Builder. You can get started with the pre-built SQL query templates in Query Builder or write your own custom SQL queries to unlock even more insights.

Braze provides pre-built dashboard templates for frequent use cases such as analysis of revenue using last-touch attribution. Note that the ability to edit a template dashboard is not yet available.

{% alert note %}
Dashboard Builder is currently in early access. Contact your customer success manager if you're interested in participating in this early access.
{% endalert %}

## Running a dashboard template

1. Go to **Analytics** > **Dashboard Builder**. The home page lists all existing dashboards within your workspace, with Braze-created templates at the top. These are denoted with "(Braze)" in the title.
2. Select the dashboard you’re interested in.
3. Select **Run Dashboard** to generate a dashboard using that template.

### Available dashboard templates

#### Revenue - Last Touch Attribution

The **Revenue - Last Touch Attribution** template provides a review of revenue across campaigns, Canvases, and channels. All revenue data is attributed to the last-touched message during the attribution window.

Touches include `Email Click`, `Content Card Click`, `In-App Message Click`, `SMS Delivery`, `WhatsApp Read`, and `Webhook Send`.

| Metrics | Definition |
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
{: .reset-td-br-1 .reset-td-br-2}

#### Devices and carriers

| Metrics | Definition |
| --- | --- |
| Device Carriers | Count of users in the selected date range who opened a push notification, grouped by device carrier. |
| Device Model | Count of users in the selected date range who opened a push notification, grouped by device model. |
| Device Operating System | Count of users in the selected date range who opened a push notification, grouped by device operating system. |
| Device Screen Size | Count of users in the selected date range who opened a push notification, grouped by device screen resolution (size). |
{: .reset-td-br-1 .reset-td-br-2}

## Creating a customized dashboard

1. Select **Create Dashboard**, or an existing dashboard and **Edit**. Then select **+ Add Tile**.
2. Select **Select Existing Query** and choose a query you've run in Query Builder.
3. To edit how the query results display in the tile, select the pencil icon to change the title and chart type.<br><br>![Tile editor view with options to change the title and chart type.][2]{: style="max-width:60%;"}<br><br>
    - If selecting a chart type of **Column**, **Bar**, or **Line**:
        - Select a field from the query to use for your X-axis.
        - De-select the columns you're not interested in.<br><br>![Dropdown with the chart types.][1]{: style="max-width:40%;"}

{: start="4"}        
4. Make sure to save your changes. If you want to delete the tile, select the trash can icon. Deleted tiles can't be reverted and must be recreated.
5. Adjust the tile size by dragging the bottom right corner, and the tile position on the dashboard by dragging the handle at the top right corner.<br><br>![Tile getting dragging by the handle.][3]<br><br>
6. Add additional tiles until your dashboard is complete.
7. Select **View Dashboard**, and then select **Run Dashboard**. Your dashboard might take up to a few minutes to finish generating reports.

## Share your feedback with us

Feel free to share your feedback with us by contacting your customer success manager or by replying to the enablement email you received.

[1]: {% image_buster /assets/img/chart_type.png %}
[2]: {% image_buster /assets/img/sample_tile.png %}
[3]: {% image_buster /assets/img/drag_tile.png %}
