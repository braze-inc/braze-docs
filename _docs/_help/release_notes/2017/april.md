---
nav_title: April
page_order: 9
---

# April 2017

## HTML In Browser Messages
We now support interactive in-browser message types including custom HTML and email capture formats, enabling you to reach your customers wherever they are. Learn more about in app messages [here][48].

## Personalized In-App Message with Connected Content

We’ve added {% raw %} {%connected_content%} {% endraw %} blocks in triggered in-app messages which allows you to add rich personalization by inserting any information accessible via API directly into your messages. Now, you can use Connected Content inside your app in addition to your push, email and webhooks. Learn more about Connected Content [here][34].

## Improved Navigation for News Feed cards
We’ve improved the UI for building News Feed cards, making it easier for you to navigate and create your campaigns. Learn more about News Feed cards [here][33].

## Improved Preview for iOS Rich Notifications
Our preview notifications on iOS now display Rich notifications giving you a clear view of exactly what you are sending out to your customers, down to the font size. Learn more about iOS Rich notifications [here][32].

## Added “Influenced Opens” to Push Statistics
We’ve added “Influenced Opens” to our list of standard Campaign and Canvas statistics offered in Braze, making it easier to know your campaigns breakdown of Influenced, Direct and Total Opens. Learn more about Influenced Opens [here][31].

## Upgrade to Internal Groups

You can now create multiple Internal Groups and assign properties indicating whether the group will be used for SDK logging, REST API logging, or message content testing. Learn more about event user logs and testing [here][30].

> Update: Internal Groups can also be used to [send seed emails]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/#seed-groups).

## New Options for Web URLs

You now have the option of opening Web URLs in an external web browser for push messages, in-app and in-browser messages, and News Feed cards. The "Deep Link into App" action is also now compatible with HTTP/HTTPs deep links. If using a partner like Branch or Apple's Universal Links, you'll require SDK customization. Learn more about deep linking [here][29].

## New "Perform Conversion" Event Canvas

We've added a new "Performed Conversion" event and an "In Canvas Control" filter for improved retargeting options. Learn more about using retargeting filters [here][28].



[4]: {{site.baseurl}}/developer_guide/rest_api/export/#kpi-export
[5]: {% image_buster /assets/img_archive/improved_error_log.png %}
[6]: {% image_buster /assets/img_archive/uninstall_tracking_checkbox.png %}
[11]: {% image_buster /assets/img_archive/approx_limit_for_IAM.png %}
[12]: {{site.baseurl}}/developer_guide/rest_api/messaging/#connected-audience-object
[13]: https://www.braze.com/blog/connected-audiences/
[14]: {{site.baseurl}}/help/troubleshooting_guide/troubleshooting_guide/#email
[15]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/branching/#branching
[16]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/scheduling_your_campaign/
[17]: {{site.baseurl}}/user_guide/data_and_analytics/exporting_dashboard_data/#exporting-dashboard-data
[18]: {{site.baseurl}}/help/troubleshooting_guide/troubleshooting_guide/#email
[19]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[20]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[21]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/
[22]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/engagement_reports/#engagement-reports
[23]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#creating-a-canvas
[24]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/scheduling_your_campaign/#setting-up-a-triggered-campaign
[25]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/engagement_reports/#engagement-reports
[26]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#creating-a-webhook
[27]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#retargeting-campaigns
[28]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#retargeting-campaigns
[29]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking
[30]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[31]: {{site.baseurl}}/user_guide/data_and_analytics/influenced_opens/#influenced-opens
[32]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#ios-10-rich-notifications
[33]: {{site.baseurl}}/user_guide/engagement_tools/news_feed/creating_a_news_feed_item/#news-feed-cards
[34]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
[35]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/engagement_reports/#engagement-reports
[36]: {{site.baseurl}}/help/best_practices/email/#what-is-ip-warming
[37]: {{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/
[38]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/personalized_messaging/#adding-personalizable-attributes-objects
[39]: {{site.baseurl}}/help/best_practices/push/
[40]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/
[41]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#creating-an-in-app-message
[42]: {{site.baseurl}}/user_guide/administrative/app_settings/tags/#campaign-segment-and-news-feed-card-tags
[43]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/#content-test-groups
[44]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment
[45]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/
[46]: {{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#security-settings
[47]: {{site.baseurl}}/help/best_practices/web_sdk/#web-push
[48]: {{site.baseurl}}/help/best_practices/in-app_messages/
[49]: {{site.baseurl}}/developer_guide/rest_api/messaging/#overview
[50]: {{site.baseurl}}/user_guide/administrative/manage_your_users/user_import/#user-import
[51]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#step-5-preview-message
[52]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#targeting-filters
[53]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#step-6-preview-message
[54]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template
[55]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[56]: {{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api
[57]: {{site.baseurl}}/help/troubleshooting_guide/troubleshooting_guide/#email
[58]: {{site.baseurl}}/help/best_practices/web_sdk/#web-push
[59]: {{site.baseurl}}/user_guide/data_and_analytics/engagement_reports/#creating-a-new-report
[60]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/
[61]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/
[62]: {{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#segmentation-filters
[63]: {{site.baseurl}}/help/troubleshooting_guide/troubleshooting_guide/#email
[64]: {{site.baseurl}}/developer_guide/platform_integration_guides/fireos/advanced_use_cases/locations_and_geofences/#locations--geofences
[65]: {{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api
[66]: {{site.baseurl}}/help/best_practices/push/
[67]: {{site.baseurl}}/help/troubleshooting_guide/troubleshooting_guide/#email
[68]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/
[69]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[70]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_action_buttons/#how-to-use-action-buttons
[71]: {{site.baseurl}}/developer_guide/rest_api/api_network_connectivity_issues/#whitelisting-brazes-api-endpoint-ip-ranges
[72]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/engagement_reports/#engagement-reports
[73]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#using-user-search
[74]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_stories/
[75]: {{site.baseurl}}/partners/braze_currents/how_it_works/
[76]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#custom-footer
[77]: {{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#notification-preferences
[78]: {{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#slack-incoming-webhook-integration
[79]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#media-library
[80]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#recommended-option-using-a-p8-file-authentication-tokens
[81]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/engagement_reports/#engagement-reports
[82]: {{site.baseurl}}/developer_guide/rest_api/export/#users-by-identifier-endpoint
[83]: https://dashboard-01.braze.com/app_settings/app_settings/email/
[84]: {{site.baseurl}}/user_guide/message_building_by_channel/email/css_inline/#css-inlining
[85]: {{site.baseurl}}/developer_guide/rest_api/basics/#api-ip-whitelisting
[86]: {{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys
[87]: {{site.baseurl}}/developer_guide/rest_api/email_templates/#email-templates
[88]: {{site.baseurl}}/developer_guide/rest_api/export/#user-export
[89]: {{site.baseurl}}/help/best_practices/utilizing_badge_count/#utilizing-badge-count
[90]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/troubleshooting/#step-1-configuring-the-push-certificate-and-provisioning-profile
[91]: {{site.baseurl}}/user_guide/message_building_by_channel/email/link_templates/#link-templates
[92]: {{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#custom-event-and-attribute-management
[93]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_stories/
[94]: {{site.baseurl}}/user_guide/data_and_analytics/uninstall_tracking/#uninstall-tracking-for-campaigns
[95]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_stories/#push-stories
[96]: {{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#inbox-vision
[97]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/#step-2-create-or-choose-a-template
[98]:{{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#authentication-rules
