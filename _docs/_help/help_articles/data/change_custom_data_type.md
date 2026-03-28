---
nav_title: Changing custom attribute or event data type
article_title: Change Custom Attribute or Event Data Type
page_order: 1

page_type: solution
description: "This help article walks you through how to change the data type of a custom attribute or custom event, and the implications of doing so."
---

# Change custom attribute or event data type

## Prerequisites

The custom attribute must not currently be in use in any active campaigns, Canvases, or segments. If you attempt to change the data type while the attribute is still referenced, the dashboard will display an error and block the change.

## Changing the data type

1. Stop any active campaigns or Canvases that use the attribute in segments or filters.
2. Remove the attribute from all segment, campaign, and Canvas filters.
3. Go to **Data Settings** > **Custom Attributes** (or **Custom Events**), find the attribute, and update it to the desired data type.
4. Update the attribute values on existing user profiles to match the new data type (for example, using the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)).
5. Reapply the attribute to relevant segments, campaigns, and Canvases, then reactivate any stopped campaigns or Canvases.

![Custom Attributes tab to edit attribute or data type]({% image_buster /assets/img/change_custom_attribute.png %})

## Things to know

- **User data is not retroactively updated.** If a user profile had the attribute with the old data type, that value remains unchanged. The segmentation filter will look for the new data type, so users with the old value will be excluded from matching segments until their profile is updated.
- **New data must match the new data type.** After the change, API calls or SDK events that send the previous data type for this attribute will not be accepted. Only values matching the new data type will be ingested.
- **Filters are not automatically updated.** Segments and campaign filters referencing the changed attribute are not retroactively updated. You must remove and re-add them after the change.

{% alert important %}
The ability to prevent automatic detection from updating the custom attribute data type is currently in early access. Contact your customer success manager if you’re interested in participating in this early access.
{% endalert %}

_Last updated on February 8, 2024_

