---
nav_title: In-App Message Delivery
platform: FireOS
page_order: 3

---

# In-App Message Delivery

## Trigger Types

Our in-app message product allows you to trigger an in-app message display as a result of several different event types: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, `Push Click`.  Furthermore, `Specific Purchase` and `Custom Event` triggers can contain robust property filters.

{% alert important %}
Triggered in-app messages only work with custom events logged through the SDK and not through the REST APIs.  If you're working with Android, please check out how to log custom events [here]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/#tracking-custom-events). If you're working with iOS, check out how to log custom events [here]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/#tracking-custom-events).
{% endalert %}

## Delivery Semantics

All in-app messages that a user is eligible for are delivered to the user's device on session start. For more information about the SDK's session start semantics, see our [session lifecycle documentation][86]. Upon delivery, the SDK will pre-fetch assets so that they are available immediately at trigger time, minimizing display latency.

When a trigger event has more than one eligible in-app message associated with it, only the in-app message with the highest priority will be delivered.

For in-app messages that display immediately on delivery (*i.e.*, session start, push click) there can be some latency due to assets not being prefetched.

## Minimum Time Interval Between Triggers

By default, we rate limit in-app messages to once every 30 seconds to ensure a quality user experience.

To override this value, set `com_appboy_trigger_action_minimum_time_interval_seconds` in your `appboy.xml`. An example can be found in our sample application's [`appboy.xml`][87].

## Server-side Event Triggering

By default in-app messages are triggered by custom events logged by the SDK. If you would like to trigger in-app messages by server sent events you are also able to achieve this.

To enable this feature, a silent push is sent to the device which allows a custom push receiver to log an SDK based event. This SDK event will subsequently trigger the user-facing in-app message.

### Step 1: Register a Custom Broadcast Receiver to Log Custom Event

Register your custom `BroadcastReceiver` to listen for a specific silent push within your AndroidManifest.xml. For more information on how to register a custom `BroadcastReceiver` please review [Braze's push documentation][78].

### Step 2: Create your BroadcastReceiver

Your receiver will handle the intent broadcast by the silent push and log an SDK event. Starting in SDK 2.0.0, events can be logged in the background without issue. All clients implementing this solution must be on SDK v2.0.0+.

It will subclass `BroadcastReceiver` and override `onReceive()`. For a detailed example, please see our [EventBroadcastReceiver.java][72].

>  Two events will be logged for the in-app message to be delivered, one by the server and one from within your custom `BroadcastReceiver`. To ensure the same event is not duplicated, the event logged from within your `BroadcastReceiver` should be given a generic naming convention, for example, "in-app message trigger event," and not the same name as the server sent event. If this is not done segmentation and user data may be affected by duplicate events being logged for a single user action.

For further details on custom handling push receipts, opens, and key-value pairs please visit this section of our [Documentation][78].

### Step 3: Create a Push Campaign

Create a silent push campaign which is triggered via the server sent event. For details on how to create a silent push campaign please review this section of our [Docs][73].

![serverEventTrigger][75]

The push campaign must include key-value pair extras which indicate that this push campaign is sent with the intention to log an SDK custom event. This event will be used to trigger the in-app message

![kvpConfiguration][76]

The [EventBroadcastReceiver.java][72] recognizes the key-value pairs and logs the appropriate SDK custom event.

Should you want to include any event properties to attach to your 'In-App Message Trigger' event, you can achieve this by passing these in the key-value pairs of the push payload. In the example above the campaign name of the subsequent in-app message has been included. Your custom `BroadcastReceiver` can then pass the value as the parameter of the event property when logging the custom event.

###  Step 4: Create an In-App Message Campaign

Create your user visible in-app message campaign from within Braze’s dashboard. This campaign should have an Action Based delivery, and be triggered from the custom event logged from within the custom [EventBroadcastReceiver.java][72].

In the example below the specific in-app message to be triggered has been configured by sending the event property as part of the initial silent push.

![serverEventTrigger][77]

>  If a server sent event is logged whilst the app is not in the foreground, the event will log but the in-app message will not be displayed. Should you want the event to be delayed until the application is in the foreground, a check must be included in your custom push receiver to dismiss or delay the event until the app has entered the foreground.

## Local In-App Messages

In-app messages can be created within the app and displayed locally in real-time.  All customization options available on the dashboard are also available locally.  This is particularly useful for displaying messages that you wish to trigger within the app in real-time.

```java
  // Initializes a new slideup type in-app message and specifies its message.
  InAppMessageSlideup inAppMessage = new InAppMessageSlideup();
  inAppMessage.setMessage("Welcome to Braze! This is a slideup in-app message.");
```

>  Do not display in-app messages when the soft keyboard is displayed on screen as rendering is undefined in this circumstance.

### Manually Triggering In-App Message Display

The following method will manually display your in-app message.

```java
  AppboyInAppMessageManager.getInstance().addInAppMessage(inAppMessage);
```
See [`InAppMessageTesterFragment.java`][2] in the DroidBoy sample app for example usage.

### In-Depth: Defining Custom In-App Message Types

Braze's `slideup` in-app message object extends [`InAppMessageBase`][27].  Braze's `full` and `modal` type messages extend [`InAppMessageImmersiveBase`][28].  Extending one of these classes gives you the option of adding custom functionality to your locally generated in-app messages.

See [`CustomInAppMessage.java`][29] in the DroidBoy sample app for an example implementation.

[1]: https://github.com/Appboy/appboy-android-sdk/tree/master/samples/manual-session-integration
[2]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/InAppMessageTesterFragment.java
[3]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/IInAppMessage.html
[4]: {{site.baseurl}}/help/best_practices/in-app_messages/in-app_message_behavior/#in-app-message-behavior
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/
[6]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/res/values/styles.xml
[7]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/CustomInAppMessageManagerListener.java
[8]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/IInAppMessageImmersive.html
[9]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/CustomInAppMessageAnimationFactory.java
[12]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/#setting-a-custom-view-factory
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/
[14]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/news_feed/#key-value-pairs
[15]: http://fortawesome.github.io/Font-Awesome/
[17]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/#modal-in-app-messages
[18]: http://developer.android.com/reference/android/view/View.html
[19]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/#setting-a-custom-manager-listener
[20]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/inappmessage/IInAppMessageAnimationFactory.java
[21]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/inappmessage/listeners/IInAppMessageManagerListener.java
[22]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/#setting-a-custom-animation-factory
[23]: http://developer.android.com/reference/android/R.integer.html#config_shortAnimTime
[24]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/inappmessage/IInAppMessageImmersiveView.java
[25]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/inappmessage/IInAppMessageView.java
[26]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/CustomInAppMessageView.java
[27]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/InAppMessageBase.html
[28]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/InAppMessageImmersiveBase.html
[29]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/CustomInAppMessage.java
[30]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#creating-an-in-app-message
[33]: {% image_buster /assets/img_archive/foodo-slideup.gif %}
[34]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/inappmessage/AppboyInAppMessageManager.java
[36]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/CustomInAppMessageManagerListener.java
[39]: https://developer.android.com/guide/topics/ui/dialogs.html
[40]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/#html-full-in-app-messages
[41]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/#full-in-app-messages
[42]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/inappmessage/IInAppMessageViewFactory.java
[43]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/CustomInAppMessageViewFactory.java
[44]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/IInAppMessage.html#getExtras()
[45]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/inappmessage/InAppMessageOperation.java
[50]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/MessageButton.html
[51]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/InAppMessageHtmlFull.html
[52]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/IInAppMessageHtml.html
[53]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/
[54]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/#in-app-message-customization
[55]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/#gifs-iams
[59]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/#activity-lifecycle-callback-integration-api-14
[60]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/res/values-xlarge/styles.xml
[65]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/
[66]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Appboy.html#requestInAppMessageRefresh--
[67]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/AppboyInAppMessageManager.html#requestDisplayInAppMessage--
[68]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/
[69]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/AppboyInAppMessageManager.html#ensureSubscribedToInAppMessageEvents-android.content.Context-
[70]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/
[71]: https://developer.android.com/guide/topics/graphics/hardware-accel.html#controlling
[72]: https://gist.github.com/robbiematthews/1d037e2c366e523b2dda5f2e053ea2a9
[73]: {{site.baseurl}}/developer_guide/platform_integration_guides/fireos/push_notifications/silent_push_notifications/#silent-push-notifications
[75]: {% image_buster /assets/img_archive/serverSentPush.png %}
[76]: {% image_buster /assets/img_archive/kvpConfiguration.png %}
[77]: {% image_buster /assets/img_archive/IAMeventTrigger.png %}
[78]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/#step-1-register-your-broadcastreceiver
[79]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization
[80]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/AppboyInAppMessageManager.html#registerInAppMessageManager-android.app.Activity-
[81]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/AppboyInAppMessageManager.html#unregisterInAppMessageManager-android.app.Activity-
[82]: https://developer.android.com/reference/android/app/Application.html#onCreate()
[83]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/inappmessage/InAppMessageOperation.java
[84]: {% image_buster /assets/img_archive/trigger-iam-composer.png %}
[85]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#original-in-app-messages
[86]: {{site.baseurl}}/developer_guide/platform_integration_guides/fireos/analytics/tracking_sessions/#session-lifecycle
[87]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/res/values/appboy.xml
[88]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/#tracking-custom-events
[89]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/#tracking-custom-events
