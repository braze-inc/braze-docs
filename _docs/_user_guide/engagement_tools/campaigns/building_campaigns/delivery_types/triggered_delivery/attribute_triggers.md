---
nav_title: Attribute triggers
article_title: Attribute Triggers
page_order: 1
alias: /attribute_triggers/
page_type: reference
description: "This reference article gives an overview of attribute triggers and how you can use them to send action-based messages to users."
tool:
  - Campaigns

---

# Attribute triggers

> Attribute triggers allow you to send action-based messages when a user's subscription state or custom attribute values change. 

Attribute triggers are available for the following scenarios:

- Subscription state updates.
- Boolean, integer, string, or date custom attribute values change to any value.
- Boolean, integer, or string custom attribute values change to a specific value.

To start using attribute triggers, create a campaign or Canvas component and select **Action-Based Delivery** as your delivery method. Then, select the attribute trigger that you'd like to use.

!["Action-Based delivery" section with a dropdown to select a trigger.]({% image_buster /assets/img_archive/trigger_attribute.png %})

### Update subscription status

Use the `Update Subscription Status` trigger to target users when their subscription status is updated. 

For example, you can target users when their email or push subscription status changes to opted in, and thank them for opting in. You can also send a webhook to your systems whenever a user unsubscribes from email so that your internal systems are up to date with the latest subscription status information.

{% alert important %}
This trigger doesn't apply when a new user is created with the default email global state of `subscribed` and there is a subsequent request to update the state to `subscribed` since the subscription status has not changed.
{% endalert %}

### Update subscription group status

Use the `Update Subscription Group Status` trigger to target users when their subscription group status for Email, SMS or WhatsApp is updated. 

For example, you can target users with a welcome SMS message when they opt in to your program. You can also specify the source of the update to have finer control over when a message fires. 

Available update sources vary per channel:
- Canvas User Update Step
- CSV Import
- List-Unsubscribe
- Preference Center
- REST API
- SDK
- Shopify (Email, SMS)
- Inbound Message (SMS)

For example, you may want to only send your welcome SMS when the update comes from the REST API and not an inbound message, since Braze already automatically responds to certain inbound SMS.

### Change custom attribute value

For change attribute, the trigger is evaluated first, then the audience criteria. This differs from the default behavior of audience criteria evaluated first, then trigger. To avoid a race condition, ensure the attribute used as the trigger is not the same as the attribute used to qualify your audience.

#### Any new value option

Use the `Change Custom Attribute Value` trigger with the `any new value` option to target users when a boolean, integer, string or date value changes to any new value.

For example, target users when their number of reward points changes to let them know how many points they now have. In this example, let's say that a user has 85 reward points and you've set up a campaign to trigger when the reward point attribute changes to any new value. If this user's reward point attribute value changes to any new value (such as 83, 84, 86, and so on), then the campaign will trigger.

Consider the next example use case with a tier update notification. You might want to alert users if their rewards tier changes. To accomplish this use case, set up a campaign that triggers off of `Change Custom Attribute Value` and set it to trigger when the custom attribute rewards tier changes to any new value.

{% alert important %}
Attribute triggers are not currently available for array attributes.
{% endalert %}

![A "Change Custom Attribute Value" trigger for the "AA_current_rewards_tier" changing to any value.]({% image_buster /assets/img_archive/any_value.png %})

You can also use Liquid to personalize the message body with the customer's new rewards tier and provide the customer with more information about the change.

{% raw %}
```liquid
Your rewards tier was just changed to {{custom_attribute.${AA_current_rewards_tier}}}
```
{% endraw %}

#### Specific value

Use the `Change Custom Attribute Value` trigger with the `specific value` option to target users when a boolean, integer, or string custom attribute changes to a specific value. 

For example, target users when their rewards tier changes to the best tier. For this example, say that the best rewards tier is Super VIP. You can set up a campaign to trigger when a user's rewards tier custom attribute changes to `Super VIP` so that you can congratulate the user on becoming a Super VIP.

![A "Change Custom Attribute Value" trigger for the "AA_current_rewards_tier" changing to the specific value of "super vip".]({% image_buster /assets/img_archive/super_vip.png %})

{% alert important %}
- Attribute triggers for specific custom attribute values are not available for array and date custom attributes.
- The custom attribute values change trigger does not trigger when the custom attribute value is updated to null.  
- The custom attribute values change trigger will only trigger when the value of a custom attribute changes. If a custom attribute's current value is re-sent to Braze (e.g the value for the favorite color attribute is red, and you resend the value red to Braze), the custom attribute values change trigger will not occur.
- The custom attribute values change trigger also applies for new users created. 
{% endalert %}

