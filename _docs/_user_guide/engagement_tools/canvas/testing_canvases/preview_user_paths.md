---
nav_title: Preview user paths
article_title: Preview User Paths
page_order: 0.3
alias: /preview_user_paths/
description: "This page covers how you can preview user paths in Canvas."
Tool:
  - Canvas
---

# Preview user paths in Canvas

> Experience the Canvas journey you've created for your users. This includes previewing the timing and messages they will receive. These test runs act as quality assurance that your messages are sent to the right audience, all before sending your Canvas.

## Creating a test run

Follow these steps to preview your user journey:

1. Go to your Canvas builder. Save any unsaved changes and resolve any errors.
2. Select **Test Canvas** in the footer.
3. Select a test user.
4. (Optional) Select a recipient for the test.
5. Select **Run Test**.

You can run a preview if you don't have permission to edit a Canvas, but this preview will run with unsaved changes if there are any.

### Supported steps

The following steps are supported:
- Message 
- Audience Path
- Decision Split
- Delay
- Action Path
- Experiment Path
- User Update (only in the UI editor, meaning steps using JSON editor will be skipped)

If the test overlaps with a step type that isn't listed above, the unsupported step will be skipped, and the test user will continue to the next supported step.

### Canvas step details

To view more details for the entrance criteria, select **See more**. Steps with segmentation will show the met or unmet criteria. Messages will also show this for delivery validations and channel eligibility. Message steps will show which channels were sent versus not sent.

### Liquid

Liquid logic will be processed during a test run, even if you're not sending an actual test message. This means the [abort message logic]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages) and other Liquid logic are reflected and could impact the Canvas user journey.

If your preview sends the last step of your user journey instead of aborting, the preview may be using the current time as the time being tested for Liquid evaluation, not the actual time the user would be in the step based on the Canvas entry time.

## Previews for timing

For scheduled Canvases, the test user will enter at the next scheduled entrance time. For action-based Canvases with start dates, the test user will enter at the start date and time. 

While the default start times still apply, the entrance time is configurable in all instances, meaning you can simulate a date in the past or future. However, you can't test before the start date or after the end date for the Canvas.

Message and Delay steps show the time at which a user would progress or receive the message without needing to reconfigure the delays. Note that while the steps will indicate whether Intelligent Timing is used, this preview of the user path does not calculate an estimate for a test user.

For Canvases with an action trigger like "change in custom attribute value," Braze will attempt to simulate the change by temporarily setting the user's attribute in the trigger to be blank **only for the test run of the Canvas** (this doesn't affect the user profile). This is meant to test that the attribute changes from its current value.

## When users enter and exit

Test users will enter the preview even if they aren't eligible in real life. If they aren't eligible, you can see why they haven't met the criteria. When a test user enters the preview, we assume the test user has met the target audience criteria and performed the action trigger criteria. For example, for a Canvas that uses custom events in the entry criteria, the test user is assumed to have performed the custom event as expected in the entry criteria. However, if the same custom event is used elsewhere in the Canvas (like in the exit criteria), consider how this might impact your user path.

Events, API triggers, custom attributes, and Canvas entry properties are applied based on the Canvas entry. The test run simulates the user journey without applying these elements to change the actual user profile or the flow of the Canvas. For example, during testing, when a custom attribute is used as a Canvas trigger, the trigger criteria is applied to the user's preview **as if** they had triggered the custom attribute change.

### Consideration

If you test an Action Path with actions that correspond to exit criteria (including event properties), the exit criteria will be triggered, and the test run will end. If you test a Message step that corresponds to exit criteria, the exit criteria will be triggered, and the test run will end. 

At this point, you can't select a specific event or property within an action path to trigger exit criteria (only the path as a whole). If a user could potentially meet multiple exit criteria, the first one that is processed and that they meet is shown as the result.

## Experiment Paths and Canvas variants

- For Canvases with top-level variants, select a variant at the start of the test.
- For Experiment Paths, select the variant the user progresses through when the test user encounters the step.
- For Experiment Paths using Personalized Path or Winning Variant, while there’s a delay period over which the test user waits in a Message step, this delay isn’t taken into account since Braze assumes the user progressed through the selected variant immediately.

## Test sends

You can opt to send test messages to an internal test group or an individual user as the test run populates. This means that only messages the user encounters along the test path will be sent. The recipients will receive messages with their attributes by default, but you can override these with the test user’s attributes.

To send all test messages in a Canvas at once, regardless of the path, and without previewing the path, you can select **Send All Test Messages** in the **Test Sends** tab.

## Responsiveness

Canvas steps are responsive to timing when previewing user paths. Updates made via the User Update step are reflected in subsequent steps in the flow but are not applied to the actual user profile. The effects of a user entering a variant are reflected in future steps in a preview.

Similarly, filters will recognize actions that occurred as a result of the test user interacting with other steps in the Canvas. For example, this preview mode recognizes that a user encountered a Message step that was “sent” earlier in the Canvas, and it will recognize that the test user “took action” to advance through an action path.

Refer to [Exit criteria]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria) for more details on responsive behavior.

## Connected Content

Connected Content will be executed if it’s included in the Canvas. This means if you test a Canvas that has Connected Content calls or Content Blocks that contain Connected Content, the Canvas may send the Connected Content calls, which would modify the data referenced in other campaigns or Canvases.

When previewing user paths, consider removing the Connected Content that alters user profiles or data referenced in other Canvases or campaigns.

## Webhooks

Webhooks will execute when test messages are sent, but not during the test run. Similar to Connected Content, consider removing webhooks that alter user profiles or data referenced in other Canvases or campaigns.

## Use case

In this scenario, the Canvas is set up to target users who haven't had a session in an app. This journey includes a Message step with a welcome email, a Delay step set for one day, and an Audience Paths step that splits into two paths: users with at least one session, and everyone else. Depending on which audience path a user falls into, the subsequent Message step will be sent.

![An example of a Canvas with a Message step, Delay step, Audience Paths step, and two Message steps.]({% image_buster /assets/img/preview_user_path_example.png %}){:style="max-width:70%"}

Because our test user meets the Canvas entry criteria, they can enter the Canvas and go through the user journey. However, because our test user hasn't opened the app in the last calendar day, they will continue down the "Everyone else" path and receive a push notification that reads: "Last chance! Complete your first task for an exclusive bonus."

![The "Test Results" section shows that the test user has met the entry criteria and provides a summary of their journey, including which steps they were sent.]({% image_buster /assets/img/preview_user_path_results_example.png %})

