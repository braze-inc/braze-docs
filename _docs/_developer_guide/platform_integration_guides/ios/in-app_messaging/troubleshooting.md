---
nav_title: Troubleshooting
platform: iOS
page_order: 4

---

# Troubleshooting In-App Messages

{% include archive/troubleshooting_iams.md platform="iOS" %}

[1]: #customize-inAppMessage-dashboard
[2]: #customize-inAppMessage-code
[3]: #set-delegate
[4]: #customize-inAppMessage-display
[5]: #before-display
[6]: #manual-cue
[7]: #situational-display
[8]: #inAppMessage-click
[9]: #custom-view
[10]: #custom-inAppMessage
[11]: #custom-complete
[12]: #method-declarations
[13]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#creating-an-in-app-message
[14]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/ABKInAppMessage.h
[15]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/ABKInAppMessageController.h
[16]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/ABKInAppMessageControllerDelegate.h
[19]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/CustomInAppMessageViewController.m
[21]: {% image_buster /assets/img_archive/foodo-slideup.gif %}
[23]: #setting-delegates
[25]: https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#2121
[26]: http://fortawesome.github.io/Font-Awesome/
[27]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#in-app-messages-triggered
[29]: {% image_buster /assets/img_archive/ABKInAppMessage-models.png %}
[30]: #in-app-message-controller-delegate
[31]: #customizing-appboy-on-startup
[32]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/ABKInAppMessageControllerDelegate.h
[33]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/troubleshooting/#step-2-devices-register-for-apns-and-provide-braze-with-push-tokens
[34]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h
[35]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/ViewController.m
[36]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/AppDelegate.m
[37]: https://github.com/Appboy/appboy-ios-sdk/tree/master/AppboyUI/ABKInAppMessage/ViewControllers
[38]: #in-app-mssage-ui-delegate
[39]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/
[40]: {% image_buster /assets/img_archive/iosServerSentPush.png %}
[41]: {% image_buster /assets/img_archive/iOSServerPush.png %}
[42]: {% image_buster /assets/img_archive/iosIAMeventTrigger.png %}
