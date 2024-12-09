---
nav_title: "Onboarding Flow"
article_title: Onboarding Flow
alias: "/onboarding_flow"
page_order: 0
description: "This reference article covers how to welcome new users, guide them through benefits, and drive action using a compelling call to action."
---

# Onboarding flow

> Use the **Onboarding flow** in-app message template to collect user attributes, insights, and preferences that power your campaign strategy. 

## SDK requirements

### Minimum SDK versions

Messages created using the drag-and-drop editor can only be sent to users on the following minimum SDK versions. See the [Prerequisites][1] section of [Creating an in-app message with drag-and-drop]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/) for more details and nuances to be aware of.

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

### SDK versions for text links

If you want to include text links that do not dismiss the message, users must be on the following minimum SDK versions:

{% sdk_min_versions swift:6.2.0 android:26.0.0 %}

{% alert warning %}
If you include a link in your in-app message that redirects to a URL and the end user is not on the minimum SDK versions specified, clicking on the link will close the message and the user will not be able to return to the message to submit the form.
{% endalert %}

## Creating an onboarding flow

When creating a drag-and-drop in-app message, select **Onboarding flow** for your template and select **Build message**. This template is supported for both mobile apps and web browsers.

![The in-app message editor with the onboarding flow template.][img1]

### Step 1: Set up your message styles

Before you start customizing your template, you can set message-level styles for the entire message using the side menu. For example, you may want to customize the font of all the text or the color of all the links included in your message. You can also make the message a modal or fullscreen display type.

### Step 2: Customize your onboarding flow

To get started building your onboarding flow, use the **Pages** section to add or delete messages to your flow. After you have your desired number of messages, select the buttons on each page. Then, use the side menu to select where users go when they select the button—whether they exit the flow or go to the next message.

### Step 3: Style your message

You can customize the look and feel of your message using the drag-and-drop [in-app message components][3].

## Reporting

After your campaign has launched, you can analyze results in real time to see how many users have engaged with your campaign. To see how many users have opted in to the subscription group, you can [create a segment][5] of users who subscribed to the subscription group by filtering for users who have received the in-app message and submitted the form.

[img1]: {% image_buster /assets/img/templates/onboarding_editor.png %}

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#prerequisites
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components
[5]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/