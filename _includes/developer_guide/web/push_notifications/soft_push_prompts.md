{% multi_lang_include developer_guide/prerequisites/web.md %} You'll also need to [set up push notifications]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web).

## About soft push prompts

It's often a good idea for sites to implement a "soft" push prompt where you "prime" the user and make your case for sending them push notifications before requesting push permission. This is useful because the browser throttles how often you may prompt the user directly, and if the user denies permission you can never ask them again.

Alternatively, if you would like to include special custom handling, instead of calling `requestPushPermission()` directly as described in the standard [Web push integration]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/#step-2-browser-registration), use our [triggered in-app messages]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web).

{% alert tip %}
This can be done without SDK customization using our new [no code push primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/). 
{% endalert %}

## Setting up soft push prompts

{% multi_lang_include archive/web-v4-rename.md %}

### Step 1: Create a push primer campaign

First, you must create a "Prime for Push" in-app messaging campaign in the Braze dashboard:

1. Create a **Modal** in-app message with the text and styling you want. 
2. Next, set the on-click behavior to **Close Message**. This behavior will be customized later.
3. Add a key-value pair to the message where the key is `msg-id`, and the value is `push-primer`.
4. Assign a custom event trigger action (such as "prime-for-push") to the message. You can create the custom event manually from the dashboard if needed.

### Step 2: Remove calls

In your Braze SDK integration, find and remove any calls to `automaticallyShowInAppMessages()` from within your loading snippet.

### Step 3: Update integration

Finally, replace the removed call with the following snippet. Call `subscribeToInAppMessage()` before calling `openSession()`. This ensures your in-app message listener is registered in time to receive the push primer message.

```javascript
import * as braze from "@braze/web-sdk";
// Be sure to remove any calls to braze.automaticallyShowInAppMessages()
braze.subscribeToInAppMessage(function(inAppMessage) {
  // check if message is not a control variant
  if (inAppMessage instanceof braze.inAppMessage) {
    // access the key-value pairs, defined as `extras`
    const keyValuePairs = inAppMessage.extras || {};
    // check the value of our key `msg-id` defined in the Braze dashboard
    if (keyValuePairs["msg-id"] === "push-primer") {
      // We don't want to display the soft push prompt to users on browsers
      // that don't support push, or if the user has already granted/blocked permission
      if (
        braze.isPushSupported() === false ||
        braze.isPushPermissionGranted() ||
        braze.isPushBlocked()
      ) {
        // do not call `showInAppMessage`
        return;
      }

      // user is eligible to receive the native prompt
      // register a click handler on one of the two buttons
      if (inAppMessage.buttons[0]) {
        // Prompt the user when the first button is clicked
        inAppMessage.buttons[0].subscribeToClickedEvent(function() {
          braze.requestPushPermission(
            function() {
              // success!
            },
            function() {
              // user declined
            }
          );
        });
      }
    }
  }

  // show the in-app message now
  braze.showInAppMessage(inAppMessage);
});
```

When you wish to display the soft push prompt to the user, call `braze.logCustomEvent` - with whatever event name triggers this in-app message.
