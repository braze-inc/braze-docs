---
nav_title: The HTML Looks Strange
page_order: 0
---

# The HTML Looks Strange When I Send A Test Email To Myself

If your [Test Email][37] looks off, we recommend that you...

* [Check HTML](#check-html-setup),
* [Check Conflicts](#check-conflicts),
* [Check Rendering](#check-rendering), or
* [Switch CSS In-lining](#switch-css-in-lining).

### Check HTML Setup

First, confirm with your developers that your HTML is set up properly.

### Check Conflicts

Certain Chrome extensions will cause issues with Braze’s email editor (one example is [Grammarly][38]). If you’re using one of these, you should either: 
- edit Braze emails in a browser that does not have Grammarly
- contact your Braze account manager and ask to flip your email editors to HTML only/plain text. 

NB plain text view removes your ```WYSIWYG``` (what you see is what you get) editor, so you should first ensure that all team members are comfortable with HTML before making this request.

### Check Rendering

Emails render differently on different browsers and email clients. Record which browsers and email clients you’re experiencing issues with.

- Preview your emails in a program like [Email on Acid][39] or [Litmus][40]. These allow you to preview what emails look like in different browsers and email clients.

- Once you’ve identified which browsers/email clients are causing issues, let your developer team know that they’ll need to modify their HTML and make edits to accommodate those browsers/email clients.

### Switch CSS In-lining

There are times when the preview in Email on Acid or Litmus still does not match what is sent via the Braze dashboard. One possible cause for this is the CSS in-lining that is performed by Braze may differ from the CSS in-lining performed by other tools. If you suspect that this is the case, contact your BRaze account manager to ask for CSS in-lining to be turned off.

Still need help? [Open a support ticket]({{ site.baseurl }}/support_contact/), or leave feedback below.

[1]: {{ site.baseurl }}/user_guide/engagement_tools/segments/using_user_search/#overview-tab
[2]: {% image_buster /assets/img_archive/trouble1.png %}
[3]: {% image_buster /assets/img_archive/trouble2.png %}
[4]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#freq-cap-feat-over
[5]: {% image_buster /assets/img_archive/trouble3.png %}
[6]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#step-5-distribute-users-among-your-variants
[7]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#in-campaign-control-group-filter
[8]: {{ site.baseurl }}/user_guide/data_and_analytics/exporting_dashboard_data/#exporting-to-csv
[9]: {{ site.baseurl }}/help/release_notes/2016/september/#segment-changelogs
[10]: {% image_buster /assets/img_archive/trouble4.png %}
[11]: {% image_buster /assets/img_archive/trouble5.png %}
[12]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/in-app_messaging/#logging-impressions-and-clicks
[13]: {{ site.baseurl }}/developer_guide/platform_integration_guides/fireos/in-app_messaging/#setting-custom-listeners
[14]: {% image_buster /assets/img_archive/trouble6.png %}
[15]: {{ site.baseurl }}/help/best_practices/in-app_messages/#in-app-message-specs
[16]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/tracking_sessions/
[17]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/
[18]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/
[19]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/in-app_messaging/#minimum-time-interval-between-triggers
[20]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/#minimum-time-interval-between-triggers
[21]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/in_app_messaging/#minimum-time-interval-between-triggers
[22]: {{ site.baseurl }}/user_guide/data_and_analytics/user_data_collection/#custom-event-properties
[23]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/logging_purchases/#properties-purchases
[24]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[25]: {% image_buster /assets/img_archive/trouble7.png %}
[26]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/advanced_use_cases/locations_and_geofences/
[27]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/location_tracking/
[28]: {% image_buster /assets/img_archive/trouble8.png %}
[29]: {% image_buster /assets/img_archive/trouble9.png %}
[30]: {% image_buster /assets/img_archive/trouble10.png %}
[33]: {% image_buster /assets/img_archive/NikeSneakers.png %}
[34]: {% image_buster /assets/img_archive/VennDiagram.png %}
[35]: {{ site.baseurl }}/user_guide/data_and_analytics/viewing_and_understanding_segment_data/#user-preview
[36]: {{ site.baseurl }}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[37]: {{ site.baseurl }}/developer_guide/platform_wide/sending_test_messages/#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa
[38]: https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en
[39]: https://www.emailonacid.com/
[40]: https://litmus.com/
[41]: {% image_buster /assets/img_archive/trouble15.png %}
[42]: {% image_buster /assets/img_archive/trouble16.png %}
[43]: {% image_buster /assets/img_archive/trouble17.png %}
[44]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#step-2-add-conversion-events
[45]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-tracking-rules
[46]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[47]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting
[48]: {% image_buster /assets/img_archive/targeting_error.png %}
[49]: {% image_buster /assets/img_archive/us_canada.png %}
[50]: {% image_buster /assets/img_archive/not_us_not_canada.png %}
