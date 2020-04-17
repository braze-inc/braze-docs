---
nav_title: July
page_order: 6
---

# July 2017

## Large Images In Web Push

We’ve added support for large images for Web Push on Chrome for Windows and Android, giving you the ability to create rich, engaging customer experiences. Learn more about web push [here][58].

## Updates to Email Fields

You can now lock emails to a specific set of from-addresses, ensuring that you don’t accidentally input the wrong address. The email composition form will be pre-populated with addresses used in the last 6 months to streamline the process. Learn more about email best practices [here][57].

## Updates to Campaign Details API

The /campaign/details API endpoint now gives information about its messages, allowing you to pull subject, HTML body, from-address, and reply-to fields using the API. Learn more about our APIs [here][56].

## Updates to Liquid Templating

We’ve added the ability to template variant attributes in Canvases and Campaigns. In Canvas, you can now template both the variant’s API id as well as the variant’s name, and in Campaigns you can now template a message’s message_api_id and message_name. Both updates allow for more flexibility in your messaging, allowing you to build personalized campaigns. Learn more about personalized messaging [here][55].

## New HTML Email Editor

You can now easily write and test emails with a full-screen HTML editor that enables live preview, personalization via Liquid and an improved full-screen text editor with line numbers and syntax highlighting. Learn more about email composition [here][54].

## Updates to Previews

You can now follow the screen window as you scroll down message previews in Campaigns & Canvas, ensuring that you can always see the changes reflected. Learn more about previewing and testing [here][53].

## New Segment Membership filter

We added a new filter, Segment Membership, enabling you to target users based off their membership in any of your existing segments. In addition, we’ve added the ability to use of both “And” and “Or” logic in segment filters, as well as the ability to nest segments within each other. These updates enable you to send customized messages to your customers with more precision. Learn more about filters [here][52].

## Update to Android Preview

We updated the Android preview to reflect more recent versions of Android since Android N.  Learn more about preview messages [here][51].


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
