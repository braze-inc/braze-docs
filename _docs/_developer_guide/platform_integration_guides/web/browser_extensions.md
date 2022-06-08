---
nav_title: Browser Extensions
article_title: Browser Extensions Integration for Web
platform: Web
page_order: 20
page_type: reference
description: "This article describes how to use the Braze Web SDK inside your Browser Extensions (Google Chrome, Firefox)."

---

# Browser extension integration

Integrate Braze's Web SDK within your browser extension to collect analytics and display rich messaging to users. This includes both **Google Chrome Extensions** and **Firefox Add-Ons**.

## What's supported

In general, since Extensions are simply HTML and Javascript, you can use Braze for the following:

* **Analytics**: Capture custom events, attributes, and even identify repeat users within your extension. Use these profile traits to power cross-channel messaging.
* **In-app messages**: Trigger in-app messages when users take action within your extension, using our native or custom HTML messaging.
* **Content Cards**: Add a feed of native cards to your extension for onboarding or promotional content.
* **Web Push**: Send timely notifications even when your web page is not currently open.

## Extension types

Braze can be included in the following areas of your extension:

| Area | Details | What's supported |
|--------|-------|------|
| Popup Page | The [Popup][1] page is a dialog that can be shown to users when clicking on your extension's icon in the browser toolbar.| Analytics, in-app messages, and Content Cards |
| Background Scripts | [Background Scripts][2] allow your extension to inspect and interact with user navigation or modify webpages (for example, how ad blockers detect and change content on pages). | Analytics, in-app messages, and Content Cards.<br><br>Background scripts aren't visible to users, so for messaging, you would need to communicate with browser tabs or your popup page when displaying messages. |
| Options Pages | The [Options Page][3] lets your users toggle settings within your extension. It's a standalone HTML page that opens a new tab. | Analytics, in-app messages, and Content Cards |
{: .reset-td-br-1 .reset-td-br-2, .reset-td-br-3}

## Permissions

No additional permissions are required in your `manifest.json` when integrating the Braze SDK (`braze.min.js`) as a local file bundled with your extension. 

However, if you use [Google Tag Manager][8], or reference Braze's SDK from an external URL, or have set a strict Content Security Policy for your extension, you will need to adjust the [`content_security_policy`][6] setting in your `manifest.json` to allow remote script sources.

## Getting started

{% alert tip %}
Before you get started, make sure you've read through the Web SDK's [Initial SDK setup guide]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/) to learn more about our Javascript integration in general.  <br><br>You may also want to bookmark the [Javascript SDK reference](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html) for full details on all of the different SDK methods and configuration options.
{% endalert %}

To integrate Braze's Web SDK, you'll first need to download a copy of the latest Javascript library. This can be done using NPM or directly downloading it from [Braze's CDN][7].

Alternatively, if you prefer to use [Google Tag Manager][8] or use an externally hosted copy of Braze's SDK, keep in mind that loading external resources will require you to adjust your [`content_security_policy`][6] setting in your `manifest.json`.

Once downloaded, be sure to copy the `braze.min.js` file somewhere into your extension's directory. For example, using NPM:

```bash
npm install --save @braze/web-sdk;
cp node_modules/@braze/web-sdk/braze.min.js /path/to/extension
```

### Extension popups {#popup}

To add Braze to an extension popup, reference the local Javascript file in your `popup.html`, as you would in a regular website. If you're using Google Tag Manager, you can add Braze using our [Google Tag Manager templates][8] instead.

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

### Background script {#background-script}

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

For more information on our supported initialization options, visit the [Web SDK reference][10].

## Push

Extension popup dialogs don't allow for push prompts (they don't have the URL bar in the navigation). So to register and request push permission within an extension's Popup dialog, you'll have to make use of an alternate domain workaround, as described in [Alternate push domain][11].

[1]: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Popups
[2]: https://developer.chrome.com/extensions/background_pages
[3]: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Options_pages
[6]: https://developer.chrome.com/extensions/contentSecurityPolicy
[7]: https://js.appboycdn.com/web-sdk/latest/braze.min.js
[8]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/
[10]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize
[11]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain
