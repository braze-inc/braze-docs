---
nav_title: Pre and post-launch checklist
article_title: Pre and Post-Launch Checklist
page_order: 2
description: "This article provides a guideline for things to check before and after you launch a Canvas."
tool: Canvas

---

# Pre and post-launch checklist

> This article provides a guideline for things to check before and after you launch a Canvas.

## Things to consider before launch

Before you launch a Canvas, there are several details you can check to ensure that your messaging and send times align with your audience's preferences. Things to consider include any variations in time zones, entry settings, and more. Using this checklist as a guide, finetune these areas based on your use case to help contribute to the success of your Canvas. 

### Review time zone settings

If you're entering users according to their local time zone using a scheduled entry schedule, you should launch your Canvas at least 24 hours prior to when you want users to enter your Canvas. For example, here's a Canvas that hasn't left enough time between the launch and the scheduled entry time. In this scenario, there may be some users who won't enter your Canvas since the scheduled entry time has already passed in certain time zones. 

{% alert tip %} 
You'll see an alert if you haven't scheduled enough of a buffer. A quick solution is to adjust the send time to ensure that users can remain in the targeted segment for a full 24 hours.
{% endalert %}

![A Canvas scheduled to enter users at one time starting at 10 am on April 30, 2025, in their local time.]({% image_buster /assets/img_archive/canvas_checklist1.png %}){: style="max-width:75%;"}

### Consider using regular expressions for audience filters

After setting up the preliminary details of when your users should enter a Canvas, it's recommended to now check your segments or filters in the **Target Audience** step of building a Canvas. In this step, you can also review the **Target Population** summary to see how your target audience has been set up. 

Here, consider using a regular expression for segments or filters in Audience Paths steps, delivery validation settings in Message and Decision Split steps as well. A [regular expression]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/) (also referred to as regex) is a string, which means it recognizes patterns and takes into account characters, instead of things like capitalization. This means that if you're using "Equals / Does Not Equal," you could be limiting your audience size because of simple syntax errors.

If you notice that your target audience is smaller than expected, try using "Matches Regex" or "Does Not Match Regex" instead of "Equals" or "Does Not Equal". This may account for those missing users, and target a larger audience. 

### Identify entry settings and race conditions

A race condition can occur when you've used the same entry criteria in both your **Entry Schedule** and **Target Audience** settings. 

If you're using action-based entry, check that you haven't used the same trigger action here as in your target audience. A race condition may occur in which the user is not in the audience at the time they perform the trigger event, which means they won't enter the Canvas.

{% alert tip %}
Check out the [best practices]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/#scenario-3-matching-action-based-triggers-and-audience-filters) for avoiding this race condition when setting up an action-based Canvas with the same trigger as the audience filter.
{% endalert %}

### Check Canvas entry properties and event properties

Though similar in name, [Canvas entry properties and event properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) function differently within your Canvas workflows. Canvas entry properties are tied to your entry settings, and they can be referenced in any message component throughout your Canvas. Canvas entry properties are properties of the event or API call that triggers a user's entry into a Canvas, using action-based or API-triggered entry settings.

Event properties, on the other hand, can only be referenced in the first Message step following an Action Paths step. Event properties are properties of a custom event or purchase event that the user performed during the evaluation window of an Action Paths step, and that triggers their progression down one of the defined action path.

Check your message preview for any Message steps referencing Canvas entry properties or event properties.

### Review Message steps for user advancement

By default, users will advance through all Message steps regardless of whether they received the message. If you want to advance the users who receive a particular message, you can do so by adding a Decision Split step directly after your Message component. Add the filter "Received Message from Canvas Step" as the additional filter, then select the Canvas and Message step.

For Message steps with in-app messaging, you may want to use an Action Paths component instead of the Decision Split component. This will allow you to advance users based on whether they've viewed your in-app message. Define an action group by adding the filter "Interact with Step" and select **View in app message**. Then, set the evaluation window of the step to the expiration window of the in-app message.

For a Message component in multi-channel messaging, we recommend the following:
* Include a Delay step in between your Message and Decision Split steps, and set the delay to at least five seconds
* If the component includes Intelligent Timing, set the delay to 24 hours
* If the component includes rate limiting, split your messages into several single-channel Message steps and connect them together. Then, connect the Decision Split step directly after the last Message step to check whether a user received any of the messages. You can also use this method as an alternative for a multi-channel Message step with Intelligent Timing.

## Things to consider after launch

You've launched your Canvas! Now, what? Use this checklist to see how you can review and adjust your Canvas in the event of discrepancies after launch based on these scenarios.

### Many entries, but few sends

For example, let's say that you've noticed a disparity between your number of messages sent versus total entries. You can identify and uncover areas to adjust your Canvas by checking these key areas.

#### Entry audience

If you're using a scheduled send campaign, double-check your target audience by reviewing your target population. How do the numbers look across the channels, and how does that relate to the channels you've used in your Canvas? If the lowest numbers correspond with the channels you've used in your Canvas, you may have found the issue.

#### First component of the Canvas

Review any audience filters, action triggers, or segments used in the beginning components of your Canvas. Are there any misspellings, or too-strict conditions that are preventing your Canvas from starting off right? Are you using "Equals" when you should be using "Matches Regex"?

#### Canvas control group 

Review the distribution of users between your variants and your control group. Is the control group larger than you meant it to be? If so, you can edit this setting. If you have **Intelligent Selection** turned on, and the control group is winning, consider stopping your Canvas and trying a new approach.

### An empty total audience

If you aren’t seeing any entry data for your Canvas, the reason that users may not be entering your Canvas can be due to race conditions and restrictive audience segmentation filters.

If you're using action-based entry in your entry schedule, check that you haven't used the same trigger action here as in your **Target Audience**. A race condition may occur in which the user is not in the audience at the time they perform the trigger event, which means they won't enter the Canvas.

Additionally, check that the selected segment has users in it by reviewing the **Target Population** table in the **Target Audience** settings. If this number is low, see how you can adjust your entry settings, or review your selected segments or filters for any errors.

### Unexpected drop-off between steps

Another apparent way to identify areas of adjustment for your Canvas can occur when there's a large drop-off from one Canvas step to the next. In this case, check that your audience filters and exception events don't have any misspellings or capitalization errors. And as always, check that your audience filters aren't so strict as to omit a majority of your users from entering the Canvas. 

Next, it's important to identify these settings that can affect when and if messages are sent to your users:
- [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/)
- Quiet Hours
- Delivery validations

In general, choose either Intelligent Timing or Quiet Hours for your Canvas, not both. The same suggestion applies to use either Intelligent Timing or [rate limiting]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/), not both. For more information on how to best use the Intelligence Suite, read our [Intelligence FAQ]({{site.baseurl}}/user_guide/brazeai/intelligence/faqs/).

### Suspicious send volumes between paths

When the volume of sends between two or more paths (either Audience Paths or Action Paths) isn't what you expect, this can be an opportunity to check your segments, filters, or trigger actions. Also, be sure to identify and remove any overlapping filters.

