---
nav_title: Why are my conversions low?
page_order: 1

page_type: solution
description: "This help article walks you through troubleshooting campaigns or Canvases with lower than expected conversion rates."
tool:
- Canvas
- Campaigns
noindex: true
---

# Why Are My Conversions Low?

Your conversions (when your user performs an action within your message that you defined during the creation of your campaign) might not be as high as you expect them to be - whether as compared to previous comparable campaigns or your predictions/expectations. Conversions are a tricky business, but are dependent upon a few simple functions in our platform: event tracking and conversion deadlines.

To quickly troubleshoot why that is, we recommend that you...

* [Check Event Tracking](#ensure-the-event-is-tracking)
* [Verify Deadline](#verify-the-deadline-to-convert)


## Ensure the Event is Tracking

When a campaign triggers a session start or custom event, you want to ensure that this event, or session is happening frequently enough to trigger the message. Check this data on the [Overview][1] (for session data) or [Custom Events][2] pages:

![trouble17][43]

## Verify the Deadline to Convert

For each conversion event that you select per campaign, you set the [deadline][44]. This means you are setting a time limit within which a conversion must happen in order for it to count towards each respective campaign.

Please ensure you’ve reviewed Braze's information on [calculating conversions][45] in order to understanding your campaign metrics.

Still need help? [Open a support ticket]({{site.baseurl}}/support_contact/).

[1]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/understanding_your_app_usage_data/#understanding-your-app-usage-data
[2]: {{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[43]: {% image_buster /assets/img_archive/trouble17.png %}
[44]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#step-2-add-conversion-events
[45]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-tracking-rule