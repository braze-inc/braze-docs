---
nav_title: Adiar mensagens acionadas
article_title: "Tutorial: Adiar e restaurar mensagens acionadas"
description: ""
page_order: 1
layout: scrolly
---

# Tutorial: Adiar e restaurar mensagens acionadas

> Siga o código de exemplo neste tutorial para adiar e restaurar mensagens no app acionadas usando o SDK do Braze.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} No entanto, nenhuma configuração adicional é necessária.

## Adiar e restaurar mensagens acionadas para Web

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

!!etapa
linhas-index.js=2

#### 1\. Remover chamadas para `automaticallyShowInAppMessages()`

Remova qualquer chamada para [`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages), pois elas substituirão qualquer lógica personalizada que você implemente mais tarde.

!!etapa
linhas-index.js=6

#### 2\. Ativar depuração (opcional)

Para facilitar a solução de problemas durante o desenvolvimento, considere ativar a depuração.

!!etapa
linhas-index.js=9-16

#### 3\. Inscreva-se no manipulador de retorno de chamada da mensagem no app

Registre um retorno de chamada com [`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage) para receber uma mensagem sempre que uma mensagem no app for acionada.

!!etapa
linhas-index.js=11-12

#### 4\. Adiar a instância `message`

Para adiar a mensagem, chame [`deferInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#deferinappmessage). O Braze irá serializar e salvar esta mensagem para que você possa exibi-la em um carregamento de página futuro.

!!etapa
linhas-index.js=18-24

#### 5\. Recuperar uma mensagem previamente adiada

Para recuperar qualquer mensagem previamente adiada, chame [`getDeferredInAppMessage()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getdeferredinappmessage). 

!!etapa
linhas-index.js=21-23

#### 6\. Exibir a mensagem adiada

Após recuperar uma mensagem adiada, exiba-a passando-a para [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage).

!!etapa
linhas-index.js=13-15

#### 7\. Exibir uma mensagem imediatamente

Para mostrar uma mensagem em vez de adiá-la, chame [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage) diretamente no seu `subscribeToInAppMessage` retorno de chamada.
{% endscrolly %}
{% endsdktab %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} Você também precisará [ativar mensagens no app para Android]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=android#android_enabling-in-app-messages).

## Adiar e restaurar mensagens acionadas para Android

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

!!etapa
linhas-MainApplication.kt=13-16

#### 1\. Criar uma instância `Application` singleton

Use um objeto acompanhante para expor sua classe `Application` como um singleton para que possa ser acessada mais tarde no seu código.

!!etapa
linhas-MainApplication.kt=25

#### 2\. Ativar depuração (opcional)

Para facilitar a solução de problemas durante o desenvolvimento, considere ativar a depuração.

!!etapa
linhas-MainApplication.kt=34-36

#### 3\. Registrar retornos de chamada do ciclo de vida da atividade

Registrar o ouvinte padrão da Braze para gerenciar o ciclo de vida da mensagem no app.

!!etapa
linhas-MainApplication.kt=39-49

#### 4\. Configurar um ouvinte de mensagem no app

Use `BrazeInAppMessageManager` para definir um ouvinte personalizado que intercepta mensagens antes de serem exibidas.

!!etapa
linhas-MainApplication.kt=43,46

#### 5\. Crie lógica condicional

Use a flag `showMessage` para controlar o tempo—retorne `DISPLAY_NOW` para exibir a mensagem agora ou `DISPLAY_LATER` para adiá-la.

!!etapa
linhas-MainApplication.kt=52-55

#### 6\. Crie um método para exibir mensagens adiadas

Use `showDeferredMessage` para disparar a próxima mensagem no app. Quando `showMessage` estiver `true`, o ouvinte retornará `DISPLAY_NOW`.

!!etapa
linhas-MainActivity.kt=29

#### 7\. Dispare o método a partir da sua interface de usuário

Para exibir a mensagem que foi adiada anteriormente, chame `showDeferredMessage(true)` a partir da sua interface de usuário, como um botão ou toque.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} Você também precisará [ativar mensagens no app para Swift]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=swift#swift_enabling-in-app-messages).

## Adiar e restaurar mensagens disparadas para Swift

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

!!etapa
linhas-AppDelegate.swift=5

#### 1\. Implemente o `BrazeInAppMessageUIDelegate`

Na sua classe `AppDelegate`, implemente o [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) para que você possa sobrescrever seu método `inAppMessage` mais tarde.

!!etapa
linhas-AppDelegate.swift=19

#### 2\. Ativar depuração (opcional)

Para facilitar a solução de problemas durante o desenvolvimento, considere ativar a depuração.

!!etapa
linhas-AppDelegate.swift=25-27

#### 3\. Configure sua interface Braze e delegado

`BrazeInAppMessageUI()` renderiza mensagens no app por padrão. Ao atribuir `self` como seu delegado, você pode interceptar e lidar com mensagens antes que sejam exibidas. Certifique-se de salvar a instância, pois você precisará dela mais tarde para restaurar mensagens adiadas.

!!etapa
linhas-AppDelegate.swift=32-41

#### 4\. Substitua `DisplayChoice` por lógica condicional

Substitua [`inAppMessage(_:displayChoiceForMessage:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) para determinar quando uma mensagem deve ser exibida. Retorne `.now` para mostrá-la imediatamente, ou `.reenqueue` para adiá-la para depois.

!!etapa
linhas-AppDelegate.swift=43-46

#### 5\. Crie um método para mostrar mensagens adiadas

Crie um método que chama `showDeferredMessage(true)` para exibir a próxima mensagem adiada na pilha. Quando chamado, `showMessage` é definido como `true`, fazendo com que o delegado retorne `.now`.

!!etapa
linhas-ContentView.swift=1-14

#### 5\. Dispare o método a partir da sua interface de usuário

Para exibir a mensagem que foi adiada anteriormente, chame `showDeferredMessage(true)` a partir da sua interface de usuário, como um botão ou toque.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}
