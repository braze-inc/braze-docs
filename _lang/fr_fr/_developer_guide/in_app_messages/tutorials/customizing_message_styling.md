---
nav_title: Personnaliser le style des messages
article_title: "Tutoriel : Personnalisation du style à l'aide de paires clé-valeur"
description: ""
page_order: 1
layout: scrolly
---

# Tutoriel : Personnalisation du style des messages à l'aide de paires clé-valeur

> Suivez l'exemple de code de ce didacticiel pour personnaliser le style de vos messages in-app à l'aide de paires clé-valeur dans le SDK de Braze.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} Cependant, aucune configuration supplémentaire n'est nécessaire.

## Personnalisation du style personnalisé des messages à l'aide de paires clé-valeur pour le Web

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Customizing Message Styling Web" %}

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

!étape
lignes-index.js=2

#### 1\. Supprimer les appels à `automaticallyShowInAppMessages()`

Supprimez tous les appels à [`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages) car ils remplaceront toute logique personnalisée que vous mettrez en œuvre ultérieurement.

!étape
lignes-index.js=6

#### 2\. Activer le débogage (facultatif)

Pour faciliter la résolution des problèmes lors du développement, pensez à activer le débogage.

!étape
lignes-index.js=9-21

#### 3\. S'abonner au gestionnaire de rappel des messages in-app.

Enregistrez un rappel avec [`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage) pour recevoir un message chaque fois qu'un message in-app est déclenché.

!étape
lignes-index.js=10-13

#### 4\. Accéder à la propriété `message.extras` 

Utilisez `message.extras` pour accéder aux types de personnalisation, aux attributs de style ou à toute autre valeur définie dans le tableau de bord. Toutes les valeurs sont renvoyées sous forme de chaînes de caractères.

!étape
lignes-index.js=19

#### 5\. Appel conditionnel `showInAppMessage`

Pour afficher le message, appelez la touche [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage). Sinon, utilisez les propriétés personnalisées nécessaires.

{% endscrolly %}
{% endsdktab %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} Vous devrez également [activer les messages in-app pour Android]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=android#android_enabling-in-app-messages).

## Personnalisation du style des messages à l'aide de paires clé-valeur pour Android

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Customizing Message Styling Android" %}

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

!étape
lignes-MainApplication.kt=19

#### 1\. Activer le débogage (facultatif)

Pour faciliter la résolution des problèmes lors du développement, pensez à activer le débogage.

!étape
lignes-MainApplication.kt=28-30

#### 2\. Enregistrer les fonctions de rappel du cycle de vie des activités

Enregistrez l'auditeur par défaut de Braze pour gérer le cycle de vie des messages in-app.

!étape
lignes-CustomInAppMessageViewFactory.kt=8

#### 3\. Créez votre classe de fabrique de vues personnalisée

Assurez-vous que votre classe est conforme à [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html) afin qu'elle puisse construire et renvoyer des messages personnalisés.

!étape
lignes-CustomInAppMessageViewFactory.kt=15-20

#### 4\. Déléguer à l'usine par défaut de Braze

Déléguez à la fabrique par défaut pour conserver le style intégré de Braze avant d'appliquer vos propres modifications conditionnelles.

!étape
lignes-CustomInAppMessageViewFactory.kt=30-32,35-41

#### 5\. Accéder à des paires clé-valeur à partir de `inAppMessage.extras`

Utilisez `inAppMessage.extras` pour accéder aux types de personnalisation, aux attributs de style ou à toute autre valeur définie dans le tableau de bord. Appliquer les surcharges de style avant de renvoyer la vue.

!étape
lignes-MainApplication.kt=33-34

#### 6\. Mettre en place un système personnalisé de `IInAppMessageViewFactory`

Mettre en œuvre [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html) dans votre classe personnalisée pour construire et afficher les messages in-app.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} Vous devrez également [activer les messages in-app pour Swift]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=swift#swift_enabling-in-app-messages).

## Personnalisation du style des messages à l'aide de paires clé-valeur pour Swift

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Customizing Message Styling Swift" %}

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

!étape
lignes-AppDelegate.swift=5

#### 1\. Mettre en œuvre `BrazeInAppMessageUIDelegate`

Dans votre classe `AppDelegate`, implémentez [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/delegate) afin que vous puissiez remplacer sa méthode `inAppMessage` ultérieurement.

!étape
lignes-AppDelegate.swift=17

#### 2\. Activer le débogage (facultatif)

Pour faciliter la résolution des problèmes lors du développement, pensez à activer le débogage.

!étape
lignes-AppDelegate.swift=30-50

#### 3\. Préparer les messages avant qu'ils ne soient affichés

Braze appelle `inAppMessage(_:prepareWith:)` pendant la préparation du message. Utilisez-le pour personnaliser le style ou appliquer une logique basée sur des paires clé-valeur.

!étape
lignes-AppDelegate.swift=34

#### 4\. Accéder à des paires clé-valeur à partir de `message.extras`

Utilisez `message.extras` pour accéder aux types de personnalisation, aux attributs de style ou à toute autre valeur définie dans le tableau de bord.

!étape
lignes-AppDelegate.swift=38-46

#### 5\. Mise à jour des attributs de style du message

Utilisez [`inAppMessage(_:prepareWith:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) pour accéder au site `PresentationContext` et modifier directement les attributs de style. Chaque type de message in-app expose des attributs différents.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}
