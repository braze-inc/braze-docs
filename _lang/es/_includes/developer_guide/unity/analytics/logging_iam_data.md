## Suscribirse a mensajes dentro de la aplicación

Puedes registrar objetos del juego Unity para recibir notificaciones de mensajes dentro de la aplicación. Recomendamos configurar los oyentes del objeto del juego desde el editor de configuración de Braze. En el editor de configuración, las escuchas deben establecerse por separado para Android e iOS.

Si necesitas configurar la escucha de tu objeto del juego en tiempo de ejecución, utiliza `AppboyBinding.ConfigureListener()` y especifica `BrazeUnityMessageType.IN_APP_MESSAGE`.

## Análisis sintáctico de mensajes

Los mensajes entrantes de `string` recibidos en la devolución de llamada de tu objeto del juego de mensajería dentro de la aplicación pueden analizarse en nuestros objetos modelo suministrados previamente para mayor comodidad.

Utiliza `InAppMessageFactory.BuildInAppMessage()` para analizar tu mensaje dentro de la aplicación. El objeto resultante será una instancia de [`IInAppMessage.cs`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessage.cs) o [`IInAppMessageImmersive.cs`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessageImmersive.cs) dependiendo de su tipo.

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

## Registro de datos de mensajes

Los clics y las impresiones deben registrarse manualmente para los mensajes dentro de la aplicación no mostrados directamente por Braze.

Utiliza `LogClicked()` y `LogImpression()` en [`IInAppMessage`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessage.cs) para registrar los clics y las impresiones de tu mensaje.

Utiliza `LogButtonClicked(int buttonID)` en [`IInAppMessageImmersive`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessageImmersive.cs) para registrar los clics en los botones. Ten en cuenta que los botones se representan como listas de instancias [`InAppMessageButton`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/InAppMessageButton.cs), cada una de las cuales contiene un `ButtonID`.
