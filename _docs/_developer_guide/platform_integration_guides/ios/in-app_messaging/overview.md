---
nav_title: Overview
platform: iOS
page_order: 0
search_rank: 5
---

# In-App Messages

__In-App Messages__ help you get content to your user without interrupting their day with a push notification. Customized and tailored in-app messages enhance the user experience and help your audience get the most value out of your app. With a variety of layouts and customization tools to choose from, in-app messages engage your users more than ever before.

To see examples of in-app messages, check out our [Client Integration Gallery][31].

{% comment %}
Embed video on the right. Demos all of the topics mentioned on this page.
{% endcomment %}

{% alert note %}
Braze has refreshed in-app messages! Though the creation process is very much the same, our in-app messages have a new, modern look and feel optimized for the best experiences for your customers and give you more options to personalize the experience. For more information on our most recent upgrades to in-app messages, check out our [Generation Comparison documentation]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/generations/)!
{% endalert %}

[Create an in-app message]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/create/) now!

By default, in-app messages are enabled after completing the standard SDK integration, including GIF support. Note that if you did not integrate SDWebImage, in-app messages with images will not work.

## When to Use In-App Messages

In-app messages are good for a lot of things. They can be used in web apps, Android apps, iOS apps, and more!

In-app messages don't deliver outside of the user's app and won't intrude on their home screen, like push notifications do. In-app messages, by their nature, exist within your app and come with context and are almost never unwelcome! They're always delivered when the user is active within your app.

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

## In-App Message Types
Braze currently offers the following default in-app message types: `Slideup`, `Modal`, `Full` and `HTML Full`. Each in-app message type is highly customizable across content, images, icons, click actions, analytics, display and delivery.

All in-app messages are subclasses of the `ABKInAppMessage`, which defines basic behavior and traits for all in-app messages. The in-app message class structures as following:

![ABKInAppMessage models][29]

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

[`HTML Full`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_h_t_m_l_full.html) in-app messages are useful for creating fully customized user content. User-defined HTML Full in-app message content is displayed in a `WKWebView`and may optionally contain other rich content, such as images and fonts, allowing for full control over message appearance and functionality.

The following example shows a paginated HTML Full in-app message:

![HTML5 Example]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

> Full in-app message content is displayed in a WKWebView and may optionally contain other rich content, such as images and fonts, allowing for full control over message appearance and functionality. **Please note that we currently do not support display of custom HTML in-app messages in an iFrame on the iOS and Android platforms.**

{% endtab %}
{% endtabs %}


[1]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_slideup.html
[2]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/InAppMessageSlideup.html
[3]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_modal.html
[4]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/InAppMessageModal.html
[5]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_full.html
[6]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/InAppMessageFull.html
[7]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_h_t_m_l_full.html
[8]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/InAppMessageHtmlFull.html
[9]: {% image_buster /assets/img_archive/In-App_Slideup.png %}
[10]: {% image_buster /assets/img_archive/In-App_Modal.png %}
[11]: {% image_buster /assets/img_archive/In-App_Full.png %}
[12]: {% image_buster /assets/img_archive/HTML5.gif %}
[13]: {% image_buster /assets/img_archive/trigger-iam-composer.png %}
[14]: {{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/create/#original-in-app-messages
[15]: {{ site.baseurl }}/developer_guide/platform_integration_guides/{{ include.platform }}/analytics/tracking_sessions/#session-lifecycle
[16]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/AppDelegate.m
[17]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/res/values/appboy.xml
[19]: {{ site.baseurl }}/developer_guide/platform_integration_guides/{{ include.platform }}/in-app_messaging/#in-app-messages-triggered
[23]: {% image_buster /assets/img_archive/ios-html-full-iam.gif %}
[24]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/#tracking-custom-events
[25]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/#tracking-custom-events
[29]: {% image_buster /assets/img_archive/ABKInAppMessage-models.png %}
[30]: {{ site.baseurl }}/help/best_practices/push/creating_custom_opt-in_prompts/#creating-custom-opt-in-prompts
[31]: {{ site.baseurl }}/help/best_practices/client_integration_gallery/#client-integration-iam
