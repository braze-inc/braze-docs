---
nav_title: Using Event Logging
article_title: Using Event Logging
page_order: 6

page_type: solution
description: "This help article describes how to use event logging to troubleshoot issues with your Braze integration."
---

# Using event logging

The [Event User Log][1] helps you troubleshoot any issues with your Braze integration.

Two particularly helpful steps are setting up:
* [An anonymous profile](#setting-up-an-anonymous-profile)
* [Event logging](#using-event-logging)

## Setting up an anonymous profile

To set up an anonymous profile, check out this article on [adding test users][2].

## Using event logging

Use event logging to test what behavior looks like for an anonymous user. This can be particularly helpful to identify the user ID if the app being tested doesn't collect email. You can use Braze along with your device’s IP address to add that device as a test user.

This is also a great way to find anonymous users. You can also use this information to test what data is being sent to Braze and check for any discrepancies. From this view, you are able to identify whether the deltas of your data are being sent to Braze. If an email address or push token is being sent with every event logged, then all data is being sent to Braze.

Still need help? Open a [support ticket]({{site.baseurl}}/braze_support/).

_Last updated on March 27, 2019_

[1]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab
[2]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users