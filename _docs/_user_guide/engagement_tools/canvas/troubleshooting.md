---
nav_title: Troubleshooting
article_title: Troubleshooting Canvases
page_order: 11
page_type: reference
description: "This page provides troubleshooting steps for Canvases."
tool: Canvas
---

# Troubleshooting Canvases

> This page helps you troubleshoot issues with your Canvases.

## Why did a user not receive a triggered Canvas step?

First, confirm that the custom event is being passed to Braze. Go to **Analytics** > **Custom Events Report**, and then select the respective custom event and date range. If the event doesn't display, confirm that it's set up correctly and that the user performed the correct action.

If the custom event displays, further troubleshoot by doing the following:

- Check the user's profile download to confirm they triggered the event and when they did it. If the event was triggered, compare the timestamp for when the event was triggered to the time the Canvas went live. The event may have been triggered before the Canvas went live.
- Review changelogs for the Canvas and any segments used in targeting to determine if the user was in the segment when their custom event was triggered. If they weren't in the segment, they wouldn't have received the Canvas step.
- Verify whether the user was entered into a control group through segmentation and consequently prevented from receiving the Canvas step.
- If there is a scheduled delay, check if the user's custom event was triggered before the delay. If the event was triggered before the delay, they wouldn't have received the Canvas step.

{% alert note %}
In-app messages can only be triggered by events sent through the SDK, not the REST API.
{% endalert %}