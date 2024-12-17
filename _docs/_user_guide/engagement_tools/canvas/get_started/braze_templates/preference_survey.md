---
nav_title: Collect User Preferences
article_title: Collect User Preferences
page_order: 2
page_type: reference
description: "This article describes how to use a Braze Canvas template to drive early adoption with a guided onboarding flow to introduce new users to your brand and collect preferences to keep them engaged long-term."
tool: Canvas
---

# Onboarding with preferences survey

> Use the onboarding with preferences survey template to create a guided onboarding workflow that target new users. Introduce them to your brand, help them get started, and collect their preferences to keep them engaged long-term.

This article will walk you through a use case for the **Onboarding with preferences survey** template, which is designed for the consideration stage of the user lifecycle. When you’re finished, you’ll have created a Canvas that sends emails and in-app messages to users when they start a session or when they haven't completed their onboarding.

## Prerequisites

To successfully use this template, you'll need the following:

- A [survey]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/templates/simple_survey) containing multiple questions to determine user preferences.

## Tailoring the template to your needs

Let’s say we’re working for StyleRyde, an on-demand ridesharing app that gets people where they need to go. Before creating the Canvas, we [set up a simple survey]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog) that includes a series of engaging questions to determine the experience and impression of a user's first ride with the app.

To access the template, when creating a new Canvas, select **Use a Canvas template** > **Braze templates**. Then, next to **Onboarding with preferences survey**, select **Apply Template**. Now, we can go through the template to fit it for our needs.

### Step 1: Set up the details

Let’s adjust the Canvas details to reflect our goal.

1. Select **Edit** next to the template name.

{:start="2"}
2. Update the Canvas name to specify that the Canvas is for targeting new users when they first use the app.
3. Update the description to explain that this Canvas contains personalized messaging.
4. Add the tag **Onboarding** so that we can filter for it on the Canvas home page. 

### Step 2: Assign conversion events


### Step 3: Tailor the entry schedule

Let’s keep the entry schedule as **Action-Based** so that users will enter our Canvas when they start a session in the app.

### Step 4: Select the target audience

We’ll define our target audience as users who have used the rideshare app for the first time.

### Step 5: Select your send settings

We’ll keep the default subscription settings, so we only send to users who have subscribed or opted into receiving messages or notifications, and skip the other settings (frequency capping, quiet hours, and seed groups).


### Step 6: Customize your Canvas

Now, we’ll build our Canvas by customizing the channels and content that will send to users. Because we’re using all four of the template channels (mobile and web push, SMS, and email) and using the [Intelligent Channel]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/) filter, we don’t need to add or remove any.

We’ll begin our customization by going through each Message step to update the content.


### Step 7: Test and launch your Canvas

After testing and reviewing our Canvas to make sure it works as expected, we’ll launch it by selecting **Launch Canvas**.

{% alert tip %}
Check out our [Pre and post-launch checklist]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) for things to consider before and after you launch a Canvas.
{% endalert %}