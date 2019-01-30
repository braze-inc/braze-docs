---
nav_title: In-App Messages In Canvas
platform: Canvas
subplatform: Create a Canvas
page_order: 2
---

# In-App Messages In Canvas

In-app Messages in canvas are now in Beta. If you’re interested in participating in the beta program, please contact your customer success manager or Braze’s support team.

## Adding an In-App Message to Canvas

In-app messages can be included in any Canvas step. Please note that in app messages from canvases can only be displayed at session start. In-app message steps triggered off of custom events will not display in real time when the user completes the event. After completing the trigger event, your users will be eligible to receive the associated in-app message on their next session start.

## Canvas Step Advancement

In some canvases, a customer will be eligible to receive a particular in-app message and the in-app message will never display for them.

This scenario could occur if a customer does not open the app during the in-app message’s availability window or if higher priority in-app messages display when the user opens their app. Note that eligibility means that a customer **could** get a particular message if they open their app - it does not mean that the in-app message actually displays for that customer.

Braze considers an in-app message as “sent” as soon as the user becomes eligible for the in-app message. As such, a user advances to subsequent canvas steps as soon as they are eligible to receive an in app message (or actually receive an email, push or webhook) from previous step.

More specifically, if a canvas step includes an in-app message, users will advance to the next step if they:

- Meet the segmentation criteria for the current step as well as the subsequent step
- Do not perform exception events for the current step before in-app message eligibility begins

To summarize, once a user becomes eligible for an in-app message in a canvas step, advancement to the next step is guaranteed.

## In-app Message Availability Window

The availability window controls the duration of in app message eligibility. The maximum length of the availability window is 14 days.

![availability][43]

## In-app Message Eligibility Options

You can choose whether you’d like the in-app message to be displayed in the event that the customer has received messages from subsequent steps. By default, customers will not receive in-app messages from previous steps once they’ve received a message from a subsequent step.

![eligibility][44]

## Setting Message Priority

It is possible that a customer will trigger two in-app messages within your Canvas at the same time. When this occurs, Braze will follow the priority order below to determine which in-app message is displayed. Drag different Canvas steps to re-order their priority. By default, steps earlier in a Canvas variant will display before later steps.

![step_priority][45]

Navigate to the “send settings” of the canvas section to prioritize in-app messages from a canvas against in-app messages from other canvases and campaigns.

By default, canvas step priority is set to medium with the most recently created steps having the highest relative priority. Canvas/campaign level priorities also default to medium with the highest relative priority defaulting to the most recently created items.

![canvas_priority][46]


[43]: {% image_buster /assets/img_archive/window.png %}
[44]: {% image_buster /assets/img_archive/eligibility.png %}
[45]: {% image_buster /assets/img_archive/step_priority.png %}
[46]: {% image_buster /assets/img_archive/canvas_priority.png %}
