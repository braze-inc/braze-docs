---
nav_title: Aplazar mensajes desencadenados
article_title: "Tutorial: Aplazar y restaurar mensajes desencadenados"
description: ""
page_order: 1
layout: scrolly
---

# Tutorial: Aplazar y restaurar mensajes desencadenados

> Sigue el código de ejemplo de este tutorial para aplazar y restaurar mensajes desencadenados dentro de la aplicación utilizando el SDK de Braze.

{% sdktabs %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} También tendrás que [habilitar los mensajes dentro de la aplicación para Android]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=android#android_enabling-in-app-messages).

## Aplazar y restaurar mensajes desencadenados para Android

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

Paso
líneas-MainApplication.kt=13-16

#### 1\. Crea una instancia singleton `Application` 

Utiliza un objeto compañero para exponer tu clase `Application` como un singleton, de modo que se pueda acceder a ella más adelante en tu código.

Paso
líneas-MainApplication.kt=25

#### 2\. Habilitar la depuración (opcional)

Para facilitar la solución de problemas durante el desarrollo, considera la posibilidad de habilitar la depuración.

Paso
líneas-MainApplication.kt=34-36

#### 3\. Registra las devoluciones de llamada del ciclo de vida de la actividad

Registra la escucha predeterminada de Braze para gestionar el ciclo de vida de los mensajes dentro de la aplicación.

Paso
líneas-MainApplication.kt=39-49

#### 4\. Configurar un receptor de mensajes dentro de la aplicación

Utiliza `BrazeInAppMessageManager` para configurar una escucha personalizada que intercepte los mensajes antes de que se muestren.

Paso
líneas-MainApplication.kt=43,46

#### 5\. Crear lógica condicional

Utiliza la bandera `showMessage` para controlar el tiempo: `DISPLAY_NOW` para mostrar el mensaje ahora o `DISPLAY_LATER` para aplazarlo.

Paso
líneas-MainApplication.kt=52-55

#### 6\. Crear un método para mostrar mensajes en diferido

Utiliza `showDeferredMessage` para desencadenar el siguiente mensaje dentro de la aplicación. Cuando `showMessage` sea `true`, el oyente devolverá `DISPLAY_NOW`.

Paso
líneas-MainActivity.kt=29

#### 7\. Desencadena el método desde tu interfaz de usuario

Para mostrar el mensaje aplazado previamente, llama a `showDeferredMessage(true)` desde tu interfaz de usuario, como un botón o un toque.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} También tendrás que [habilitar los mensajes dentro de la aplicación para Swift]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=swift#swift_enabling-in-app-messages).

## Aplazamiento y restablecimiento de mensajes desencadenados para Swift

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

Paso
líneas-AppDelegate.swift=5

#### 1\. Pon en práctica la `BrazeInAppMessageUIDelegate`

En tu clase `AppDelegate`, implementa el método [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) para que puedas anular su método `inAppMessage` más adelante.

Paso
líneas-AppDelegate.swift=19

#### 2\. Habilitar la depuración (opcional)

Para facilitar la solución de problemas durante el desarrollo, considera la posibilidad de habilitar la depuración.

Paso
líneas-AppDelegate.swift=25-27

#### 3\. Configura tu interfaz de usuario Braze y delega

`BrazeInAppMessageUI()` muestra mensajes dentro de la aplicación de forma predeterminada. Asignando `self` como delegado, puedes interceptar y gestionar los mensajes antes de que se muestren. Asegúrate de guardar la instancia, ya que la necesitarás más adelante para restaurar los mensajes diferidos.

Paso
líneas-AppDelegate.swift=32-41

#### 4\. Anula `DisplayChoice` con lógica condicional

Anular [`inAppMessage(_:displayChoiceForMessage:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) para determinar cuándo debe mostrarse un mensaje. Devuelve `.now` para mostrarlo inmediatamente, o `.reenqueue` para aplazarlo para más tarde.

Paso
líneas-AppDelegate.swift=43-46

#### 5\. Crear un método para mostrar mensajes en diferido

Crea un método que llame a `showDeferredMessage(true)` para mostrar el siguiente mensaje diferido de la pila. Cuando se llama, `showMessage` se establece en `true`, haciendo que el delegado devuelva `.now`.

Paso
líneas-ContentView.swift=1-14

#### 5\. Desencadena el método desde tu interfaz de usuario

Para mostrar el mensaje aplazado previamente, llama a `showDeferredMessage(true)` desde tu interfaz de usuario, como un botón o un toque.

{% endscrolly %}
{% endsdktab %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} Sin embargo, no es necesaria ninguna configuración adicional.

## Aplazar y restaurar mensajes desencadenados para Web

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

Paso
líneas-index.js=2

#### 1\. Eliminar las llamadas a `automaticallyShowInAppMessages()`

Elimina las llamadas a [`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages) ya que anularán cualquier lógica personalizada que implementes más adelante.

Paso
líneas-index.js=6

#### 2\. Habilitar la depuración (opcional)

Para facilitar la solución de problemas durante el desarrollo, considera la posibilidad de habilitar la depuración.

Paso
líneas-index.js=9-16

#### 3\. Suscribirse al controlador de devolución de llamada de mensajes dentro de la aplicación

Registra una devolución de llamada con [`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage) para recibir un mensaje cada vez que se desencadene un mensaje dentro de la aplicación.

Paso
líneas-index.js=11-12

#### 4\. Aplaza la instancia `message` 

Para aplazar el mensaje, llama a [`deferInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#deferinappmessage). Braze serializará y guardará este mensaje para que puedas mostrarlo en una futura carga de página.

Paso
líneas-index.js=18-24

#### 5\. Recuperar un mensaje aplazado anteriormente

Para recuperar cualquier mensaje aplazado previamente, llama a [`getDeferredInAppMessage()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getdeferredinappmessage). 

Paso
líneas-index.js=21-23

#### 6\. Mostrar el mensaje en diferido

Tras recuperar un mensaje en diferido, muéstralo pasándolo a [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage).

Paso
líneas-index.js=13-15

#### 7\. Mostrar un mensaje inmediatamente

Para mostrar un mensaje en lugar de aplazarlo, llama a [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage) directamente en tu devolución de llamada a `subscribeToInAppMessage`.
{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}
