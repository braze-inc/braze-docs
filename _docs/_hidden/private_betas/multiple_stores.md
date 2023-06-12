---
nav_title: Multiple Store Support
permalink: "/shopify_multiple_store/"
hidden: true
layout: dev_guide
---

# Shopify multiple store support

> Connect multiple Shopify stores to a single app group with our new beta for multiple store support to have a holistic view of your customers across all markets or brands. Build and launch automation programs and journeys in a single workspace without duplicating efforts across multiple instances. 

{% alert important %}
Shopify multiple store support is currently in beta. The feature may change, iterate, and evolve as the product team continues development.
{% endalert %}

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Create [email subscription group]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#create-a-group) for each store | Once created, you will designate the Email Subscription Group to the specific store during the “[Collect email or SMS subscribers]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/#step-5-collect-email-or-sms-subscribers)” step of the setup flow.<br><br>This is required for you to track which store’s Email subscription group your users belong to for compliance purposes. |
| Audit and update segments, campaigns, and Canvas using Shopify attributes | The custom attributes the Shopify integration collects will transform into a new data structure, nested object. As a result, if you are using these attributes today, you'll need to stop any segments, campaigns, and Canvases. Once you’ve added multiple stores, update all segments, campaigns, and Canvases to the new format.<br><br>If you are not using any attributes today, you can ignore this. |
| Audit and update Shopify alias | The `shopify_customer_id` alias will be migrated to `shopify_customer_id_{{storename}}` after you connect more than one store. Ensure you are updating any internal systems to use the new alias. The legacy alias, `shopify_customer_id`, will be deprecated. If you are not using the alias today, you can ignore this. |
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
- **Customers with multiple regions and markets as stores**: Ensure you set the correct email subscription group to the right store for every store install. We recommend you enable “Override existing global subscription state for users” for every store. This will always override the Braze global email subscription state and the selected email subscription group with the most recent subscription from any Shopify store for the user. 
- **Customers with multiple brands as stores**: Currently, we do not have support to override only the email subscription group (recommended). This will be supported ahead of general availability.<br><br> 
4. Repeat this process for each store as many times as you want.<br><br>
5. To view each store’s integration and configure advanced settings, click into a store in the drop-down menu:<br>![][2]

## Shopify data

### Shopify alias
After you connect more than one store, all incoming Shopify users will have a new alias, `shopify_customer_id_{{storename}}` in addition to the existing alias, `shopify_customer_id`. Note that `shopify_customer_id` is a legacy alias and will be deprecated soon. You should transition to using the new alias moving forward.

### Shopify custom attributes
After you connect more than one store, the following attributes will be synced as a nested object that contains the per-store value and aggregate value:
- `shopify_tags`
- `shopify_order_count` (only available via Historical Backfill)
- `shopify_total_spent` (only available via Historical Backfill)

### Shopify custom events
After you connect more than one store, incoming Shopify custom events will now contain a new event property, `shopify_storefront`. Refer to [Shopify data processing]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_data_processing#supported-shopify-events) to see all custom events supported in this integration. This event property provides the Shopify store domain the event is coming from.

### Shopify user merging
If you have the same user across multiple Shopify stores, Braze syncs customer data to a single profile if their email address or phone number already exists using the alias, `shopify_email` or `shopify_phone`. Note that it is possible for user data (i.e., city) to not match across multiple Shopify stores for the same user, but Braze will always update the user profile with the most recent activity on any store. 

## Not currently supported
The following features and functionalities are not currently supported but will be supported for general availability:
- Ability to import a catalog for each store
- Ability to override only a specific email subscription group state without overriding the global email subscription status. This is ideal for stores with multiple brands that want email subscriptions from different stores to be managed and updated individually without impacting other email subscription groups and the overall global state.
- `shopify_storefront` property is not supported for [ScriptTag events]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_data_processing#supported-shopify-events).

[1]: {% image_buster /assets/img/multiple_stores.png %}
[2]: {% image_buster /assets/img/multiple_stores2.png %}
