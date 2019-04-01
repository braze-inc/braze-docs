---
nav_title: Integration
platform: FireOS
page_order: 1
search_rank: 4
---
## Integration {#in-app-messaging-integration}

### Step 1: Braze In-App Message Manager Registration

In-App Message display is managed by the [`AppboyInAppMessageManager`][34] class. Every activity in your app must be registered with the `AppboyInAppMessageManager` to allow it to add in-app message views to the view hierarchy. There are two ways to accomplish this:

#### Activity Lifecycle Callback Integration (Recommended)

The [Activity Lifecycle Callback Integration][59] handles in-app message registration automatically, no extra integration is required. This is the recommended integration for handling in-app message registration.

#### Manual In-App Message Registration

A manual in-app message registration requires 3 steps.

>  If you did the activity lifecycle integration, then you should *not* do a manual in-app message integration.

* In your [`Application.onCreate()`][82], [`ensureSubscribedToInAppMessageEvents()`][69] should be called.

```java
AppboyInAppMessageManager.getInstance().ensureSubscribedToInAppMessageEvents(context);
```

* In every activity where in-app messages can be shown, [`registerInAppMessageManager()`][80] should be called in that activity's `onResume()`.

```java
@Override
public void onResume() {
  super.onResume();
  // Registers the AppboyInAppMessageManager for the current Activity. This Activity will now listen for
  // in-app messages from Braze.
  AppboyInAppMessageManager.getInstance().registerInAppMessageManager(activity);
}
```

* In every activity where [`registerInAppMessageManager()`][80] was called, [`unregisterInAppMessageManager()`][81] should be called in that activity's `onPause()`.

```java
@Override
public void onPause() {
  super.onPause();
  // Unregisters the AppboyInAppMessageManager for the current Activity.
  AppboyInAppMessageManager.getInstance().unregisterInAppMessageManager(activity);
}
```


[1]: https://github.com/Appboy/appboy-android-sdk/tree/master/samples/manual-session-integration
[2]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/InAppMessageTesterFragment.java
[3]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/IInAppMessage.html
[4]: {{ site.baseurl }}/help/best_practices/in-app_messages/in-app_message_behavior/#in-app-message-behavior
[5]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/
[6]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/res/values/styles.xml
[7]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/CustomInAppMessageManagerListener.java
[8]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/IInAppMessageImmersive.html
[9]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/CustomInAppMessageAnimationFactory.java
[12]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/#setting-a-custom-view-factory
[13]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/
[14]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/news_feed/#key-value-pairs
[15]: http://fortawesome.github.io/Font-Awesome/
[17]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/#modal-in-app-messages
[18]: http://developer.android.com/reference/android/view/View.html
[19]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/#setting-a-custom-manager-listener
[20]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/inappmessage/IInAppMessageAnimationFactory.java
[21]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/inappmessage/listeners/IInAppMessageManagerListener.java
[22]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/#setting-a-custom-animation-factory
[23]: http://developer.android.com/reference/android/R.integer.html#config_shortAnimTime
[24]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/inappmessage/IInAppMessageImmersiveView.java
[25]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/inappmessage/IInAppMessageView.java
[26]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/CustomInAppMessageView.java
[27]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/InAppMessageBase.html
[28]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/InAppMessageImmersiveBase.html
[29]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/CustomInAppMessage.java
[30]: {{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/creating_an_in-app_message/#creating-an-in-app-message
[33]: {% image_buster /assets/img_archive/foodo-slideup.gif %}
[34]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/inappmessage/AppboyInAppMessageManager.java
[36]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/CustomInAppMessageManagerListener.java
[39]: https://developer.android.com/guide/topics/ui/dialogs.html
[40]: {{ site.baseurl }}/docs/developer_guide/platform_integration_guides/android/in-app_messaging/#html-full-in-app-messages
[41]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/#full-in-app-messages
[42]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/inappmessage/IInAppMessageViewFactory.java
[43]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/CustomInAppMessageViewFactory.java
[44]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/IInAppMessage.html#getExtras()
[45]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/inappmessage/InAppMessageOperation.java
[50]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/MessageButton.html
[51]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/InAppMessageHtmlFull.html
[52]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/IInAppMessageHtml.html
[53]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/
[54]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/#in-app-message-customization
[55]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/#gifs-iams
[59]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/#activity-lifecycle-callback-integration-api-14
[60]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/res/values-xlarge/styles.xml
[65]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/
[66]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Appboy.html#requestInAppMessageRefresh--
[67]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/AppboyInAppMessageManager.html#requestDisplayInAppMessage--
[68]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/
[69]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/AppboyInAppMessageManager.html#ensureSubscribedToInAppMessageEvents-android.content.Context-
[70]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/
[71]: https://developer.android.com/guide/topics/graphics/hardware-accel.html#controlling
[72]: https://gist.github.com/robbiematthews/1d037e2c366e523b2dda5f2e053ea2a9
[73]: {{ site.baseurl }}/developer_guide/platform_integration_guides/fireos/push_notifications/silent_push_notifications/#silent-push-notifications
[75]: {% image_buster /assets/img_archive/serverSentPush.png %}
[76]: {% image_buster /assets/img_archive/kvpConfiguration.png %}
[77]: {% image_buster /assets/img_archive/IAMeventTrigger.png %}
[78]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/push_notifications/integration/#step-1-register-your-broadcastreceiver
[79]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization
[80]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/AppboyInAppMessageManager.html#registerInAppMessageManager-android.app.Activity-
[81]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/AppboyInAppMessageManager.html#unregisterInAppMessageManager-android.app.Activity-
[82]: https://developer.android.com/reference/android/app/Application.html#onCreate()
[83]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/inappmessage/InAppMessageOperation.java
