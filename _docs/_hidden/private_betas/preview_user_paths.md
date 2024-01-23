---
nav_title: Preview User Paths
article_title: Preview User Paths
permalink: /preview_user_paths/
description: "This reference article covers how to preview user paths in Canvas."
Tool:
  - Canvas
hidden: true
---

# Preview user paths in Canvas

> Experience the Canvas journey you've created for your users. This includes previewing the timing and messages they will receive. These test runs act as quality assurance that your messages are sent to the right audience, all before sending the Canvas.

{% alert important %}
Previewing user paths in Canvas is currently in early access and only available in pre-launch draft Canvases. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

## Start a test run

Follow these steps to preview your user journey:

1. Go to your Canvas builder. Save any unsaved changes and resolve any errors.
2. Click **Test Canvas** in the footer.
3. Select a test user.
4. (optional) Select a recipient for the test.
5. Click **Run Test**.

You can run a preview if you don't have permission to edit a Canvas, but this preview will run with unsaved changes if there are any.

### Supported steps

The following steps are supported:
- Message 
- Audience Path
- Decision Split
- Delay
- Action Path
- Experiment Path

If the test overlaps with a step type that isn't listed above, the unsupported step will be skipped, and the test user will continue to the next supported step.

### Canvas step details

To view more details for entrance criteria, click **See more**. Steps with segmentation will show the met or unmet criteria. Messages will also show this for delivery validations and channel eligibility. Message steps will show which channels were sent versus not sent.

## Previews for timing

For scheduled Canvases, the test user will enter at the next scheduled entrance time. For action-based Canvases with start dates, the test user will enter on the start date and time.

Message and Delay steps show the time at which a user would progress or receive the message without needing to reconfigure the delays. Note that while the steps will indicate whether Intelligent Timing is used, this preview of the user path does not calculate an estimate for a test user.

## Action Paths and events

If your Canvas includes an Action Paths step, select whether a user took an action or not in the step. During this preview, an event isn’t performed, meaning that event properties aren’t applied based on the step’s outcome. The same is true for the Canvas entry in that Braze does not perform the entry event or API trigger, so the event and API trigger properties are not applied based on the Canvas entry.

## When users enter and exit

Test users will enter the preview even if they are not eligible in real life. If they are not eligible, you can see why they would not have met the criteria.

While exit criteria are not yet supported, you can still view the exits in the sidebar and the Canvas body. For testing purposes, the following are assumed to be true:

- Re-eligibility is allowed.
- Rate limiting and frequency capping are valid.

## Experiment Paths and Canvas variants

- For Canvases with top-level variants, select a variant at the start of the test.
- For Experiment Paths, select the variant the user progresses through when the test user encounters the step.
- For Experiment Paths using Personalized Path or Winning Variant, while there’s a delay period over which the test user waits in a Message step, this delay isn’t taken into account since Braze assumes the user progressed through the selected variant immediately.

## Test sends

You can opt to send test messages to an internal test group or an individual user as the test run populates. This means that only messages the user encounters along the test path will be sent. The recipients will receive messages with their own attributes by default, but you can override these with the test user’s attributes.

## Responsiveness

At the moment, filters within steps in this preview mode are not responsive to the timing assumed by the test run. For example, if an audience path references an event that has occurred on or after a specific date, and the test run shows the results for a future date, the filter will not take that future date into account.

Similarly, filters won’t recognize actions that occurred as a result of the test user interacting with other steps in the Canvas. For example, this preview mode won’t recognize that a user encountered a Message step that was “sent” earlier in the Canvas, and it won’t recognize that the test user “took action” to advance through an action path.

## Connected Content

Connected Content will be executed if it’s included in the Canvas. If your Canvas includes Connected Content, remove the Connected Content that is configured to alter user profiles or data that is referenced in other Canvases or campaigns. Or, you can opt to not preview the user journey.

## Webhooks

Webhooks will execute when test messages are sent, but not during the test run. Similar to Connected Content, consider removing webhooks that are configured to alter user profiles or data that is referenced in other Canvases or campaigns.

## Example

In this example, the Canvas is set up to target users who haven't had a session in an app. This journey includes a Message step with a welcome email, a Delay step set for one day, and an Audience Paths step that splits into two paths: users with at least one session, and everyone else. Depending on which audience path a user falls in, the subsequent Message step will be sent.

![][1]{:style="max-width:70%"}

Because our test user meets the Canvas entry criteria, they can enter the Canvas and go through the user journey. However, because our test user hasn't opened the app in the last calendar day, they will continue down the "Everyone else" path and receive a push notification that reads: "Last chance! Complete your first task for an exclusive bonus."

![][2]

[1]: {% image_buster /assets/img/preview_user_path_example.png %}
[2]: {% image_buster /assets/img/preview_user_path_results_example.png %}
