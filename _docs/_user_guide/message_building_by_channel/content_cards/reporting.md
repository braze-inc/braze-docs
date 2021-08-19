---
nav_title: Reporting & Analytics
article_title: Reporting & Analytics
page_order: 4
description: "This reference article provides an overview of the different Content Card reporting metrics and analytics options provided in the Braze dashboard."
channel:
  - content cards
tool:
  - Reports
  
---

# Reporting & Analytics

> This reference article provides an overview of the different Content Card reporting metrics and analytics options provided in the Braze dashboard.

## Content Card Metrics

- **Recipients**: The number of users who have received a Content Card that received at least one impression.
- **Impressions**: The number of times a Content Card was visible and on-screen.
- **Clicks**: The number of times a user has clicked the CTA Link of a Content Card.
- **Dismissals**: The number of times a user has swiped away or clicked to dismiss a Content Card.

To see the meanings of all Content Cards metrics, check the [Report Metrics Glossary][1].

### Control Groups

To measure the impact of an individual Content Card, a [Control Group][2] can be added to an A/B Test.

The Campaign Details Analytics Block (located above the Performance table) will not include metrics from the Control Group variant.

{% alert warning %}
If you have a customized feed, be sure to log impressions for control cards to inform our analytics of when a user _would have seen_ the control card in its feed position. For more detail, see the [iOS](/docs/developer_guide/platform_integration_guides/ios/content_cards/data_model/#card-methods), [Android](/docs/developer_guide/platform_integration_guides/android/content_cards/customization/#fully-custom-content-card-display-for-android), and [Web](/docs/developer_guide/platform_integration_guides/web/content_cards/integration/#control-group) developer guides.
{% endalert %}

## Reporting in Campaigns

Campaigns will deliver your reports in a series of blocks. You may see more or less than those listed in the tabs below, but each has its own useful purpose.

{% tabs %}

{% tab Campaign Details %}

**Campaign Details**

The Campaign Details analytics block will give you a high-level overview of the entire Content Card campaign.

![CC_Campaign_Details]({% image_buster /assets/img/cc-campaign-details.png %})

{% endtab %}

{% tab Message Performance %}

**Message Performance**

This block will define the messages performance on multiple levels (by Variant, Audience %, Unique Impressions, Impressions, Body Clicks, Button Clicks, Revenue, Primary Conversions, and more!). Click on the <i class="fa fa-eye preview-icon"></i> to view your message.

![CC_Message_Performance]({% image_buster /assets/img/cc-message-performance.png %})

{% endtab %}

{% tab Historical Performance %}

**Historical Performance**

This block allows you to see the message's performance over a set time period on a timeline.

![CC_Historical_Performance]({% image_buster /assets/img/cc-historical-performance.png %})

{% endtab %}

{% tab Conversion Event Details %}

**Conversion Event Details**

This block will show you the performance of your conversion events for an individual Content Card.

![CC_Conversion]({% image_buster /assets/img/cc-conversion.png %})

{% endtab %}

{% endtabs %}

For definitions of all Content Cards metrics, refer to the [Report Metrics Glossary][1].

[1]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/
[2]: {{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants
