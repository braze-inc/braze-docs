---
nav_title: Event user log
article_title: Event User Log
page_order: 7
page_type: reference
description: "This reference article covers the Event User Log, which can help you debug or troubleshoot issues in your Braze Integration."

---

# Event User Log

> The Event User Log can help you break down, debug, or otherwise troubleshoot issues in your Braze Integration. This tab gives you a log of errors that details the type of error, which app it's associated with, when it happened, and often an opportunity to view the raw data associated with it.

{% alert tip %}
In addition to this article, we also recommend checking out our [Quality Assurance and Debugging Tools](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/) Braze Learning course, which covers how to use the Event User Log to conduct your own troubleshooting and debugging.
{% endalert %}

To access the log, go to **Settings** > **Event User Log**.

To find your logs easily, you can filter based on:

* SDK or API
* App Names
* Time frame
* User

Each log is broken up into multiple sections, which can include:

* Device Attributes
* User Attributes
* Events
* Campaign Events
* Response Data

Select the **Expand data** icon to show the raw JSON data for that specific log.

![The "Expand data icon" next to a specific log.]({% image_buster /assets/img_archive/expand_data.png %})

Event User Logs will remain in the dashboard for 30 days after they are logged.

![Raw logs for events]({% image_buster /assets/img_archive/rawlogs.png %}){: style="max-width:60%;"}

## Troubleshooting

### Missing SDK logs for test users

If you've added a user to an internal group, but they aren't showing any SDK logs in the Event User Log, this may be a result of a missing configuration option. In order to capture SDK logs, make sure to select **Record User Events for group members** in the **Internal Group Settings** for that [internal group]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/).

### Delay in logs updates

This is potentially a normal slowness on the part of our API.

When you call SDK methods, generally the SDK caches those events locally and flushes them to the server every 10 seconds. It can take anywhere from a second to a few minutes for our job processing queue to ingest events, depending on the overall load at the time.  

If you're looking for events to arrive as fast as possible, try calling the `requestImmediateDataFlush()` function.

### Session end and session start have similar timestamps (iOS)

The Event User Log shows the timestamp of when Braze was notified the session ended, which will be milliseconds before the next session starts. Braze is unable to know the session has ended before the app is re-opened because iOS is aggressive about stopping the execution of threads when the app is in the background—so no data can be flushed to Braze until the app is reopened.

While the session end time will be specified as seconds before session start, when the event is flushed, the Session Duration is flushed separately and is correct—reflecting the time the app was open. Therefore, this behavior does not impact the `Median Session Duration` filter.

In relation to user sessions, you can use Braze to monitor data like:

- How many sessions a user has had
- When a user last started a session
- If the user starts a session after receiving a campaign
- What the user's median session duration is

These behaviors are not impacted by the session end event being flushed on the next session.

