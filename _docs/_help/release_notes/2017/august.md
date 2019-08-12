---
nav_title: August
page_order: 5
---

# August 2017

## Update to Push Action Buttons

We added support for [push action buttons][70] to our REST API messaging endpoints.

## Update to Liquid Templating

You can now [personalize a message][69] based on:
- The device it was sent to,
- Device ID,
- Carrier,
- IDFA,
- Model,
- OS, and
- Platform

## API Triggered Canvas

You can now trigger a [Canvas][68] via API endpoints (send, schedule, update, delete) that match the existing ones for Campaigns, allowing you to further automate and optimize your marketing.

## Web Push Action Buttons

We’ve added support for push action buttons on the web SDK for Chrome, allowing you increase your engagement by giving your users contextual choices that simplify their busy lives. Learn more about best practices for push notifications [here][66].

## New API Endpoints

We’ve exposed new API endpoints, /email/hard_bounces, that lets you pull hard bounces by email address or in a given date range, and /messages/scheduled_broadcasts, that lets you pull the next time that scheduled Campaigns and scheduled-entry Canvases will begin. These new endpoints allow you for further customization and optimization of your campaigns. Learn more about our API endpoints [here][65].

## Geofences

We’ve added a new feature, Geofences, that allows you to trigger messages in real-time when customers enter and exit defined geographical areas, enabling personalized, relevant communication with your customers. Learn more about location marketing in [Academy][64].

## Update to Email Editor

We’ve added dynamic autocompleting to our new email editor, so you can now autocomplete with your customers’ actual custom attributes and events when using Liquid, making your life easier. Learn more about email best practices in [Academy][63].

## Update to Date Filters

We’ve added a “never” date filter so you can target customers who have never received or interacted with one of your message, enabling you to have clean customer lists and ensure email deliverability. Learn more about filters [here][62].

## Update to Canvas

We’ve added percentages to the top of each Canvas variant so now, you can see which variants are performing better at a glance. Learn more about Canvas [here][61].

## Canvas with Intelligent Selection

Canvas now has Intelligent Selection, allowing you to test your Canvases with more efficiency. Learn more about our Intelligence Suite [here][60].

## Update to Email Display Names

We’ve added support of special UTF-8 characters in email display names, so you can create even more personalized emails for your customers. Learn more about email best practices [here][67].

## Engagement Reports CSV Aggregation

Now, you can receive consolidated data for every campaign and every Canvas in two separate files regardless of how many campaigns or canvases are selected, allowing you to have all the data you need, when you need it. Learn more about Engagement Reports [here][59].

> Update: As noted in our [September 2017 release notes]({{ site.baseurl }}/help/release_notes/2017/august/#september-2017), you can now aggregate data from a specific period of time as well as schedule exports to run on a recurring basis.



[1]: {% image_buster /assets/img_archive/exception_event_trigger.png %}
[2]: {% image_buster /assets/img_archive/has_received_tag.png %}
[3]: {% image_buster /assets/img_archive/group_pause.png %}
[4]: {{ site.baseurl }}/developer_guide/rest_api/export/#kpi-export
[5]: {% image_buster /assets/img_archive/improved_error_log.png %}
[6]: {% image_buster /assets/img_archive/uninstall_tracking_checkbox.png %}
[7]: {% image_buster /assets/img_archive/test_send_on_webhooks.png %}
[8]: {% image_buster /assets/img_archive/export_campaign_recipients.png %}
[9]: {% image_buster /assets/img_archive/IAM_impression_cap.png %}
[10]: {% image_buster /assets/img_archive/developer_console_filter.png %}
[11]: {% image_buster /assets/img_archive/approx_limit_for_IAM.png %}
[12]: {{ site.baseurl }}/developer_guide/rest_api/messaging/#connected-audience-object
[13]: https://www.braze.com/blog/connected-audiences/
[14]: {{ site.baseurl }}/help/troubleshooting_guide/troubleshooting_guide/#email
[15]: {{ site.baseurl }}/user_guide/engagement_tools/canvas/create_a_canvas/branching/#branching
[16]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/scheduling_your_campaign/
[17]: {{ site.baseurl }}/user_guide/data_and_analytics/exporting_dashboard_data/#exporting-dashboard-data
[18]: {{ site.baseurl }}/help/troubleshooting_guide/troubleshooting_guide/#email
[19]: {{ site.baseurl }}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[20]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[21]: {{ site.baseurl }}/user_guide/engagement_tools/segments/creating_a_segment/
[22]: {{ site.baseurl }}/user_guide/data_and_analytics/your_reports/engagement_reports/#engagement-reports
[23]: {{ site.baseurl }}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#creating-a-canvas
[24]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/scheduling_your_campaign/#setting-up-a-triggered-campaign
[25]: {{ site.baseurl }}/user_guide/data_and_analytics/your_reports/engagement_reports/#engagement-reports
[26]: {{ site.baseurl }}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#creating-a-webhook
[27]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#retargeting-campaigns
[28]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#retargeting-campaigns
[29]: {{ site.baseurl }}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking
[30]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[31]: {{ site.baseurl }}/user_guide/data_and_analytics/influenced_opens/#influenced-opens
[32]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#ios-10-rich-notifications
[33]: {{ site.baseurl }}/user_guide/engagement_tools/news_feed/creating_a_news_feed_item/#news-feed-cards
[34]: {{ site.baseurl }}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
[35]: {{ site.baseurl }}/user_guide/data_and_analytics/your_reports/engagement_reports/#engagement-reports
[36]: {{ site.baseurl }}/help/best_practices/email/#what-is-ip-warming
[37]: {{ site.baseurl }}/user_guide/data_and_analytics/configuring_reporting/
[38]: {{ site.baseurl }}/user_guide/personalization_and_dynamic_content/personalized_messaging/#adding-personalizable-attributes-objects
[39]: {{ site.baseurl }}/help/best_practices/push/
[40]: {{ site.baseurl }}/user_guide/engagement_tools/templates_and_media/
[41]: {{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/create/#creating-an-in-app-message
[42]: {{ site.baseurl }}/user_guide/administrative/app_settings/tags/#campaign-segment-and-news-feed-card-tags
[43]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/#content-test-groups
[44]: {{ site.baseurl }}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment
[45]: {{ site.baseurl }}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/
[46]: {{ site.baseurl }}/user_guide/onboarding/platform_administrative_features/#security-settings
[47]: {{ site.baseurl }}/help/best_practices/web_sdk/#web-push
[48]: {{ site.baseurl }}/help/best_practices/in-app_messages/
[49]: {{ site.baseurl }}/developer_guide/rest_api/messaging/#overview
[50]: {{ site.baseurl }}/user_guide/administrative/manage_your_users/user_import/#user-import
[51]: {{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/create/#step-5-preview-message
[52]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#targeting-filters
[53]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#step-6-preview-message
[54]: {{ site.baseurl }}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template
[55]: {{ site.baseurl }}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[56]: {{ site.baseurl }}/developer_guide/rest_api/basics/#what-is-a-rest-api
[57]: {{ site.baseurl }}/help/troubleshooting_guide/troubleshooting_guide/#email
[58]: {{ site.baseurl }}/help/best_practices/web_sdk/#web-push
[59]: {{ site.baseurl }}/user_guide/data_and_analytics/engagement_reports/#creating-a-new-report
[60]: {{ site.baseurl }}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/
[61]: {{ site.baseurl }}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/
[62]: {{ site.baseurl }}/user_guide/engagement_tools/segments/segmentation_filters/#segmentation-filters
[63]: {{ site.baseurl }}/help/troubleshooting_guide/troubleshooting_guide/#email
[64]: {{ site.baseurl }}/developer_guide/platform_integration_guides/fireos/advanced_use_cases/locations_and_geofences/#locations--geofences
[65]: {{ site.baseurl }}/developer_guide/rest_api/basics/#what-is-a-rest-api
[66]: {{ site.baseurl }}/help/best_practices/push/
[67]: {{ site.baseurl }}/help/troubleshooting_guide/troubleshooting_guide/#email
[68]: {{ site.baseurl }}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/
[69]: {{ site.baseurl }}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[70]: {{ site.baseurl }}/user_guide/message_building_by_channel/push/push_action_buttons/#how-to-use-action-buttons
[71]: {{ site.baseurl }}/developer_guide/rest_api/api_network_connectivity_issues/#whitelisting-brazes-api-endpoint-ip-ranges
[72]: {{ site.baseurl }}/user_guide/data_and_analytics/your_reports/engagement_reports/#engagement-reports
[73]: {{ site.baseurl }}/user_guide/engagement_tools/segments/using_user_search/#using-user-search
[74]: {{ site.baseurl }}/user_guide/message_building_by_channel/push/push_stories/
[75]: {{ site.baseurl }}/partners/braze_currents/how_it_works/
[76]: {{ site.baseurl }}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#custom-footer
[77]: {{ site.baseurl }}/user_guide/onboarding/platform_administrative_features/#notification-preferences
[78]: {{ site.baseurl }}/user_guide/onboarding/platform_administrative_features/#slack-incoming-webhook-integration
[79]: {{ site.baseurl }}/user_guide/engagement_tools/templates_and_media/media_library/#media-library
[80]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#recommended-option-using-a-p8-file-authentication-tokens
[81]: {{ site.baseurl }}/user_guide/data_and_analytics/your_reports/engagement_reports/#engagement-reports
[82]: {{ site.baseurl }}/developer_guide/rest_api/export/#users-by-identifier-endpoint
[83]: https://dashboard-01.braze.com/app_settings/app_settings/email/
[84]: {{ site.baseurl }}/user_guide/message_building_by_channel/email/css_inline/#css-inlining
[85]: {{ site.baseurl }}/developer_guide/rest_api/basics/#api-ip-whitelisting
[86]: {{ site.baseurl }}/developer_guide/rest_api/basics/#app-group-rest-api-keys
[87]: {{ site.baseurl }}/developer_guide/rest_api/email_templates/#email-templates
[88]: {{ site.baseurl }}/developer_guide/rest_api/export/#user-export
[89]: {{ site.baseurl }}/help/best_practices/utilizing_badge_count/#utilizing-badge-count
[90]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/push_notifications/troubleshooting/#step-1-configuring-the-push-certificate-and-provisioning-profile
[91]: {{ site.baseurl }}/user_guide/message_building_by_channel/email/link_templates/#link-templates
[92]: {{ site.baseurl }}/user_guide/onboarding/platform_administrative_features/#custom-event-and-attribute-management
[93]: {{ site.baseurl }}/user_guide/message_building_by_channel/push/push_stories/
[94]: {{ site.baseurl }}/user_guide/data_and_analytics/uninstall_tracking/#uninstall-tracking-for-campaigns
[95]: {{ site.baseurl }}/user_guide/message_building_by_channel/push/push_stories/#push-stories
[96]: {{ site.baseurl }}/user_guide/message_building_by_channel/email/inbox_vision/#inbox-vision
[97]: {{ site.baseurl }}/user_guide/message_building_by_channel/email/creating_an_email_template/#step-2-create-or-choose-a-template
[98]:{{ site.baseurl }}/user_guide/onboarding/platform_administrative_features/#authentication-rules
