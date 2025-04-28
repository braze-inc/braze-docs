---
nav_title: Report Builder
article_title: Report Builder
alias: /report_builder/
page_type: reference
description: "This reference article describes the Report Builder feature."
tool:
    - Reports
page_order: 6.2
---

# Report Builder

> This page covers how to use Report Builder to create and view granular reports using Braze data, and how to add reports to dashboards.

## Using a report template

1. Go to **Analytics** > **Report Builder (New)**.
2. Select the **More options** arrow next to the **Create New Report** button, and then select **Use a report template**.<br><br>!["Create New Report" button dropdown with options to create a custom report or use a template.][9]{: style="max-width:40%;"}<br><br>
3. Select one of the report templates from the Braze template library.
    - Use the **Row items** and **Tags** dropdown to find relevant reports to your use cases.<br><br>!["Braze report templates" window with list of Braze templates to select from.][8]{: style="max-width:90%;"}<br><br>
4. Follow step 3 and onward in [Creating a report](#creating-a-report) to further customize the report to fit your use case.

## Creating a report

1. Go to **Analytics** > **Report Builder (New)**.
2. Select **Create New Report**.
3. In the **Rows** dropdown, select one of the following to create a report:
    - Campaigns
    - Canvases
    - Campaigns and Canvases
    - Channels
    - Tags

![The "Rows and columns" section with fields to select the rows and groupings for your report.][1]{: style="width:90%;"}

{: start="4"}
4. (Optional) Select **Add drilldown** to break down your data into more granular views:
    - Channels
    - Date
        - Use this to split your data into smaller time ranges. For example, if you're interested in how your campaigns performed by day, select the following configuration:
            - **Rows**: Campaigns
            - **Grouping:** Date
            - **Interval:** Days
    - Variants
    - Campaigns and Canvases

{% alert tip %}
Try out different configurations of drilldown options to explore the many ways you can break down your data. 
{% endalert %}

{: start="5"}
5. In the **Columns** section, select **Customize Metrics**.

![The "Customize Metrics" section with options to select multiple metrics.][2]{: style="width:90%;"}

{: start="6"}
6. Browse metrics by category and select the corresponding checkbox to add a metric to your report. 
    - Reorder the metrics and columns by dragging the dotted icon up or down. 
7. In **Report content**, configure the date range for which you’d like to include data in your report.
8. Then, depending on your selections in step 3, choose to manually or automatically add campaigns, Canvases, or both to your report.
    - **Add manually:** Choose each campaign or Canvas to include in the report by using the filters for **Last Sent** dates and tags or channels, or searching the campaign or Canvas name.<br><br>![The "Manually add campaigns and canvases" section with a list of campaigns to select.][3]{: style="width:90%;"}<br><br>
    - **Add automatically:** Set rules for which campaigns or Canvases to include in the report. You're only required to select one field on this page.
        - Note that as additional campaigns or Canvases satisfy the conditions you set on this screen, they will automatically be added to future runs of your report.<br><br>![The "Automatically add campaigns and canvases" section with fields to set rules for which campaigns and Canvases should be added to the report.][4]{: style="width:90%;"}<br><br>
9. Run the report by selecting **Save & Run**.

{% alert note %}
The report may take up to a few minutes to run, depending on the date range and number of campaigns or Canvases you selected in the configuration stage.
{% endalert %}

## Viewing a report

After running your report, you can view your results in table format on the report page. 

![A table of the report data for each campaign's metrics.][5]{: style="width:90%;"}

### Creating a report chart

At the bottom of the page you can create a chart of your data by selecting a **Chart type** and configuring the chart metrics. By default, you'll see the first metric.

![A chart of the report data with options to configure the chart's x-axis, y-axis, chart type, and more.][6]{: style="max-width:90%;"}

{% alert note %}
To create a line chart, select **Date** as a drilldown option when configuring the report. This will display trends over time.
{% endalert %}

#### Downloading a report chart

To download an image of the report chart, select the dotted icon then choose a download option.

![A menu with download options for different file formats.][7]{: style="max-width:30%;"}

## Adding a report to a dashboard

1. Select the dotted icon at the top of the report table.
2. Select **Add to dashboard**.
3. Select whether you want to create a new dashboard or add to an existing dashboard.<br><br>![Window with options to select if you want to add the report to a new or existing dashboard.][10]{: style="width:90%;"}<br><br>
4. Follow the steps in [Dashboard Builder]({{site.baseurl}}/user_guide/analytics/reporting/dashboard_builder/) to learn more about building a dashboard.

[1]: {% image_buster /assets/img/report_builder_2/rows_and_columns.png %} 
[2]: {% image_buster /assets/img/report_builder_2/customize_metrics.png %} 
[3]: {% image_buster /assets/img/report_builder_2/manually_add.png %} 
[4]: {% image_buster /assets/img/report_builder_2/automatically_add.png %} 
[5]: {% image_buster /assets/img/report_builder_2/report_table.png %} 
[6]: {% image_buster /assets/img/report_builder_2/visualize_table.png %} 
[7]: {% image_buster /assets/img/report_builder_2/download_options.png %} 
[8]: {% image_buster /assets/img/report_builder_2/report_templates.png %} 
[9]: {% image_buster /assets/img/report_builder_2/create_new_report.png %} 
[10]: {% image_buster /assets/img/report_builder_2/add_to_dashboard.png %} 