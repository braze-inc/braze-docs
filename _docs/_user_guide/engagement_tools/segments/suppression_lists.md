---
nav_title: Suppression Lists
article_title: Suppression Lists
page_order: 2.5
page_type: reference
tool: Segments
description: "This page covers how to use suppression lists to specify which users should never receive your messages."

---

# Suppression lists

> Suppression lists specify groups of users who will never receive messages. Admins can create suppression lists with segment filters to narrow down a user group the same way you would for segmentation.

{% alert important %}
Suppression lists are currently in beta. If you're interested in being part of this beta, reach out to your customer success manager. During the beta, functionality may change, and you can have up to five active suppression lists at a time, but let your customer success manager know if you need more. 
{% endalert %}

## How it works

Suppression lists automatically apply to certain forms of messaging, but you can set exceptions for selected tags. If your selected exception tags are used in a campaign or Canvas, then that suppression list won't apply to that campaign or Canvas. Messages from campaigns or Canvases with exception tags will still reach any suppression list users that are part of your target segments.

### Messages not affected by suppression lists

As part of the beta, suppression lists will not apply to the following message types (in other words, suppression list users **will still** receive messages that belong to the following):
- Feature Flags
- Transactional use cases
- API campaigns
- API-triggered campaigns
- API-triggered Canvases
- Campaigns triggered by the Braze API (`/messages` and `/send`)

You don't need to add an exception tag for any of these use cases, as suppression lists automatically won't apply to them. To exclude a group of users from a message within these use cases, you need to create a target segment that excludes these users.

{% alert important %}
During the beta, we collect customer feedback to help improve our product. Tell your customer success manager if you plan to apply suppression lists to transational use cases.
{% endalert %}

### Channels affected by suppression lists

Suppression lists will automatically apply to all of the following channels (unless the campaign or Canvas contains an exception tag): 
- SMS
- Email
- Push
- In-app messages
- Content Card
- Banner
- SMS/MMS
- Webhook
- WhatsApp
- LINE

## Setting up suppression lists

Because suppression lists can significantly impact the messages you send, only admins can edit, save, active, and deactivate suppression lists (all users can view suppression lists).

1. Go to **Audience** > **Suppression Lists**.<br><br>![The "Suppression Lists" page with a list of three suppression lists.][1]<br><br>
2. Select **Create Suppression List** and add a name.<br><br>![A window called "Create a Suppression List" with a field to enter a name.][2]{: style="max-width:80%;"}<br><br>
3. Use segment filters to identify the users in your suppression lists. 

{% alert important %}
Though the setup process seems similar to [segment creation]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), a suppression list is a group of users that you **do not** want to send messages to regardless of segment membership.
{% endalert %}

![A suppression list builder with a filter for users who last opened an email more than 90 days ago.][3]

{: start="4"}
4. Determine whether to have exceptions based on tag by checking the box beneath your segment name (refer to [How it works](#how-it-works) for more information), then add the tags of campaigns or Canvases that users in this suppression list should still receive. <br><br>In other words, if you add the exception tag “Shipping confirmation”, users in your suppression list will be excluded from all messaging except those that use the tag “Shipping confirmation".<br><br>![The "Shipping List Details" section with an exception tag applied called "Shipping confirmation".][4]<br><br>
5. Save or activate your suppression list.
- When you save, your suppression list will be saved but won't be activated, which means it won't go into effect. Your suppression list will remain inactive until you activate it, and inactive suppression lists won't impact messaging (users won't excluded from messages).
- When you activate, your suppression list will be saved and immediately go into effect, which means users in your suppression list will immediately be excluded from campaigns or Canvases (except for ones containing an exception tag).

{% alert note %}
Only admins can save or activate suppression lists. You can have up to five active suppression lists at a time in the beta.
{% endalert %}

{: start="6"}
6. You can deactivate or archive suppression lists when you no longer need them. 
- To deactivate, select an active suppression list and select **Deactivate**. Deactivated suppression lists can be reactivated later.
- To archive, do so from the **Suppression Lists** page.

## Checking suppression list usage

### In a campaign

![The "Suppression Lists" section with one active suppression list, called "Low marketing health scores".][5]

Check the **Suppression List** section on the **Target Audience** page to view whether suppression lists are being applied to a campaign.

### In a Canvas

Check the **Suppression List** section on the **Target Audience** page to view whether suppression lists are being applied to a Canvas. You can also view applied suppression lists in the **Summary** step.

[1]: {% image_buster /assets/img/suppression_lists_home.png %}
[2]: {% image_buster /assets/img/create_suppression_list.png %}
[3]: {% image_buster /assets/img/suppression_list_filters.png %}
[4]: {% image_buster /assets/img/exception_tags.png %}
[5]: {% image_buster /assets/img/active_suppression_list.png %}
