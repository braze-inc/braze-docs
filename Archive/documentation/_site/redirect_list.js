
  function removeleadingslash(str){
    var rstr = str;
    if (rstr.slice(-1) === "/") {
      rstr = rstr.slice(0, -1);
    }
    return rstr;
  }

(function(){
  //lower case name => path name

  var validurls = {};
  var urlpath = removeleadingslash(window.location.pathname);
  var urlsearch = window.location.search;
  var pagetype = urlpath.split('/');


  var siteurl = '';
    validurls['/academy'] = '/docs/user_guide/introduction/';
    validurls['/academy/best_practices/#android-push-category'] = '/docs/help/best_practices/push/additional_android_best_practices/#android-push-category';
    validurls['/academy/best_practices/#android-push-priority'] = '/docs/help/best_practices/push/additional_android_best_practices/#android-push-priority';
    validurls['/academy/best_practices/#android-push-visibility'] = '/docs/help/best_practices/push/additional_android_best_practices/#android-push-visibility';
    validurls['/academy/best_practices/#body-styling'] = '/docs/help/best_practices/email/email_styling_tips/#body-styling';
    validurls['/academy/best_practices/#email'] = '/docs/help/best_practices/email/overview/';
    validurls['/academy/best_practices/email#managing-email-subscriptions'] = '/docs/help/best_practices/email/managing_email_subscriptions/';
    validurls['/academy/best_practices/email'] = '/docs/help/best_practices/email/managing_email_subscriptions/';
    validurls['/academy/best_practices/'] = '/docs/help/home/';

    validurls['/academy/dashboard_features/#changing-email-subscriptions'] = '/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions';
    validurls['/academy/dashboard_features/#common-errors'] = '/docs/user_guide/data_and_analytics/user_data_collection/user_import/#common-errors';
    validurls['/academy/dashboard_features/#conversion-events'] = '/docs/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events';
    validurls['/academy/dashboard_features/#creating-a-webhook'] = '/docs/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#creating-a-webhook';
    validurls['/academy/dashboard_features/#creating-geofence-sets-via-bulk-upload'] = '/docs/user_guide/engagement_tools/locations_and_geofences/creating_geofences/#creating-geofence-sets-via-bulk-upload';
    validurls['/academy/dashboard_features/#css-inlining'] = '/docs/user_guide/message_building_by_channel/email/css_inline/#css-inlining';
    validurls['/academy/dashboard_features/#dashboard-fallback-channel'] = '/docs/user_guide/message_building_by_channel/push/notification_channels/#dashboard-fallback-channel';
    validurls['/academy/dashboard_features/#event-user-logs'] = '/docs/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab';
    validurls['/academy/dashboard_features/#frequency-capping'] = '/docs/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#frequency-capping';
    validurls['/academy/dashboard_features/#json-keyvalue-pairs'] = '/docs/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#step-3-create-the-request-body';
    validurls['/academy/dashboard_features/#locations--geofences'] = '/docs/developer_guide/platform_integration_guides/fireos/advanced_use_cases/locations_and_geofences/#locations--geofences';
    validurls['/academy/dashboard_features/#news-feed-categories'] = '/docs/user_guide/engagement_tools/news_feed/news_feed_categories/';
    validurls['/academy/dashboard_features/#notification-channels'] = '/docs/user_guide/message_building_by_channel/push/notification_channels/#notification-channels';
    validurls['/academy/dashboard_features/#user-import'] = '/docs/user_guide/data_and_analytics/user_data_collection/user_import/';
    validurls['/academy/dashboard_features/'] = '/docs/user_guide/introduction/';
    validurls['/academy/deep_dives/conversion_events'] = '/docs/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/';
    validurls['/academy/deep_dives/creating_a_webhook'] = '/docs/user_guide/message_building_by_channel/webhooks/creating_a_webhook/';
    validurls['/academy/deep_dives/multivariate_testing#intelligent-selection'] = '/docs/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#intelligent-selection';
    validurls['/academy/deep_dives/multivariate_testing'] = '/docs/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/';

    validurls['/academy/message_building_and_personalization/personalization/#connected-content'] = '/docs/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/';
    validurls['/academy/quick_wins/personalized_messaging#conditionals'] = '/docs/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/';
    validurls['/academy/quick_wins/personalized_messaging'] = '/docs/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/';

    validurls['/academy/getting_started'] = '/docs/user_guide/onboarding_with_braze/overview/';
    validurls['/academy/getting_started#list-unsubscribe-settings'] = '/docs/user_guide/administrative/manage_your_braze_users/company-wide_settings_management/#list-unsubscribe-settings';
    validurls['/academy/quick_wins/optimal_send_time'] = '/docs/user_guide/intelligence/intelligent_timing/';
    validurls['/academy/scheduling_and_organizing_campaigns/#intelligent-delivery'] = '/docs/user_guide/intelligence/intelligent_timing/';
    validurls['/academy/troubleshooting_guide/'] = '/docs/help/home/';
    validurls['/academy/user_targeting/#external-user-id'] = '/docs/developer_guide/rest_api/messaging/#external-user-id';

    validurls['/documentation/android/#advanced-settings'] = '/docs/developer_guide/platform_integration_guides/android/push_notifications/advanced_settings/';
    validurls['/documentation/android/#locations--geofences'] = '/docs/developer_guide/platform_integration_guides/fireos/advanced_use_cases/locations_and_geofences/#locations--geofences';
    validurls['/documentation/android/#push-notifications'] = '/docs/developer_guide/platform_integration_guides/android/push_notifications/integration/';
    validurls['/documentation/android/#step-4-define-notification-channels'] = '/docs/developer_guide/platform_integration_guides/android/push_notifications/integration/#step-4-define-notification-channels';
    validurls['/documentation/android/#step-4-set-your-firebase-credentials'] = '/docs/developer_guide/platform_integration_guides/android/push_notifications/integration/#step-4-set-your-firebase-credentials';
    validurls['/documentation/android/#uninstall-tracking'] = '/docs/developer_guide/platform_integration_guides/android/analytics/uninstall_tracking/#uninstall-tracking';
    validurls['/documentation/auto_advance'] = '/docs/auto_advance/';
    validurls['/documentation/enabling_message_channels/push_notifications/baidu'] = '/docs/developer_guide/platform_integration_guides/android/push_notifications/integration_baidu/';
    validurls['/documentation/enabling_message_channels/push_notifications/ios'] = '/docs/developer_guide/platform_integration_guides/ios/push_notifications/integration/';

    validurls['/documentation/ios/#push-notifications'] = '/docs/developer_guide/platform_integration_guides/ios/push_notifications/integration/';
    validurls['/documentation/partner_integrations/#adjust'] = '/docs/partners/adjust/';
    validurls['/documentation/frequently_asked_questions#local-timezone-delivery'] = '/docs/help/faqs/#what-does-local-time-zone-delivery-offer';
    validurls['/documentation/frequently_asked_questions'] = '/docs/help/faqs/';

    validurls['/documentation/partner_integrations/#appsflyer'] = '/docs/partners/appsflyer/';
    validurls['/documentation/partner_integrations/#branch'] = '/docs/partners/branch_for_attribution/';
    validurls['/documentation/partner_integrations/#kochava'] = '/docs/partners/kochava/';
    validurls['/documentation/partner_integrations/#singular'] = '/docs/partners/singular/';
    validurls['/documentation/partner_integrations/#tune-mobileapptracking'] = '/docs/partners/tune/';
    validurls['/documentation/partner_integrations/'] = '/docs/partners/';
    validurls['/documentation/platform_wide/#app-group-configuration'] = '/docs/developer_guide/platform_wide/app_group_configuration/#app-group-configuration';
    validurls['/documentation/rest_api/#email-sync'] = '/docs/developer_guide/rest_api/email_sync/';
    validurls['/documentation/rest_apis/email-sync'] = '/docs/developer_guide/rest_api/email_sync/';
    validurls['/documentation/rest_apis/email_sync'] = '/docs/developer_guide/rest_api/email_sync/';
    validurls['/docs/user_guide/data_and_analytics/engagement_reports/#engagement-reports'] = '/docs/user_guide/data_and_analytics/your_reports/engagement_reports/#engagement-reports';

    validurls['/documentation/rest_api/#export'] = '/docs/developer_guide/rest_api/export/#export';
    validurls['/documentation/rest_apis/export'] = '/docs/developer_guide/rest_api/export/#export';

    validurls['/documentation/rest_api/#messaging'] = '/docs/developer_guide/rest_api/messaging/';
    validurls['/documentation/rest_api/#user-data'] = '/docs/developer_guide/rest_api/user_data/#user-data';
    validurls['/documentation/rest_apis/user-data'] = '/docs/developer_guide/rest_api/user_data/#user-data';
    validurls['/documentation/rest_apis/user_data'] = '/docs/developer_guide/rest_api/user_data/#user-data';

    validurls['/documentation/rest_api/messaging'] = '/docs/developer_guide/rest_api/messaging/';
    validurls['/documentation/rest_apis/messaging'] = '/docs/developer_guide/rest_api/messaging/';
    validurls['/documentation/rest_api/#endpoints'] = '/docs/developer_guide/rest_api/basics/#endpoints';
    validurls['/documentation/rest_apis/endpoints'] = '/docs/developer_guide/rest_api/basics/#endpoints';
    validurls['/documentation/rest_api/#user-track-endpoint'] = '/docs/developer_guide/rest_api/user_data/#user-track-endpoint';
    validurls['/documentation/rest_api/#users-by-segment-endpoint'] = '/docs/developer_guide/rest_api/export/#users-by-segment-endpoint';

    validurls['/documentation/rest_apis/'] = '/docs/developer_guide/rest_api/basics/';
    validurls['/documentation/web'] = '/docs/developer_guide/platform_integration_guides/web/initial_sdk_setup/';
    validurls['/documentation/platform_wide/'] = '/docs/developer_guide/home/';
    validurls['/academy/home/'] = '/docs/user_guide/introduction/';

    validurls['/documentation/android'] = '/docs/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/';
    validurls['/documentation/fireos'] = '/docs/developer_guide/platform_integration_guides/fireos/initial_sdk_setup/';
    validurls['/documentation/ios'] = '/docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/initial_sdk_setup/';
    validurls['/documentation/windows_universal'] = '/docs/developer_guide/platform_integration_guides/windows_universal/initial_sdk_setup/';
    validurls['/documentation/web'] = '/docs/developer_guide/platform_integration_guides/web/initial_sdk_setup/';
    validurls['/documentation/tvos'] = '/docs/developer_guide/platform_integration_guides/tvos/initial_sdk_setup/';
    validurls['/documentation/sdk_integration/unity/ios'] = '/docs/developer_guide/platform_integration_guides/unity/ios/sdk_integration/';
    validurls['/documentation/sdk_integration/xamarin/ios'] = '/docs/developer_guide/platform_integration_guides/xamarin/ios/sdk_integration/';
    validurls['/documentation/cordova/ios'] = '/docs/developer_guide/platform_integration_guides/cordova/ios/initial_sdk_setup/';
    validurls['/documentation/react_native/ios'] = '/docs/developer_guide/platform_integration_guides/react_native/ios/sdk_integration/';

    validurls['/documentation/android/'] = '/docs/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/';
    validurls['/documentation/eclipse_setup/'] = '/docs/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#android-sdk-integration';
    validurls['/documentation/cordova/android_and_fireos/'] = '/docs/developer_guide/platform_integration_guides/cordova/android_and_fireos/initial_sdk_setup/';
    validurls['/documentation/cordova/ios/'] = '/docs/developer_guide/platform_integration_guides/cordova/ios/cordova_integration/';
    validurls['/documentation/fireos/'] = '/docs/developer_guide/platform_integration_guides/fireos/initial_sdk_setup/';
    validurls['/documentation/ios/'] = '/docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/initial_sdk_setup/';
    validurls['/documentation/delayed_braze_initialization_ios/'] = '/docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/initial_sdk_setup/#appboysharedinstance-and-swift-nullability';
    validurls['/documentation/react_native/android_and_fireos/'] = '/docs/developer_guide/platform_integration_guides/react_native/android_and_fireos/initial_sdk_setup/';
    validurls['/documentation/react_native/ios/'] = '/docs/developer_guide/platform_integration_guides/react_native/ios/sdk_integration/';
    validurls['/documentation/platform_wide/'] = '/docs/developer_guide/platform_wide/platform_features/';
    validurls['/documentation/programmatic_message_sending/'] = '/docs/developer_guide/rest_api/messaging/#messaging';
    validurls['/documentation/braze_faqs/'] = '/docs/help/faqs/';
    validurls['/documentation/faqs/'] = '/docs/help/faqs/';
    validurls['/documentation/currents/'] = '/docs/partners/braze_currents/how_it_works/';
    validurls['/documentation/partner_integrations/'] = '/docs/partners/home/';
    validurls['/documentation/apptimize_integration/'] = '/docs/partners/technology_partners/channel_extensions/ab_testing/apptimize/';
    validurls['/documentation/okta/'] = '/docs/user_guide/administrative/logging_in_and_security/single_sign_on/';
    validurls['/documentation/email_spam_testing/'] = '/docs/user_guide/message_building_by_channel/email/inbox_vision/#spam-testing';
    validurls['/documentation/link_templates/'] = '/docs/user_guide/message_building_by_channel/email/link_templates/';

    validurls['/academy/app_settings/'] = '/docs/user_guide/administrative/app_settings/developer_console/api_settings_tab/#api-settings-tab';
    validurls['/academy/best_practices/'] = '/docs/help/home/';
    validurls['/academy/campaigns/ideas_and_strategies/'] = '/docs/user_guide/engagement_tools/campaigns/ideas_and_strategies/active_user_campaigns/';
    validurls['/academy/campaigns/scheduling_and_organizing/'] = '/docs/user_guide/engagement_tools/campaigns/scheduling_and_organizing/scheduling_your_campaign/';
    validurls['/academy/campaigns/testing_and_more/'] = '/docs/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/';
    validurls['/academy/canvas/create_a_canvas/'] = '/docs/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/';
    validurls['/academy/canvas/get_started/'] = '/docs/user_guide/engagement_tools/canvas/get_started/canvas/';
    validurls['/academy/data_and_analytics/'] = '/docs/user_guide/data_and_analytics/configuring_reporting/';
    validurls['/academy/gdpr_compliance/'] = '/docs/help/gdpr_compliance/';
    validurls['/academy/getting_started/'] = '/docs/user_guide/onboarding_with_braze/overview/';
    validurls['/academy/home/'] = '/docs/user_guide/introduction/';
    validurls['/academy/locations_and_geofences/'] = '/docs/user_guide/engagement_tools/locations_and_geofences/about/';
    validurls['/academy/manage_your_users/'] = '/docs/user_guide/administrative/manage_your_braze_users/adding_users_to_your_dashboard/';
    validurls['/academy/message_building_and_personalization/email/'] = '/docs/user_guide/message_building_by_channel/email/creating_an_email_campaign/';
    validurls['/academy/message_building_and_personalization/in-app_messages/'] = '/docs/user_guide/message_building_by_channel/in-app_messages/create/';
    validurls['/academy/message_building_and_personalization/personalization/'] = '/docs/user_guide/personalization_and_dynamic_content/overview/';
    validurls['/academy/message_building_and_personalization/push/'] = '/docs/user_guide/message_building_by_channel/push/creating_a_push_message/';
    validurls['/academy/message_building_and_personalization/webhooks/'] = '/docs/user_guide/message_building_by_channel/webhooks/creating_a_webhook/';
    validurls['/academy/news_feed/'] = '/docs/user_guide/engagement_tools/news_feed/creating_a_news_feed_item/';
    validurls['/academy/release_notes/'] = '/docs/help/release_notes/most_recent/';
    validurls['/academy/templates_and_media/'] = '/docs/user_guide/engagement_tools/templates_and_media/about/';
    validurls['/academy/troubleshooting_guide/'] = '/docs/help/home/';
    validurls['/academy/user_targeting/'] = '/docs/user_guide/engagement_tools/segments/creating_a_segment/';
    validurls['/academy/webinars/'] = '/docs/help/webinars/overview';



  var urlhash = window.location.hash;

  function redirecturl(ky,uh,redirect) {
    var val_urls = validurls[ky];
    var hashes = val_urls.split('#');
    var returl = hashes[0] + redirect;
    if (hashes[1]) {
      returl += '#' + hashes[1];
    }
    else if (uh ) {
      returl += uh;
    }
    return returl;
  }


  if (window.location.href.indexOf('redirected=true') == -1) {
    var redirected  = '?redirected=true' ;
    if (urlsearch.indexOf('?') > -1 ) {
      redirected = urlsearch + '&redirected=true';
    }
    if (validurls[urlpath.toLowerCase() + '/' + urlhash] ) {
      window.location  =  redirecturl(urlpath.toLowerCase() + '/' + urlhash,urlhash,redirected);
    }
    else if (validurls[urlpath.toLowerCase() + urlhash] ) {
      window.location  =  redirecturl(urlpath.toLowerCase() + urlhash,urlhash,redirected);
    }
    else if (validurls[urlpath.toLowerCase() + '/'] ) {
      window.location  =  redirecturl(urlpath.toLowerCase() + '/',urlhash,redirected);
    }
    else if (validurls[urlpath.toLowerCase()] ) {
      window.location  =  redirecturl(urlpath.toLowerCase(),urlhash,redirected);
    }
  }


}  )();
