---
nav_title: In-App Messages
page_order: 2
description: "This landing page is home to all things in-app messaging for the Braze Swift SDK."
---

# In-app messages

> [In-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) help you get content to your user without interrupting their day with a push notification. Customized and tailored in-app messages enhance the user experience and help your audience get the most value from your app. With a variety of layouts and customization tools to choose from, in-app messages engage your users more than ever before. For in-app message examples, check out our [case studies](https://www.braze.com/customers).

## Prerequisites

Before you can use in-app messaging, you'll need to integrate the [Braze Swift SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration/) into your app. However, no additional setup is required.

## Message types

Each in-app message type is highly customizable across content, images, icons, click actions, analytics, display, and delivery. They are enumerated types of `Braze.InAppMessage`, which defines basic behavior and traits for all in-app messages. For the full list of in-app message properties and usage, see the [`InAppMessage` class](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage).

These are the available in-app message types in Braze and how they will look like for end-users.

{% tabs %}
{% tab Slideup %}

[`Slideup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/slideup-swift.struct) in-app messages are given this name because they "slide up" or "slide down" from the top or bottom of the screen. They cover a small portion of the screen and provide an effective and non-intrusive messaging capability.

![A slideup in-app message at the bottom and the top of a phone screen.]({% image_buster /assets/img/slideup-spec.png %}){: style="max-width:35%;border:none;"}


{% endtab %}
{% tab Modal %}

[`Modal`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/modal-swift.struct) in-app messages appear in the center of the screen and are framed by a translucent panel. Useful for more critical messaging, they can be equipped with up to two analytics-enabled buttons.

![A modal in-app message in the center of a phone screen.]({% image_buster /assets/img/modal-header-text.png %}){: style="max-width:35%;border:none;"}

{% endtab %}
{% tab Modal Image %}

[`Modal Image`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/modalimage-swift.struct) in-app messages appear in the center of the screen and are framed by a translucent panel. These messages are similar to the `Modal` type except without header or message text. Useful for more critical messaging, they can be equipped with up to two analytics-enabled buttons.

![A modal image in-app message in the center of a phone screen.]({% image_buster /assets/img/modal-full-image.png %}){: style="max-width:35%;border:none;"}

{% endtab %}
{% tab Fullscreen %}

[`Full`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/full-swift.struct) in-app messages are useful for maximizing the content and impact of your user communication. The upper half of a `Full` in-app message contains an image, and the lower half displays text and up to two analytics-enabled buttons.

![A fullscreen in-app message shown across an entire phone screen.]({% image_buster /assets/img/full-screen-header-text.png %}){: style="max-width:35%;border:none;"}

{% endtab %}
{% tab Full Screen Image %}

[`Full Image`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/fullimage-swift.struct) in-app messages are similar to `Full` in-app messages except without header or message text. This message type is useful for maximizing the content and impact of your user communication. A `Full Image` in-app message contains an image spanning the entire screen, with the option to display up to two analytics-enabled buttons.

![A fullscreen image in-app message shown across an entire phone screen.]({% image_buster /assets/img/full-screen-image.png %}){: style="max-width:35%;border:none;"}

{% endtab %}
{% tab Custom HTML %}

[`HTML`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/html-swift.struct) in-app messages are useful for creating fully customized user content. User-defined HTML Full in-app message content is displayed in a `WKWebView`and may optionally contain other rich content, such as images and fonts, allowing for full control over message appearance and functionality. <br><br>iOS in-app messages support a JavaScript `brazeBridge` interface to call methods on the Braze Web SDK from within your HTML, see our [best practices]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/) for more details.

The following example shows a paginated HTML Full in-app message:

![An HTML in-app message with a carousel of content and interactive buttons.]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

Note that we currently do not support the display of custom HTML in-app messages in an iFrame on the iOS and Android platforms.

{% endtab %}
{% tab Control %}

[`Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/control-swift.struct) in-app messages do not contain a UI component and are used primarily for analytics purposes. This type is used to verify receipt of an in-app message sent to a control group.

For further details about Intelligent Selection and control groups, refer to [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/).

{% endtab %}
{% endtabs %}
