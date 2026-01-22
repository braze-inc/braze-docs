---
nav_title: Export usage analytics
article_title: Export Usage Analytics
page_order: 3

page_type: reference
description: "This reference article covers how to export high-level app usage data."
tool: 
  - Reports

---

# Export usage analytics

> This page covers the **Home** page of the dashboard, which contains high-level data of app usage, as well as detailed statistics of different KPIs by date.

To export CSVs of data from this page:

1. Set the time frame and apps you want to view data for. By default, the dashboard shows the last 30 days of data for all apps.

![Time period and app fields on the Home dashboard.]({% image_buster /assets/img_archive/home_dashboard_select_date.png %}){: style="max-width:60%;"}

{:start="2"}
2. Scroll down to the **Performance Over Time** graph.
3. Select the data you'd like to export in the **Statistics For** field. See the [available data](#available-data) for you to export.

![Performance Over Time graph on the Home dashboard.]({% image_buster /assets/img_archive/home_dashboard_export.png %})

{:start="4"}
4. Select <i class="fas fa-bars" title="Chart context menu"></i> and then select your export option.

## Available data

You can export CSVs with the following data:

- Session Count by Date
    - (Optional) Session Count for Different Segments
    - (Optional) Session Count for Different App Versions
- DAUs by Date
    - (Optional) DAUs for Different Segments
- Email Statistics by Date
    - Number of Emails Sent
    - Number of Emails Delivered
    - Number of Emails Opened
    - Number of Email Clicks
    - Number of Email Bounces
    - Number of Emails Reported as Spam
- In-App Messages by Date
    - Number of In-App Messages Sent
    - In-App Message Impressions
    - Number of In-App Messages Opened
- MAUs by Date
- Number of New Users by Date
- Push Notifications by Date
    - (Optional) Push Notifications for Different App Platforms
    - Number of Push Notifications Sent
    - Total Opens
    - Direct Opens
    - Bounces
- Session Count by Hour
- Session Count per MAU by Date
- Stickiness by Date

{% alert tip %}
For help with CSV and API exports, visit our [export troubleshooting]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/) article.
{% endalert %}

