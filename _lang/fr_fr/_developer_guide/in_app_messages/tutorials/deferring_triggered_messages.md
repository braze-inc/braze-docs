---
nav_title: Report des messages déclenchés
article_title: "Tutoriel : Report et restauration des messages déclenchés"
description: ""
page_order: 1
layout: scrolly
---

# Tutoriel : Report et restauration des messages déclenchés

> Suivez l'exemple de code de ce tutoriel pour différer et restaurer les messages in-app déclenchés à l'aide du SDK de Braze.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} Cependant, aucune configuration supplémentaire n'est nécessaire.

## Report et restauration des messages déclenchés pour le Web

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

!étape
lignes-index.js=2

#### 1\. Supprimer les appels à `automaticallyShowInAppMessages()`

Supprimez tous les appels à [`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages) car ils remplaceront toute logique personnalisée que vous mettrez en œuvre ultérieurement.

!étape
lignes-index.js=6

#### 2\. Activer le débogage (facultatif)

Pour faciliter la résolution des problèmes lors du développement, pensez à activer le débogage.

!étape
lignes-index.js=9-16

#### 3\. S'abonner au gestionnaire de rappel des messages in-app.

Enregistrez un rappel avec [`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage) pour recevoir un message chaque fois qu'un message in-app est déclenché.

!étape
lignes-index.js=11-12

#### 4\. Report de l'instance `message` 

Pour différer l'envoi du message, appelez le [`deferInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#deferinappmessage). Braze sérialise et enregistre cet envoi de messages afin que vous puissiez l'afficher lors d'un prochain chargement de page.

!étape
lignes-index.js=18-24

#### 5\. Récupérer un message précédemment différé

Pour récupérer tout envoi de messages précédemment différés, appelez [`getDeferredInAppMessage()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getdeferredinappmessage). 

!étape
lignes-index.js=21-23

#### 6\. Afficher l'envoi de messages différés

Après avoir récupéré un message différé, affichez-le en le passant à [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage).

!étape
lignes-index.js=13-15

#### 7\. Affichage immédiat d'un message

Pour afficher un message au lieu de le différer, appelez [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage) directement dans votre rappel `subscribeToInAppMessage`.
{% endscrolly %}
{% endsdktab %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} Vous devrez également [activer les messages in-app pour Android]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=android#android_enabling-in-app-messages).

## Report et restauration des messages déclenchés pour Android

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

!étape
lignes-MainApplication.kt=13-16

#### 1\. Créer une instance unique de `Application` 

Utilisez un objet compagnon pour exposer votre classe `Application` en tant que singleton afin qu'elle soit accessible ultérieurement dans votre code.

!étape
lignes-MainApplication.kt=25

#### 2\. Activer le débogage (facultatif)

Pour faciliter la résolution des problèmes lors du développement, pensez à activer le débogage.

!étape
lignes-MainApplication.kt=34-36

#### 3\. Enregistrer les fonctions de rappel du cycle de vie des activités

Enregistrez l'auditeur par défaut de Braze pour gérer le cycle de vie des messages in-app.

!étape
lignes-MainApplication.kt=39-49

#### 4\. Configurer un récepteur de messages in-app

Utilisez `BrazeInAppMessageManager` pour définir un récepteur personnalisé qui intercepte les messages avant qu'ils ne soient affichés.

!étape
lignes-MainApplication.kt=43,46

#### 5\. Créer une logique conditionnelle

Utilisez le drapeau `showMessage` pour contrôler le délai : renvoyez `DISPLAY_NOW` pour afficher le message maintenant ou `DISPLAY_LATER` pour le différer.

!étape
lignes-MainApplication.kt=52-55

#### 6\. Créer une méthode d'envoi de messages différés

Utilisez `showDeferredMessage` pour déclencher le message in-app suivant. Lorsque `showMessage` est `true`, l'auditeur renvoie `DISPLAY_NOW`.

!étape
lignes-MainActivity.kt=29

#### 7\. Déclencher la méthode à partir de votre interface utilisateur

Pour afficher l'envoi de messages précédemment différé, appelez `showDeferredMessage(true)` à partir de votre interface utilisateur, par exemple en appuyant sur un bouton ou en tapotant.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} Vous devrez également [activer les messages in-app pour Swift]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=swift#swift_enabling-in-app-messages).

## Report et restauration des messages déclenchés pour Swift

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

!étape
lignes-AppDelegate.swift=5

#### 1\. Mettre en œuvre le `BrazeInAppMessageUIDelegate`

Dans votre classe `AppDelegate`, implémentez la méthode [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) afin que vous puissiez remplacer sa méthode `inAppMessage` ultérieurement.

!étape
lignes-AppDelegate.swift=19

#### 2\. Activer le débogage (facultatif)

Pour faciliter la résolution des problèmes lors du développement, pensez à activer le débogage.

!étape
lignes-AppDelegate.swift=25-27

#### 3\. Configurez votre interface utilisateur Braze et déléguez.

`BrazeInAppMessageUI()` rend les messages in-app par défaut. En attribuant à `self` le statut de délégué, vous pouvez intercepter et traiter les messages avant qu'ils ne soient affichés. Veillez à enregistrer l'instance, car vous en aurez besoin ultérieurement pour restaurer les messages différés.

!étape
lignes-AppDelegate.swift=32-41

#### 4\. Remplacer `DisplayChoice` par une logique conditionnelle

Ignorer [`inAppMessage(_:displayChoiceForMessage:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) pour déterminer quand un message doit être affiché. Retournez `.now` pour l'afficher immédiatement, ou `.reenqueue` pour le reporter à plus tard.

!étape
lignes-AppDelegate.swift=43-46

#### 5\. Créer une méthode pour afficher les messages différés

Créez une méthode qui appelle `showDeferredMessage(true)` pour afficher le message différé suivant dans la pile. Lorsqu'il est appelé, `showMessage` est défini comme `true`, ce qui fait que le délégué renvoie `.now`.

!étape
lignes-ContentView.swift=1-14

#### 5\. Déclencher la méthode à partir de votre interface utilisateur

Pour afficher l'envoi de messages précédemment différé, appelez `showDeferredMessage(true)` à partir de votre interface utilisateur, par exemple en appuyant sur un bouton ou en tapotant.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}
