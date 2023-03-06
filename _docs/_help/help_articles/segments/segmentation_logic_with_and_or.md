---
nav_title: Segmentation Logic
article_title: Segmentation Logic 
page_order: 3

page_type: solution
description: "This help article walks you through the differences between AND and OR operators, and how you can use them to build powerful segments."
tool: Segments
---

# Segmentation logic 

The `AND` and `OR` operators enable powerful filtering when creating a [segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/). 

## Using the AND operator

Use `AND` if you are interested in the intersection of two groups. This is what is similar between the two groups. If you'd like to include customers with two or more values for a particular attribute, you should use the `AND` operator. 

Let's consider the example use case for targeting customers from every country except for Canada and the United States. The statement `Country is not United States AND Country is not Canada` will only include customers who are not from the United States and who are not from Canada. Therefore, both United States customers and Canadian customers will be excluded.

## Using the OR operator

Use `OR` if you want to target users who meet at least one condition in a group of conditions. If you have three conditions linked together by `OR`, then one, two, or all of the conditions could be true in order for the statement to be true.

For example, imagine that you want to send a message to all your users on version 1.0 or 1.1 of your app. In order to target the users that are on version 1.0 and on version 1.1, you can use the filters `Is 1.0` and `Is 1.1` with the `OR` operator in your segment. This will target all users who are on versions 1.0 or 1.1.

In this next example, consider a promotion that is valid for both United States and Canadian customers. You want to make sure that only customers in areas where the promotion is valid receive the promotion. In this scenario, use the following statement to target your campaign: `Country is United States OR Country is Canada`.

With the `OR` operator, your campaign will only go to customers whose country is Canada or whose country is United States.

### Avoiding the OR operator

In certain circumstances, the `OR` operator should not be used. 

For example, do not use `OR` if you have a campaign that is valid in every country except for the United States and Canada. To filter for this segment, you might try to invert the logic from the previous scenario. However, this leads to a segment that targets all customers: `Country is not United States OR Country is not Canada`.

The preceding statement targets all customers because all customers meet the criteria for one or more of the filters. Canadian customers meet the criteria for `Country is not United States`. US customers meet the criteria for `Country is not Canada`.

The following negative targeting criteria should not be used with the `OR` operator when two or more filters are referencing the same attribute:

- `is not`
- `does not equal`
- `does not match regex`

If `is not`, `does not equal`, or `does not match regex` are used with the `OR` operator two or more times in a statement, customers with all values for the relevant attribute will be targeted.

## Using both operators

In this next example, we'll use both `AND` and `OR` operators. Here, the target audience includes users who purchased Nike sneakers or Adidas sneakers, and are opted in to receive email notifications.

![Building a segment for Sneaker Shoppers where a customer's favorite brand equals Nike or Adidas, and they have opted in to email][33]

Another way to ensure you're building the right logic is to create your segment and [preview the users][35] who are falling into it based on your filters. This way you can make sure that their attributes, app version, or any other segmentation matches what you are seeing.

Still need help? Open a [support ticket]({{site.baseurl}}/braze_support/).

_Last updated on June 3, 2022_

[33]: {% image_buster /assets/img_archive/NikeSneakers.png %}
[35]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#viewing-and-understanding-segment-data
