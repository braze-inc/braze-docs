---
nav_title: Custom Events
page_order: 1
description: "Custom events are actions taken by, or updates about, your users; they're best suited for tracking high-value user interactions with your application."
---

# Custom Events

Custom events are actions taken by, or updates about, your users; they're best suited for tracking high-value user interactions within your application. Logging a custom event can trigger any number/type of follow-up campaigns, and enables the listed segmentation filters on the recency and frequency of that event.

## Custom Event Segmentation Filters

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the custom event has occurred __more than X number of times__ | __MORE THAN__ | __NUMBER__ |
| Check if the custom event has occurred __less than X number of times__ | __LESS THAN__ | __NUMBER__ |
| Check if the custom event has occurred __exactly X number of times__ | __EXACTLY__ | __NUMBER__ |
| Check if the custom event last occurred __after X date__ | __AFTER__ | __TIME__ |
| Check if the custom event last occurred __before X date__ | __BEFORE__ | __TIME__ |
| Check if the custom event last occurred __more than X days ago__ | __MORE THAN__ | __NUMBER OF DAYS AGO__ (Positive Number) |
| Check if the custom event last occurred __less than X days ago__ | __LESS THAN__ | __NUMBER OF DAYS AGO__ (Positive Number) |
| Check if the custom event occurred __more than X (Max = 50) number of times__ | __MORE THAN__ | in the past __Y Days (Y = 1,3,7,14,21,30)__ |
| Check if the custom event occurred __less than X (Max = 50) number of times__ | __LESS THAN__ | in the past __Y Days (Y = 1,3,7,14,21,30)__ |
| Check if the custom event occurred __exactly X (Max = 50) number of times__ | __EXACTLY__ | in the past __Y Days (Y = 1,3,7,14,21,30)__ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Custom Event Analytics

Braze notes the number of times these events have occurred as well as the last time they were performed by each user for segmentation. On the [custom events analytics page][7] you can view in aggregate how often each custom event occurs, as well as by segment over time for more detailed analysis. This is particularly useful to view how your campaigns have affected custom event activity by looking at the gray lines Braze overlays on the time-series to indicate the last time a campaign was sent.

![custom_event_analytics_example.png][8]

{% alert tip %}
[Incrementing Custom attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#integers) can be used to keep a counter on a user action similar to a custom event. However, you will not be able to view custom attribute data in a time-series. User actions that do not need to be analyzed in time-series should be recorded via this method.
{% endalert %}

### Custom Events Analytics Not Showing?

Please note that Segments created with custom event data cannot show previous historic data from before they were created.

## Custom Event Storage

All User Profile data, including Custom event metadata (first/last occurrence, total count, and X in Y over 30 days) is stored as long as each profile is active.

# Custom Event Properties

With Custom Event Properties, you can set properties on Custom events and purchases. These properties can then be used for further qualifying trigger conditions, increasing personalization in messaging, and generating more sophisticated analytics through raw data export. Property values can be string, numeric, boolean, or time objects. However, property values cannot be array objects.

For example, if an eCommerce application wanted to send a message to a user when he/she abandons their cart, it could additionally improve its target audience and allow for increased campaign personalization by adding a Custom Event Property of the 'cart value' of users' carts.

{% alert important %}
Each Custom event or purchase can have up to 256 distinct Custom event properties. If a Custom event or purchase is logged with more than 256 properties, only the first 256 will be captured and available for use.
{% endalert %}

![customEventProperties.png][16]

Custom event properties can also be used for personalization within the messaging template. Any campaign using [Action-Based Delivery][19] with a trigger event can use custom event properties from that event for messaging personalization. If a gaming application wanted to send a message to users who had completed a level, it could further personalize the message with a property for the time it took users to complete that level. In this example, the message is personalized for three different segments using [conditional logic][18].  The Custom event property called ``time_spent``, can be included in the message by calling ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``.

{% alert warning %}
Triggered in-app messages with templated Custom event properties (for example, ``{event_properties.${time_spent}}}``) will fail and not display if there is no internet connectivity.
{% endalert %}

You can change the data type of your Custom event property, but please be aware of [the impacts of changing data types]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/) after data has been collected.

{% alert important %}
Braze will ban or block users ("dummy users") with over 5 million sessions and no longer ingest their SDK events because they are usually the result of misintegration. If you find that this has happened for a legitimate user, please reach out to your Braze account manager.
{% endalert %}

## Custom Event Property Storage
Custom event properties are designed to help you personalize your messaging or build granular Action-Based Delivery Campaigns. As such, Custom event properties are not stored long-term.

If you need to segment on the values of event properties, you have options:
1. **Within 30 days:** Braze support personnel can enable segmentation on the frequency and recency of specific event property values over the past thirty (30) days. If you’d like to leverage event properties for Segmentation, please contact your Braze account executive or Customer Success Manager.
2. **Beyond 30 days:** Since all other data types on the profile are stored indefinitely, you can segment on event property values long-term by copying them into Custom attributes. For example, in a streaming video scenario, you might copy the title of each show into an array of "shows watched" for long-term segmentation. The copying process can take place entirely within Braze in many scenarios.

Braze's Success and Support teams can help recommend the best approach depending on your specific needs. Please note these approaches may have additional data usage impact.

[7]: https://dashboard-01.braze.com/dashboard/custom_events/
[8]: {% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png"
[16]: {% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png"
[18]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
[19]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/scheduling_your_campaign/#action-based-delivery-event-triggered-campaigns
