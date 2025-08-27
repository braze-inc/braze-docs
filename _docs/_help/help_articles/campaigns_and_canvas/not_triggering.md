---
nav_title: Untriggered campaign or Canvas
article_title: Untriggered Campaign or Canvas
page_order: 5

page_type: solution
description: "This help article walks you through steps to resolve issues with campaigns or Canvases not triggering as expected."
tool: 
- Campaigns
- Canvas
---

# Untriggered campaign or Canvas

There are a number of reasons why you did not get the expected trigger behavior. The solution for the most common error is to ensure that the campaign that you are triggering does not use the same trigger event in the segment.

## Campaign triggers

Segment membership is evaluated before trigger actions. This means that if the user does not fall into the segment first, they will not receive the campaign even if they perform the trigger.

If your campaign is triggered off of a custom event, you will want to make sure that this event is not pre-filtered by a segment you want to use in the campaign. 

For example, if the segment includes the event `SessionStart` "Has Used App more than once" and the event the campaign triggers off of is `SessionStart`, the user will receive the message, but it won't necessarily be for the first session. This is because during the first step when checking if a user should receive a campaign, the campaign is reviewing the segment target audience. 

In short, avoid configuring an action-based campaign or Canvas with the same trigger as the audience filter (such as a changed attribute or performed a custom event). A [race condition]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/#race-conditions/) may occur in which the user is not in the audience when they perform the trigger event, which means they won't receive the campaign or enter the Canvas.

{% alert tip %}
For further assistance with campaign troubleshooting, be sure to contact Braze Support within 30 days of your issue's occurrence as we only have the last 30 days of diagnostic logs.
{% endalert %}

_Last updated on June 25, 2024_

