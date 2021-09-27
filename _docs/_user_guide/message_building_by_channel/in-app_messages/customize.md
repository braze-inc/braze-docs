---
nav_title: Customize
article_title: Customization
page_order: 2
description: "In addition to the out-of-the-box In-App Message templates, Braze also offers customized messaging templates that allow custom HTML, Modals with custom CSS, Video, and more."
channel:
  - in-app messages
  
---

# Customization

In addition to the out-of-the-box [In-App Message templates][1], you can also create customized message templates with the following features:

- [Custom HTML templates](#custom-html-messages) - create a customized template with HTML, JavaScript, and CSS.
- [Modal with custom CSS (web only)](#web-modal-css) - add custom CSS to standard templates for more flexible styling options.
- [Email Capture Form (web only)](#email-capture-form) - collect email addresses into Braze.
- [Reusable Color profiles and CSS](#reusable-color-profiles) - save and re-use color profiles for in-app message templates.
- [Video](#video) - add video to a custom in-app message.

{% alert tip %}
Additional customization of the appearance of your In-App Messages can be accomplished by your developers. See our [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/), [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#in-app-message-customization), or [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/) integration documentation on In-App Messages for more details.
{% endalert %}

## HTML In-App Messages {#custom-html-messages}

While Braze’s out-of-the-box in-app messages can be customized in a variety of ways, you can gain even greater control over the look and feel of your campaigns using messages designed and built using HTML, CSS, and JavaScript. With some simple composition, you can unlock custom functionality and branding to match any of your needs. HTML in-app messages allow for greater control over the look and feel of a message, including:

- Custom Fonts and Styles
- Videos
- Multiple Images
- On-click behaviors
- Interactive Components
- Custom Animations

Custom HTML messages can use the [JavaScript Bridge](#javascript-bridge) methods to log events, set custom attributes, close the message, and more!

Check out our [GitHub repository][2] that contains detailed instructions on how to use and customize HTML in-app messages for your needs, and for a set of HTML5 in-app messages templates to help you get started.

{% alert note %}
To enable HTML in-app messages in the Web SDK, your SDK integration must supply the `allowUserSuppliedJavascript` initialization option to Braze: for example `appboy.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. This is for security reasons since HTML in-app messages can execute JavaScript, so we require a site maintainer to enable them.
{% endalert %}


### JavaScript Bridge {#javascript-bridge}

HTML in-app messages for Web, Android, and iOS support a JavaScript "bridge" interface to the Braze Web SDK, allowing you to trigger custom Braze actions when users click on elements with links or otherwise engage with your content. These methods exist with the global `appboyBridge` variable.

For example, to log a custom attribute and custom event, then close the message, you could use the following JavaScript within your HTML in-app message:

```html
<button id="button">Set Favorite Color</button>
<script>
// wait for the `appboyBridge` ready event, "ab.BridgeReady"
window.addEventListener("ab.BridgeReady", function(){
  // event handler when the button is clicked
  document.querySelector("#button").onclick = function(){
    // track Button 1 clicks for analytics
    // Note: this requires Android SDK v8.0.0, Web SDK v2.5.0, and iOS SDK v3.23.0
    appboyBridge.logClick("0");
    // set the user's custom attribute
    appboyBridge.getUser().setCustomUserAttribute("favorite color", "blue");
    // track a custom event
    appboyBridge.logCustomEvent("completed survey");
    // send the enqueued data to Braze
    appboyBridge.requestImmediateDataFlush();
    // close this in-app message
    appboyBridge.closeMessage();
  };
}, false);
</script>
```
#### appboyBridge methods

The following JavaScript methods are supported within Braze's HTML in-app messages:

<style>
/* makes first column wider */
#article-main > table:first-of-type > tbody > tr td:first-child {
    min-width: 470px !important;
}
/* makes code column smaller font */
#article-main > table:first-of-type > tbody > tr td:first-child code {
    font-size:12px !important;
}
#article-main > table:first-of-type td {
  word-break: break-word;
}
</style>

{% include archive/appboyBridge.md %}

### Link-Based Actions

In addition to custom JavaScript, Braze SDKs can also send analytics data with these convenient URL shortcuts. Note that these query parameters and URL schemes are all case sensitive.

#### Button Click Tracking

{% alert warning %}
The use of `abButtonID` is no longer supported in new "HTML with Preview" message types. Please see our [upgrade guide]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/preview/#backward-incompatible-changes) for more information.
{% endalert %}

To log button clicks for in-app message analytics, you can add `abButtonId` as a query parameter to any deep link, redirect URL, or `<a>` tag.

Use `?abButtonId=0` to log a "Button 1" click, and `?abButtonId=1` to log a "Button 2" click.

As with other URL parameters, the first parameter should begin with a question mark `?`, while subsequent parameters should be separated by an ampersand `&`.

**Examples**:

- `https://example.com/?abButtonId=0` - Button 1 click
- `https://example.com/?abButtonId=1` - Button 2 click
- `https://example.com/?utm_source=braze&abButtonId=0` - Button 1 click with other existing URL parameters
- `myApp://deep-link?page=home&abButtonId=1` - Mobile deeplink with Button 2 click
- `<a href="https://example.com/?abButtonId=1">` - `<a>` tag with Button 2 click

{% alert note %}
In-app messages support only Button 1 and Button 2 clicks. URLs that do not specify one of these two button IDs will be logged as generic "body clicks".
{% endalert %}

#### Open Link in New Window

To open links in a new window, set `?abExternalOpen=true`. The message will be dismissed before opening the link.

For deep linking, Braze will open your URL regardless of the value of `abExternalOpen`.

#### Open as Deeplink (mobile only)

To have Braze handle your HTTP(S) link as a deep link, set `?abDeepLink=true`.

When this query string parameter is absent or set to `false`, Braze will try to open the web link in an internal web browser inside the host app.

#### Custom Events (mobile only)

For mobile apps, you can log log a custom event by setting a link's URL to `appboy://customEvent` together with a `name` URL parameter.

For example, `appboy://customEvent?name=eventName` will log a custom event of `eventName`.

Be sure to URL encode spaces and other special characters as you would in any other URL. For example, `appboy://customEvent?name=event%20name` sends `event name`.

Additional query parameters will be passed as property key-value pairs.

`appboy://customEvent?name=eventName&property1=value1&property2=value2` would log an event called `eventName` with the properties `property1`=`value1` and `property2`=`value2`.

#### News Feed (mobile only)

For mobile apps, you can open the News Feed by setting a link's URL to `appboy://feed`.

For example, `<a href="appboy://feed">View Feed</a>`.

#### Close In-App Message (mobile only)

To close an in-app message, you can set a link's URL to `appboy://close`.

For example, `<a href="appboy://close">Close</a>` will close the in-app message.

## Modal with CSS (Web Only) {#web-modal-css}

If you choose to use a web-only Web Modal with CSS message, you can [apply your own template](#css-template) or write your own CSS in the provided space. This space is already pre-filled with the CSS shown in your message preview, but feel free to adjust it slightly to meet your needs.

If you choose to apply your own template, click __Apply Template__ and choose from the In-App Message Template Gallery. If you don't have any options, you can upload a [CSS Template using the CSS Template builder](#in-app-message-templates).

## Web Email Capture Form {#email-capture-form}

Email capture messages allow you to easily prompt users of your site to submit their email address, after which it will be available within the Braze system for use in all your messaging campaigns.

To navigate to this option, you must create an in-app messaging campaign. From there, ensure **Send To** is set to **Web Browsers**, then select **Web Email Capture Form** for your **Message Type**.

![Select Web Email Capture Form][4]

{% alert note %}
To enable Email Capture in-app messages, your SDK integration must supply the `allowUserSuppliedJavascript` initialization option to Braze, e.g. `appboy.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. This is for security reasons since HTML in-app messages can execute JavaScript, so we require a site maintainer to enable them.
{% endalert %}

#### Customizable Features

- Header, body, and submit button text
- An optional image
- An optional "Terms of Service" link
- Different colors for the header and body text, buttons and background
- Key-value pairs
- Style for header and body text, buttons, button border color, background, and overlay

![emailimage][5]

## Reusable Message Templates {#reusable-color-profiles}

You can save in-app message and in-browser message templates on the dashboard to swiftly build new campaigns and messages using your style. Go to __Templates & Media__, then the __In-App Message Templates__ tab. From this page, you can either edit existing templates or click __+ Create__ and choose __Color Profile__ or __CSS Template__ to create new templates to use in your in-app messages.

### Color Profile

You can customize the color scheme of your message template by either entering HEX color code or by clicking the colored box and selecting a color with the color picker.

Click __Save Color Profile__ on the bottom right when you’re finished.

#### Managing Color Profiles

You can also [duplicate][6] and [archive][7] templates! Learn more about creating and managing templates and creative content in [Templates & Media][8].

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

#### Managing CSS Templates

You can also [duplicate][6] and [archive][7] templates! Learn more about creating and managing templates and creative content in [Templates & Media][8].


## Video {#video}

To play a video in an HTML In-App Message, include the following `<video>` element in your HTML, and replace the video names with your file's name (or the remote asset's URL).

To use a local video asset, be sure to include this file when uploading assets to your campaign.

To support iOS devices, you must include the `playsinline` attribute since full screen playback is not supported at this time.

{% alert note %}
iOS does not support autoplay by default. To update this default option, you can modify the [`ABKInAppMessageHTMLViewController`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ViewControllers/ABKInAppMessageHTMLViewController.m)
{% endalert %}

You can find other possible `<video>` options on [MDN Web Docs][9]

```
<video class="video" autoplay muted playsinline controls>
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.mp4" type="video/mp4">
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.ogg" type="video/ogg">
  Your device does not support playing this video.
</video>
```

{% alert warning %}
Full screen videos will not render correctly on iOS and are not supported at this time. You must include the `playsinline` attribute to show the video within the HTML message instead.
{% endalert %}


[1]: {{site.baseurl}}/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/
[2]: https://github.com/Appboy/appboy-custom-html5-in-app-message-templates
[4]: {% image_buster /assets/img/email_capture_config.png %}
[5]: {% image_buster /assets/img/email_capture.png %}
[6]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/
[7]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/archive/
[8]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/
[9]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video
