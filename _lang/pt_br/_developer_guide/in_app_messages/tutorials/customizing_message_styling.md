---
nav_title: Personalizar o estilo da mensagem
article_title: "Tutorial: Personalizando o estilo usando pares chave-valor"
description: ""
page_order: 1
layout: scrolly
---

# Tutorial: Personalizando o estilo da mensagem usando pares chave-valor

> Siga o código de exemplo neste tutorial para personalizar o estilo da sua mensagem no app usando pares chave-valor no SDK do Braze.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} No entanto, nenhuma configuração adicional é necessária.

## Personalizando o estilo da mensagem usando pares chave-valor para Web

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

!!etapa
linhas-index.js=2

#### 1\. Remover chamadas para `automaticallyShowInAppMessages()`

Remova qualquer chamada para [`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages), pois elas substituirão qualquer lógica personalizada que você implemente depois.

!!etapa
linhas-index.js=6

#### 2\. Ativar depuração (opcional)

Para facilitar a solução de problemas durante o desenvolvimento, considere ativar a depuração.

!!etapa
linhas-index.js=9-21

#### 3\. Inscreva-se no manipulador de retorno de chamada da mensagem no app

Registre um retorno de chamada com [`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage) para receber uma mensagem sempre que uma mensagem no app for acionada.

!!etapa
linhas-index.js=10-13

#### 4\. Acesse a propriedade `message.extras`

Use `message.extras` para acessar tipos de personalização, atributos de estilo ou quaisquer outros valores definidos no dashboard. Todos os valores são retornados como strings.

!!etapa
linhas-index.js=19

#### 5\. Chame condicionalmente `showInAppMessage`

Para exibir a mensagem, chame [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage). Caso contrário, use quaisquer propriedades personalizadas conforme necessário.

{% endscrolly %}
{% endsdktab %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} Você também precisará [ativar mensagens no app para Android]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=android#android_enabling-in-app-messages).

## Personalizando o estilo da mensagem usando pares chave-valor para Android

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

!!etapa
linhas-MainApplication.kt=19

#### 1\. Ativar depuração (opcional)

Para facilitar a solução de problemas durante o desenvolvimento, considere ativar a depuração.

!!etapa
linhas-MainApplication.kt=28-30

#### 2\. Registrar retornos de chamada do ciclo de vida da atividade

Registre o listener padrão do Braze para gerenciar o ciclo de vida da mensagem no app.

!!etapa
linhas-CustomInAppMessageViewFactory.kt=8

#### 3\. Crie sua classe de fábrica de visualização personalizada

Certifique-se de que sua classe esteja em conformidade com [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html) para que possa construir e retornar visualizações de mensagens personalizadas.

!!etapa
linhas-CustomInAppMessageViewFactory.kt=15-20

#### 4\. Delegar à fábrica padrão do Braze

Delegue à fábrica padrão para manter o estilo embutido do Braze antes de aplicar suas próprias alterações condicionais.

!!etapa
linhas-CustomInAppMessageViewFactory.kt=30-32,35-41

#### 5\. Acesse pares chave-valor de `inAppMessage.extras`

Use `inAppMessage.extras` para acessar tipos de personalização, atributos de estilo ou quaisquer outros valores definidos no dashboard. Aplique substituições de estilo antes de retornar a visualização.

!!etapa
linhas-MainApplication.kt=33-34

#### 6\. Implemente um `IInAppMessageViewFactory` personalizado

Implemente [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html) em sua classe personalizada para construir e renderizar visualizações de mensagens no app.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} Você também precisará [ativar mensagens no app para SWIFT]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=swift#swift_enabling-in-app-messages).

## Personalizando o estilo da mensagem usando pares chave-valor para SWIFT

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

!!etapa
linhas-AppDelegate.swift=5

#### 1\. Implemente `BrazeInAppMessageUIDelegate`

Na sua `AppDelegate` classe, implemente [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/delegate) para que você possa substituir seu método `inAppMessage` mais tarde.

!!etapa
linhas-AppDelegate.swift=17

#### 2\. Ativar depuração (opcional)

Para facilitar a solução de problemas durante o desenvolvimento, considere ativar a depuração.

!!etapa
linhas-AppDelegate.swift=30-50

#### 3\. Prepare as mensagens antes que sejam exibidas

Braze chama `inAppMessage(_:prepareWith:)` durante a preparação da mensagem. Use isso para personalizar o estilo ou aplicar lógica com base em pares chave-valor.

!!etapa
linhas-AppDelegate.swift=34

#### 4\. Acesse pares chave-valor de `message.extras`

Use `message.extras` para acessar tipos de personalização, atributos de estilo ou quaisquer outros valores definidos no dashboard.

!!etapa
linhas-AppDelegate.swift=38-46

#### 5\. Atualize os atributos de estilo da mensagem

Use [`inAppMessage(_:prepareWith:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) para acessar o `PresentationContext` para que você possa modificar os atributos de estilo diretamente. Cada tipo de mensagem no app expõe atributos diferentes.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}
