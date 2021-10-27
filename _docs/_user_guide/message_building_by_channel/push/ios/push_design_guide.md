---
nav_title: "Push Notification Design Guide"
article_title: iOS 15 Push Notification Design Guide
page_type: reference
page_order: 10
description: "This reference article covers guidelines and recommendations to consider while designing iOS messages."
platform: iOS
channel:
  - push
tool:
  - Campaigns
---

# iOS push notification design guide

While we can't provide a hard and fast rule for the precise number of characters to include in a push, we have some great guidelines and recommendations for you to consider while designing iOS messages. When in doubt, keep it short and sweet. Play it safe, targeting about 30–40 characters for both the message title and body.

## Overview of notification states

Your users may view push notifications in a variety of different situations, and could see different lengths of text as follows.

<table>
<thead>
  <tr>
    <th>Lock screen or Notification Center</th>
    <th>Expanded</th>
    <th>Device active</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td width="33%">This is the most common scenario.<br><br><b>Title:</b> 1 line of text<br><b>Body:</b> 4 lines of text<br><b>Image:</b> square thumbnail</td>
    <td width="33%">When a user long-presses a message.<br><br><b>Title:</b> 1 line of text<br><b>Body:</b> 7 lines of text<br><b>Image:</b> 2:1 aspect ratio (recommended, see note below)</td>
    <td width="33%">When a user receives a push while their phone is unlocked and active.<br><br><b>Title:</b> 1 line of text<br><b>Body:</b> 2 lines of text</td>
  </tr>
</tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

![alt text][1]

{% alert note %}
While we recommend a 2:1 aspect ratio for expanded push notifications, nearly any aspect ratio is supported. Images will always span the full width of the notification, and the height will adjust accordingly.
{% endalert %}

## Variables in text truncation

When creating content, consider the following scenarios that may impact how much text is displayed.

### Timing

Depending on when a user engages with a push notification, the timestamp can shorten the title text.

### Images

Body text is shortened by about 10 characters per line when an image is present.

### Interruption level

Time Sensitive and Critical denotations push the title down to a new line without the timestamp, giving it a little more space.

### And more

The following also impact text truncation:

- **Phone display settings:** a user can increase or decrease the global UI font size on their phone, typically for accessibility reasons.
- **Device width:** the message could be displayed on a small phone, or a wide iPad.
- **Content types:** emojis and wide characters like "m" and "w" take up more space than "i" or "t", and longer words like "engagement" may line-wrap more abruptly than shorter words.

[1]: {% image_buster /assets/img_archive/push_ios_notification_states.png %}
[2]: {% image_buster /assets/img_archive/push_ios_lockscreen.png %}