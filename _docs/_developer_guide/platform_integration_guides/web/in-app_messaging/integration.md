---
nav_title: Integration
article_title: In-App Message Integration for Web
platform: Web
channel: in-app messages
page_order: 0
page_type: reference
description: "This article includes resources on in-app message types and message behavior for your web application."

---

# In-app messages integration

[In-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) help you get content to your users without interrupting their day with a push notification. Customized and tailored in-app messages enhance the user experience and help your audience get the most value from your app. With various layouts and customization tools to choose from, in-app messages engage your users more than ever before.

Check out our [case studies][53] to see examples of in-app messages.

## In-app message types

Braze currently offers the following default in-app message types: 

- `Slideup`
- `Modal`
- `Full`
- `HTML`

Each in-app message type is customizable across content, images, icons, click actions, analytics, display, and delivery.

All in-app messages inherit their prototype from [`InAppMessage`][2], which defines basic behavior and traits for all in-app messages. The protypical subclasses are [`SlideUpMessage`][3], [`ModalMessage`][6], [`FullScreenMessage`][7], and [`HtmlMessage`][12].

## Expected behaviors by message type

These are what it looks like for your users to open one of our out-of-the-box in-app message types.

{% tabs %}
{% tab Slideup %}

[`SlideUp`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html) in-app messages are so-named because traditionally on mobile platforms, they "slide up" or "slide down" from the top or bottom of the screen. In the Braze Web SDK, these messages are displayed as more of a Growl or Toast style notification to align with the web's dominant paradigm. They cover a small portion of the screen and provide an effective and non-intrusive messaging capability.

![An in-app message sliding from the bottom of a phone screen displaying "Humans are complicated. Custom engagement shouldn't be." In the background is the same in-app message displayed in the bottom corner of a web page.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}

[`Modal`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html) in-app messages appear in the center of the screen and are framed by a translucent panel. Useful for more critical messaging, they can be equipped with up to two click action and analytics-enabled buttons.

![A modal in-app message in the center of a phone screen displaying "Humans are complicated. Custom engagement shouldn't be." In the background is the same in-app message displayed in the center of a web page.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Full Screen %}

[`Full`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html) in-app messages are useful for maximizing the content and impact of your user communication. On narrow browser windows (e.g., the mobile web), `full` in-app messages take up the entire browser window. On larger browser windows, `full` in-app messages appear similarly to `modal` in-app messages. The upper half of a `full` in-app message contains an image, and the lower half allows up to eight lines of text as well as up to two click action, and analytics-enabled buttons

![A full screen in-app message shown across an entire phone screen displaying, "Humans are complicated. Custom engagement shouldn't be." In the background is the same in-app message displayed largely in the center of a web page.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Custom HTML %}

[`HTML`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.htmlmessage.html) in-app messages are useful for creating fully customized user content. User-defined HTML is displayed in an iframe and may contain rich content, such as images, fonts, videos, and interactive elements, allowing for full control over message appearance and functionality. These support a JavaScript `appboyBridge` interface to call methods on the Braze Web SDK from within your HTML, see our [best practices]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/) for more details.

{% alert important %}

To enable HTML in-app messages, your SDK integration **must** supply the `allowUserSuppliedJavascript` initialization option to Braze, e.g., `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. This is for security reasons - HTML in-app messages can execute JavaScript so we require a site maintainer to enable them.

{% endalert %}

The following example shows a paginated HTML in-app message:

![An HTML in-app message with the a carousel of content and interactive buttons.]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

{% endtab %}
{% endtabs %}

## Integration

By default, in-app messages are automatically displayed as part of our recommended [integration instructions][1]. Additional customization can be done by following the steps in this guide.

[1]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[2]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html
[3]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html
[6]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html
[7]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html
[12]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.htmlmessage.html
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#slideup-in-app-messages
[17]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#modal-in-app-messages
[41]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#full-in-app-messages
[42]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#html-in-app-messages
[53]: https://www.braze.com/customers
