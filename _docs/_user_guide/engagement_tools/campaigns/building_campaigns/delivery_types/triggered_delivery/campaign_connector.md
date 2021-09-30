---
nav_title: Campaign Connector
article_title: Campaign Connector
page_order: 2
tool: Campaigns
page_type: tutorial
description: "This how-to article goes over what Braze's Campaign Connector is and how to use it to deliver targeted, relevant content at the right time."

---
# Campaign Connector

> This how-to article goes over what Braze's Campaign Connector is and how to use it to deliver targeted, relevant content at the right time.

## Overview

Braze's Campaign Connector allows you to create campaigns that are triggered when users interact with active campaigns or News Feed Cards. This feature is useful because it enables you to deliver targeted, relevant content at the right time. This feature allows you to target users who complete the following interactions with active campaigns:

- View in-app message
- Click in-app message
- Click e-mail
- Open e-mail
- Directly open push notification
- Perform conversion event
- Receive e-mail
- Receive push notification
- Are enrolled in a control group

As well as users who complete the following interactions with active News Feed Cards:

- View
- Click

## Delivery Rules

The Campaign Connector feature only works with active campaigns. In addition, you cannot use Campaign Connector to send a message to a user after they have completed an interaction with a campaign. For example, if you are a running a marketing campaign for 9 weeks and you set up a follow-on campaign that utilizes Campaign Connector at the beginning of week 4, the follow-on campaign will only deliver messages to users that interacted with the marketing campaign after the follow-on campaign was published (weeks 4-9). Therefore, in order to ensure that your follow-on campaigns reach every user that you are targeting, you should:

- Set up your original campaign as a draft
- Set up and publish your follow-on campaign
- Publish the original campaign

These delivery rules are particularly pertinent if you are targeting users who are enrolled in a control group, receive an email or receive a push notification. Because users will be enrolled in the control group as soon as you publish the original campaign, you must publish the follow-on campaign before you publish the original campaign. Similarly, if you publish the original campaign before the follow-on campaign, many users may receive your email and/or push notification before the follow-on campaign is published.

## How to Use the Campaign Connector Feature

### Step 1: Create a New Campaign
Compose the messages that you wish to send to your users. You can select a classic campaign or a single channel campaign, depending on your use case.

### Step 2: Select Interaction and Target Campaign

You can target users who interact with an active campaign, or users who interact with an active News Feed Card.

#### Targeting Users Who Interact with a Campaign
Select [action-based delivery][7] and add the "Interact with Campaign" trigger. Then, choose the trigger interaction. Next, you’ll select the active campaign that you’d like to target.

![Interact with Campaign][4]

#### Targeting Users Who Interact with a News Feed Card

Select action-based delivery and add the "Interact with Card" trigger. Then choose whether you’d like to target users who view a News Feed Card or users who click a News Feed Card. Select the active News Feed Card that you’d like to target.

![Interact With Card][5]

### Step 3: Set Schedule Delay and Add Exceptions If Necessary

If you choose to set a schedule delay, you can add an exception to the trigger action. For example, you might want to resend an email campaign to users who did not open the original e-mail.  In this scenario, you can choose "Received e-mail" as the trigger and set a schedule delay of one week. Then you can add "Open e-mail" as an exception. Now, you’ll resend the email to users who did not open the original email within a week of receiving it.

![Schedule Delay][6]

Exception events will only trigger while a user is waiting to receive the message it’s associated with. If a user performs the action before waiting for the message, the exception event will not trigger.


### Step 4: Proceed with Campaign Creation

Continue creating your campaign just as you normally would. Note that if you want to ensure that you send a message to every user that is going to interact with a specific campaign, then it would be best to target a segment that contains all of the users of your app.

## Use Cases

You can use Campaign Connector to target users who engage or do not engage with active campaigns.

For example, you might choose to target users who clicked on a promotional push message that advertised free shipping so that you can send them a promotional push message advertising 15% off a purchase.

Or, you might follow up with users who clicked a deep link in an onboarding in-app message by sending them another in-app message that highlights additional features.  This way, you can target users that have demonstrated that they are interested in learning more about the features of your application and avoid annoying the users that prefer to discover these features by themselves.

You can also use this feature to target users who receive a push notification reminding them that they have abandoned their cart. For example, you might want to resend the notification to users who did not directly open it. However, you'll likely want to exclude users that have made a purchase since you send the original notification, even if they did not directly open it. You can achieve this use case by adding a "Received push notification" trigger for the campaign "Abandoned Cart," setting a schedule delay and adding ‘Makes Purchase' and 'Directly opened push notifications' as exceptions.

[4]: {% image_buster /assets/img_archive/Campaign_Connector1.png %}
[5]: {% image_buster /assets/img_archive/Campaign_Connector2.png %}
[6]: {% image_buster /assets/img_archive/Campaign_Connector3.png %}
[7]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/
