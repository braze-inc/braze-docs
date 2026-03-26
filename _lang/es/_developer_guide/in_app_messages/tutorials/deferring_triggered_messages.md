---
nav_title: Aplazamiento de mensajes desencadenados
article_title: "Tutorial: Aplazamiento y restauración de mensajes desencadenados"
description: ""
page_order: 1
layout: scrolly
---

# Tutorial: Aplazamiento y restauración de mensajes desencadenados

> Sigue el código de ejemplo de este tutorial para aplazar y restaurar mensajes desencadenados dentro de la aplicación utilizando el SDK de Braze.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} Sin embargo, no es necesario realizar ninguna configuración adicional.

## Aplazamiento y restauración de mensajes desencadenados para la Web

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

!!paso
líneas-=2index.js

#### 1\. Eliminar llamadas a `automaticallyShowInAppMessages()`

Elimina cualquier llamada a[`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages)  , ya que anularán cualquier lógica personalizada que implementes más adelante.

!!paso
líneas-=6index.js

#### 2\. Habilitar depuración (opcional)

Para facilitar la solución de problemas durante el desarrollo, considera la posibilidad de habilitar la depuración.

!!paso
líneas-=9-16index.js

#### 3\. Suscríbete al controlador de devolución de llamada de mensajes dentro de la aplicación.

Registra una devolución de llamada con[`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage)  para recibir un mensaje cada vez que se desencadene un mensaje dentro de la aplicación.

!!paso
líneas-=11-12index.js

#### 4\. Aplazar la`message`instancia

Para posponer el mensaje, llama [`deferInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#deferinappmessage)al . Braze serializará y guardará este mensaje para que puedas mostrarlo en una futura carga de la página.

!!paso
líneas-=18-24index.js

#### 5\. Recuperar un mensaje aplazado anteriormente

Para recuperar cualquier mensaje aplazado anteriormente, llama a [`getDeferredInAppMessage()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getdeferredinappmessage). 

!!paso
líneas-=21-23index.js

#### 6\. Mostrar el mensaje diferido

Después de recuperar un mensaje diferido, muéstralo pasándolo a [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage).

!!paso
líneas-=13-15index.js

#### 7\. Mostrar un mensaje inmediatamente

Para mostrar un mensaje en lugar de aplazarlo, llama[`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage)directamente a  en tu`subscribeToInAppMessage`devolución de llamada.
{% endscrolly %}
{% endsdktab %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} También tendrás que [habilitar los mensajes dentro de la aplicación para Android]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=android#android_enabling-in-app-messages).

## Aplazamiento y restauración de mensajes desencadenados para Android

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

!!paso
líneas-=13-16MainApplication.kt

#### 1\. Crear una instancia `Application`única

Utiliza un objeto complementario para exponer tu`Application`clase como un singleton, de modo que se pueda acceder a ella más adelante en tu código.

!!paso
líneas-=25MainApplication.kt

#### 2\. Habilitar depuración (opcional)

Para facilitar la solución de problemas durante el desarrollo, considera la posibilidad de habilitar la depuración.

!!paso
líneas-=34-36MainApplication.kt

#### 3\. Registra las devoluciones de llamada del ciclo de vida de la actividad

Registra el listener predeterminado de Braze para gestionar el ciclo de vida de los mensajes dentro de la aplicación.

!!paso
líneas-=39-49MainApplication.kt

#### 4\. Configurar un detector de mensajes dentro de la aplicación

Utiliza`BrazeInAppMessageManager`  para configurar un listener personalizado que intercepte los mensajes antes de que se muestren.

!!paso
líneas-=43MainApplication.kt,46

#### 5\. Crear lógica condicional

Utiliza la`showMessage`bandera para controlar la sincronización: devuelve`DISPLAY_NOW`  para mostrar el mensaje ahora o`DISPLAY_LATER`  para aplazarlo.

!!paso
líneas-=52-55MainApplication.kt

#### 6\. Crear un método para mostrar mensajes diferidos.

Utiliza`showDeferredMessage`  para desencadonar el siguiente mensaje dentro de la aplicación. Cuando`showMessage`  es `true`, el oyente devolverá `DISPLAY_NOW`.

!!paso
líneas-=29MainActivity.kt

#### 7\. Desencadena el método desde tu interfaz de usuario.

Para mostrar el mensaje previamente aplazado, llama a`showDeferredMessage(true)`  desde tu interfaz de usuario, por ejemplo, un botón o un toque.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} También tendrás que [habilitar los mensajes dentro de la aplicación para SWIFT]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=swift#swift_enabling-in-app-messages).

## Aplazamiento y restauración de mensajes desencadenados para SWIFT

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

!!paso
líneas-=5AppDelegate.swift

#### 1\. Implementar el `BrazeInAppMessageUIDelegate`

En tu`AppDelegate`clase, implementa el [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate)método para que puedas`inAppMessage` sobrescribirlo más adelante.

!!paso
líneas-=19AppDelegate.swift

#### 2\. Habilitar depuración (opcional)

Para facilitar la solución de problemas durante el desarrollo, considera la posibilidad de habilitar la depuración.

!!paso
líneas-=25-27AppDelegate.swift

#### 3\. Configura tu interfaz de usuario de Braze y delega

`BrazeInAppMessageUI()` muestra mensajes dentro de la aplicación de forma predeterminada. Al asignar`self`  como tu delegado, puedes interceptar y gestionar los mensajes antes de que se muestren. Asegúrate de guardar la instancia, ya que la necesitarás más adelante para restaurar los mensajes diferidos.

!!paso
líneas-=32-41AppDelegate.swift

#### 4\. Anular`DisplayChoice`con lógica condicional

Anular[`inAppMessage(_:displayChoiceForMessage:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb)para determinar cuándo se debe mostrar un mensaje. Devuelve`.now`  para mostrarlo inmediatamente o`.reenqueue`  para posponerlo para más tarde.

!!paso
líneas-=43-46AppDelegate.swift

#### 5\. Crear un método para mostrar mensajes diferidos.

Crea un método que llame a`showDeferredMessage(true)`  para mostrar el siguiente mensaje diferido de la pila. Cuando se llama, la configuración`showMessage` es ,`true` lo que hace que el delegado devuelva `.now`.

!!paso
líneas-=1-14ContentView.swift

#### 5\. Desencadena el método desde tu interfaz de usuario.

Para mostrar el mensaje previamente aplazado, llama a`showDeferredMessage(true)`  desde tu interfaz de usuario, por ejemplo, un botón o un toque.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}
