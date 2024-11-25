---
nav_title: Onboarding
article_title: Onboarding
page_order: 5
page_type: reference
description: "This article describes how to use a Braze Canvas template to create onboarding journeys that promote strong initial adoption and encourage lasting relationships with your users."
tool: Canvas
---

# Onboarding

> Start your users' journey with this onboarding template. This template is designed to promote strong initial adoption and encourage lasting relationships with your users. By leveraging personalized communication and a structured set of messages, you can seamlessly introduce your users to your brand and initiate the beginning of a lasting relationship.

In this article, we'll walk you through a use case for the **Onboarding** template, which is intended for the consideration stage of the user lifecycle, to create a seamless onboarding journey for new users. After this article, you'll have customized this Braze Canvas template with personalized messages for these new users.

## Prerequisites

Before using this template, you need to create the following [email templates]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template) to reference in the Canvas:

- A welcome email to all users of your app
- An email with tips on how to use your app
- A feedback email that includes a user survey

## Tailoring the template to your needs

Let's say we're working at PantsLabyrinth, and our goal is to enhance user engagement, build trust and loyalty with our users, and encourage them to stay engaged. To do so, we want to focus on crafting messages that target new users who have yet to interact with the app.

To access the onboarding template, when creating a new Canvas, select **Use a Canvas template** > **Braze templates**. Then, next to **Onboarding**, select **Apply Template**. Let's begin to customize this template to fit our use case.

### Step 1: Set up the details

Let's adjust the Canvas details to reflect our goal.

1. Select **Edit** next to the template name.

![The current title and description of the Canvas.]({% image_buster /assets/img/canvas_templates/onboarding_old_name_description.png %}){: style="max-width:60%;"}

{:start="2"}
2. Update the Canvas name to specify that the Canvas is for onboarding new users.
3. Update the description to specify that the Canvas maps out a user journey that promotes trust and loyalty with users.
4. Add the tag **Onboarding** so that we can filter for it on the Canvas home page.

![The new name, description, and tag for the Canvas.]({% image_buster /assets/img/canvas_templates/onboarding_new_name_description.png %}){: style="max-width:60%;"}

### Step 2: Assign your conversion events

Next, let's assign our conversion events. Conversion events are a type of metric that can be used to measure the success of the Canvas. For **Custom event name**, select **Email Click** as the custom event.

![Primary Conversion Event - A with the conversion type "Performs Custom Event" with the custom event name "Email Click". There is a 4-day conversion deadline.][1]

This means new users have up to four days to click the welcome email. In this case, we want our new users to feel a sense of urgency to engage with PantsLabyrinth and subscribe to a recurring delivery on seasonal clothing.

### Step 3: Set an entry schedule

Because the goal is to target new users of PantsLabyrinth, we'll keep the Canvas as action-based. For **Start Session**, select **Start Session in Any App** to allow users who start a session in any app to enter the Canvas.

Next, adjust the **Entry Window** to determine when users can enter the Canvas. Let's say there's an upcoming PantsLabyrinth subscription launch in late-October. This is where we'll set the start time as **2024/10/28 8:00 am**. Optionally, we can also let users enter the Canvas in their local time zone.

![An entry window with the start time October 28, 2024 at 8 am. Users will enter this message in their local time zone.][4]

### Step 4: Target your audience

By targeting the right audience, we can effectively engage with new users. For example, this template targets all users who first used an app less than one day ago, which is accurate for our use case. So, we'll leave this section as is.

### Step 5: Set send settings

As the default, this Canvas is sent to users who are subscribed or opted in and follows frequency capping rules. We'll keep these settings as is.

### Step 6: Customize your Canvas

Now, let's build the Canvas by customizing the templated steps.

#### Set up the welcome email

1. Select the Message step named "Welcome Email".
2. Select **Edit message** to replace the template's email with our welcome email.
3. Select **Done**.

Now, our users will receive this welcome email after they have started a session in our app. As to not overwhelm users with repeated messaging, we recommend using the Delay step as part of the user journey.

#### Customize the Audience Path

In the Audience Path step named **Audience Split**, we can customize the filter for our engaged users. In the template, the filter is **Has clicked email for step Welcome Email**, which means users are split into two groups: users who have clicked the welcome email and those who haven't.

![An Audience Split step with one path for engaged users and one path for everyone else.][2]{: style="max-width:70%;"}

As an online clothing retailer, PantsLabyrinth also has an active group of mobile users. So, in a separate onboarding Canvas, we can also select the following filter to identify and split our mobile users into these segments:

- **Has clicked content card for step Welcome Content Card**
- **Everyone Else**

#### Target more users with Audience Paths

From the set of users who haven't interacted with our app, we can further target these users by editing the "Check for Clicks" step and "Winback Nudge" step.

### Step 7: Test and launch your Canvas

After testing and reviewing our Canvas to make sure it works as expected, select **Launch Canvas** to launch the Canvas. Now, we can provide our new users with a personalized onboarding experience to encourage a lasting relationship!

{% alert tip %}
Check out our [Pre and post-launch checklist]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) for things to consider before and after you launch a Canvas.
{% endalert %}

[1]: {% image_buster /assets/img/canvas_templates/onboarding1.png %}
[2]: {% image_buster /assets/img/canvas_templates/onboarding2.png %}
[3]: {% image_buster /assets/img/canvas_templates/onboarding3.png %}
[4]: {% image_buster /assets/img/canvas_templates/onboarding4.png %}