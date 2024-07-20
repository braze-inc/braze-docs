---
nav_title: Integration
article_title: In-App Message Overview for iOS
platform: Swift
page_order: 0
description: "This article covers iOS in-app messaging types, expected behaviors, and several use cases for the Swift SDK."
channel:
  - in-app messages

---

# In-app message integration

> [In-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) help you get content to your user without interrupting their day with a push notification. Customized and tailored in-app messages enhance the user experience and help your audience get the most value from your app. With a variety of layouts and customization tools to choose from, in-app messages engage your users more than ever before.

Check out our [case studies](https://www.braze.com/customers) to see examples of in-app messages.

## In-app message types

Braze currently offers the following default in-app message types: 

- Slideup
- Modal
- Modal Image
- Full
- Full Image
- Custom HTML
- Control

Each in-app message type is highly customizable across content, images, icons, click actions, analytics, display, and delivery.

For a full list of in-app message properties and usage, refer to the [`InAppMessage` class documentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage).

All in-app messages are enumerated types of `Braze.InAppMessage`, which defines basic behavior and traits for all in-app messages. Each type of in-app message and its corresponding details is listed in the tabs below.

### Expected behaviors by message types

This is what it looks like for your users to open one of our default in-app message types.

{% tabs %}
{% tab Slideup %}

[`Slideup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/slideup-swift.struct) in-app messages are so-named because they "slide up" or "slide down" from the top or bottom of the screen. They cover a small portion of the screen and provide an effective and non-intrusive messaging capability.

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

For further details about Intelligent Selection and control groups, refer to [Intelligent Selection]({{site.baseurl}}/user_guide/sage_ai/intelligence/intelligent_selection/).

{% endtab %}
{% endtabs %}


{% alert important %}
The standard SDK integration includes steps that activate in-app messages, including GIF support. For more details on GIF support, refer to this [tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support).
{% endalert %}


[30]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
[31]: https://www.braze.com/customers
