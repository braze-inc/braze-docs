---
nav_title: Mensagem no app
article_title: Envio de mensagens no app para Unity
channel: in-app messaging
platform: 
  - Unity
  - iOS
  - Android
page_order: 2
description: "Este artigo de referência aborda as diretrizes de configuração de envio de mensagens no app para a plataforma Unity."

---

# Integração de envio de mensagens no app

> Este artigo de referência aborda as diretrizes de configuração de envio de mensagens no app para a plataforma Unity.

## Configuração do comportamento padrão de mensagens no app

{% tabs %}
{% tab Android %}

No Android, as mensagens no app da Braze são automaticamente exibidas de forma nativa. Para desativar essa funcionalidade, desmarque a opção **Exibir automaticamente mensagens no app** no editor de configuração do Braze.

Como alternativa, você pode definir `com_braze_inapp_show_inapp_messages_automatically` como `false` em `braze.xml` do seu projeto Unity.

A operação inicial de exibição de mensagens no app pode ser definida na configuração do Braze por meio da "Operação de exibição inicial do gerenciador de mensagens no app".

{% endtab %}
{% tab iOS %}

No iOS, as mensagens no app da Braze são automaticamente exibidas de forma nativa. Para desativar essa funcionalidade, defina os ouvintes de objetos de jogo no editor de configuração do Braze e certifique-se de que **Braze Displays In-App Messages** não esteja selecionado.

A operação inicial de exibição de mensagens no app pode ser definida na configuração do Braze por meio da "Operação de exibição inicial do gerenciador de mensagens no app".

{% endtab %}
{% endtabs %}

## Envio de mensagens no app para configuração do comportamento de exibição

Opcionalmente, você pode alterar o comportamento de exibição das mensagens no app em tempo de execução por meio do seguinte:

```csharp
// Sets in-app messages to display immediately when triggered.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_NOW);

// Sets in-app messages to display at a later time and be saved in a stack.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER);

// Sets in-app messages to be discarded after being triggered.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISCARD);
```

## Exibição de mensagens no app sob demanda

Você pode exibir a próxima mensagem no app disponível no stack por meio do método `DisplayNextInAppMessage()`. As mensagens são adicionadas a essa pilha de mensagens salvas se `DISPLAY_LATER` ou `BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER` for escolhido como a ação de exibição de mensagens no app.

```csharp
Appboy.AppboyBinding.DisplayNextInAppMessage();
```

## Recebimento de dados de mensagens no app no Unity

Você pode registrar objetos de jogo Unity para serem notificados sobre mensagens no app. Recomendamos configurar os ouvintes de objetos de jogo no editor de configuração do Braze. No editor de configuração, os ouvintes devem ser definidos separadamente para Android e iOS.

Se você precisar configurar o ouvinte do objeto do jogo em tempo de execução, use `AppboyBinding.ConfigureListener()` e especifique `BrazeUnityMessageType.IN_APP_MESSAGE`.

## Análise de mensagens no app

As mensagens `string` recebidas em seu retorno de chamada de objeto de jogo de mensagem no app podem ser analisadas em nossos objetos de modelo pré-fornecidos por conveniência.

Use `InAppMessageFactory.BuildInAppMessage()` para analisar sua mensagem no app. O objeto resultante será uma instância de [`IInAppMessage.cs`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessage.cs) ou [`IInAppMessageImmersive.cs`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessageImmersive.cs) dependendo de seu tipo.

### Exemplo de retorno de chamada de mensagem no app

```csharp
// Automatically logs a button click, if present.
void InAppMessageReceivedCallback(string message) {
  IInAppMessage inApp = InAppMessageFactory.BuildInAppMessage(message);
  if (inApp is IInAppMessageImmersive) {
    IInAppMessageImmersive inAppImmersive = inApp as IInAppMessageImmersive;
    if (inAppImmersive.Buttons != null && inAppImmersive.Buttons.Count > 0) {
      inAppImmersive.LogButtonClicked(inAppImmersive.Buttons[0].ButtonID);
    }
  }
}
```

## Suporte a GIFs

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}

## Análise de dados

Os cliques e impressões devem ser registrados manualmente para mensagens no app não exibidas diretamente pelo Braze.

Use `LogClicked()` e `LogImpression()` em [`IInAppMessage`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessage.cs) para registrar os cliques e as impressões da sua mensagem.

Use `LogButtonClicked(int buttonID)` on [`IInAppMessageImmersive`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessageImmersive.cs) para registrar os cliques nos botões. Observe que os botões são representados como listas de instâncias[`InAppMessageButton`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/InAppMessageButton.cs) cada uma das quais contém um `ButtonID`.

## Ouvintes de ação personalizados

Se precisar de mais controle sobre como um usuário interage com as mensagens no app, use um `BrazeInAppMessageListener` e atribua-o a `Appboy.AppboyBinding.inAppMessageListener`. Para todos os delegados que você não quiser usar, basta deixá-los como `null`.

```csharp
BrazeInAppMessageListener listener = new BrazeInAppMessageListener() {
  BeforeInAppMessageDisplayed = BeforeInAppMessageDisplayed,
  OnInAppMessageButtonClicked = OnInAppMessageButtonClicked,
  OnInAppMessageClicked       = OnInAppMessageClicked,
  OnInAppMessageHTMLClicked   = OnInAppMessageHTMLClicked,
  OnInAppMessageDismissed     = OnInAppMessageDismissed,
};
Appboy.AppboyBinding.inAppMessageListener = listener;

public void BeforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
  // Executed before an in-app message is displayed.
}

public void OnInAppMessageButtonClicked(IInAppMessage inAppMessage, InAppMessageButton inAppMessageButton) {
  // Executed whenever an in-app message button is clicked.
}

public void OnInAppMessageClicked(IInAppMessage inAppMessage) {
  // Executed whenever an in-app message is clicked.
}

public void OnInAppMessageHTMLClicked(IInAppMessage inAppMessage, Uri uri) {
  // Executed whenever an HTML in-app message is clicked.
}

public void OnInAppMessageDismissed(IInAppMessage inAppMessage) {
  // Executed whenever an in-app message is dismissed without a click.
}
```

