---
nav_title: In-App Message Types
page_order: 2
search_rank: 5
platform: Android
---

# In-App Message Types

Braze offers several default in-app message types, each customizable with messages, images, [Font Awesome][15] icons, click actions, analytics, editable styling and color schemes.  The currently available types are [`Slideup`][13], [`Modal`][17], [`Full`][41], and [`HTML Full`][40].  It is also possible to [define your own custom in-app message view][12].

All in-app messages implement the [`IInAppMessage`][3] interface, which defines basic behavior and traits for all in-app messages.  [`InAppMessageBase`][27] is an abstract class that implements `IInAppMessage` and provides the foundational in-app message implementation.  All in-app message classes are subclasses of `InAppMessageBase`.

In addition, there is a subinterface of `IInAppMessage` called [`IInAppMessageImmersive`][8], which adds click action and analytics enabled [buttons][50], as well as header text and a close button.  [`InAppMessageImmersiveBase`][28] is an abstract class that implements `IInAppMessageImmersive` and provides the foundational `immersive` in-app message implementation.  `Modal` and `Full` in-app messages are subclasses of `InAppMessageImmersiveBase`.

HTML Full in-app messages are [`InAppMessageHtmlFull`][51] instances, which implement [`IInAppMessageHtml`][52], another subclass of `IInAppMessage`.

{% include archive/in_app_message.md platform="Android" %}

## Local In-App Messages

In-app messages can be created within the app and displayed locally in real-time.  All customization options available on the dashboard are also available locally.  This is particularly useful for displaying messages that you wish to trigger within the app in real-time.

{% tabs %}
{% tab JAVA %}

```java
// Initializes a new slideup type in-app message and specifies its message.
InAppMessageSlideup inAppMessage = new InAppMessageSlideup();
inAppMessage.setMessage("Welcome to Braze! This is a slideup in-app message.");
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Initializes a new slideup type in-app message and specifies its message.
val inAppMessage = InAppMessageSlideup()
inAppMessage.message = "Welcome to Braze! This is a slideup in-app message."
```

{% endtab %}
{% endtabs %}

>  Do not display in-app messages when the soft keyboard is displayed on screen as rendering is undefined in this circumstance.

### Manually Triggering In-App Message Display

The following method will manually display your in-app message.

{% tabs %}
{% tab JAVA %}

```java
AppboyInAppMessageManager.getInstance().addInAppMessage(inAppMessage);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
AppboyInAppMessageManager.getInstance().addInAppMessage(inAppMessage)
```

{% endtab %}
{% endtabs %}

See [`InAppMessageTesterFragment.java`][2] in the DroidBoy sample app for example usage.

#### In-Depth: Defining Custom In-App Message Types

Braze's `slideup` in-app message object extends [`InAppMessageBase`][27].  Braze's `full` and `modal` type messages extend [`InAppMessageImmersiveBase`][28].  Extending one of these classes gives you the option of adding custom functionality to your locally generated in-app messages.

See [`CustomInAppMessage.java`][29] in the DroidBoy sample app for an example implementation.

[1]: https://github.com/Appboy/appboy-android-sdk/tree/master/samples/manual-session-integration
[2]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/InAppMessageTesterFragment.java
[3]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/IInAppMessage.html
[4]: {{ site.baseurl }}//help/best_practices/in-app_messages/in-app_message_behavior/#in-app-message-behavior
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
