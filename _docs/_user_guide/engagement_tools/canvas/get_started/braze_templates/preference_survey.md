---
nav_title: Onboarding with preferences survey
article_title: Onboarding with Preferences Survey
page_order: 5.5
page_type: reference
description: "This article describes how to use a Braze Canvas template to drive early adoption with a guided onboarding flow to introduce new users to your brand and collect preferences to keep them engaged long-term."
tool: Canvas
---

# Onboarding with preferences survey

> Use the onboarding with preferences survey template to create a guided onboarding workflow that target new users. Introduce them to your brand, help them get started, and collect their preferences to keep them engaged long-term.

This article will walk you through a use case for the **Onboarding with preferences survey** template, which is designed for the consideration stage of the user lifecycle. When you’re finished, you’ll have created a Canvas that sends emails and in-app messages to users when they start a session and when they haven't completed their onboarding.

## Prerequisites

To successfully use this template, you'll need the following:

- A welcome email that prompts users to begin onboarding.
- A followup email that includes tips to get started with the app for users who onboarded.
- A followup email to prompt users to complete their onboarding.
- A [survey]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/templates/simple_survey) containing multiple questions to determine user preferences.

## Tailoring the template to your needs

Let’s say we’re working for StyleRyde, an on-demand ridesharing app that gets people where they need to go. Before creating the Canvas, we [set up a simple survey]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog) that includes a series of engaging questions to determine the experience and impression of a user's first ride with the app.

To access the template, when creating a new Canvas, select **Use a Canvas template** > **Braze templates**. Then, next to **Onboarding with preferences survey**, select **Apply Template**. Now, we can go through the template to fit it for our needs.

### Step 1: Set up the details

Let’s adjust the Canvas details to reflect our goal.

1. Select **Edit** next to the template name.

![The current title and description of the Canvas.]({% image_buster /assets/img/canvas_templates/preference_survey1.png %}){: style="max-width:50%;"}

{:start="2"}
2. Update the Canvas name to specify that the Canvas is for targeting new users when they first use the app.
3. Update the description to explain that this Canvas contains personalized messaging.
4. Add the tag **Onboarding** so that we can filter for it on the Canvas home page.

![The new name, description, and tag for the Canvas.]({% image_buster /assets/img/canvas_templates/preference_survey2.png %}){: style="max-width:90%;"}

### Step 2: Assign conversion events

Update the **Primary Conversion Event - A** to **Performs Custom Event**. Then, select **Last Used App** for the custom event.

![Last Used App as the selected custom event name for the conversion event.]({% image_buster /assets/img/canvas_templates/preference_survey3.png %}){: style="max-width:90%;"}

### Step 3: Tailor the entry schedule

Let’s keep the entry schedule as **Action-Based** so that users will enter our Canvas when they start a session in the app. This way, we can begin to build our relationship with timely engagement.

We'll make one update to this section by adjusting the **Entry Window** to our desired date and time.

!["Entry Window" section with the start time January 30, 2025 at 12 pm.]({% image_buster /assets/img/canvas_templates/preference_survey4.png %}){: style="max-width:90%;"}

### Step 4: Select the target audience

We’ll keep the target audience as is to target our users who first used the StyleRyde app less than one day ago.

![The "First used these apps less than 1 days ago" filter selected to target the entry audience.]({% image_buster /assets/img/canvas_templates/preference_survey5.png %}){: style="max-width:90%;"}

### Step 5: Select your send settings

We’ll keep the default subscription settings, so we only send to users who have subscribed or opted into receiving messages or notifications with Quiet Hours turned on, and skip the other settings (frequency capping and seed groups).

!["Send Settings" section with the subscription settings for users who are subscribed or opted-in with Quiet Hours turned on between 12 am and 8 pm.]({% image_buster /assets/img/canvas_templates/preference_survey6.png %}){: style="max-width:90%;"}

### Step 6: Customize your Canvas

Now, we’ll build our Canvas by customizing the content that will send to users. 

1. For the first Message step **Welcome Email**, we'll update this step to include our StyleRyde welcome email.
2. Next, we'll keep the Action Path step as is. This step splits our users into two groups in a three-day window:

- Users who have started a session or clicked the onboarding email
- Users who haven't started a session or clicked the onboarding email

![An Action Path step split into two paths, with one for users who have started a session and another for everyone else.]({% image_buster /assets/img/canvas_templates/preference_survey8.png %}){: style="max-width:50%;"}

From here, we'll target our users and messaging based on the aforementioned groups.

#### Target your engaged users

For our users who have started a session or engaged with our onboarding email from the first Message step, we'll update the **Getting Started Tips** Message step to include the essential travel and safety tips for our new StyleRyde users.

After a user completed their onboarding, they'll exit the Canvas.

Next, update the **Content Preferences Survey** Message step to include our preferences survey that prompts our users to select what topics they're interested in receiving information on in the future.

![A preview of the preferences survey that prompts users to select all interests that apply.]({% image_buster /assets/img/canvas_templates/preference_survey7.png %}){: style="max-width:90%;"}

#### Nudge users who haven't started onboarding 

For our other users, we'll update the **Winback Nudge** Message step with our followup email to prompt users to complete their onboarding.

As our last step for re-engagement, we'll rename **Step 2** to **Final Winback Nudge** and update the step with our in-app message to prompt our new users to complete their onboarding.

### Step 7: Test and launch your Canvas

After testing and reviewing our Canvas to make sure it works as expected, we’ll launch it by selecting **Launch Canvas**.

{% alert tip %}
Check out our [Pre and post-launch checklist]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) for things to consider before and after you launch a Canvas.
{% endalert %}