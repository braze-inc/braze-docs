---
nav_title: Active user campaigns
article_title: Active User Campaigns
page_order: 0.5
page_type: tutorial
description: "This how-to article describes the benefits of active user campaigns within the Braze dashboard and the steps to create and set up one."
tool: 
  - Campaigns

---

# Active user campaigns

> Identify your active users to help you make tailored campaigns and reward those who frequent your platform. 

Reaching out to already-active users of your app can be a powerful tool in helping to build a dedicated following of consistent app users. A little bit of personalized recognition of your power users can turn them into evangelists for your app.

You can also check out our [Braze Learning course](https://learning.braze.com/quick-overview-segment-and-campaign-setup) on marketing strategy for email and recommended lifecycle campaigns!

## Understanding active users

Braze defines an "active user" for a given period of time as any user who has a session in that time period.

If a user loses connectivity, we will cache the session data locally and upload it when the user regains a network connection. These sessions will also be applied to the active user count. Additionally, if your app has a registration process, Braze will count all users as active—registered or unregistered.

If you set User IDs to identify users when a new user logs in they will be counted as a separate active user. Users who are updated via the API will also be counted as an active user in the time period that they are updated.

## Step 1: Identifying your top users

Using our selection of filters, create a user segment that you feel encompasses your most loyal, consistent user base. The following sample segment defines the top users.

![]({% image_buster /assets/img_archive/define_top_users.png %} "Define your top users")

Additionally, you will not have to continue updating this segment, as users who pass in or out of the campaign's restrictions will be correspondingly targeted or dismissed.

{% alert note %}
The preceding example segments users by general app usage. In most cases, the total collection of filters needed to define your top user segment will largely be defined by the specifics of your app.
{% endalert %}

## Step 2: Reach out to your top users

### Make your users feel appreciated

Make your users feel appreciated by thanking them for their loyalty and dedication to your app. Give your users more reasons to keep coming back to your app to encourage further activity. This can take the form of special deals or bonuses exclusively for your top users. 

Unexpected rewards can be more effective at encouraging continued user actions than if you had promised them from the start!

![A campaign in the Compose step with an iOS rich notification that reads: "Thanks again for shopping with us! To show our appreciation, we're giving you free shipping on your next purchase".]({% image_buster /assets/img/congratulations_push.jpg %})

### Keep track of your results

Keep track of opens to ensure that you are targeting the proper collection of users with the optimal message type. Additionally, keep track of any push opt-outs and be wary of losing these crucial users.

