---
nav_title: User retargeting
article_title: User Retargeting
page_order: 4
description: "This reference article covers how users can retarget their messages by users WhatsApp interactions."
page_type: reference
channel:
  - WhatsApp
---

# User retargeting 

> In addition to changing the user’s subscription state, Braze will also record interactions with the user profile for filtering and triggering messages.<br><br>These filters and triggers allow you to filter users that have received WhatsApp messages or received WhatsApp messages from a specific WhatsApp campaign or Canvas step.

## Retargeting options

{% alert note %}
When building audiences with user retargeting, you may wish to include or exclude certain users based on their preferences, and in order to comply with privacy laws, such as the “Do Not Sell or Share” right under the CCPA. Marketers should implement the relevant filters for users’ eligibility within their Canvas and/or Campaign entry criteria.
{% endalert %}

### Filter users by WhatsApp

Users can be filtered by when they last received a WhatsApp or if they have received a WhatsApp from a specific WhatsApp campaign. Filters can be set in the Target Users step of the campaign builder.

**Filter by last received WhatsApp**<br>
![Filter for last receiving a WhatsApp message on April 22, 2025.]({% image_buster /assets/img/whatsapp/whatsapp23.png %}){: style="max-width:75%"}

**Filter by received messages from WhatsApp campaign**<br>
Filters users who have received a message from a specific WhatsApp campaign. With this filter, you also have the option to filter off those that have not received messages from a WhatsApp campaign.<br>
![Filter for receiving a WhatsApp campaign.]({% image_buster /assets/img/whatsapp/whatsapp22.png %}){: style="max-width:75%"}

### Filter by engagement
Retarget users who have, or have not, read a WhatsApp campaign or Canvas step. 

**Retarget users who have opened/read a specific WhatsApp Campaign**
1. Create a segment using the **Clicked/Opened Campaign** filter.
2. Select **read WhatsApp message**.
3. Choose the desired campaign.<br>

![Filter for having read a WhatsApp message.]({% image_buster /assets/img/whatsapp/whatsapp21.png %}){: style="max-width:75%"}

**Retarget users who have opened/read a specific Canvas Step**
1. Create a segment using the **Clicked/Opened Step** filter.
2. Select **read WhatsApp message**.
3. Choose the desired Canvas and Canvas steps.<br>

![Filter for reading a WhatsApp step.]({% image_buster /assets/img/whatsapp/whatsapp20.png %}){: style="max-width:75%"}

**Filter by campaign or Canvas attribution**<br>
Filter for users who have opened/read to a specific WhatsApp campaign or Canvas component or tag.

![Filter for opening a specific WhatsApp message.]({% image_buster /assets/img/whatsapp/whatsapp19.png %}){: style="max-width:75%"}

