{% multi_lang_include developer_guide/prerequisites/web.md %}

## Message triggers

## Trigger types

In-app messages are automatically triggered when the SDK logs one of the following custom event types: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, and `Push Click`. Note that the `Specific Purchase` and `Custom Event` triggers also contain robust property filters.

{% alert note %}
In-app messages can't be triggered through the API or by API events&#8212;only custom events logged by the SDK. To learn more about logging, see [Logging Custom Events]({{site.baseurl}}/developer_guide/analytics/logging_events/).
{% endalert %}

### Delivery semantics

All eligible in-app messages are delivered to a user's device at the start of their session. When delivered, the SDK will prefetch assets, so they're available at trigger time, minimizing display latency. If the trigger event has more than one eligible in-app message, only the message with the highest priority will be delivered.

For more information about the SDK's session start semantics, see[Session Lifecycle]({{site.baseurl}}/developer_guide/platform_integration_guides/analytics/tracking_sessions/).

### Rate limits

By default, you can send an in-app message once every 30 seconds.

To override this, add the following property to your Braze configuration&#8212;before the Braze instance is initialized. You can set it to any positive integer, which represents the minimum time interval in seconds. For example:

```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```

## Key-value pairs

When you create a campaign in Braze, you can set key-value pairs as `extras`, which the the in-app messaging object can use to send data to your app. For example:

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  if (inAppMessage instanceof braze.ControlMessage) {
    return braze.showInAppMessage(inAppMessage);
  }


  if (inAppMessage instanceof braze.InAppMessage) {
    const extras = inAppMessage.extras;
    if (extras) {
      for (const key in extras) {
        console.log("key: " + key + ", value: " + extras[key]);
      }
    }
  }
  braze.showInAppMessage(inAppMessage);
});
```

## Disabling automatic triggers

To prevent in-app messages from automatically triggering:

Remove the call to `braze.automaticallyShowInAppMessages()` within your loading snippet, then create custom logic to handle showing or not showing in-app messages.

```javascript
braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  
  if (inAppMessage.isControl) { // v4.5.0+, otherwise use  `inAppMessage instanceof braze.ControlMessage`
     return braze.showInAppMessage(inAppMessage);
  }
  
  // Display the in-app message. You could defer display here by pushing this message to code within your own application.
  // If you don't want to use the Braze built-in display capabilities, you could alternatively pass the in-app message to your own display code here.
  
  if ( should_show_the_message_according_to_your_custom_logic ) {
      braze.showInAppMessage(inAppMessage);
  } else {
      // do nothing
  }
});
```

{% alert important %}
If you don't remove `braze.automaticallyShowInAppMessages()` from your website, then call `braze.showInAppMessage`, the message may display multiple times.
{% endalert %}

The `inAppMessage` parameter will be an [`braze.InAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) subclass or an [`braze.ControlMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.controlmessage.html) object, each of which has various lifecycle event subscription methods. See the [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) for full documentation.

Only one [`Modal`]({{site.baseurl}}/developer_guide/in_app_messages/?tab=modal&sdktab=web) or [`Full`]({{site.baseurl}}/developer_guide/in_app_messages/?tab=full&sdktab=web) in-app message can be displayed at a given time. If you attempt to show a second modal or full message while one is already showing, `braze.showInAppMessage` will return false, and the second message will not display.

## Manually triggering messages

### Displaying a message in real-time

In-app messages can also be created within your site and displayed locally in real-time. All customization options available on the dashboard are also available locally. This is particularly useful for displaying messages you wish to trigger within the app in real-time. However, analytics on these locally-created messages will not be available within the Braze dashboard.

```javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```

## Triggering exit-intent messages

Exit-intent messages are non-disruptive in-app messages used to communicate important information to visitors before they leave your site.

To set up triggers for these message types, implement an exit-intent library in your website (such as [ouibounce's open-source library](https://github.com/carlsednaoui/ouibounce)), then use the following code to log `'exit intent'` as a custom event in Braze. Now your future in-app message campaigns can use this message type as a custom event trigger.

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```
