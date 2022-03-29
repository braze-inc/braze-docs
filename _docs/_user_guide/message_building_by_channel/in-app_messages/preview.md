---
nav_title: HTML Preview
article_title: HTML In-App Message Preview
page_order: 9
description: "This reference article covers the new in-app messaging HTML Preview feature."
channel:
  - in-app messages

---

# In-app messages HTML Preview

Learn about the new Preview features for custom HTML in-app messages.

{% sdk_min_versions web:2.5.0 android:8.0.0 ios:3.23.0 %}

## New features

### Interactive preview

The message preview screen shows a realistic preview that renders the JavaScript included in your message.

This means you can preview and interact with your custom messages (i.e., click-through pagination, submit forms or surveys, watch JavaScript animations, etc.)

![Interacting with the HTML preview by swiping through pages.]({% image_buster /assets/img/iam-beta-javascript-preview.gif %})

{% alert tip %}
We'll ensure that any [`appboyBridge`]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#javascript-bridge) javascript methods you use in your HTML won't actually update user profiles while previewing in the dashboard.
{% endalert %}

### Cross-channel HTML messages

This new HTML message type now lets you create one message that can be sent to both mobile and web!

![Creating an in-app message that sends to both Mobile and Web browsers where "Message Type" is Custom Code and "Custom Type" is HTML Upload with Preview.]({% image_buster /assets/img/iam-beta-html-cross-channel.png %})

### New asset uploader

Upload campaign assets to the Braze Media Library using a simple drag-and-drop interface. You can either upload files individually or via ZIP and copy/paste their URLs or asset file names directly into your HTML.

We've also added the ability to upload the following supported file types:

| File Type | File Extension|
|:-------- |:------------|
| Font Files| `.ttf`, `.woff`, `.otf`, `.woff2`|
| SVG Images| `.svg`|
| Javascript Files| `.js`|
| CSS Files| `.css`|
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
Using Braze's Media Library CDN to host assets will ensure your messages are displayed on mobile devices even if a user has a poor internet connection or offline.
{% endalert %}

### Syntax highlighting

The code editor now includes Syntax Highlighting with a number of different color themes to choose from.

This helps to easily spot potential code errors directly in the message composer, and better organize your code (using spaces or tabs - whichever side of that argument you're on).

![Syntax highlighting options in the "Editor Settings" dropdown when composing an HTML in-app message.]({% image_buster /assets/img/iam-beta-html-syntax-highlighting.png %})

### Button tracking improvements

You can now track performance within your message using the new [`appboyBridge.logClick(button_id)`][1] JavaScript method. This allows you to programatically track  "Button 1", "Button 2", and "Body Clicks" using `appboyBridge.logClick("0")`, `appboyBridge.logClick("1")`, or `appboyBridge.logClick()`, respectively.

This method replaces the previous automatic click tracking methods (i.e. `?abButtonId=0`) which have been removed. Additionally, HTML in-app messages are no longer limited to recording one button click event per impression.

For example, to close a message and log Button 2 click, you can use:

```
<a href="#" onclick="appboyBridge.logClick('1');appboyBridge.closeMessage()">✖</a>
```

You can also track new custom button names - up to 100 unique names per campaign, for example `appboyBridge.logClick("blue button")` or `appboyBridge.logClick("viewed carousel page 3")`.

#### Requirements

* Up to 100 unique button IDs are allowed per campaign.
* Each button ID can not be longer than 255 characters.
* Only alphanumeric, space, dash, and underscore characters are allowed.

**Note**: This method replaces the previous automatic click tracking methods (i.e. `?abButtonId=0`) which have been removed.

## Backward incompatible changes {#backward-incompatible-changes}

1. The most notable incompatible change with this new message type is the SDK requirements. Users whose App SDK does not meet the minimum [SDK version requirements](#supported-sdk-versions) will not be shown the message.
<br>

2. The `appboy://close` deeplink which was previously supported on mobile apps has been removed in favor of the Javascript, `appboyBridge.closeMessage()`. This allows cross-platform HTML since the web does not support deep links.

3. Automatic click tracking, which used `?abButtonId=0` for button IDs, and "body click" tracking on close buttons have been removed. The code examples below show how to change your HTML to use our new Click Tracking javascript methods:

| Before | After |
|:-------- |:------------|
|<code>&lt;a href="appboy://close"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="appboyBridge.logClick();appboyBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
|<code>&lt;a href="appboy://close?abButtonId=0"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="appboyBridge.logClick('0');appboyBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
|<code>&lt;a href="app://deeplink?abButtonId=0">Track button 1&lt;/a&gt;</code>|<code>&lt;a href="app://deeplink" onclick="appboyBridge.logClick('0')"&gt;Track button 1&lt;/a&gt;</code>|
|<code>&lt;script&gt;<br>location.href = "appboy://close?abButtonId=1"<br>&lt;/script&gt;</code>|<code>&lt;script&gt;<br>window.addEventListener("ab.BridgeReady", function(){<br>&nbsp;&nbsp;appboyBridge.logClick("1");<br>&nbsp;&nbsp;appboyBridge.closeMessage();<br>});<br>&lt;/script&gt;</code>|

## Creating a new campaign {#instructions}

### SDK requirements {#supported-sdk-versions}

These new features require upgrading to the following Braze SDK version:

{% sdk_min_versions web:2.5.0 android:8.0.0 ios:3.23.0 %}

{% alert warning %}
Because this message type can only be received by certain newer SDK versions, users that are on unsupported SDK versions will not receive the message. Consider adopting this new message type once a significant portion of your user base is reachable, or target only those users whose app version is above the requirements. Learn more about [filtering by most recent app version]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions).
{% endalert %}

### New message type {#new-message-type}

When creating a "Custom Code" message, choose the new "HTML Upload with Preview" option as shown below:

![Selecting HTML Upload with Preview for the "Custom Type" when creating a custom code in-app message.]({% image_buster /assets/img/iam-beta-html-dropdown.gif %})

Keep in mind that your mobile app users need to upgrade to the supported SDK versions to receive this message. 

We recommend that you [nudge users to upgrade]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/) their mobile apps before launching campaigns that depend on newer Braze SDK versions. 

### Uploading asset files {#upload-assets}

Use Braze's Media Library to upload and host assets for your custom HTML messages.

We recommend uploading assets to Braze's Media Library for two reasons:

1. Assets added to a campaign via Media Library will allow your messages to be displayed even while the user is offline
2. Assets uploaded to Braze can be more easily reused across campaigns.

To add _new_ assets to your campaign, use the Drag-and-Drop section to upload a file _and_ add associate the file with this campaign.

You can also add _existing_ assets to your campaign that you've already uploaded to Braze's Media Library by selecting **Add from Media Library**.

Once your assets are added to a campaign, you can use the _Copy Link_ button to store the file's URL to your clipboard. Then, paste the copied asset URL into your HTML as you normally would when referencing a remote asset.

Alternatively, you can use the asset file names directly in the HTML message.

{% alert tip %}
You can press `CTRL+F` or `CMD+F` within the HTML Editor to search within your code!
{% endalert %}


[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#javascript-bridge
