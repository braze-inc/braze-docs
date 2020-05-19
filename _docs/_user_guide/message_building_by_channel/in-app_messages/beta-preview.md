---
nav_title: Beta
platform: Message_Building_and_Personalization
subplatform: In-App Messages
page_order: 9
hidden: true
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

This new HTML message type can now be used across both mobile and web!

![New HTML In App Message Cross Channel]({% image_buster /assets/img/iam-beta-html-cross-channel.png %})

### Syntax Highlighting

The code editor now includes Syntax Highlighting with a number of different color themes to choose from.

This helps to easily spot potential code errors directly in the message composer, and better organize your code (using spaces or tabs - whichever side of that argument you're on).

![New HTML In App Message Syntax Highlighting]({% image_buster /assets/img/iam-beta-html-syntax-highlighting.png %})

### Button Tracking Improvements

We've introduced a new [`appboyBridge`][1] JavaScript method (`appboyBridge.logClick(button_id_string)`) to programatically track button clicks, for scenarios where users are not clicking links, or for tracking buttons after making some API request within a campaign. See our JavaScript [documentation](https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.logClick) for more details.

Additionally, HTML In-App Messages are no longer limited to recording one button click even per impression.

## Migration Guide

There are two steps required to migrate to the new HTML Beta

### SDK Requirements {#supported-sdk-versions}

These Beta features are currently supported on *Web only* and require upgrading to the following Braze SDK version:

* Web SDK v2.5+ [Changelog]({{site.baseurl}}/developer_guide/platform_integration_guides/web/changelog/#250)
* iOS SDK - v3.23.0+ [Changelog]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/#3230)
* Android SDK - v8.0.0+ [Changelog]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog/#800)

{% alert warning %}
Because this new message type has SDK version depdendencies, be sure to use the new option when enough of your user base has upgraded. Users on older SDK versions will not be served the message.
{% endalert %}

### New Message Type

Toggle the new "Custom Message" type when creating your HTML campaign, as shown below:

![New HTML In App Message Beta Dropdown]({% image_buster /assets/img/iam-beta-html-dropdown.png %})

Keep in mind that your mobile app users need to upgrade to the supported SDK versions in order to receive this message. 

We recommend that you [nudge users to upgrade]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/) their mobile apps before launching campaigns that depend on newer Braze SDK versions. 

## Upcoming Features

The following features are planned and coming soon!

### Asset Management

* Upload assets directly to the Media Library from within a campaign via simple drag-and-drop interface

* List assets associated with this campaign, and quickly copy their URLs to use within your HTML

* Support for uploading additional file types (Fonts, SVG Images, JavaScript, CSS)

## Providing Feedback

Feedback is encouraged and welcome! 

Please send any feedback or suggestions through to your Braze Customer Success Team.

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#javascript-bridge
