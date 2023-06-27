---
nav_title: Multiple Store Support
permalink: "/shopify_multiple_store/"
hidden: true
layout: dev_guide
---

# Shopify multiple store support

> Connect multiple Shopify stores to a single app group with our new beta for multiple store support to have a holistic view of your customers across all markets or brands. Build and launch automation programs and journeys in a single workspace without duplicating efforts across multiple instances. 

{% alert important %}
Shopify multiple store Support is currently being provided as a beta version, which may contain bugs. The feature may also change, iterate, and evolve as the product team continues development. 
{% endalert %}

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Create [email subscription group]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#create-a-group) for each store | Once created, you will designate the Email Subscription Group to the specific store during the “[Collect email or SMS subscribers]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/#step-5-collect-email-or-sms-subscribers)” step of the setup flow.<br><br>This is required for you to track which store’s Email subscription group your users belong to for compliance purposes. |
| Audit and update segments, campaigns, and Canvas using Shopify attributes | The custom attributes collected from multiple stores will be in the format of a nested object, which differs from the current structure used in the overall Shopify integration, which is formatted as a string value. As a result, you'll need to update all segments, campaigns, or Canvas to the new format after connecting multiple stores to use the “Nested Custom Attribute” filter or update the “Change Custom Attribute” trigger event.<br><br>If you are not using any of the attributes today, you can ignore this. |
| Audit and update Shopify alias | The `shopify_customer_id` alias will be migrated to {% raw %}`shopify_customer_id_{{storename}}`{% endraw %} after you connect more than one store. Ensure you are updating any internal systems to use the new alias. The legacy alias, `shopify_customer_id`, will be deprecated. If you are not using the alias today, you can ignore this. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Integration
With Braze’s multiple-store support, you can:
- Have a 360° view of your customers across stores
- Create segments of your customers with aggregate store data 
- Set up messaging or journeys as your customers move across different stores
- Manage email and SMS subscriptions across different stores

### Setting up an additional store
1. Once you have installed your first store, select the **+ Connect New Store** option.<br>![][1]<br><br>
2. You will be prompted to go through the onboarding flow for this new store. More details can be found in our [Setting up Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/#step-2-brazes-setup-wizard) guide.<br><br>Note that the settings from the previous store will be carried over, but you can update these accordingly.<br><br>
3. For the collect email or sms subscribers step:
- **Customers with multiple regions and markets as stores**: Ensure you set the correct email subscription group to the right store for every store install. To track a user's most recent subscription state from any store, you must enable the “Override existing global state for users” option when installing each store. Doing so will override the Braze global email subscription state and the email subscription group.
- **Customers with multiple brands as stores**: Currently, we do not have support to override only the email subscription group without also overriding the global email subscription state. We aim to provide this support ahead of general availability.<br><br>
4. Repeat this installation for as many stores as you need.<br><br>
5. To view each store’s integration and configure advanced settings, click into a store in the drop-down menu:<br>![][2]

## Shopify data

### Shopify alias

{% raw %}After you connect more than one store, all incoming Shopify users will have a new alias, `shopify_customer_id_{{storename}}` in addition to the existing alias, `shopify_customer_id`. Note that `shopify_customer_id` is a legacy alias and will be deprecated when this feature is generally available. You should transition to using the new alias moving forward. {% endraw %}

### Shopify custom attributes

After you connect more than one store, the following attributes will be synced as a nested object that contains the per-store value and aggregate value:
- `shopify_tags`
- `shopify_order_count` (only available via Historical Backfill)
- `shopify_total_spent` (only available via Historical Backfill)

### Shopify custom events

After you connect more than one store, incoming Shopify custom events will now contain a new event property, `shopify_storefront`. Refer to [Shopify data processing]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_data_processing#supported-shopify-events) to see all custom events supported in this integration. This event property provides the Shopify store domain the event is coming from.

### Shopify user merging and syncing

If the user’s Shopify customer ID, email address, or phone number exists already within Braze using the alias, {% raw %}`shopify_customer_id_{{storefront_domain}}` `shopify_email`, or `shopify_phone`, {% endraw %} then we’ll update the existing user profile. If those aliases do not exist within Braze, we will create a new user profile. Note that it is possible for a user’s data (e.g., city) to differ across multiple Shopify stores for the same user; in such cases, Braze will always update the user profile from the store with the most recent activity. 

{% alert warning %}
Braze will update the user profile with Shopify customer data from the store with the most recent activity. This means that any attributes, such as email, phone number, sending phone, city, etc., can be overwritten with the most recent store activity. For example, if a user has a different phone number in two different stores, Braze will update the user profile with the phone number from the store with the most recent activity.
{% endalert %}

## Not currently supported

The following features and functionalities are not currently supported; however, we plan to provide such support if and when we make this feature generally available:
- Ability to import a catalog for each store
- Ability to override only a specific email subscription group state without overriding the global email subscription status. This is ideal for stores with multiple brands that want email subscriptions from different stores to be managed and updated individually without impacting other email subscription groups and the overall global state.
- `shopify_storefront` property is not supported for [ScriptTag events]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_data_processing#supported-shopify-events).

[1]: {% image_buster /assets/img/multiple_stores.png %}
[2]: {% image_buster /assets/img/multiple_stores2.png %}
