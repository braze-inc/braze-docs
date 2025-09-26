---
nav_title: "Push action buttons"
article_title: Push Action Buttons
page_order: 1
page_type: reference
description: "This reference article covers what push action buttons are and the difference across iOS and Android platforms."
channel:
  - Push

---

# Push action buttons

![An iOS push notification with two push action buttons: Accept and Decline.]({% image_buster /assets/img_archive/push_action_example.png %}){: style="float:right;max-width:40%;margin-left:15px;border:none;"}

> Push action buttons allow you to set content and actions for buttons when using Braze iOS and Android push notifications. With action buttons, your users can interact directly with your app from a notification without needing to click into an app experience.

## Creating action buttons

Each interactive button can link to a web page or a deep link or open the app. 

- For standard push campaigns, you can specify your push action buttons in the **On-Click Behavior** section of the push message composer in the dashboard.
- For [quick push campaigns]({{site.baseurl}}/quick_push), action buttons can be configured separately for each platform under the **Settings** tab.

{% tabs %}
{% tab iOS %}
### iOS {#ios}

To use action buttons in your iOS push messages, do the following:

1. Turn on action buttons in the **Compose** tab for a standard campaign or in the **Settings** tab for quick push.
2. Select your **iOS Notification Category** from the following available button combinations:
 - Accept / Decline
 - Yes / No
 - Confirm / Cancel
 - More
 - Pre-registered custom iOS Category

![iOS Notification Category dropdown menu.]({% image_buster /assets/img_archive/push_action_buttons_ios.png %}){: style="max-width:70%"}

{% alert note %}
Due to iOS's handling of buttons, you need to perform additional integration steps when setting up push action buttons, which are outlined in our [developer documentation]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_customizing-push-categories). In particular, you need to either configure iOS Categories or select from certain default button options. For Android integrations, these buttons will work automatically.
{% endalert %}
{% endtab %}
{% tab Android %}
### Android {#android}

To use action buttons in your Android push messages, do the following:

1. Turn on action buttons in the **Compose** tab for a standard campaign or in the **Settings** tab for quick push.
2. Select <i class="fas fa-plus-circle"></i> **Add Button** and specify your button text and **On-Click Behavior**. You can select from the following available actions:
  - Open App
  - Redirect to Web URL
  - [Deep Link]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) Into Application

![Selecting "Open App" as the on-click behavior for a notification button.]({% image_buster /assets/img_archive/push_action_buttons_android.png %}){: style="max-width:70%"}

You can add up to three buttons in your push.

#### Android character limits

Unlike iOS buttons, which are stacked, Android buttons are displayed side-by-side in a row. This means that the more buttons you add (up to three), the less space you have for button copy. 

![Android push action buttons with truncated text.]({% image_buster /assets/img_archive/push_action_truncated.png %}){: style="max-width:50%"}

The following table outlines how many characters you can add before your button copy is truncated, depending on how many buttons you have:

| Number of Buttons | Maximum characters per button |
| --- | --- |
| 1 | 46 characters |
| 2 | 20 characters |
| 3 | 11 characters |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

