---
nav_title: Customize
platform: Message_Building_and_Personalization
subplatform: In-App Messages
page_order: 2
---

# Customization

You can either use our [Customizable In-App Message Types](#customizable-in-app-message-types) ([Web Modal CSS](#web-modal-css), [Custom Web Messages](#custom-web-messages), or the [Email Capture Form](#email-capture-form)), which will allow you to refine specific types of messages with precise granularity, or create [Custom In-App Message Templates](#in-app-message-templates) to use over and over again. You can also put [video](#video) into your messages.

## Customizable In-App Message Types

{% alert tip %}
Additional customization of the appearance of your In-App Messages can be accomplished by your developers. See our [iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/), [Web]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/in_app_messaging/#in-app-message-customization), or [Android]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/) integration documentation on In-App Messages for more details.
{% endalert %}

### Web Modal CSS

If you choose to use a web-only, Web Modal with CSS message, you can [apply your own template](#css-template) or write your own CSS in the provided space. This space is already pre-filled with the CSS shown in your message preview, and you should feel free to adjust it slightly to meet your needs.

If you choose to apply your own template, click __Apply Template__ and choose from the In-App Message Template Gallery. If you don't have any options, you can upload a [CSS Template using the CSS Template builder](#in-app-message-templates).

### Custom Web Messages

While Braze’s out-of-the box in-app messages can be customized in a variety of ways, you can gain even greater control over the look and feel of your campaigns using messages designed and built using HTML, CSS, and Javascript. With some simple composition, you can unlock custom functionality and branding to match any of your needs. HTML in-app messages allow for greater control over the look and feel of a message, and anything supported by HTML5 is also supported by Braze.

#### JavaScript Bridge (appboyBridge) {#javascript-bridge}

HTML in-app messages support a Javascript "bridge" interface to the Braze Web SDK, allowing you to trigger custom Braze actions when users click on elements with links or otherwise engage with your content. The following javascript methods are supported in Braze's HTML in-app messages:

{% include archive/appboyBridge.md platform="web" %}

Additionally, for analytics tracking, any `<a>` or `<button>` elements in your HTML will automatically log a "click" action to the campaign associated with the in-app message. To log a "button click" instead of a "body click," either provide a query string value of abButtonId on your link's href (e.g. `<a href="http://mysite.com?abButtonId=0">click me</a>`), or provide an id on the HTML element (e.g. `<a id="0" href="http://mysite.com">click me</a>`).
{% alert note %}
The only button ids currently accepted are "0" and "1." A link with a button id of 0 will be represented as "Button 1" on the Dashboard, while a link with a button id of 1 will be represented as "Button 2."
{% endalert %}

{% alert note %}
  To enable HTML in-app messages, your SDK integration must supply the `enableHtmlInAppMessages` initialization option to Braze: for example `appboy.initialize('YOUR-API_KEY', {enableHtmlInAppMessages: true})`. This is for security reasons - HTML in-app messages can execute javascript so we require a site maintainer to enable them.
{% endalert %}

#### Link-Based Actions (Mobile Apps)

HTML in-app messages on mobile apps can trigger custom Braze actions when users click on elements with links. The supported link schemes are:

Supported Scheme | Corresponding Action | Supported Query Strings
--- | --- |---
Normal Web URL or Deep Linking | For web URLs, Braze will open the new content of the link in a webview within your app by default, or in an external browser when query `abExternalOpen` is true. The HTML5 in-app message will be dismissed before opening the link. For deep linking, Braze will open your URL regardless of the value of `abExternalOpen`. | `abExternalOpen` and `abButtonId`
`appboy://close` | Braze will dismiss the HTML in-app message. | None
`appboy://feed` | Braze will dismiss the HTML in-app message and display a modal News Feed. | `abButtonId`
`appboy://customEvent` | Braze will log a custom event and will NOT dismiss the HTML in-app message. | `name`<br>All additional queries will be set as properties of the custom event.

{% alert tip %}
Link-based actions are not supported by the Web SDK. For cross-platform compatibility, please refer to the [Javascript Bridge](#javascript-bridge) methods.
{% endalert %}

#### Supported Query Strings

You can customize your link actions by appending the optional URL query strings below to your HTTP(S) link:

Query String Name | Value | Action
-----------|-------|-------
`abButtonId` | `{0,1}` | Braze will use the value specified as the button's ID for analytics tracking<br>([https://www.mycompany.com?abButtonId=0](https://www.mycompany.com?abButtonId=0)) *
`name` | Arbitrary string | This represents the custom event name for use with `appboy://customEvent` (e.g., `appboy://customEvent?name=eventName`).
`abExternalOpen` | `{true, false}` | When this query string parameter is absent or set to `false`, Braze will try to open the web link in an internal web browser inside the host app. To have Braze open the web link in an external web browser, set this parameter to `true`.
`abDeepLink` | `{true, false}` | When this query string parameter is absent or set to `false`, Braze will try to open the web link in an internal web browser inside the host app. To have Braze handle your HTTP(S) link as a deep link, set this parameter to `true`.

Analytics tracking is enabled by default for all links that have the `abButtonId` query (see above). A link with `abButtonId=0` will be represented as Button 1 on the Dashboard, while a link with `abButtonId=1` will be represented as Button 2.


Examples:

- `appboy://close`
	- sample close button: `<a href="appboy://close">Close</a>`
- `appboy://feed?abButtonId=0`
- `appboy://customEvent?name=eventName&property1=value1&property2=value2`
	- This would log an event called `eventName` with the properties `property1`=`value1` and `property2`=`value2`.

If you are interested in customizing your in-app messages, please make sure your design or development team is aware of these parameters.

#### HTML In-App Message Templates

We've designed a set of HTML5 in-app messages templates to help you get started. Check out our [Github repository](https://github.com/Appboy/appboy-custom-html5-in-app-message-templates) which contains detailed instructions on how to use and customize these templates for your needs.

##### Customizable Features
- Fonts
- Styles
- Images + Videos
- On-click behaviors
- Interactive Components
- Animation

### Email Capture Form
Email capture messages allow you to easily prompt users of your site to submit their email address, after which it will be available within the Braze system for use in all your messaging campaigns.

{% alert note %}
To enable Email Capture in-app messages, your SDK integration must supply the `enableHtmlInAppMessages` initialization option to Braze, e.g. `appboy.initialize('YOUR-API_KEY', {enableHtmlInAppMessages: true})`. This is for security reasons - HTML in-app messages can execute javascript so we require a site maintainer to enable them.
{% endalert %}

#### Customizable Features
- Header, body, and submit button text
- An optional image
- An optional "Terms of Service" link
- Different colors for the header and body text, buttons and background
- Key-value pairs
- Style for header and body text, buttons, button border color, background, and overlay

## In-App Message Templates

You can save in-app message and in-browser message templates on the dashboard to swiftly build new campaigns and messages using your style. Go to __Templates & Media__, then the __In-App Message Templates__ tab. From this page, you can either edit existing templates, or click __+ Create__ and choose __Color Profile__ or __CSS Template__ to create new templates to use in your in-app messages.

### Color Profile

You can customize the color scheme of your message template by either entering HEX color code or by clicking the colored box and selecting a color with the color picker.

Click __Save Color Profile__ on the bottom right when you’re finished.

### CSS Template

You can customize a complete CSS template for your [Web Modal In-App Message](#web-modal-css).

Name and tag your CSS Template, then choose whether or not it will be your default template. You can write your own CSS in the provided space. This space is already pre-filled with the CSS shown in your message preview, and you should feel free to adjust it slightly to meet your needs.

```css
.ab-message-header, .ab-message-text {
  color: #333333;
  text-align: center;
}

.ab-message-header {
  font-size: 20px;
  font-weight: bold;
}

.ab-message-text {
  font-size: 14px;
  font-weight: normal;
}

.ab-close-button svg {
  fill: #9b9b9b;
}

.ab-message-button {
  border: 1px solid #1b78cf;
  font-size: 14px;
  font-weight: bold;
}
.ab-message-button:first-of-type {
  background-color: white;
  color: #1b78cf;
}
.ab-message-button:last-of-type, .ab-message-button:first-of-type:last-of-type {
  background-color: #1b78cf;
  color: white;
}

.ab-background {
  background-color: white;
}

.ab-icon {
  background-color: #0073d5;
  color: white;
}

.ab-page-blocker {
  background-color: rgba(51, 51, 51, .75);
}
```

As you can see, you can edit everything from the background color to font size and weight, and so much more.

## Video

You are able to display HTML5 videos in our customizable in-app message types with sound included. You can either use an embedded link from a third party (like [Youtube](https://support.google.com/youtube/answer/171780?hl=en)) using custom a HTML5 file, or upload a video to your Braze account in the `assets.zip` folder. This uploaded video will then be sent to the device for local playback, so there is no need for a network connection to play the video. This second option is recommended mostly for shorter videos.

{% tabs %}
  {% tab Android %}

__Android__

To use a video in Android in-app messages, all you need to do is create a custom HTML5 file [using one of our templates on Github](https://github.com/Appboy/appboy-custom-html5-in-app-message-templates).

Then, copy and paste the following `HTML` snippet into your code, replacing the source parameters with your actual file names.

```
<video class="video" autoplay muted playsinline controls>
  <source src="mov_bbb.mp4" type="video/mp4">
  <source src="mov_bbb.ogg" type="video/ogg">
  Your device does not support HTML5 video.
</video>
```

Then, in your working directory, add the video file and zip all the files. Make sure to include the `CSS/JavaScript` but exclude the `HTML`.

Finally, upload the files to your Braze account using the HTML + Asset Zip in your In-App Message Compose tab. You can either upload the ZIP or enter its URL.

![Video_IAM]({% image_buster /assets/img/video_iam.png %})
{% endtab %}

{% tab iOS %}
__iOS__

By default, the `WKWebView` in our default view controller [here](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ViewControllers/ABKInAppMessageHTMLViewController.m) allows inline media playback, including videos, but does not support autoplay.

Example `HTML` snippet:

```
<video class="video" playsinline>
  <source src="mov_bbb.mp4" type="video/mp4">
  <source src="mov_bbb.ogg" type="video/ogg">
  Your device does not support HTML5 video.
</video>
```

![Video_IAM]({% image_buster /assets/img/video_iam.png %})

{% endtab %}

{% tab Web %}

__Web__

To use a video in Web in-app messages, embed a link from a third party (like [Youtube](https://support.google.com/youtube/answer/171780?hl=en)) into your [Custom Web Message]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-web-message).

{% endtab %}
{% endtabs %}
