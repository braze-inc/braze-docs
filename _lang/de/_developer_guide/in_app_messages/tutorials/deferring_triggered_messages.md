---
nav_title: Aufschieben von getriggerten Nachrichten
article_title: "Anleitung: Aufschieben und Wiederherstellen getriggerter Nachrichten"
description: ""
page_order: 1
layout: scrolly
---

# Anleitung: Aufschieben und Wiederherstellen getriggerter Nachrichten

> Folgen Sie dem Beispielcode in diesem Tutorial, um mit dem Braze SDK getriggerte In-App-Nachrichten aufzuschieben und wiederherzustellen.

{% sdktabs %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} Sie müssen auch [In-App-Nachrichten für Android aktivieren]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=android#android_enabling-in-app-messages).

## Aufschieben und Wiederherstellen getriggerter Nachrichten für Android

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

!Schritt
Zeilen-MainApplication.kt=13-16

#### 1\. Erstellen Sie eine singleton `Application` Instanz

Verwenden Sie ein Begleitobjekt, um Ihre Klasse `Application` als Singleton darzustellen, damit Sie später in Ihrem Code darauf zugreifen können.

!Schritt
Zeilen-MainApplication.kt=25

#### 2\. Enablement von Fehlersuchen (optional)

Um die Fehlerbehebung während der Entwicklung zu erleichtern, sollten Sie das Debugging aktivieren.

!Schritt
Zeilen-MainApplication.kt=34-36

#### 3\. Lebenszyklusrückrufe für Aktivitäten registrieren

Registrieren Sie den Standard-Listener von Braze, um den Lebenszyklus der In-App-Nachrichten zu verwalten.

!Schritt
Zeilen-MainApplication.kt=39-49

#### 4\. Einrichten eines Hörers für In-App-Nachrichten

Verwenden Sie `BrazeInAppMessageManager`, um einen angepassten Listener einzustellen, der Nachrichten abfängt, bevor sie angezeigt werden.

!Schritt
Zeilen-MainApplication.kt=43,46

#### 5\. Erstellen Sie bedingte Logik

Verwenden Sie das Flag `showMessage`, um das Timing zu steuern - geben Sie `DISPLAY_NOW` ein, um die Nachricht sofort anzuzeigen, oder `DISPLAY_LATER`, um sie zu verschieben.

!Schritt
Zeilen-MainApplication.kt=52-55

#### 6\. Erstellen Sie eine Methode zur Anzeige von zeitversetzten Nachrichten

Verwenden Sie `showDeferredMessage`, um die nächste In-App-Nachricht zu triggern. Wenn `showMessage` `true` ist, gibt der Listener `DISPLAY_NOW` zurück.

!Schritt
Zeilen-MainActivity.kt=29

#### 7\. Triggern Sie die Methode von Ihrer UI aus

Um die zuvor aufgeschobene Nachricht anzuzeigen, rufen Sie `showDeferredMessage(true)` von Ihrer UI aus auf, z. B. über einen Button oder durch Antippen.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} Sie müssen auch [In-App-Nachrichten für Swift aktivieren]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=swift#swift_enabling-in-app-messages).

## Aufschieben und Wiederherstellen von getriggerten Nachrichten für Swift

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

!Schritt
Zeilen-AppDelegate.swift=5

#### 1\. Implementieren Sie die `BrazeInAppMessageUIDelegate`

Implementieren Sie in Ihrer Klasse `AppDelegate` die Methode [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) damit Sie die Methode `inAppMessage` später überschreiben können.

!Schritt
Zeilen-AppDelegate.swift=19

#### 2\. Enablement von Fehlersuchen (optional)

Um die Fehlerbehebung während der Entwicklung zu erleichtern, sollten Sie das Debugging aktivieren.

!Schritt
Zeilen-AppDelegate.swift=25-27

#### 3\. Richten Sie Ihr Braze UI ein und delegieren Sie

`BrazeInAppMessageUI()` rendert In-App-Nachrichten standardmäßig. Wenn Sie `self` als Delegierten zuweisen, können Sie Nachrichten abfangen und bearbeiten, bevor sie angezeigt werden. Speichern Sie die Instanz unbedingt, da Sie sie später benötigen, um verschobene Nachrichten wiederherzustellen.

!Schritt
Zeilen-AppDelegate.swift=32-41

#### 4\. Überschreiben Sie `DisplayChoice` mit bedingter Logik

Überschreiben Sie [`inAppMessage(_:displayChoiceForMessage:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) um festzulegen, wann eine Nachricht angezeigt werden soll. Geben Sie `.now` ein, um es sofort anzuzeigen, oder `.reenqueue`, um es auf später zu verschieben.

!Schritt
Zeilen-AppDelegate.swift=43-46

#### 5\. Erstellen Sie eine Methode zur Anzeige zeitversetzter Nachrichten

Erstellen Sie eine Methode, die `showDeferredMessage(true)` aufruft, um die nächste zurückgestellte Nachricht im Stack anzuzeigen. Beim Aufruf wird `showMessage` auf `true` gesetzt, so dass der Delegierte `.now` zurückgibt.

!Schritt
Zeilen-ContentView.swift=1-14

#### 5\. Triggern Sie die Methode von Ihrer UI aus

Um die zuvor aufgeschobene Nachricht anzuzeigen, rufen Sie `showDeferredMessage(true)` von Ihrer UI aus auf, z. B. über einen Button oder durch Antippen.

{% endscrolly %}
{% endsdktab %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} Es ist jedoch keine zusätzliche Einrichtung erforderlich.

## Aufschieben und Wiederherstellen von getriggerten Nachrichten für das Internet

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

!Schritt
Zeilen-index.js=2

#### 1\. Entfernen Sie Aufrufe von `automaticallyShowInAppMessages()`

Entfernen Sie alle Aufrufe von [`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages) da sie jede angepasste Logik, die Sie später implementieren, außer Kraft setzen werden.

!Schritt
Zeilen-index.js=6

#### 2\. Enablement von Fehlersuchen (optional)

Um die Fehlerbehebung während der Entwicklung zu erleichtern, sollten Sie das Debugging aktivieren.

!Schritt
Zeilen-index.js=9-16

#### 3\. Abonnieren Sie den Callback Handler für In-App-Nachrichten

Registrieren Sie einen Callback mit [`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage) um jedes Mal eine Nachricht zu erhalten, wenn eine In-App-Nachricht ausgelöst wird.

!Schritt
Zeilen-index.js=11-12

#### 4\. Verschieben Sie die Instanz `message` 

Um die Nachricht aufzuschieben, rufen Sie [`deferInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#deferinappmessage). Braze serialisiert und speichert diese Nachricht, damit Sie sie bei einem späteren Laden der Seite anzeigen können.

!Schritt
Zeilen-index.js=18-24

#### 5\. Rufen Sie eine zuvor aufgeschobene Nachricht ab

Um alle zuvor zurückgestellten Nachrichten abzurufen, rufen Sie [`getDeferredInAppMessage()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getdeferredinappmessage). 

!Schritt
Zeilen-index.js=21-23

#### 6\. Anzeige der aufgeschobenen Nachricht

Nachdem Sie eine aufgeschobene Nachricht abgerufen haben, zeigen Sie sie an, indem Sie sie an [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage).

!Schritt
Zeilen-index.js=13-15

#### 7\. Eine Nachricht sofort anzeigen

Um eine Nachricht anzuzeigen, anstatt sie zu verschieben, rufen Sie [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage) direkt in Ihrem `subscribeToInAppMessage` Callback auf.
{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}
