---
nav_title: Customizing Message Styling
article_title: "Tutorial: Customizing styling using key-value pairs"
description: ""
page_order: 1
layout: scrolly
---

# Tutorial: Customizing message styling using key-value pairs

> Follow along with the sample code in this tutorial to customize your in-app message styling using key-value pairs in the Braze SDK.

{% sdktabs %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} You'll also need to [enable in-app messages for Android]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=android#android_enabling-in-app-messages).

## Customizing message styling using key-value pairs for Android

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md %}

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

        // Set up custom in-app message view factory
        BrazeInAppMessageManager.getInstance()
        .setCustomInAppMessageViewFactory(CustomInAppMessageViewFactory())
    }
}
```

```kotlin file=CustomInAppMessageViewFactory.kt
import android.app.Activity
import android.graphics.Color
import android.view.View
import com.braze.models.inappmessage.IInAppMessage
import com.braze.ui.inappmessage.BrazeInAppMessageManager
import com.braze.ui.inappmessage.IInAppMessageViewFactory

class CustomInAppMessageViewFactory : IInAppMessageViewFactory {

    override fun createInAppMessageView(
        activity: Activity,
        inAppMessage: IInAppMessage
    ): View {
        // 1) Obtain Braze’s default view factory for this message type
        val defaultFactory =
            BrazeInAppMessageManager.getInstance()
                .getDefaultInAppMessageViewFactory(inAppMessage)
                ?: throw IllegalStateException(
                    "Braze default IAM view factory is missing"
                )

        // 2) Inflate the default view
        val iamView = defaultFactory
            .createInAppMessageView(activity, inAppMessage)
            ?: throw IllegalStateException(
                "Braze default IAM view is null"
            )

        // 3) Get your KVP extras
        val extras = inAppMessage.extras ?: emptyMap()
        val customization = extras["customization"]
        val overrideColor = extras["custom-color"]

        // 4) Style your root view
        if (customization == "slideup-attributes" && overrideColor != null) {
            try {
                iamView.setBackgroundColor(Color.parseColor(overrideColor))
            } catch (_: IllegalArgumentException) {
                // ignore bad styling
            }
        }

        return iamView
    }
}
```

!!step
lines-MainApplication.kt=19

#### 1. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

!!step
lines-MainApplication.kt=28-30

#### 2. Register activity lifecycle callbacks

Register Braze's default activity lifecycle callback listener to handle the lifecycle of in-app messages.

!!step
lines-CustomInAppMessageViewFactory.kt=8

#### 3. Create your custom view factory class

Make sure that your class conforms to [IInAppMessageViewFactory](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html); this will allow us to create a custom view factory class that will construct and render the message views.

!!step
lines-CustomInAppMessageViewFactory.kt=15-20

#### 4. Delegate first to Braze’s default factory

In this use case, we're simply overlaying our own conditional styling, so we want to make sure the IAM's built-in styling is preserved.

!!step
lines-CustomInAppMessageViewFactory.kt=30-32,35-41

#### 5. Get key-value pairs, and apply your styling

Inspect `inAppMessage.extras` for the keys of your choice (set via the dashboard). Apply any overrides (e.g. call view.setBackgroundColor(...)) before returning that view.

!!step
lines-MainApplication.kt=33-34

#### 6. Set your custom [IInAppMessageViewFactory](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html)

Use `IInAppMessageViewFactory` to create a custom view factory class that will construct and render the message views.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} You'll also need to [enable in-app messages for Swift]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=swift#swift_enabling-in-app-messages).

## Customizing message styling using key-value pairs for Swift

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md %}

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
    configuration.logger.level = .debug

    let braze = Braze(configuration: configuration)
    AppDelegate.braze = braze

    // Set up Braze In-App Message UI and delegate
    let inAppMessageUI = BrazeInAppMessageUI()
    inAppMessageUI.delegate = self
    brazeInstance.inAppMessagePresenter = inAppMessageUI

    return true
  }

    func inAppMessage(
      _ ui: BrazeInAppMessageUI,
      prepareWith context: inout BrazeInAppMessageUI.PresentationContext
    ) {
      let customization = context.message.extras["customization"] as? String

      if customization == "slideup-attributes" {
        // Create a new attributes object and make customizations.
        var attributes = context.attributes?.slideup
        attributes?.font = UIFont(name: "Chalkduster", size: 17)!
        attributes?.imageSize = CGSize(width: 65, height: 65)
        attributes?.cornerRadius = 20
        attributes?.imageCornerRadius = 10
        if #available(iOS 13.0, *) {
          attributes?.cornerCurve = .continuous
          attributes?.imageCornerCurve = .continuous
        }

        context.attributes?.slideup = attributes
      }
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

#### 1. Implement `BrazeInAppMessageUIDelegate`

Have your AppDelegate conform to `BrazeInAppMessageUIDelegate`, which lets you intercept and customize handling in-app messages.

!!step
lines-AppDelegate.swift=17

#### 2. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

!!step
lines-AppDelegate.swift=30-50

#### 3. Prepare messages before they're displayed

The Braze SDK will call this function whenever a message is being prepared for presentation. You can choose to intercept it, render it differently, or grab key-value pairs.

!!step
lines-AppDelegate.swift=34

#### 4. Access key-value pairs from message.extras

Use the extras dictionary to retrieve values like customization types, or attributes, or really any dashboard-defined properties.

!!step
lines-AppDelegate.swift=38-46

#### 5. Update the message's styling attributes

[BrazeInAppMessageUIDelegate inAppMessage(\_:prepareWith:)](<https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog>) surfaces `PresentationContext`, which allows direct modification of the message's styling attributes. Each type of in-app message has different attributes available.

{% endscrolly %}
{% endsdktab %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} However, no additional setup is required.

## Customizing message styling using key-value pairs for Web

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md %}

{% scrolly %}

```js file=index.js
import * as braze from "@braze/web-sdk";
// Remove any calls to `braze.automaticallyShowInAppMessages()`

braze.initialize("YOUR-API-KEY", {
  baseUrl: "YOUR-ENDPOINT",
  enableLogging: true,
});

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
lines-index.js=2

#### 1. Remove calls to `automaticallyShowInAppMessages()`

Be sure to remove any calls to [`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages).

This method will show your messages regardless of any customized code you add later on.

!!step
lines-index.js=6

#### 2. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

!!step
lines-index.js=9-21

#### 3. Subscribe to the in-app message callback handler

Register a callback using [`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage).

This method will be called whenever an in-app message has been triggered, with a `message` argument.

!!step
lines-index.js=10-13

#### 4. Access the `message.extras` property

Key-value pairs you have defined in the Braze dashboard will be available using the `extras` message property.

All values supplied will be typed as a string

!!step
lines-index.js=19

#### 5. Conditionally call the `showInAppMessage` method

If you want Braze to display the message, call the [`showInAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage) method on the provided `message`.

Otherwise you can use the custom properties as you wish!
{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}
