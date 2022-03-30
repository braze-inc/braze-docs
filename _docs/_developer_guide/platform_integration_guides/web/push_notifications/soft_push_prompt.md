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

It's often a good idea for sites to implement a "soft" push prompt where you "prime" the user and make your case for sending them push notifications before requesting push permission. This is useful because the browser throttles how often you may prompt the user directly, and if the user denies permission, you can never ask them again. 

This can be done simply through Braze's [triggered in-app messages]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#in-app-messaging) for a seamless user experience. Instead of calling `appboy.registerAppboyPushMessages()` directly as described in the standard [Web push integration]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/#step-2-browser-registration), instead:

## Step 1: Create a push primer campaign

First, you must create a "Prime for Push" in-app messaging campaign in the Braze dashboard:

1. Create a **Modal** in-app message and give it whatever text and styling you would like. 
2. Next, set the on-click behavior to **Close Message**. This behavior will be customized later.
3. Add a key-value pair to the message where the key is `msg-id`, and the value is `push-primer`.
4. Assign a custom event trigger action "prime-for-push" to the message. You can create the custom event manually from the dashboard if needed.

## Step 2: Remove calls

In your Braze SDK integration, find and remove any calls to `appboy.display.automaticallyShowNewInAppMessages()` from within your loading snippet.

## Step 3: Update integration

Finally, replace the removed call with the following snippet:

```javascript

// Be sure to remove calls to appboy.display.automaticallyShowNewInAppMessages() 
// from your code as noted in the steps above

appboy.subscribeToInAppMessage(function(inAppMessage) {
  var shouldDisplay = true;

  if (inAppMessage instanceof appboy.InAppMessage) {
    // Read the key-value pair for msg-id
    var msgId = inAppMessage.extras["msg-id"];

    // If this is our push primer message
    if (msgId == "push-primer") {
      // We don't want to display the soft push prompt to users on browsers that don't support push, or if the user
      // has already granted/blocked permission
      if (!appboy.isPushSupported() || appboy.isPushPermissionGranted() || appboy.isPushBlocked()) {
        shouldDisplay = false;
      }
      if (inAppMessage.buttons[0] != null) {
        // Prompt the user when the first button is clicked
        inAppMessage.buttons[0].subscribeToClickedEvent(function() {
          appboy.registerAppboyPushMessages();
        });
      }
    }
  }

  // Display the message
  if (shouldDisplay) {
    appboy.display.showInAppMessage(inAppMessage);
  }
});
```

When you wish to display the soft push prompt to the user, call `appboy.logCustomEvent("prime-for-push")` - for instance, to prompt the user on every page load just after the Braze session begins:

```
appboy.openSession();
appboy.logCustomEvent("prime-for-push");
```