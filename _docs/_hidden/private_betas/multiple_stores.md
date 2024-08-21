---
nav_title: Multiple Store Support
permalink: "/shopify_multiple_store/"
hidden: true
layout: dev_guide
---

# Shopify multiple store support

> Connect multiple Shopify stores to a single workspace with our new beta for multiple store support to have a holistic view of your customers across all markets. Build and launch automation programs and journeys in a single workspace without duplicating efforts across multiple instances. 

{% alert important %}
Support for multiple Shopify stores is available in beta, which may contain bugs. This feature is subject to change as development continues.
{% endalert %}

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Create [email subscription group]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#create-a-group) for each store | After the Email Subscription Group is created, you will designate it to the specific store during the “[Collect email or SMS subscribers]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/#step-5-collect-email-or-sms-subscribers)” step of the setup flow.<br><br>This is required for you to track which store’s Email subscription group your users belong to for compliance purposes. |
| Audit and update segments, campaigns, and Canvas using Shopify attributes | The custom attributes collected from multiple stores will be in the format of a nested object, which differs from the current structure used in the overall Shopify integration, which is formatted as a string value. As a result, you'll need to update all segments, campaigns, or Canvas to the new format after connecting multiple stores to use the “Nested Custom Attribute” filter or update the “Change Custom Attribute” trigger event.<br><br>If you are not using any of the attributes today, you can ignore this. |
| Audit and update Shopify alias | The `shopify_customer_id` alias will be migrated to {% raw %}`shopify_customer_id_{{storename}}`{% endraw %} after you connect more than one store. Make sure you are updating any internal systems to use the new alias. The legacy alias, `shopify_customer_id`, will be deprecated. If you are not using the alias today, you can ignore this. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Integration
With Braze’s multiple-store support, you can:
- Have a 360° view of your customers across stores
- Create segments of your customers with aggregate store data 
- Set up messaging or journeys as your customers move across different stores
- Manage email and SMS subscriptions across different stores

{% alert important %}
Supporting multiple brands in a single workspace increases the likelihood for duplicate user profiles, as users can shop between those brands. We suggest placing each brand into their own workspace.
{% endalert %}

### Setting up an additional store
1. After you install your first store, select the **+ Connect New Store** option.<br>![][1]{: style="max-width:70%;"}<br><br>
2. Go through the onboarding flow for this new store. More details can be found in our [Setting up Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/) guide.<br><br>Note that the settings from the previous store can be carried over, but you can update the settings accordingly as you progress through your onboarding.<br><br>
3. For the collect email or SMS subscribers step:
- To appropriately collect email and SMS subscriptions for each store, you must assign unique subscription groups to each store setup. 
- We suggest that you **do not** enable “Override existing global state for users” as it can globally unsubscribe your customers if they interacted with more than one of your stores.<br><br>
4. Repeat this installation for as many stores as you need.<br><br>
5. To view each store’s integration and configure advanced settings, click into a store in the drop-down menu:<br>![][2]{: style="max-width:70%;"}

## Shopify data

### Shopify alias

{% raw %}After you connect more than one store, all incoming Shopify users will have a new alias, `shopify_customer_id_{{storename}}` in addition to the existing alias, `shopify_customer_id`. Note that `shopify_customer_id` is a legacy alias and will be deprecated when this feature is generally available. You should transition to using the new alias moving forward. {% endraw %}

### Shopify custom attributes

After you connect more than one store, the following attributes will be synced as a nested object that contains the per-store value and aggregate value:
- `shopify_tags`
- `shopify_order_count` (only available via Historical Backfill)
- `shopify_total_spent` (only available via Historical Backfill)

To use custom events when creating or editing a segment, select the **Nested Custom Attribute** filter and locate your nested attribute. For help identifying the specific path or field in the object, use the [Generate Schema]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support#generate-schema) tool. After you select the nested attributes, a field with a plus button will appear next to the selected attributes for you to specify the path. To learn more about nested attributes, see [Nested custom attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/).

![3]{:style="max-width:70%;"}

You can specify your path by typing it into the field or clicking the plus button and selecting the path.

![4]{:style="max-width:70%;"}

### Shopify custom events

After you connect more than one store, incoming Shopify custom events will now contain a new event property, `shopify_storefront`. Refer to [Shopify data processing]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_data_processing#supported-shopify-events) to see all custom events supported in this integration. This event property provides the Shopify store domain the event is coming from.

### Action-based delivery or conversion tracking

To trigger messaging to users completing actions with a specific store:

1. Navigate to the **Schedule Delivery** step of your campaign.
2. Select **Perform Custom Event** as a trigger event.
![5]{:style="max-width:70%;"}
3. Select a Shopify event as the trigger event, such as **shopify_created_order**, and the **Add property filters** checkbox.
![6]{:style="max-width:70%;"}
4. Select **Basic Property** in the **Add Filter** dropdown.
5. Select **shopify_storefront** and enter the store’s full Shopify domain.
![7]{:style="max-width:70%;"}


### Shopify user merging and syncing

If the user’s Shopify customer ID, email address, or phone number exists already within Braze using the alias, {% raw %}`shopify_customer_id_{{storefront_domain}}`, `shopify_email`, or `shopify_phone`, {% endraw %} then we’ll update the existing user profile. If those aliases do not exist within Braze, we will create a new user profile. Note that it is possible for a user’s data (for example, city) to differ across multiple Shopify stores for the same user. In such cases, Braze will always update the user profile from the store with the most recent activity. 

{% alert warning %}
Braze will update the user profile with Shopify customer data from the store with the most recent activity. This means that any attributes, such as email, phone number, sending phone, city, etc., can be overwritten with the most recent store activity. For example, if a user has a different phone number in two different stores, Braze will update the user profile with the phone number from the store with the most recent activity.
{% endalert %}

[1]: {% image_buster /assets/img/multiple_stores.png %}
[2]: {% image_buster /assets/img/multiple_stores2.png %}
[3]: {% image_buster /assets/img/shopify_nested_attributes.png %}
[4]: {% image_buster /assets/img/shopify_tags.png %}
[5]: {% image_buster /assets/img/shopify_add_trigger.png %}
[6]: {% image_buster /assets/img/shopify_select_event.png %}
[7]: {% image_buster /assets/img/shopify_enter_storefront.png %}
