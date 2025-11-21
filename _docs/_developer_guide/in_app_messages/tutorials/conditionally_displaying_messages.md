---
nav_title: Conditionally displaying messages
article_title: "Tutorial: Conditionally displaying in-app messages"
description: ""
page_order: 1
layout: scrolly
---

# Tutorial: Conditionally displaying in-app messages

> Follow along with the sample code in this tutorial to conditionally display in-app messages using the Braze SDK.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} However, no additional setup is required.

## Conditionally displaying in-app messages for Web

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Conditionally Displaying Messages Web" %}

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

Remove any calls to [`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages), as they'll override any custom logic you implement later.

!!step
lines-index.js=6

#### 2. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

!!step
lines-index.js=9-18

#### 3. Subscribe to in-app message updates

Register a callback with [`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage) to receive a `message` any time an in-app message is triggered.

!!step
lines-index.js=10-13

#### 4. Create conditional logic

Create custom logic to control when messages are displayed. In this example, the logic checks if the URL contains `"checkout"` or if a `#checkout` element exists on the page.

!!step
lines-index.js=16

#### 5. Display messages with `showInAppMessage`

To display the message, call [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage). If omitted, the message will be skipped.

{% endscrolly %}
{% endsdktab %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} You'll also need to [enable in-app messages for Android]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=android#android_enabling-in-app-messages).

## Conditionally displaying in-app messages for Android

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Conditionally Displaying Messages Android" %}

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

To make troubleshooting easier while developing, consider enabling debugging.

!!step
lines-MainApplication.kt=26-28

#### 2. Register activity lifecycle callbacks

Register Braze’s default listener to handle the in-app message lifecycle.

!!step
lines-MainApplication.kt=30-44

#### 3. Set up an in-app message listener

Use `BrazeInAppMessageManager` to set a custom listener that intercepts messages before they're displayed.

!!step
lines-MainApplication.kt=34-42

#### 4. Create conditional logic

Use custom logic to control message display timing. In this example, the custom logic checks if the `should_display_message` extra is set to `"true"`.

!!step
lines-MainApplication.kt=38,41

#### 5. Return or discard the message

Return an `InAppMessageOperation` with `DISPLAY_NOW` to display the message, or with `DISCARD` to suppress it.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} You'll also need to [enable in-app messages for Swift]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=swift#swift_enabling-in-app-messages).

## Conditionally displaying in-app messages for Swift

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Conditionally Displaying Messages Swift" %}

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

#### 1. Implement the `BrazeInAppMessageUIDelegate`

In your AppDelegate class, implement the [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/delegate) so you can override its `inAppMessage` method later.

!!step
lines-AppDelegate.swift=12

#### 2. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

!!step
lines-AppDelegate.swift=19-21

#### 3. Set up your Braze UI and delegate

`BrazeInAppMessageUI()` renders in-app messages by default. By assigning `self` as its delegate, you can intercept and handle messages before they're displayed.

!!step
lines-AppDelegate.swift=26-33

#### 4. Override `DisplayChoice` with conditional logic

Override [`inAppMessage(_:displayChoiceForMessage:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) to decide whether a message should be shown. Return `.now` to display the message or `.discard` to suppress it.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}
