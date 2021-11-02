---
nav_title: Segmentation Logic with Negative OR Filters
article_title: Segmentation Logic with Negative OR Filters
page_order: 4

page_type: solution
description: "This article walks you through best practices on when to use or not use the OR operator, and when to use the AND operator."
tool: Segments
---

# Segmentation logic with negative OR filters

The OR operator must be used with care, especially when considering:
* [When to apply the OR operator](#using-or)
* [When not to apply the OR operator](#when-not-to-apply-the-or-operator)
* [When to apply the AND operator](#when-to-apply-the-and-operator)

## When to apply the OR operator {#using-or}

Use the `OR` operator to create a statement that will evaluate to true if a user meets the criteria for one or more filters in the statement. 

For example, consider a promotion that is valid for both United States and Canadian customers. You want to make sure that only customers in areas where the promotion is valid receive the promotion. In this scenario, use the following statement to target your campaign:

`Country is United States OR Country is Canada`

![United States OR Canada][49]{: style="max-width:80%"}

With the `OR` operator, your campaign will only go to customers whose country is Canada or whose country is United States.

## When not to apply the OR operator

In certain circumstances, the `OR` operator should not be used. For example, do not use `OR`if you have a campaign that is valid in every country except for the United States and Canada. To filter for this segment, you might try to invert the logic from the previous scenario. However, this leads to a segment that targets all customers: 

`Country is not United States OR Country is not Canada`

![Not United States OR Canada][50]{: style="max-width:80%"}

The preceeding statement targets all customers because all customers meet the criteria for one or more of the filters. Canadian customers meet the criteria for `Country is not United States`. US customers meet the criteria for `Country is not Canada`.

The following negative targeting criteria should not be used with the `OR` operator when two or more filters are referencing the same attribute:

- `is not`
- `does not equal`
- `does not match regex`

If `is not`, `does not equal`, or `does not match regex` are used with the `OR` operator two or more times in a statement, customers with all values for the relevant attribute will be targeted.

## When to apply the AND operator

If you'd like to include customers with two or more values for a particular attribute, you should use the `AND` operator. Let's return to the example use case—targeting customers from every country except for Canada and the United States.

The statement `Country is not United States AND Country is not Canada` will only include customers who are not from the United States and who are not from Canada. Therefore, both United States customers and Canadian customers will be excluded.

Still need help? [Open a support ticket]({{site.baseurl}}/support_contact/).

_Last updated on September 17, 2021_

[49]: {% image_buster /assets/img_archive/us_canada.png %}
[50]: {% image_buster /assets/img_archive/not_us_not_canada.png %}
