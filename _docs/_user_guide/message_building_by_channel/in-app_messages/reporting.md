---
nav_title: Reporting & Analytics
page_order: 7
---

# Reporting & Analytics {#IAM-Reporting}


## In-App Message Analytics Glossary

In reporting for in-app messages, you'll see various reports on the following metrics.

| Metric | Definition |
|---|---|
| Sends | The total number of messages sent in this campaign.
| Total Impressions | The number of users whose devices reported that the in-app message has been delivered (if you receive it twice, you will be counted as twice).
| Unique Impressions | The total number of people who actually received and viewed the in-app message (if you receive it twice, you will be only counted as one user). |
| Unique Recipients | Exact number of users who received a particular message.
| Total Conversions | The total number of times every defined event occurred. This defined event is determined by the marketer when building the campaign. |
| Primary Conversion Event | The number of times a defined event occurred. This defined event is determined by the marketer when building the campaign. |
| Revenue | The total revenue in dollars from campaign recipients within the set primary conversion window. |
| Body Clicks| Occurs when someone clicks on a slideup, modal, or full-screen in-app message that has no buttons. |
| Button Clicks | Total number of clicks on a certain button of the message. |

{% comment %}
Reporting in Canvas

In Canvas, you'll see in-app message performance mapped onto the Canvas you've created. You can use the control panel at the top of the page to uncheck other messaging types and only view the in-app messages in your Canvas.

![In-App_Message_Canvas_Reporting]({% image_buster /assets/img/in-app-message-canvas-reporting.png %})

{% endcomment %}

## Reporting in Campaigns

Campaigns will deliver your reports in a series of blocks. You may see more or less than those listed in the tabs below, but each has their own useful purpose.

{% tabs %}

{% tab Campaign Details %}

__Campaign Details__

The Campaign Details analytics block will give you a high-level overview of the entire in-app message campaign.

![In-App_Message_Campaign_Details]({% image_buster /assets/img/in-app-message-campaign-details.png %})

{% endtab %}

{% tab Message Performance %}

__Message Performance__

This block will define the messages performance on multiple levels (by Variant, Audience %, Unique Impressions, Impressions, Body Clicks, Button Clicks, Revenue, Primary Conversions, and more!). Click on the <i class="fa fa-eye preview-icon"></i> to view your message.

![In-App_Message_Message_Performance]({% image_buster /assets/img/in-app-message-message-performance.png %})

{% endtab %}

{% tab Historical Performance %}

__Historical Performance__

This block allows you to see the message's performance over a set time period on a timeline.

![In-App_Message_Historical_Performance]({% image_buster /assets/img/in-app-message-historical-performance.png %})

{% endtab %}
{% endtabs %}

{% comment %}
If you select to only sent to users who can see the latest Braze version of in-app messages (Generation 3), your Target Audience will not adjust to reflect your choice.
{% endcomment %}
