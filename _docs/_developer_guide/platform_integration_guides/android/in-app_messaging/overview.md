---
nav_title: Overview
article_title: In-App Message Overview for Android/FireOS
page_order: 0
platform: 
  - Android
  - FireOS
description: "This article covers Android in-app messaging, when to best use it, in addition to several great use cases."
channel:
  - in-app messages

---

# In-app messages

[In-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) help you get content to your users without interrupting their day with a push notification. Customized and tailored in-app messages enhance the user experience and help your audience get the most value from your app. With various layouts and customization tools to choose from, in-app messages engage your users more than ever before.

To see examples of in-app messages, check out our [case studies][83].

## In-app message types

Braze offers several default in-app message types, each customizable with messages, images, [Font Awesome][15] icons, click actions, analytics, editable styling, and color schemes. The currently available types are:

- [`Slideup`][91]
- [`Modal`][90]
- [`Full`][93]
- [`HTML Full`][92]

It is also possible to define your own [custom in-app message view][12].

All in-app messages implement the [`IInAppMessage`][3] interface, which defines all in-app messages' basic behavior and traits. [`InAppMessageBase`][27] is an abstract class that implements `IInAppMessage` and provides the foundational in-app message implementation. All in-app message classes are subclasses of `InAppMessageBase`.

In addition, there is a subinterface of `IInAppMessage` called [`IInAppMessageImmersive`][8], which adds click-action and analytics enabled [buttons][50], as well as header text and a close button. [`InAppMessageImmersiveBase`][28] is an abstract class that implements `IInAppMessageImmersive` and provides the foundational `immersive` in-app message implementation. `Modal` and `Full` in-app messages are subclasses of `InAppMessageImmersiveBase`.

HTML full in-app messages are [`InAppMessageHtmlFull`][51] instances, which implement [`IInAppMessageHtml`][52], another subclass of `IInAppMessage`.

### Expected behaviors by message type

These are what it looks like for your users to open one of our out-of-the-box in-app message types.

{% tabs %}
{% tab Slideup %}
[`Slideup`](https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html) in-app messages are so-named because they "slide up" or "slide down" from the top or bottom of the screen. They cover a small portion of the screen and provide an effective and non-intrusive messaging capability.

![An in-app message sliding from the bottom of a phone screen displaying "Humans are complicated. Custom engagement shouldn't be." In the background is the same in-app message displayed in the bottom right corner of a web page.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}
[`Modal`](https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html) in-app messages appear in the center of the screen and are framed by a translucent panel. Useful for more critical messaging, they can be equipped with two click-action and analytics-enabled buttons.

![A modal in-app message in the center of a phone screen displaying "Humans are complicated. Custom engagement shouldn't be." In the background is the same in-app message displayed in the center of a web page.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Full Screen %}
[`Full`](https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html) in-app messages are useful for maximizing the content and impact of your user communication. The upper half of a `full` in-app message contains an image, and the lower half displays text and up to two click action and analytics-enabled buttons.

![A full screen in-app message shown across an entire phone screen displaying, "Humans are complicated. Custom engagement shouldn't be." In the background is the same in-app message displayed largely in the center of a web page.]({% image_buster /assets/img_archive/In-App_Full.png %})

{% endtab %}
{% tab Custom HTML %}
[`HTML Full`](https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html-full/index.html) in-app messages are useful for creating fully customized user content. User-defined HTML full in-app message content is displayed in a `WebView` and may optionally contain other rich content, such as images and fonts, allowing for full control over message appearance and functionality. <br><br>Android in-app messages support a JavaScript `brazeBridge` interface to call methods on the Braze Web SDK from within your HTML, see our <a href="https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages/best_practices/">best practices</a> for more details.

![An HTML in-app message with the a carousel of content and interactive buttons.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% alert important %}
Please note that we currently do not support the display of custom HTML in-app messages in an iFrame on the iOS and Android platforms.
{% endalert %} 

{% endtab %}
{% endtabs %}

#### Defining custom in-app message types

The `slideup` in-app message object extends [`InAppMessageBase`][27]. 
The `full` and `modal` type messages extends [`InAppMessageImmersiveBase`][28]. Extending one of these classes gives you the option of adding custom functionality to your locally generated in-app messages.

[3]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html
[8]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-immersive/index.html
[12]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/#setting-a-custom-view-factory
[15]: http://fortawesome.github.io/Font-Awesome/
[27]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html
[28]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html
[50]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html
[51]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html-full/index.html
[52]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-html/index.html
[83]: https://www.braze.com/customers
[84]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
[90]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html
[91]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html
[92]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html-full/index.html
[93]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html
