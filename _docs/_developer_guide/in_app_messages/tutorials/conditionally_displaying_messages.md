---
nav_title: Conditionally Displaying Messages
article_title: "Tutorial: Conditionally displaying in-app messages"
description: ""
page_order: 1
layout: scrolly
---

# Tutorial: Conditionally displaying in-app messages

> Follow along with the sample code in this tutorial to conditionally display in-app messages using the Braze SDK.

{% sdktabs %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} You'll also need to [enable in-app messages for Android]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=android#android_enabling-in-app-messages).

## Conditionally displaying in-app messages for Android

{% scrolly %}

```kotlin file=MainApplication.kt
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
                // Check if we should show the message
                val shouldShow = inAppMessage.extras["should_display_message"] == "true"

                return if (shouldShow) {
                    // Show the message using Braze's UI
                    InAppMessageOperation.DISPLAY_NOW
                } else {
                    // Discard the message (or we could also create our own UI using KVP values)
                    InAppMessageOperation.DISCARD
                }
            }
        })
    }
}
```

!!step
lines-MainApplication.kt=17

#### 1. Enable debugging (optional)

Enable debugging while developing to make troubleshooting easier!

!!step
lines-MainApplication.kt=26-28

#### 2. Register activity lifecycle callbacks

Register Braze's default activity lifecycle callback listener to handle the lifecycle of in-app messages.

!!step
lines-MainApplication.kt=30-44

#### 3. Set up the in-app message listener

Use `BrazeInAppMessageManager` to set a custom listener that will intercept messages before they're displayed.

!!step
lines-MainApplication.kt=34-42

#### 4. Check for any display condition

Apply your custom logic to control whether or not the message should be displayed.

In this example, we're checking if the `should_display_message` extra is set to "true".

!!step
lines-MainApplication.kt=38,41

#### 5. Return the appropriate operation

Return `InAppMessageOperation.DISPLAY_NOW` to show the message using Braze's UI, or `InAppMessageOperation.DISCARD` to prevent the message from being displayed.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} You'll also need to [enable in-app messages for Swift]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=swift#swift_enabling-in-app-messages).

## Conditionally displaying in-app messages for Swift

{% scrolly %}

```swift file=AppDelegate.swift
import SwiftUI
import BrazeKit
import BrazeUI

class AppDelegate: NSObject, UIApplicationDelegate, BrazeInAppMessageUIDelegate {
    static var braze: Braze?

    func application(_ application: UIApplication,
                     didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil) -> Bool {
        // 1. Braze configuration with your SDK API key and endpoint
        let configuration = Braze.Configuration(apiKey: "YOUR_API_ENDPOINT", endpoint: "YOUR_API_KEY")
        configuration.logger.level = .debug

        // 2. Initialize Braze SDK instance
        let brazeInstance = Braze(configuration: configuration)
        AppDelegate.braze = brazeInstance

        // 3. Set up Braze In-App Message UI and delegate
        let inAppMessageUI = BrazeInAppMessageUI()
        inAppMessageUI.delegate = self
        brazeInstance.inAppMessagePresenter = inAppMessageUI

        return true
    }

    func inAppMessage(_ ui: BrazeInAppMessageUI,
                      displayChoiceForMessage message: Braze.InAppMessage) -> BrazeInAppMessageUI.DisplayChoice {
        if let showFlag = message.extras["should_display_message"] as? String, showFlag == "true" {
            return .now
        } else {
            return .discard
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

In your AppDelegate class, implement the [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/delegate). This will allow you to override its `inAppMessage` method later on.

!!step
lines-AppDelegate.swift=12

#### 2. Enable debugging (optional)

Enable debugging while developing to make troubleshooting easier!

!!step
lines-AppDelegate.swift=19-21

#### 3. Set up Braze In-App Message UI and delegate

`BrazeInAppMessageUI()` is the default UI renderer for IAMs. By setting its delegate to your `BrazeInAppMessageUIDelegate` implementation (in this case, `self`), it'll ensure its methods are called before any IAMs are invoked.

!!step
lines-AppDelegate.swift=26-33

#### 4. Override `DisplayChoice` with your logic

Override [`BrazeInAppMessageUIDelegate .inAppMessage(_:displayChoiceForMessage:)`](<https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb>) with the checks you'd like to perform. There are 2 enumeration types we will use in this case:

- `.now` will return the message as normal (now).
- `.discard` will throw the message away.

{% endscrolly %}
{% endsdktab %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} However, no additional setup is required.

## Conditionally displaying in-app messages for Web

{% scrolly %}

```js file=index.js
import * as braze from "@braze/web-sdk";
// Remove any calls to `braze.automaticallyShowInAppMessages()`

braze.initialize("YOUR-API-KEY", {
  baseUrl: "YOUR-ENDPOINT",
  enableLogging: true,
});

braze.subscribeToInAppMessage(function (message) {
  if (
    location.pathname === "/checkout" ||
    document.getElementById("#checkout")
  ) {
    // do not show the message
  } else {
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

Enable debugging while developing to make troubleshooting easier!

!!step
lines-index.js=9-18

#### 3. Subscribe to the in-app message callback handler

Register a callback using [`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage).

This method will be called whenever an in-app message has been triggered, with a `message` argument.

!!step
lines-index.js=10-13

#### 4. Check for any display condition

Apply your custom logic to control whether or not the message should be displayed.

In this example, we're checking if the URL contains "checkout" or if a `#checkout` element exists on the page.

!!step
lines-index.js=16

#### 5. Conditionally call the `showInAppMessage` method

If you want to display the message, call the [`showInAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage) method on the provided `message`

If you do not want to display the message, don't call `showInAppMessage`
{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}
