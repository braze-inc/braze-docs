---
nav_title: Personalização do envio de mensagens
article_title: "Tutorial: Personalização do estilo usando pares de valores-chave"
description: ""
page_order: 1
layout: scrolly
---

# Tutorial: Personalização do estilo de mensagens usando pares de valores-chave

> Siga o exemplo de código deste tutorial para personalizar o estilo de suas mensagens no app com o uso de pares de valores-chave no SDK do Braze.

{% sdktabs %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} Você também precisará [ativar as mensagens no app para Android]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=android#android_enabling-in-app-messages).

## Personalização do estilo de mensagens usando pares de valores-chave para Android

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

!!! etapa
linhas-MainApplication.kt=19

#### 1\. Ativar a depuração (opcional)

Para facilitar a solução de problemas durante o desenvolvimento, considere a possibilidade de ativar a depuração.

!!! etapa
Linhas -MainApplication.kt=28-30

#### 2\. Registrar retornos de chamada do ciclo de vida da atividade

Registre o ouvinte padrão do Braze para lidar com o ciclo de vida das mensagens no app.

!!! etapa
linhas-CustomInAppMessageViewFactory.kt=8

#### 3\. Crie sua classe de fábrica de exibição personalizada

Certifique-se de que sua classe esteja em conformidade com [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html) para que ela possa construir e retornar exibições de mensagens personalizadas.

!!! etapa
Linhas -CustomInAppMessageViewFactory.kt=15-20

#### 4\. Delegar à fábrica padrão do Braze

Delegue à fábrica padrão para manter o estilo incorporado do Braze antes de aplicar suas próprias alterações condicionais.

!!! etapa
Linhas -CustomInAppMessageViewFactory.kt=30-32,35-41

#### 5\. Acessar pares de valores-chave de `inAppMessage.extras`

Use `inAppMessage.extras` para acessar tipos de personalização, atributos de estilo ou quaisquer outros valores definidos no dashboard. Aplicar substituições de estilo antes de retornar a exibição.

!!! etapa
Linhas -MainApplication.kt=33-34

#### 6\. Implementar um `IInAppMessageViewFactory`

Implementar [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html) em sua classe personalizada para construir e renderizar exibições de mensagens no app.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} Você também precisará [ativar as mensagens no app para o Swift]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=swift#swift_enabling-in-app-messages).

## Personalização do estilo de mensagens usando pares de valores-chave para Swift

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

!!! etapa
linhas-AppDelegate.swift=5

#### 1\. Implementar `BrazeInAppMessageUIDelegate`

Em sua classe `AppDelegate`, implemente [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/delegate) para que você possa substituir seu método `inAppMessage` posteriormente.

!!! etapa
linhas-AppDelegate.swift=17

#### 2\. Ativar a depuração (opcional)

Para facilitar a solução de problemas durante o desenvolvimento, considere a possibilidade de ativar a depuração.

!!! etapa
Linhas -AppDelegate.swift=30-50

#### 3\. Prepare as mensagens antes de serem exibidas

Braze chama `inAppMessage(_:prepareWith:)` durante a preparação da mensagem. Use-o para personalizar o estilo ou aplicar lógica com base em pares de valores-chave.

!!! etapa
linhas-AppDelegate.swift=34

#### 4\. Acessar pares de valores-chave de `message.extras`

Use `message.extras` para acessar tipos de personalização, atributos de estilo ou quaisquer outros valores definidos no dashboard.

!!! etapa
Linhas -AppDelegate.swift=38-46

#### 5\. Atualizar as atribuições de estilo da mensagem

Use [`inAppMessage(_:prepareWith:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) para acessar o site `PresentationContext` e poder modificar diretamente as atribuições de estilo. Cada tipo de mensagem no app expõe diferentes atribuições.

{% endscrolly %}
{% endsdktab %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} Entretanto, não é necessária nenhuma configuração adicional.

## Personalização de mensagens pela internet usando pares de valores-chave

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

!!! etapa
linhas-index.js=2

#### 1\. Remover chamadas para `automaticallyShowInAppMessages()`

Remova todas as chamadas para [`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages) pois elas substituirão qualquer lógica personalizada que você implementar posteriormente.

!!! etapa
linhas-index.js=6

#### 2\. Ativar a depuração (opcional)

Para facilitar a solução de problemas durante o desenvolvimento, considere a possibilidade de ativar a depuração.

!!! etapa
linhas-index.js=9-21

#### 3\. Assinar o manipulador de retorno de chamada de mensagem no app

Registre um retorno de chamada com [`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage) para receber uma mensagem sempre que uma mensagem no app for disparada.

!!! etapa
linhas-index.js=10-13

#### 4\. Acesse a propriedade `message.extras` 

Use `message.extras` para acessar tipos de personalização, atributos de estilo ou quaisquer outros valores definidos no dashboard. Todos os valores são retornados como strings.

!!! etapa
linhas-index.js=19

#### 5\. Chamar condicionalmente `showInAppMessage`

Para exibir a mensagem, ligue para [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage). Caso contrário, use as propriedades personalizadas conforme necessário.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}
