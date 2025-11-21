---
nav_title: Deferring triggered messages
article_title: "Tutorial: Deferring and restoring triggered messages"
description: ""
page_order: 1
layout: scrolly
---

# Tutorial: Deferring and restoring triggered messages

> Follow along with the sample code in this tutorial to defer and restore triggered in-app messages using the Braze SDK.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} However, no additional setup is required.

## Deferring and restoring triggered messages for Web

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Deferring Triggered Messages Web" %}

{% scrolly %}

```js file=index.js
import * as braze from "@braze/web-sdk";
// Remove any calls to `braze.automaticallyShowInAppMessages()`

braze.initialize("YOUR-API-KEY", {
  baseUrl: "YOUR-ENDPOINT",
  enableLogging: true,
});

braze.subscribeToInAppMessage(function (message) {
  const shouldDefer = true; // customize for your own logic
  if (shouldDefer) {
    braze.deferInAppMessage(message);
  } else {
    braze.showInAppMessage(message);
  }
});

// elsewhere in your app
document.getElementById("button").onclick = function () {
  const deferredMessage = braze.getDeferredInAppMessage();
  if (deferredMessage) {
    braze.showInAppMessage(deferredMessage);
  }
};
```

!!step
lines-index.js=2

#### 1. Remove calls to `automaticallyShowInAppMessages()`

Remove any calls to [`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages) , as they’ll override any custom logic you implement later.

!!step
lines-index.js=6

#### 2. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

!!step
lines-index.js=9-16

#### 3. Subscribe to the in-app message callback handler

Register a callback with [`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage) to receive a message any time an in-app message is triggered.

!!step
lines-index.js=11-12

#### 4. Defer the `message` instance

To defer the message, call [`deferInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#deferinappmessage). Braze will serialize and save this message so you can display it on a future page load.

!!step
lines-index.js=18-24

#### 5. Retrieve a previously deferred message

To retrieve any previously-deferred messages, call [`getDeferredInAppMessage()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getdeferredinappmessage). 

!!step
lines-index.js=21-23

#### 6. Display the deferred message

After retrieving a deferred message, display it by passing it to [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage).

!!step
lines-index.js=13-15

#### 7. Display a message immediately

To show a message instead of deferring it, call [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage) directly in your `subscribeToInAppMessage` callback.
{% endscrolly %}
{% endsdktab %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} You'll also need to [enable in-app messages for Android]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=android#android_enabling-in-app-messages).

## Deferring and restoring triggered messages for Android

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Deferring Triggered Messages Android" %}

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
    companion object {
        private var instance: MyApplication? = null
        fun getInstance(): MyApplication = instance!!
    }

    private var showMessage = false

    override fun onCreate() {
        super.onCreate()
        instance = this

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
                return if (showMessage) {
                    // Show the message using Braze's UI
                    InAppMessageOperation.DISPLAY_NOW
                } else {
                    // Re-enqueue the message for later
                    InAppMessageOperation.DISPLAY_LATER
                }
            }
        })
    }

    fun showDeferredMessage(show: Boolean) {
        showMessage = show
        BrazeInAppMessageManager.getInstance().requestDisplayInAppMessage()
    }
}
```

```kotlin file=MainActivity.kt
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material.Button
import androidx.compose.material.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            ContentView()
        }
    }
}

@Composable
fun ContentView() {
    Column(
        modifier = Modifier.padding(16.dp),
        verticalArrangement = Arrangement.spacedBy(20.dp)
    ) {
        // ... your UI

        Button(onClick = {
            MyApplication.getInstance().showDeferredMessage(true)
        }) {
            Text("Show Deferred IAM")
        }
    }
}
```

!!step
lines-MainApplication.kt=13-16

#### 1. Create a singleton `Application` instance

Use a companion object to expose your `Application` class as a singleton so it can be accessed later in your code.

!!step
lines-MainApplication.kt=25

#### 2. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

!!step
lines-MainApplication.kt=34-36

#### 3. Register activity lifecycle callbacks

Register Braze’s default listener to handle the in-app message lifecycle.

!!step
lines-MainApplication.kt=39-49

#### 4. Set up an in-app message listener

Use `BrazeInAppMessageManager` to set a custom listener that intercepts messages before they’re displayed.

!!step
lines-MainApplication.kt=43,46

#### 5. Create conditional logic

Use the `showMessage` flag to control timing&#8212;return `DISPLAY_NOW` to display the message now or `DISPLAY_LATER` to defer it.

!!step
lines-MainApplication.kt=52-55

#### 6. Create a method for displaying deferred messages

Use `showDeferredMessage` to trigger the next in-app message. When `showMessage` is `true`, the listener will return `DISPLAY_NOW`.

!!step
lines-MainActivity.kt=29

#### 7. Trigger the method from your UI

To display the previously-deferred message, call `showDeferredMessage(true)` from your UI, such as a button or tap.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} You'll also need to [enable in-app messages for Swift]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=swift#swift_enabling-in-app-messages).

## Deferring and restoring triggered messages for Swift

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Deferring Triggered Messages Swift" %}

{% scrolly %}

```swift file=AppDelegate.swift
import SwiftUI
import BrazeKit
import BrazeUI

class AppDelegate: UIResponder, UIApplicationDelegate, BrazeInAppMessageUIDelegate {
    static private(set) var shared: AppDelegate!

    private var braze: Braze!
    public var showMessage: Bool = false

    func application(
      _ application: UIApplication,
      didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {
        AppDelegate.shared = self

        // 1. Braze configuration with your SDK API key and endpoint
        let configuration = Braze.Configuration(apiKey: "a1fc095b-ae3d-40f4-bb33-3fb5176562c0", endpoint: "sondheim.braze.com")
        configuration.logger.level = .debug

        // 2. Initialize Braze SDK instance
        braze = Braze(configuration: configuration)

        // 3. Set up Braze In-App Message UI and delegate
        let ui = BrazeInAppMessageUI()
        ui.delegate = self
        braze.inAppMessagePresenter = ui

        return true
    }

    func inAppMessage(
      _ ui: BrazeInAppMessageUI,
      displayChoiceForMessage message: Braze.InAppMessage
    ) -> BrazeInAppMessageUI.DisplayChoice {
        if !showMessage {
            return .reenqueue
        }

        return .now
    }

    func showDeferredMessage(showMessage: Bool) {
        self.showMessage = showMessage
        (braze.inAppMessagePresenter as? BrazeInAppMessageUI)?.presentNext()
    }
}
```

```swift file=SampleApp.swift
import SwiftUI

@main
struct IAMDeferApp: App {
    @UIApplicationDelegateAdaptor(AppDelegate.self) var delegate

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
```

```swift file=ContentView.swift
import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack(spacing: 20) {
            // ...your UI

            Button("Show Deferred IAM") {
                AppDelegate.shared.showDeferredMessage(showMessage: true)
            }
        }
        .padding()
    }
}
```

!!step
lines-AppDelegate.swift=5

#### 1. Implement the `BrazeInAppMessageUIDelegate`

In your `AppDelegate` class, implement the [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) so you can override its `inAppMessage` method later.

!!step
lines-AppDelegate.swift=19

#### 2. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

!!step
lines-AppDelegate.swift=25-27

#### 3. Set up your Braze UI and delegate

`BrazeInAppMessageUI()` renders in-app messages by default. By assigning `self` as its delegate, you can intercept and handle messages before they're displayed. Be sure to save the instance, as you'll need it later to restore deferred messages.

!!step
lines-AppDelegate.swift=32-41

#### 4. Override `DisplayChoice` with conditional logic

Override [`inAppMessage(_:displayChoiceForMessage:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) to determine when a message should be displayed. Return `.now` to show it immediately, or `.reenqueue` to defer it for later.

!!step
lines-AppDelegate.swift=43-46

#### 5. Create a method to show deferred messages

Create a method that calls `showDeferredMessage(true)` to display the next deferred message in the stack. When called, `showMessage` is set to `true`, making the delegate return `.now`.

!!step
lines-ContentView.swift=1-14

#### 5. Trigger the method from your UI

To display the previously-deferred message, call `showDeferredMessage(true)` from your UI, such as a button or tap.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}
