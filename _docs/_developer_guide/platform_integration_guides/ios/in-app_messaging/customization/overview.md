---
nav_title: Overview
article_title: In-App Message Customization Overview for iOS
platform: iOS
page_order: 1
description: "This reference article covers in-app messaging customization options for your iOS application."
channel:
  - in-app messages

---

# Customization overview {#in-app-message-customization}

Braze's in-app message types are highly customizable across messages, images, [Font Awesome][26] icons, click actions, analytics, editable styling, custom display options, and custom delivery options. Multiple options can be configured on a per in-app message basis from within the [dashboard][13]. Braze additionally provides multiple levels of advanced customization to satisfy a variety of use cases and needs.

{% alert important %}
By default, in-app messages are enabled after completing the standard SDK integration, including GIF support.
<br><br>
**Note that integration of `SDWebImage` is required if you plan on using our Braze UI for displaying images** within iOS in-app messages, News Feed, or Content Cards.
{% endalert %}

## Key-value pair extras

`ABKInAppMessage` objects may carry key-value pairs as `extras`. These are specified on the dashboard when creating a campaign. Key-value pairs can be used to send data down with an in-app message for further handling by your app.

[13]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#creating-an-in-app-message
[26]: http://fortawesome.github.io/Font-Awesome/
