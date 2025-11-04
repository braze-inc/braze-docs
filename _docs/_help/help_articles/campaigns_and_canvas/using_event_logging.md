---
nav_title: Using event logging
article_title: Using Event Logging
page_order: 6
page_type: solution
description: "This help article describes how to use event logging to troubleshoot issues with your Braze integration."
---

# Using event logging

To help troubleshoot issues with your Braze integration, you can set up an anonymous user profile and an [event user log]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab). For steps on how to set up an anonymous profile, refer to [Adding test users]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users).

## About logging

Use event logging to test what behavior looks like for an anonymous user. This can be particularly helpful to identify the user ID if the app being tested doesn't collect email. You can use Braze and your device's IP address to add that device as a test user.

This is a great way to find anonymous users. You can also use this information to test what data is being sent to Braze and check for discrepancies. From this view, you can identify whether the deltas of your data are being sent to Braze. If an email address or push token is sent with every event logged, then all data is sent to Braze.

Still need help? Open a [support ticket]({{site.baseurl}}/braze_support/).

_Last updated on November 16, 2022_

