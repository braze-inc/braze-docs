---
nav_title: Funnel reports
article_title: Funnel Reports for Campaigns and Canvases
page_order: 6
page_type: reference
description: "This page covers the benefits of funnel reports, how to set them up, and how to interpret your report."
tool: Reports
---

# Funnel reports

> Funnel reporting offers a visual report that allows you to analyze the journeys your customers take after receiving a campaign or Canvas. ![Funnel Report 2]({% image_buster /assets/img/funnel_report/funnel_report2.png %}){: style="float:right;max-width:15%;margin-bottom:15px; border: 0"}

If your campaign or Canvas uses a control group or multiple variants, you can understand how the different variants have impacted the conversion funnel at a more granular level and optimize based on this data.

![Funnel Report 1]({% image_buster /assets/img/funnel_report/funnel_report1.jpg %}){: style="max-width:80%;"}

## Setting up funnel reports

![Funnel Report 5]({% image_buster /assets/img/funnel_report/canvas_campaign.png %}){: style="float:right;max-width:40%;border:0;margin-left:15px;"}

You can run funnel reports for existing active campaigns and Canvases. These reports show a series of events that a campaign recipient progresses through over 1-30 days from the date they enter the Canvas or campaign. A user is considered converted through a step in the funnel if they perform the event in the specified order.

Funnel reporting is available from the following locations in the dashboard:

- The **Campaign Analytics** page for a specific campaign
- The **Canvas Details** page for a specific Canvas, by selecting the **Analyze Variants** button 

{% alert important %}
Funnel Reports are not available for [API campaigns]({{site.baseurl}}/api/api_campaigns/).
{% endalert %}

### Step 1: Select a date range

You can select a time frame for your report (within the past six months), and refine the data to see users who, upon entering the campaign or Canvas, completed the funnel events within a set window (maximum of 30 days). In the following example, your funnel would look for users who received this campaign or Canvas in the last seven days and completed the funnel within three days.

{% alert note %}
If you set the window to complete the funnel to one day, then the funnel event must occur within 24 hours of message receipt. However, if you select multiple days, the timing window is counted as calendar days in the company time zone.
{% endalert %}

![Funnel report for a Canvas with "Last 7 Days" selected in the time frame dropdown.]({% image_buster /assets/img/funnel_report/funnel_report5.png %}){: style="max-width:90%;"}

### Step 2: Select events for funnel steps

For every funnel report, the first event is when the user receives your message. From there, the subsequent events you choose funnel the number of users who performed those events, as well as the previous events. 

#### Available funnel report events

| Campaign | Started Session, Made Purchase, Performed Custom Event, Message Engagement Event |
| Canvas | Started Session, Made Purchase, Performed Custom Event, Received Canvas Step, Interacted with Step |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert note %}
The **Interacted with Step** report event can only be used with Canvas steps that use the Email or push messaging channels.
{% endalert %}

![Funnel report for a Canvas with a dropdown of the available report events.]({% image_buster /assets/img/funnel_report/funnel_report3.png %}){: style="max-width:80%;"}

Funnel reports allow you to compare the success of your messages beyond just the conversion events or message engagement events you initially set up. So if there's a conversion event you didn't add initially, you can still track conversions for that event using a funnel.

For example, if you select a 14-day report time window, followed by the events `Added to cart` and `Made purchase`, you will see both the number of users who added to cart within 14 days of receiving the message and the number of users who added to cart and then made a purchase within 14 days of receiving the campaign.

As another example, you may want to see the percentage of users that converted on an email after clicking on it. To calculate this, you could create a report where the second event is clicking your email and the third event is performing your conversion event.

After selecting **Build Report**, the funnel report may take several minutes to generate. During this time, you can navigate away from the report to other pages in the dashboard. You'll receive an in-dashboard notification when your report is ready.

## Interpreting your funnel report

In your funnel report, you can directly compare the control group alongside the variants you have set up. Each consecutive event will show what percentage of the previous users completed that action and converted through the funnel.

### Funnel report components

- **Horizontal axis**: Displays the percentage of message recipients who performed those actions. 
- **Chart**: Displays the number of received messages, the number of users that performed the prior actions, as well as the action you chose, the conversion rate, and the percentage change from control.
- **Regenerate Option**: Allows you to regenerate your report and indicates when the current report was last generated. 
- **Variants**: Denoted by colored columns, funnel reporting allows up to 8 variants and a control group. By default, the **chart** will only show three variants. To see more, you can manually select the rest of the variants.

![Funnel report chart.]({% image_buster /assets/img/funnel_report/funnel_report4.jpg %})

**For campaigns with multiple variants**: Braze will show a table with metrics for each event and variant and the percentage change from control. The conversion rate is the number of users who performed the event (and subsequent ones) per message recipient.

**For campaigns with re-eligibility**: If a user receives the campaign more than once in the report time window, Braze will determine whether the user should be included in the funnel based on the actions this user took after the first time they received the campaign within the time window.
- Note that there may be a discrepancy between the funnel and standard conversion values, as users can convert more than once with re-eligibility, but funnel reports will convert a maximum of one time even if a user performs the event more than once. 

**For multivariant campaigns with re-eligibility**: If a user receives multiple variants from the campaign during the report time window, Braze will determine whether they should be included in the variant funnel based on the actions this user took after the first time they received the campaign variant. This means that the same user could count toward multiple different variants if they received multiple variants during the time window for the funnel.

{% alert important %}
Orphaned users are not tracked in funnel reports. When an anonymous user enters a Canvas or campaign and later becomes identified through the `changeUser()` method, their Braze ID changes. Funnel reports only track follow-up events that match the user ID at the time of entry and do not account for events performed by the user after their ID changes. This means that conversion events performed by the user after becoming identified will not be included in the funnel report.
{% endalert %}

