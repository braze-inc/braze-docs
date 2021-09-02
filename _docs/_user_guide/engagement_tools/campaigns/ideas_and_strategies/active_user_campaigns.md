---
nav_title: Active User Campaigns
article_title: Active User Campaigns
page_order: 0
page_type: tutorial
description: "This how-to article describes Active User Campaigns within the Braze dashboard and the steps to create and set up one."
tool: 
  - Campaigns

---
# Active User Campaigns

> This article will discuss the benefits of Active User Campaigns within the Braze dashboard, as well as how to identify and reach out to your top users.
> <br>
> <br>
> Knowing which users are active, or "top" users can help you make tailored campaigns and reward those who frequent your platform. 

Reaching out to already active users of your app can be a powerful tool in helping to build a dedicated following of consistent app users. A little bit of personalized recognition of your power users can turn them into evangelists for your app.

You can also check out [our LAB course](http://lab.braze.com/quick-overview-segment-and-campaign-setup) on marketing strategy for email and recommended lifecycle campaigns!

## Understanding Active Users

Braze defines an "active user" for a given period of time as any user who has a session in that time period.

If a user loses connectivity, we will cache the session data locally and upload it when the user regains a network connection. These sessions will also be applied to the active user count. Additionally, if your app has a registration process, Braze will count all users as active—registered or unregistered.

If you set User IDs to identify users when a new user logs in they will be counted as a separate active user. Users who are updated via the API will also be counted as an active user in the time period that they are updated.

## Step 1: Identifying Your Top Users

Using Braze's selection of filters, create a user segment that you feel encompasses your most loyal, consistent user base. A sample segment to define your top users is shown below.

![Define top users][1]

Additionally, you will not have to continue updating this segment, as users who pass in or out of the campaign's restrictions will be correspondingly targeted or dismissed.

{% alert note %}
The example above segments users by general app usage. In most cases, the total collection of filters needed to define your top user segment will largely be defined by the specificities of your app.
{% endalert %}

## Step 2: Reach Out to Your Top Users

### Make Your Users Feel Appreciated
Make your users feel appreciated by thanking them for their loyalty and dedication to your app. Give your users more reasons to keep coming back to your app to encourage further activity. This can take the form of special deals or bonuses exclusively for your top users. 

Unexpected rewards can be more effective at encouraging continued user actions than if you had promised them from the start!

![Congrats Push][2]

### Keep Track of Your Results
Keep track of opens to ensure that you are targeting the proper collection of users with the optimal message type. Additionally, keep track of any push opt-outs and be wary of losing these crucial users.

[1]: {% image_buster /assets/img_archive/define_top_users.png %} "Define your top users"
[2]: {% image_buster /assets/img/congratulations_push.jpg %}