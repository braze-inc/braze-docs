---
nav_title: In-App Message Impressions Appear Lower Than Expected
page_order: 1

page_type: solution
description: "This help article covers actions you can take if your in-app message impressions are lower than you'd like them to be."
channel: in-app messages
noindex: true
---
# In-App Message Impressions Appear Lower Than Expected

If your impressions are lower than you'd like them to be, we recommend you...

* [Check Segment](#segment-size)
* [Check Changelogs](#segment-changelogs)
* [Run Tests](#run-tests)
* [Check Event Triggers](#event-triggers)
* [Check Message Impressions](#message-impressions)

## Segment Size

It’s important to ensure that your Segment size in the campaign reflects your intended audience. Perhaps there are filters applied limiting your audience and causing your campaign to have fewer impressions.

## Segment Changelogs

If the impression count is low compared to where it once was, make sure no one unintentionally altered the Segment or campaign since launch. Our Segment and campaign changelogs will give you insight into changes that have been made, who made the change, and when it happened.

![trouble4][10]

## Run Tests

A quick way to identify any obvious issues is to clone the campaign and target your own userid/email and launch the campaign. Once you perform the message trigger (session start, custom event, etc.), verify that you receive the message correctly. Then, navigate to the dashboard and refresh the page to see if your impression is logged correctly. If it is not, then the problem is likely within your implementation.


## Event Triggers

If the campaign is triggered by a session start or a custom event, you want to ensure that this event or session is happening frequently enough to trigger the message. Check this data on the [Overview][1] (for session data) or [Custom Events][2] pages:

![trouble5][11]

## Message Impressions

Customization of the in-app message UI or delivery mechanisms within the SDK may require your developers to utilize our methods to manually log in-app message impressions. Check with your developers to see if you use in-app message customization.

You can read more about this:
  * [iOS][12] In-app message documentation
  * [Android][13] In-app message documentation

Still need help? [Open a support ticket]({{site.baseurl}}/support_contact/).

[1]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/understanding_your_app_usage_data/#understanding-your-app-usage-data
[2]: {{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[10]: {% image_buster /assets/img_archive/trouble4.png %}
[11]: {% image_buster /assets/img_archive/trouble5.png %}
[12]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/#logging-impressions-and-clicks
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/#setting-custom-listeners
