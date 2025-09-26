---
nav_title: Personalizar el estilo de los mensajes
article_title: "Tutorial: Personalización del estilo mediante pares clave-valor"
description: ""
page_order: 1
layout: scrolly
---

# Tutorial: Personalización del estilo del mensaje mediante pares clave-valor

> Sigue el código de ejemplo de este tutorial para personalizar el estilo de tu mensaje dentro de la aplicación utilizando pares clave-valor en el SDK de Braze.

{% sdktabs %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} También tendrás que [habilitar los mensajes dentro de la aplicación para Android]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=android#android_enabling-in-app-messages).

## Personalización del estilo de los mensajes mediante pares clave-valor para Android

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

Paso
líneas-MainApplication.kt=19

#### 1\. Habilitar la depuración (opcional)

Para facilitar la solución de problemas durante el desarrollo, considera la posibilidad de habilitar la depuración.

Paso
líneas-MainApplication.kt=28-30

#### 2\. Registra las devoluciones de llamada del ciclo de vida de la actividad

Registra la escucha predeterminada de Braze para gestionar el ciclo de vida de los mensajes dentro de la aplicación.

Paso
líneas-CustomInAppMessageViewFactory.kt=8

#### 3\. Crea tu clase de fábrica de vistas personalizada

Asegúrate de que tu clase se ajusta a [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html) para que pueda construir y devolver vistas de mensajes personalizadas.

Paso
líneas-CustomInAppMessageViewFactory.kt=15-20

#### 4\. Delegar en la fábrica predeterminada de Braze

Delega en la fábrica predeterminada para conservar el estilo incorporado de Braze antes de aplicar tus propios cambios condicionales.

Paso
líneas-CustomInAppMessageViewFactory.kt=30-32,35-41

#### 5\. Acceder a los pares clave-valor de `inAppMessage.extras`

Utiliza `inAppMessage.extras` para acceder a los tipos de personalización, atributos de estilo o cualquier otro valor definido en el panel. Aplica las modificaciones de estilo antes de devolver la vista.

Paso
líneas-MainApplication.kt=33-34

#### 6\. Implementa un sistema personalizado `IInAppMessageViewFactory`

Implementa [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html) en tu clase personalizada para construir y mostrar vistas de mensajes dentro de la aplicación.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} También tendrás que [habilitar los mensajes dentro de la aplicación para Swift]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=swift#swift_enabling-in-app-messages).

## Personalización del estilo de los mensajes mediante pares clave-valor para Swift

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

Paso
líneas-AppDelegate.swift=5

#### 1\. Pon en marcha `BrazeInAppMessageUIDelegate`

En tu clase `AppDelegate`, implementa [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/delegate) para que puedas anular su método `inAppMessage` más adelante.

Paso
líneas-AppDelegate.swift=17

#### 2\. Habilitar la depuración (opcional)

Para facilitar la solución de problemas durante el desarrollo, considera la posibilidad de habilitar la depuración.

Paso
líneas-AppDelegate.swift=30-50

#### 3\. Prepara los mensajes antes de mostrarlos

Braze llama a `inAppMessage(_:prepareWith:)` durante la preparación del mensaje. Utilízalo para personalizar el estilo personalizado o aplicar una lógica basada en pares clave-valor.

Paso
líneas-AppDelegate.swift=34

#### 4\. Acceder a los pares clave-valor de `message.extras`

Utiliza `message.extras` para acceder a los tipos de personalización, atributos de estilo o cualquier otro valor definido en el panel.

Paso
líneas-AppDelegate.swift=38-46

#### 5\. Actualiza los atributos de estilo del mensaje

Utiliza [`inAppMessage(_:prepareWith:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) para acceder a `PresentationContext` y poder modificar directamente los atributos de estilo. Cada tipo de mensaje dentro de la aplicación expone diferentes atributos.

{% endscrolly %}
{% endsdktab %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} Sin embargo, no es necesaria ninguna configuración adicional.

## Personalización del estilo de los mensajes mediante pares clave-valor para Web

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

Paso
líneas-index.js=2

#### 1\. Eliminar las llamadas a `automaticallyShowInAppMessages()`

Elimina las llamadas a [`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages) ya que anularán cualquier lógica personalizada que implementes más adelante.

Paso
líneas-index.js=6

#### 2\. Habilitar la depuración (opcional)

Para facilitar la solución de problemas durante el desarrollo, considera la posibilidad de habilitar la depuración.

Paso
líneas-index.js=9-21

#### 3\. Suscribirse al controlador de devolución de llamada de mensajes dentro de la aplicación

Registra una devolución de llamada con [`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage) para recibir un mensaje cada vez que se desencadene un mensaje dentro de la aplicación.

Paso
líneas-index.js=10-13

#### 4\. Accede a la propiedad `message.extras` 

Utiliza `message.extras` para acceder a los tipos de personalización, atributos de estilo o cualquier otro valor definido en el panel. Todos los valores se devuelven como cadenas.

Paso
líneas-index.js=19

#### 5\. Llama condicionalmente `showInAppMessage`

Para visualizar el mensaje, llama a [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage). Si no, utiliza las propiedades personalizadas que necesites.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}
