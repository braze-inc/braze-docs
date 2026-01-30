---
nav_title: Affichage conditionnel des messages
article_title: "Tutoriel : Affichage conditionnel des messages in-app"
description: ""
page_order: 1
layout: scrolly
---

# Tutoriel : Affichage conditionnel des messages in-app

> Suivez l'exemple de code de ce tutoriel pour afficher de manière conditionnelle des messages in-app à l'aide du SDK de Braze.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} Cependant, aucune configuration supplémentaire n'est nécessaire.

## Affichage conditionnel des messages in-app pour le web

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

!étape
lignes-index.js=2

#### 1\. Supprimer les appels à `automaticallyShowInAppMessages()`

Supprimez tous les appels à [`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages)car ils remplaceront toute logique personnalisée que vous mettrez en œuvre ultérieurement.

!étape
lignes-index.js=6

#### 2\. Activer le débogage (facultatif)

Pour faciliter la résolution des problèmes lors du développement, pensez à activer le débogage.

!étape
lignes-index.js=9-18

#### 3\. S'abonner aux envois de messages in-app

Enregistrez un rappel avec [`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage) pour recevoir un `message` chaque fois qu'un message in-app est déclenché.

!étape
lignes-index.js=10-13

#### 4\. Créer une logique conditionnelle

Créez une logique personnalisée pour contrôler l'affichage des messages. Dans cet exemple, la logique vérifie si l'URL contient `"checkout"` ou si un élément `#checkout` existe sur la page.

!étape
lignes-index.js=16

#### 5\. Affichage des messages avec `showInAppMessage`

Pour afficher le message, appelez la touche [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage). En cas d'omission, le message sera ignoré.

{% endscrolly %}
{% endsdktab %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} Vous devrez également [activer les messages in-app pour Android]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=android#android_enabling-in-app-messages).

## Affichage conditionnel des messages in-app pour Android

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

!étape
lignes-MainApplication.kt=17

#### 1\. Activer le débogage (facultatif)

Pour faciliter la résolution des problèmes lors du développement, pensez à activer le débogage.

!étape
lignes-MainApplication.kt=26-28

#### 2\. Enregistrer les fonctions de rappel du cycle de vie des activités

Enregistrez l'auditeur par défaut de Braze pour gérer le cycle de vie des messages in-app.

!étape
lignes-MainApplication.kt=30-44

#### 3\. Configurer un récepteur de messages in-app

Utilisez `BrazeInAppMessageManager` pour définir un récepteur personnalisé qui intercepte les messages avant qu'ils ne soient affichés.

!étape
lignes-MainApplication.kt=34-42

#### 4\. Créer une logique conditionnelle

Utilisez une logique personnalisée pour contrôler la synchronisation de l'affichage des messages. Dans cet exemple, la logique personnalisée vérifie si l'option `should_display_message` est définie sur `"true"`.

!étape
lignes-MainApplication.kt=38,41

#### 5\. Renvoyer ou rejeter le message

Retournez un `InAppMessageOperation` avec `DISPLAY_NOW` pour afficher le message, ou avec `DISCARD` pour le supprimer.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} Vous devrez également [activer les messages in-app pour Swift]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=swift#swift_enabling-in-app-messages).

## Affichage conditionnel des messages in-app pour Swift

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

!étape
lignes-AppDelegate.swift=5

#### 1\. Mettre en œuvre le `BrazeInAppMessageUIDelegate`

Dans votre classe AppDelegate, implémentez la méthode [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/delegate) afin que vous puissiez remplacer sa méthode `inAppMessage` ultérieurement.

!étape
lignes-AppDelegate.swift=12

#### 2\. Activer le débogage (facultatif)

Pour faciliter la résolution des problèmes lors du développement, pensez à activer le débogage.

!étape
lignes-AppDelegate.swift=19-21

#### 3\. Configurez votre interface utilisateur Braze et déléguez.

`BrazeInAppMessageUI()` rend les messages in-app par défaut. En attribuant à `self` le statut de délégué, vous pouvez intercepter et traiter les messages avant qu'ils ne soient affichés.

!étape
lignes-AppDelegate.swift=26-33

#### 4\. Remplacer `DisplayChoice` par une logique conditionnelle

Remplacer [`inAppMessage(_:displayChoiceForMessage:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) pour décider si un message doit être affiché. Retournez `.now` pour afficher le message ou `.discard` pour le supprimer.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}
