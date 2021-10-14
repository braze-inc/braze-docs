---
nav_title: Untriggered Campaign or Canvas
article_title: Untriggered Campaign or Canvas
page_order: 5

page_type: solution
description: "This help article walks you through steps to resolve issues with campaigns or Canvases not triggering as expected."
tool: 
- Campaigns
- Canvas
---

# Untriggered Campaign or Canvas

There are a number of reasons why you did not get the expected trigger behavior.

The solution to the most common error, is to ensure that the campaign that you are triggering does not use the same trigger event in the segment.


## Campaign Triggers

Remember, if the user does not fall into the segment first, they will not receive the campaign even if they perform the trigger.

If your campaign is triggering off of a custom event, you will want to make sure that this event is not pre-filtered by a segment you want to input into the campaign. 

For example, if the Segment includes the event Session Start “Has Used App more than once” and the event the campaign triggers off of is Session Start, the user will receive the message, it just won’t necessarily be for the first session. This is because the first step when checking to see if a user should receive a campaign is reviewing the segment target audience. 

In short, avoid configuring an action-based campaign or Canvas with the same trigger as the audience filter (i.e., a changed attribute or performed a custom event). A race condition may occur in which the user is not in the audience at the time they perform the trigger event, which means they won't receive the campaign or enter the Canvas.  

Still need help? [Open a support ticket]({{site.baseurl}}/support_contact/).

_Last updated on August 5, 2021_