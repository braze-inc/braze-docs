---
nav_title: Lapsed user
article_title: Lapsed User
page_order: 4
page_type: reference
description: "This article describes how to use a Braze Canvas template to bring users back to your app with incentives based on their past engagements."
tool: Canvas
---

# Lapsed user

> Use the lapsed user template to remind users of the value your brand brings to them, and encourage their return with exciting offers and incentives based on their past engagements.

This article will walk you through a use case for the **Lapsed User** template, which is designed for the retention and loyalty step of the user lifecycle. When you’re finished, you’ll have created a Canvas that encourages users to return to your app with promotions that vary based on their behavior, such as whether they started a session in your app after receiving a promotional message.

## Prerequisites

To successfully use the lapsed user template, you need to configure [Braze Audience Sync]({{site.baseurl}}/partners/canvas_audience_sync/) with the partners and audiences you use.

## Tailoring the template to your needs

Let’s say we’re working for MovieCanon, a streaming service that has exclusive content for movies and shows. We can use the lapsed user template to promote perks and premium content for users who haven’t visited our app in 30 days.

Before creating the Canvas, we set up the [Braze Audience Sync to Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) integration so that we can add user data from Braze to Google Audiences to send advertisements based on behavioral triggers, segmentation, and more.

To access the lapsing user template, when creating a new Canvas, select **Use a Canvas template** > **Braze templates**. Then, next to **Lapsing User**, select **Apply Template**. Now, we can go through the template to fit it for our needs.

### Step 1: Set up the details 

Let’s adjust the Canvas details to reflect our goal.

1. Select **Edit** next to the template name.

![The current title and description of the Canvas.]({% image_buster /assets/img/canvas_templates/lapsed_user_old_name_description.png %}){: style="max-width:45%;"}

{:start="2"}
2. Update the Canvas name to specify that this Canvas will message users with promotions and do an audience sync for those who start a session.
3. Update the description to explain that this Canvas contains perks and promotions.
4. Add the tag **Lapsing/Retention** so that we can filter for this Canvas on the Canvas home page.

!["Set Up Canvas Details" step with Canvas name of "Lapsed User - Visit App" and a brief Canvas description]({% image_buster /assets/img/canvas_templates/lapsing_user_1.png %})

### Step 2: Assign your conversion events

Update **Primary Conversion Event - A** to target users from our app (MovieCanon), and leave **Primary Conversion Event - B** as the default of making any purchase.

!["Assign Conversion Events" section with a primary conversion even of a user starting a session in a specific app.]({% image_buster /assets/img/canvas_templates/lapsing_user_2.png %})

### Step 3: Tailor the entry schedule

Let’s keep the entry schedule as **Scheduled** and the default time-based options, so that the Canvas checks for lapsed users daily.

We’ll make two adjustments to this step: 

1. Select a start date and time.
2. Select ending parameters of **On a specific date** and a date two months out. Let’s say we have another lapsing user Canvas we want to start after this one.

!["Entry Schedule" step for a scheduled Canvas that enters users at a designated time.]({% image_buster /assets/img/canvas_templates/lapsing_user_3.png %})

### Step 4: Select our target audience

We’ll keep the default settings for the entry audience, which is set to users who haven’t used our app in over 30 days. We’ll also keep the default entry controls so that users can re-enter the Canvas after four weeks. This means every time a user doesn’t visit our app for over 30 days straight, they’ll be entered into the Canvas.

!["Target Audience" step targeting users who last used the apps in 30 days.]({% image_buster /assets/img/canvas_templates/lapsing_user_4.png %})

### Step 5: Select your send settings

We’ll keep most of the default subscription settings:

- Only send to users who have subscribed or opted into receiving messages or notifications.
- Apply our [frequency capping rules]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) so that we don’t overwhelm our audience with how many messages they receive. In this case, we set our frequency capping to limit the number of campaigns or Canvas steps tagged with “Lapsing/Retention” that a user can receive to two every week.
- Don’t send messages during quiet hours in the user's local time (12 am to 8 am).

The only setting we’ll change is what to do when a message triggers during quiet hours. Instead of cancelling the message, select **Send at next available time** so that our users don’t miss out on any promotions.

!["Quiet Hours" section with a start time of 12 am and end time of 8 am.]({% image_buster /assets/img/canvas_templates/lapsing_user_5.png %})

### Step 6: Customize your Canvas

Now, we’ll build our Canvas by customizing the templated steps:

1. Customize the first email that will send to all users who haven’t visited our app in over 30 days. For our use case, we’ll customize an email that tells users they’ll unlock new perks when they visit our app today. 

![Canvas Message step for an email that tells users to unlock new perks when they visit today.]({% image_buster /assets/img/canvas_templates/lapsing_user_6.png %})

{: start="2"}
2. Customize the action path component called “Start Session?” by selecting our app for the **Started Session** path. 

![Action path for sessions that are started in a specific app.]({% image_buster /assets/img/canvas_templates/lapsing_user_7.png %})

{: start="3"}
3. Keep the default for the Decision Split step called “Sessions?”, which defines the “>1 Session” group as users who’ve used our app more than once in the last calendar day.
4. Customize the Message step for users who fall into the “>1 Session” group. In our use case, we’ll thank users for visiting our app and highlight perks that they’ve unlocked.
5. Make sure our Google Audience sync is set up in the Ad Audience Update step, so that we update and sync the user data of users who had multiple sessions after receiving our first email.
6. Keep the default for the [Experiment Path]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step#experiment-paths) component called “A/B Test”. This will randomly send one of two promotions (that we will customize in the next step) to users who’ve had fewer than two sessions.
7. Customize the two promotions that will send to users as part of the Experiment Path. In our use case, we’ll make one a 20% promotion for a three-month subscription and the other a 10% promotion for a one-month subscription.

![Canvas steps with branching paths based on how many sessions a user had.]({% image_buster /assets/img/canvas_templates/lapsing_user_8.png %}){: style="max-width:70%;"}

### Step 7: Test and launch the Canvas

After testing and reviewing our Canvas to make sure it works as expected, we’ll launch it by selecting **Launch Canvas**. Now our users who haven’t visited our app in over 30 days and have subscribed to our messaging channels will receive emails encouraging them to return!

{% alert tip %}
Check out our [Pre and post-launch checklist]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) for things to consider before and after you launch a Canvas.
{% endalert %}

