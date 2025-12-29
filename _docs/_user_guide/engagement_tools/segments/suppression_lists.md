---
nav_title: Suppression lists
article_title: Suppression Lists
page_order: 3
page_type: reference
tool: Segments
description: "This page covers how to use suppression lists to specify which users should never receive your messages."

---

# Suppression lists

> Suppression lists are groups of users who automatically do not receive any campaigns or Canvases. Suppression lists are defined by segment filters, and users will enter and exit suppression lists as they meet filter criteria. You can also set exception tags so that the suppression list won’t apply to campaigns or Canvases with those tags. Messages from campaigns or Canvases with exception tags will still reach suppression list users who are in the target segments.

## Why use suppression lists?

Suppression lists are dynamic and automatically apply to all forms of messaging, but you can set exceptions for selected tags. If your selected exception tags are used in a campaign or Canvas, then that suppression list won't apply to that campaign or Canvas. Messages from campaigns or Canvases with exception tags will still reach any suppression list users that are part of your target segments.

### Message types and channels affected by suppression lists

Suppression lists will apply to all message types and channels except for [feature flags]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/). This means that suppression lists by default apply to all channels, campaigns, and Canvases, including:
- [API campaigns]({{site.baseurl}}/api/api_campaigns/)
- API-triggered campaigns and Canvases
- [Transactional emails]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign/)

The only message type that suppression lists do not apply to is feature flags. Users in a suppression list won't be suppressed from feature flags, but will be suppressed from all other channels. 

You can use exception tags so that suppression list users are still targeted by particular campaigns and Canvases. For details, refer to step 4 in [Setting up suppression lists](#setup). If you do not add exception tags to a suppression list, then users in that suppression list will not be targeted with any messaging besides feature flags. 

{% alert note %}
Suppression lists are applied to API campaigns that are created in the Braze dashboard with a `campaign_id`. Suppression lists don't apply to messages sent through [Braze messaging endpoints]({{site.baseurl}}/api/endpoints/messaging/) without an associated `campaign_id`. 
{% endalert %}

![The "Exception Settings" section with a checkbox to not apply the suppression list to API-triggered campaigns and Canvases.]({% image_buster /assets/img/suppression_list_checkbox.png %}){: style="max-width:70%;"}

## Setting up suppression lists {#setup}

{% alert note %}
All users can view suppression lists, but only users with [admin permissions]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?tab=admin#list-of-permissions) can create and manage suppression lists.
{% endalert %}

1. Go to **Audience** > **Suppression Lists**.<br><br>![The "Suppression Lists" page with a list of three suppression lists.]({% image_buster /assets/img/suppression_lists_home.png %})<br><br>
2. Select **Create Suppression List** and add a name.<br><br>![A window called "Create a Suppression List" with a field to enter a name.]({% image_buster /assets/img/create_suppression_list.png %}){: style="max-width:80%;"}<br><br>
3. Use segment filters to identify the users in your suppression lists. You must select at least one.

{% alert important %}
Though the setup process seems similar to [segment creation]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), a suppression list is a group of users that you **do not** want to send messages to regardless of segment membership.
{% endalert %}

![A suppression list builder with a filter for users who last opened an email more than 90 days ago.]({% image_buster /assets/img/suppression_list_filters.png %})

{: start="4"}
4. Determine whether to have exceptions based on tag by checking the box beneath your segment name (refer to [Why use suppression lists?](#why-use-suppression-lists) for more information), then add the tags of campaigns or Canvases that users in this suppression list should still receive. <br><br>In other words, if you add the exception tag “Shipping confirmation”, users in your suppression list will be excluded from all messaging except those that use the tag “Shipping confirmation".<br><br>![The "Shipping List Details" section with an exception tag applied called "Shipping confirmation".]({% image_buster /assets/img/exception_tags.png %})<br><br>
5. Save or activate your suppression list.
- When you save, your suppression list will be saved but won't be activated, which means it won't go into effect. Your suppression list will remain inactive until you activate it, and inactive suppression lists won't impact messaging (users won't be excluded from messages).
- When you activate, your suppression list will be saved and immediately go into effect, which means users in your suppression list will immediately be excluded from campaigns or Canvases (except for ones containing an exception tag).

{% alert note %}
Only admins can save or activate suppression lists. You can have up to five active suppression lists at a time in the beta.
{% endalert %}

You can deactivate or archive suppression lists when you no longer need them. 
- To deactivate, select an active suppression list and select **Deactivate**. Deactivated suppression lists can be reactivated later.
- To archive, do so from the **Suppression Lists** page.

## Suppression list usage

To check if your suppression list prevented a user from receiving a message, use **User Lookup** in the **Target Audience** step within your campaign or Canvas. Here, you'll be able to see which suppression list they're part of.

!["User Lookup" window showing that a user is in a suppression list.]({% image_buster /assets/img/suppression_list_user_lookup.png %}){: style="max-width:70%;"}

{% alert tip %}
You can also find applied suppression lists in the **Summary** step.
{% endalert %}

While creating a campaign or Canvas, use **User Lookup** within the **Target Audience** step to search for a user, and if they aren't in the target audience, you can see the suppression list they're part of. 

!["User Lookup" window showing that a user is in a suppression list.]({% image_buster /assets/img/suppression_list_user_lookup.png %}){: style="max-width:70%;"}

### Campaign 

If a user is in a suppression list, they won't receive a campaign for which that suppression list applies. Refer to [Message types and channels affected by suppression lists](#message-types-and-channels-affected-by-suppression-lists) for cases when a suppression list won't apply.

![The "Suppression Lists" section with one active suppression list, called "Low marketing health scores".]({% image_buster /assets/img/active_suppression_list.png %})

### Canvas 

From the moment a user is added to a suppression list, they will not enter Canvases. If they have already entered a Canvas, they won't receive Message steps. This means that if a user is already inside a Canvas when they are added to a suppression list, they will advance through the Canvas until the next Message step, at which point they will exit without receiving the Message step. 

For example, let's say a Canvas has a User Update step followed by a Message step. If a user enters the Canvas and then is added to a suppression list, that user will still proceed through the User Update step (where they may be updated), and then exit at the Message step, at which point they will be included in the exited metrics.
