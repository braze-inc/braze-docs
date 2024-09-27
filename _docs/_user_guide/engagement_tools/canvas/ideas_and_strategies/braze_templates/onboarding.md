---
nav_title: Onboarding
article_title: Onboarding
page_order: 5
page_type: reference
description: "This article describes use a Braze Canvas template to create onboarding journeys that promote strong initial adoption and encourage lasting relationships with your users."
tool: Canvas
---

# Onboarding

> Start your users' journey with this onboarding template. This template is designed to promote strong initial adoption and encourage lasting relationships with your users. By leveraging personalized communication and a structured set of messages, you can seamlessly introduce your users to your brand and initiate the beginning of a lasting relationship.

In this article, we'll walk you through a use case for the **Onboarding** template, which is intended for the consideration stage of the user lifecycle, to create a seamless onboarding journey for new users. After this article, you'll have customized this Braze Canvas template with personalized messages for these new users.

## Prerequisites

Before using this template, we created [email templates]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template) to reference in this Canvas:

- A welcome email to all users of our app
- An email with tips on how to use our app
- A feedback email that includes a user survey

To access this template, when creating a new Canvas, select **Use a Canvas template** > **Braze templates** > **Onboarding**.

## Tailoring the template to your needs

Let's say you're a marketer at PantsLabyrinth, and your goal is to enhance user engagement, build trust and loyalty with your users, and encourage them to stay engaged. To do so, you want to focus on crafting messages that target new users who have yet to interact with your app. Let's begin to customize this template to fit our use case.

### Step 1: Set up details and assign your conversion events
In the template:

1. Update the Canvas name to specify that the Canvas is for onboarding new users.
2. Update the description to specify that the Canvas maps out a user journey that promotes trust and loyalty with users.
3. Add the tag **Onboarding**, so that we can filter for it on the Canvas home page.

Next, let's assign our conversion events. Conversion events are a type of success metric that can be used to measure the success of the Canvas. The onboarding template has the following [conversion event]({{site.baseurl}}//user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/#primary-conversion-event) to get you started.

![][1]

So, new users have up to four days to perform the custom event. In this case, you want your new users to feel a sense of urgency to engage with PantsLabyrinth and subscribe to a recurring delivery on seasonal clothing.

### Step 2: Set an entry schedule

Because your goal is to target new users of PantsLabyrinth, you'll keep the Canvas as action-based and allow users who start a session in the app to enter the Canvas. However, you could further evaluate if a user has taken any specific actions such as making a purchase.

Next, adjust the **Entry Window** to determine when users can enter the Canvas. Let's say there's an upcoming PantsLabyrinth subscription launch in late-October. This is where you'll set the start time as **2024/10/28 8:00 am**. Optionally, you can also let users enter the Canvas in their local time zone.

![][4]

### Step 3: Determine who enters the Canvas

By targeting the right audience, you can effectively engage with new users. For example, this template targets all users who first used an app less than one day ago, which is accurate for our use case. So, we'll leave this section as is.

### Step 4: Set your send settings

As the default, this Canvas is sent to users who are subscribed or opted in and follows frequency capping rules. We'll keep these settings as is.

### Step 5: Customize your Canvas

Now, we’ll build our Canvas by customizing the templated steps.

#### Set up your welcome email

1. In the Canvas builder, select the Message step named "Welcome Email".
2. Select **Edit message** to replace the template's email with your welcome email.
3. Select **Done**.

Your users will receive this welcome email after they have started a session in your app. As to not overwhelm your users with repeated messaging, we recommend using the Delay step as part of the user journey.

#### Customize your Audience Path

In the Audience Path step named "Audience Split", you can customizing the filter for your engaged users. In the template, the filter is **Has clicked email for step Welcome Email**, which means users are split into two groups: users who have opened the welcome email and those who haven't.

![][2]{: style="max-width:70%;"}

As an online clothing retailer, PantsLabyrinth also has an active group of mobile users. So, in a separate onboarding Canvas, we can also select the following filter to identify and split your mobile users into these segments:

- **Has clicked content card for step Welcome Content Card**
- **Everyone Else**

#### Target more users with Audience Paths

From the set of users who haven't interacted with your app, you can further target these users by creating another Audience Paths step. This creates another split for engaged users and everyone else. For the **Everyone Else** group, you can use a Message step to nudge these users to sign up for a subscription to PantsLabyrinth.

### Step 6: Launch your Canvas

After testing and reviewing our Canvas to make sure it works as expected, select **Launch Canvas** to launch the Canvas. Now, we can provide our new users with a personalized onboarding experience to encourage a lasting relationship!

{% alert tip %}
Check out our [Pre and post-launch checklist]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) for things to consider before and after you launch a Canvas.
{% endalert %}

[1]: {% image_buster /assets/img/canvas_templates/onboarding1.png %}
[2]: {% image_buster /assets/img/canvas_templates/onboarding2.png %}
[3]: {% image_buster /assets/img/canvas_templates/onboarding3.png %}
[4]: {% image_buster /assets/img/canvas_templates/onboarding4.png %}