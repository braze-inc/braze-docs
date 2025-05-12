## Inscrevendo-se em mensagens no aplicativo

Você pode registrar objetos de jogo Unity para serem notificados sobre mensagens no app. Recomendamos configurar os ouvintes de objetos de jogo no editor de configuração do Braze. No editor de configuração, os ouvintes devem ser definidos separadamente para Android e iOS.

Se você precisar configurar o ouvinte do objeto do jogo em tempo de execução, use `AppboyBinding.ConfigureListener()` e especifique `BrazeUnityMessageType.IN_APP_MESSAGE`.

## Analisando mensagens

As mensagens `string` recebidas em seu retorno de chamada de objeto de jogo de mensagem no app podem ser analisadas em nossos objetos de modelo pré-fornecidos por conveniência.

Use `InAppMessageFactory.BuildInAppMessage()` para analisar sua mensagem no app. O objeto resultante será uma instância de [`IInAppMessage.cs`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessage.cs) ou [`IInAppMessageImmersive.cs`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessageImmersive.cs) dependendo de seu tipo.

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

## Registrando dados de mensagens

Os cliques e impressões devem ser registrados manualmente para mensagens no app não exibidas diretamente pelo Braze.

Use `LogClicked()` e `LogImpression()` em [`IInAppMessage`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessage.cs) para registrar os cliques e as impressões da sua mensagem.

Use `LogButtonClicked(int buttonID)` on [`IInAppMessageImmersive`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessageImmersive.cs) para registrar os cliques nos botões. Observe que os botões são representados como listas de instâncias[`InAppMessageButton`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/InAppMessageButton.cs) cada uma das quais contém um `ButtonID`.
