---
nav_title: Custom Events
page_order: 1
---

# Custom Events

Custom Events are actions taken by your users; they're best suited for tracking high-value user interactions with your application. Logging a custom event can trigger any number of follow-up campaigns with configurable delays, and enables the following segmentation filters around the recency and frequency of that event:

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the custom event has occurred __more than X number of times__ | __MORE THAN__ | __INTEGER__ |
| Check if the custom event has occurred __less than X number of times__ | __LESS THAN__ | __INTEGER__ |
| Check if the custom event has occurred __exactly X number of times__ | __EXACTLY__ | __INTEGER__ |
| Check if the custom event last occurred __after X date__ | __AFTER__ | __DATE__ |
| Check if the custom event last occurred __before X date__ | __BEFORE__ | __DATE__ |
| Check if the custom event last occurred __more than X days ago__ | __MORE THAN__ | __NUMBER OF DAYS AGO__ (Positive) Integer) |
| Check if the custom event last occurred __less than X days ago__ | __LESS THAN__ | __NUMBER OF DAYS AGO__ (Positive) Integer) |
| Check if the custom event occurred __more than X (Max = 50) number of times__ | __MORE THAN__ | in the past __Y Days (Y = 1,3,7,14,21,30)__ |
| Check if the custom event occurred __less than X (Max = 50) number of times__ | __LESS THAN__ | in the past __Y Days (Y = 1,3,7,14,21,30)__ |
| Check if the custom event occurred __exactly X (Max = 50) number of times__ | __EXACTLY__ | in the past __Y Days (Y = 1,3,7,14,21,30)__ |

Braze notes the number of times these events have occurred as well as the last time they were performed by each user for segmentation. On the [custom events analytics page][7] you can view in aggregate how often each custom event occurs, as well as by segment over time for more detailed analysis. This is particularly useful to view how your campaigns have affected custom event activity by looking at the gray lines Braze overlays on the time-series to indicate the last time a campaign was sent.

![custom_event_analytics_example.png][8]

{% alert tip %}
[Incrementing Custom Attributes]({{ site.baseurl }}/user_guide/data_and_analytics/custom_data/custom_attributes/#integers) can be used to keep a counter on a user action similar to a custom event. However, you will not be able to view custom attribute data in a time-series. User actions that do not need to be analyzed in time-series should be recorded via this method.
{% endalert %}

## Custom Event Storage

All User Profile data (Custom Events, Custom Attribute, Custom Data) is stored as long as those profiles are active. If you'd like to leverage Event Properties for Segmentation, please contact your Braze account or customer success manager.


# Custom Event Properties

With Custom Event Properties, you can set properties on custom events and purchases. These properties can then be used for further qualifying trigger conditions, increasing personalization in messaging, and generating more sophisticated analytics through raw data export. Property values can be string, numeric, boolean, or Date objects. However, property values cannot be array objects.

For example, if an eCommerce application wanted to send a message to a user when he/she abandons their cart, it could additionally improve its target audience and allow for increased campaign personalization by adding a Custom Event Property of the 'cart value' of users' carts.

{% alert important %}
Each Custom Event or Purchase can have up to 256 distinct Custom Event Properties. If a Custom Event or Purchase is logged with more than 256 properties, only the first 256 will be captured and available for use.
{% endalert %}

![customEventProperties.png][16]

Custom Event Properties can also be used for personalization within the messaging template. Any campaign using [Action-Based Delivery][19] with a trigger event can use custom event properties from that event for messaging personalization. If a gaming application wanted to send a message to users who had completed a level, it could further personalize the message with a property for the time it took users to complete that level. In this example, the message is personalized for three different segments using [conditional logic][18].  The Custom Event Property called ``time_spent``, can be included in the message by calling ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``.

{% alert warning %}
Triggered in-app messages with templated custom event properties (for example, ``{event_properties.${time_spent}}}``) will fail gracefully and not display if there is no Internet connectivity.
{% endalert %}

Custom Event Properties are designed to help you personalize your messaging or build granular Action-Based Delivery Campaigns. If you would like to create segments based on event property recency and frequency, please reach out to your Customer Success Manager, as this may incur additional data costs.

You can change the data type of your custom event, but you should be aware of [what other changes this action entails]({{ site.baseurl }}/help/help_articles/data/change_custom_data_type/).

{% alert important %}
Braze will ban or block users ("dummy users") with over 5 million sessions and no longer ingest their SDK events because they are usually the result of misintegration. If you find that this has happened for a legitimate user, please reach out to your Braze account manager.
{% endalert %}

[7]: https://dashboard-01.braze.com/dashboard/custom_events/
[8]: {% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png"
[9]: http://www.regextester.com/pregsyntax.html
[10]: #integers
[11]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/
[12]: #automatic-data-collection
[13]: {{ site.baseurl }}/user_guide/personalization_and_dynamic_content/overview/#personalized-messaging
[14]: #taxiride-sharing-app-use-case
[15]: #customeventproperties
[16]: {% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png"
[17]: {% image_buster /assets/img_archive/custom_event_properties_gaming.png %} "custom_event_properties_gaming.png"
[18]: {{ site.baseurl }}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
[19]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/scheduling_your_campaign/#action-based-delivery-event-triggered-campaigns
