---
nav_title: HTML Preview
article_title: HTML In-App Message Preview
page_order: 9
description: "This reference article covers custom code in-app messages using HTML upload with preview."
channel:
  - in-app messages

---

# In-app messages HTML Preview

When crafting [custom HTML in-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages), you can preview your interactive content directly in Braze. 

The message preview panel of the editor shows a realistic preview that renders the JavaScript included in your message. You can preview and interact with your custom messages from the preview panel by clicking through pagination, submitting forms or surveys, watching JavaScript animations, and more!

![Interacting with the HTML preview by swiping through pages.]({% image_buster /assets/img/iam-beta-javascript-preview.gif %})

{% alert tip %}
Any `appboyBridge` JavaScript methods you use in your HTML won't update user profiles while previewing in the dashboard.
{% endalert %}

## SDK requirements {#supported-sdk-versions}

To use the HTML preview for in-app messages, you must upgrade to the following minimum Braze SDK versions:

{% sdk_min_versions web:2.5.0 android:8.0.0 ios:3.23.0 %}

{% alert warning %}
Because this message type can only be received by certain later SDK versions, users that are on unsupported SDK versions will not receive the message. Consider adopting this message type after a significant portion of your user base is reachable, or target only those users whose app version is later than the requirements. Learn more about [filtering by most recent app version]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions).
{% endalert %}

## Creating a campaign {#instructions}

When creating a **Custom Code** in-app message, choose **HTML Upload with Preview** as the custom type. If you haven't previously created custom code in-app messages (live or drafts), this option is automatically applied and you won't need to make a selection.

![Creating an in-app message that sends to both Mobile and Web browsers where "Message Type" is Custom Code and "Custom Type" is HTML Upload with Preview.]({% image_buster /assets/img/iam-beta-html-cross-channel.png %})

Keep in mind that your mobile app users need to upgrade to the supported SDK versions to receive this message. We recommend that you [nudge users to upgrade]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/) their mobile apps before launching campaigns that depend on newer Braze SDK versions.

### Asset files

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

1. Assets added to a campaign via the Media Library allow your messages to be displayed even while the user is offline, or has poor internet connection.
2. Assets uploaded to Braze can be more easily reused across campaigns.

#### Adding asset files

You can add new or existing assets to your campaign.

{% tabs %}
{% tab Adding new assets %}
To add new assets to your campaign, use the drag-and-drop section to upload a file, then copy/paste their URLs or asset file names directly into your HTML to associate the file with this campaign.
{% endtab %}

{% tab Adding existing assets %}
To add assets that you've already uploaded to Braze's Media Library, select **Add from Media Library**.
{% endtab %}
{% endtabs %}

After your assets are added, they will appear in the **Assets for this campaign** section. Hover over an asset and select <i class="fas fa-copy"></i> **Copy** to copy the file's URL to your clipboard. Then paste the copied asset URL into your HTML as you normally would when referencing a remote asset.

Alternatively, you can use the asset file names directly in the HTML message.

### HTML editor

Changes you make in the HTML automatically render in the Preview panel as you type. Any `appboyBridge` JavaScript methods you use in your HTML won’t update user profiles while previewing in the dashboard.

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

## Backward incompatible changes {#backward-incompatible-changes}

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

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#javascript-bridge
