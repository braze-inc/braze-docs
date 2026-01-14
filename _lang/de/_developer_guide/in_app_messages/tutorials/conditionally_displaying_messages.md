---
nav_title: Bedingte Anzeige von Nachrichten
article_title: "Anleitung: Bedingte Anzeige von In-App-Nachrichten"
description: ""
page_order: 1
layout: scrolly
---

# Anleitung: Bedingte Anzeige von In-App-Nachrichten

> Folgen Sie dem Beispielcode in diesem Tutorial, um In-App-Nachrichten mit dem Braze SDK bedingt anzuzeigen.

{% sdktabs %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} Sie müssen auch [In-App-Nachrichten für Android aktivieren]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=android#android_enabling-in-app-messages).

## Bedingte Anzeige von In-App-Nachrichten für Android

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

!Schritt
Zeilen-MainApplication.kt=17

#### 1\. Enablement von Fehlersuchen (optional)

Um die Fehlerbehebung während der Entwicklung zu erleichtern, sollten Sie das Debugging aktivieren.

!Schritt
Zeilen-MainApplication.kt=26-28

#### 2\. Lebenszyklusrückrufe für Aktivitäten registrieren

Registrieren Sie den Standard-Listener von Braze, um den Lebenszyklus der In-App-Nachrichten zu verwalten.

!Schritt
Zeilen-MainApplication.kt=30-44

#### 3\. Einrichten eines Hörers für In-App-Nachrichten

Verwenden Sie `BrazeInAppMessageManager`, um einen angepassten Listener einzustellen, der Nachrichten abfängt, bevor sie angezeigt werden.

!Schritt
Zeilen-MainApplication.kt=34-42

#### 4\. Erstellen Sie bedingte Logik

Verwenden Sie eine angepasste Logik, um die Anzeige von Nachrichten zeitlich zu steuern. In diesem Beispiel prüft die angepasste Logik, ob das Extra `should_display_message` auf `"true"` eingestellt ist.

!Schritt
Zeilen-MainApplication.kt=38,41

#### 5\. Zurücksenden oder Verwerfen der Nachricht

Geben Sie eine `InAppMessageOperation` mit `DISPLAY_NOW` zurück, um die Nachricht anzuzeigen, oder mit `DISCARD`, um sie zu unterdrücken.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} Sie müssen auch [In-App-Nachrichten für Swift aktivieren]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=swift#swift_enabling-in-app-messages).

## Bedingte Anzeige von In-App-Nachrichten für Swift

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md %}

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

!Schritt
Zeilen-AppDelegate.swift=5

#### 1\. Implementieren Sie die `BrazeInAppMessageUIDelegate`

Implementieren Sie in Ihrer AppDelegate-Klasse die [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/delegate) damit Sie später die Methode `inAppMessage` überschreiben können.

!Schritt
Zeilen-AppDelegate.swift=12

#### 2\. Enablement von Fehlersuchen (optional)

Um die Fehlerbehebung während der Entwicklung zu erleichtern, sollten Sie das Debugging aktivieren.

!Schritt
Zeilen-AppDelegate.swift=19-21

#### 3\. Richten Sie Ihr Braze UI ein und delegieren Sie

`BrazeInAppMessageUI()` rendert In-App-Nachrichten standardmäßig. Wenn Sie `self` als Delegierten zuweisen, können Sie Nachrichten abfangen und bearbeiten, bevor sie angezeigt werden.

!Schritt
Zeilen-AppDelegate.swift=26-33

#### 4\. Überschreiben Sie `DisplayChoice` mit bedingter Logik

Überschreiben Sie [`inAppMessage(_:displayChoiceForMessage:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) um zu entscheiden, ob eine Nachricht angezeigt werden soll. Geben Sie `.now` ein, um die Nachricht anzuzeigen oder `.discard`, um sie zu unterdrücken.

{% endscrolly %}
{% endsdktab %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} Es ist jedoch keine zusätzliche Einrichtung erforderlich.

## Bedingte Anzeige von In-App-Nachrichten für das Internet

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

!Schritt
Zeilen-index.js=2

#### 1\. Entfernen Sie Aufrufe von `automaticallyShowInAppMessages()`

Entfernen Sie alle Aufrufe von [`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages)da sie jede angepasste Logik, die Sie später implementieren, außer Kraft setzen werden.

!Schritt
Zeilen-index.js=6

#### 2\. Enablement von Fehlersuchen (optional)

Um die Fehlerbehebung während der Entwicklung zu erleichtern, sollten Sie das Debugging aktivieren.

!Schritt
Zeilen-index.js=9-18

#### 3\. Updates für In-App-Nachrichten abonnieren

Registrieren Sie einen Callback mit [`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage) um jedes Mal, wenn eine In-App-Nachricht ausgelöst wird, einen `message` zu erhalten.

!Schritt
Zeilen-index.js=10-13

#### 4\. Erstellen Sie bedingte Logik

Erstellen Sie eine angepasste Logik, um zu steuern, wann Nachrichten angezeigt werden. In diesem Beispiel prüft die Logik, ob die URL `"checkout"` enthält oder ob ein `#checkout` Element auf der Seite existiert.

!Schritt
Zeilen-index.js=16

#### 5\. Nachrichten anzeigen mit `showInAppMessage`

Um die Nachricht anzuzeigen, rufen Sie [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage). Wenn Sie dies nicht tun, wird die Nachricht übersprungen.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}
