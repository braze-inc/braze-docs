---
nav_title: "Push Action Buttons"
article_title: Push Action Buttons
page_order: 1
page_type: reference
description: "This reference article covers what push action buttons are and the difference across iOS and Android platforms."
channel:
  - Push

---

# Push action buttons

![Push Action Buttons][1]{: style="float:right;max-width:40%;margin-left:15px;"}

> This reference article covers what push action buttons are and the difference across iOS and Android platforms. 

Push action buttons enable you to set content and actions for buttons when utilizing Braze's iOS and Android push notifications. With action buttons, your users can interact directly with your app from a notification without needing to click into an app experience to take action.

## How to use action buttons

Each interactive button can link to a webpage, a deep link, open the app, or dismiss the notification. You can specify your push action buttons in the **On Click Behavior** section of the push message composer in the dashboard.

### iOS push action buttons {#ios}

To use action buttons in your iOS push messages, create a [push campaign]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/) and enable action buttons in the **Compose** tab.

![Enable push action buttons]({% image_buster /assets/img_archive/push_action_enable.png %}){: style="max-width:60%"}

Then select your **Notification Category**. You can select from the following available button combinations:

- Accept / Decline
- Yes / No
- Confirm / Cancel
- More
- Pre-registered Custom Category

![iOS Push Action Buttons]({% image_buster /assets/img_archive/push_action_buttons_ios.png %}){: style="max-width:70%"}

>  Due to iOS’s handling of buttons, you will need to perform additional integration steps when setting up push action buttons, which are outlined in our [developer documentation]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/action_buttons/). In particular, you will need to either configure iOS Categories or will need to select from certain default button options. For Android integrations, these buttons will work out of the box.

### Android push action buttons {#android}

To use action buttons in your Android push messages, create a [push campaign]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/) and enable notification buttons in the **Compose** tab.

![Enable push action buttons]({% image_buster /assets/img_archive/push_action_enable2.png %}){: style="max-width:60%"}

Then click <i class="fas fa-plus-circle"></i> **Add Button** and specify your button text and **On-Click Behavior**. You can select from the following available actions:

- Open App
- Redirect to Web URL
- [Deep Link]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) into Application
- Dismiss Notification

You can add up to three buttons in your push.

![Android Push Action Buttons]({% image_buster /assets/img_archive/push_action_buttons_android.png %}){: style="max-width:70%"}

#### Character limits

Unlike iOS buttons, which are stacked, Android buttons are displayed side-by-side in a row. This means that the more buttons you add (up to three), the less space you have for your button copy. 

![Android push action buttons with truncated text]({% image_buster /assets/img_archive/push_action_truncated.png %}){: style="max-width:50%" }

The following table outlines how many characters you can add before your button copy is truncated, depending on how many buttons you have:

| Number of Buttons | Max characters per button |
| --- | --- |
| 1 | 46 characters |
| 2 | 20 characters |
| 3 | 11 characters |
{: .reset-td-br-1 .reset-td-br-2}


[1]: {% image_buster /assets/img_archive/push_action_example.png %}
[2]: {% image_buster /assets/img_archive/push_action_enable.png %}

