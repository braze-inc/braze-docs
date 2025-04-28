---
nav_title: Suppression Lists
article_title: Suppression Lists
page_order: 2.5
page_type: reference
tool: Segments
description: "This page covers how to use suppression lists to specify which users should never receive your messages."

---

# Suppression lists

> Suppression lists specify groups of users who will never receive messages. Admins can create dynamic suppression lists with segment filters to narrow down a user group the same way you would for segmentation.

{% alert important %}
Suppression lists are currently in beta. If you're interested in being part of this beta, reach out to your customer success manager. During the beta, functionality may change, and you can have up to five active suppression lists at a time, but let your customer success manager know if you need more. 
{% endalert %}

## Why use suppression lists?

Suppression lists are dynamic and automatically apply to certain forms of messaging, but you can set exceptions for selected tags. If your selected exception tags are used in a campaign or Canvas, then that suppression list won't apply to that campaign or Canvas. Messages from campaigns or Canvases with exception tags will still reach any suppression list users that are part of your target segments.

### Messages not affected by suppression lists

As part of the beta, suppression lists will not apply to the following message types (in other words, suppression list users **will still** receive messages that belong to the following):
- [Feature Flags]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/)
- [Transactional emails]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign/)
- [API campaigns]({{site.baseurl}}/api/api_campaigns/)

You don't need to add an exception tag for any of these use cases, as suppression lists automatically won't apply to them. To exclude a group of users from a message within these use cases, you need to create a target segment that excludes these users.

{% alert important %}
During the beta, we collect customer feedback to help improve our product. Tell your customer success manager if you plan to apply suppression lists to transactional emails.
{% endalert %}

### Channels affected by suppression lists

Suppression lists are dynamic and will automatically apply to all of the following channels (unless the campaign or Canvas contains an exception tag): 
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

By default, suppression lists will apply to any API-triggered campaigns and API-triggered Canvases. You can change this by checking **Do not apply this suppression list to all API-triggered campaigns and API-triggered Canvases** in the **Exception Settings** section.

![The "Exception Settings" section with a checkbox to not apply the suppression list to API-triggered campaigns and Canvases.][6]{: style="max-width:70%;"}

## Setting up suppression lists

Because suppression lists can significantly impact the messages you send, only admins can edit, save, active, and deactivate suppression lists (all users can view suppression lists).

1. Go to **Audience** > **Suppression Lists**.<br><br>![The "Suppression Lists" page with a list of three suppression lists.][1]<br><br>
2. Select **Create Suppression List** and add a name.<br><br>![A window called "Create a Suppression List" with a field to enter a name.][2]{: style="max-width:80%;"}<br><br>
3. Use segment filters to identify the users in your suppression lists. You must select at least one.

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

You can deactivate or archive suppression lists when you no longer need them. 
- To deactivate, select an active suppression list and select **Deactivate**. Deactivated suppression lists can be reactivated later.
- To archive, do so from the **Suppression Lists** page.

## Suppression list usage

To check if your suppression list prevented a user from receiving a message, use **User Lookup** in the **Target Audience** step within your campaign or Canvas. Here, you'll be able to see which suppression list they're part of.

!["User Lookup" window showing that a user is in a suppression list.][7]{: style="max-width:70%;"}

{% alert tip %}
You can also find applied suppression lists in the **Summary** step.
{% endalert %}

While creating a campaign or Canvas, use **User Lookup** within the **Target Audience** step to search for a user, and if they aren't in the target audience, you can see the suppression list they're part of. 

!["User Lookup" window showing that a user is in a suppression list.][7]{: style="max-width:70%;"}

{% tabs local %}
{% tab campaign %}
If a user is in a suppression list, they won't receive a campaign for which that suppression list applies. Refer to [Messages not affected by suppression lists](#messages-not-affected-by-suppression-lists) for cases when a suppression list won't apply.

![The "Suppression Lists" section with one active suppression list, called "Low marketing health scores".]({% image_buster /assets/img/active_suppression_list.png %})
{% endtab %}
{% tab canvas %}
If a user is in a suppression list, they will still enter the Canvas but won't be able to receive Message steps within the Canvas. When they advance to a Message step, they will be exited from the Canvas. However, a user in a suppression list is still able to receive non-Message steps prior to a Message step. 

#### Preventing segments from entering a Canvas

For a segment to not be entered into a Canvas **at all**, you can configure that Canvas' Target settings to exclude that segment by following these steps:

1. Build a segment using the same filters and criteria as your suppression list.
2. In the **Target** step, use the **Segment Membership** filter to target users who aren't included in your segment.

For example, let’s say you have a Canvas with an applied suppression list. The Canvas has a User Update step followed by a Message step. In this scenario, suppression list users will enter the Canvas, proceed through the User Update step (where the user may be updated, based on how that step is configured), and then exit at the Message step (at which point the user will be included in the “Exited” metrics). 
{% endtab %}
{% endtabs %}

[1]: {% image_buster /assets/img/suppression_lists_home.png %}
[2]: {% image_buster /assets/img/create_suppression_list.png %}
[3]: {% image_buster /assets/img/suppression_list_filters.png %}
[4]: {% image_buster /assets/img/exception_tags.png %}
[6]: {% image_buster /assets/img/suppression_list_checkbox.png %}
[7]: {% image_buster /assets/img/suppression_list_user_lookup.png %}