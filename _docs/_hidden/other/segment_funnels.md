---
nav_title: Segment funnels
permalink: /segment_funnels/
hidden: true
page_type: reference
---

# Segment Funnels

> Segment funnels are great for narrowing your audience for a specific campaign use case, learning about that audience and their interactions, and using that knowledge to strategize and develop effective campaigns.

Segment funnels allow you to see how each added filter impacts your segment statistics. When creating a segment, a row of data will appear under each filter. This data will provide the following information for users that are targeted by all filters up to that point:

- Total number of users targeted and the percentage of your audience base
- LTV and LTV for paying users  
- Number of users emailable
- Number of users opted in to email
- Number of users that are push enabled  
- Number of users opted in to push

![]({% image_buster /assets/img_archive/segment_funnel_example.png %})

## Best practices

- By adding filters that document your user flow, you can see the points where users fall off. For instance, if you're a social networking app and you want to see where you might be losing users during your onboarding process, you may want to add custom data filters for signing up, adding friends, and sending the first message. If you find that 85% of users are signing up and adding friends, but only 45% sent the first message, then you'll know to focus on encouraging more message sends during your onboarding and marketing campaigns.

- Segment funnels let you compare the percentage of users who commit different actions. For instance, do active users, or those with high LTV, [tend to interact more with push or email](#push-email)? To find out, create a segment of active users with one or more filters, and then see how statistics change when you add a filter for opting in to push, and when you add a filter for opting in to email.

- Analyze how LTV changes as you add filters. For active users, do those who connect to Facebook or those who connect to X (formerly Twitter) have a higher LTV? Or is LTV significantly higher for those who have connected to both? If you find, for instance, that connecting to X (formerly Twitter) has very little impact on LTV but connecting to Facebook has a large impact, you may want your marketing campaigns to focus on incentivizing Facebook connections.

## Use cases

### Impact of a specific user action on conversions {#push-email}

By analyzing the impact of a certain user action (such as adding items to a wish list) on a conversion (such as making purchases), you can answer the following questions:

- Does the user action coincide with more purchases?
- How prevalent is the user action? Should you create marketing campaigns that encourage more of that action?

For example, let's say you have a group where all users who added items to a wish list also made a purchase. Since only a small percentage of users added items to a wish list, this app may want to incentivize this behavior more through marketing campaigns.

![Segment funnel example with the following filters: "Last used these apps less than 30 days ago", "Last Added Item to Waitlist less than 30 days ago", and "Last Made Purchase less than 30 days ago" to reach 4,302 users.]({% image_buster /assets/img_archive/Wish_List_2.png %})

### Compare messaging channels

Create a segment of active users (or users with desired traits) and compare their interactions with different engagement channels, such as email and push notifications. For instance, if more loyal users are subscribed to push, you may want to spend more time on sending active user campaigns via push. However, if you find that the LTV is higher for those who are subscribed to email, you might want to prompt more active users to subscribe to email.

![Segment funnel for email example with the following filters: "Last Made Purchase less than 30 days ago", "Last used these apps less than 30 days ago", "Foreground Push Enabled is true", and "Email Subscription Status is Opted In" to reach 2,799 users.]({% image_buster /assets/img_archive/Wish_List_Email.png %})

### iOS or Android push opt-ins

This use case leverages the "Foreground Push Enabled for App" filter to target iOS or Android users that have opted-in for push.

![]({% image_buster /assets/img/seg_filter_examples/ios.png %})

![]({% image_buster /assets/img/seg_filter_examples/android.png %})

### Full push-enabled audience

This use case leverages the "Foreground Push Enabled" filter to target users that have opted-in for push.

![]({% image_buster /assets/img/seg_filter_examples/both.png %})

### Global control group of push-enabled audience

This use case leverages the "Foreground Push Enabled" and "Random Bucket #" filter to target users that are part of the global control group that have opted-in for push.

![]({% image_buster /assets/img/seg_filter_examples/global_control.png %})

### Recent purchasers

This use case leverages the "Last Made Purchase" filter to target users that last made a purchase in less than 7 days ago.

![]({% image_buster /assets/img/seg_filter_examples/recent_purchase.png %})

### Push engagement

This use case leverages the "Last Did Custom Event" filter where the custom event is "opened any push" to target users that have shown push engagement over the past 21 days.

![]({% image_buster /assets/img/seg_filter_examples/push_engagement.png %})

### Money spent in app

This use case leverages the "Money Spent" filter to target users that have spent at least 1000 dollars.

![]({% image_buster /assets/img/seg_filter_examples/moneyspent.png %})


