---
nav_title: Segmentation Logic
article_title: Segmentation Logic 
page_order: 3

page_type: solution
description: "This article walks you through the differences between AND and OR operators, and how you can use them to build powerful segments."
tool: Segments
---

# Segmentation logic 

The `AND` and `OR` operators enable powerful filtering when [creating a segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/). Using these operators, you can target your users based on their actions or behaviors in the **Target Audience** step of building your campaigns or Canvases.

## Understanding the AND and OR operators

The `AND` and `OR` operators function in different ways. You can use each operator depending on what you want to achieve when segmenting your audience. 

### When to use the AND operator

In general, use `AND` if you're interested in the intersection of two or more values for a particular attribute.

Let's consider how to target users in a campaign from every country except for Canada and the United States. In this case, using the `AND` operator can help filter these users. The statement `Country is not United States AND Country is not Canada` will only include users who are not from the United States and who are not from Canada. So, by using this logic, both users in Canada and the United States will be excluded.

### When to use the OR operator

Use `OR` if your goal is to target users who meet at least one condition in a set of conditions. If you have three conditions linked together by `OR`, then one, two, or all of the conditions can be true in order for the actual statement to be true.

For example, imagine that you want to send a message to all your users on version 1.0 or 1.1 of your app. In order to target the users that are on version 1.0 and on version 1.1, you can use the filters `Is 1.0` and `Is 1.1` with the `OR` operator in your segment. This will target all users who are on versions 1.0 or 1.1.

In this next example, consider a promotion that is valid for both users in the United States and Canadian. You want to make sure that only users in areas where the promotion is valid receive the promotion. In this scenario, use the following statement to target your campaign: `Country is United States OR Country is Canada`. With the `OR` operator, your campaign would only go to users whose country is Canada or whose country is United States.

#### When to avoid the OR operator

There can be user targeting situations where using the `OR` operator should be avoided. For example, avoid using `OR` if you have a campaign that is valid in every country except for the United States and Canada. To filter for this segment, you might try to invert the logic from the previous scenario. However, this leads to a segment that targets all users: `Country is not United States OR Country is not Canada`.

The preceding statement targets all users because all users meet the criteria for one or more of the filters. Users in Canada meet the criteria for `Country is not United States`. Users located in the United States would meet the criteria for `Country is not Canada`. 

So, using the `AND` operator in this scenario ensures that the users who receive the campaign are those who are in the segment and not in the other segments at the same time. 

The following negative targeting criteria should not be used with the `OR` operator when two or more filters are referencing the same attribute:

- `is not`
- `does not equal`
- `does not match regex`

If `is not`, `does not equal`, or `does not match regex` are used with the `OR` operator two or more times in a statement, users with all values for the relevant attribute will be targeted.

### Using both operators

In this next example, we'll use both `AND` and `OR` operators. Here, the target audience includes users who purchased Nike sneakers or Adidas sneakers, and are opted in to receive email notifications.

![Building a segment for Sneaker Shoppers where a user's favorite brand equals Nike or Adidas, and they have opted in to email][33]

Another way to ensure you're building the right logic is to create your segment and [preview the users][35] who are falling into it based on your filters. This way you can make sure that their attributes, app version, or any other segmentation matches what you are seeing.

Still need help? Open a [support ticket]({{site.baseurl}}/braze_support/).

_Last updated on June 3, 2022_

[33]: {% image_buster /assets/img_archive/NikeSneakers.png %}
[35]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#viewing-and-understanding-segment-data
