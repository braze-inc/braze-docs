---
nav_title: Mostrar mensajes condicionalmente
article_title: "Tutorial: Visualización condicional de mensajes dentro de la aplicación"
description: ""
page_order: 1
layout: scrolly
---

# Tutorial: Visualización condicional de mensajes dentro de la aplicación

> Sigue el código de ejemplo de este tutorial para mostrar mensajes dentro de la aplicación de forma condicional utilizando el SDK de Braze.

{% sdktabs %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} También tendrás que [habilitar los mensajes dentro de la aplicación para Android]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=android#android_enabling-in-app-messages).

## Visualización condicional de mensajes dentro de la aplicación para Android

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

Paso
líneas-MainApplication.kt=17

#### 1\. Habilitar la depuración (opcional)

Para facilitar la solución de problemas durante el desarrollo, considera la posibilidad de habilitar la depuración.

Paso
líneas-MainApplication.kt=26-28

#### 2\. Registra las devoluciones de llamada del ciclo de vida de la actividad

Registra la escucha predeterminada de Braze para gestionar el ciclo de vida de los mensajes dentro de la aplicación.

Paso
líneas-MainApplication.kt=30-44

#### 3\. Configurar un receptor de mensajes dentro de la aplicación

Utiliza `BrazeInAppMessageManager` para establecer una escucha personalizada que intercepte los mensajes antes de que se muestren.

Paso
líneas-MainApplication.kt=34-42

#### 4\. Crear lógica condicional

Utiliza una lógica personalizada para controlar el tiempo de visualización de los mensajes. En este ejemplo, la lógica personalizada comprueba si el extra `should_display_message` está configurado en `"true"`.

Paso
líneas-MainApplication.kt=38,41

#### 5\. Devolver o descartar el mensaje

Devuelve un `InAppMessageOperation` con `DISPLAY_NOW` para mostrar el mensaje, o con `DISCARD` para suprimirlo.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} También tendrás que [habilitar los mensajes dentro de la aplicación para Swift]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=swift#swift_enabling-in-app-messages).

## Visualización condicional de mensajes dentro de la aplicación para Swift

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

Paso
líneas-AppDelegate.swift=5

#### 1\. Pon en práctica la `BrazeInAppMessageUIDelegate`

En tu clase AppDelegate, implementa el método [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/delegate) para que puedas anular su método `inAppMessage` más adelante.

Paso
líneas-AppDelegate.swift=12

#### 2\. Habilitar la depuración (opcional)

Para facilitar la solución de problemas durante el desarrollo, considera la posibilidad de habilitar la depuración.

Paso
líneas-AppDelegate.swift=19-21

#### 3\. Configura tu interfaz de usuario Braze y delega

`BrazeInAppMessageUI()` muestra mensajes dentro de la aplicación de forma predeterminada. Asignando `self` como delegado, puedes interceptar y gestionar los mensajes antes de que se muestren.

Paso
líneas-AppDelegate.swift=26-33

#### 4\. Anula `DisplayChoice` con lógica condicional

Anula [`inAppMessage(_:displayChoiceForMessage:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) para decidir si se debe mostrar un mensaje. Devuelve `.now` para mostrar el mensaje o `.discard` para suprimirlo.

{% endscrolly %}
{% endsdktab %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} Sin embargo, no es necesaria ninguna configuración adicional.

## Visualización condicional de mensajes dentro de la aplicación para Web

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

Paso
líneas-index.js=2

#### 1\. Eliminar las llamadas a `automaticallyShowInAppMessages()`

Elimina las llamadas a [`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages)ya que anularán cualquier lógica personalizada que implementes más adelante.

Paso
líneas-index.js=6

#### 2\. Habilitar la depuración (opcional)

Para facilitar la solución de problemas durante el desarrollo, considera la posibilidad de habilitar la depuración.

Paso
líneas-index.js=9-18

#### 3\. Suscríbete a las actualizaciones de mensajes dentro de la aplicación

Registra una devolución de llamada con [`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage) para recibir una `message` cada vez que se desencadene un mensaje dentro de la aplicación.

Paso
líneas-index.js=10-13

#### 4\. Crear lógica condicional

Crea una lógica personalizada para controlar cuándo se muestran los mensajes. En este ejemplo, la lógica comprueba si la URL contiene `"checkout"` o si existe un elemento `#checkout` en la página.

Paso
líneas-index.js=16

#### 5\. Mostrar mensajes con `showInAppMessage`

Para visualizar el mensaje, llama a [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage). Si se omite, se saltará el mensaje.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}
