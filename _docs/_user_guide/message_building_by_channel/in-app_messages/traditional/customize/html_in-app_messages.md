---
nav_title: HTML In-App Messages
article_title: Custom HTML In-App Messages
page_order: 0
page_type: reference
description: "This article provides an overview of custom code in-app messages, including JavaScript methods, button tracking, and using the interactive HTML preview in Braze."
channel:
  - in-app messages
---

# Custom HTML in-app messages {#custom-html-messages}

> While Braze's standard in-app messages can be customized in a variety of ways, you can gain even greater control over the look and feel of your campaigns using messages designed and built using HTML, CSS, and JavaScript. With some simple composition, you can unlock custom functionality and branding to match any of your needs. 

HTML in-app messages allow for greater control over the look and feel of a message, including the following:

- Custom fonts and styles
- Videos
- Multiple images
- On-click behaviors
- Interactive components
- Custom animations

Custom HTML messages can use the [JavaScript Bridge](#javascript-bridge) methods to log events, set custom attributes, close the message, and more! Check out our [GitHub repository][2] that contains detailed instructions on how to use and customize HTML in-app messages for your needs, and for a set of HTML5 in-app messages templates to help you get started.

{% alert note %}
To enable HTML in-app messages through the Web SDK, you must supply the `allowUserSuppliedJavascript` initialization option to Braze: for example `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. This is for security reasons since HTML in-app messages can execute JavaScript, so we require a site maintainer to enable them.
{% endalert %}

## JavaScript bridge {#javascript-bridge}

HTML in-app messages for Web, Android, iOS, and Swift SDKs support a JavaScript "bridge" to interface with Braze SDK, allowing you to trigger custom Braze actions when users click on elements with links or otherwise engage with your content. These methods exist with the global `appboyBridge` variable.

For example, to log a custom attribute and custom event, then close the message, you could use the following JavaScript within your HTML in-app message:

```html
<button id="button">Set Favorite Color</button>
<script>
// Wait for the `appboyBridge` ready event, "ab.BridgeReady"
window.addEventListener("ab.BridgeReady", function(){
  // Event handler when the button is clicked
  document.querySelector("#button").onclick = function(){
    // Track Button 1 clicks for analytics
    // Note: This requires Android SDK v8.0.0, Web SDK v2.5.0, Swift SDK v5.4.0, and iOS SDK v3.23.0
    appboyBridge.logClick("0");
    // Set the user's custom attribute
    appboyBridge.getUser().setCustomUserAttribute("favorite color", "blue");
    // Track a custom event
    appboyBridge.logCustomEvent("completed survey");
    // Send the enqueued data to Braze
    appboyBridge.requestImmediateDataFlush();
    // Close this in-app message
    appboyBridge.closeMessage();
  };
}, false);
</script>
```

### JavaScript Bridge methods {#bridge}

The following JavaScript methods are supported within Braze's HTML in-app messages:

<style>
/* Makes first column wider */
#article-main > table:first-of-type > tbody > tr td:first-child {
    min-width: 470px !important;
}
/* Makes code column smaller font */
#article-main > table:first-of-type > tbody > tr td:first-child code {
    font-size:12px !important;
}
#article-main > table:first-of-type td {
  word-break: break-word;
}
</style>

{% multi_lang_include archive/appboyBridge.md %}

## Link-based actions

In addition to custom JavaScript, Braze SDKs can also send analytics data with these convenient URL shortcuts. Note that these query parameters and URL schemes are all case sensitive.

### Button click tracking

{% alert warning %}
The use of `abButtonID` is not supported in [HTML with Preview]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/preview/) message types. For more information, see our [upgrade guide]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/preview/#backward-incompatible-changes).
{% endalert %}

To log button clicks for in-app message analytics, you can add `abButtonId` as a query parameter to any deep link, redirect URL, or anchor element `<a>`. Use `?abButtonId=0` to log a "Button 1" click, and `?abButtonId=1` to log a "Button 2" click.

As with other URL parameters, the first parameter should begin with a question mark `?`, while subsequent parameters should be separated by an ampersand `&`.

#### Examples

- `https://example.com/?abButtonId=0` - Button 1 click
- `https://example.com/?abButtonId=1` - Button 2 click
- `https://example.com/?utm_source=braze&abButtonId=0` - Button 1 click with other existing URL parameters
- `myApp://deep-link?page=home&abButtonId=1` - Mobile deeplink with Button 2 click
- `<a href="https://example.com/?abButtonId=1">` - Anchor element `<a>` with Button 2 click

{% alert note %}
In-app messages support only Button 1 and Button 2 clicks. URLs that do not specify one of these two button IDs will be logged as generic "body clicks".
{% endalert %}

### Open link in new window (mobile only)

To open links outside your app in a new window, set `?abExternalOpen=true`. The message will be dismissed before opening the link.

For deep linking, Braze will open your URL regardless of the value of `abExternalOpen`.

### Open as deeplink (mobile only)

To have Braze handle your HTTP or HTTPS link as a deep link, set `?abDeepLink=true`.

When this query string parameter is absent or set to `false`, Braze will try to open the web link in an internal web browser inside the host app.

### News Feed (mobile only)

{% alert note %}
News Feed is being deprecated. Braze recommends that customers who use our News Feed tool move over to our Content Cards messaging channel—it's more flexible, customizable, and reliable. Check out the [migration guide]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) for more.
{% endalert %}

For mobile apps, you can open the News Feed by setting a link's URL to `appboy://feed`.

For example, `<a href="appboy://feed">View Feed</a>`.

### Close in-app message

To close an in-app message, you can use the `appboyBridge.closeMessage()` javascript method.

For example, `<a onclick="appboyBridge.closeMessage()" href="#">Close</a>` will close the in-app message.

## HTML upload with preview

When crafting custom HTML in-app messages, you can preview your interactive content directly in Braze. 

The message preview panel of the editor shows a realistic preview that renders the JavaScript included in your message. You can preview and interact with your custom messages from the preview panel by clicking through pagination, submitting forms or surveys, watching JavaScript animations, and more!

![Interacting with the HTML preview by swiping through pages.]({% image_buster /assets/img/iam-beta-javascript-preview.gif %})

{% alert tip %}
Any `appboyBridge` JavaScript methods you use in your HTML won't update user profiles while previewing in the dashboard.
{% endalert %}

### SDK requirements {#supported-sdk-versions}

To use the HTML preview for in-app messages, you must upgrade to the following minimum Braze SDK versions:

{% sdk_min_versions web:2.5.0 android:8.0.0 ios:3.23.0 %}

{% alert warning %}
Because this message type can only be received by certain later SDK versions, users that are on unsupported SDK versions will not receive the message. Consider adopting this message type after a significant portion of your user base is reachable, or target only those users whose app version is later than the requirements. Learn more about [filtering by most recent app version]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions).
{% endalert %}

### Creating a campaign {#instructions}

When creating a **Custom Code** in-app message, choose **HTML Upload with Preview** as the custom type. If you haven't previously created custom code in-app messages (live or drafts), this option is automatically applied and you won't need to make a selection.

![Creating an in-app message that sends to both Mobile and Web browsers where "Message Type" is Custom Code and "Custom Type" is HTML Upload with Preview.]({% image_buster /assets/img/iam-beta-html-cross-channel.png %})

Keep in mind that your mobile app users need to upgrade to the supported SDK versions to receive this message. We recommend that you [nudge users to upgrade]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/) their mobile apps before launching campaigns that depend on newer Braze SDK versions.

#### Asset files

When creating custom code in-app messages with HTML upload, you can upload campaign assets to the Braze [Media Library]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) to reference in your message.

The following file types are supported for upload:

| File Type        | File Extension                    |
| :--------------- | :-------------------------------- |
| Font Files       | `.ttf`, `.woff`, `.otf`, `.woff2` |
| SVG Images       | `.svg`                            |
| Javascript Files | `.js`                             |
| CSS Files        | `.css`                            |
{: .reset-td-br-1 .reset-td-br-2}

Braze recommends uploading assets to the Media Library for two reasons:

1. Assets added to a campaign via the Media Library allow your messages to be displayed even while the user is offline, or has a poor internet connection.
2. Assets uploaded to Braze can be reused across campaigns.

##### Adding asset files

You can add new or existing assets to your campaign.

To add new assets to your campaign, use the drag-and-drop section to upload a file. Assets added in this section will also be automatically added to the Media Library. To add assets that you've already uploaded to the Media Library, select **Add from Media Library**.

After your assets are added, they will appear in the **Assets for this campaign** section. 

If an asset's filename matches that of a local HTML asset it will be replaced automatically (for example, `cat.png` is uploaded and `<img src="cat.png" />` exists). 

Otherwise, hover over an asset from the list and select <i class="fas fa-copy"></i> **Copy** to copy the file's URL to your clipboard. Then paste the copied asset URL into your HTML as you normally would when referencing a remote asset.


### HTML editor

Changes you make in the HTML automatically render in the preview panel as you type. Any [`appboyBridge` JavaScript](#bridge) methods you use in your HTML won't update user profiles while previewing in the dashboard.

You can configure **Editor Settings** to toggle wrap text, change the font size, or choose a color theme. The code editor includes different color themes for syntax highlighting, which helps you spot potential code errors directly in the message composer and better organize your code (using spaces or tabs—whichever side of that argument you're on).

![Syntax highlighting options in the "Editor Settings" dropdown when composing an HTML in-app message.]({% image_buster /assets/img/iam-beta-html-syntax-highlighting.png %})

{% alert tip %}
You can press <kbd>Ctrl</kbd> + <kbd>F</kbd> (Windows) or <kbd>Command</kbd> + <kbd>F</kbd> (Mac) within the HTML editor to search within your code!
{% endalert %}

### Button tracking {#button-tracking-improvements}

You can track performance within your custom code in-app message using the [`appboyBridge.logClick(button_id)`][1] JavaScript method. This allows you to programmatically track "Button 1", "Button 2", and "Body Clicks" using `appboyBridge.logClick("0")`, `appboyBridge.logClick("1")`, or `appboyBridge.logClick()`, respectively.

| Clicks     | Method                       |
| ---------- | ---------------------------- |
| Button 1   | `appboyBridge.logClick("0")` |
| Button 2   | `appboyBridge.logClick("1")` |
| Body click | `appboyBridge.logClick()`    |
| Custom button tracking |`appboyBridge.logClick("your custom name here")`|
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
This method of button tracking replaces the prior automatic click tracking methods (i.e., `?abButtonId=0`), which have been removed.
{% endalert %}

You can track multiple button click events per impression. For example, to close a message and log a Button 2 click, you can use the following:

```html
<a href="#" onclick="appboyBridge.logClick('1');appboyBridge.closeMessage()">✖</a>
``` 

You can also track new custom button names—up to 100 unique names per campaign. For example, `appboyBridge.logClick("blue button")` or `appboyBridge.logClick("viewed carousel page 3")`.

#### Limitations

- You can have up to 100 unique button IDs per campaign.
- Button IDs can have up to 255 characters each.
- Button IDs can only include letters, numbers, spaces, dashes, and underscores.

### Backward incompatible changes {#backward-incompatible-changes}

1. The most notable incompatible change with this new message type is the SDK requirements. Users whose app SDK does not meet the minimum [SDK version requirements](#supported-sdk-versions) will not be shown the message.
<br>

2. The `appboy://close` deeplink, which was previously supported on mobile apps, has been removed in favor of the JavaScript `appboyBridge.closeMessage()`. This allows for cross-platform HTML messages, since the web does not support deeplinks.

3. Automatic click tracking, which used `?abButtonId=0` for button IDs, and "body click" tracking on close buttons have been removed. The following code examples show how to change your HTML to use our new click tracking JavaScript methods:

   | Before | After |
   |:-------- |:------------|
   |<code>&lt;a href="appboy://close"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="appboyBridge.logClick();appboyBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
   |<code>&lt;a href="appboy://close?abButtonId=0"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="appboyBridge.logClick('0');appboyBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
   |<code>&lt;a href="app://deeplink?abButtonId=0">Track button 1&lt;/a&gt;</code>|<code>&lt;a href="app://deeplink" onclick="appboyBridge.logClick('0')"&gt;Track button 1&lt;/a&gt;</code>|
   |<code>&lt;script&gt;<br>location.href = "appboy://close?abButtonId=1"<br>&lt;/script&gt;</code>|<code>&lt;script&gt;<br>window.addEventListener("ab.BridgeReady", function(){<br>&nbsp;&nbsp;appboyBridge.logClick("1");<br>&nbsp;&nbsp;appboyBridge.closeMessage();<br>});<br>&lt;/script&gt;</code>|

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/
[2]: https://github.com/braze-inc/in-app-message-templates
