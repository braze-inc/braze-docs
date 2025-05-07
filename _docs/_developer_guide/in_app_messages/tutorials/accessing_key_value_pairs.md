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

class AppDelegate: UIResponder, UIApplicationDelegate, BrazeInAppMessageUIDelegate {
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

    return true
  }

  func inAppMessage(
    _ ui: BrazeInAppMessageUI,
    displayChoiceForMessage message: Braze.InAppMessage
  ) -> BrazeInAppMessageUI.DisplayChoice {
      let extras = message.extras

      let template   = extras["custom-template"] as? String ?? ""
      let color      = extras["custom-color"]   as? String ?? ""
      let messageId  = extras["message-id"]     as? String ?? ""

      // Your custom logic
      print("Template: \(template), Color: \(color), ID: \(messageId)")

      return .now
  }
}
```

```swift file=SampleApp.swift
import SwiftUI

@main
struct SampleApp: App {
  @UIApplicationDelegateAdaptor(AppDelegate.self) var appDelegate

  var body: some Scene {
    WindowGroup {
      YourView()
    }
  }
}
```

!!step
lines-AppDelegate.swift=5

#### 1. Implement BrazeInAppMessageUIDelegate

Have your AppDelegate conform to BrazeInAppMessageUIDelegate, which lets you intercept and handle in-app messages.

!!step
lines-AppDelegate.swift=23-38

#### 2. Handle messages before they're displayed

The Braze SDK will call this function whenever a message is about to show. You can choose to intercept it, render it differently, or grab key-value pairs.

!!step
lines-AppDelegate.swift=27-31

#### 3. Access key-value pairs from message.extras

Use the extras dictionary to retrieve values like custom-template, custom-color, or any dashboard-defined properties.

!!step
lines-AppDelegate.swift=36

#### 4. Choose whether to show the message

Return `.now` to use Braze's built-in In-App Message UI.

{% endscrolly %}
{% endtab %}
{% tab Android %}
{% scrolly %}

```kotlin file=MainApplication.kt
package com.example.brazedevlab

import android.app.Application
import com.braze.Braze
import com.braze.support.BrazeLogger
import com.braze.configuration.BrazeConfig
import com.braze.ui.inappmessage.BrazeInAppMessageManager
import com.braze.BrazeActivityLifecycleCallbackListener
import com.braze.ui.inappmessage.listeners.IInAppMessageManagerListener
import com.braze.models.inappmessage.IInAppMessage
import com.braze.ui.inappmessage.InAppMessageOperation
import android.util.Log

class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Enable verbose Braze SDK logs
        BrazeLogger.logLevel = Log.VERBOSE

        // Initialize Braze
        val brazeConfig = BrazeConfig.Builder()
            .setApiKey("YOUR-API-KEY")
            .setCustomEndpoint("YOUR-ENDPOINT")
            .build()
        Braze.configure(this, brazeConfig)

        registerActivityLifecycleCallbacks(
            BrazeActivityLifecycleCallbackListener()
        )
        // Set up in-app message listener
        BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener(object : IInAppMessageManagerListener {
            override fun beforeInAppMessageDisplayed(inAppMessage: IInAppMessage): InAppMessageOperation {
                val extras = inAppMessage.extras

                val template = extras["custom-template"] ?: ""
                val color = extras["custom-color"] ?: ""
                val messageId = extras["message-id"] ?: ""

                // Your custom logic
                Log.d("Braze", "Template: $template, Color: $color, ID: $messageId")

                // Return DISPLAY_NOW to show the message using Braze's UI
                return InAppMessageOperation.DISPLAY_NOW
            }
        })
    }
}
```

!!step
lines-MainApplication.kt=19

#### 1. Turn on debugging (optional)

Turn on debugging while developing to make troubleshooting easier!

!!step
lines-MainApplication.kt=28-30

#### 2. Register activity lifecycle callbacks

Register Braze's default activity lifecycle callback listener to handle the lifecycle of in-app messages.

!!step
lines-MainApplication.kt=32-46

#### 3. Set up the in-app message listener

Use `BrazeInAppMessageManager` to set a custom listener that will intercept messages before they're displayed.

!!step
lines-MainApplication.kt=34-38

#### 4. Access key-value pairs from message.extras

Use the extras map to retrieve values like custom-template, custom-color, or any dashboard-defined properties.

!!step
lines-MainApplication.kt=44

#### 5. Choose whether to show the message

Return `InAppMessageOperation.DISPLAY_NOW` to use Braze's built-in In-App Message UI.

{% endscrolly %}
{% endtab %}
{% endtabs %}
