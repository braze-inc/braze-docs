---
nav_title: Using Event Logging
article_title: Using Event Logging
page_order: 6

page_type: solution
description: "This help article describes how to use event logging to troubleshoot issues with your Braze integration."
---

# The Event Log

The Event User Log helps you troubleshoot any issues with your Braze integration.

Two particularly helpful steps are:
* [Setting Up an Anonymous Profile](#setting-up-an-anonymous-profile)
* [Setting Up Event Logging](#using-event-logging)

## Setting Up An Anonymous Profile

For more information on how to set up an anonymous profile to test in Braze, review the [Event User Log][46] or the [Test User][51] section of the User Guide.

## Using Event Logging

Use Event Logging to test what behavior looks like for an anonymous user. It can also be helpful when the App you are testing does not collect email and you are struggling to find the user ID. You can use Braze along with your device’s IP to add that device as a test user.

This is a great way to find anonymous users. You can also use this information to test what data is being sent to Braze and check any discrepancies. From this view you are also able to identify whether the deltas of your data are being sent to Braze. If an email address or push token is being sent with every event logged that indicates that all data is being sent to Braze.

Still need help? [Open a support ticket]({{site.baseurl}}/support_contact/).

[46]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[51]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users
