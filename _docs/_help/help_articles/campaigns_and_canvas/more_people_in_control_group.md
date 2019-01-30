---
nav_title: Why is my control group so large?
page_order: 3
---

# Why Is My Control Group So Large?

When you created your Canvas, you may have expected your audience to split evenly between your Control Group and your Variant, like in [our example](#example) below. We can explain why that is an how to fix it!

Which group a user joins (either the Control Group or a Variant group) depends on their settings. A user will enter a Canvas when they fit all of your criteria defined in the [Entry Step][1]. When setting up your Canvas, you define what percentage of users will enter each variant and the control group.

If your control group is large compared to your variant group (and this is not your intent), we recommend that you:

* [Set Entry Audience Push status](#set-entry-audience-push-status)
* [Set Entry Audience Email status](#set-entry-audience-email-status)


When creating a Canvas with a control group, ensure that all users in the Entry Audience are able to receive messages within the Canvas - i.e. the Canvas contains push and email messages.

### Set Entry Audience Push Status

Set your entry audience filter to ‘Is Push Enabled’.

### Set Entry Audience Email Status

Set your entry audience filter to 'is Opted In or Subscribed’.


## Example

Let’s imagine the following scenario:
- A Canvas has a single __variant__ and a __control group__.
- The first step of the __variant__ is a push notification.
- 90% of users were selected to enter the __variant__, and 10% to enter the __control group__.

![trouble15][41]

In this scenario, 90% of the users who enter the Canvas should enter the variant. However, this is not the outcome because only users who are **eligible to receive a push notification** enter the variant.

If we look back to the Entry Audience (active users), we can see that even though it contains 39.8k users, only 29.1k (73%) of them are Push Enabled:

![trouble16][42]

This means that even though we specified 90% of users to enter the variant, not all of those users are actually **able to** receive a push notification. This means that those users will not be able to enter the variant and will default to the control group.

Still need help? [Open a support ticket]({{ site.baseurl }}/docs/support_contact/).

[1]: {{site.baseurl }}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2-use-the-entry-wizard-to-set-up-your-canvas
[41]: {% image_buster /assets/img_archive/trouble15.png %}
[42]: {% image_buster /assets/img_archive/trouble16.png %}
