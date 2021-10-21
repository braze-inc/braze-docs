---
nav_title: Overview
article_title: In-App Message Overview for iOS
platform: iOS
page_order: 0
description: "This article covers iOS in-app messaging, when to best use it, in addition to several great use cases."
channel:
  - in-app messages

---

# In-App Messages

[In-App Messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) help you get content to your user without interrupting their day with a push notification. Customized and tailored in-app messages enhance the user experience and help your audience get the most value out of your app. With a variety of layouts and customization tools to choose from, in-app messages engage your users more than ever before.

To see examples of in-app messages, check out our [Case Studies][31].

## In-App Message Types

Braze currently offers the following default in-app message types: 

- `Slideup`
- `Modal`
- `Full`
- `HTML Full`

Each in-app message type is highly customizable across content, images, icons, click actions, analytics, display, and delivery.

All in-app messages are subclasses of the `ABKInAppMessage`, which defines basic behavior and traits for all in-app messages. The in-app message class structures as following:

![ABKInAppMessage models][29]

{% alert important %}
By default, in-app messages are enabled after completing the standard SDK integration, including GIF support. 
<br><br>
__Note that integration of `SDWebImage` is required if you plan on using our Braze UI for displaying images__ within iOS In-App Messages, News Feed, or Content Cards.
{% endalert %}

### Expected behaviors by message types

These are what it looks like for your users to open one of our out-of-the-box in-app message types.

{% tabs %}
  {% tab Slideup %}

  [`Slideup`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_slideup.html) in-app messages are so-named because they "slide up" or "slide down" from the top or bottom of the screen.  They cover a small portion of the screen and provide an effective and non-intrusive messaging capability.

  <br>

  ![Slideup Behavior]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

  <br>

{% endtab %}
{% tab Modal %}

[`Modal`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_modal.html) in-app messages appear in the center of the screen and are framed by a translucent panel. Useful for more critical messaging, they can be equipped with up to two click action and analytics enabled buttons.

 <br>

  ![Modal Behavior]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

 <br>

{% endtab %}
{% tab Full Screen %}

[`Full`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_full.html) in-app messages are useful for maximizing the content and impact of your user communication.  The upper half of a `full` in-app message contains an image and the lower half displays text as well as up to two click action and analytics enabled buttons.

<br>

![Full-Screen Behavior]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% tab Custom HTML %}

[`HTML Full`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_h_t_m_l_full.html) in-app messages are useful for creating fully customized user content. User-defined HTML Full in-app message content is displayed in a `WKWebView`and may optionally contain other rich content, such as images and fonts, allowing for full control over message appearance and functionality. <br><br>iOS in-app messages support a JavaScript `appboyBridge` interface to call methods on the Braze Web SDK from within your HTML, see <a href="https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages/best_practices//">Best Practices</a> for more details.

The following example shows a paginated HTML Full in-app message:

![HTML5 IAM Example]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

> Full in-app message content is displayed in a WKWebView and may optionally contain other rich content, such as images and fonts, allowing for full control over message appearance and functionality. **Please note that we currently do not support display of custom HTML in-app messages in an iFrame on the iOS and Android platforms.**

> **Starting in iOS SDK version 3.19.0, the following JavaScript methods are no-ops in HTML in-app messages: `alert`, `confirm`, `prompt`.**

{% endtab %}
{% endtabs %}


[29]: {% image_buster /assets/img_archive/ABKInAppMessage-models.png %}
[30]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
[31]: https://www.braze.com/customers
