---
nav_title: Exibição condicional de mensagens
article_title: "Tutorial: Exibição condicional de mensagens no app"
description: ""
page_order: 1
layout: scrolly
---

# Tutorial: Exibição condicional de mensagens no app

> Siga o código de exemplo neste tutorial para exibir condicionalmente mensagens no app usando o SDK do Braze.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} No entanto, não é necessária nenhuma configuração adicional.

## Exibição condicional de mensagens no app para a Web

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

!!!etapa
linhas-index.js=2

#### 1\. Remover chamadas para `automaticallyShowInAppMessages()`

Remova todas as chamadas para [`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages)pois elas substituirão qualquer lógica personalizada que você implementar posteriormente.

!!!etapa
linhas-index.js=6

#### 2\. Ativar a depuração (opcional)

Para facilitar a solução de problemas durante o desenvolvimento, considere a possibilidade de ativar a depuração.

!!!etapa
Linhas -index.js=9-18

#### 3\. Assine as atualizações de mensagens no app

Registre um retorno de chamada com [`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage) para receber um `message` sempre que uma mensagem no app for disparada.

!!!etapa
linhas-index.js=10-13

#### 4\. Criar lógica condicional

Crie uma lógica personalizada para controlar quando as mensagens são exibidas. Neste exemplo, a lógica verifica se o URL contém `"checkout"` ou se existe um elemento `#checkout` na página.

!!!etapa
linhas-index.js=16

#### 5\. Envio de mensagens com `showInAppMessage`

Para exibir a mensagem, ligue para [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage). Se for omitido, a mensagem será ignorada.

{% endscrolly %}
{% endsdktab %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} Você também precisará [ativar as mensagens no app para Android]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=android#android_enabling-in-app-messages).

## Exibição condicional de mensagens no app para Android

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

!!!etapa
linhas-MainApplication.kt=17

#### 1\. Ativar a depuração (opcional)

Para facilitar a solução de problemas durante o desenvolvimento, considere a possibilidade de ativar a depuração.

!!!etapa
Linhas -MainApplication.kt=26-28

#### 2\. Registrar retornos de chamada do ciclo de vida da atividade

Registre o ouvinte padrão do Braze para lidar com o ciclo de vida das mensagens no app.

!!!etapa
Linhas -MainApplication.kt=30-44

#### 3\. Configure um ouvinte de mensagens no app

Use `BrazeInAppMessageManager` para definir um ouvinte personalizado que intercepta as mensagens antes de serem exibidas.

!!!etapa
Linhas -MainApplication.kt=34-42

#### 4\. Criar lógica condicional

Use a lógica personalizada para controlar o tempo de exibição das mensagens. Neste exemplo, a lógica personalizada verifica se o extra `should_display_message` está definido como `"true"`.

!!!etapa
Linhas -MainApplication.kt=38,41

#### 5\. Retornar ou descartar a mensagem

Retorne um `InAppMessageOperation` com `DISPLAY_NOW` para exibir a mensagem ou com `DISCARD` para suprimi-la.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} Você também precisará [ativar as mensagens no app para o Swift]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=swift#swift_enabling-in-app-messages).

## Exibição condicional de mensagens no app para Swift

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

!!!etapa
linhas-AppDelegate.swift=5

#### 1\. Implementar o `BrazeInAppMessageUIDelegate`

Em sua classe AppDelegate, implemente o método [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/delegate) para que você possa substituir seu método `inAppMessage` posteriormente.

!!!etapa
linhas-AppDelegate.swift=12

#### 2\. Ativar a depuração (opcional)

Para facilitar a solução de problemas durante o desenvolvimento, considere a possibilidade de ativar a depuração.

!!!etapa
Linhas -AppDelegate.swift=19-21

#### 3\. Configure sua UI do Braze e delegue

`BrazeInAppMessageUI()` renderiza mensagens no app por padrão. Ao atribuir o endereço `self` como seu delegado, você pode interceptar e tratar as mensagens antes que elas sejam exibidas.

!!!etapa
Linhas -AppDelegate.swift=26-33

#### 4\. Substituir o site `DisplayChoice` pela lógica condicional

Substituir [`inAppMessage(_:displayChoiceForMessage:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) para decidir se uma mensagem deve ser mostrada. Retorne `.now` para exibir a mensagem ou `.discard` para suprimi-la.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}
