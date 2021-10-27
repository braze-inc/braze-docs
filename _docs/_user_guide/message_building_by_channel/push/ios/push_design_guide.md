---
nav_title: "Push Notification Design Guide (iOS 15+)"
article_title: iOS 15 Push Notification Design Guide
page_type: reference
page_order: 10
description: "This reference article covers guidelines and recommendations to consider while designing push messages for iOS 15+."
platform: iOS
channel:
  - push
tool:
  - Campaigns
---

# iOS 15 push notification design guide

> This reference article covers guidelines and recommendations to consider while designing push messages for iOS 15 and above.

While we can't provide a hard and fast rule for the precise number of characters to include in a push, we have some great guidelines and recommendations for you to consider while designing iOS messages. When in doubt, keep it short and sweet. Play it safe, targeting about 30–40 characters per line for both the message title and body.

## Notification states

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

{% tabs %}
{% tab Timing %}

### Timing

Depending on when a user engages with a push notification, the timestamp can shorten the title text.

![Example push notification with a timestamp of "now" and title character count of 35]({% image_buster/assets/img_archive/push_ios_timing_35.png %})
<br>Title character count: **35**

![Example push notification with a timestamp of "3h ago" and title character count of 33]({% image_buster/assets/img_archive/push_ios_timing_33.png %})
<br>Title character count: **33**

![Example push notification with a timestamp of "Yesterday, 8:37 AM" and title character count of 22]({% image_buster/assets/img_archive/push_ios_timing_22.png %})
<br>Title character count: **22**

{% endtab %}
{% tab Images %}

### Images

Body text is shortened by about 10 characters per line when an image is present.

![Example push notification with no image and a body character count of 179]({% image_buster/assets/img_archive/push_ios_images_179.png %})
<br>Body character count: **179**

![Example push notification with an image and a body character count of 154]({% image_buster/assets/img_archive/push_ios_images_154.png %})
<br>Body character count: **154**

{% endtab %}
{% tab Interruption level %}

### Interruption level

Time Sensitive and Critical denotations push the title down to a new line without the timestamp, giving it a little more space.

![Example push notification with no Time Sensitive or Critical denotation and a title character count of 35]({% image_buster/assets/img_archive/push_ios_interruption_level_35.png %})
<br>Title character count: **35**

![Example push notification with a Time Sensitive denotation and a title character count of 39]({% image_buster/assets/img_archive/push_ios_interruption_level_39.png %})
<br>Title character count: **39**

{% endtab %}
{% tab More %}

### And more

The following also impact text truncation:

- **Phone display settings:** a user can increase or decrease the global UI font size on their phone, typically for accessibility reasons.
- **Device width:** the message could be displayed on a small phone, or a wide iPad.
- **Content types:** emojis and wide characters like "m" and "w" take up more space than "i" or "t", and longer words like "engagement" may line-wrap more abruptly than shorter words.

{% endtab %}
{% endtabs %}

[1]: {% image_buster /assets/img_archive/push_ios_notification_states.png %}