---
nav_title: Soft Push Prompt
article_title: Soft Push Prompt for Web
platform: Web
page_order: 19
page_type: reference
description: "This article covers how to create a soft push prompt for your web application"
channel: push

---

# Soft push prompt

{% alert tip %}
Braze now supports push registration in-app messages out-of-the-box with no coding required! To learn more visit our [Push primer guide]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/).
{% endalert %}

It's often a good idea for sites to implement a "soft" push prompt where you "prime" the user and make your case for sending them push notifications before requesting push permission. This is useful because the browser throttles how often you may prompt the user directly, and if the user denies permission, you can never ask them again. 

This can be done simply through Braze's [triggered in-app messages]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#trigger-types) for a seamless user experience. Instead of calling `requestPushPermission()` directly as described in the standard [Web push integration]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/#step-2-browser-registration), instead.

{% include archive/web-v4-rename.md %}

## Step 1: Create a push primer campaign

First, you must create a "Prime for Push" in-app messaging campaign in the Braze dashboard:

1. Create a **Modal** in-app message and give it whatever text and styling you would like. 
2. Next, set the on-click behavior to **Close Message**. This behavior will be customized later.
3. Add a key-value pair to the message where the key is `msg-id`, and the value is `push-primer`.
4. Assign a custom event trigger action "prime-for-push" to the message. You can create the custom event manually from the dashboard if needed.

## Step 2: Remove calls

In your Braze SDK integration, find and remove any calls to `automaticallyShowInAppMessages()` from within your loading snippet.

## Step 3: Update integration

Finally, replace the removed call with the following snippet:

```javascript

// Be sure to remove calls to automaticallyShowInAppMessages() 
// from your code as noted in the steps above

braze.subscribeToInAppMessage(function(inAppMessage) {
  if (inAppMessage instanceof braze.InAppMessage) {
    // checks the key-value pair for a "msg-id" key
    const keyValuePairs = inAppMessage.extras || {};

    // If this is our push primer message
    if (keyValuePairs["msg-id"] === "push-primer") {
      if (!braze.isPushSupported() || braze.isPushPermissionGranted() || braze.isPushBlocked()) {
        // do not show the message because user/browser is not eligible
        return;
      }

      // the browser is eligible to request push permission
      // register a callback when the left-button is clicked
      if (inAppMessage.buttons[0] != null) {
        // Prompt the user when the first button is clicked
        inAppMessage.buttons[0].subscribeToClickedEvent(function() {
          braze.requestPushPermission(function(){
            // success!
          }, function(){
            // user declined
          });
        });
      }

      // show the in-app message now
      braze.showInAppMessage(inAppMessage);
    }
  }
});
```

When you wish to display the soft push prompt to the user, call `braze.logCustomEvent("prime-for-push")` - for instance, to prompt the user on every page load just after the Braze session begins:

```
braze.openSession();
braze.logCustomEvent("prime-for-push");
```
