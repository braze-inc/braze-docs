---
nav_title: Beta
platform: Message_Building_and_Personalization
subplatform: In-App Messages
page_order: 9
hidden: true
---

# In-App Messages HTML Preview Beta

Learn about the new Beta Version of custom HTML In-App Messages.

## New Features

### Interactive Preview

The message preview screen now shows a more realistic preview that renders the Javascript included in your message.

This means you can now preview _and interact_ with your custom messages (i.e. click through pagination, submit forms or surveys, watch javascript animations, etc.)

![New HTML In App Preview]({% image_buster /assets/img/iam-beta-javascript-preview.gif %})

{% alert info %}
Any [`appboyBridge`]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/customize/#javascript-bridge) methods included in the HTML won't update user profiles while in the preview.
{% endalert %}

### Syntax Highlighting

The code editor now includes Syntax Highlighting with a number of different color themes to choose from.

This helps to easily spot potential code errors directly in the message composer, and better organize your code (using spaces or tabs - whichever side of that argument you're on).

![New HTML In App Message Syntax Highlighting]({% image_buster /assets/img/iam-beta-html-syntax-highlighting.png %})


## Migration Guide

There are two steps required to migrate to the new HTML Beta

### SDK Requirements {#supported-sdk-versions}

These Beta features are supported on Web only, and require upgrading to the following Braze SDK version:

* Web SDK v2.5+ [Changelog]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/changelog/#250)

<!-- * Android SDK v5.0+ [Changelog]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/changelog/#500) -->

### New Message Type

Toggle the new "Custom Message" type when creating your HTML campaign, as shown below:

![New HTML In App Message Beta Dropdown]({% image_buster /assets/img/iam-beta-html-dropdown.png %})

<!--
### Cross-Channel HTML Messages

This new HTML message type can now be used across both mobile and web!

As always, it's recommended to [nudge users to upgrade]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/) their mobile apps before launching campaigns that depend on newer Braze SDK versions.

![New HTML In App Message Cross Channel]({% image_buster /assets/img/iam-beta-html-cross-channel.png %})
-->
## Upcoming Features

The following features are planned and coming soon!

### Mobile App Support

* Adding support to preview custom HTML In-App Messages for Mobile Apps

* Send a custom HTML In-App Message to both mobile and web with the same campaign

### Asset Management

* Upload assets directly to the Media Library from within a campaign via simple drag-and-drop interface

* List assets associated with this campaign, and quickly copy their URLs to use within your HTML

* Support for uploading additional file types (Fonts, SVG Images, Javascript, CSS)

## Providing Feedback

Feedback is encouraged and welcome! 

Please send any feedback or suggestions through to your Braze Customer Success Team.