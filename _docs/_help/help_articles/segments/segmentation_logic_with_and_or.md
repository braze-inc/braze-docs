---
nav_title: Segmentation logic
article_title: Segmentation Logic 
page_order: 3

page_type: solution
description: "This help article walks you through the differences between AND and OR operators, and how you can use them to build powerful segments."
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

There can be user targeting situations where using the `OR` operator should be avoided. The `OR` operator creates a statement that evaluates to true if a user meets the criteria for one or more of the filters in a statement. For example, if you want to create a segment of users who belong to "foodies" but do not belong to either "non-foodies" or "candy-lovers", then using the `OR` operator would work here.

![]({% image_buster /assets/img_archive/or_operator_segment.png %})

However, if your goal is to segment users who belong to the "foodies" segment and are not in either of the "non-foodies" and "candy-lovers" segments, then use the `AND` operator. This way, users who receive the campaign or Canvas are in the intended segment ("foodies") and not in the other segments ("non-foodies" and "candy-lovers") at the same time. 

The following negative targeting criteria should not be used with the `OR` operator when two or more filters are referencing the same attribute:

- `is not`
- `does not equal`
- `does not match regex`

If `is not`, `does not equal`, or `does not match regex` are used with the `OR` operator two or more times in a statement, users with all values for the relevant attribute will be targeted.

### Using both operators

In this next example, we'll use both `AND` and `OR` operators. Here, the target audience includes users who purchased Nike sneakers or Adidas sneakers, and are opted in to receive email notifications.

![Building a segment for Sneaker Shoppers where a user's favorite brand equals Nike or Adidas, and they have opted in to email]({% image_buster /assets/img_archive/NikeSneakers.png %})

Another way to ensure you're building the right logic is to create your segment and [preview the users]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/) who are falling into it based on your filters. This way you can make sure that their attributes, app version, or any other segmentation matches what you are seeing.

Still need help? Open a [support ticket]({{site.baseurl}}/braze_support/).

_Last updated on June 3, 2022_

