---
nav_title: Accessing Key-Value Pairs
guide_top_header: Accessing In-App Message Key-Value Pairs
article_title: Accessing Key-Value Pairs
page_order: 1
layout: scrolly
description: "A tutorial on how to access key-value pairs with in-app messages"
---

# Accessing Key-Value Pairs

{% tabs %}
{% tab Web %}
{% scrolly %}

```js file=index.js
import * as braze from "@braze/web-sdk";
// remove any calls to `automaticallyShowInAppMessages()`
// REMOVE --> braze.automaticallyShowInAppMessages()

braze.subscribeToInAppMessage(function (message) {
  const extras = message.extras;
  const customTemplateType = extras["custom-template"] || "";
  const customColor = extras["custom-color"] || "";
  const customMessageId = extras["message-id"] || "";

  if (customTemplateType) {
    // add your own custom code to render this message
  } else {
    // otherwise, use Braze built-in UI
    braze.showInAppMessage(message);
  }
});
```

!!step
lines-index.js=2-3

#### 1. Remove calls to `automaticallyShowInAppMessages()`

Be sure to remove any calls to [`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages).

This method will show your messages regardless of any customized code you add later on.

!!step
lines-index.js=5,17

#### 2. Subscribe to the in-app message callback handler

Register a callback using [`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage).

This method will be called whenever an in-app message has been triggered, with a `message` argument.

!!step
lines-index.js=6

#### 3. Access the `message.extras` property

Key-value pairs you have defined in the Braze dashboard will be available using the `extras` message property.

All values supplied will be typed as a string

!!step
lines-index.js=11-16

#### 4. Conditionally call the `showInAppMessage` method

If you want Braze to display the message, call the [`showInAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage) method on the provided `message`.

Otherwise you can use the custom properties as you wish!
{% endscrolly %}
{% endtab %}
{% tab iOS %}
{% scrolly %}

```swift file=AppDelegate.swift
import UIKit
import BrazeKit
import BrazeUI

@main
class AppDelegate: UIResponder, UIApplicationDelegate {
  var window: UIWindow?
  static var braze: Braze?

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    let configuration = Braze.Configuration(
      apiKey: "YOUR-API-KEY",
      endpoint: "YOUR-ENDPOINT"
    )
    let braze = Braze(configuration: configuration)
    AppDelegate.braze = braze

    braze.inAppMessageDelegate = InAppMessageHandler()
    return true
  }
}
```

```swift file=InAppMessageHandler.swift
import BrazeKit
import BrazeUI

class InAppMessageHandler: NSObject, BrazeInAppMessageUIDelegate {
  func beforeInAppMessageDisplayed(_ message: Braze.InAppMessage) -> BrazeInAppMessageDisplayChoice {
    if let extras = message.extras {
      let template = extras["custom-template"] ?? ""
      let color = extras["custom-color"] ?? ""
      let messageId = extras["message-id"] ?? ""

      // TODO: Render using custom logic
      print("Template: \(template), Color: \(color), ID: \(messageId)")
    }

    return .displayNow
  }
}
```

!!step
lines-AppDelegate.swift=13-15

#### 1. Create a Braze SDK configuration

Use your dashboard API key and endpoint to create a Braze.Configuration object.

!!step
lines-AppDelegate.swift=16

#### 2. Instantiate the Braze object

Pass your configuration to initialize Braze, then store the instance globally for access across the app.

!!step
lines-AppDelegate.swift=17

#### 3. Assign the instance to a static variable

This makes the Braze instance accessible anywhere in your app using AppDelegate.braze.

!!step
lines-AppDelegate.swift=19

#### 4. Set the in-app message delegate

Hook into in-app messages by setting braze.inAppMessageDelegate = InAppMessageHandler(), a class you define next.

!!step
lines-InAppMessageHandler.swift=4-5

#### 5. Implement BrazeInAppMessageUIDelegate

Create a class that conforms to BrazeInAppMessageUIDelegate, which lets you intercept and customize in-app messages.

!!step
lines-InAppMessageHandler.swift=6

#### 6. Handle messages before they're displayed

Braze will call beforeInAppMessageDisplayed whenever a message is about to show. You can choose to intercept or render it differently.

!!step
lines-InAppMessageHandler.swift=7-13

#### 7. Access key-value pairs from message.extras

Use the extras dictionary to retrieve values like custom-template, custom-color, or any dashboard-defined properties.

!!step
lines-InAppMessageHandler.swift=15

#### 8. Choose whether to show the message

Return .displayNow to use Braze’s built-in UI, or return .discard / .displayLater to take full control.

{% endscrolly %}
{% endtab %}
{% endtabs %}
