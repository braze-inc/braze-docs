---
nav_title: Attribute Triggers
article_title: Attribute Triggers
page_order: 1
alias: /attribute_triggers/
page_type: reference
description: "This reference article gives an overview of attribute triggers and how you can use them to send action-based messages to users."
tool:
  - Campaigns

---

# Attribute Triggers Overview

> This reference article gives an overview of attribute triggers and how you can use them to send action-based messages.

Attribute triggers allow you to send action-based messages when a user's subscription state or custom attribute values change. Attribute triggers are available for the following scenarios:

- Subscription state updates.
- Boolean, integer, string, or date custom attribute values change to any value.
- Boolean, integer, or string custom attribute values change to a specific value.

To start using attribute triggers, create a campaign or Canvas step and select action-based delivery. Then, select the attribute trigger that you'd like to use.

![attribute triggers][1]

### Subscription Status Updates

Use the "subscription status update" trigger to target users when their subscription status is updated. For example, you can target users when their email subscription status changes to opted in, and thank them for opting in. You can also send a webhook to your systems whenever a user unsubscribes from email so that your internal systems are up to date with the latest subscription status information.

### Custom Attribute Values Change to Any Value

Use the "change custom attribute value" trigger with the "any new value" option to target users when a boolean, integer, string or date value changes to any new value. For example, target users when their number of loyalty points changes to let them know how many points they now have. In this example, let's say that a user has 85 loyalty points and you've set up a campaign to trigger when the loyalty point attribute changes to any new value. If this user's loyalty point attribute value changes to any new value (e.g 83, 84, 86, etc.) the campaign will trigger.

Another example use case is a tier update notification. You might want to alert users if their loyalty tier changes. To accomplish this use case, set up a campaign that triggers off of "change custom attribute value" and set it to trigger when the custom attribute loyalty tier changes to any new value.

{% alert important %}
Attribute triggers are not currently available for array attributes.
{% endalert %}

![any value][2]

You can also personalize the message body with the customer's new loyalty tier so that you can provide the customer with more information about the change.

![personalize][3]


### Custom Attribute Values Change to A Specific Value

Use the "change custom attribute value" trigger with the "specific value" option to target users when a boolean, integer or string custom attribute changes to a specific value. For example, target users when their loyalty tier changes to the best tier. For this example, let's say that the best loyalty tier is Super VIP. You can set up a campaign to trigger when a user's loyalty tier custom attribute changes to "Super VIP" so that you can congratulate the user on becoming a Super VIP.

![super vip][4]

{% alert important %}
- Attribute triggers for specific custom attribute values are not available for array and date custom attributes.
- The custom attribute values change trigger does not trigger when the custom attribute value is updated to null.  
- The custom attribute values change trigger will only trigger when the value of a custom attribute changes. If a custom attribute's current value is re-sent to Braze (e.g the value for the favorite color attribute is red, and you resend the value red to Braze), the custom attribute values change trigger will not occur.
- The custom attribute values change trigger also applies for new users created. 
{% endalert %}



[1]:{% image_buster /assets/img_archive/trigger_attribute.png %}
[2]:{% image_buster /assets/img_archive/any_value.png %}
[3]:{% image_buster /assets/img_archive/trigger_personalize.png %}
[4]:{% image_buster /assets/img_archive/super_vip.png %}
