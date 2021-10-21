---
nav_title: Segment Funnels
article_title: Segment Funnels
page_order: 3

page_type: reference
tool: Segments
description: "This reference article explains how to use Braze Segment Funnels, their best practices, and example use cases."

---
# Segment funnels

> This reference article explains how to use Braze Segment Funnels, their best practices, and use cases. 
> <br>
> <br>
> Segment funnels are great for narrowing your audience for a specific campaign use case, learning about that audience and their interactions, and using that knowledge to strategize and develop effective campaigns.


Segment funnels allow you to see how each added filter impacts your segment statistics. When creating a segment, a row of data will appear under each filter. This data will provide the following information for users that are targeted by all filters up to that point:

- Total number of users targeted and the percentage of your audience base
- LTV and LTV for paying users  
- Number of users emailable
- Number of users opted in to email
- Number of users that are push enabled  
- Number of users opted in to push

![Segment funnel overview][1]

## Best practices

- By adding filters that document your user flow, you can see the points where users fall off. For instance, if you're a social networking app and you want to see where you might be losing users during your onboarding process, you may want to add custom data filters for signing up, adding friends, and sending the first message. If you find that 85% of users are signing up and adding friends, but only 45% sent the first message, then you'll know to focus on encouraging more message sends during your onboarding and marketing campaigns.

- Segment funnels let you compare the percentage of users who commit different actions. For instance, do active users, or those with high LTV, [tend to interact more with push or email][4]? To find out, create a segment of active users with one or more filters, and then see how statistics change when you add a filter for opting in to push, and when you add a filter for opting in to email.

- Analyze how LTV changes as you add filters. For active users, do those who connect to Facebook or those who connect to Twitter have a higher LTV? Or is LTV significantly higher for those who have connected to both? If you find, for instance, that connecting to Twitter has very little impact on LTV but connecting to Facebook has a large impact, you may want your marketing campaigns to focus on incentivizing Facebook connections.


## Sample use cases

### Impact of a specific user action on conversions {#push-email}
By analyzing the impact of a certain user action (such as adding items to a wish list) on a conversion (such as making purchases) you can answer the following questions:

- Does the user action coincide with more purchases?
- How prevalent is the user action? Should you create marketing campaigns that encourage more of that action?

In the example below, all users who added items to a wish list also made a purchase. Since only a small percentage of users added items to a wish list, this app may want to incentivize this behavior more through marketing campaigns.

![Segment funnel for users][3]

### Compare messaging channels
Create a segment of active users (or users with desired traits) and compare their interactions with different engagement channels, such as the News Feed, email and push notifications. For instance, if more loyal users are subscribed to push, you may want to spend more time on sending active user campaigns via push. However, if you find that the LTV is higher for those who are subscribed to email, you might want to prompt more active users to subscribe to email.

![Segment funnel for email][5]


[1]: {% image_buster /assets/img_archive/segment_funnel_example.png %}
[3]: {% image_buster /assets/img_archive/Wish_List_2.png %}
[4]: #push-email
[5]: {% image_buster /assets/img_archive/Wish_List_Email.png %}
