---
page_order: 2
nav_title: In-App Messages
description: "This landing page is home to all things in-app messaging for the Braze Android SDK."
---

# In-app messages

> [In-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) help you get content to your user without interrupting their day with a push notification. Customized and tailored in-app messages enhance the user experience and help your audience get the most value from your app. With a variety of layouts and customization tools to choose from, in-app messages engage your users more than ever before. For in-app message examples, check out our [case studies](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html).

## Prerequisites

Before you can use Braze in-app messages, you'll need to complete the following:

1. [Integrate the Braze Android SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/android/sdk_integration/)
2. [Complete the initial in-app message setup]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in_app_messages/setup/)

## About the interface

The [`IInAppMessage`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html) interface defines the basic behavior and traits of all in-app messages through its subclass, [`InAppMessageBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html). It also includes a subinterface, [`IInAppMessageImmersive`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-immersive/index.html), which allows you to add close, click-action, and analytics [buttons](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html) to your app.

{% alert important %}
In-app messages containing buttons will include the `clickAction` message in the final payload if the click action is added prior to adding the button text.
{% endalert %}

## Message types

Braze offers several default in-app message types, each customizable with messages, images, [Font Awesome](https://fontawesome.com/icons?d=gallery&p=2) icons, click actions, analytics, editable styling, and color schemes.

{% tabs local %}
{% tab Slideup %}
[`slideup`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html) in-app messages are so-named because they "slide up" or "slide down" from the top or bottom of the screen. They cover a small portion of the screen and provide an effective and non-intrusive messaging capability.

The `slideup` in-app message object extends [`InAppMessageBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html).

![An in-app message sliding from the bottom of a phone screen displaying "Humans are complicated. Custom engagement shouldn't be." In the background is the same in-app message displayed in the bottom right corner of a web page.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}
[`modal`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html) in-app messages appear in the center of the screen and are framed by a translucent panel. Useful for more critical messaging, they can be equipped with two click-action and analytics-enabled buttons.

This message type is a subclass of [`InAppMessageImmersiveBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html), an abstract class that implements `IInAppMessageImmersive`, giving you the option to add custom functionality to your locally generated in-app messages.

![A modal in-app message in the center of a phone screen displaying "Humans are complicated. Custom engagement shouldn't be." In the background is the same in-app message displayed in the center of a web page.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Full Screen %}
[`full`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html) in-app messages are useful for maximizing the content and impact of your user communication. The upper half of a `full` in-app message contains an image, and the lower half displays text and up to two click action and analytics-enabled buttons.

This message type extends [`InAppMessageImmersiveBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html), giving you the option to add custom functionality to your locally generated in-app messages.

![A full screen in-app message shown across an entire phone screen displaying, "Humans are complicated. Custom engagement shouldn't be." In the background is the same in-app message displayed largely in the center of a web page.]({% image_buster /assets/img_archive/In-App_Full.png %})

{% endtab %}
{% tab Custom HTML %}
[`HTML`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html/index.html) in-app messages are useful for creating fully customized user content. User-defined HTML in-app message content is displayed in a `WebView` and may optionally contain other rich content, such as images and fonts, allowing for full control over message appearance and functionality.

These messages instances of [`InAppMessageHtml`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html/index.html), which implement the `IInAppMessage` subclass: [`IInAppMessageHtml`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-html/index.html).

Android in-app messages support a JavaScript `brazeBridge` interface to call methods on the Braze Web SDK from within your HTML, see our <a href="{{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/">best practices</a> for more details.

![An HTML in-app message with the a carousel of content and interactive buttons.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% alert important %}
We currently do not support the display of custom HTML in-app messages in an iFrame on the iOS and Android platforms.
{% endalert %} 

{% endtab %}
{% endtabs %}

## Custom message types

You can also define a custom in-app message view for your app. For a full walkthrough, see [Custom view factory]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in_app_messages/customization/custom_listeners/#custom-view-factory).
