---
nav_title: Anpassen des Stils von Nachrichten
article_title: "Anleitung: Anpassen des Stils mit Schlüssel-Wert-Paaren"
description: ""
page_order: 1
layout: scrolly
---

# Anleitung: Anpassen des Stils von Nachrichten mit Schlüssel-Wert-Paaren

> Folgen Sie dem Beispielcode in diesem Tutorial, um das Styling Ihrer In-App-Nachricht mit Hilfe von Schlüssel-Wert-Paaren im Braze SDK anzupassen.

{% sdktabs %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} Sie müssen auch [In-App-Nachrichten für Android aktivieren]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=android#android_enabling-in-app-messages).

## Anpassen des Stils von Nachrichten mit Schlüssel-Wert-Paaren für Android

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

!Schritt
Zeilen-MainApplication.kt=19

#### 1\. Enablement von Fehlersuchen (optional)

Um die Fehlerbehebung während der Entwicklung zu erleichtern, sollten Sie das Debugging aktivieren.

!Schritt
Zeilen-MainApplication.kt=28-30

#### 2\. Lebenszyklusrückrufe für Aktivitäten registrieren

Registrieren Sie den Standard-Listener von Braze, um den Lebenszyklus der In-App-Nachrichten zu verwalten.

!Schritt
Zeilen-CustomInAppMessageViewFactory.kt=8

#### 3\. Erstellen Sie Ihre angepasste View Factory Klasse

Stellen Sie sicher, dass Ihre Klasse konform ist mit [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html) damit sie angepasste Nachrichtenansichten erstellen und zurückgeben kann.

!Schritt
Zeilen-CustomInAppMessageViewFactory.kt=15-20

#### 4\. Delegieren Sie an die Standardfabrik von Braze

Delegieren Sie an die Standardfabrik, um das in Braze integrierte Styling beizubehalten, bevor Sie Ihre eigenen bedingten Änderungen anwenden.

!Schritt
Zeilen-CustomInAppMessageViewFactory.kt=30-32,35-41

#### 5\. Zugriff auf Schlüssel-Wert-Paare von `inAppMessage.extras`

Verwenden Sie `inAppMessage.extras`, um auf angepasste Typen, Attribute für die Gestaltung oder andere im Dashboard definierte Werte zuzugreifen. Wenden Sie Styling-Überschreibungen an, bevor Sie die Ansicht zurückgeben.

!Schritt
Zeilen-MainApplication.kt=33-34

#### 6\. Implementieren Sie eine angepasste `IInAppMessageViewFactory`

Implementieren Sie [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html) in Ihrer angepassten Klasse, um In-App-Nachricht-Ansichten zu erstellen und darzustellen.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} Sie müssen auch [In-App-Nachrichten für Swift aktivieren]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=swift#swift_enabling-in-app-messages).

## Anpassen des Stils von Nachrichten mit Schlüssel-Wert-Paaren für Swift

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

!Schritt
Zeilen-AppDelegate.swift=5

#### 1\. Implementieren Sie `BrazeInAppMessageUIDelegate`

Implementieren Sie in Ihrer Klasse `AppDelegate` [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/delegate) damit Sie die Methode `inAppMessage` später überschreiben können.

!Schritt
Zeilen-AppDelegate.swift=17

#### 2\. Enablement von Fehlersuchen (optional)

Um die Fehlerbehebung während der Entwicklung zu erleichtern, sollten Sie das Debugging aktivieren.

!Schritt
Zeilen-AppDelegate.swift=30-50

#### 3\. Bereiten Sie Nachrichten vor, bevor sie angezeigt werden

Braze ruft `inAppMessage(_:prepareWith:)` während der Vorbereitung von Nachrichten auf. Verwenden Sie es, um den Stile anzupassen oder Logik auf der Grundlage von Schlüssel-Wert-Paaren anzuwenden.

!Schritt
Zeilen-AppDelegate.swift=34

#### 4\. Zugriff auf Schlüssel-Wert-Paare von `message.extras`

Verwenden Sie `message.extras`, um auf angepasste Typen, Attribute für die Gestaltung oder andere im Dashboard definierte Werte zuzugreifen.

!Schritt
Zeilen-AppDelegate.swift=38-46

#### 5\. Update der Styling-Attribute der Nachricht

Verwenden Sie [`inAppMessage(_:prepareWith:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) um auf `PresentationContext` zuzugreifen, damit Sie die Attribute für die Gestaltung direkt ändern können. Jede Art von In-App-Nachricht enthält unterschiedliche Attribute.

{% endscrolly %}
{% endsdktab %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} Es ist jedoch keine zusätzliche Einrichtung erforderlich.

## Anpassen des Stils von Nachrichten mit Hilfe von Schlüssel-Wert-Paaren für das Internet

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

!Schritt
Zeilen-index.js=2

#### 1\. Entfernen Sie Aufrufe von `automaticallyShowInAppMessages()`

Entfernen Sie alle Aufrufe von [`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages) da sie jede angepasste Logik, die Sie später implementieren, außer Kraft setzen werden.

!Schritt
Zeilen-index.js=6

#### 2\. Enablement von Fehlersuchen (optional)

Um die Fehlerbehebung während der Entwicklung zu erleichtern, sollten Sie das Debugging aktivieren.

!Schritt
Zeilen-index.js=9-21

#### 3\. Abonnieren Sie den Callback Handler für In-App-Nachrichten

Registrieren Sie einen Callback mit [`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage) um jedes Mal eine Nachricht zu erhalten, wenn eine In-App-Nachricht ausgelöst wird.

!Schritt
Zeilen-index.js=10-13

#### 4\. Rufen Sie die Eigenschaft `message.extras` auf.

Verwenden Sie `message.extras`, um auf angepasste Typen, Attribute für die Gestaltung oder andere im Dashboard definierte Werte zuzugreifen. Alle Werte werden als Strings zurückgegeben.

!Schritt
Zeilen-index.js=19

#### 5\. Bedingt aufrufen `showInAppMessage`

Um die Nachricht anzuzeigen, rufen Sie [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage). Andernfalls verwenden Sie die angepassten Eigenschaften nach Bedarf.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}
