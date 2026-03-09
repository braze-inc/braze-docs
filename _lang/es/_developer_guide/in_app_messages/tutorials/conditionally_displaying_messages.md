---
nav_title: Mostrar mensajes de forma condicional
article_title: "Tutorial: Mostrar mensajes dentro de la aplicación de forma condicional"
description: ""
page_order: 1
layout: scrolly
---

# Tutorial: Mostrar mensajes dentro de la aplicación de forma condicional

> Sigue el código de ejemplo de este tutorial para mostrar mensajes dentro de la aplicación de forma condicional utilizando el SDK de Braze.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} Sin embargo, no es necesario realizar ninguna configuración adicional.

## Visualización condicional de mensajes dentro de la aplicación para Web

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

!!paso
líneas-=2index.js

#### 1\. Eliminar llamadas a `automaticallyShowInAppMessages()`

Elimina cualquier llamada a [`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages), ya que anularán cualquier lógica personalizada que implementes más adelante.

!!paso
líneas-=6index.js

#### 2\. Habilitar depuración (opcional)

Para facilitar la solución de problemas durante el desarrollo, considera la posibilidad de habilitar la depuración.

!!paso
líneas-=9-18index.js

#### 3\. Suscríbete a las actualizaciones de mensajes dentro de la aplicación.

Realiza el registro de una devolución de llamada con[`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage)  para recibir una`message`  cada vez que se desencadene un mensaje dentro de la aplicación.

!!paso
líneas-=10-13index.js

#### 4\. Crear lógica condicional

Crea una lógica personalizada para controlar cuándo se muestran los mensajes. En este ejemplo, la lógica comprueba si la URL contiene`"checkout"`  o si existe un`#checkout`elemento  en la página.

!!paso
líneas-=16index.js

#### 5\. Mostrar mensajes con `showInAppMessage`

Para mostrar el mensaje, llama [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage)a . Si se omite, el mensaje se omitirá.

{% endscrolly %}
{% endsdktab %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} También tendrás que [habilitar los mensajes dentro de la aplicación para Android]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=android#android_enabling-in-app-messages).

## Visualización condicional de mensajes dentro de la aplicación para Android

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

!!paso
líneas-=17MainApplication.kt

#### 1\. Habilitar depuración (opcional)

Para facilitar la solución de problemas durante el desarrollo, considera la posibilidad de habilitar la depuración.

!!paso
líneas-=26-28MainApplication.kt

#### 2\. Registra las devoluciones de llamada del ciclo de vida de la actividad

Registra el listener predeterminado de Braze para gestionar el ciclo de vida de los mensajes dentro de la aplicación.

!!paso
líneas-=30-44MainApplication.kt

#### 3\. Configurar un detector de mensajes dentro de la aplicación

Utiliza`BrazeInAppMessageManager`  para configurar un listener personalizado que intercepte los mensajes antes de que se muestren.

!!paso
líneas-=34-42MainApplication.kt

#### 4\. Crear lógica condicional

Utiliza lógica personalizada para controlar el momento en que se muestran los mensajes. En este ejemplo, la lógica personalizada comprueba si el`should_display_message`extra está establecido en `"true"`.

!!paso
líneas-=38MainApplication.kt,41

#### 5\. Devolver o descartar el mensaje

Devuelve un`InAppMessageOperation`  con`DISPLAY_NOW`  para mostrar el mensaje, o con`DISCARD`  para ocultarlo.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} También tendrás que [habilitar los mensajes dentro de la aplicación para SWIFT]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=swift#swift_enabling-in-app-messages).

## Visualización condicional de mensajes dentro de la aplicación para SWIFT

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

!!paso
líneas-=5AppDelegate.swift

#### 1\. Implementar el `BrazeInAppMessageUIDelegate`

En tu clase AppDelegate, implementa  para[`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/delegate)que puedas sobrescribir su`inAppMessage`método  más adelante.

!!paso
líneas-=12AppDelegate.swift

#### 2\. Habilitar depuración (opcional)

Para facilitar la solución de problemas durante el desarrollo, considera la posibilidad de habilitar la depuración.

!!paso
líneas-=19-21AppDelegate.swift

#### 3\. Configura tu interfaz de usuario de Braze y delega

`BrazeInAppMessageUI()` muestra mensajes dentro de la aplicación de forma predeterminada. Al asignar`self`  como tu delegado, puedes interceptar y gestionar los mensajes antes de que se muestren.

!!paso
líneas-=26-33AppDelegate.swift

#### 4\. Anular`DisplayChoice`con lógica condicional

Anular[`inAppMessage(_:displayChoiceForMessage:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb)para decidir si se debe mostrar un mensaje. Vuelve a`.now`  para mostrar el mensaje o`.discard`  para ocultarlo.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}
