---
nav_title: Reports and insights
article_title: Reports and Insights
description: "Learn how to view BrazeAI Decisioning Studio™ reports in Braze, so you can understand how AI-powered decisions impact your campaigns."
page_order: 3
---

# Reports and insights

> Learn how to view BrazeAI Decisioning Studio™ reports in Braze, so you can understand how AI-powered decisions impact your campaigns. From performance metrics to data health and system changes, these reports help you understand results, troubleshoot issues, and make informed decisions with confidence.

## Prerequisites

Before you can view Decisioning Studio reports in the Braze, you'll need to:

- Have an active contract for Braze and BrazeAI Decisioning Studio™. 
- Contact your CSM to enable BrazeAI Decisioning Studio™ for you on your behalf.
- Have a live BrazeAI Decisioning Studio™ agent.

## Viewing reports {#view}

To view metrics for a Decisioning Studio agent in Braze, go to **AI Decisioning** > **BrazeAI Decisioning Studio™**, then select an agent.

![BrazeAI Decisioning Studio™ reporting home screen showing a dashboard with multiple report cards. Each card displays a report type such as Performance, Insights, Diagnostics, and Timeline, with brief descriptions and icons for each.]( {% image_buster /assets/img/decisioning_studio/reporting_home.png %} )

Here, you can view reports like performance, insights, diagnostics, and timelines. For more details, see [Available reports](#available-reports).

## Changing report dates

After [opening a report](#view), you can change the date range by selecting a new start and end date from the calendar dropdown.

![BrazeAI Decisioning Studio™ date range selector open with a calendar dropdown. The calendar displays selectable start and end dates for customizing the report view.]({% image_buster /assets/img/decisioning_studio/reporting_change_date_range.png %}){: style="max-width:50%;"}

You can also set a default start date or choose dates to always exclude. Excluded dates will be filtered out of all reports for that agent.

To set or exclude dates, select <i class="fa-solid fa-gear"></i> **Settings**, then change your default date or exclude dates as needed.

![Settings panel open in BrazeAI Decisioning Studio™ showing options to set a default start date and exclude specific dates from reports. The panel displays two sections labeled Default start date and Exclude dates. Under Exclude dates, several dates are listed with checkboxes next to each.]({% image_buster /assets/img/decisioning_studio/reporting_set_exclude_dates.png %})

## Available reports {#available-reports}

- **[Performance]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/performance/)**: High-level agent metrics that compare treatment groups to control groups, with **Trending** and **Driver Tree** views.
- **[Insights]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/insights/)**: How recommendation options in your action bank are generated, including **Agent preferences** and **SHAPs** reports.
- **[Diagnostics]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/diagnostics/)**: Outbound and inbound data health, including recommendation volume and data feed monitoring.
- **[Timeline]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/timeline/)**: A visual record of key events (agent runs, configuration changes, guardrail updates) alongside performance metrics.
