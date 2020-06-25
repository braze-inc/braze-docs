---
nav_title: Beta
platform: Message_Building_and_Personalization
subplatform: In-App Messages
page_order: 9
hidden: true
desciption: "This reference article covers the new in-app messaging HTML Preview feature."
---

# In-App Messages HTML Preview Beta

Learn about the new Beta Version of custom HTML In-App Messages.

{% alert important %}
This feature is in *Beta*. Ask your Braze team for more information on how to get access.
{% endalert %}

## New Features

### Interactive Preview

The message preview screen now shows a more realistic preview that renders the JavaScript included in your message.

This means you can now preview _and interact_ with your custom messages (i.e. click through pagination, submit forms or surveys, watch JavaScript animations, etc.)

![New HTML In App Preview]({% image_buster /assets/img/iam-beta-javascript-preview.gif %})

{% alert tip %}
We'll ensure that any [`appboyBridge`]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#javascript-bridge) javascript methods you use in your HTML won't actually update user profiles _while previewing in the dashboard_.
{% endalert %}


### Cross-Channel HTML Messages

This new HTML message type now lets you create one message that can be sent to both mobile and web!

![New HTML In App Message Cross Channel]({% image_buster /assets/img/iam-beta-html-cross-channel.png %})

### Asset Management

Upload campaign assets to the Media Library directly from your campaign using a simple drag-and-drop interface.

This new workflow makes it easy to upload a file, copy its URL, and paste directly into your HTML.

We've also added support for additional file types, including Fonts (.ttf, .woff, .otf, .woff2), SVG images (.svg), Javascript (.js), and CSS (.css) files.

Uploading files to campaigns will ensure they are cached on mobile devices in case your message is shown while a user has a poor internet connection.

### Syntax Highlighting

The code editor now includes Syntax Highlighting with a number of different color themes to choose from.

This helps to easily spot potential code errors directly in the message composer, and better organize your code (using spaces or tabs - whichever side of that argument you're on).

![New HTML In App Message Syntax Highlighting]({% image_buster /assets/img/iam-beta-html-syntax-highlighting.png %})

### Button Tracking Improvements

We've introduced a new [`appboyBridge`][1] JavaScript method (`appboyBridge.logClick(id_string)`) to programatically track button clicks, for scenarios where users are not clicking links, or for tracking buttons after making some API request within a campaign. See our JavaScript [documentation]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#javascript-bridge) for more details.

Additionally, HTML In-App Messages are no longer limited to recording one button click even per impression.

## Migration Guide

There are two steps required to migrate to the new HTML Beta

### SDK Requirements {#supported-sdk-versions}

These Beta features require upgrading to the following Braze SDK version:

* Web SDK v2.5+ [Changelog]({{site.baseurl}}/developer_guide/platform_integration_guides/web/changelog/#250)
* iOS SDK - v3.23.0+ [Changelog]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/#3230)
* Android SDK - v8.0.0+ [Changelog]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog/#800)

{% alert warning %}
Because this new message type has SDK version depdendencies, be sure to use the new option when enough of your user base has upgraded. Users on older SDK versions will not be served the message.

Did you know you can create segments to target greater-than or less-than certain app versions? [Learn More]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions)
{% endalert %}

### New Message Type {#new-message-type}

When creating a "Custom Code" message, choose the new "HTML Upload with Preview" option as shown below:

![New HTML In App Message Beta Dropdown]({% image_buster /assets/img/iam-beta-html-dropdown.png %})

Keep in mind that your mobile app users need to upgrade to the supported SDK versions in order to receive this message. 

We recommend that you [nudge users to upgrade]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/) their mobile apps before launching campaigns that depend on newer Braze SDK versions. 

### Uploading Asset Files {#upload-assets}

Uploading assets to a custom HTML message is optional, although it's recommended if there's a chance your user is offline or has a poor connection when displaying the message.

There are three ways you can upload assets to a campaign:

1. Drag-and-drop one or more assets into the Campaign Assets section, or
2. Click the upload area to choose files from your computer, or
3. Use the Media Library button to choose assets you've already uploaded to our Media Library

Once your assets are added to a campaign, you can use the Copy Link button to get the asset's location on Braze's CDN.

Then, paste the copied asset URL into your HTML as you normally would.

![New HTML In App Message Asset Uploader]({% image_buster /assets/img/iam-beta-html-asset-uploader.png %})

## Providing Feedback

Feedback is encouraged and welcome! 

Please send any feedback or suggestions through to your Braze Customer Success Team.

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#javascript-bridge
