---
nav_title: In-App Message Templates
platform: iOS
page_order: 4
search_rank: 5
---

# In-App Message Templates

## Custom App Store Review Prompt
{% raw %}
Creating a campaign to ask users for an App Store review is a popular usage of in-app messages.

Start by [setting the In-App Message delegate][30] in your app. Next,implement the following delegate method to disable the default App Store review message:

```objc
- (ABKInAppMessageDisplayChoice)beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage {
   if (inAppMessage.extras != nil && inAppMessage.extras[@"Appstore Review"] != nil) {
     [[UIApplication sharedApplication] openURL:inAppMessage.uri];
     return ABKDiscardInAppMessage;
   } else {
     return ABKDisplayInAppMessageNow;
   }
}
```

In your deep link handling code,  you can then add the following code to process the `{YOUR-APP-SCHEME}:appstore-review` deep link:

```objc
- (BOOL)application:(UIApplication *)application
            openURL:(NSURL *)url
  sourceApplication:(NSString *)sourceApplication
         annotation:(id)annotation {
  NSString *urlString = url.absoluteString.stringByRemovingPercentEncoding;
  if ([urlString isEqualToString:@"{YOUR-APP-SCHEME}:appstore-review"]) {
    [SKStoreReviewController requestReview];
    return YES;
  }
  // Other deep link handling code…
}
```

Next, create an In-App Messaging campaign with the following:

- add the key-value pair `“Appstore Review” : “true”`
- set the "On Click Behavior" to "Deep Link Into App," using the above deep link (e.g., `{YOUR-APP-SCHEME}:appstore-review`)

{% endraw %}

{% alert tip %}
  Apple limits App Store review prompts to a maximum of three (3) times per year for each user, so your campaign should be [rate-limited]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#user-centric-rate-limiting) to three times per year per user. 

  Users may turn off App Store review prompts. As a result, your custom review prompt should not promise that a native App Store review prompt will appear, or directly ask for a review.
{% endalert %}




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
[13]: {{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/creating_an_in-app_message/#creating-an-in-app-message
[14]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/ABKInAppMessage.h
[15]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/ABKInAppMessageController.h
[16]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/ABKInAppMessageControllerDelegate.h
[17]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/ABKInAppMessageView.h
[18]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/ABKInAppMessageViewController.h
[19]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/CustomInAppMessageViewController.m
[21]: {% image_buster /assets/img_archive/foodo-slideup.gif %}
[23]: #setting-delegates
[25]: https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#2121
[26]: http://fortawesome.github.io/Font-Awesome/
[27]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/in_app_messaging/#in-app-messages-triggered
[29]: {% image_buster /assets/img_archive/ABKInAppMessage-models.png %}
[30]: #in-app-message-controller-delegate
[31]: #customizing-appboy-on-startup
[32]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/ABKInAppMessageControllerDelegate.h
[33]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/push_notifications/troubleshooting/#step-2-devices-register-for-apns-and-provide-braze-with-push-tokens
[34]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/InAppMessage/ABKInAppMessageUIDelegate.h
[35]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/ViewController.m
[36]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/AppDelegate.m
[37]: https://github.com/Appboy/appboy-ios-sdk/tree/master/AppboyUI/InAppMessage/ViewControllers
[38]: #in-app-mssage-ui-delegate
[39]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/
[40]: {% image_buster /assets/img_archive/iosServerSentPush.png %}
[41]: {% image_buster /assets/img_archive/iOSServerPush.png %}
[42]: {% image_buster /assets/img_archive/iosIAMeventTrigger.png %}
