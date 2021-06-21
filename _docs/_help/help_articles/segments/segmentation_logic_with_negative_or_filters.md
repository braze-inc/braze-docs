---
nav_title: Segmentation Logic With Negative Or Filters
page_order: 2

page_type: solution
description: "This article walks you through best practices on when to use or not use the OR operator, and when to use the AND operator."
tool: Segments
---

# Segmentation Logic With Negative OR Filters

The OR operator must be used with care, especially when considering:
* [When to apply the OR operator](#using-or)
* [When not to apply the OR operator](#when-not-to-apply-the-or-operator)
* [When to apply the AND operator](when-to-apply-the-and-operator)

# Using OR

The "OR" operator allows you to create a statement that will evaluate to true if a user meets the criteria for one or more filters in the statement. For example, consider a promotion that is valid for your US and Canadian customers. You want to make sure that only customers in areas where the promotion is valid receive the promotion. You can use the following statement to target your campaign: `Country is United States OR Country is Canada`

![us_or_canada][49]

A customer who meets one or more of the country filters will receive your campaign so your campaign will only go to customers whose country is Canada or whose country is United States.

# When Not to Apply the OR Operator

In certain circumstances, the "OR" operator should not be used, it is possible to break the logic. For example, let's say that you have a campaign that is valid in every country EXCEPT for the US and Canada. Inverting our logic from the last scenario leads to a segment that targets **all** customers: `Country is not United States OR Country is not Canada`


![not_us_or_canada][50]

The above statement will target all customers, because all customers will meet the criteria for one or more of the filters. Canadian customers meet the criteria for "Country is not United states". US customers meet the criteria for "Country is not Canada".

The negative targeting criteria "is not" and "does not equal" **should not** be used with the "OR" operator when two or more filters are referencing the same attribute. If "is not" or "does not equal" is used with the "OR" operator two or more times in a statement, customers will all values for the relevant attribute will be targeted.

## When To Apply the AND Operator

If you'd like to include customers with two or more values for a particular attribute, you should use the "AND" operator. Let's return to our use case - targeting customers from every country except for Canada and the United States.

`Country is not United States AND Country is not Canada` will only include customers who are not from the United States AND who are not from Canada. Therefore, both United States customers and Canadian customers will be excluded.

Because there are no valid use cases for using "Or" operands with two or more negative filters that have the same attribute, Braze will not allow you to continue creating your campaign or segment if you use this configuration with "does not equal" or "is not" comparisons.

![targeting_error][48]

If you received this warning message and aren't sure how to correct your campaign, Canvas or segment, please get in touch with your Customer Success Manager or write to our support team.

Still need help? [Open a support ticket]({{site.baseurl}}/support_contact/).

[48]: {% image_buster /assets/img_archive/targeting_error.png %}
[49]: {% image_buster /assets/img_archive/us_canada.png %}
[50]: {% image_buster /assets/img_archive/not_us_not_canada.png %}
