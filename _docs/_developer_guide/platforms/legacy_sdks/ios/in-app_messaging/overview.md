---
nav_title: Overview
article_title: In-App Message Overview for iOS
platform: iOS
page_order: 0
description: "This reference article covers iOS in-app messaging types, expected behaviors, and several use cases."
channel:
  - in-app messages
search_rank: 4
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# In-app messages

[In-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) help you get content to your user without interrupting their day with a push notification. Customized and tailored in-app messages enhance the user experience and help your audience get the most value from your app. With a variety of layouts and customization tools to choose from, in-app messages engage your users more than ever before.

Check out our [case studies](https://www.braze.com/customers) to see examples of in-app messages.

## In-app message types

Braze currently offers the following default in-app message types: 

- `Slideup`
- `Modal`
- `Full`
- `HTML Full`

Each in-app message type is highly customizable across content, images, icons, click actions, analytics, display, and delivery.

All in-app messages are subclasses of the `ABKInAppMessage`, which defines basic behavior and traits for all in-app messages. The in-app message class structures are as follows:

![A graphic showing that the ABKInAppMessage class is the root class of the ABKInAppMessageSlideup, ABKInAppMessageImmersive, and ABKInAppMessageHTML. The ABKInAppMessage includes customizable properties like message, extras, duration, click action, URI, dismiss action, icon orientation, and text alignment. The ABKInAppMessageSlideup includes customizable properties like chevron and slide-up anchor. The ABKInAppMessageImmersive includes customizable properties like header, close button, frame, and in-app message buttons. ABKInAppMessageHTML allows you to manually log HTML in-app message button clicks.]({% image_buster /assets/img_archive/ABKInAppMessage-models.png %})

{% alert important %}
By default, in-app messages are enabled after completing the standard SDK integration, including GIF support. 
<br><br>
Note that integration of `SDWebImage` is required if you plan on using our Braze UI for displaying images within iOS in-app messages or Content Cards.
{% endalert %}

### Expected behaviors by message types

This is what it looks like for your users to open one of our default in-app message types.

{% tabs %}
{% tab Slideup %}

[`Slideup`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_slideup.html) in-app messages are so-named because they "slide up" or "slide down" from the top or bottom of the screen. They cover a small portion of the screen and provide an effective and non-intrusive messaging capability.

![An in-app message sliding from the bottom of a phone screen displaying "Humans are complicated. Custom engagement shouldn't be." In the background is the same in-app message displayed in the bottom corner of a web page.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}


{% endtab %}
{% tab Modal %}

[`Modal`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_modal.html) in-app messages appear in the center of the screen and are framed by a translucent panel. Useful for more critical messaging, they can be equipped with up to two click action and analytics-enabled buttons.

![A modal in-app message in the center of a phone screen displaying "Humans are complicated. Custom engagement shouldn't be." In the background is the same in-app message displayed in the center of a web page.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Full Screen %}

[`Full`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_full.html) in-app messages are useful for maximizing the content and impact of your user communication. The upper half of a `full` in-app message contains an image, and the lower half displays text and up to two click action and analytics-enabled buttons.

![A full screen in-app message shown across an entire phone screen displaying, "Humans are complicated. Custom engagement shouldn't be." In the background is the same in-app message displayed largely in the center of a web page.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Custom HTML %}

[`HTML Full`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_h_t_m_l_full.html) in-app messages are useful for creating fully customized user content. User-defined HTML Full in-app message content is displayed in a `WKWebView`and may optionally contain other rich content, such as images and fonts, allowing for full control over message appearance and functionality. <br><br>iOS in-app messages support a JavaScript `brazeBridge` interface to call methods on the Braze Web SDK from within your HTML, see our [best practices]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/) for more details.

The following example shows a paginated HTML Full in-app message:

![An HTML in-app message with a carousel of content and interactive buttons.]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

Full in-app message content is displayed in a `WKWebView` and may optionally contain other rich content, such as images and fonts, allowing full control over message appearance and functionality. Note that we currently do not support the display of custom HTML in-app messages in an iFrame on the iOS and Android platforms.

{% alert note %}
Starting in iOS SDK version 3.19.0, the following JavaScript methods are no-ops in HTML in-app messages: `alert`, `confirm`, `prompt`.
{% endalert %}

{% endtab %}
{% endtabs %}

