---
nav_title: HTML Preview
platform: Message_Building_and_Personalization
subplatform: In-App Messages
page_order: 9
hidden: true
description: "This reference article covers the new in-app messaging HTML Preview feature."
---

# In-App Messages HTML Preview Early Access

Learn about the new Early Access version of custom HTML In-App Messages.

{% alert important %}
This feature is in *Early Access*. Ask your Braze account team to get access!
{% endalert %}

## New Features

### Interactive Preview

The message preview screen now shows a more realistic preview that renders the JavaScript included in your message.

This means you can now preview _and interact_ with your custom messages (i.e. click-through pagination, submit forms or surveys, watch JavaScript animations, etc.)

![New HTML In App Preview]({% image_buster /assets/img/iam-beta-javascript-preview.gif %})

{% alert tip %}
We'll ensure that any [`appboyBridge`]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#javascript-bridge) javascript methods you use in your HTML won't actually update user profiles _while previewing in the dashboard_.
{% endalert %}


### Cross-Channel HTML Messages

This new HTML message type now lets you create one message that can be sent to both mobile and web!

![New HTML In App Message Cross Channel]({% image_buster /assets/img/iam-beta-html-cross-channel.png %})

### New Asset Uploader

Upload campaign assets to the Braze Media Library using a simple drag-and-drop interface.

This new workflow makes it easy to upload files and copy/paste their URLs directly into your HTML.

We've also added the ability to upload newly supported file types, including:

| File Type | File Extension|
|:-------- |:------------|
| Font Files| `.ttf`, `.woff`, `.otf`, `.woff2`|
| SVG Images| `.svg`|
| Javascript Files| `.js`|
| CSS Files| `.css`|

{% alert tip %}
Using Braze's Media Library CDN to host assets will ensure your messages are displayed on mobile devices even if a user has a poor internet connection or offline.
{% endalert %}

### Syntax Highlighting

The code editor now includes Syntax Highlighting with a number of different color themes to choose from.

This helps to easily spot potential code errors directly in the message composer, and better organize your code (using spaces or tabs - whichever side of that argument you're on).

![New HTML In App Message Syntax Highlighting]({% image_buster /assets/img/iam-beta-html-syntax-highlighting.png %})

### Button Tracking Improvements

You can now track performance within your message using the new [`appboyBridge.logClick(button_id)`][1] JavaScript method. This allows you to programatically track  "Button 1", "Button 2", and "Body Clicks" using `appboyBridge.logClick("0")`, `appboyBridge.logClick("1")`, or `appboyBridge.logClick()`, respectively.

This method replaces the previous automatic click tracking methods (i.e. `?abButtonId=0`) which have been removed. Additionally, HTML In-App Messages are no longer limited to recording one button click event per impression.

For example, to close a message and log Button 2 click, you can use:

```
<a href="#" onclick="appboyBridge.logClick('1');appboyBridge.closeMessage()">✖</a>
```

You can also track new custom button names - up to 100 unique names per campaign, for example `appboyBridge.logClick("blue button")` or `appboyBridge.logClick("viewed carousel page 3")`.

{% alert important %}
Note: Custom button IDs is not enabled by default and must be enabled for your account by Braze.
{% endalert %}

#### Requirements

* Up to 100 unique Button IDs are allowed per campaign
* Each Button ID can not be longer than 255 characters
* Only alphanumeric, space, dash, and underscore characters are allowed.

**Note**: This method replaces the previous automatic click tracking methods (i.e. `?abButtonId=0`) which have been removed.

## Backward Incompatible Changes {#backward-incompatible-changes}

1. The most notable incompatible change with this new message type is the SDK requirements. Users whose App SDK does not meet the minimum [SDK version requirements](#supported-sdk-versions) will not be shown the message.
<br>

2. Zip files are no longer used to manage a message's assets. Instead, you should use our new [Asset Uploader](#upload-assets) and paste absolute asset URLs directly into your HTML - just like you would for an email campaign. See the [Migration Steps](#migration-guide) for more information on transitioning away from zip files.
<br>

3. The `appboy://close` deeplink which was previously supported on mobile apps has been removed in favor of the Javascript, `appboyBridge.closeMessage()`. This allows cross-platform HTML since the web does not support deep links.

4. Automatic click tracking, which used `?abButtonId=0` for button IDs, and "body click" tracking on close buttons have been removed. The code examples below show how to change your HTML to use our new Click Tracking javascript methods:

| Before | After |
|:-------- |:------------|
|<code>&lt;a href="appboy://close"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="appboyBridge.logClick();appboyBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
|<code>&lt;a href="appboy://close?abButtonId=0"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="appboyBridge.logClick('0');appboyBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
|<code>&lt;a href="app://deeplink?abButtonId=0">Track button 1&lt;/a&gt;</code>|<code>&lt;a href="app://deeplink" onclick="appboyBridge.logClick('0')"&gt;Track button 1&lt;/a&gt;</code>|
|<code>&lt;script&gt;<br>location.href = "appboy://close?abButtonId=1"<br>&lt;/script&gt;</code>|<code>&lt;script&gt;<br>window.addEventListener("ab.BridgeReady", function(){<br>&nbsp;&nbsp;appboyBridge.logClick("1");<br>&nbsp;&nbsp;appboyBridge.closeMessage();<br>});<br>&lt;/script&gt;</code>|

## Creating a New Campaign {#instructions}

### SDK Requirements {#supported-sdk-versions}

These new features require upgrading to the following Braze SDK version:

* Web SDK v2.5+ [Changelog]({{site.baseurl}}/developer_guide/platform_integration_guides/web/changelog/#250)
* iOS SDK - v3.23.0+ [Changelog]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/#3230)
* Android SDK - v8.0.0+ [Changelog]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog/#800)

{% alert warning %}
Because this message type can only be received by certain newer SDK versions, users that are on unsupported SDK versions will not receive the message. 


Consider adopting this new message type once a significant portion of your user base is reachable, or target only those users whose app version is _above_ the requirements. [Learn More]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions)
{% endalert %}

### New Message Type {#new-message-type}

When creating a "Custom Code" message, choose the new "HTML Upload with Preview" option as shown below:

![New HTML In App Message Early Access Dropdown]({% image_buster /assets/img/iam-beta-html-dropdown.gif %})

Keep in mind that your mobile app users need to upgrade to the supported SDK versions to receive this message. 

We recommend that you [nudge users to upgrade]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/) their mobile apps before launching campaigns that depend on newer Braze SDK versions. 

### Uploading Asset Files {#upload-assets}

Use Braze's Media Library to upload and host assets for your custom HTML messages.

We recommend uploading assets to Braze's Media Library for two reasons:

1. Assets added to a campaign via Media Library will allow your messages to be displayed even while the user is offline
2. Assets uploaded to Braze can be more easily reused across campaigns.

To add _new_ assets to your campaign, use the Drag-and-Drop section to upload a file _and_ add associate the file with this campaign.

You can also add _existing_ assets to your campaign that you've already uploaded to Braze's Media Library.

![New HTML In App Message Asset Uploader]({% image_buster /assets/img/iam-beta-html-asset-uploader.gif %})

Once your assets are added to a campaign, you can use the _Copy Link_ button to store the file's URL to your clipboard.

Then, paste the copied asset URL into your HTML as you normally would when referencing a remote asset.

{% alert tip %}
You can press `CTRL+F` or `CMD+F` within the HTML Editor to search within your code!
{% endalert %}

### Migrating Old "Zip File" Campaigns {#migration-guide}

Older campaigns that used zip-files are not supported in this new In-App Message composer.

If you want to migrate those older zip-file campaigns, follow these instructions:

1. Download the .zip asset file to your computer, and unzip the files
2. Upload all of your asset files into the new campaign. (Tip: you can select all files and drag-and-drop them in)
3. For each newly uploaded asset, copy its uploaded file URL and replace them in your HTML's older local asset references

For example, if your old HTML contains a reference that looks like this:

```html
<img src="/cat.png" />
```

Replace it with its respective uploaded asset URL, like this:

```html
<img src="https://cdn.braze.com/appboy/communication/assets/font_assets/files/5ee3869ae16e174f34fac566/original.png" />
```

## Providing Feedback

Feedback is encouraged and welcome! Email any questions or suggestions to our team at [in-app-message-preview-beta@braze.com](mailto:in-app-message-preview-beta@braze.com?subject=Feedback%20for%20Custom%20HTML%20In-App%20Message%20with%20Preview&body=Company%20Name:%20%0D%0ACampaign%20Link:%20%0D%0AFeedback:).

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#javascript-bridge
