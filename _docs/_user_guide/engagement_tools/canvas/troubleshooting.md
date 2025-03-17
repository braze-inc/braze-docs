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

First, confirm that the custom event is being passed to Braze. Go to **Analytics** > **Custom Events Report**, and then select the respective custom event and date range. If the event doesn't pass, confirm that it's set up correctly and that the user performed the correct action.

If the custom event passes, further troubleshoot by doing the following:

- Check the user's profile download to confirm they triggered the event and when they did it. If the event was triggered, compare the timestamp for when the event was triggered to the time the Canvas went live.
- Determine if the user would have been in the segment when triggering by reviewing changelogs for the Canvas and any segments used in targeting.
- Verify whether the user was entered into a control group through segmentation.
- If there is a scheduled delay, check if the event was triggered after the delay. 

If the triggered event changes the user's segment membership and the segment is used within the **Target Audiences** step, this could cause the user to drop out of the Canvas. If the user is currently in the segment, verify how they entered the segment (such as through an attribute or event change). Sometimes the properties come in differently than expected, such as through different datatypes or case.

{% alert note %}
In-app messages can only be triggered by events sent through the SDK, not the REST API.
{% endalert %}