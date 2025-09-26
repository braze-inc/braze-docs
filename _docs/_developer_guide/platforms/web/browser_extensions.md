---
nav_title: Browser extensions
article_title: Browser Extensions Integration for Web
platform: Web
page_order: 20
page_type: reference
description: "This article describes how to use the Braze Web SDK inside your Browser Extensions (Google Chrome, Firefox)."

---

# Browser extension

> This article describes how to use the Braze Web SDK inside your Browser Extensions (Google Chrome, Firefox).

Integrate the Braze Web SDK within your browser extension to collect analytics and display rich messaging to users. This includes both **Google Chrome Extensions** and **Firefox Add-Ons**.

## What's supported

In general, since extensions are HTML and JavaScript, you can use Braze for the following:

* **Analytics**: Capture custom events, attributes, and even identify repeat users within your extension. Use these profile traits to power cross-channel messaging.
* **In-app messages**: Trigger in-app messages when users take action within your extension, using our native or custom HTML messaging.
* **Content Cards**: Add a feed of native cards to your extension for onboarding or promotional content.
* **Web Push**: Send timely notifications even when your web page is not currently open.

## What's not supported

* Service workers are not supported by the Braze Web SDK, however, this is on the roadmap for future consideration.

## Extension types

Braze can be included in the following areas of your extension:

| Area | Details | What's supported |
|--------|-------|------|
| Popup Page | The [Popup](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Popups) page is a dialog that can be shown to users when clicking on your extension's icon in the browser toolbar.| Analytics, in-app messages, and Content Cards |
| Background Scripts | [Background Scripts](https://developer.chrome.com/extensions/background_pages) (Manifest v2 only) allow your extension to inspect and interact with user navigation or modify webpages (for example, how ad blockers detect and change content on pages). | Analytics, in-app messages, and Content Cards.<br><br>Background scripts aren't visible to users, so for messaging, you would need to communicate with browser tabs or your popup page when displaying messages. |
| Options Pages | The [Options Page](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Options_pages) lets your users toggle settings within your extension. It's a standalone HTML page that opens a new tab. | Analytics, in-app messages, and Content Cards |
{: .reset-td-br-1 .reset-td-br-2, .reset-td-br-3 role="presentation" }

## Permissions

No additional permissions are required in your `manifest.json` when integrating the Braze SDK (`braze.min.js`) as a local file bundled with your extension. 

However, if you use [Google Tag Manager]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/), or reference the Braze SDK from an external URL, or have set a strict Content Security Policy for your extension, you will need to adjust the [`content_security_policy`](https://developer.chrome.com/extensions/contentSecurityPolicy) setting in your `manifest.json` to allow remote script sources.

## Getting started

{% alert tip %}
Before you get started, make sure you've read through the Web SDK's [Initial SDK setup guide]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) to learn more about our JavaScript integration in general.  <br><br>You may also want to bookmark the [JavaScript SDK reference](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html) for full details on all of the different SDK methods and configuration options.
{% endalert %}

To integrate the Braze Web SDK, you'll first need to download a copy of the latest JavaScript library. This can be done using NPM or directly downloading it from the [Braze CDN](https://js.appboycdn.com/web-sdk/latest/braze.min.js).

Alternatively, if you prefer to use [Google Tag Manager]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/) or use an externally hosted copy of the Braze SDK, keep in mind that loading external resources will require you to adjust your [`content_security_policy`](https://developer.chrome.com/extensions/contentSecurityPolicy) setting in your `manifest.json`.

Once downloaded, be sure to copy the `braze.min.js` file somewhere into your extension's directory.

### Extension popups {#popup}

To add Braze to an extension popup, reference the local JavaScript file in your `popup.html`, as you would in a regular website. If you're using Google Tag Manager, you can add Braze using our [Google Tag Manager templates]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/) instead.

```html
<html>
    <title>popup.html</title>
    <!-- Add the Braze library -->
    <script src="/relative/path/to/braze.min.js"></script>
    <script>
    // Initialize Braze here
    </script>
</html>
```

### Background script (Manifest v2 only) {#background-script}

To use Braze within your extension's background script, add the Braze library to your `manifest.json` in the `background.scripts` array. This will make the global `braze` variable available in your background script context.


```json
{
    "manifest_version": 2,
    "background": {
        "scripts": [
            "relative/path/to/braze.min.js",
            "background.js"
        ],
    }
}
```

### Options page {#options-page}

If you use an options page (via the `options` or `options_ui` manifest properties), you can include Braze just as you would in the [`popup.html` instructions](#popup).

## Initialization

Once the SDK is included, you can initialize the library as usual. 

Since cookies are not supported in browser extensions, you can disable cookies by initializing with `noCookies: true`.

```javascript
braze.initialize("YOUR-API-KEY-HERE", {
    baseUrl: "YOUR-API-ENDPOINT",
    enableLogging: true,
    noCookies: true
});
```

For more information on our supported initialization options, visit the [Web SDK reference](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize).

## Push

Extension popup dialogs don't allow for push prompts (they don't have the URL bar in the navigation). So to register and request push permission within an extension's Popup dialog, you'll have to make use of an alternate domain workaround, as described in [Alternate push domain]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain).

