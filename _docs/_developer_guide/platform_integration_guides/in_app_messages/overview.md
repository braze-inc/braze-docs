---
nav_title: Overview
page_order: 0
description: ""
---

# Overview

> Combine Android, FireOS, iOS, and Web.

Android & FireOS:

# In-App Messages

__In-App Messages__ help you get content to your user without interrupting their day with a push notification. Customized and tailored in-app messages enhance the user experience and help your audience get the most value out of your app. With a variety of layouts and customization tools to choose from, in-app messages engage your users more than ever before.

To see examples of in-app messages, check out our [Client Integration Gallery][83].

## When to Use In-App Messages

In-app messages are good for a lot of things. They can be used in web apps, Android apps, iOS apps, and more!

In-app messages don't deliver outside of the user's app and won't intrude on their home screen like push notifications do. In-app messages, by their nature, exist within your app and come with context and are almost never unwelcome! They're always delivered when the user is active within your app.

#### Great Use Cases

- New App Features
- App Management
- Reviews
- App Upgrades/Updates
- Giveaways & Sweepstakes
- Sales and Promotions
- Product Sales
- Encouraging and rewarding discovery
- [Permission Requests/Push Priming][84]

## In-App Message Types

Braze offers several default in-app message types, each customizable with messages, images, [Font Awesome][15] icons, click actions, analytics, editable styling and color schemes. The currently available types are `Slideup`, `Modal`, `Full`, and `HTML Full`. It is also possible to [define your own custom in-app message view][12].

All in-app messages implement the [`IInAppMessage`][3] interface, which defines basic behavior and traits for all in-app messages. [`InAppMessageBase`][27] is an abstract class that implements `IInAppMessage` and provides the foundational in-app message implementation. All in-app message classes are subclasses of `InAppMessageBase`.

In addition, there is a subinterface of `IInAppMessage` called [`IInAppMessageImmersive`][8], which adds click action and analytics enabled [buttons][50], as well as header text and a close button. [`InAppMessageImmersiveBase`][28] is an abstract class that implements `IInAppMessageImmersive` and provides the foundational `immersive` in-app message implementation. `Modal` and `Full` in-app messages are subclasses of `InAppMessageImmersiveBase`.

HTML Full in-app messages are [`InAppMessageHtmlFull`][51] instances, which implement [`IInAppMessageHtml`][52], another subclass of `IInAppMessage`.

### Expected Behaviors by Message Types

These are what each in-app message type will appear like for your users.

{% tabs %}
  {% tab Slideup %}
  [`Slideup`](https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/InAppMessageSlideup.html) in-app messages are so-named because they "slide up" or "slide down" from the top or bottom of the screen.  They cover a small portion of the screen and provide an effective and non-intrusive messaging capability.

  <br>

  ![Slideup Behavior]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

  <br>

{% endtab %}
{% tab Modal %}
[`Modal`](https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/InAppMessageModal.html) in-app messages appear in the center of the screen and are framed by a translucent panel. Useful for more critical messaging, they can be equipped with up to two click action and analytics enabled buttons.

  <br>

  ![Modal Behavior]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

  <br>


{% endtab %}
{% tab Full Screen %}
[`Full`](https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/InAppMessageHtmlFull.html) in-app messages are useful for maximizing the content and impact of your user communication.  The upper half of a `full` in-app message contains an image and the lower half displays text as well as up to two click action and analytics enabled buttons.

![Full Example]({% image_buster /assets/img_archive/In-App_Full.png %})


{% endtab %}
{% tab Custom HTML %}
[`HTML Full`](https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/IInAppMessageHtml.html) in-app messages are useful for creating fully customized user content. User-defined HTML Full in-app message content is displayed in a {% if include.platform == "iOS" %}`WKWebView`{% elsif include.platform == "Android" %}`WebView`{% endif %} and may optionally contain other rich content, such as images and fonts, allowing for full control over message appearance and functionality. <br><br>Android in-app messages support a JavaScript `appboyBridge` interface to call methods on the Braze Web SDK from within your HTML, see <a href="https://www.braze.com/docs/help/best_practices/in-app_messages/previous_in-app_message_generations/">Best Practices</a> for more details.

<br>

![Full-Screen Behavior]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

<br>

Full in-app message content is displayed in a `WKWebView` and may optionally contain other rich content, such as images and fonts, allowing for full control over message appearance and functionality.

{% alert important %}
Please note that we currently do not support display of custom HTML in-app messages in an iFrame on the iOS and Android platforms.
{% endalert %}

{% endtab %}
{% endtabs %}

#### In-Depth: Defining Custom In-App Message Types

Braze's `slideup` in-app message object extends [`InAppMessageBase`][27]. Braze's `full` and `modal` type messages extend [`InAppMessageImmersiveBase`][28]. Extending one of these classes gives you the option of adding custom functionality to your locally generated in-app messages.

[3]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/IInAppMessage.html
[8]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/IInAppMessageImmersive.html
[12]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/#setting-a-custom-view-factory
[15]: http://fortawesome.github.io/Font-Awesome/
[27]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/InAppMessageBase.html
[28]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/InAppMessageImmersiveBase.html
[50]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/MessageButton.html
[51]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/InAppMessageHtmlFull.html
[52]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/IInAppMessageHtml.html
[83]: {{site.baseurl}}/help/best_practices/client_integration_gallery/#client-integration-iam
[84]: {{site.baseurl}}/help/best_practices/push/creating_custom_opt-in_prompts/#creating-custom-opt-in-prompts

iOS:


# In-App Messages

## When to Use In-App Messages

In-app messages are good for a lot of things. They can be used in web apps, Android apps, iOS apps, and more!

In-app messages don't deliver outside of the user's app and won't intrude on their home screen like push notifications do. In-app messages, by their nature, exist within your app and come with context and are almost never unwelcome! They're always delivered when the user is active within your app.

### Great Use Cases

- New App Features
- App Management
- Reviews
- App Upgrades/Updates
- Giveaways & Sweepstakes
- Sales and Promotions
- Product Sales
- Encouraging and rewarding discovery
- [Permission Requests/Push Priming][30]

To see examples of in-app messages, check out our [Client Integration Gallery][31].

[Create an in-app message]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/) now!

## In-App Message Types
Braze currently offers the following default in-app message types: `Slideup`, `Modal`, `Full` and `HTML Full`. Each in-app message type is highly customizable across content, images, icons, click actions, analytics, display, and delivery.

All in-app messages are subclasses of the `ABKInAppMessage`, which defines basic behavior and traits for all in-app messages. The in-app message class structures as following:

![ABKInAppMessage models][29]

{% alert important %}
By default, in-app messages are enabled after completing the standard SDK integration, including GIF support. 
<br><br>
__Note that integration of `SDWebImage` is required if you plan on using our Braze UI for displaying images__ within iOS In-App Messages, News Feed, or Content Cards.
{% endalert %}

### Expected Behaviors by Message Types

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

[`HTML Full`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_h_t_m_l_full.html) in-app messages are useful for creating fully customized user content. User-defined HTML Full in-app message content is displayed in a `WKWebView`and may optionally contain other rich content, such as images and fonts, allowing for full control over message appearance and functionality. <br><br>iOS in-app messages support a JavaScript `appboyBridge` interface to call methods on the Braze Web SDK from within your HTML, see <a href="https://www.braze.com/docs/help/best_practices/in-app_messages/previous_in-app_message_generations/">Best Practices</a> for more details.

The following example shows a paginated HTML Full in-app message:

![HTML5 Example]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

> Full in-app message content is displayed in a WKWebView and may optionally contain other rich content, such as images and fonts, allowing for full control over message appearance and functionality. **Please note that we currently do not support display of custom HTML in-app messages in an iFrame on the iOS and Android platforms.**

> **Starting in iOS SDK version 3.19.0, the following JavaScript methods are no-ops in HTML in-app messages: `alert`, `confirm`, `prompt`.**

{% endtab %}
{% endtabs %}


[29]: {% image_buster /assets/img_archive/ABKInAppMessage-models.png %}
[30]: {{site.baseurl}}/help/best_practices/push/creating_custom_opt-in_prompts/#creating-custom-opt-in-prompts
[31]: {{site.baseurl}}/help/best_practices/client_integration_gallery/

Web:


# In-App Messages

__In-App Messages__ help you get content to your user without interrupting their day with a push notification. Customized and tailored in-app messages enhance the user experience and help your audience get the most value out of your app. With a variety of layouts and customization tools to choose from, in-app messages engage your users more than ever before.

{% comment %}
Embed video on the right. Demos all of the topics mentioned on this page.
{% endcomment %}

## When to Use In-App Messages

In-app messages are good for a lot of things. They can be used in web apps, Android apps, iOS apps, and more!

In-app messages don't deliver outside of the user's app and won't intrude on their home screen, like push notifications do. In-app messages, by their nature, exist within your app and come with context and are rarely unwelcome! They're always delivered when the user is active within your app.

#### Great Use Cases

- New App Features
- App Management
- Reviews
- App Upgrades/Updates
- Giveaways & Sweepstakes

To see examples of in-app messages, check out our [Client Integration Gallery][53].

## In-App Message Types

Braze currently offers the following default in-app message types: [`Slideup`][13], [`Modal`][17], and [`Full`][41] and [`HTML`][42].  Each in-app message type is customizable across content, images, icons, click actions, analytics, display, and delivery.

All in-app messages inherit their prototype from [`appboy.InAppMessage`][2], which defines basic behavior and traits for all in-app messages. The protypical subclasses are [appboy.SlideUpMessage][3], [appboy.ModalMessage][6], [appboy.FullScreenMessage][7], and [appboy.HtmlMessage][12].

## Expected Behaviors by Message Types

These are what it looks like for your users to open one of our out-of-the-box in-app message types.

{% tabs %}
  {% tab Slideup %}

  [`SlideUp`](https://js.appboycdn.com/web-sdk/latest/doc/ab.SlideUpMessage.html) in-app messages are so-named because traditionally on mobile platforms they "slide up" or "slide down" from the top or bottom of the screen. In the Braze Web SDK, these messages are displayed as more of a Growl or Toast style notification, to align with the web's dominant paradigm. They cover a small portion of the screen and provide an effective and non-intrusive messaging capability.

  <br>

  ![Slideup Behavior]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

  <br>

{% endtab %}
{% tab Modal %}

[`Modal`](https://js.appboycdn.com/web-sdk/latest/doc/ab.ModalMessage.html) in-app messages appear in the center of the screen and are framed by a translucent panel. Useful for more critical messaging, they can be equipped with up to two click action and analytics enabled buttons.

  <br>

  ![Modal Behavior]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

  <br>

{% endtab %}
{% tab Full Screen %}

[`Full`](https://js.appboycdn.com/web-sdk/latest/doc/ab.FullScreenMessage.html) in-app messages are useful for maximizing the content and impact of your user communication. On narrow browser windows (e.g. the mobile web), `full` in-app messages take up the entire browser window. On larger browser windows, `full` in-app messages appear similarly to `modal` in-app messages. The upper half of a `full` in-app message contains an image and the lower half allows up to eight lines of text as well as up to two click action and analytics enabled buttons

<br>

![Full-Screen Behavior]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% tab Custom HTML %}

[`HTML`](https://js.appboycdn.com/web-sdk/latest/doc/ab.HtmlMessage.html) in-app messages are useful for creating fully customized user content. User-defined HTML is displayed in an iframe and may contain rich content, such as images, fonts, videos, and interactive elements, allowing for full control over message appearance and functionality. These support a JavaScript `appboyBridge` interface to call methods on the Braze Web SDK from within your HTML, see [Best Practices]({{site.baseurl}}/help/best_practices/in-app_messages/web_browsers_only/#web-html-messages) for more details.

{% alert important %}

To enable HTML in-app messages, your SDK integration __must__ supply the `allowUserSuppliedJavascript` initialization option to Braze, e.g. `appboy.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. This is for security reasons - HTML in-app messages can execute JavaScript so we require a site maintainer to enable them.
<br> <br>
At Braze, the web SDK treats the "Email Web Capture Form" message type template as an HTML in-app message, therefore the same `allowUserSuppliedJavascript` option must be set.

{% endalert %}

The following example shows a paginated HTML in-app message:

![HTML5 Example]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

{% endtab %}
{% endtabs %}

[2]: https://js.appboycdn.com/web-sdk/latest/doc/ab.InAppMessage.html
[3]: https://js.appboycdn.com/web-sdk/latest/doc/ab.SlideUpMessage.html
[6]: https://js.appboycdn.com/web-sdk/latest/doc/ab.ModalMessage.html
[7]: https://js.appboycdn.com/web-sdk/latest/doc/ab.FullScreenMessage.html
[12]: https://js.appboycdn.com/web-sdk/latest/doc/ab.HtmlMessage.html
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#slideup-in-app-messages
[17]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#modal-in-app-messages
[41]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#full-in-app-messages
[42]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#html-in-app-messages
[53]: {{site.baseurl}}/help/best_practices/client_integration_gallery/#client-integration-iam
