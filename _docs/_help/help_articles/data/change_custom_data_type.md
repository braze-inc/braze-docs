---
nav_title: Changing Custom Attribute or Event Data Type
article_title: Changing Custom Attribute or Event Data Type
page_order: 0

page_type: solution
description: "This help article walks you through how to change the data type of a custom attribute or custom event, and the implications of doing so."
---

# Changing the Data Type of a Custom Attribute or Event

To change the data type of a custom attribute or event, from the Braze dashboard, navigate to __Manage Settings__ and select the either the __Custom Attributes__ or __Custom Events__ Tab. 

![Change Data Type of Custom Attirbutes][1]

If you must change the data type of a custom attribute or event (for example, from a `date` to a `string`)...

- Relevant filters in Segments, campaigns, Canvases, or other locations using the changed attribute or event are not automatically updated. Before you can modify attributes, you must remove the filter or triggers that reference them. 
- User data __will not be retroactively updated__. If the changed attribute was on a profile prior to the data type change, then that value will still be the old data type. This can cause users to fall out of the Segments that contain the changed attribute. The filter will actively look for the new data type, but if a profile still has the previous data type, that user will now be excluded from the Segment. These users must be updated to fall back into the proper Segments. You can do this via Braze's [`user/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/#custom-attribute-data-types).
- New data coming in will not be accepted if it is not the new data type. For example, an API call to the `user/track` endpoint that contains the previous data type for a changed attribute will not be accepted. You must call the new data type.

[1]: {% image_buster /assets/img/change_custom_attribute.png %}