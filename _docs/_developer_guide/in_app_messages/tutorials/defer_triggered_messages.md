---
nav_title: Deferring Triggered Messages
article_title: "Tutorial: Deferring and restoring triggered messages"
description: ""
page_order: 1
layout: scrolly
---

# Tutorial: Deferring and restoring triggered messages

> Follow along with the sample code in this tutorial to defer and restore triggered in-app messages using the Braze SDK.

{% sdktabs %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} You'll also need to [enable in-app messages for Android]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=android#android_enabling-in-app-messages).

## Deferring and restoring triggered messages for Android

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md %}

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

#### 1. Set up a singleton instance

Create a companion object to provide access to the Application instance.

!!step
lines-MainApplication.kt=25

#### 2. Enable debugging (optional)

Enable debugging while developing to make troubleshooting easier!

!!step
lines-MainApplication.kt=34-36

#### 3. Register activity lifecycle callbacks

Register Braze's default activity lifecycle callback listener to handle the lifecycle of in-app messages.

!!step
lines-MainApplication.kt=39-49

#### 4. Set up the in-app message listener

Use `BrazeInAppMessageManager` to set a custom listener that will intercept messages before they're displayed.

!!step
lines-MainApplication.kt=43,46

#### 5. Control message display with `showMessage`

Use the `showMessage` flag to determine whether to show the message now or later.

!!step
lines-MainApplication.kt=52-55

#### 6. Create a method to show deferred messages

`showDeferredMessage` will present the next IAM (the IAM at the top of the stack), and setting `showMessage` to true will make our listener return `DISPLAY_NOW`.

!!step
lines-MainActivity.kt=29

#### 7. Trigger the method from your UI

Restoring the message elsewhere in your app, in this case an activity with a trigger button.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} You'll also need to [enable in-app messages for Swift]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=swift#swift_enabling-in-app-messages).

## Deferring and restoring triggered messages for Swift

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md %}

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

#### 1. Have you AppDelegate class conform to `BrazeInAppMessageUIDelegate`

Have your `AppDelegate` conform to [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate). This will allow you to override its `inAppMessage` method later on.

!!step
lines-AppDelegate.swift=19

#### 2. Enable debugging (optional)

Enable debugging while developing to make troubleshooting easier!

!!step
lines-AppDelegate.swift=25-27

#### 3. Set up Braze In-App Message UI and its delegate

`BrazeInAppMessageUI()` is the default UI renderer for IAMs. By setting its delegate to your `BrazeInAppMessageUIDelegate` implementation (in this case, `self`), it'll ensure its methods are called before any IAMs are invoked.

Save `inAppMessageUI`; you will need it later when restoring the message.

!!step
lines-AppDelegate.swift=32-41

#### 4. Override `DisplayChoice` with your logic

Override [`BrazeInAppMessageUIDelegate .inAppMessage(_:displayChoiceForMessage:)`](<https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb>) with the checks you'd like to perform. There are 2 enumeration types we will use in this case:

- `.now` will return the message as normal (now).
- `.reenqueue` will place the message back on the top of the stack of IAM messages.

!!step
lines-AppDelegate.swift=43-46

#### 5. Create a method to show deferred messages

`showDeferredMessage` will present the next IAM (the IAM at the top of the stack), and setting `self.showMessage` to true will make our DisplayChoice return `.now`

!!step
lines-ContentView.swift=1-14

#### 5. Trigger the method elsewhere in your code

Here, our UI is restoring the method from a button-click.

{% endscrolly %}
{% endsdktab %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} However, no additional setup is required.

## Deferring and restoring triggered messages for Web

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

Be sure to remove any calls to [`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages). This method will show your messages regardless of any customized code you add later on.

!!step
lines-index.js=6

#### 2. Enable debugging (optional)

Enable debugging while developing to make troubleshooting easier!

!!step
lines-index.js=9-16

#### 3. Subscribe to the in-app message callback handler

This method will be called whenever an in-app message has been triggered.

!!step
lines-index.js=11-12

#### 4. Defer the `message` instance

Use the [`deferInAppMessage(message)](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#deferinappmessage) method to defer the message for later display.

This method automatically serializes and stores the `message` allow you to retrieve it on a subsequent pageload.

!!step
lines-index.js=18-24

#### 5. Retrieve a previously deferred message

At some point later, use the [`getDeferredInAppMessage()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getdeferredinappmessage) method to retrieve any deferred messages.

!!step
lines-index.js=21-23

#### 6. Show the deferred in-app message

Use the [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage) method to display the message at the new appropriate time.

!!step
lines-index.js=13-15

#### 7. Show the in-app message in other cases

In other cases where you don't want to defer the immediate display of the message, continue calling [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage) in your message listener.
{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}
