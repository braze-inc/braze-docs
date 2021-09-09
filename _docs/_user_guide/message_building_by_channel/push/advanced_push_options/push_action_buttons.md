---
nav_title: "Push Action Buttons"
article_title: Push Action Buttons
page_order: 1
page_type: reference
description: "This reference article covers what Push Action buttons are and the difference across iOS and Android platforms."
channel:
  - Push

---

# Push Action Buttons

> Push Action Buttons enable you to set content and actions for buttons when utilizing Braze's iOS and Android push notifications. Your users will now be able to interact directly with your app from a notification without needing to click into an app experience to take action.

![Push Action Buttons][1]

## How To Use Action Buttons

Each interactive button can link to a webpage, a deep link, open the app, or dismiss the notification. You can specify your Push Action Buttons in the ‘On Click Behavior’ section of the push message composer in the Dashboard.

{% tabs %} 
{% tab iOS Push Action Buttons %}

### iOS Push Action Buttons
![iOS Push Action Buttons]({% image_buster /assets/img_archive/ios_push_action_buttons.png %})

>  Due to iOS’s handling of buttons, you will need to perform additional integration steps when setting up push action buttons, which are outlined in our Documentation. In particular, you will need to either configure iOS Categories or will need to select from certain default button options. For Android integrations, these buttons will work out of the box.

For instructions on Integrating iOS Push Action Button, check out our [documentation]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/action_buttons/).

{% endtab %} 
{% tab Android Push Action Buttons %}

### Android Push Action Buttons
![Android Push Action Buttons]({% image_buster /assets/img_archive/android_push_action_buttons.png %})

{% endtab %} 
{% endtabs %} 


[1]: {% image_buster /assets/img_archive/push_action_buttons.png %}

