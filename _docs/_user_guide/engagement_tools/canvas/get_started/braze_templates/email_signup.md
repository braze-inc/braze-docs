---
nav_title: Email sign-up with double opt-in
article_title: Email Sign-Up with Double Opt-In
page_order: 2
page_type: reference
description: "This article describes how to use a Braze Canvas template to expand your reach with verified email sign-ups."
tool: Canvas
---

# Email sign-up with double opt-in

> Use the email sign-up with double opt-in template to expand your reach with verified email sign-ups. Target new users to capture their email, confirm their subscription, and receive a promotion code, all in one seamless journey.

This article will walk you through a use case for the **Email sign-up with double opt-in** template, which is designed for the consideration stage of the user lifecycle. When you’re finished, you’ll have created a Canvas that sends emails and in-app messages to users when they start a session or when they haven't completed their onboarding.

## Prerequisites

To successfully use this template, you need the following:

- A [multi-page in-app message]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page) with one page to capture your users' emails and another to communicate a success message. 
- A confirmation email for users to verify their email address.
- A welcome email with an exclusive promotion code for users who double opt-in.

## Tailoring the template to your needs

Let’s say you're working for Steppington, a health app known for its features such as calorie tracking, digital exercise classes, and flash-mob marathons. Before creating the Canvas, you [set up multi-page in-app and in-browser messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page) that includes a series of engaging questions to determine the experience and impression of a user's first ride with the app.

To access the template, when creating a new Canvas, select **Use a Canvas template** > **Braze templates**. Then, next to **Email sign-up with double opt-in**, select **Apply Template**. Now, we can go through the template to fit it for our needs.

### Step 1: Set up the details

Adjust the Canvas details to reflect your goal.

1. Select **Edit** next to the template name.

![The current title and description of the Canvas.]({% image_buster /assets/img/canvas_templates/email_signup1.png %}){: style="max-width:50%;"}

{:start="2"}
2. Update the Canvas name to specify that the Canvas is for targeting new users when they first use the app.
3. Update the description to explain that this Canvas contains personalized messaging for users to double-opt in.
4. Add the tag **Email** so that we can filter for it on the Canvas home page.

![The new name, description, and tag for the Canvas.]({% image_buster /assets/img/canvas_templates/email_signup2.png %}){: style="max-width:90%;"}

### Step 2: Assign conversion events

Next, assign our conversion events. Conversion events are a type of metric that you can use to measure the success of the Canvas. For **Conversion event type**, select **Performs Custom Event**. Then, select **email_opt_in** for the **Custom event name**.

!["Assign Conversion Events" section for the conversion event type of opting in for email.]({% image_buster /assets/img/canvas_templates/email_signup3.png %}){: style="max-width:90%;"}

Keep the template's conversion deadline of three days because you want to target your most recent users.

### Step 3: Tailor the entry schedule

Keep the entry schedule as **Action-Based** so that users enter your Canvas when they start a session in the app. This way, you can begin to build your relationship with timely engagement.

Also, consider keeping the **Action Based Options** as is so that users enter the Canvas only when they start a session.

![An action-based entry schedule to enter users who start any session into the Canvas.]({% image_buster /assets/img/canvas_templates/email_signup4.png %}){: style="max-width:90%;"}

For the **Entry Window**, update the **Started Time (Required)** to our desired date and time.

![An entry window with the start time January 16, 2025 at 12:30 pm. Users will enter this message in their local time zone.]({% image_buster /assets/img/canvas_templates/email_signup5.png %}){: style="max-width:90%;"}

### Step 4: Select the target audience

Define your target audience as Steppington users who don't have an email address in their user profile by keeping the template's default [segmentation filter]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) `Email Available is false`.

![Entry Audience with the "Email Available is false" filter.]({% image_buster /assets/img/canvas_templates/email_signup6.png %}){: style="max-width:90%;"}

### Step 5: Select your send settings

Keep the default subscription settings, so you send only to users who have subscribed or opted in to receiving messages or notifications, and skip the other settings (frequency capping, quiet hours, and seed groups).

![Default sending options to only send to users who are subscribed or opted-in.]({% image_buster /assets/img/canvas_templates/email_signup7.png %}){: style="max-width:90%;"}

### Step 6: Customize your Canvas

Next, build the Canvas by customizing the channels and content that you want to send to users. Because you're focusing on verifying email sign-ups, you don't need to add or remove any of the template's Canvas steps and channels.

1. Select the first Message step named **Email Sign-up**. This is where you update the template to use our multi-page in-app (and in-browser) message.

- Page 1 captures the emails.
- Page 2 displays a confirmation message.

![Two pages of an in-app message to capture user emails and display a success message.]({% image_buster /assets/img/canvas_templates/email_signup8.png %}){: style="max-width:90%;"}

{:start="2"}
2. From here, keep the **Subscribed** Action Path step as is. This step splits our users into two groups in a one-day window:

- Users who have subscribed to Steppington with their email
- Users who haven't subscribed to Steppington with their email

{:start="3"}
3. Next, replace the email body with our branded confirmation email for the **Verify Email** Message step. This will send an email to our subscribed users and prompt them to confirm their email address and opt in to our messaging.
4. Keep the **Confirm Subscription** Action Path step as is. This step further splits our users into those who have confirmed their email and those who have not, with a one-week window.
5. Lastly, update the **Welcome + Discount** Message step with our confirmation email that includes an exclusive promotion code.

{% alert note %}
The **Verify Email** Message step is triggered on the user's second session. This is because the first session start event would trigger the Canvas, but a second session start after the user has reached the first **Email Sign-up** Message step is required for the user to be eligible to trigger the second in-app message.
{% endalert %}

### Step 7: Test and launch your Canvas

After testing and reviewing your Canvas to make sure it works as expected, launch it by selecting **Launch Canvas**.

{% alert tip %}
Check out our [Pre and post-launch checklist]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) for things to consider before and after you launch a Canvas.
{% endalert %}
